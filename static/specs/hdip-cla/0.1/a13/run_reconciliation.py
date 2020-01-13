#!/usr/bin/env python3
"""HDIP-CLA 0.1 A13: bounded, source-led cross-artifact reconciliation.

A machine PASS establishes parity of tested formalizations, NOT M16 conformance.
The frozen M17/M16 text is read, never updated. No machine remediation is applied.
"""
import argparse
import collections
import csv
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from urllib.parse import quote, unquote

from rdflib import Graph, Literal, URIRef
from rdflib.compare import isomorphic
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = pathlib.Path('static/specs/hdip-cla/0.1')
M17 = pathlib.Path('docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze.md')
M16 = pathlib.Path('docs/architecture/cla/hdip-cla-0.1-m16-architecture-invariants-conformance-model.md')
M04 = pathlib.Path('docs/architecture/cla/hdip-cla-0.1-m04-principles-design-invariants.md')
SOURCES = {}


def file(rel):
    rel = pathlib.Path(rel)
    p = (ROOT / rel).resolve()
    if not p.is_relative_to(ROOT) or not p.is_file():
        raise ValueError('Missing/unsafe source file: ' + str(rel))
    SOURCES[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return p


def read(rel): return file(rel).read_text(encoding='utf-8')
def load(rel): return json.loads(read(rel))
def path(stage, name): return BASE / stage / name

def section(doc, begin, end=None):
    start = doc.find(begin)
    if start < 0: raise ValueError('Source section not found: ' + begin)
    stop = doc.find(end, start + len(begin)) if end else len(doc)
    return doc[start:stop if stop >= 0 else len(doc)]


def checks(group, pairs):
    defects=[]; passed=[]
    for check_id,actual,expected,authority in pairs:
        if actual == expected: passed.append(check_id)
        else: defects.append({'id':check_id, 'classification':'FORMALIZATION_DEFECT', 'sourceAuthority':authority,
                              'expected':_short(expected),'observed':_short(actual)})
    return {'gate':group,'status':'PASS' if not defects else 'DEFECTS_FOUND',
            'assertions':len(pairs),'passed':len(passed),'findings':defects,
            'passedCheckIds':passed}


def _short(v):
    if isinstance(v,set): v=sorted(v)
    if isinstance(v,(list,dict)):
        if len(v)>25: return {'count':len(v),'sample':str(v)[:400]}
        return v
    return str(v)[:600] if len(str(v))>600 else v


def frozen_inventory(m17,a1):
    bykind=collections.defaultdict(set)
    for e in a1['elements']: bykind[e['kind']].add(e['id'])
    # IDs and counts checked against M17's own frozen inventory section, not handoff prose.
    s=section(m17,'# 4. Frozen HDIP-CLA 0.1 architecture inventory','# 5. Frozen logical structure')
    rows=re.findall(r'^\| \*\*(.+?)\*\* \| \*\*(\d+)\*\*',s, re.M)
    expected_labels={'Logical Planes':('PLANE',5),'Shared Foundation':('FOUNDATION',1),
      'Cross-Cutting Overlays':('OVERLAY',9),'Canonical logical ABBs':('ARCHITECTURE_BUILDING_BLOCK',22),
      'Core logical Registries':('LOGICAL_REGISTRY',5),'Data-profile Registry specialization':('REGISTRY_SPECIALIZATION',1),
      'Principal projection/compilation artifacts':('PROJECTION_COMPILATION_ARTIFACT',7),
      'Canonical inter-Plane interactions':('INTERACTION',21),'External/adjacent Boundary Families':('BOUNDARY_FAMILY',12),
      'Realization Pattern families':('REALIZATION_PATTERN',8),'Profile Pattern families':('PROFILE_PATTERN',6),
      'Reference Views':('REFERENCE_VIEW',10),'Representative End-to-End Flows':('REPRESENTATIVE_FLOW',10),
      'Core Architecture Invariants':('ARCHITECTURE_INVARIANT',48)}
    m17numbers=dict((label,int(n)) for label,n in rows)
    pair=[]
    for label,(kind,number) in expected_labels.items():
        pair.append(('M17_COUNT_'+kind, (m17numbers.get(label),len(bykind[kind])), (number,number),str(M17)))
    tokens=section(m17,'# 5. Frozen logical structure','# 7. Frozen Registry')
    patterns={'PLANE':r'HDIP-P[1-5](?![-\w])','FOUNDATION':r'HDIP-FND(?![-\w])',
         'OVERLAY':r'HDIP-X[1-9](?![-\w])','ARCHITECTURE_BUILDING_BLOCK':r'HDIP-(?:P[1-5]|X[1-9])-ABB-\d\d(?![-\w])'}
    for kind,pattern in patterns.items():
        expected=set(re.findall(pattern,tokens))
        pair.append(('M17_EXACT_IDS_'+kind,bykind[kind], expected,str(M17)))
    # M17 later sections enumerate Registry/Inter-Plane/Boundary/Pattern/View IDs, but
    # direct IDs for some families reside in their M08-M15 source docs, not in M17 tables.
    pair.extend([
        ('A1_UNIQUE_IDENTITIES',len(bykind['PLANE'] | bykind['OVERLAY']),14,str(M17)),
        ('A1_NO_SIXTH_PLANE','HDIP-FND' not in bykind['PLANE'],True,str(M17)),
        ('A1_NO_X2_X8_ABB',all(not id.startswith(('HDIP-X2-ABB','HDIP-X8-ABB')) for id in bykind['ARCHITECTURE_BUILDING_BLOCK']),True,str(M17)),
        ('A1_PDEP_AND_SSCF_STAGE_COUNTS',
            (sum(i.startswith('HDIP-CLA-PDEP-STAGE-') for i in bykind['LIFECYCLE_STAGE']),
             sum(i.startswith('HDIP-CLA-SSCF-STAGE-') for i in bykind['LIFECYCLE_STAGE'])), (11,8),str(M17)),
        ('A1_CEP_IS_PROJECTION',any(e['kind']=='EXPERIENCE_PROJECTION' and 'Consumer Experience Projection' in e['canonicalName'] for e in a1['elements']),True,str(M17)),
        ('A1_LIFECYCLE_IDS',len(bykind['LIFECYCLE']),2,str(M17))])
    return checks('FROZEN_M17_INVENTORY',pair)


def invariant_reconciliation(m16,a1,a2,a3):
    pairs=[]
    frozen={}
    for line in m16.splitlines():
        cols=[x.strip().replace('**','') for x in line.strip().split('|')]
        if len(cols)>5 and re.fullmatch(r'M16-I\d\d',cols[1]):frozen[cols[1]]=(cols[2],cols[3],cols[4])
    inv={x['id']:x for x in a3['invariants']}
    ids={e['id'] for e in a1['elements'] if e['kind']=='ARCHITECTURE_INVARIANT'}
    expected={f'M16-I{i:02d}' for i in range(1,49)}
    pairs.extend([('M16_FROZEN_TABLE_48',set(frozen),expected,str(M16)),
                  ('A3_INVARIANT_IDS',set(inv),expected,str(M16)),('A1_INVARIANT_IDS',ids,expected,str(M17))])
    for iid,(name,condition,mode) in frozen.items():
        meta=inv.get(iid,{})
        pairs.append(('M16_EXACT_TEXT_'+iid,(meta.get('name'),meta.get('canonicalCondition'),meta.get('assessmentMode')),(name,condition,mode),str(M16)))
    pairs.append(('M16_MODE_DISTRIBUTION',dict(collections.Counter(i['assessmentMode'] for i in a3['invariants'])),
                  {'STRUCTURAL':7,'HYBRID':37,'ASSESSMENT':4},str(M16)))
    preserved=[r for r in a2['relationships'] if r['type']=='PRESERVES_SOURCE_INVARIANT']
    ancestries=[t for t in a2['traceabilityRecords'] if t['traceType']=='INVARIANT_ANCESTRY']
    pairs.extend([('M04_PRESERVATION_RELATIONS',len(preserved),40,str(M16)),
                  ('M04_ANCESTRY_TRACE',len(ancestries),40,str(M16)),
                  ('M04_SOURCE_REFERENCES',set((r['source'],r['target']) for r in preserved),
                      {(f'M16-I{i:02d}',f'M04-I{i:02d}') for i in range(1,41)},str(M16))])
    trace_by_id={t['id']:t for t in a2['traceabilityRecords']}
    for idx in range(1,49):
        iid=f'M16-I{idx:02d}';obj=inv[iid]
        if idx<=40:
            t=trace_by_id.get(obj.get('a2AncestryTraceId'),{})
            pairs.append(('A3_A2_ANCESTRY_'+iid,(obj.get('sourceInvariantId'),t.get('subject'),t.get('target')),
                         (f'M04-I{idx:02d}',iid,f'M04-I{idx:02d}'),str(M16)))
        else: pairs.append(('NO_FAKE_M04_ANCESTRY_'+iid,obj.get('sourceInvariantId') in (None,''),True,str(M16)))
    # M16 positive vocab cannot be extended by machine diagnostics.
    pairs.extend([('M16_RESULT_VOCAB',{x['token'] for x in a3['invariantResults']},
        {'SATISFIED','VIOLATED','INDETERMINATE','NOT_APPLICABLE'},str(M16)),
        ('M16_OVERALL_VOCAB',{x['token'] for x in a3['overallOutcomes']},
        {'CONFORMANT','NONCONFORMANT','INDETERMINATE'},str(M16)),
        ('M16_NO_CONDITIONAL_PASS','CONDITIONALLY_CONFORMANT' not in json.dumps(a3['overallOutcomes']),True,str(M16)),
        ('M16_PROFILE_OPERATIONS',dict(collections.Counter(x['disposition'] for x in a3['profileOperations'])),
        {'PERMITTED':9,'PROHIBITED':14},str(M16))])
    return checks('M16_A1_A2_A3_CONFORMANCE_SEMANTICS',pairs)


def identity_scope(s, source):
    if s.startswith('HIST::'):return 'historical',s
    if source=='EXTERNAL_REFERENCE':return 'external',s
    if source in ('DERIVATION_REFERENCE','DERIVATION_IDENTIFIER'):return 'derivation',s
    return 'element',s


def canonical(s, scope, policy):
    return URIRef(policy['canonicalBase']+policy['identityScopes'][scope]+quote(s,safe='-._~'))


def graph_reconciliation(a1,a2,a3,policy):
    g=Graph();g.parse(str(file(path('a5','canonical-architecture-graph.ttl'))),format='turtle')
    N=lambda k:URIRef(policy['canonicalBase']+policy['identityScopes']['ontology']+k)
    triples=set(g);pairs=[]
    pairs.append(('A5_GRAPH_TRIPLES',len(g),13727,'A5 canonical RDF serialization'))
    for e in a1['elements']:
        u=canonical(e['id'],'element',policy)
        pairs.append(('A1_GRAPH_ID_'+e['id'],(u,N('identifier'),Literal(e['id'])) in triples,True,'A1 and A5'))
    for r in a2['relationships']:
        rec=canonical(r['id'],'relationRecord',policy)
        scope,src=identity_scope(r['source'],'A1_ELEMENT')
        dest_scope,tar=identity_scope(r['target'],r['targetScope'])
        sub=canonical(src,scope,policy); obj=canonical(tar,dest_scope,policy)
        pred=canonical(r['type'],'relationshipPredicate',policy)
        expectation={(rec,N('id'),Literal(r['id'])), (rec,N('source'),sub),
                     (rec,N('target'),obj), (rec,N('relationshipType'),pred),
                     (rec,N('targetScope'),Literal(r['targetScope'])), (rec,N('modality'),Literal(r['modality'])),
                     (rec,N('assertionClass'),Literal(r['assertionClass'])),(sub,pred,obj)}
        pairs.append(('A2_DIRECT_AND_REIFIED_'+r['id'], all(x in triples for x in expectation),True,'A2 and A5'))
    for t in a2['traceabilityRecords']:
        rec=canonical(t['id'],'traceRecord',policy)
        subject_scope,subject=identity_scope(t['subject'],'A1_ELEMENT')
        target_scope,target=identity_scope(t['target'],t['targetKind'])
        trip={(rec,N('id'),Literal(t['id'])),(rec,N('subject'),canonical(subject,subject_scope,policy)),
              (rec,N('target'),canonical(target,target_scope,policy)),(rec,N('traceType'),Literal(t['traceType']))}
        pairs.append(('A2_TRACE_GRAPH_'+t['id'],all(x in triples for x in trip),True,'A2 and A5'))
    for i in a3['invariants']:
        u=canonical(i['id'],'element',policy)
        trip={(u,N('canonicalCondition'),Literal(i['canonicalCondition'])),
              (u,N('assessmentMode'),Literal(i['assessmentMode']))}
        pairs.append(('A3_INVARIANT_GRAPH_'+i['id'],all(x in triples for x in trip),True,'A3 and A5'))
    return checks('A1_A2_A3_A5_GRAPH_EXACT_REPRESENTATION',pairs),g


def rdf_migration(policy,g5):
    g4=Graph();g4.parse(str(file(path('a4','architecture-graph.ttl'))),format='turtle')
    mapping={}
    for rec in csv.DictReader(read(path('a5','iri-migration-map.csv')).splitlines()):
        mapping[rec['a4ProvisionalBase']]=rec['a5CanonicalBase']
    pred=[]
    for key,value in mapping.items():
        pred.append(('IRI_BASE_'+key, bool(value.startswith(policy['canonicalBase'])),True,'A5 IRI policy'))
    def conv(term):
        if not isinstance(term,URIRef):return term
        v=str(term)
        for k,base in mapping.items():
            if v.startswith(k): return URIRef(base+v[len(k):])
        return term
    # Canonical graph includes A4 provisional graph metadata, carried as literal rather
    # than silently rewriting the historical A4 policy claim.
    translated=Graph()
    for s,p,o in g4:translated.add((conv(s),conv(p),conv(o)))
    pred.extend([('A4_A5_GRAPH_TRIPLE_COUNT',(len(g4),len(g5)),(13727,13727),'A4 and A5'),
                 ('A4_A5_BIJECTIVE_RDF',isomorphic(translated,g5),True,'A4 and A5')])
    gj=Graph();gj.parse(str(file(path('a5','canonical-architecture-graph.jsonld'))),format='json-ld')
    gn=Graph();gn.parse(str(file(path('a5','canonical-architecture-graph.nt'))),format='nt')
    pred.append(('A5_TTL_JSONLD_NTRIPLES_ISOMORPHIC',isomorphic(g5,gj) and isomorphic(g5,gn),True,'A5 RDF serializations'))
    pred.extend([('A5_CANONICAL_BASE',policy['canonicalBase'],'https://kivanura.org/specs/hdip-cla/0.1/id/','A5 policy'),
                 ('A5_SCOPES',len(policy['identityScopes']),9,'A5 policy'),
                 ('A5_NO_EQUIVALENCE',all('sameAs' not in str(p) for s,p,o in g5),True,'M17 authority')])
    return checks('A4_TO_A5_IRI_AND_RDF_EQUIVALENCE',pred)


def structural_contracts(a1,a2,a3,g5):
    pairs=[]
    docs=[('a1-architecture-elements','a1/architecture-element-registry.json'),
          ('a2-relationship-traceability','a2/relationship-traceability-registry.json'),
          ('a3-invariant-conformance','a3/invariant-conformance-catalogue.json'),
          ('a5-canonical-iri-policy','a5/canonical-iri-policy.json'),
          ('a5-jsonld-context','a5/hdip-cla-context.jsonld'),
          ('a5-expanded-graph','a5/canonical-architecture-graph.jsonld')]
    for typ,doc in docs:
        sch=load(path('a7',typ+'.schema.json')); Draft202012Validator.check_schema(sch)
        failures=list(Draft202012Validator(sch,format_checker=FormatChecker()).iter_errors(load(BASE/doc)))
        pairs.append(('A7_SCHEMA_'+typ,not failures,True,'A7 structural schemas'))
    examples=sorted((ROOT/BASE/'a8/examples').glob('*-positive.json'))
    pairs.append(('A8_POSITIVE_COUNT',len(examples),6,'A8 schemas'))
    for p in examples:
        kind=p.name.removesuffix('-positive.json')
        schema=load(path('a8',kind+'.schema.json'))
        errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(load(p.relative_to(ROOT))))
        pairs.append(('A8_FIXTURE_'+kind,not errors,True,'A8 schemas'))
    # A6 shape graph verifies syntactically and local subset remains bounded.
    shacl=Graph();shacl.parse(str(file(path('a6','architecture-structural-shapes.ttl'))),format='turtle')
    pairs.extend([('A6_SHAPES_NONEMPTY',len(shacl)>0,True,'A6'),
                  ('A6_NOT_INDEPENDENT_CERTIFICATION',load(path('a6','a6-validation.json')).get('independentSHACLProcessorRun') is not True,True,'A6 limitation')])
    # Exact graph fidelity checked separately; no inferential validity asserted.
    return checks('A6_A7_A8_SCHEMA_AND_SHAPE_COHERENCE',pairs)


