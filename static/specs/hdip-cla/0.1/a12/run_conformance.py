#!/usr/bin/env python3
"""A12 reproducible machine-evidence runner. Never grants M16 conformance."""
import argparse, collections, hashlib, importlib.util, json, pathlib, subprocess, sys
from datetime import datetime
from jsonschema import Draft202012Validator, FormatChecker
from rdflib import Graph
from rdflib.compare import isomorphic

ROOT=pathlib.Path(__file__).resolve().parents[5]
HERE=pathlib.Path(__file__).resolve().parent
BASE='static/specs/hdip-cla/0.1'
HASHES={}

def source(rel):
    p=(ROOT/rel).resolve()
    if not p.is_relative_to(ROOT) or not p.is_file(): raise ValueError('Missing/unsafe input: '+str(rel))
    HASHES[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    return p

def load(rel):return json.loads(source(rel).read_text(encoding='utf-8'))
def issue(kind,value):return {'code':kind,'detail':str(value)}

def inventories():
    a1=load(f'{BASE}/a1/architecture-element-registry.json')
    a2=load(f'{BASE}/a2/relationship-traceability-registry.json')
    a3=load(f'{BASE}/a3/invariant-conformance-catalogue.json')
    ids={e['id'] for e in a1['elements']}; ext={e['id'] for e in a2['externalReferences']}
    actual={'elements':len(a1['elements']),'relationships':len(a2['relationships']),
        'traceability':len(a2['traceabilityRecords']),'invariants':len(a3['invariants'])}
    errors=[]
    for k,n in {'elements':209,'relationships':911,'traceability':332,'invariants':48}.items():
        if actual[k]!=n:errors.append(issue('COUNT_DRIFT',f'{k} {actual[k]} != {n}'))
    if len(ids)!=actual['elements']:errors.append(issue('DUPLICATE_ID','A1'))
    modes=collections.Counter(i['assessmentMode'] for i in a3['invariants'])
    if modes!={'STRUCTURAL':7,'HYBRID':37,'ASSESSMENT':4}:errors.append(issue('M16_MODE_DRIFT',modes))
    if {i['id'] for i in a3['invariants']}!={f'M16-I{x:02d}' for x in range(1,49)}:errors.append(issue('M16_ID_DRIFT','I01-I48'))
    for i in a3['invariants']:
        if i['id'] not in ids:errors.append(issue('A1_INVARIANT_UNRESOLVED',i['id']))
    for r in a2['relationships']:
        if not r['source'].startswith('HIST::') and r['source'] not in ids:errors.append(issue('A2_SOURCE_UNRESOLVED',r['id']))
        if r['targetScope']=='A1_ELEMENT' and r['target'] not in ids:errors.append(issue('A2_TARGET_UNRESOLVED',r['id']))
        if r['targetScope']=='EXTERNAL_REFERENCE' and r['target'] not in ext:errors.append(issue('A2_EXTERNAL_UNRESOLVED',r['id']))
    return {'id':'A1_A2_A3_INTEGRITY','result':'PASS' if not errors else 'FAIL','counts':actual,'modes':dict(modes),'issues':errors}

def a7_schemas():
    pairs=[('a1-architecture-elements','a1/architecture-element-registry.json'),
        ('a2-relationship-traceability','a2/relationship-traceability-registry.json'),
        ('a3-invariant-conformance','a3/invariant-conformance-catalogue.json'),
        ('a5-canonical-iri-policy','a5/canonical-iri-policy.json'),
        ('a5-jsonld-context','a5/hdip-cla-context.jsonld'),
        ('a5-expanded-graph','a5/canonical-architecture-graph.jsonld')]
    tests=[]
    for schema_id,doc in pairs:
        schema=load(f'{BASE}/a7/{schema_id}.schema.json'); obj=load(f'{BASE}/{doc}')
        Draft202012Validator.check_schema(schema)
        errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(obj))
        tests.append({'schema':schema_id,'result':'PASS' if not errors else 'FAIL','errors':[x.message[:160] for x in errors[:3]]})
    return {'id':'A7_SCHEMA_REGRESSION','result':'PASS' if all(x['result']=='PASS' for x in tests) else 'FAIL','cases':tests}

