#!/usr/bin/env python3
"""Guarded, optional patch of LIVE research-state.json after applying the overlay.
Run from the INFOPS repository root. It never replaces the live file with an old snapshot.
"""
import json
from pathlib import Path
p=Path('research/p01-s04/research-state.json')
if not p.is_file(): raise SystemExit('Missing live research-state.json; no changes made')
a=json.loads(p.read_text(encoding='utf-8'))
expected={'project':'INFOPS','stage':'P01-S04','g06E1Executions':0,'g06E2Executions':0,
          'g06ResidualObligationsOpen':12,'g03NormativeReleaseHoldsOpen':12,
          's04C06OwnerDisposition':'APPROVE','s04OriginalStageCriteriaIndependentlyVerified':False,
          's04IndependentRepositoryAuditEstablished':False,'s04ConsolidationOwnerApprovedDecisions':6}
for k,v in expected.items():
 if a.get(k)!=v: raise SystemExit(f'Guard mismatch {k}: expected {v!r}, saw {a.get(k)!r}; no changes made')
if a.get('s04CurrentStatus') not in ['NOT_CLOSED','CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)']:
 raise SystemExit('Unexpected current status; no changes made')
if a.get('s04ClosureEffectiveness') not in ['PENDING_ORIGINAL_STAGE_PREREQUISITE_VERIFICATION',
 'OWNER_ATTESTED_PROSPECTIVE_EFFECTIVE_2026-11-08']:
 raise SystemExit('Unexpected closure effectiveness value; no changes made')
a['asOf']='2026-11-08'
a['stageS04Closed']=True
a['s04CurrentStatus']='CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)'
a['s04ClosureEffectiveness']='OWNER_ATTESTED_PROSPECTIVE_EFFECTIVE_2026-11-08'
a['s04ProspectiveClosureAuthority']='INFOPS-P01-S04-PCI-0.1'
a['s04ProspectiveClosureDecision']='TA01-EVAL-10-F01'
a['s04ProspectiveClosureCommit']='7ddea588a1c6d7088878fc0bc294bf37012dce1e'
a['s04ProspectiveClosureEffectRecognitionDate']='2026-11-08'
a['s04ProspectiveClosureAttestationRecord']='research/p01-s04/ta01-pc10-effectiveness-attestation-2026-11-08.json'
a['nextDecision']='S04_CONDITIONALLY_CLOSED_TRACK_B_AND_NORMATIVE_RELEASE_NOT_AUTHORIZED'
# historical C06 reference intentionally untouched
p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Updated live research-state.json with prospective effective S04 closure; historical fields retained')
