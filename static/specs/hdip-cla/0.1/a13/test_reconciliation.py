#!/usr/bin/env python3
"""Mutation/guard tests for A13. All synthetic changes remain in memory."""
import copy
import json
import unittest
from rdflib import Graph
import run_reconciliation as r

class ReconciliationGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m17=r.read(r.M17);cls.m16=r.read(r.M16)
        cls.a1=r.load(r.path('a1','architecture-element-registry.json'))
        cls.a2=r.load(r.path('a2','relationship-traceability-registry.json'))
        cls.a3=r.load(r.path('a3','invariant-conformance-catalogue.json'))
        cls.policy=r.load(r.path('a5','canonical-iri-policy.json'))
        cls.g=Graph();cls.g.parse(str(r.file(r.path('a5','canonical-architecture-graph.ttl'))),format='turtle')

    def assertDefect(self, result, checkId):
        self.assertEqual(result['status'],'DEFECTS_FOUND')
        self.assertIn(checkId,[f['id'] for f in result['findings']])

    def test_01_clean_m17(self):
        self.assertEqual(r.frozen_inventory(self.m17,self.a1)['status'],'PASS')

    def test_02_bad_plane_inventory_detected(self):
        a=copy.deepcopy(self.a1)
        a['elements']=[e for e in a['elements'] if e['id']!='HDIP-P5']
        self.assertDefect(r.frozen_inventory(self.m17,a),'M17_COUNT_PLANE')

    def test_03_freeze_source_count_drift_detected(self):
        mutated=self.m17.replace('**5** — HDIP-P1..P5','**6** — HDIP-P1..P5',1)
        self.assertNotEqual(mutated,self.m17)
        self.assertDefect(r.frozen_inventory(mutated,self.a1),'M17_COUNT_PLANE')

    def test_04_m16_condition_rewrite_detected(self):
        a=copy.deepcopy(self.a3)
        a['invariants'][0]['canonicalCondition']='This is a prohibited replacement condition.'
        self.assertDefect(r.invariant_reconciliation(self.m16,self.a1,self.a2,a),'M16_EXACT_TEXT_M16-I01')

    def test_05_mode_drift_detected(self):
        a=copy.deepcopy(self.a3)
        a['invariants'][0]['assessmentMode']='STRUCTURAL'
        self.assertDefect(r.invariant_reconciliation(self.m16,self.a1,self.a2,a),'M16_MODE_DISTRIBUTION')

    def test_06_a2_graph_target_divergence_detected(self):
        a=copy.deepcopy(self.a2)
        a['relationships'][0]['target']='HDIP-P1'
        result,g=r.graph_reconciliation(self.a1,a,self.a3,self.policy)
        self.assertDefect(result,'A2_DIRECT_AND_REIFIED_HDIP-CLA-A2-REL-0001')

    def test_07_a3_graph_condition_divergence_detected(self):
        a=copy.deepcopy(self.a3)
        a['invariants'][0]['canonicalCondition']='synthetic erroneous condition'
        result,g=r.graph_reconciliation(self.a1,self.a2,a,self.policy)
        self.assertDefect(result,'A3_INVARIANT_GRAPH_M16-I01')

    def test_08_historical_scope_preserved(self):
        scope,token=r.identity_scope('HIST::COVP','A1_ELEMENT')
        self.assertEqual((scope,token),('historical','HIST::COVP'))
        self.assertEqual(r.compatible_authority(self.a1,self.a2,self.a3,self.m17)['status'],'PASS')

    def test_09_no_positive_conformance_outcome(self):
        self.assertEqual(set(x['token'] for x in self.a3['overallOutcomes']),
                         {'CONFORMANT','NONCONFORMANT','INDETERMINATE'})
        self.assertEqual(r.corpus_and_runner()['status'],'PASS')

    def test_10_provisional_base_cannot_become_canonical(self):
        a=copy.deepcopy(self.policy)
        a['canonicalBase']='urn:invalid:'
        self.assertDefect(r.rdf_migration(a,self.g),'A5_CANONICAL_BASE')

if __name__=='__main__':unittest.main(verbosity=2)