def graphs():
    ttl=f'{BASE}/a5/canonical-architecture-graph.ttl'; jld=f'{BASE}/a5/canonical-architecture-graph.jsonld'
    shapes=f'{BASE}/a6/architecture-structural-shapes.ttl'; runner=f'{BASE}/a11/run_negative_boundary_tests.py'
    a=Graph();a.parse(str(source(ttl)),format='turtle')
    b=Graph();b.parse(str(source(jld)),format='json-ld')
    source(shapes)
    s=importlib.util.spec_from_file_location('a11_local_subset',source(runner))
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    defects=m.local_shacl_core_subset(shapes,ttl)
    same=isomorphic(a,b)
    passed=len(a)==len(b)==13727 and same and not defects
    return {'id':'A5_GRAPH_A6_LOCAL_SHACL_SUBSET','result':'PASS' if passed else 'FAIL',
        'turtleTriples':len(a),'jsonLdTriples':len(b),'rdfIsomorphic':same,'localShapeDefects':defects[:8],
        'independentSHACL':'NOT_RUN'}

def subprocess_report(rel):
    cmd=[sys.executable,str(source(rel))]
    process=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=150)
    try:result=json.loads(process.stdout)
    except ValueError as e:raise RuntimeError('Invalid predecessor JSON: '+rel+': '+process.stderr[:400]) from e
    return process.returncode,result

def positive():
    suite=load(f'{BASE}/a10/positive-test-suite.json')
    rc,result=subprocess_report(f'{BASE}/a10/run_positive_tests.py')
    expected={c['testId']:c for c in suite['cases']}; observed={r['testId']:r for r in result['results']}
    defects=[]
    if len(expected)!=len(observed)!=16 or set(expected)!=set(observed):defects.append('A10 IDs/counts mismatch')
    if len(expected)!=16 or len(observed)!=16: defects.append('Expected exactly 16 A10 tests')
    for cid,c in expected.items():
        r=observed.get(cid,{})
        if r.get('machineResult')!='PASS_STRUCTURAL_ONLY' or r.get('architectureConformance')!='NOT_ESTABLISHED' or r.get('errors'):
            defects.append('Positive boundary mismatch '+cid)
        if c['expected']['architectureConformance']!='NOT_ESTABLISHED':defects.append('Suite claims architecture conformance '+cid)
        if c['type']=='SCENARIO_DECLARATION_SET':
            source(c['manifestPath'])
            for d in c['declarations']:source(d['path']);source(d['schemaPath'])
    source(f'{BASE}/a9/example-corpus.json')
    if rc or result.get('failed'):defects.append('A10 predecessor returned failure')
    return {'id':'A10_POSITIVE_TESTS','result':'PASS' if not defects else 'FAIL','cases':len(observed),
            'passed':result.get('passed'),'issues':defects,'results':result['results']}

def negative():
    suite=load(f'{BASE}/a11/negative-boundary-test-suite.json')
    rc,result=subprocess_report(f'{BASE}/a11/run_negative_boundary_tests.py')
    expected={c['caseId']:c['expectedDisposition'] for c in suite['cases']}
    observed={r['caseId']:r for r in result['results']}
    defects=[]
    if len(expected)!=54 or len(observed)!=54 or set(expected)!=set(observed):defects.append('A11 IDs/count mismatch')
    for cid,r in observed.items():
        if r['actualDisposition']!=expected.get(cid) or not r['expectationMatched']:defects.append('A11 expectation mismatch '+cid)
        if r['m16InvariantResult']!='NOT_EVALUATED' or r['overallConformance']!='NOT_ESTABLISHED':
            defects.append('A11 erroneously assigned M16 outcome '+cid)
    dispositions=dict(collections.Counter(r['actualDisposition'] for r in observed.values()))
    if dispositions!={'MACHINE_REJECTED':33,'FLAGGED_DECLARED_CONTRADICTION':11,'INDETERMINATE_REVIEW_REQUIRED':10}:
        defects.append('A11 dispositions drift')
    for c in suite['cases']:
        fixture=load(c['fixturePath'])
        for key in ('sourceDocument','schemaDocument','sourceTurtle','shapesTurtle'):
            if key in fixture: source(fixture[key])
    if rc or result.get('mismatched'):defects.append('A11 predecessor returned failure')
    return {'id':'A11_NEGATIVE_BOUNDARY_TESTS','result':'PASS' if not defects else 'FAIL','cases':len(observed),
            'matched':result.get('matched'),'dispositions':dispositions,'issues':defects,'results':result['results']}

