#!/usr/bin/env python3
"""A11 negative/boundary test runner. Does not emit M16 conformance results.

Only reads the source repository. Applies RFC6901-style JSON pointer mutations in
memory and evaluates declared expectation classes; no source artifact is edited.
"""
import argparse,copy,json,pathlib,sys,collections
from jsonschema import Draft202012Validator
from rdflib import Graph,URIRef,Literal,RDF,Namespace

REPO=pathlib.Path(__file__).resolve().parents[5]
HERE=pathlib.Path(__file__).resolve().parent


def read_rel(rel):
    target=(REPO/rel).resolve()
    if not target.is_relative_to(REPO) or not target.is_file():
        raise ValueError('missing or unsafe repository path: '+str(rel))
    return json.loads(target.read_text(encoding='utf-8'))


def modify(data, operations):
    out=copy.deepcopy(data)
    for op in operations:
        path=op['path']
        if path=='':
            if op['op']!='replace':raise ValueError('root mutation supports only replace')
            out=copy.deepcopy(op['value']);continue
        if not path.startswith('/') or op['op'] not in ('replace','remove','add'):
            raise ValueError('invalid mutation operation')
        parts=[x.replace('~1','/').replace('~0','~') for x in path[1:].split('/')]
        ref=out
        for part in parts[:-1]:ref=ref[int(part)] if isinstance(ref,list) else ref[part]
        key=parts[-1]
        if isinstance(ref,list):
            idx=int(key)
            if op['op']=='remove':ref.pop(idx)
            elif op['op']=='add':ref.insert(idx,copy.deepcopy(op['value']))
            else:ref[idx]=copy.deepcopy(op['value'])
        else:
            if op['op']=='remove':del ref[key]
            else:ref[key]=copy.deepcopy(op['value'])
    return out


def a1_ids():
    a1=read_rel('static/specs/hdip-cla/0.1/a1/architecture-element-registry.json')
    return {e['id'] for e in a1['elements']}


def reference_errors(check,data,ids):
    errors=[]
    if check=='A1_UNIQUE_IDENTITIES':
        entries=[e['id'] for e in data['elements']]
        if len(entries)!=len(set(entries)):errors.append('DUPLICATE_ARCHITECTURE_ID')
    elif check=='A2_RELATIONSHIP_ENDPOINTS':
        external={e['id'] for e in data['externalReferences']}
        for r in data['relationships']:
            if r['source'].startswith('HIST::'):
                continue
            if r['source'] not in ids: errors.append('UNRESOLVED_A1_SOURCE:'+r['id'])
            scope=r['targetScope']
            if scope=='A1_ELEMENT' and r['target'] not in ids:errors.append('UNRESOLVED_A1_TARGET:'+r['id'])
            if scope=='EXTERNAL_REFERENCE' and r['target'] not in external:errors.append('UNRESOLVED_EXTERNAL_TARGET:'+r['id'])
    elif check=='A9_MANIFEST_REFERENCES':
        for key in ('m15FlowRefs','m12InteractionRefs','m13BoundaryRefs'):
            for ref in data.get(key,[]):
                if ref not in ids:errors.append('UNRESOLVED_MANIFEST_REFERENCE:'+ref)
        for key in ('m14ProfileRef','m14RealizationPatternRef'):
            if data.get(key) and data[key] not in ids:errors.append('UNRESOLVED_MANIFEST_REFERENCE:'+data[key])
    elif check=='ILLUSTRATIVE_CLAIM_GUARD':
        for k,v in [('normativeStatus','ILLUSTRATIVE_ONLY'),('assessmentStatus','NOT_ASSESSED'),('claimOutcome','INDETERMINATE')]:
            if data.get(k)!=v:errors.append('UNSUPPORTED_EXAMPLE_CLAIM:'+k)
    else:raise ValueError('unknown reference check: '+str(check))
    return errors


DECLARED_CONTRADICTIONS={
    'SHARED_REALIZATION_GRANTS_SEMANTIC_AUTHORITY',
    'DATA_INFORMATION_INTELLIGENCE_ARE_IDENTICAL',
    'DATA_PDEP_UNIVERSAL_FOR_ALL_FAMILIES',
    'REGISTRATION_ALONE_CONFERS_PRODUCTNESS',
    'PRODUCT_ACCESS_CONFERS_DECISION_AUTHORIZATION',
    'PROFILE_WAIVER_MAKES_PASS',
    'LATEST_VERSION_ALWAYS_GOVERNED_CURRENT',
    'HYBRID_CHECKS_AUTOMATICALLY_PROVE_SATISFACTION',
    'LATER_REASSESSMENT_OVERWRITES_HISTORICAL_STATE',
    'CEP_IS_SIXTH_PLANE',
    'REALIZATION_PATTERN_INHERITS_ADJACENT_CONFORMANCE'
}



