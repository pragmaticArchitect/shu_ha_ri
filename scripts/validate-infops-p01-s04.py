#!/usr/bin/env python3
"""Validate S04 owner-review research overlays. NOT Product, conformance or publication certification."""
from pathlib import Path
import hashlib,json,sys,re

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research/p01-s04'
ISSUES=[]
def need(condition,msg):
    if not condition:ISSUES.append(msg)
def read(name):
    p=R/name
    if not p.is_file():
        ISSUES.append('Missing S04 research artifact '+name)
        return {}
    try:return json.loads(p.read_text(encoding='utf-8'))
    except Exception as exc:
        ISSUES.append(f'Bad S04 JSON {name}: {exc}')
        return {}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

state=read('research-state.json')
decisions=read('owner-decision-register.json')
upstream=read('s02-s03-owner-approvals.json')
sources=read('source-authority-register.json')
holds=read('normative-release-holds.json')
g04=read('g04-proposed-owner-review-sequence.json')
protected=read('s03-protected-file-hashes.json')
reconciliation=read('baseline-reconciliation.json')
manifest=read('overlay-manifest.json')

for tag,x in [('state',state),('decisions',decisions),('sources',sources)]:
    need(x.get('project')=='INFOPS',tag+' wrong project')
    need(x.get('normative') is False,tag+' must remain non-normative')
need(state.get('stage')=='P01-S04','wrong S04 stage')
need(state.get('ownerReviewedResearchDecisionsTotal')==32,'wrong reviewed S04 decision count')
need(state.get('explicitApprovalsWithResearchSummaryAvailable')==32,'S02/S03 approval summaries not recorded for all 32 S04 owner-reviewed decisions')
need(state.get('s02OwnerApprovedResearchDecisions')==6 and state.get('s03OwnerApprovedResearchDecisions')==9,'S02/S03 approval counts must be 6+9')
need(state.get('g01OwnerApprovedAntecedentDecisions')==15 and state.get('g01ClosureBasisVerifiedFromOwnerRegister') is True,'G01 closure must be supported by explicitly approved S02/S03 decisions')
need(state.get('actualProductsQualified')==0,'S04 cannot qualify real Products')
for marker in ['normative','upstreamSourcePinsAdopted','informationFamilyNecessaryAndSufficientProven','infoprodNormative','infopdsNormative','dppCoreAdopted','informationDppProfileNormative','hdipArchitectureConformanceCertified','productMaturityOrPMDDGranted','publicationAuthorized']:
    need(state.get(marker) is False,marker+' must be false')
need(state.get('gates',{}).get('G03')=='CLOSED_CONDITIONAL_RESEARCH','G03 must have conditional research closure')
need(state.get('gates',{}).get('G04')=='PREPARED_NOT_STARTED','G04 must remain unapproved')

