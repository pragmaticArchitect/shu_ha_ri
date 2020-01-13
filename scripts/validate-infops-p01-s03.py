#!/usr/bin/env python3
"""Validate S03 research traceability only. NEVER certify INFOPS Productness/family or PMDD."""
from pathlib import Path
import hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'research/p01-s03'
issues=[]
def expect(condition, message):
    if not condition: issues.append(message)
def load(file):
    path=RES/file
    if not path.is_file():
        issues.append('Missing S03 research file '+file)
        return {}
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        issues.append(f'Invalid JSON {file}: {exc}')
        return {}

rules=load('candidate-rules.json')
cases=load('case-evaluations.json')
analogy=load('teaching-analogy.json')
decisions=load('review-decisions.json')
integrity=load('baseline-integrity.json')
state=json.loads((ROOT/'static/spec/infops/0.1/scaffold-state.json').read_text(encoding='utf-8'))

for label,obj,key in [('rules',rules,'rules'),('cases',cases,'cases'),('analogy',analogy,'elements'),('decisions',decisions,'decisions')]:
    expect(obj.get('project')=='INFOPS',f'{label}: wrong project')
    expect(obj.get('stage')=='P01-S03',f'{label}: stage mismatch')
    expect(obj.get('normative') is False,f'{label}: normative must be false')
    expect(obj.get('ownerAccepted') is False,f'{label}: owner acceptance must be false')
    expect(obj.get('qualificationDecisionsIssued') is False,f'{label}: cannot issue Product qualification decisions')
    expect(obj.get('actualProductsQualified')==0,f'{label}: cannot claim real qualified Products')
    expect(obj.get('count')==len(obj.get(key,[])),f'{label}: count mismatch')

rule_ids=[r['id'] for r in rules.get('rules',[])]
expect(rule_ids==[f'Q{x}' for x in range(6)],'Q0..Q5 candidate rules must exist in order')
expect(rules.get('conditionalConjunction')==[f'Q{x}' for x in range(5)],'Candidate conjunction must be Q0-Q4 only')
expect(rules.get('adjudicationGate')=='Q5','Competing-family gate Q5 must stay distinct from ontology predicates')
expect(rules.get('jointSufficiency')=='NOT_ESTABLISHED','Joint sufficiency cannot be claimed')
for r in rules.get('rules',[]):
    expect(r.get('jointSufficiencyProven') is False,f'Rule {r["id"]}: cannot be proven sufficient')
    expect(bool(r.get('authority') and r.get('question') and r.get('nonQualifiers')),f'Rule {r["id"]}: missing scope/evidence')
expect((rules.get('rules') or [{}])[0].get('authority')=='BPS/PIN','Productness authority must remain BPS')
expect((rules.get('rules') or [{}])[-1].get('kind')=='REVIEW_ADJUDICATION_GATE_NOT_ONTOLOGICAL_PROPERTY','Q5 must be a review gate')

S02=json.loads((ROOT/'research/p01-s02/cases.json').read_text(encoding='utf-8'))
s02ids={c['caseId'] for c in S02['cases']}
caseids=[c['caseId'] for c in cases.get('cases',[])]
expect(caseids==[f'S03-T{x:02d}' for x in range(1,21)],'S03-T01..20 case IDs expected')
allowed={'PRODUCTNESS_UNESTABLISHED','PROVISIONAL_INFORMATION_MATCH','COMPETING_FAMILY_PLAUSIBLE','CONFLICT_REVIEW','CANDIDATE_CONDITION_NOT_MET','INSUFFICIENT_EVIDENCE','REALIZATION_INVARIANCE_CONDITIONAL','SEMANTIC_CHANGE_REVIEW'}
covered=set()
for c in cases.get('cases',[]):
    cid=c['caseId']
    expect(c.get('researchDisposition') in allowed,f'{cid}: illegal disposition')
    expect(c.get('qualificationIssued') is False,f'{cid}: cannot certify qualification')
    expect(bool(c.get('hypotheticalSubject') and c.get('neededEvidence')),f'{cid}: missing subject/evidence')
    expect(bool(c.get('sourceCaseIds') and c.get('linkedRules')),f'{cid}: missing trace refs')
    for q in c.get('linkedRules',[]):
        expect(q in rule_ids, f'{cid}: unknown rule {q}')
        covered.add(q)
    for src in c.get('sourceCaseIds',[]): expect(src in s02ids,f'{cid}: unknown S02 case {src}')
