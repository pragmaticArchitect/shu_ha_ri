#!/usr/bin/env python3
"""Bounded local guards for A15 package verifier; never change source files."""
import copy
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch
import run_release_verification as rv

ROOT=rv.ROOT
BASE=rv.readj(ROOT/rv.MANIFEST)

class ReleaseGuards(unittest.TestCase):
    def evaluate(self,modifier=None):
        x=copy.deepcopy(BASE)
        if modifier:modifier(x)
        return rv.check(ROOT,x)
    def assertRejected(self,report,gate=None):
        self.assertEqual(report['status'],'FAIL_RELEASE_INTEGRITY')
        if gate:
            self.assertEqual(next(x for x in report['checks'] if x['id']==gate)['status'],'FAIL')

    def test_01_clean_package_passes(self):
        x=self.evaluate()
        self.assertEqual(x['status'],'PASS_BOUNDED_RELEASE_INTEGRITY')
        self.assertEqual(x['checksPassed'],8)
        self.assertEqual(x['architectureConformance'],'NOT_ESTABLISHED')

    def test_02_machine_cannot_claim_conformant(self):
        self.assertRejected(self.evaluate(lambda m:m.update(architectureConformance='CONFORMANT')),'AUTHORITY_AND_CLAIM_BOUNDARY')

    def test_03_release_is_not_governance_approval(self):
        self.assertRejected(self.evaluate(lambda m:m.update(productionPublicationApproval='APPROVED')),'AUTHORITY_AND_CLAIM_BOUNDARY')

    def test_04_release_disposition_cannot_be_overstated(self):
        self.assertRejected(self.evaluate(lambda m:m.update(releaseDisposition='CERTIFIED')),'AUTHORITY_AND_CLAIM_BOUNDARY')

    def test_05_manifest_root_detects_inventory_mutation(self):
        self.assertRejected(self.evaluate(lambda m:m['files'][0].update(bytes=42)),'COMPLETE_PACKAGE_INVENTORY')

    def test_06_pred_lock_requires_exact_identity(self):
        self.assertRejected(self.evaluate(lambda m:m['a14Predecessor']['immutableFiles'].update({rv.M17:'deadbeef'})),
                            'FROZEN_AND_PREDECESSOR_AUTHORITY_LOCK')

    def test_07_open_verification_dependencies_cannot_disappear(self):
        self.assertRejected(self.evaluate(lambda m:m['outstandingVerification'].pop()),'UNRESOLVED_DEPENDENCIES_EXPLICIT')

    def test_08_historical_authority_fingerprint_protected(self):
        self.assertRejected(self.evaluate(lambda m:m.update(m17SourceSha256='deadbeef')),
                            'FROZEN_AND_PREDECESSOR_AUTHORITY_LOCK')

    def test_09_inventory_paths_cannot_escape_repo(self):
        def modify(m):
            m['files'][0]['path']='../../outside'
            m['inventorySha256']=rv.inventory_digest(m['files'])
        self.assertRejected(self.evaluate(modify),'SHA256_CONTENT_INTEGRITY')

    def test_10_actual_tampered_bytes_detected(self):
        target=BASE['files'][0]['path']
        real=rv.safe_path
        with tempfile.TemporaryDirectory() as td:
            tampered=pathlib.Path(td)/'tampered.txt'
            tampered.write_bytes(b'counterfactual-invalid-file')
            def intercept(root,rel):return tampered if rel==target else real(root,rel)
            with patch.object(rv,'safe_path',side_effect=intercept):
                self.assertRejected(self.evaluate(),'SHA256_CONTENT_INTEGRITY')

    def test_11_manifest_exclusion_drift_detected(self):
        self.assertRejected(self.evaluate(lambda m:m['inventoryExclusions'].pop()),'COMPLETE_PACKAGE_INVENTORY')

    def test_12_unverified_dependency_cannot_be_marked_pass(self):
        self.assertRejected(self.evaluate(lambda m:m['outstandingVerification'][0].update(status='PASS')),
                            'UNRESOLVED_DEPENDENCIES_EXPLICIT')

if __name__=='__main__': unittest.main(verbosity=2)
