#!/usr/bin/env python3
"""A14 bounded counterfactual guards; modifications occur in memory only."""
import copy
import json
import pathlib
import unittest
import run_regression as r


class A14RegressionGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock=r.read_json(r.HERE/'a13-predecessor-lock.json')
        cls.a10=r.read_json(r.ROOT/r.BASE/'a10/positive-test-suite.json')
        cls.a12=r.read_json(r.ROOT/r.BASE/'a12/a12-execution-report.json')
        cls.a13=r.read_json(r.ROOT/r.BASE/'a13/a13-reconciliation-report.json')
        cls.a11=r.read_json(r.ROOT/r.BASE/'a11/a11-test-results.json')
        cls.a10results=r.read_json(r.ROOT/r.BASE/'a10/a10-validation.json')

    def test_01_lock_preserves_original_predecessor(self):
        self.assertEqual(r.predecessor_lock(r.ROOT,self.lock)['status'],'PASS')

    def test_02_lock_detects_frozen_m17_byte_drift(self):
        mutant=copy.deepcopy(self.lock)
        x=next(x for x in mutant['files'] if x['path'].endswith('m17-cross-artifact-reconciliation-freeze.md'))
        x['sha256']='0'*64
        d=r.predecessor_lock(r.ROOT,mutant)
        self.assertEqual(d['status'],'FAIL')
        self.assertTrue(any('PREDECESSOR_DRIFT' in s for s in d['findings']))

    def test_03_lock_detects_frozen_executable_schema_drift(self):
        mutant=copy.deepcopy(self.lock)
        x=next(x for x in mutant['files'] if x['path'].endswith('lifecycle-declaration.schema.json'))
        x['sha256']='f'*64
        self.assertEqual(r.predecessor_lock(r.ROOT,mutant)['status'],'FAIL')

    def test_04_lock_detects_duplicate_baseline_entry(self):
        mutant=copy.deepcopy(self.lock)
        mutant['files'][-1]=copy.deepcopy(mutant['files'][0])
        self.assertEqual(r.predecessor_lock(r.ROOT,mutant)['status'],'FAIL')

    def test_05_lock_rejects_path_traversal(self):
        mutant=copy.deepcopy(self.lock)
        mutant['files'][0]['path']='../../outside.md'
        d=r.predecessor_lock(r.ROOT,mutant)
        self.assertEqual(d['status'],'FAIL')
        self.assertTrue(any('UNSAFE' in s.upper() or 'unsafe' in s.lower() for s in d['findings']))

    def test_06_a10_pass_promotion_rejected(self):
        data={'results':[{'testId':'x'+str(i),'machineResult':'PASS_STRUCTURAL_ONLY','architectureConformance':'NOT_ESTABLISHED','errors':[]} for i in range(16)],'failed':0,'passed':16}
        self.assertFalse(r.validate_a10(data)[0])
        data['results'][0]['architectureConformance']='CONFORMANT'
        self.assertTrue(r.validate_a10(data)[0])

    def test_07_a11_indeterminate_promotion_rejected(self):
        data=copy.deepcopy(self.a11)
        self.assertFalse(r.validate_a11(data)[0])
        candidate=next(x for x in data['results'] if x['actualDisposition']=='INDETERMINATE_REVIEW_REQUIRED')
        candidate['m16InvariantResult']='SATISFIED'
        self.assertTrue(r.validate_a11(data)[0])

    def test_08_a11_violation_washing_rejected(self):
        data=copy.deepcopy(self.a11)
        data['results'][0]['actualDisposition']='INDETERMINATE_REVIEW_REQUIRED'
        self.assertTrue(r.validate_a11(data)[0])

    def test_09_a12_conformance_promotion_rejected(self):
        data=copy.deepcopy(self.a12)
        self.assertFalse(r.validate_a12(data)[0])
        data['architectureConformance']='CONFORMANT'
        self.assertTrue(r.validate_a12(data)[0])

    def test_10_a12_source_snapshot_tampering_detected(self):
        data=copy.deepcopy(self.a12)
        data['sourceSnapshotSha256']='0'*64
        self.assertTrue(r.validate_a12(data)[0])

    def test_11_a13_lost_assertions_detected(self):
        data=copy.deepcopy(self.a13)
        self.assertFalse(r.validate_a13(data)[0])
        data['gates'][0]['passed']-=1
        self.assertTrue(r.validate_a13(data)[0])

    def test_12_a13_missing_limitation_detected(self):
        data=copy.deepcopy(self.a13)
        data['limitations']=[x for x in data['limitations'] if x['id']!='LIM-SHACL']
        self.assertTrue(r.validate_a13(data)[0])

    def test_13_a13_m16_machine_outcome_rejected(self):
        data=copy.deepcopy(self.a13)
        data['machineAssignedM16Results']=48
        self.assertTrue(r.validate_a13(data)[0])

    def test_14_guard_output_never_claims_conformance(self):
        result=r.conformance_guard([r.gate('synthetic',[],1)])
        self.assertEqual(result['details']['implementationConformance'],'NOT_ESTABLISHED')
        self.assertEqual(result['details']['assignedInvariantResults'],0)

    def test_15_bad_runner_gate_not_silently_passed(self):
        result=r.conformance_guard([r.gate('synthetic',['prohibited counterexample'],1)])
        self.assertEqual(result['status'],'FAIL')

    def test_16_locked_paths_exempt_only_navigation(self):
        self.assertEqual(set(self.lock['exemptFromByteLock']),{r.PROGRAMME,r.SIDEBAR})
        self.assertTrue(all(x['path'] not in (r.PROGRAMME,r.SIDEBAR) for x in self.lock['files']))


if __name__=='__main__':unittest.main(verbosity=2)