G=decisions.get('gates',[])
need([x.get('gate') for x in G]==['G01','G02','G03','G04','G05','G06','G07'],'Unexpected S04 gate order')
if len(G)==7:
    g01,g02,g03,g4=G[:4]
    need(g01.get('ownerReviewedCount')==15 and g01.get('approvedCount')==15,'G01 must record fifteen approved S02/S03 antecedents')
    need(g01.get('individualDispositionBreakdownAvailable') is True,'G01 approved antecedent dispositions must be present')
    need(g01.get('granularVerbatimAvailableInThisArchive') is False,'Full G01 deliberations must not be fabricated')
    need(not g01.get('granularDetails'),'Do not invent separate G01-Fxx finding details')
    need(g01.get('closureBasis')=='S02_S03_OWNER_APPROVALS_15','Missing S02/S03 closure basis')
    need(len(g01.get('ownerApprovedAntecedentDecisions',[]))==15,'Expected fifteen G01 approved antecedent decisions')
    need(g02.get('ownerReviewedCount')==7 and g02.get('approvedCount')==7,'G02 count incorrect')
    need([d.get('id') for d in g02.get('decisions',[])]==[f'G02-Q{x}' for x in range(6)]+['G02-X01'],'G02 Q0..Q5/X01 missing')
    need(all(d.get('disposition')=='APPROVED' and d.get('normative') is False for d in g02.get('decisions',[])),'G02 must be research approved')
    need(g03.get('ownerReviewedCount')==10 and g03.get('approvedCount')==10,'G03 count incorrect')
    need([d.get('id') for d in g03.get('decisions',[])]==['G03-D01']+[f'G03-D{x:02d}-F01' for x in range(2,11)],'G03 D01..D10 IDs mismatch')
    need(g03.get('decisions',[{}])[0].get('disposition')=='APPROVED_AS_AMENDED','G03 D01 must preserve owner amendment')
    need(all(d.get('normative') is False for d in g03.get('decisions',[])),'G03 must be non-normative')
    need(g03.get('sourcePinsAdopted') is False and g03.get('normativeAdoptionReady') is False,'G03 cannot promote sources')
    need(g4.get('ownerReviewedCount')==0 and g4.get('approvedCount')==0,'G04 not yet reviewed')

# Subsequent owner-approved research dispositions over historical proposed S02/S03 snapshots.
need(upstream.get('project')=='INFOPS' and upstream.get('normative') is False, 'Owner approval ledger must be INFOPS research only')
need(upstream.get('approvedTotal')==15 and upstream.get('ownerReviewedRefinementsIncorporated') is True, 'Wrong owner-approved S02/S03 basis')
need(upstream.get('normativeQualificationAuthorized') is False and upstream.get('sourceVersionsAdopted') is False, 'S02/S03 approvals cannot authorize norms')
need(upstream.get('actualProductsQualified')==0, 'Owner approvals cannot certify Products')
need(upstream.get('g01ClosureRelation',{}).get('count')==15 and upstream.get('g01ClosureRelation',{}).get('countedOnceInG01') is True, 'G01 closure must count 15 approvals exactly once')
expectedIDs=[f'S02-D{i:02d}' for i in range(1,7)]+[f'S03-D{i:02d}' for i in range(1,10)]
approvals=[v for group in upstream.get('stages',[]) for v in group.get('decisions',[])]
need([v.get('id') for v in approvals]==expectedIDs, 'Missing/misordered owner approval IDs')
need(all(v.get('disposition')=='APPROVED' and v.get('normative') is False and v.get('reviewedRefinementsIncorporated') is True for v in approvals), 'Every S02/S03 approved finding must remain research-only')
need(all(v.get('ownerApprovedResearchPosition') and v.get('originalResearchProposal') for v in approvals), 'Approved summaries and historic proposals must be retained')
need([v.get('id') for v in G[0].get('ownerApprovedAntecedentDecisions',[])]==expectedIDs, 'G01 owner register must agree with S02/S03 approval ledger')
need([v.get('ownerApprovedResearchPosition') for v in G[0].get('ownerApprovedAntecedentDecisions',[])]==[v.get('ownerApprovedResearchPosition') for v in approvals], 'G01 owner summary provenance mismatch')
need(decisions.get('ownerReviewedResearchCount')==32 and decisions.get('explicitApprovalsWithResearchSummaryAvailable')==32, 'S04 aggregate review count mismatch')
for stage,src in [('S02','research/p01-s02/research-decisions.json'),('S03','research/p01-s03/review-decisions.json')]:
    doc=json.loads((ROOT/src).read_text(encoding='utf-8'))
    need(doc.get('ownerAccepted') is False and all(v.get('state')=='PROPOSED' for v in doc.get('decisions',[])), f'Historical {stage} proposal snapshot must remain unchanged')