expect(covered==set(rule_ids),'All Q0-Q5 must be challenged by casework')
expect(len(set(c['researchDisposition'] for c in cases.get('cases',[])))>=6,'Cases should include substantial conflict/uncertainty cases')
expect(sum(c['researchDisposition']=='PROVISIONAL_INFORMATION_MATCH' for c in cases.get('cases',[]))>=2,'No provisional positive research controls')
expect(sum(c['researchDisposition']=='CONFLICT_REVIEW' for c in cases.get('cases',[]))>=2,'No competing-family conflict controls')

ids=[d['decisionId'] for d in decisions.get('decisions',[])]
expect(ids==[f'S03-D{x:02d}' for x in range(1,10)],'S03-D01..D09 expected')
expect(all(d.get('state')=='PROPOSED' and d.get('ownerAccepted') is False for d in decisions.get('decisions',[])), 'Owner decisions must all remain proposed')
expect(len(decisions.get('outstandingGates',[]))>=6,'Missing explicit S04 open gates')

expected_analogy=['Data','Curated Data','Information','Knowledge','Intelligence']
expect([e['term'] for e in analogy.get('elements',[])]==expected_analogy,'Preserve five original KivaNura teaching terms')
expect(analogy.get('usage')=='INFORMATIVE_TEACHING_ONLY','Analogy must not be normative')
expect(len(analogy.get('notNormativeGuardrails',[]))>=8,'Analogy guardrails missing')
analogy_md=ROOT/'docs/foundations/crude-oil-to-driver-teaching-analogy.md'
expect(analogy_md.is_file(),'Teaching analogy Markdown missing')
if analogy_md.is_file():
    atxt=analogy_md.read_text(encoding='utf-8')
    for label in ('Crude oil','Refined oil','Fuel in motion','Roadmap and manual','Driver or pilot','NON-NORMATIVE'):
        expect(label.lower() in atxt.lower(),f'Analogy missing original/refinement {label}')
    expect('not a' in atxt.lower(),'Teaching status disclaimer absent')

expected_new=[
 'docs/ontology/p01-stage-03-candidate-qualification-rules.md',
 'docs/ontology/p01-stage-03-decision-procedure.md',
 'docs/ontology/p01-stage-03-boundary-casework.md',
 'docs/ontology/p01-stage-03-pfi-semantic-invariance.md',
 'docs/ontology/p01-stage-03-review-decisions.md',
 'docs/foundations/crude-oil-to-driver-teaching-analogy.md'
]
for doc in expected_new:
    path=ROOT/doc
    expect(path.is_file(),f'Missing S03 document {doc}')
    if path.is_file():
        content=path.read_text(encoding='utf-8').lower()
        expect('non-normative' in content or 'not normative' in content,f'S03 document missing research status: {doc}')
expect(cases.get('count')==20,'Expected 20 S03 casework records')

expect(state.get('p01Stage')=='S03_CANDIDATE_QUALIFICATION','S03 site status mismatch')
expect(state.get('releaseStatus')=='P01_STAGE_03_DRAFT','S03 release status mismatch')
for flag in ['normative','stageAccepted','qualifiedInformationProductRulesPublished','jointSufficiencyEstablished','ownerAccepted']:
    expect(state.get(flag) is False,f'Forbidden positive release/qualification state: {flag}')
expect(state.get('stage3ResearchOnly') is True,'S03 must be research only')
package=json.loads((ROOT/'package.json').read_text(encoding='utf-8'))
expect(package.get('overrides',{}).get('webpack')=='5.99.9','Netlify/Webpack fix missing')
expect(package.get('dependencies',{}).get('@docusaurus/core')=='3.9.2','Docusaurus baseline altered')

expect(integrity.get('normative') is False and integrity.get('stage')=='P01-S03','Baseline integrity manifest mislabeled')
for rel,want_hash in integrity.get('sha256',{}).items():
    path=ROOT/rel
    expect(path.is_file(),f'Preserved S01/S02 source removed: {rel}')
    if path.is_file():
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        expect(actual==want_hash,f'S01/S02 source unexpectedly changed: {rel}')
expect(len(integrity.get('sha256',{}))>=12,'Not enough baseline S01/S02 preservation hashes')

print(f'INFOPS P01-S03 research validation: {len(rule_ids)} candidate rules, {len(caseids)} hypothetical cases, {len(analogy.get("elements",[]))} analogy elements, {len(ids)} proposed decisions, {len(integrity.get("sha256",{}))} prior source hashes; {len(issues)} issue(s)')
for i in issues: print('ERROR:',i)
print('NOTE: S03 validation checks research consistency only: NO Product qualification, approval, normative release or live PFI test was conducted.')
sys.exit(1 if issues else 0)
