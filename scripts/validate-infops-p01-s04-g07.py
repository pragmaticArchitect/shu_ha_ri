#!/usr/bin/env python3
"""G07 owner-closure static research projection validation, no network or execution tests."""
import json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'research/p01-s04'
load=lambda name:json.loads((p/name).read_text(encoding='utf-8'))
s=load('research-state.json');r=load('owner-decision-register.json');g=load('g07-owner-approved-decisions.json');c=load('g07-closure-record.json')
assert s['ownerReviewedResearchDecisionsTotal']==65
assert r['ownerReviewedResearchCount']==65
assert s['gates']['G07']=='CLOSED_CONDITIONAL_RESEARCH (NORMATIVE_READINESS_NOT_ESTABLISHED)'
assert not s['stageS04Closed'] and not s['publicationAuthorized']
assert g['ownerApprovedDecisions']==8 and len(g['decisions'])==8
assert [d['clauseCount'] for d in g['decisions']]==[17,18,18,20,20,20,20,22]
assert all(len(d['clauses'])==d['clauseCount'] and d['ownerDisposition']=='APPROVED' for d in g['decisions'])
assert c['qualifier']=='NORMATIVE_READINESS_NOT_ESTABLISHED'
assert not c['normativeReleaseAuthorized'] and not c['s04Closed']
assert c['g06ResearchDesignsE0']==62 and c['g06ReferenceE1Executed']==0 and c['g06IntegratedPfiE2Executed']==0
assert len(c['g06ResidualObligations'])==12 and set(c['g06ResidualObligations'].values())=={'OPEN'}
assert len(c['g03ReleaseHolds'])==12 and set(c['g03ReleaseHolds'].values())=={'OPEN'}
assert c['originalUnresolvedFalsifications']==['F06','F14','F16']
assert not c['normativeSourcePinsAdopted'] and not c['normativeSchemasAdopted']
assert all((root/'docs/ontology'/file).exists() for file in ['p01-stage-04-g07-owner-approved-decisions.md','p01-stage-04-g07-closure-record.md'])
assert "'ontology/p01-stage-04-g07-closure-record'" in (root/'sidebars.js').read_text()
print('PASS_STATIC_G07_RESEARCH_OVERLAY_CHECKS')
