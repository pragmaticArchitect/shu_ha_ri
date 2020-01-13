#!/usr/bin/env python3
"""Static INFOPS PC-10 approval-not-effective overlay invariants; not a Git audit."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base=root/'research/p01-s04'
a=json.loads((base/'ta01-pc01-pc10-owner-assessment-ledger.json').read_text())
b=json.loads((base/'ta01-pc10-prospective-closure-effect.json').read_text())
assert a['fourIndependentApprovalLedgers']=={'g01ThroughG07Substantive':65,'s04C01ThroughC06Consolidation':6,'s04V01F01ThroughF07Verification':7,'ta01F01ThroughF07Governance':7}
assert len(a['assessmentSubledger'])==10
assert [x['criterion'] for x in a['assessmentSubledger']]==[f'PC-{i:02d}' for i in range(1,11)]
assert all(x['criterionAssessment']=='SATISFIED' for x in a['assessmentSubledger'][:9])
assert a['assessmentSubledger'][9]['criterionAssessment']=='OWNER_DECISION_APPROVED_CLOSURE_NOT_EFFECTIVE'
assert a['actualEffectiveS04Status']=='NOT_CLOSED'
assert b['approvalState']=='APPROVED_NOT_EFFECTIVE' and b['actualEffectiveS04Status']=='NOT_CLOSED'
assert b['effectuation']['qualifyingCommit']=='NOT_ESTABLISHED'
assert b['historicalC06']['status']=='APPROVED_NOT_EFFECTIVE'
assert b['historicalC06']['safeguards']==['C06-F01.6','C06-F01.29']
assert b['v01']['series']=='NOT_CLOSED' and b['v01']['generalActivity']=='VERIFICATION_ACTIVITY_SUSPENDED_CONDITIONAL'
assert b['originalAuthority']['c02IndependentRepositoryAudit']=='NOT_ESTABLISHED'
assert b['research']['g06E0Designs']['total']==62
assert sum(b['research']['g06E0Designs'][x] for x in ('FX','PE','NE','TR'))==62
assert b['research']['e1ActualReferenceExecutions']==b['research']['e2ActualIntegratedPfiExecutions']==0
assert b['obligations']['totalOpen']==24 and b['obligations']['discharged']==0
assert b['obligations']['G06-RO01-RO12']==b['obligations']['G03-R01-R12']=='ALL_OPEN'
assert b['research']['unresolvedFalsifications']==['F06','F14','F16']
print('PASS_STATIC_OVERLAY_CHECKS: PC-10 approved/not-effective; S04 NOT_CLOSED; 65/6/7/7; 62 unexecuted E0; E1/E2=0; 24 OPEN')
