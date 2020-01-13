#!/usr/bin/env python3
"""G05 owner-approved conditional research closure integrity validator.

This validates exact repo-overlay provenance, case preservation, decision-document
parity and non-normative release boundaries. It does NOT qualify Products,
prove semantic truth, execute all D07 probes or authorize publication.
"""
import hashlib, json, sys, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ISSUES=[]
def need(ok,msg):
    if not ok: ISSUES.append(msg)
def js(path):
    file=ROOT/path
    if not file.is_file():
        ISSUES.append('Missing '+path)
        return {}
    try: return json.loads(file.read_text(encoding='utf-8'))
    except (ValueError,UnicodeError) as e:
        ISSUES.append('Bad JSON '+path+': '+str(e)); return {}
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

g05=js('research/p01-s04/g05-owner-approved-decisions.json')
probes=js('research/p01-s04/g05-adversarial-probes.json')
closure=js('research/p01-s04/g05-closure-record.json')
base=js('research/p01-s04/g05-preclosure-baseline-integrity.json')
manifest=js('research/p01-s04/g05-overlay-manifest.json')
state=js('research/p01-s04/research-state.json')
reg=js('research/p01-s04/owner-decision-register.json')
holds=js('research/p01-s04/normative-release-holds.json')
g04=js('research/p01-s04/g04-owner-approved-decisions.json')
g04cases=js('research/p01-s04/g04-case-reconciliation.json')
g04tests=js('research/p01-s04/g04-falsification-reconciliation.json')
s02cases=js('research/p01-s02/cases.json')
s02tests=js('research/p01-s02/hypothesis-tests.json')
s03=js('research/p01-s03/case-evaluations.json')

need(g05.get('project')=='INFOPS' and g05.get('gate')=='G05','Wrong G05 project/gate')
need(g05.get('status')=='CLOSED_CONDITIONAL_RESEARCH' and g05.get('closureDecisionId')=='G05-D08-F01','G05 owner closure missing')
need(g05.get('normative') is False and g05.get('normativeReleaseAuthorized') is False,'G05 must not authorize normativity')
need(g05.get('ownerReviewedCount')==8 and g05.get('approvedCount')==8 and len(g05.get('decisions',[]))==8,'G05 count mismatch')
expectedIds=[f'G05-D{i:02d}-F01' for i in range(1,9)]
need([d.get('id') for d in g05.get('decisions',[])]==expectedIds,'Wrong G05 decision identity/order')
expectedClauseCounts=[9,10,8,9,10,10,11,11]
for d,num in zip(g05.get('decisions',[]),expectedClauseCounts):
    need(d.get('ownerDisposition')=='APPROVED' and d.get('normative') is False and d.get('qualificationIssued') is False,'G05 decision incorrectly normative/approved: '+d.get('id','?'))
    need(d.get('decisionDate')=='2026-10-20' and d.get('publicationAuthorized') is False,'G05 source date/publication status invalid')
    need(len(d.get('clauses',[]))==num,'G05 clause-count mismatch: '+d.get('id','?'))
    need([c.get('id') for c in d.get('clauses',[])]==[f'F01.{i}' for i in range(1,num+1)],'G05 clause identifiers mismatch: '+d.get('id','?'))
    need(all(len(c.get('position',''))>=50 and c.get('topic') for c in d.get('clauses',[])),'G05 approved finding content too short/missing: '+d.get('id','?'))
need(closure.get('closureDecisionId')=='G05-D08-F01' and closure.get('closureStatus')=='CLOSED_CONDITIONAL_RESEARCH','G05 closure record mismatch')
need(closure.get('approvedDecisions')==expectedIds and closure.get('totalApprovedInG05')==8,'Closure approved-decision parity failure')
need(closure.get('allProgrammeResearchApprovedCount')==49 and closure.get('previousG04ApprovedCount')==41,'Wrong closure counts')
need(closure.get('releaseAuthorized') is False and closure.get('normative') is False and closure.get('schemasNormative') is False,'Closure incorrectly issues Product norm')
need(closure.get('actualProductsCertified')==0 and closure.get('sourcePinsAdopted') is False and closure.get('stageS04Closed') is False,'Closure overclaims certification/adoption')
need(closure.get('allHoldsOpen') is True and closure.get('releaseHolds')==[f'G03-R{i:02d}' for i in range(1,13)],'Closure lost open hold references')
need(closure.get('subsequentGates')=={'G06':'PENDING_NOT_STARTED','G07':'PENDING_NOT_STARTED'},'G06/G07 must remain pending')
q=closure.get('qualificationResearchLimits',{})
need(q.get('Q0')=='BPS_PRODUCTNESS_INDEPENDENT' and q.get('Q1_Q4UniversalNecessity')=='NOT_ESTABLISHED' and q.get('Q0_Q4JointSufficiency')=='NOT_ESTABLISHED' and q.get('jointSufficiencyFormallyRefuted') is False and q.get('Q5')=='PROCEDURAL_ONLY','Q0-Q5 epistemic limits altered')

