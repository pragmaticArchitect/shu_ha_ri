#!/usr/bin/env python3
"""Static consistency checks for the newly effective prospective closure record."""
import json
from pathlib import Path
base=Path('research/p01-s04')
a=json.loads((base/'ta01-pc10-prospective-closure-effect.json').read_text())
b=json.loads((base/'ta01-pc01-pc10-owner-assessment-ledger.json').read_text())
c=json.loads((base/'ta01-pc10-effectiveness-attestation-2026-11-08.json').read_text())
assert a['actualEffectiveS04Status']=='CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)'
assert a['effectuation']['qualifyingCommit']==c['qualifyingCommit']['sha']
assert a['historicalC06']['status']=='APPROVED_NOT_EFFECTIVE'
assert a['originalAuthority']['c02IndependentRepositoryAudit']=='NOT_ESTABLISHED'
assert a['v01']['generalActivity']=='VERIFICATION_ACTIVITY_SUSPENDED_CONDITIONAL'
assert a['research']['g06E0Designs']['total']==62 and a['research']['g06E0Designs']['execution']=='UNEXECUTED'
assert a['research']['e1ActualReferenceExecutions']==a['research']['e2ActualIntegratedPfiExecutions']==0
assert a['obligations']['totalOpen']==24 and a['obligations']['discharged']==0
assert len(b['assessmentSubledger'])==10
assert len([x for x in b['assessmentSubledger'] if x['criterionAssessment']=='SATISFIED'])==9
assert b['fourIndependentApprovalLedgers']==dict(g01ThroughG07Substantive=65,s04C01ThroughC06Consolidation=6,s04V01F01ThroughF07Verification=7,ta01F01ThroughF07Governance=7)
assert c['closureEffectRecognitionDate']=='2026-11-08'
assert c['historicalC06']=='APPROVED_NOT_EFFECTIVE'
assert c['normativeReleaseAuthorized'] is False and c['trackBAuthorized'] is False
# Existing sidebar path remains unchanged, so no sidebar edit needed.
for path in ['docs/governance/infops-p01-s04-pc10-owner-approved-pending-effect.md',
             'docs/governance/infops-p01-s04-ta01-pc01-pc10-owner-assessments.md']:
 txt=Path(path).read_text()
 assert 'CLOSED_CONDITIONAL_RESEARCH' in txt
 assert '2026' in txt
rs=base/'research-state.json'
if rs.exists():
 state=json.loads(rs.read_text())
 if state.get('s04ProspectiveClosureDecision')=='TA01-EVAL-10-F01':
  assert state['stageS04Closed'] is True
  assert state['s04CurrentStatus']==a['actualEffectiveS04Status']
  assert state['s04IndependentRepositoryAuditEstablished'] is False
print('PASS — prospective owner-attested effective closure and non-effect invariants')
