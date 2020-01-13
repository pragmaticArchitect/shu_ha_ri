#!/usr/bin/env python3
"""HDIP-CLA 0.1 A14: bounded, deterministic regression of frozen A13 predecessor.

No M16 invariant or overall implementation conformance result is assigned.
No predecessor artifact is written or auto-rebaselined by this runner.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
from collections import Counter

from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[5]
HERE = pathlib.Path(__file__).resolve().parent
BASE = pathlib.Path('static/specs/hdip-cla/0.1')
PROGRAMME = 'docs/architecture/executable/hdip-cla-0.1-executable-programme.md'
SIDEBAR = 'sidebars.ts'


def read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding='utf-8'))


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def checked(root, rel):
    if not isinstance(rel, str) or not rel or '\\' in rel or '\x00' in rel:
        raise ValueError('Invalid path')
    p = (root / rel).resolve()
    if not p.is_relative_to(root.resolve()) or not p.is_file():
        raise ValueError('Missing, non-file or unsafe source path: ' + rel)
    return p


def gate(name, errors, checked_count=0, details=None):
    return {'id': name, 'status': 'PASS' if not errors else 'FAIL',
            'checked': checked_count, 'findings': errors[:50], 'details': details or {}}


def predecessor_lock(root, manifest):
    findings=[]
    records=manifest.get('files', [])
    paths=[r.get('path') for r in records]
    if len(records)!=243 or len(set(paths))!=243:
        findings.append('Predecessor inventory must have 243 unique locked files')
    for rec in records:
        rel=rec['path']
        try:
            if rel in (PROGRAMME,SIDEBAR):
                findings.append('Mutable navigation file must not be in frozen lock: '+rel)
            actual=sha256(checked(root,rel).read_bytes())
            if actual!=rec['sha256']:
                findings.append('PREDECESSOR_DRIFT:'+rel+':expected='+rec['sha256']+':actual='+actual)
        except (ValueError,OSError,KeyError) as exc:
            findings.append('PREDECESSOR_MISSING_OR_INVALID:'+str(rel)+':'+str(exc))
    return gate('A13_PREDECESSOR_SHA256_LOCK',findings,len(records),
                {'baselineFileCount':245,'lockedFileCount':len(records),
                 'intentionalMutablePaths':[PROGRAMME,SIDEBAR],
                 'sourceZipSha256':manifest.get('sourceZipSha256')})


def cli(root, relative, args=None, timeout=180):
    script=checked(root,relative)
    command=[sys.executable,str(script)]+(args or [])
    proc=subprocess.run(command,cwd=root,capture_output=True,text=True,timeout=timeout,
                        env=None,check=False)
    return proc


def json_runner(root, script, name, validator):
    try:
        proc=cli(root,str(BASE/script))
        if proc.returncode:
            return gate(name,['Runner exited '+str(proc.returncode)+': '+proc.stderr[-400:]],0)
        try: doc=json.loads(proc.stdout)
        except json.JSONDecodeError:
            return gate(name,['Runner emitted invalid JSON: '+proc.stdout[:200]],0)
        errors,n,details=validator(doc)
        return gate(name,errors,n,details)
    except (OSError,ValueError,subprocess.TimeoutExpired) as e:
        return gate(name,['EXECUTION_ERROR:'+type(e).__name__+':'+str(e)[:220]],0)


def validate_a10(doc):
    issues=[];items=doc.get('results',[])
    if len(items)!=16 or doc.get('failed')!=0 or doc.get('passed')!=16:issues.append('A10 case total/count drift')
    ids=[r.get('testId') for r in items]
    if len(ids)!=len(set(ids)):issues.append('A10 duplicate testId')
    for r in items:
        if r.get('machineResult')!='PASS_STRUCTURAL_ONLY' or r.get('architectureConformance')!='NOT_ESTABLISHED' or r.get('errors'):
            issues.append('A10 invalid result boundary: '+str(r.get('testId')))
    return issues,len(items),{'cases':len(items),'machineResult':'PASS_STRUCTURAL_ONLY'}


def validate_a11(doc):
    issues=[];items=doc.get('results',[])
    if len(items)!=54 or doc.get('matched')!=54 or doc.get('mismatched')!=0: issues.append('A11 total/count mismatch')
    ids=[r.get('caseId') for r in items]
    if len(ids)!=len(set(ids)):issues.append('A11 duplicate caseId')
    d=Counter(r.get('actualDisposition') for r in items)
    expected={'MACHINE_REJECTED':33,'FLAGGED_DECLARED_CONTRADICTION':11,'INDETERMINATE_REVIEW_REQUIRED':10}
    if dict(d)!=expected:issues.append('A11 disposition distribution mismatch')
    for r in items:
        if not r.get('expectationMatched') or r.get('m16InvariantResult')!='NOT_EVALUATED' or r.get('overallConformance')!='NOT_ESTABLISHED':
            issues.append('A11 result/authority boundary invalid: '+str(r.get('caseId')))
    return issues,len(items),{'dispositions':dict(sorted(d.items()))}


def validate_a12(doc):
    expected=['A1_A2_A3_INTEGRITY','A7_SCHEMA_REGRESSION','A5_GRAPH_A6_LOCAL_SHACL_SUBSET','A10_POSITIVE_TESTS','A11_NEGATIVE_BOUNDARY_TESTS']
    issues=[];gates=doc.get('checks',[])
    if [g.get('id') for g in gates]!=expected or any(g.get('result')!='PASS' for g in gates):issues.append('A12 5-gate coverage/status drift')
    if doc.get('machineGate')!='PASS' or doc.get('architectureConformance')!='NOT_ESTABLISHED' or doc.get('machineAssignedM16Results')!=0:issues.append('A12 conformance overstatement')
    if doc.get('independentSHACLProcessorRun') is not False:issues.append('A12 unsubstantiated independent SHACL claim')
    counts=next((g.get('counts',{}) for g in gates if g.get('id')==expected[0]),{})
    if counts!={'elements':209,'relationships':911,'traceability':332,'invariants':48}:issues.append('A12 canonical count mismatch')
    positives=next((g for g in gates if g.get('id')==expected[3]),{})
    negatives=next((g for g in gates if g.get('id')==expected[4]),{})
    if positives.get('cases')!=16 or negatives.get('cases')!=54: issues.append('A12 integrated suite count drift')
    hashes=doc.get('sourceHashes',{})
    digest=sha256(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode())
    if digest!=doc.get('sourceSnapshotSha256'):issues.append('A12 source fingerprint mismatch')
    return issues,len(gates),{'sourceHashCount':len(hashes),'snapshotSha256':digest}


def validate_a13(doc):
    expected=['FROZEN_M17_INVENTORY','M16_A1_A2_A3_CONFORMANCE_SEMANTICS','A1_A2_A3_A5_GRAPH_EXACT_REPRESENTATION',
        'A4_TO_A5_IRI_AND_RDF_EQUIVALENCE','A6_A7_A8_SCHEMA_AND_SHAPE_COHERENCE',
        'A9_A10_A11_A12_CORPUS_AND_RUNNER','M17_COMPATIBILITY_AUTHORITY_SEPARATION']
    issues=[];gs=doc.get('gates',[])
    if [g.get('gate') for g in gs]!=expected or any(g.get('status')!='PASS' for g in gs):issues.append('A13 7-gate coverage/status drift')
    total=sum(g.get('assertions',0) for g in gs); passed=sum(g.get('passed',0) for g in gs)
    if total!=1715 or passed!=1715 or doc.get('totalAssertions')!=1715 or doc.get('passedAssertions')!=1715 or doc.get('defectCount')!=0:issues.append('A13 assertion count/defect drift')
    if doc.get('status')!='PASS_BOUNDED_RECONCILIATION' or doc.get('architectureConformance')!='NOT_ESTABLISHED' or doc.get('machineAssignedM16Results')!=0: issues.append('A13 assertion/conformance overstatement')
    lim={x.get('id') for x in doc.get('limitations',[])}
    if lim!={'LIM-SHACL','LIM-BUILD','LIM-M16-ASSESSMENT','LIM-OWL','LIM-EXTERNAL'}:issues.append('A13 limitations silently changed')
    hashes=doc.get('sourceHashes',{})
    if sha256(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode())!=doc.get('sourceSnapshotSha256'):issues.append('A13 source snapshot invalid')
    return issues,total,{'gates':len(gs),'assertions':total,'sourceHashCount':len(hashes)}


def guards(root,stage,expected_count):
    name=f'{stage.upper()}_MUTATION_GUARDS'
    script=BASE/stage/({'a12':'test_runner.py','a13':'test_reconciliation.py','a14':'test_regression.py'}[stage])
    try:
        proc=cli(root,str(script),timeout=180)
        output=proc.stderr+'\n'+proc.stdout
        import re
        matches=re.findall(r'Ran (\d+) tests?',output)
        number=int(matches[-1]) if matches else 0
        errors=[]
        if proc.returncode!=0: errors.append('Guard suite returned nonzero '+str(proc.returncode)+': '+output[-600:])
        if number!=expected_count:errors.append('Guard test count '+str(number)+' != '+str(expected_count))
        if 'FAILED' in output or 'OK' not in output:errors.append('Guard test suite did not report OK')
        return gate(name,errors,number,{'expectedCount':expected_count})
    except (OSError,ValueError,subprocess.TimeoutExpired) as e:
        return gate(name,['EXECUTION_ERROR:'+str(e)[:300]],0)


def schema_fixtures(root):
    cases=[]; issues=[]
    folder=BASE/'a8';schemas=sorted((root/folder).glob('*.schema.json'))
    for f in schemas:
        name=f.name.removesuffix('.schema.json')
        schema=read_json(f); Draft202012Validator.check_schema(schema)
        v=Draft202012Validator(schema,format_checker=FormatChecker())
        for status in ('positive','negative'):
            relative=str(folder/'examples'/(name+'-'+status+'.json'))
            document=read_json(checked(root,relative))
            has_errors=bool(list(v.iter_errors(document)))
            passed=has_errors==(status=='negative')
            if not passed:issues.append('A8 fixture mismatch: '+relative)
            cases.append({'schema':name,'fixture':status,'expected':'REJECT' if status=='negative' else 'ACCEPT','matched':passed})
    if len(cases)!=12:issues.append('Expected 12 A8 fixture validations; found '+str(len(cases)))
    return gate('A8_POSITIVE_NEGATIVE_SCHEMA_FIXTURES',issues,len(cases),{'caseResults':cases})


def conformance_guard(gates):
    return gate('M16_NO_AUTOMATED_CONFORMANCE_PROMOTION',
        ['A14 machine checks cannot establish M16 implementation conformance'] if any(g['status']!='PASS' for g in gates) else [],
        len(gates),{'machineOutcomeOnly':'PASS_BOUNDED_REGRESSION','implementationConformance':'NOT_ESTABLISHED',
                    'assignedInvariantResults':0})


def run(root=ROOT,manifest=None,stop_after=None):
    root=pathlib.Path(root).resolve()
    manifest=manifest or read_json(checked(root,str(BASE/'a14/a13-predecessor-lock.json')))
    gates=[predecessor_lock(root,manifest)]
    tasks=[
        ('A10_POSITIVE_SUITE',lambda:json_runner(root,'a10/run_positive_tests.py','A10_POSITIVE_SUITE',validate_a10)),
        ('A11_NEGATIVE_BOUNDARY_SUITE',lambda:json_runner(root,'a11/run_negative_boundary_tests.py','A11_NEGATIVE_BOUNDARY_SUITE',validate_a11)),
        ('A12_INTEGRATED_MACHINE_EVIDENCE',lambda:json_runner(root,'a12/run_conformance.py','A12_INTEGRATED_MACHINE_EVIDENCE',validate_a12)),
        ('A13_FROZEN_SOURCE_RECONCILIATION',lambda:json_runner(root,'a13/run_reconciliation.py','A13_FROZEN_SOURCE_RECONCILIATION',validate_a13)),
        ('A8_SCHEMA_FIXTURE_REGRESSION',lambda:schema_fixtures(root)),
        ('A12_GUARD_TESTS',lambda:guards(root,'a12',12)),
        ('A13_MUTATION_TESTS',lambda:guards(root,'a13',10)),
        ('A14_COUNTERFACTUAL_GUARDS',lambda:guards(root,'a14',16)),
    ]
    for name,fn in tasks:
        if stop_after and len(gates)>=stop_after:break
        try:gates.append(fn())
        except Exception as e:gates.append(gate(name,['EXECUTION_ERROR:'+type(e).__name__+':'+str(e)[:400]]))
    # The claim guard is always emitted, independent of failures, and does not certify.
    guard=conformance_guard(gates);gates.append(guard)
    passed=sum(g['status']=='PASS' for g in gates)
    result='PASS_BOUNDED_REGRESSION' if passed==len(gates) and not stop_after else 'REGRESSION_FAILURE_OR_INCOMPLETE'
    files=manifest.get('files',[])
    manifest_hash=sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode())
    return {'reportId':'HDIP-CLA-0.1-A14-REGRESSION-REPORT','stage':'A14','authority':'M17_FROZEN_HUMAN_READABLE',
            'machineScope':'BOUNDED_REGRESSION_ONLY','status':result,
            'architectureConformance':'NOT_ESTABLISHED','machineAssignedM16Results':0,
            'passedGates':passed,'totalGates':len(gates),'gates':gates,
            'a13PredecessorLockedFiles':len(files),'baselineLockDigest':manifest_hash,
            'limitations':[{'id':'LIM-SHACL','status':'NOT_INDEPENDENTLY_VERIFIED'},
                           {'id':'LIM-OWL','status':'NOT_INDEPENDENTLY_VERIFIED'},
                           {'id':'LIM-BUILD','status':'NOT_RUN'},
                           {'id':'LIM-M16-ASSESSMENT','status':'OUTSIDE_MACHINE_BOUNDARY'},
                           {'id':'LIM-EXTERNAL','status':'OUTSIDE_MACHINE_BOUNDARY'}],
            'noAutomaticRebaseline':True,'noSourceMutation':True,
            'note':'PASS indicates tested structural/regression conditions only; no M16 CONFORMANT result.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',help='Write report to given path (no source files may be overwritten)')
    args=p.parse_args()
    report=run()
    payload=json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    if args.output:
        dest=pathlib.Path(args.output).resolve()
        protected=(BASE/'a14/a13-predecessor-lock.json')
        if dest.is_relative_to(ROOT) and dest!=(ROOT/BASE/'a14/a14-regression-report.json').resolve():
            p.error('In-repository output limited to A14 report')
        if dest==(ROOT/protected).resolve():p.error('Cannot overwrite locked baseline')
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(payload,encoding='utf-8')
        print(report['status']+': '+str(report['passedGates'])+'/'+str(report['totalGates'])+' gates')
    else:print(payload,end='')
    return 0 if report['status']=='PASS_BOUNDED_REGRESSION' else 2

if __name__=='__main__':sys.exit(main())