def local_shacl_core_subset(shape_path, fixture_path):
    """Bounded evaluator ONLY for A6 sh:minCount/maxCount/datatype/nodeKind=IRI.
    Not a SHACL standards implementation or replacement for pySHACL.
    """
    SH=Namespace('http://www.w3.org/ns/shacl#')
    shapes=Graph();shapes.parse(str((REPO/shape_path).resolve()),format='turtle')
    data=Graph();data.parse(str((REPO/fixture_path).resolve()),format='turtle')
    issues=[]
    for snode in shapes.subjects(RDF.type,SH.NodeShape):
        for cl in shapes.objects(snode,SH.targetClass):
            for focus in data.subjects(RDF.type,cl):
                for prop in shapes.objects(snode,SH.property):
                    predicate=next(shapes.objects(prop,SH.path),None)
                    if predicate is None:continue
                    values=list(data.objects(focus,predicate))
                    lower=next(shapes.objects(prop,SH.minCount),None)
                    upper=next(shapes.objects(prop,SH.maxCount),None)
                    dtype=next(shapes.objects(prop,SH.datatype),None)
                    nkind=next(shapes.objects(prop,SH.nodeKind),None)
                    if lower is not None and len(values)<int(lower):issues.append('minCount:'+str(predicate))
                    if upper is not None and len(values)>int(upper):issues.append('maxCount:'+str(predicate))
                    for v in values:
                        if dtype is not None and (not isinstance(v,Literal) or v.datatype not in (dtype,None)):
                            issues.append('datatype:'+str(predicate))
                        if nkind==SH.IRI and not isinstance(v,URIRef):issues.append('nodeKind:'+str(predicate))
    return issues

def run_case(c,ids,modes):
    cat=c['category'];evidence=[]
    if cat=='SCHEMA_NEGATIVE':
        baseline=read_rel(c['sourceDocument'])
        schema=read_rel(c['schemaDocument'])
        Draft202012Validator.check_schema(schema)
        v=Draft202012Validator(schema)
        if list(v.iter_errors(baseline)):
            raise ValueError('original source does not validate against original schema: '+c['sourceDocument'])
        mutated=modify(baseline,c['mutations'])
        errs=list(v.iter_errors(mutated))
        evidence=[str(x.message)[:250] for x in errs[:3]]
        result='MACHINE_REJECTED' if errs else 'UNEXPECTED_SCHEMA_ACCEPTANCE'
    elif cat in ('REFERENCE_NEGATIVE','MANIFEST_GUARD'):
        mutated=modify(read_rel(c['sourceDocument']),c['mutations'])
        errors=reference_errors(c['check'],mutated,ids)
        evidence=errors[:3]
        result='MACHINE_REJECTED' if errors else 'UNEXPECTED_REFERENCE_ACCEPTANCE'
    elif cat=='SHACL_SUBSET_NEGATIVE':
        evidence=local_shacl_core_subset(c['shapesTurtle'],c['sourceTurtle'])
        result='MACHINE_REJECTED' if evidence else 'UNEXPECTED_SHACL_ACCEPTANCE'
    elif cat=='EXPLICIT_CONTRADICTION':
        assertn=c['assertion']
        if assertn.get('fixtureOnly') is True and assertn.get('declared') is True and assertn.get('code') in DECLARED_CONTRADICTIONS and assertn['code']==c['check']:
            result='FLAGGED_DECLARED_CONTRADICTION'
            evidence=['Explicit fixture assertion contradicts a named frozen architecture distinction; no real-world implementation finding']
        else: result='UNSUPPORTED_CONTRADICTION_FIXTURE'
    elif cat=='EVIDENCE_BOUNDARY':
        e=c['assertion'];inv=e['invariantId']; mode=modes.get(inv)
        if inv not in c['m16TraceRefs'] or mode not in ('HYBRID','ASSESSMENT'):
            raise ValueError('invalid judgement-boundary invariant: '+str(inv))
        if (e.get('materialHumanAssessmentPending') is True and e.get('acceptedEvidenceRef') is None and e.get('scopeRationaleAccepted') is False):
            result='INDETERMINATE_REVIEW_REQUIRED'
            evidence=['M16 '+mode+' judgement/evidence remains unresolved; machine metadata insufficient']
        else:result='UNSUPPORTED_EVIDENCE_FIXTURE'
    else:raise ValueError('unknown category '+cat)
    return {'caseId':c['caseId'],'category':cat,'expectedDisposition':c['expectedDisposition'],
        'actualDisposition':result,'expectationMatched':result==c['expectedDisposition'],
        'diagnostics':evidence,'m16InvariantResult':'NOT_EVALUATED',
        'overallConformance':'NOT_ESTABLISHED'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--suite',default=str(HERE/'negative-boundary-test-suite.json'));parser.add_argument('--output');args=parser.parse_args()
    suite=json.loads(pathlib.Path(args.suite).read_text())
    ids=a1_ids()
    inv=read_rel('static/specs/hdip-cla/0.1/a3/invariant-conformance-catalogue.json')
    modes={i['id']:i['assessmentMode'] for i in inv['invariants']}
    results=[];seen=set()
    for entry in suite['cases']:
        c=read_rel(entry['fixturePath'])
        if c['caseId']!=entry['caseId'] or c['caseId'] in seen:raise ValueError('fixture mismatch/duplicate')
        seen.add(c['caseId']);results.append(run_case(c,ids,modes))
    matched=sum(r['expectationMatched'] for r in results)
    report={'suiteId':suite['suiteId'],'caseCount':len(results),'matched':matched,'mismatched':len(results)-matched,
            'countsByCategory':dict(collections.Counter(r['category'] for r in results)),
            'countsByDisposition':dict(collections.Counter(r['actualDisposition'] for r in results)),
            'architectureConformance':'NOT_ESTABLISHED','m16InvariantResult':'NOT_EVALUATED','results':results}
    txt=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output:pathlib.Path(args.output).write_text(txt)
    else:sys.stdout.write(txt)
    return 0 if report['mismatched']==0 else 1

if __name__=='__main__':sys.exit(main())