need(state.get('gates',{}).get('G05')=='CLOSED_CONDITIONAL_RESEARCH' and state.get('gates',{}).get('G06')=='PENDING' and state.get('gates',{}).get('G07')=='PENDING','Gate statuses invalid')
need(state.get('gates',{}).get('G04')=='CLOSED_CONDITIONAL_RESEARCH' and state.get('gates',{}).get('G03')=='CLOSED_CONDITIONAL_RESEARCH','Prior gates changed')
need(state.get('ownerReviewedResearchDecisionsTotal')==49 and state.get('explicitApprovalsWithResearchSummaryAvailable')==49,'S04 counts invalid')
need(state.get('stageS04Closed') is False and state.get('g05ProbesEmpiricallyExecuted') is False,'Research closure must not be S04 or empirical-test completion')
for field in ['normative','upstreamSourcePinsAdopted','informationFamilyNecessaryAndSufficientProven','infoprodNormative','infopdsNormative','dppCoreAdopted','informationDppProfileNormative','hdipArchitectureConformanceCertified','productMaturityOrPMDDGranted','publicationAuthorized']:
    need(state.get(field) is False,'Normative/proof flag incorrect: '+field)
need(state.get('actualProductsQualified')==0,'Actual Product qualification incorrectly recorded')
need(reg.get('ownerReviewedResearchCount')==49 and reg.get('explicitApprovalsWithResearchSummaryAvailable')==49,'Master owner-decision count mismatch')
G=reg.get('gates',[])
need([g.get('gate') for g in G]==['G01','G02','G03','G04','G05','G06','G07'],'Gate identities invalid')
if len(G)==7:
    need([g.get('approvedCount') for g in G[:5]]==[15,7,10,9,8],'Owner approval group counts wrong')
    need(G[4].get('state')=='CLOSED_CONDITIONAL_RESEARCH' and G[4].get('closureDecisionId')=='G05-D08-F01','Owner register G05 state invalid')
    need(G[4].get('decisions')==g05.get('decisions'),'FULL G05 decision/clauses parity mismatch with main register')
    need(G[5].get('state')=='PENDING' and G[6].get('state')=='PENDING','Owner register prematurely starts next gate')
    need([d.get('id') for d in G[3].get('decisions',[])]==[d.get('id') for d in g04.get('decisions',[])],'G04 owner IDs altered while adding G05')
    need(all(x.get('title')==y.get('title') and x.get('summary')==y.get('summary') for x,y in zip(G[3].get('decisions',[]),g04.get('decisions',[]))),'G04 approved titles/summaries altered while adding G05')
need(g04.get('ownerReviewedCount')==9 and g04.get('status')=='CLOSED_CONDITIONAL_RESEARCH','G04 historical closure altered')
need(holds.get('normativeAdoptionReady') is False and len(holds.get('holds',[]))==12,'Release hold count/status wrong')
need([h.get('id') for h in holds.get('holds',[])]==[f'G03-R{i:02d}' for i in range(1,13)],'Hold identifiers modified')
need(all(h.get('resolved') is False for h in holds.get('holds',[])),'Normative-release hold falsely resolved')

need(len(s02cases.get('cases',[]))==36 and len(s02tests.get('tests',[]))==16 and len(s03.get('cases',[]))==20,'Original S02/S03 corpus counts wrong')
testMap={t['testId']:t['hypotheticalInference'] for t in s02tests.get('tests',[])}
need(all(testMap.get(f)=='UNRESOLVED' for f in ['F06','F14','F16']),'Unresolved F06/F14/F16 changed')
need(closure.get('originalResearch')=={'S02Cases':36,'S02Tests':16,'S03Cases':20,'preserved':True,'unresolved':['F06','F14','F16']},'Closure original research statement altered')
need(g04cases.get('cases')==[{k:x[k] for k in ['caseId','scenario','researchDisposition']} for x in s02cases.get('cases',[])],'Original S02 C01-C36 dispositions changed relative to G04')
need(g04cases.get('s03Cases')==[{'caseId':x['caseId'],'researchDisposition':x['researchDisposition'],'sourceCaseIds':x.get('sourceCaseIds',[])} for x in s03.get('cases',[])],'Original S03 T01-T20 dispositions changed relative to G04')
need(g04tests.get('tests')==[{'testId':x['testId'],'hypotheticalInference':x['hypotheticalInference'],'linkedCaseIds':x['linkedCaseIds']} for x in s02tests.get('tests',[])],'Original S02 F01-F16 dispositions changed relative to G04')
need(g04tests.get('Q1_Q4UniversalNecessityProven') is False and g04tests.get('Q0_Q4JointSufficiencyProven') is False and g04tests.get('empiricalClassifierMetricsEstablished') is False,'G04 falsification proof overclaimed')

