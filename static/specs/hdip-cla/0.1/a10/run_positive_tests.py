#!/usr/bin/env python3
"""A10 positive structural test runner. No M16 conformance result is asserted."""
import json,sys,pathlib,collections
from jsonschema import Draft202012Validator

def main():
    repo=pathlib.Path(__file__).resolve().parents[5]
    a9=repo/'static/specs/hdip-cla/0.1/a9'
    here=pathlib.Path(__file__).resolve().parent
    suite=json.loads((here/'positive-test-suite.json').read_text())
    corpus=json.loads((a9/'example-corpus.json').read_text())
    a1=json.loads((repo/'static/specs/hdip-cla/0.1/a1/architecture-element-registry.json').read_text())
    def deep_ids(obj):
        if isinstance(obj,dict):
            for k,v in obj.items():
                if k in ('id','elementId','canonicalId') and isinstance(v,str): yield v
                yield from deep_ids(v)
        elif isinstance(obj,list):
            for v in obj:yield from deep_ids(v)
    ids=set(deep_ids(a1)); records=a1.get('elements',[])
    if len(ids)<209:
        ids=set()
        for e in records:ids.add(e.get('id',e.get('elementId')))
    results=[]
    for case in suite['cases']:
        errors=[]
        try:
            if case['type']=='SCENARIO_DECLARATION_SET':
                m=json.loads((repo/case['manifestPath']).read_text())
                if m['exampleId']!=case['scenarioId']:errors.append('scenario ID mismatch')
                if m.get('assessmentStatus')!='NOT_ASSESSED' or m.get('claimOutcome')!='INDETERMINATE':errors.append('invalid architecture-claim boundary')
                if m.get('normativeStatus')!='ILLUSTRATIVE_ONLY':errors.append('example falsely normative')
                for key in ('m12InteractionRefs','m13BoundaryRefs','m15FlowRefs'):
                    for ref in m.get(key,[]):
                        if ref not in ids:errors.append('unresolved '+key+': '+ref)
                for key in ('m14ProfileRef','m14RealizationPatternRef'):
                    if m.get(key) and m[key] not in ids:errors.append('unresolved '+key+': '+m[key])
                for dec in case['declarations']:
                    schema=json.loads((repo/dec['schemaPath']).read_text())
                    Draft202012Validator.check_schema(schema)
                    data=json.loads((repo/dec['path']).read_text())
                    errors += [dec['path']+': '+e.message for e in Draft202012Validator(schema).iter_errors(data)]
            else:
                code=case['check']; manifests=[json.loads((a9/e['path']).read_text()) for e in corpus['examples']]
                if code=='M15_FLOW_COVERAGE':
                    covered={v for m in manifests for v in m['m15FlowRefs']}
                    missing={f'M15-FLOW-{n:02d}' for n in range(1,11)}-covered
                    if missing:errors.append('missing flows: '+str(sorted(missing)))
                elif code=='A8_SCHEMA_REGISTRY':
                    used={d['kind'] for m in manifests for d in m['declarations']}
                    expected={p.name.removesuffix('.schema.json') for p in (repo/'static/specs/hdip-cla/0.1/a8').glob('*.schema.json')}
                    if used!=expected:errors.append('declaration type coverage mismatch: '+str(sorted(expected-used)))
                elif code=='A1_REFERENCE_RESOLUTION':
                    for m in manifests:
                        for key in ('m12InteractionRefs','m13BoundaryRefs','m15FlowRefs'):
                            for ref in m.get(key,[]):
                                if ref not in ids:errors.append('unresolved '+ref)
                        for key in ('m14ProfileRef','m14RealizationPatternRef'):
                            if m.get(key) and m[key] not in ids:errors.append('unresolved '+m[key])
                elif code=='M16_ASSESSMENT_BOUNDARY':
                    for m in manifests:
                        if m.get('claimOutcome')!='INDETERMINATE' or m.get('assessmentStatus')!='NOT_ASSESSED':errors.append('promoted conformance claim: '+m['exampleId'])
                    for entry in suite['cases']:
                        if entry['expected']['architectureConformance']!='NOT_ESTABLISHED':errors.append('promoted test outcome')
                elif code=='M17_AUTHORITY_PRESERVATION':
                    for m in manifests:
                        if m.get('normativeStatus')!='ILLUSTRATIVE_ONLY':errors.append('unfrozen example: '+m['exampleId'])
                    if suite['sourceAuthority']!='HDIP-CLA-0.1-M17':errors.append('authority mismatch')
                else:errors.append('unknown check code '+code)
        except Exception as exc:errors.append(type(exc).__name__+': '+str(exc))
        results.append({'testId':case['testId'],'machineResult':'PASS_STRUCTURAL_ONLY' if not errors else 'FAIL','architectureConformance':'NOT_ESTABLISHED','errors':errors})
    report={'suiteId':suite['suiteId'],'caseCount':len(results),'passed':sum(x['machineResult']=='PASS_STRUCTURAL_ONLY' for x in results),'failed':sum(x['machineResult']!='PASS_STRUCTURAL_ONLY' for x in results),'m16Conformance':'NOT_ASSESSED','results':results}
    print(json.dumps(report,indent=2))
    return 0 if report['failed']==0 else 1
if __name__=='__main__':sys.exit(main())
