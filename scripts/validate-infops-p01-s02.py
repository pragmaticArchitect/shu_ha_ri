#!/usr/bin/env python3
"""Stage 2 RESEARCH-LEDGER consistency checks. Never asserts INFOPS conformance."""
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'research/p01-s02'
issues=[]


def load(name):
    return json.loads((RES/name).read_text(encoding='utf-8'))


def expect(ok, msg):
    if not ok: issues.append(msg)

cases=load('cases.json')
tests=load('hypothesis-tests.json')
pfi=load('realization-experiments.json')
decisions=load('research-decisions.json')
for obj, name in [(cases,'cases'),(tests,'tests'),(pfi,'experiments'),(decisions,'decisions')]:
    expect(obj.get('normative') is False, f'{name} must remain non-normative')
    expect(obj.get('stage')=='P01-S02', f'{name} stage marker mismatch')
    expect(obj.get('count')==len(obj[name]), f'{name} inventory declared count mismatch')

cids=[x['caseId'] for x in cases['cases']]
expect(cids == [f'C{i:02d}' for i in range(1,37)],'Expected C01-C36 in order with no gaps')
allowed={'PROVISIONAL_INFO_CANDIDATE','COMPETING_FAMILY','PRODUCTNESS_NOT_SHOWN','BOUNDARY_UNRESOLVED','INVARIANCE_SUPPORTED','SEMANTIC_CHANGE','IDENTITY_OR_OCCURRENCE'}
for item in cases['cases']:
    expect(item['researchDisposition'] in allowed, f'Unknown case disposition {item["caseId"]}')
    expect(bool(item.get('conditionalInference') and item.get('requiredEvidence')), f'Missing research rationale/evidence {item["caseId"]}')
    expect(item['origin']==('S01_INITIAL' if int(item['caseId'][1:])<=18 else 'S01_ADDITIONAL' if int(item['caseId'][1:])<=28 else 'S02_NEW'), f'Origin mismatch {item["caseId"]}')
expect(cases.get('qualificationDecisionsIssued') is False,'Research must issue no qualification decisions')

ids=[x['testId'] for x in tests['tests']]
expect(ids==[f'F{i:02d}' for i in range(1,17)], 'F01-F16 required')
all_h=set()
for t in tests['tests']:
    expect(t['hypotheticalInference'] in {'COUNTEREXAMPLE_TO_RULE','SUPPORTED_UNDER_PREMISES','CONDITIONALLY_SUPPORTED','UNRESOLVED'}, f'Invalid inference {t["testId"]}')
    for cid in t['linkedCaseIds']:
        expect(cid in cids, f'Unknown case {cid} in {t["testId"]}')
    expect(len(t['linkedCaseIds'])>0,f'No evidence link {t["testId"]}')
    for h in t['linkedHypotheses']:
        expect(re.fullmatch(r'H(0[1-9]|10)',h) is not None, f'Bad hypothesis {h}')
        all_h.add(h)
expect(all_h == {f'H{i:02d}' for i in range(1,11)},'All H01-H10 must be covered')

pfiids=[x['experimentId'] for x in pfi['experiments']]
expect(pfiids==[f'PFI-F{i}' for i in range(1,11)], 'Expected PFI-F1 to F10')
expect(pfi.get('executedAgainstRuntime') is False, 'No real PFI/HDIP execution took place')
expect([d['decisionId'] for d in decisions['decisions']]==[f'S02-D{i:02d}' for i in range(1,7)],'S02-D01..06 required')
expect(all(d['state']=='PROPOSED' for d in decisions['decisions']),'No decision was approved by owner')
expect(decisions.get('ownerAccepted') is False,'Stage 2 not accepted by owner yet')

for page in ['p01-stage-02-pin-differentiation-falsification.md','p01-stage-02-case-disposition-ledger.md','p01-stage-02-cross-enterprise-realization-tests.md','p01-stage-02-hypothesis-dispositions.md']:
    path=ROOT/'docs/ontology'/page
    expect(path.is_file(),f'Missing S02 document {page}')
    if path.is_file():
        txt=path.read_text(encoding='utf-8')
        expect(('non-normative' in txt.lower() or 'not normative' in txt.lower() or 'not frozen' in txt.lower()),f'Non-normative warning missing: {page}')
        expect(('qualification' in txt.lower()),f'Qualification boundary mention missing: {page}')

for path in ['docs/ontology/p01-stage-01-authority-and-ontology-baseline.md','docs/ontology/p01-stage-01-classification-cases.md','docs/ontology/p01-stage-01-ontology-review.md','docs/ontology/p01-stage-01-realization-stress-tests.md']:
    expect((ROOT/path).is_file(),f'Original S01 source missing {path}')

try:
    probes=subprocess.run([sys.executable,str(ROOT/'scripts/run-p01-s02-synthetic-probes.py')],capture_output=True,text=True,check=False)
    expect(probes.returncode==0,'Synthetic arithmetic tests failed: '+probes.stderr.strip())
    if probes.returncode==0:
        result=json.loads(probes.stdout)
        expect(result['syntheticProbes']==8 and result['realRuntimeExecuted'] is False,'Unexpected synthetic probe status')
except Exception as e:
    issues.append('Synthetic probe runner error: '+str(e))

print(f'INFOPS P01-S02 research integrity: {len(cids)} cases, {len(ids)} hypothesis tests, {len(pfiids)} PFI experiments, {len(decisions["decisions"])} unapproved decisions, 8 synthetic probes; {len(issues)} issue(s)')
for msg in issues: print('ERROR:',msg)
print('NOTE: Passing these checks does NOT certify Productness, Product Family, PMDD, PFI or runtime conformance.')
sys.exit(1 if issues else 0)