def corpus_and_runner():
    corpus=load(path('a9','example-corpus.json'))
    records=corpus['examples']; pairs=[]
    pairs.append(('A9_EXAMPLES',len(records),11,'A9'))
    pairs.append(('A9_M15_REFERENCES',set(f for x in records for f in x['flowRefs']),
                 {f'M15-FLOW-{n:02d}' for n in range(1,11)},'M15/A9'))
    declarations=0
    for e in records:
        manifest=load(BASE/'a9'/e['path']);pairs.append(('A9_EXAMPLE_'+e['id'],manifest.get('assessmentStatus')=='NOT_ASSESSED' and manifest.get('claimOutcome')=='INDETERMINATE',True,'A9 assessment boundary'))
        count=len(manifest['declarations']);declarations+=count
        pairs.append(('A9_DECLARATION_COUNT_'+e['id'],count,e['declarationCount'],'A9 manifest'))
    pairs.append(('A9_DECLARATION_TOTAL',declarations,35,'A9'))
    suite10=load(path('a10','positive-test-suite.json'));suite11=load(path('a11','negative-boundary-test-suite.json'))
    pairs.append(('A10_CASES',len(suite10['cases']),16,'A10'))
    pairs.append(('A11_CASES',len(suite11['cases']),54,'A11'))
    pairs.append(('A10_BOUNDARY',all(c['expected']['architectureConformance']=='NOT_ESTABLISHED' for c in suite10['cases']),True,'M16/A10'))
    runner=file(path('a12','run_conformance.py'))
    process=subprocess.run([sys.executable,str(runner)],cwd=ROOT,text=True,capture_output=True,timeout=180)
    if process.returncode:
        pairs.append(('A12_CLI_RETURN',process.returncode,0,'A12 runner'))
    try:
        report=json.loads(process.stdout)
        pairs.extend([('A12_FIVE_GATES',[(c['id'],c['result']) for c in report['checks']],
                       [(id,'PASS') for id in ['A1_A2_A3_INTEGRITY','A7_SCHEMA_REGRESSION','A5_GRAPH_A6_LOCAL_SHACL_SUBSET','A10_POSITIVE_TESTS','A11_NEGATIVE_BOUNDARY_TESTS']],'A12'),
                      ('A12_CONFORMANCE_GUARD',(report['machineGate'],report['architectureConformance'],report['machineAssignedM16Results']),
                       ('PASS','NOT_ESTABLISHED',0),'A12/M16'),
                      ('A12_SOURCE_DIGEST_COUNT',len(report['sourceHashes'])>=100,True,'A12 provenance')])
    except (ValueError,KeyError) as e:
        pairs.append(('A12_OUTPUT_JSON',str(e),'valid JSON','A12'))
    return checks('A9_A10_A11_A12_CORPUS_AND_RUNNER',pairs)


