#!/usr/bin/env python3
"""Validate G06 E0 research-closure projection without rewriting G05 historical snapshots."""
import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
def j(p):return json.loads((r/p).read_text())
reg=j('research/p01-s04/g06-owner-approved-decisions.json')
items=j('research/p01-s04/g06-research-designs.json')['designs']
closure=j('research/p01-s04/g06-closure-record.json')
state=j('research/p01-s04/research-state.json')
owner=j('research/p01-s04/owner-decision-register.json')
assert len(reg['decisions'])==8 and [len(d['clauses']) for d in reg['decisions']]==[11,12,14,14,16,16,16,18]
assert all(d['ownerDisposition']=='APPROVED' and d['evidenceLevel']=='E0_DESIGN_ONLY' for d in reg['decisions'])
assert len(items)==62 and len({d['id'] for d in items})==62 and all(not d['executed'] for d in items)
assert {p:sum(i['family']==p for i in items) for p in ('FX','PE','NE','TR')}=={'FX':16,'PE':12,'NE':22,'TR':12}
assert closure['status']=='CLOSED_CONDITIONAL_RESEARCH' and closure['qualifier']=='E0_DESIGN_ONLY'
assert len(closure['residualObligations'])==12 and all(x['status']=='OPEN' for x in closure['residualObligations'])
assert len(closure['g03ReleaseHolds'])==12 and set(closure['g03ReleaseHolds'].values())=={'OPEN'}
assert closure['e1Executions']==closure['e2IntegratedPfiExecutions']==0
assert owner['ownerReviewedResearchCount']==state['ownerReviewedResearchDecisionsTotal']==57
assert state['gates']['G07']=='NOT_STARTED' and not state['stageS04Closed'] and not state['publicationAuthorized']
assert reg['unresolvedFalsifications']==['F06','F14','F16']
assert not reg['normative'] and not reg['normativeReleaseAuthorized']
for f in ('docs/ontology/p01-stage-04-g06-owner-approved-decisions.md','docs/ontology/p01-stage-04-g06-research-designs.md','docs/ontology/p01-stage-04-g06-closure-record.md'):
 assert (r/f).exists()
print('PASS: G06 8 approvals, 62 E0-only designs, 12 open residual obligations, 12 release holds, 57 programme approvals; G07 not started.')
