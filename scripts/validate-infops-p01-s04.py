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
need(state.get('explicitApprovalsWithResearchSummaryAvailable')==17,'wrong supported S04 approval count')
need(state.get('actualProductsQualified')==0,'S04 cannot qualify real Products')
for marker in ['normative','upstreamSourcePinsAdopted','informationFamilyNecessaryAndSufficientProven','infoprodNormative','infopdsNormative','dppCoreAdopted','informationDppProfileNormative','hdipArchitectureConformanceCertified','productMaturityOrPMDDGranted','publicationAuthorized']:
    need(state.get(marker) is False,marker+' must be false')
need(state.get('gates',{}).get('G03')=='CLOSED_CONDITIONAL_RESEARCH','G03 must have conditional research closure')
need(state.get('gates',{}).get('G04')=='PREPARED_NOT_STARTED','G04 must remain unapproved')

G=decisions.get('gates',[])
need([x.get('gate') for x in G]==['G01','G02','G03','G04','G05','G06','G07'],'Unexpected S04 gate order')
if len(G)==7:
    g01,g02,g03,g4=G[:4]
    need(g01.get('ownerReviewedCount')==15 and g01.get('approvedCount') is None,'G01 review count/disposition provenance incorrect')
    need(g01.get('individualDispositionBreakdownAvailable') is False,'Do not invent G01 dispositions')
    need(g01.get('granularVerbatimAvailableInThisArchive') is False,'G01 verbatim provenance cannot be asserted')
    need(not g01.get('granularDetails'),'Do not invent unavailable G01 finding details')
    need(g02.get('ownerReviewedCount')==7 and g02.get('approvedCount')==7,'G02 count incorrect')
    need([d.get('id') for d in g02.get('decisions',[])]==[f'G02-Q{x}' for x in range(6)]+['G02-X01'],'G02 Q0..Q5/X01 missing')
    need(all(d.get('disposition')=='APPROVED' and d.get('normative') is False for d in g02.get('decisions',[])),'G02 must be research approved')
    need(g03.get('ownerReviewedCount')==10 and g03.get('approvedCount')==10,'G03 count incorrect')
    need([d.get('id') for d in g03.get('decisions',[])]==['G03-D01']+[f'G03-D{x:02d}-F01' for x in range(2,11)],'G03 D01..D10 IDs mismatch')
    need(g03.get('decisions',[{}])[0].get('disposition')=='APPROVED_AS_AMENDED','G03 D01 must preserve owner amendment')
    need(all(d.get('normative') is False for d in g03.get('decisions',[])),'G03 must be non-normative')
    need(g03.get('sourcePinsAdopted') is False and g03.get('normativeAdoptionReady') is False,'G03 cannot promote sources')
    need(g4.get('ownerReviewedCount')==0 and g4.get('approvedCount')==0,'G04 not yet reviewed')

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

print(f'INFOPS P01-S04 owner-reviewed research: {len(S)} source entries, {len(H)} release holds, {len(P)} proposed G04 items, {len(F)} protected prior files; {len(ISSUES)} issue(s)')
for i in ISSUES:print('ERROR:',i)
sys.exit(1 if ISSUES else 0)
