#!/usr/bin/env python3
"""Static invariants for owner-approved INFOPS S04 V01 research overlay. Not a Docusaurus build or empirical test."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n):return json.loads((ROOT/'research/p01-s04'/n).read_text())
s=load('research-state.json');o=load('owner-decision-register.json')
r=load('s04-v01-f01-f07-owner-approved-decisions.json');v=load('s04-v01-verification-activity-state.json')
c=load('s04-conditional-closure-effect-record.json');sd=load('s04-c01-c06-owner-approved-decisions.json')
assert len(r['decisions'])==7 and [d['clauseCount'] for d in r['decisions']]==[12,18,18,16,16,14,18]
assert r['approvedClauseCount']==sum(d['clauseCount'] for d in r['decisions'])==112
assert all(d['ownerDisposition']=='APPROVE' and len(d['clauses'])==d['clauseCount'] for d in r['decisions'])
assert all([cl['id'] for cl in d['clauses']]==[f"F{int(d['id'][-2:]):02}.{i}" for i in range(1,d['clauseCount']+1)] for d in r['decisions'])
assert [d['id'] for d in r['decisions']]==[f'S04-V01-F{i:02}' for i in range(1,8)]
assert not r['normative'] and not r['originalClausesVerbatim'] and not r['noNormativeRelease'] is False
assert s['ownerReviewedResearchDecisionsTotal']==o['ownerReviewedResearchCount']==c['historicalG01ToG07SubstantiveApprovals']==65
assert s['s04ConsolidationOwnerApprovedDecisions']==o['s04ConsolidationOwnerApprovalCount']==len(sd['decisions'])==6
assert s['s04V01OwnerApprovedDecisions']==o['s04V01OwnerApprovalCount']==v['v01OwnerApprovalCount']==7
assert s['s04V01ApprovedClauseCount']==o['s04V01ApprovedClauseCount']==v['v01ApprovedClauseCount']==112
assert s['s04V01VerificationActivity']==o['s04V01VerificationActivity']==v['verificationActivityStatus']=='VERIFICATION_ACTIVITY_SUSPENDED_CONDITIONAL'
assert not s['s04V01VerificationSeriesClosed'] and not o['s04V01VerificationSeriesClosed'] and not v['verificationSeriesClosed']
assert s['s04CurrentStatus']==o['s04CurrentEffectiveStatus']==v['effectiveStageStatus']==c['effectiveStageStatus']=='NOT_CLOSED'
assert not s['stageS04Closed'] and not o['stageS04Closed'] and not v['stageClosed'] and not c['stageClosed']
assert s['s04ClosureEffectiveness']==v['s04ClosureEffectiveness']==c['closureEffectiveness']=='PENDING_ORIGINAL_STAGE_PREREQUISITE_VERIFICATION'
assert c['conditionalClosureApproved'] and v['c06OwnerApproved']
assert v['approvedTargetClassification']==c['ownerApprovedC06TargetClassification']
assert v['c06SafeguardClauses']==['F01.6','F01.29']
assert v['originalStageCharter']==v['originalStageAmendments']=='NOT_VERIFIED'
assert v['completeOriginalClosureCriteria']=='NOT_ESTABLISHED' and v['criterionLevelSatisfaction']=='NOT_PERFORMED'
assert v['boundedSourceRecoveryStatus']=='PERFORMED_WITH_LIMITATIONS' and not v['sourceScopeExhaustive'] and not v['sourceProvenNonexistent']
assert not v['independentRepositoryAuditEstablished'] and not s['s04IndependentRepositoryAuditEstablished'] and not c['independentRepositoryAuditEstablished']
assert v['unresolvedFalsifications']==['F06','F14','F16'] and v['q0ToQ4JointSufficiency']=='UNESTABLISHED_NOT_FORMALLY_DISPROVEN'
assert v['g06E0DesignsApprovedUnexecuted']==c['g06E0DesignsApprovedUnexecuted']==62
assert v['g06E1Executions']==v['g06E2IntegratedPfiExecutions']==c['g06E1Executions']==c['g06E2IntegratedPfiExecutions']==0
assert len(v['g06ResidualObligations'])==len(v['g03NormativeHolds'])==12
assert set(v['g06ResidualObligations'].values())==set(v['g03NormativeHolds'].values())=={'OPEN'}
assert v['exactIdentityVersionOccurrenceCurrentnessDistinctionsPreserved']
assert not any([v['normativeSourcePinsAdopted'],v['normativeSchemasAdopted'],v['normativeReadinessEstablished'],v['publicationAuthorized'],v['nextStageInitiated']])
assert not any([s['upstreamSourcePinsAdopted'],s['publicationAuthorized'],o['publicationAuthorized']])
primary=(ROOT/'docs/ontology/p01-stage-04-owner-decisions.md').read_text()
sub=(ROOT/'docs/ontology/p01-stage-04-v01-owner-approved-decisions.md').read_text()
status=(ROOT/'docs/ontology/p01-stage-04-v01-verification-activity.md').read_text()
assert 'editorial' in primary.lower() and 'not verbatim' in sub.lower()
for d in r['decisions']:
 assert d['id'] in primary and d['id'] in sub
 for cl in d['clauses']:
  assert cl['id'] in sub
for marker in ['NOT_CLOSED','VERIFICATION_ACTIVITY_SUSPENDED_CONDITIONAL','NOT_VERIFIED','NOT_ESTABLISHED']:
 assert marker in status
side=(ROOT/'sidebars.js').read_text()
for stem in ['p01-stage-04-v01-owner-approved-decisions','p01-stage-04-v01-verification-activity']:
 assert stem in side and (ROOT/'docs/ontology'/(stem+'.md')).exists()
print('PASS_STATIC_S04_V01_F01_F07_RESEARCH_OVERLAY_CHECKS')
