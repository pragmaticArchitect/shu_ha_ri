#!/usr/bin/env python3
"""G04 owner-approved research reconciliation validation. NOT INFOPS conformance or certification."""
import json,hashlib,sys,re
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research/p01-s04'
issues=[]
def need(ok,msg):
    if not ok: issues.append(msg)
def js(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
base=js('research/p01-s04/g04-preclosure-baseline-integrity.json')
approved=js('research/p01-s04/g04-owner-approved-decisions.json')
case_rec=js('research/p01-s04/g04-case-reconciliation.json')
test_rec=js('research/p01-s04/g04-falsification-reconciliation.json')
manifest=js('research/p01-s04/g04-overlay-manifest.json')
state=js('research/p01-s04/research-state.json')
register=js('research/p01-s04/owner-decision-register.json')
holds=js('research/p01-s04/normative-release-holds.json')
historical=js('research/p01-s04/g04-proposed-owner-review-sequence.json')
checkpoint={v['path']:v['sha256'] for v in base['files']}
g05_base=js('research/p01-s04/g05-preclosure-baseline-integrity.json')
need(len(checkpoint)==82,'G04 checkpoint must contain 82 prior source files')
need(approved['normative'] is False and approved['normativeReleaseAuthorized'] is False,'G04 approvals cannot be normative')
need(approved['ownerReviewedCount']==9 and approved['approvedCount']==9,'Expected nine G04 owner approvals')
need(approved['status']=='CLOSED_CONDITIONAL_RESEARCH' and approved['closureDecisionId']=='G04-D09-F01','G04 closure assertion mismatch')
need(len(approved['decisions'])==9,'Nine G04 decisions missing')
for idx,d in enumerate(approved['decisions'],1):
    need(d['id']==f'G04-D{idx:02d}-F01' and d['ownerDisposition']=='APPROVED','G04 owner disposition mismatch')
    need(d['decisionDate']=='2026-10-20' and d['normative'] is False and d['qualificationIssued'] is False,'G04 must be research-only')
    need(len(d['clauses'])>=10 and all(x.get('position') and x.get('topic') for x in d['clauses']),'Owner finding clauses must be substantive')
    for case_id,label in d['originalCaseDispositions'].items():
        found=next((c for c in case_rec['cases'] if c['caseId']==case_id),None)
        need(found is not None and found['researchDisposition']==label,'G04 case inference was rewritten: '+case_id)
for item in ['docs/ontology/p01-stage-04-g04-owner-approved-decisions.md','docs/ontology/p01-stage-04-g04-closure-record.md']:
    content=(ROOT/item).read_text(encoding='utf-8')
    need(content.startswith('---\n') and 'NON-NORMATIVE' in content.upper(),'Owner record missing frontmatter/non-normative disclosure: '+item)
    need("'ontology/"+Path(item).stem+"'" in (ROOT/'sidebars.js').read_text(encoding='utf-8'),'G04 sidebar missing: '+item)
doc=(ROOT/'docs/ontology/p01-stage-04-g04-owner-approved-decisions.md').read_text(encoding='utf-8')
master=(ROOT/'docs/ontology/p01-stage-04-owner-decisions.md').read_text(encoding='utf-8')
plan=(ROOT/'docs/ontology/p01-stage-04-g04-plan.md').read_text(encoding='utf-8')
intro='## G04 — Nine owner-approved decisions (full substantive record)'
ending='## Earlier owner-reviewed gates — G01 through G03'
need(intro in master and ending in master, 'G04 full master register section missing')
if intro in master and ending in master:
    section=master.split(intro,1)[1].split(ending,1)[0]
    content_start='### Decision overview'
    need(content_start in section, 'G04 full approved content not embedded in owner register')
    if content_start in section:
        actual=section[section.index(content_start):].strip()
        if '## Decision overview' in doc:
            source=doc[doc.index('## Decision overview'):].strip()
            target='\n'.join('#'+x if x.startswith(('## ','### ')) else x for x in source.splitlines()).strip()
            need(actual==target, 'Principal owner register G04 clauses diverge from complete owner-approved decision source')
need(all('#### '+d['id']+' - ' in master and d['summary'] in master for d in approved['decisions']),
     'Principal owner register missing approved G04 headings or decisions')
need('Neither G04-D01 nor any later G04 item is approved by this overlay.' not in plan,
     'Historical plan incorrectly presents G04 as currently unapproved')
need('CLOSED_CONDITIONAL_RESEARCH' in plan and 'now superseded' in plan,
     'Historic G04 plan does not explicitly distinguish its pre-approval status from current closure')

for d in approved['decisions']:
    need(d['id'] in doc and d['summary'] in doc,'Approved finding not rendered in G04 doc: '+d['id'])
    for clause in d['clauses']:need(clause['position'] in doc,'Approved clause missing from G04 doc: '+d['id']+' '+clause['topic'])
case_source='research/p01-s02/cases.json'
test_source='research/p01-s02/hypothesis-tests.json'
s03_source='research/p01-s03/case-evaluations.json'
for p in [case_source,test_source,s03_source]:
    need(sha(p)==checkpoint[p],'Protected prior-stage evidence changed: '+p)
C=js(case_source)['cases'];T=js(test_source)['tests'];S03=js(s03_source)['cases']
need(len(C)==36 and len(T)==16 and len(S03)==20,'Original corpus count changed')
need(case_rec['count']==36 and case_rec['sourceSha256']==sha(case_source),'Case reconciliation source integrity mismatch')
need(case_rec['s03SourceCaseCount']==20 and case_rec['s03SourceSha256']==sha(s03_source),'S03 reconciliation source mismatch')
need(case_rec['cases']==[{k:x[k] for k in ['caseId','scenario','researchDisposition']} for x in C],'C01-C36 dispositions changed')
need(case_rec['s03Cases']==[{'caseId':x['caseId'],'researchDisposition':x['researchDisposition'],'sourceCaseIds':x.get('sourceCaseIds',[])} for x in S03],'S03 dispositions changed')
need(case_rec['statuses']==dict(sorted(Counter(x['researchDisposition'] for x in C).items())),'Wrong original case counts')
need(test_rec['count']==16 and test_rec['sourceSha256']==sha(test_source),'Falsification source mismatch')
need(test_rec['tests']==[{'testId':x['testId'],'hypotheticalInference':x['hypotheticalInference'],'linkedCaseIds':x['linkedCaseIds']} for x in T],'F01-F16 changed')
need(test_rec['statuses']==dict(sorted(Counter(x['hypotheticalInference'] for x in T).items())),'Wrong F01-F16 outcome counts')
need(test_rec['Q1_Q4UniversalNecessityProven'] is False and test_rec['Q0_Q4JointSufficiencyProven'] is False and test_rec['empiricalClassifierMetricsEstablished'] is False,'Research proof overclaim')
q=approved['qStatus']
need(all(q[f'Q{i}'].endswith('NOT_ESTABLISHED') for i in range(1,5)),'Universal Q1-Q4 necessity not proven')
need(q['Q0_Q4_jointSufficiency']=='NOT_ESTABLISHED' and q['conjunctionFormallyRefuted'] is False,'Q0-Q4 sufficiency status incorrect')
need(q['Q5']=='PROCEDURAL_ADJUDICATION_NOT_INTRINSIC_PRODUCT_PROPERTY','Q5 must be procedural')
need(state['gates']['G04']=='CLOSED_CONDITIONAL_RESEARCH' and register['gates'][3]['state']=='CLOSED_CONDITIONAL_RESEARCH','G04 gate status inconsistent')
need(state['ownerReviewedResearchDecisionsTotal']==49 and register['ownerReviewedResearchCount']==49,'Owner decision counts wrong after G05 projection')
need(state['g04ClosureDecision']=='G04-D09-F01' and state['stageS04Closed'] is False,'Gate closure is not stage closure')
need(register['gates'][3]['approvedCount']==9 and register['gates'][3]['decisions'][-1]['id']=='G04-D09-F01','G04 approved register missing closure')
need(state['gates']['G05']=='CLOSED_CONDITIONAL_RESEARCH','G05 must reflect later owner-approved conditional closure')
for g in ['G06','G07']:
    need(state['gates'][g]=='PENDING' and approved['subsequentGates'][g]=='PENDING',g+' must be pending')
need(approved['subsequentGates']['G05']=='PENDING', 'Original G04 record must preserve its historical not-started G05 fact')
need(all(not v['resolved'] for v in holds['holds']) and len(holds['holds'])==12,'All 12 G03 source/release blockers must remain open')
need(all(not v['approved'] and v['ownerDisposition']=='NOT_REQUESTED' for v in historical['dispositions']), 'Historical G04 proposed snapshot changed')
need(historical['status']=='PROPOSED_NOT_APPROVED','Historical G04 programme source rewritten')
for flag in ['normative','upstreamSourcePinsAdopted','informationFamilyNecessaryAndSufficientProven','infoprodNormative','infopdsNormative','dppCoreAdopted','informationDppProfileNormative','publicationAuthorized']:
    need(state[flag] is False,'Current state claims normative qualification: '+flag)
# Check that no prior-archive files were changed outside the declared G04 modified set.
prior=set(checkpoint)
modified=set(manifest['modifiedPaths'])
added=set(manifest['addedPaths'])
need(prior & added==set() and modified <= prior,'G04 added/modified split invalid')
need({v['path'] for v in manifest['payload']}==(added|modified)-{'research/p01-s04/g04-overlay-manifest.json'}, 'G04 manifest payload mismatch')
# Repository owners may independently customize deployment-specific website assets.
# Such local customizations are not Product or source-authority records.
siteCustomizations={'docusaurus.config.js','src/css/custom.css','src/pages/index.module.css',
                    'static/img/favicon.svg','static/img/infops-mark.svg'}
for p,h in checkpoint.items():
    if not (ROOT/p).is_file():
        known={x['path']:x for x in g05_base.get('legacyHistoricalAttestationDiscrepancies',[])}.get(p)
        need(known is not None and known['missingFromOwnerSource'] is True and p not in g05_base.get('fileHashes',{}), 'NEW missing original pre-G04 historical file: '+p)
        continue
    if p not in modified and p not in siteCustomizations:
        need(sha(p)==h or (g05_base['fileHashes'].get(p)==sha(p)), 'Undeclared change relative to original owner G04 baseline: '+p)
    elif p in modified:
        need(sha(p)!=h,'G04 modified path unexpectedly equals pre-G04 archived file: '+p)
g05_base=js('research/p01-s04/g05-preclosure-baseline-integrity.json')
g05_changes=set(js('research/p01-s04/g05-overlay-manifest.json')['modifiedPaths'])
for v in manifest['payload']:
    need((ROOT/v['path']).is_file(),'Missing G04 payload file: '+v['path'])
    if v['path'] in g05_changes:
        need(g05_base['fileHashes'].get(v['path'])==v['sha256'],'G04 source hash differs from G05 preclosure checkpoint: '+v['path'])
    elif (ROOT/v['path']).is_file():
        need(sha(v['path'])==v['sha256'],'Changed G04 payload hash: '+v['path'])
        need((ROOT/v['path']).stat().st_size==v['sizeBytes'],'Changed G04 payload size: '+v['path'])
need(len(added)==manifest['addedCount'] and len(modified)==manifest['modifiedCount'],'Manifest counts wrong')
if g05_base.get('legacyHistoricalAttestationDiscrepancies'):
    print('INHERITED BASELINE ATTESTATION WARNING: historic missing merge notes / G01-G03 checkpoint differences are recorded, not remediated by G05.')
need(manifest['baseArchiveSha256']==base['sourceArchiveSha256'],'Wrong prior G01-G03 baseline archive hash')
need(manifest['normative'] is False and manifest['releaseAuthorized'] is False,'G04 overlay manifest cannot release standards')
need(manifest['gateClosureStatus']=='CLOSED_CONDITIONAL_RESEARCH','G04 closure manifest status wrong')
print(f'INFOPS G04 research closure: 9/9 decisions; C01-C36={len(C)}, F01-F16={len(T)}, S03-T01-T20={len(S03)} preserved; G03-R01-R12={len(holds["holds"])} OPEN; {len(added)} added, {len(modified)} modified files; {len(issues)} issue(s).')
for i in issues:print('ERROR:',i)
sys.exit(1 if issues else 0)