def triage(doc,catalogue):
    schema=load(f'{BASE}/a12/assessment-intake.schema.json')
    errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(doc))
    if errors:return {'status':'INVALID_INTAKE','errors':[e.message for e in errors[:12]],'verifiedOverall':'NOT_ESTABLISHED'}
    modes={x['id']:x['assessmentMode'] for x in catalogue['invariants']}
    valid={'APPLICABLE':{'SATISFIED','VIOLATED','INDETERMINATE'},'NOT_APPLICABLE':{'NOT_APPLICABLE'},
           'UNDETERMINED':{'INDETERMINATE'}}
    issues=[];seen=set();counts=collections.Counter()
    for a in doc['invariantAssessments']:
        iid=a['invariantId'];app=a['applicability'];result=a['result'];counts[result]+=1
        if iid in seen:issues.append(issue('DUPLICATE_INVARIANT',iid))
        seen.add(iid)
        if result not in valid[app]:issues.append(issue('APPLICABILITY_RESULT_CONFLICT',iid))
        if result=='NOT_APPLICABLE' and (not a.get('rationale') or not a.get('judgementRecord')):
            issues.append(issue('UNJUSTIFIED_NOT_APPLICABLE',iid))
        if result in ('SATISFIED','VIOLATED') and not a.get('evidenceRefs'):
            issues.append(issue('DETERMINATE_EVIDENCE_MISSING',iid))
        if result in ('SATISFIED','VIOLATED') and modes[iid] in ('HYBRID','ASSESSMENT') and not a.get('judgementRecord'):
            issues.append(issue('ACCOUNTABLE_JUDGEMENT_MISSING',iid))
        if result=='INDETERMINATE' and not a.get('rationale'):issues.append(issue('UNEXPLAINED_INDETERMINATE',iid))
    missing=sorted(set(modes)-seen)
    declared=doc.get('declaredOutcome')
    if declared=='CONFORMANT' and (missing or any(a['result'] not in ('SATISFIED','NOT_APPLICABLE') for a in doc['invariantAssessments'])):
        issues.append(issue('UNSUPPORTED_DECLARED_CONFORMANCE','Missing or unresolved invariant'))
    if declared=='INDETERMINATE' and any(a['result']=='VIOLATED' for a in doc['invariantAssessments']):
        issues.append(issue('CONFLICTING_DECLARED_OUTCOME','Explicit violated invariant'))
    if declared=='NONCONFORMANT' and not any(a['result']=='VIOLATED' for a in doc['invariantAssessments']):
        issues.append(issue('NONCONFORMANCE_NOT_SUBSTANTIATED','No submitted violated invariant'))
    if doc['claimType']!='CORE_ARCHITECTURE_CONFORMANCE' and not doc.get('profileRefs'):
        issues.append(issue('PROFILE_CONTEXT_MISSING','Non-core claim requires profile context'))
    events=doc.get('historyEvents',[])
    if len({x['eventId'] for x in events})!=len(events):issues.append(issue('DUPLICATE_HISTORY_EVENT',''))
    times=[datetime.fromisoformat(e['effectiveAt'].replace('Z','+00:00')) for e in events]
    if times!=sorted(times):issues.append(issue('NON_MONOTONIC_HISTORY',''))
    return {'status':'REVIEW_REQUIRED' if not issues else 'INPUT_INCONSISTENT_REVIEW_REQUIRED',
        'issues':issues,'submittedCount':len(seen),'missingCount':len(missing), 'missingInvariantIds':missing,
        'submittedResults':dict(counts),'declaredOutcomeUnverified':declared,
        'reviewBoundary':'ACCOUNTABLE_M16_REVIEW_REQUIRED','submittedJudgementAuthenticated':False,
        'priorHistoryExternallyVerified':False,'machineAssignedM16Results':0,'verifiedOverall':'NOT_ESTABLISHED'}

