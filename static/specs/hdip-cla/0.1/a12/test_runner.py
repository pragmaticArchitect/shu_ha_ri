#!/usr/bin/env python3
"""A12 test probes: validate failure handling, judgement boundary, and intake triage."""
import copy, importlib.util, json, pathlib, unittest
from unittest.mock import patch
HERE=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('hdip_a12_runner',HERE/'run_conformance.py')
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)

class A12GuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue=runner.load(f'{runner.BASE}/a3/invariant-conformance-catalogue.json')
        cls.partial=json.loads((HERE/'fixtures/partial-review-required.json').read_text())
    def test_partial_review_stays_indeterminate(self):
        result=runner.triage(self.partial,self.catalogue)
        self.assertEqual(result['status'],'REVIEW_REQUIRED')
        self.assertEqual(result['missingCount'],46)
        self.assertEqual(result['verifiedOverall'],'NOT_ESTABLISHED')
        self.assertEqual(result['machineAssignedM16Results'],0)
    def test_incompatible_applicability_is_rejected(self):
        invalid=json.loads((HERE/'fixtures/invalid-undetermined-satisfied.json').read_text())
        result=runner.triage(invalid,self.catalogue)
        self.assertIn('APPLICABILITY_RESULT_CONFLICT',[x['code'] for x in result['issues']])
        self.assertEqual(result['verifiedOverall'],'NOT_ESTABLISHED')
    def test_unsupported_declared_conformance_flag(self):
        candidate=copy.deepcopy(self.partial);candidate['declaredOutcome']='CONFORMANT'
        r=runner.triage(candidate,self.catalogue)
        self.assertIn('UNSUPPORTED_DECLARED_CONFORMANCE',[x['code'] for x in r['issues']])
    def test_duplicate_invariant_flag(self):
        candidate=copy.deepcopy(self.partial)
        candidate['invariantAssessments'].append(copy.deepcopy(candidate['invariantAssessments'][0]))
        r=runner.triage(candidate,self.catalogue)
        self.assertIn('DUPLICATE_INVARIANT',[x['code'] for x in r['issues']])
    def test_not_applicable_requires_accepted_rationale(self):
        candidate=copy.deepcopy(self.partial)
        candidate['invariantAssessments'][0].update(applicability='NOT_APPLICABLE',result='NOT_APPLICABLE')
        r=runner.triage(candidate,self.catalogue)
        self.assertIn('UNJUSTIFIED_NOT_APPLICABLE',[x['code'] for x in r['issues']])
    def test_hybrid_requires_judgement_and_evidence(self):
        candidate=copy.deepcopy(self.partial)
        candidate['invariantAssessments'][0].update(applicability='APPLICABLE',result='SATISFIED')
        r=runner.triage(candidate,self.catalogue)
        codes={x['code'] for x in r['issues']}
        self.assertTrue({'ACCOUNTABLE_JUDGEMENT_MISSING','DETERMINATE_EVIDENCE_MISSING'}<=codes)
    def test_bad_token_rejected_by_schema(self):
        candidate=copy.deepcopy(self.partial);candidate['invariantAssessments'][0]['result']='AUTOMATIC_PASS'
        self.assertEqual(runner.triage(candidate,self.catalogue)['status'],'INVALID_INTAKE')
    def test_out_of_order_history_flag(self):
        candidate=copy.deepcopy(self.partial)
        candidate['historyEvents']=[
            {'eventId':'e2','eventType':'supersession','effectiveAt':'2026-10-14T00:00:00Z','evidenceRef':'ref-2'},
            {'eventId':'e1','eventType':'initial','effectiveAt':'2026-10-13T00:00:00Z','evidenceRef':'ref-1'}]
        r=runner.triage(candidate,self.catalogue)
        self.assertIn('NON_MONOTONIC_HISTORY',[x['code'] for x in r['issues']])
    def test_a10_counterfactual_mismatch_fails(self):
        report=json.loads((HERE/'a12-execution-report.json').read_text())
        baseline=next(c for c in report['checks'] if c['id']=='A10_POSITIVE_TESTS')
        fabricated={'results':copy.deepcopy(baseline['results']),'failed':0,'passed':16}
        fabricated['results'][0]['machineResult']='FAIL'
        with patch.object(runner,'subprocess_report',return_value=(0,fabricated)):
            self.assertEqual(runner.positive()['result'],'FAIL')
    def test_a11_counterfactual_mismatch_fails(self):
        report=json.loads((HERE/'a12-execution-report.json').read_text())
        baseline=next(c for c in report['checks'] if c['id']=='A11_NEGATIVE_BOUNDARY_TESTS')
        fabricated={'results':copy.deepcopy(baseline['results']),'matched':54,'mismatched':0}
        fabricated['results'][0]['actualDisposition']='INDETERMINATE_REVIEW_REQUIRED'
        with patch.object(runner,'subprocess_report',return_value=(0,fabricated)):
            self.assertEqual(runner.negative()['result'],'FAIL')
    def test_no_real_world_certification_from_suite_success(self):
        report=json.loads((HERE/'a12-execution-report.json').read_text())
        self.assertEqual(report['machineGate'],'PASS')
        self.assertEqual(report['architectureConformance'],'NOT_ESTABLISHED')
        self.assertEqual(report['machineAssignedM16Results'],0)
        self.assertFalse(report['independentSHACLProcessorRun'])
    def test_deterministic_source_fingerprint(self):
        report=json.loads((HERE/'a12-execution-report.json').read_text())
        import hashlib
        material=json.dumps(report['sourceHashes'],sort_keys=True,separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(material).hexdigest(),report['sourceSnapshotSha256'])

if __name__=='__main__':unittest.main(verbosity=2)