for page in ['p01-stage-02-owner-approved-decisions.md','p01-stage-03-owner-approved-decisions.md','p01-stage-04-g01-closure-basis.md']:
    f=ROOT/'docs/ontology'/page
    need(f.is_file() and f.read_text(encoding='utf-8').startswith('---\n'), f'Missing Docusaurus owner approval addendum {page}')
    need("'ontology/"+page.removesuffix('.md')+"'" in (ROOT/'sidebars.js').read_text(encoding='utf-8'), f'Owner approval addendum missing from sidebar {page}')
for idx,stage in enumerate(['S02','S03']):
    loc=ROOT/f'research/p01-{stage.lower()}/owner-approval-addendum.json'
    need(loc.is_file(),f'Missing {stage} owner approval addendum')
    if loc.is_file():
        local=json.loads(loc.read_text(encoding='utf-8'))
        need(local.get('normative') is False and local.get('g01ClosureBasis') is True, f'{stage} owner approval addendum overclaims authority')
        need(local.get('decisions')==upstream.get('stages',[{},{}])[idx].get('decisions'), f'{stage} addendum must match canonical S04 owner approval register')
for v in approvals:
    page=ROOT/'docs/ontology'/('p01-stage-02-owner-approved-decisions.md' if v['id'].startswith('S02') else 'p01-stage-03-owner-approved-decisions.md')
    need(v['id'] in page.read_text(encoding='utf-8') and v['ownerApprovedResearchPosition'] in page.read_text(encoding='utf-8'), 'Approval not correctly rendered: '+v['id'])

S=sources.get('sources',[])
need(len(S)==17 and [z.get('id') for z in S]==[f'S{x:02d}' for x in range(1,18)],'Expected S01..S17 sources')
need(all(z.get('adoptedByINFOPS') is False and z.get('canonicalRevisionVerified') is False for z in S),'S04 source pins must not claim adoption')
need(sources.get('sourcePinsAdopted') is False,'S04 source authority register must be candidate only')
need({z['id']:z.get('source') for z in S}.get('S14')=='INFOPROD','S14 must be INFOPROD')
need({z['id']:z.get('source') for z in S}.get('S15')=='INFOPDS','S15 must be INFOPDS')
need({z['id']:z.get('source') for z in S}.get('S16')=='BPS DPP Core','S16 must be BPS DPP')
need({z['id']:z.get('source') for z in S}.get('S17')=='Information Product DPP Profile','S17 must be Information DPP Profile')

H=holds.get('holds',[])
need(len(H)==12 and [z.get('id') for z in H]==[f'G03-R{x:02d}' for x in range(1,13)],'Expected 12 G03 R01..R12 holds')
need(all(z.get('resolved') is False for z in H),'Release holds cannot be silently resolved')
need(holds.get('normativeAdoptionReady') is False,'Normative adoption not ready')
need(holds.get('canContinueConditionalResearch') is True,'Conditional research should remain available')

P=g04.get('dispositions',[])
need([z.get('id') for z in P]==[f'G04-D{x:02d}' for x in range(1,10)],'Proposed G04 D01..D09 sequence missing')
need(all(z.get('approved') is False and z.get('ownerDisposition')=='NOT_REQUESTED' for z in P),'No G04 owner decisions may be invented')
need(g04.get('status')=='PROPOSED_NOT_APPROVED' and g04.get('normative') is False,'G04 must remain research proposal')

pages=['p01-stage-04-overview.md','p01-stage-04-owner-decisions.md','p01-stage-04-source-authorities.md','p01-stage-04-artifact-boundaries.md','p01-stage-04-release-holds.md','p01-stage-04-g04-plan.md']
for p in pages:
    f=ROOT/'docs/ontology'/p
    need(f.is_file(),f'Missing S04 documentation {p}')
    if f.is_file():
        doc=f.read_text(encoding='utf-8')
        need(doc.startswith('---\n') and '\n---\n' in doc[4:],f'{p}: Docusaurus frontmatter required')