def compatible_authority(a1,a2,a3,m17):
    pairs=[]
    mapping={m['historicalTerm']:m for m in a1['compatibilityMappings']}
    frozen=section(m17,'# 12. Compatibility and historical terminology ledger','# 13. Realization, Profile')
    for label in ['SSPD','Consumer Experience Plane','DPFI / Data Product Factory & Intelligence',
                  'COVP','Data Product Registry','Resolved Product Graph','Unified Governance Bundle (UGB)',
                  'Logical Execution Plan','Selected Blueprint']:
        pairs.append(('M17_ALIAS_DOCUMENTED_'+label,label in frozen,True,str(M17)))
    for x in a1['compatibilityMappings']:
        pairs.append(('A1_ALIAS_NOT_ELEMENT_'+x['historicalTerm'],not any(e['id']==x['historicalTerm'] for e in a1['elements']),True,'M17/A1'))
    pairs.extend([('A1_COMPAT_MAPPING_COUNT',len(mapping),9,'A1'),
       ('A2_EXTERNAL_NOT_A1',not set(x['id'] for x in a2['externalReferences']) & set(x['id'] for x in a1['elements']),True,'M17/A2'),
       ('A2_TYPES_NONTRANSITIVE',all(not t['transitive'] and not t['impliesAuthorityTransfer'] and not t['impliesEquivalence'] for t in a2['relationshipTypes']),True,'M17/A2'),
       ('A3_NO_CONFORMANCE_BY_TEST','CONDITIONALLY_CONFORMANT' not in {x['token'] for x in a3['overallOutcomes']},True,'M16')])
    return checks('M17_COMPATIBILITY_AUTHORITY_SEPARATION',pairs)