need(probes.get('count')==16 and len(probes.get('probes',[]))==16,'Wrong number of D07 probes')
need(probes.get('approvedBy')=='G05-D07-F01' and probes.get('empiricalExecutionCompleted') is False and probes.get('empiricalClassifierMetricsEstablished') is False,'D07 hypothetical probes incorrectly shown executed')
need(probes.get('unresolvedOriginalFalsifications')==['F06','F14','F16'] and probes.get('originalS02S03CaseSourcesModified') is False,'D07 original research boundary broken')
allC={c['caseId'] for c in s02cases.get('cases',[])}
allF={t['testId'] for t in s02tests.get('tests',[])}
for i,t in enumerate(probes.get('probes',[]),1):
    need(t.get('probeId')==f'D07-X{i:02d}' and t.get('status')=='OWNER_APPROVED_RESEARCH_DESIGN_NOT_EMPIRICALLY_EXECUTED','D07 probe identity/status mismatch')
    need(t.get('conclusiveProductQualification') is False and t.get('changesOriginalDispositions') is False,'D07 probe makes invalid qualification claim')
    need(set(t.get('sourceCaseIds',[]))<=allC and set(t.get('sourceTestIds',[]))<=allF,'D07 references nonexistent original case/test')
    need(bool(t.get('expectedConditionalInterpretation')),'D07 probe missing expected interpretation')

# Full substantive parity: the G05 owner decisions must be directly present in
# the prominent main owner-decision register, not only separate JSON or a side page.
source=(ROOT/'docs/ontology/p01-stage-04-g05-owner-approved-decisions.md').read_text(encoding='utf-8')
master=(ROOT/'docs/ontology/p01-stage-04-owner-decisions.md').read_text(encoding='utf-8')
try:
    start=source.index('## Decision overview')
    end=source.index('**Closure constraints:**')
    section=source[start:end].strip()
    target='\n'.join('#'+line if line.startswith(('## ','### ')) else line for line in section.splitlines()).strip()
    mstart=master.index('### Decision overview',master.index('## G05 — Eight owner-approved decisions'))
    mend=master.index('## G04 — Nine owner-approved decisions')
    actual=master[mstart:mend].strip()
    need(actual==target,'G05 FULL substantive decision paragraphs diverge between dedicated and master Docusaurus page')
except ValueError as e:
    ISSUES.append('Master G05 source section missing: '+str(e))
for d in g05.get('decisions',[]):
    need(d['id'] in source and d['id'] in master and d['summary'] in source and d['summary'] in master,'G05 decision title/summary missing from documentation: '+d['id'])
    for c in d.get('clauses',[]):
        need(c['position'] in source and c['position'] in master,'Approved G05 clause omitted from prominent owner register: '+d['id']+'/'+c['id'])
need('F06, F14 and F16' in (ROOT/'docs/ontology/p01-stage-04-g05-closure-record.md').read_text(encoding='utf-8'), 'G05 closure doc must preserve unresolved F06/F14/F16')
sidebar=(ROOT/'sidebars.js').read_text(encoding='utf-8')
for p in ['p01-stage-04-g05-plan','p01-stage-04-g05-owner-approved-decisions','p01-stage-04-g05-adversarial-probes','p01-stage-04-g05-closure-record']:
    rel='docs/ontology/'+p+'.md'
    need((ROOT/rel).is_file(), 'New G05 page missing: '+rel)
    if (ROOT/rel).exists():need((ROOT/rel).read_text(encoding='utf-8').startswith('---\n'),'Missing Docusaurus frontmatter: '+rel)
    need("'ontology/"+p+"'" in sidebar,'Missing G05 sidebar entry: '+p)
need('49 distinct owner-approved research decisions' in (ROOT/'docs/ontology/p01-stage-04-overview.md').read_text(encoding='utf-8'),'S04 overview not updated to 49 approvals')