sidebar=(ROOT/'sidebars.js').read_text(encoding='utf-8')
for p in pages:
    need("'ontology/"+p.removesuffix('.md')+"'" in sidebar,f'Sidebar missing {p}')
for marker in ['INFOPROD','INFOPDS','DPP','HPD']:
    need(marker in (ROOT/'docs/ontology/p01-stage-04-artifact-boundaries.md').read_text(encoding='utf-8'),f'Artifact distinction missing {marker}')

# Owner-uploaded baseline reconciliation and checksum attestation.
need(reconciliation.get('sourceArchive')=='INFOPS.zip','Owner-uploaded source archive missing')
need(reconciliation.get('sourceZipTopDirectory')=='shu_ha_ri/','Unexpected owner archive root')
need(reconciliation.get('sourceFileCount')==60,'Expected 60 owner-uploaded baseline files')
need(reconciliation.get('ownerFilesPreservedExceptListedAttestations') is True,'Owner source preservation not recorded')
need(reconciliation.get('s02s03ResearchFilesModified') is False,'Earlier research content must be preserved')
need(len(reconciliation.get('userBaselineVsPriorS03',{}).get('contentDifferences',[]))==1,'Unexpected S02/S03 differences')
for source in reconciliation.get('userBaselineVsPriorS03',{}).get('contentDifferences',[]):
    subject=ROOT/source.get('path','')
    need(subject.is_file() and sha(subject)==source.get('ownerUploadedSha256'), 'User baseline semantic source checksum drift')
    priorIntegrity=json.loads((ROOT/'research/p01-s03/baseline-integrity.json').read_text(encoding='utf-8'))
    need(priorIntegrity.get('sha256',{}).get(source['path'])==source.get('ownerUploadedSha256'), 'S03 baseline integrity attestation not reconciled')
need(manifest.get('baselineArchive')=='INFOPS.zip','S04 manifest must target owner-uploaded archive')
need(manifest.get('sourceZipTopDirectory')=='shu_ha_ri/','S04 manifest wrong source root')
need(manifest.get('baselineFileCount')==60,'S04 manifest wrong original file count')
newfiles=manifest.get('payloadFilesExcludingThisManifest',[])
need(len(newfiles)==manifest.get('addedFiles',0)+manifest.get('modifiedFiles',0)-1,'Manifest payload count inconsistent')
for item in newfiles:
    p=ROOT/item['path']
    need(p.is_file(),'S04 manifest payload absent: '+item['path'])
    if p.is_file():
        need(sha(p)==item['sha256'],'S04 manifest payload hash mismatch: '+item['path'])
        need(p.stat().st_size==item['sizeBytes'],'S04 manifest payload size mismatch: '+item['path'])

original=read('s03-protected-file-hashes.json')
F=original.get('files',[])
need(original.get('protectedFileCount')==len(F) and len(F)>=20,'Insufficient S01-S03 original-source protection')
for obj in F:
    p=ROOT/obj['path']
    if not p.is_file():ISSUES.append('S01/S02/S03 protected file missing '+obj['path'])
    elif sha(p)!=obj['sha256']:ISSUES.append('S01/S02/S03 protected file changed '+obj['path'])

old=json.loads((ROOT/'static/spec/infops/0.1/scaffold-state.json').read_text(encoding='utf-8'))
need(old.get('releaseStatus')=='P01_STAGE_03_DRAFT' and old.get('stageAccepted') is False, 'Historical S03 scaffold release marker must remain unmodified')
need(old.get('normative') is False,'Historical stage cannot become normative')

print(f'INFOPS P01-S04 current owner approvals: {len(approvals)} S02/S03 approved research decisions forming G01 closure; G01-G03 32 decisions; {len(S)} source entries, {len(H)} release holds, {len(P)} unapproved G04 items, {len(F)} protected prior files; {len(ISSUES)} issue(s)')
for i in ISSUES:print('ERROR:',i)
sys.exit(1 if ISSUES else 0)