def run():
    m17=read(M17);m16=read(M16);file(M04)
    a1=load(path('a1','architecture-element-registry.json'))
    a2=load(path('a2','relationship-traceability-registry.json'))
    a3=load(path('a3','invariant-conformance-catalogue.json'))
    policy=load(path('a5','canonical-iri-policy.json'))
    gates=[]
    for name,fn in [
        ('FROZEN_M17_INVENTORY',lambda:frozen_inventory(m17,a1)),
        ('M16_A1_A2_A3_CONFORMANCE_SEMANTICS',lambda:invariant_reconciliation(m16,a1,a2,a3)),
        ('A1_A2_A3_A5_GRAPH_EXACT_REPRESENTATION',lambda:graph_reconciliation(a1,a2,a3,policy)[0]),
        ('A4_TO_A5_IRI_AND_RDF_EQUIVALENCE',lambda:rdf_migration(policy,_load_g5())),
        ('A6_A7_A8_SCHEMA_AND_SHAPE_COHERENCE',lambda:structural_contracts(a1,a2,a3,_load_g5())),
        ('A9_A10_A11_A12_CORPUS_AND_RUNNER',corpus_and_runner),
        ('M17_COMPATIBILITY_AUTHORITY_SEPARATION',lambda:compatible_authority(a1,a2,a3,m17))]:
        try:gates.append(fn())
        except Exception as exc:gates.append({'gate':name,'status':'ERROR','assertions':0,'passed':0,
            'findings':[{'id':'GATE_ERROR','classification':'EXECUTION_ERROR','detail':type(exc).__name__+': '+str(exc)[:400]}], 'passedCheckIds':[]})
    status='PASS_BOUNDED_RECONCILIATION' if all(x['status']=='PASS' for x in gates) else 'RECONCILIATION_DEFECTS_OR_ERRORS'
    sources=dict(sorted(SOURCES.items()))
    fingerprint=hashlib.sha256(json.dumps(sources,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'reportId':'HDIP-CLA-0.1-A13-RECONCILIATION-REPORT',
       'stage':'A13','authority':'M17_FROZEN_HUMAN_READABLE',
       'status':status,'machineScope':'FORMALIZATION_RECONCILIATION_ONLY',
       'architectureConformance':'NOT_ESTABLISHED','machineAssignedM16Results':0,
       'totalAssertions':sum(x['assertions'] for x in gates),
       'passedAssertions':sum(x['passed'] for x in gates),
       'defectCount':sum(len(x['findings']) for x in gates),
       'gates':gates,'sourceCount':len(sources),'sourceSnapshotSha256':fingerprint,
       'sourceHashes':sources,
       'limitations':[{'id':'LIM-SHACL','status':'NOT_INDEPENDENTLY_VERIFIED','meaning':'A6 SHACL uses bounded local evaluator, no independent SHACL processor test'},
                      {'id':'LIM-BUILD','status':'NOT_RUN','meaning':'No Docusaurus/npm build included in A13 reconciliation'},
                      {'id':'LIM-M16-ASSESSMENT','status':'OUTSIDE_MACHINE_BOUNDARY','meaning':'No accountable HYBRID/ASSESSMENT satisfaction or real implementation certification'},
                      {'id':'LIM-OWL','status':'NOT_INDEPENDENTLY_VERIFIED','meaning':'No full OWL reasoner/entailment profile certification'},
                      {'id':'LIM-EXTERNAL','status':'OUTSIDE_MACHINE_BOUNDARY','meaning':'No authoritative GEDRM/GEARM/GEAIRM/BPS/Product-family semantic attestation'}]}


def _load_g5():
    g=Graph();g.parse(str(file(path('a5','canonical-architecture-graph.ttl'))),format='turtle');return g


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',help='Report path, otherwise stdout')
    args=parser.parse_args()
    result=run();data=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if args.output:
        dest=pathlib.Path(args.output).resolve()
        if dest.is_relative_to(ROOT) and dest != (ROOT/path('a13','a13-reconciliation-report.json')).resolve():
            parser.error('Only A13 report is a permitted in-repository output')
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(data,encoding='utf-8')
        print(f'{result["status"]}; {result["passedAssertions"]}/{result["totalAssertions"]} assertions; report: {dest}')
    else:print(data,end='')
    return 0 if result['status']=='PASS_BOUNDED_RECONCILIATION' else 2

if __name__=='__main__':sys.exit(main())