# Strict source ZIP to overlay delta integrity, including historic files.
files=base.get('fileHashes',{})
need(base.get('sourceArchiveName')=='INFOPS(1).zip' and base.get('sourceZipRoot')=='shu_ha_ri/' and base.get('sourceFileCount')==89 and len(files)==89,'Wrong supplied G04 baseline checkpoint')
changed=set(manifest.get('modifiedPaths',[]))
added=set(manifest.get('addedPaths',[]))
need(not changed & added,'Path both added/modified')
need(changed <= set(files) and not added & set(files),'G05 overlay declares incorrect new/existing file paths')
need(len(changed)==manifest.get('modifiedCount') and len(added)==manifest.get('addedCount'),'G05 overlay counts mismatch')
need(manifest.get('archiveOverlayRoot')=='' and manifest.get('sourceZipRoot')=='shu_ha_ri/','Overlay paths must be repository-relative')
need(manifest.get('normative') is False and manifest.get('releaseAuthorized') is False and manifest.get('gateClosureStatus')=='CLOSED_CONDITIONAL_RESEARCH','Overlay falsely grants release')
need(manifest.get('baseArchiveSha256')==base.get('sourceArchiveSha256'),'Wrong source ZIP attestation in G05 manifest')
actual_files={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file()}
need(actual_files==set(files)|added,'Unexpected additions or missing owner-uploaded files')
for p,h in files.items():
    if (ROOT/p).is_file():
        current=sha(p)
        if p not in changed: need(current==h,'Undeclared change to supplied G04 file: '+p)
        else: need(current!=h,'Changed file byte-identical to G04 baseline: '+p)
for p in changed|added:need((ROOT/p).is_file(),'Missing G05 modified/added file: '+p)
payload=manifest.get('payload',[])
need({v.get('path') for v in payload}==(changed|added)-{'research/p01-s04/g05-overlay-manifest.json'},'Manifest payload path list incomplete/extra')
for obj in payload:
    p=obj['path']
    if (ROOT/p).is_file():
        need(sha(p)==obj['sha256'] and (ROOT/p).stat().st_size==obj['sizeBytes'],'G05 overlay payload hash/size drift: '+p)
    need(obj['kind']==('ADDED' if p in added else 'MODIFIED'),'Wrong G05 payload kind: '+p)
protected=js('research/p01-s04/s03-protected-file-hashes.json')
for item in protected.get('files',[]):
    p=item['path']
    need((ROOT/p).is_file() and sha(p)==item['sha256'],'Protected S01-S03 research changed: '+p)
for immutable in ['research/p01-s04/g04-owner-approved-decisions.json',
                  'research/p01-s04/g04-overlay-manifest.json',
                  'research/p01-s04/g04-case-reconciliation.json',
                  'research/p01-s04/g04-falsification-reconciliation.json',
                  'docs/ontology/p01-stage-04-g04-closure-record.md',
                  'docs/ontology/p01-stage-04-g04-owner-approved-decisions.md',
                  'docs/ontology/p01-stage-04-g04-plan.md',
                  'research/p01-s04/normative-release-holds.json',
                  'research/p01-s04/source-authority-register.json']:
    need(immutable in files and sha(immutable)==files[immutable],'Original G04/source release artifacts altered: '+immutable)

# IMPORTANT: Legacy G01-G03 overlay vs checkpoint mismatches are inherited from
# the uploaded ZIP, not repaired, not newly introduced by G05. Transparently flag.
legacy=base.get('legacyHistoricalAttestationDiscrepancies',[])
need(len(legacy)==10 and all(x.get('path') in files or x.get('missingFromOwnerSource') is True for x in legacy),'Historical source discrepancy statement missing')
need(any(x.get('path')=='INFOPS-P01-S04-MERGE-NOTES.md' and x.get('missingFromOwnerSource') is True for x in legacy),'Original owner ZIP missing merge-note discrepancy not disclosed')
need(not (ROOT/'INFOPS-P01-S04-MERGE-NOTES.md').exists(), 'Original missing historical merge-note must not be forged by G05')

print('INFOPS G05 conditional research closure: 8/8 approved; programme total 49; D07 probes 16 unexecuted; C01-C36/F01-F16/S03-T01-T20 unchanged; G03-R01-R12 all OPEN; G06/G07 not started; G05 delta {} modified/{} added files; {} issue(s).'.format(len(changed),len(added),len(ISSUES)))
print('INHERITED BASELINE CAVEAT: original owner ZIP has 10 legacy G01-G03 overlay/checkpoint discrepancies, including a missing historic merge-note. No G05 change claims to repair or conceal them.')
for i in ISSUES:print('ERROR:',i)
sys.exit(1 if ISSUES else 0)