def run(assessment_path=None):
    policy=load(f'{BASE}/a12/runner-policy.json')
    catalogue=load(f'{BASE}/a3/invariant-conformance-catalogue.json')
    source(f'{BASE}/a12/run_conformance.py')
    source(f'{BASE}/a12/assessment-intake.schema.json')
    source('docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze.md')
    checks=[]
    for fn in (inventories,a7_schemas,graphs,positive,negative):
        try:checks.append(fn())
        except Exception as e:checks.append({'id':fn.__name__,'result':'ERROR','error':type(e).__name__+': '+str(e)[:800]})
    gate='ERROR' if any(x['result']=='ERROR' for x in checks) else 'FAIL' if any(x['result']=='FAIL' for x in checks) else 'PASS'
    assessment=None
    if assessment_path:
        content=pathlib.Path(assessment_path).read_bytes()
        try:assessment=triage(json.loads(content),catalogue)
        except Exception as e:assessment={'status':'INVALID_INTAKE','error':str(e),'verifiedOverall':'NOT_ESTABLISHED'}
        assessment['inputSha256']=hashlib.sha256(content).hexdigest()
    snapshot=hashlib.sha256(json.dumps(HASHES,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'reportId':'HDIP-CLA-0.1-A12-EXECUTION-REPORT','version':'0.1-A12',
        'authority':'M17_FROZEN_HUMAN_READABLE','machineGate':gate,'checks':checks,
        'sourceSnapshotSha256':snapshot,'sourceCount':len(HASHES),'sourceHashes':dict(sorted(HASHES.items())),
        'runFingerprint':hashlib.sha256((snapshot+policy['id']).encode()).hexdigest(),
        'assessmentIntake':assessment,'architectureConformance':'NOT_ESTABLISHED',
        'machineAssignedM16Results':0,'independentSHACLProcessorRun':False,'docusaurusBuildRun':False,
        'limitations':['Machine test PASS proves bounded formalization checks only.',
            'A11 synthetic contradictions do not prove real-world violations.',
            'Local A6 SHACL subset does not substitute for independent SHACL processing.',
            'External M16 assessor identities, evidence and past assessment digests are not authenticated.',
            'No automatically established M16 conformance outcome.']}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assessment',help='Optional M16 assessment intake (not certified)')
    parser.add_argument('--output',help='Evidence report path; default stdout')
    parser.add_argument('--strict-review',action='store_true',help='Exit code 3 if assessment review is outstanding')
    args=parser.parse_args()
    report=run(args.assessment)
    payload=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output:
        dest=pathlib.Path(args.output).resolve()
        if dest.is_relative_to(ROOT) and dest != (HERE/'a12-execution-report.json').resolve():
            parser.error('In-repository output is limited to A12 execution report; other outputs must be outside the repository')
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(payload,encoding='utf-8')
        print(f'{report["machineGate"]}; report: {dest}; architecture conformance NOT_ESTABLISHED')
    else:print(payload,end='')
    if report['machineGate']!='PASS':return 2
    if report['assessmentIntake'] is not None and report['assessmentIntake']['status'] in ('INVALID_INTAKE','INPUT_INCONSISTENT_REVIEW_REQUIRED'):return 4
    if args.strict_review and report['assessmentIntake'] is not None:return 3
    return 0
if __name__=='__main__':sys.exit(main())
