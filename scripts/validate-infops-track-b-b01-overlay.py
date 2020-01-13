#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'research/p01-track-b/b01-owner-approved-charter.json'
d=json.loads(p.read_text())
assert len(d['clauses'])==20 and d['clauses'][0]['id']=='F01.1' and d['clauses'][-1]['id']=='F01.20'
assert d['ownerDisposition']=='APPROVE' and d['charterStatus']=='OWNER_APPROVED'
assert d['repositoryAdoption']=='NOT_ESTABLISHED' and d['preparatoryAuthorization']=='APPROVED_SUBJECT_TO_ADOPTION'
assert d['b01Completion']=='NOT_ESTABLISHED' and set(d['futureWorkPackages'].values())=={'NOT_AUTHORIZED'}
assert d['g06E0']['approvedUnexecuted']==62 and d['E1ObservedExecutions']==d['E2ObservedExecutions']==0
assert d['G06_RO01_RO12']==d['G03_R01_R12']=='ALL_OPEN'
assert list(d['historicalLedgers'].values())==[65,6,7,7]
assert d['s04']['historicalC06']=='APPROVED_NOT_EFFECTIVE' and 'CLOSED_CONDITIONAL_RESEARCH' in d['s04']['effectiveProspectiveStatus']
assert len(d['unresolvedFalsifications'])==3
md=(root/'docs/governance/infops-p01-tb-b01-owner-approved-research-charter.md').read_text()
assert all('### F01.%d'%i in md for i in range(1,21))
sidebar=root/'sidebars.js'
if sidebar.exists():
    assert sidebar.read_text().count('governance/infops-p01-tb-b01-owner-approved-research-charter')==1
print('PASS: B01 approved charter, 20 clauses, S04 preservation, E0/E1/E2 and obligation guards')
