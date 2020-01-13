#!/usr/bin/env python3
"""A15 bounded release verification; not an M16 conformance assessor.

Checks repository inventory/digests, authority locks, controlled release claims
and predecessor regression evidence. Default run does NOT execute A14 again.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MANIFEST = pathlib.Path('static/specs/hdip-cla/0.1/a15/a15-release-manifest.json')
REPORT = pathlib.Path('static/specs/hdip-cla/0.1/a15/a15-verification-report.json')
EXCLUDED = {str(MANIFEST), 'static/specs/hdip-cla/0.1/a15/a15-verification-report.json',
            'static/specs/hdip-cla/0.1/a15/a15-validation.json'}
PROGRAMME='docs/architecture/executable/hdip-cla-0.1-executable-programme.md'
SIDEBAR='sidebars.ts'
M17='docs/architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze.md'
BASE='static/specs/hdip-cla/0.1/'
LIMITATIONS=('INDEPENDENT_SHACL','FULL_OWL_ENTAILMENT','DOCUSAURUS_PRODUCTION_BUILD',
             'ACCOUNTABLE_M16_REALIZATION_ASSESSMENT','EXTERNAL_AUTHORITY_ATTESTATION')

def readj(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(data):return hashlib.sha256(data).hexdigest()
def deterministic(data):return json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
def safe_path(root,rel):
    if not isinstance(rel,str) or not rel or rel.startswith('/') or '\\' in rel or '\x00' in rel:
        raise ValueError('Unsafe relative path')
    p=pathlib.PurePosixPath(rel)
    if any(x in ('..','.') for x in p.parts) or str(p)!=rel:
        raise ValueError('Unsafe or noncanonical path')
    full=root/rel
    if full.is_symlink() or not full.is_file() or not full.resolve().is_relative_to(root.resolve()):
        raise ValueError('Missing or unsafe file')
    return full

def inventory_digest(items):
    # Path/content digest of included release files; excludes self-referential manifest and generated reports.
    return digest(deterministic(items).encode())

def repository_paths(root):
    ignored={'__pycache__','.git','node_modules','.docusaurus','build','.cache'}
    return sorted(p.relative_to(root).as_posix() for p in root.rglob('*')
                  if p.is_file() and not p.is_symlink() and not (set(p.relative_to(root).parts) & ignored))

def check(root, manifest, actual_override=None):
    findings=[]; checks=[]
    def gate(name,problems,detail=None):
        checks.append({'id':name,'status':'PASS' if not problems else 'FAIL',
                       'findings':problems[:20],'detail':detail or {}})
        findings.extend(name+': '+x for x in problems)
    problems=[]
    if manifest.get('releaseId')!='HDIP-CLA-0.1-EXECUTABLE-A15':problems.append('Unexpected release ID')
    if manifest.get('releaseVersion')!='0.1':problems.append('Unexpected version')
    if manifest.get('humanReadableAuthority')!='M17_FROZEN_HUMAN_READABLE':problems.append('Frozen M17 authority missing')
    if manifest.get('releaseDisposition')!='FORMALIZATION_PACKAGE_CLOSED_BOUNDED':problems.append('Incorrect bounded release disposition')
    if manifest.get('architectureConformance')!='NOT_ESTABLISHED' or manifest.get('machineAssignedM16Results')!=0:
        problems.append('Inadmissible automatic M16 conformance assertion')
    if manifest.get('externalApproval')!='NOT_ASSERTED' or manifest.get('productionPublicationApproval')!='NOT_ASSERTED':
        problems.append('Inadmissible external/publication approval assertion')
    if manifest.get('signedAttestation')!='NONE':problems.append('Unsigned release falsely signed')
    gate('AUTHORITY_AND_CLAIM_BOUNDARY',problems)

    records=manifest.get('files',[])
    problems=[]; paths=[r.get('path') for r in records if isinstance(r,dict)]
    if len(records)!=len(paths) or len(paths)!=len(set(paths)): problems.append('Duplicate/malformed file inventory')
    if set(paths)&EXCLUDED: problems.append('Self-referential report/manifest included')
    if set(manifest.get('inventoryExclusions',[]))!=EXCLUDED: problems.append('Unexpected inventory exclusions')
    if manifest.get('fileCount')!=len(paths):problems.append('Release fileCount mismatch')
    if manifest.get('inventorySha256')!=inventory_digest(records):problems.append('Release inventory root digest mismatch')
    observed=actual_override if actual_override is not None else repository_paths(root)
    if set(observed)!=set(paths)|EXCLUDED:
        problems.append('Unexpected missing/extra paths: missing='+str(len((set(paths)|EXCLUDED)-set(observed)))+
                        ' extra='+str(len(set(observed)-(set(paths)|EXCLUDED))))
    gate('COMPLETE_PACKAGE_INVENTORY',problems,{'hashedFileCount':len(records),'excludedCount':len(EXCLUDED)})

    problems=[]; passed=0
    for record in records:
        if not isinstance(record,dict):problems.append('Malformed inventory record');continue
        rel=record.get('path')
        try:
            f=safe_path(root,rel)
            contents=f.read_bytes()
            if digest(contents)!=record.get('sha256') or len(contents)!=record.get('bytes'):
                problems.append('Content digest/size mismatch: '+rel)
            else:passed+=1
        except (OSError,ValueError,TypeError) as e:problems.append('Unreadable/unsafe path: '+str(rel)+': '+str(e))
    gate('SHA256_CONTENT_INTEGRITY',problems,{'verifiedFiles':passed})

    problems=[]
    fingerprints={r['path']:r['sha256'] for r in records if isinstance(r,dict) and 'path' in r and 'sha256' in r}
    if fingerprints.get(M17)!=manifest.get('m17SourceSha256'):
        problems.append('Frozen M17 fingerprint not preserved')
    lock=manifest.get('a14Predecessor',{})
    previous=lock.get('immutableFiles',{})
    if len(previous)!=250:problems.append('Expected 250 unchanged A14 predecessor file fingerprints')
    for rel,h in previous.items():
        if rel in (PROGRAMME,SIDEBAR):problems.append('Mutable programme/sidebar path in predecessor lock')
        if fingerprints.get(rel)!=h:problems.append('A14 predecessor drift: '+rel)
    if set(lock.get('permittedChanges',[]))!={PROGRAMME,SIDEBAR}:
        problems.append('Unexpected predecessor change allowances')
    gate('FROZEN_AND_PREDECESSOR_AUTHORITY_LOCK',problems,{'lockedPredecessors':len(previous)})

    problems=[]
    a1=readj(root/(BASE+'a1/architecture-element-registry.json'))
    a2=readj(root/(BASE+'a2/relationship-traceability-registry.json'))
    a3=readj(root/(BASE+'a3/invariant-conformance-catalogue.json'))
    canonical={'a1Elements':len(a1['elements']),'a2Relationships':len(a2['relationships']),
             'a2Traceability':len(a2['traceabilityRecords']),'m16Invariants':len(a3['invariants'])}
    if canonical!={'a1Elements':209,'a2Relationships':911,'a2Traceability':332,'m16Invariants':48}:
        problems.append('Canonical A1–A3 identity/count drift')
    if manifest.get('canonicalCounts')!=canonical:problems.append('Manifest canonical count differs from source')
    gate('CANONICAL_COUNTS_AND_IDENTITY_PRESERVATION',problems,canonical)

    problems=[]
    reg=readj(root/(BASE+'a14/a14-regression-report.json'))
    if (reg.get('status')!='PASS_BOUNDED_REGRESSION' or reg.get('passedGates')!=10 or
        reg.get('totalGates')!=10 or reg.get('architectureConformance')!='NOT_ESTABLISHED' or
        reg.get('machineAssignedM16Results')!=0):problems.append('A14 stored regression evidence inconsistent')
    if manifest.get('a14RegressionEvidenceSha256')!=fingerprints.get(BASE+'a14/a14-regression-report.json'):
        problems.append('A14 regression evidence not bound to hashed package')
    gate('A14_REGRESSION_EVIDENCE_CHAIN',problems,{'storedGates':reg.get('passedGates')})

    problems=[]; obligations=manifest.get('outstandingVerification',[])
    byid={x.get('id'):x.get('status') for x in obligations if isinstance(x,dict)}
    if set(byid)!=set(LIMITATIONS) or len(obligations)!=5:problems.append('Outstanding verification register incomplete')
    if any(s in ('PASS','COMPLETE','ATTESTED','CERTIFIED','APPROVED') for s in byid.values()):
        problems.append('Unverified dependency incorrectly promoted')
    if manifest.get('releaseScope')!='SPECIFICATION_EXECUTABLE_FORMALIZATION':problems.append('Release scope drift')
    gate('UNRESOLVED_DEPENDENCIES_EXPLICIT',problems,{'openDependencies':len(obligations)})

    problems=[]
    programme=(root/PROGRAMME).read_text()
    sidebar=(root/SIDEBAR).read_text()
    if '**A15 — Executable 0.1 Release Closure** | **Complete' not in programme:problems.append('A15 not marked complete')
    if 'architecture/executable/hdip-cla-0.1-a15-executable-release-closure' not in sidebar:
        problems.append('A15 Docusaurus sidebar entry missing')
    if 'M17' not in programme:problems.append('Frozen human-readable authority missing from programme')
    gate('RELEASE_DOCUMENTATION_AND_NAVIGATION',problems)

    status='PASS_BOUNDED_RELEASE_INTEGRITY' if not findings else 'FAIL_RELEASE_INTEGRITY'
    return {'reportId':'HDIP-CLA-0.1-A15-VERIFICATION','status':status,
            'releaseDisposition':'FORMALIZATION_PACKAGE_CLOSED_BOUNDED' if not findings else 'NOT_CLOSED',
            'checksPassed':sum(x['status']=='PASS' for x in checks),'checksTotal':len(checks),
            'checks':checks,'findings':findings,
            'architectureConformance':'NOT_ESTABLISHED','machineAssignedM16Results':0,
            'externalApproval':'NOT_ASSERTED','productionPublicationApproval':'NOT_ASSERTED',
            'independentShaclProcessorRun':False,'fullOwlReasoningRun':False,
            'a14LiveRegressionExecutedByVerifier':False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=pathlib.Path,default=ROOT)
    ap.add_argument('--manifest',type=pathlib.Path,default=MANIFEST)
    ap.add_argument('--output',type=pathlib.Path)
    args=ap.parse_args()
    root=args.root.resolve()
    try:
        manifest=readj(root/args.manifest)
        report=check(root,manifest)
    except Exception as exc:
        report={'reportId':'HDIP-CLA-0.1-A15-VERIFICATION','status':'FAIL_RELEASE_INTEGRITY',
                'checksPassed':0,'checksTotal':7,'findings':[type(exc).__name__+': '+str(exc)],
                'architectureConformance':'NOT_ESTABLISHED'}
    payload=deterministic(report)
    if args.output:
        dest=args.output if args.output.is_absolute() else root/args.output
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(payload,encoding='utf-8')
    else:sys.stdout.write(payload)
    return 0 if report['status']=='PASS_BOUNDED_RELEASE_INTEGRITY' else 2
if __name__=='__main__':sys.exit(main())
