#!/usr/bin/env python3
"""Static INFOPS P01-S04 C01-C06 overlay invariants; not empirical/conformance certification."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name): return json.loads((ROOT/'research/p01-s04'/name).read_text())
s=load('research-state.json');r=load('s04-c01-c06-owner-approved-decisions.json');c=load('s04-conditional-closure-effect-record.json');o=load('owner-decision-register.json');g=load('g07-owner-approved-decisions.json')
assert len(r['decisions'])==6
assert [d['clauseCount'] for d in r['decisions']]==[22,24,24,26,28,30]
assert all(len(d['clauses'])==d['clauseCount'] and d['ownerDisposition']=='APPROVE' for d in r['decisions'])
assert s['ownerReviewedResearchDecisionsTotal']==r['historicalG01ToG07SubstantiveApprovals']==o['ownerReviewedResearchCount']==g['programmeResearchApprovals']==65
assert s['s04ConsolidationOwnerApprovedDecisions']==o['s04ConsolidationOwnerApprovalCount']==6
assert not s['stageS04Closed'] and not o['stageS04Closed'] and not c['stageClosed']
assert s['s04CurrentStatus']=='NOT_CLOSED' and c['effectiveStageStatus']=='NOT_CLOSED'
assert 'PENDING_ORIGINAL_STAGE_PREREQUISITE_VERIFICATION'==s['s04ClosureEffectiveness']==c['closureEffectiveness']
assert not s['s04OriginalStageCriteriaIndependentlyVerified'] and not c['originalStageCompletionCriteriaIndependentlyVerified']
assert not s['s04IndependentRepositoryAuditEstablished'] and not c['independentRepositoryAuditEstablished']
assert c['conditionalClosureApproved'] and c['ownerApprovedC06TargetClassification']=='CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)'
assert c['g06E0DesignsApprovedUnexecuted']==62 and c['g06E1Executions']==c['g06E2IntegratedPfiExecutions']==0
assert len(c['g06ResidualObligations'])==len(c['g03NormativeHolds'])==12
assert set(c['g06ResidualObligations'].values())==set(c['g03NormativeHolds'].values())=={'OPEN'}
assert c['unresolvedFalsifications']==['F06','F14','F16']
assert c['q0ToQ4JointSufficiency']=='UNESTABLISHED_NOT_FORMALLY_DISPROVEN'
assert c['upstreamAndFamilyAuthoritiesIndependent'] and c['a1ToA9Independent']
assert not c['normativeSourcePinsAdopted'] and not c['normativeSchemasAdopted'] and not c['publicationAuthorized'] and not c['nextStageInitiated']
assert not s['upstreamSourcePinsAdopted'] and not s['publicationAuthorized']
side=(ROOT/'sidebars.js').read_text()
for p in ['p01-stage-04-s04-owner-approved-decisions','p01-stage-04-s04-conditional-closure-effect']:
 assert p in side and (ROOT/'docs/ontology'/f'{p}.md').exists()
assert 'NOT_CLOSED' in (ROOT/'docs/ontology/p01-stage-04-s04-conditional-closure-effect.md').read_text()
print('PASS_STATIC_S04_C01_C06_RESEARCH_OVERLAY_CHECKS')
