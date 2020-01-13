---
id: hdip-cla-0.1-a11-negative-boundary-test-cases
title: HDIP-CLA 0.1 A11 — Negative / Boundary Test Cases
sidebar_label: A11 — Negative / Boundary Tests
---

# HDIP-CLA 0.1 A11 — Negative / Boundary Test Cases

**Status:** COMPLETE — test corpus and isolated runner  
**Architectural authority:** frozen M01–M17 (M16 invariant/conformance baseline; M17 precedence)  
**Dependencies:** A1–A10, particularly A7/A8 schemas, A9 corpus and A10 bounded testing discipline  
**Machine suite:** `/specs/hdip-cla/0.1/a11/negative-boundary-test-suite.json`  
**Test runner:** `/specs/hdip-cla/0.1/a11/run_negative_boundary_tests.py`

## 1. Intent and non-authority

A11 supplies deliberately invalid and deliberately ambiguous **illustrative test inputs** so that future A12 evaluation can distinguish rejected formalizations from inconclusive real-world architectural assessments. A test input is not a new canonical HDIP construct, specification requirement, real implementation finding or certificate.

M17 human-readable authority always wins. A11 must not fill absent evidence by invented certainty or silently declare M16 invariants `SATISFIED` or `VIOLATED` based only on this synthetic corpus.

## 2. Three bounded machine dispositions

| A11 machine disposition | Meaning | Not established |
|---|---|---|
| `MACHINE_REJECTED` | A mutated JSON document violates an existing A7/A8 schema or explicit cross-registry / A9 manifest constraint | Whether an external implementation violates a core M16 invariant |
| `FLAGGED_DECLARED_CONTRADICTION` | An explicit *synthetic* claim contradicts an identifiable frozen architectural distinction | That any real-world implementation actually makes the claim |
| `INDETERMINATE_REVIEW_REQUIRED` | A structurally or declaratively compatible record leaves material judgement/evidence unresolved | A positive or negative M16 invariant result |

A11 records `m16InvariantResult = NOT_EVALUATED` and `overallConformance = NOT_ESTABLISHED` for **all** cases. These are suite reporting fields, not additions to the frozen M16 enumerations. The only M16 invariant result values remain `SATISFIED`, `VIOLATED`, `INDETERMINATE`, `NOT_APPLICABLE`, and only overall outcomes `CONFORMANT`, `NONCONFORMANT`, `INDETERMINATE` when an actual bounded M16 assessment is performed.

## 3. Test coverage

The suite covers malformed A1/A2/A3/A5 machine documents; PDEP and SSCF scope; M12 logical contracts; M13 external and consequential-action boundaries; M14 Profiles; CEP identity; realization mappings; referential integrity; non-normative A9 claim boundaries; obvious declared authority/semantic assertions; historical truth; version/currentness; Productness; and evidence/judgement insufficiency.

Tests are grouped into six fixture categories: `SCHEMA_NEGATIVE`, `REFERENCE_NEGATIVE`, `MANIFEST_GUARD`, `EXPLICIT_CONTRADICTION`, `SHACL_SUBSET_NEGATIVE`, and `EVIDENCE_BOUNDARY`. The suite index and fixtures are under `/specs/hdip-cla/0.1/a11/`. Fixtures use JSON-pointer mutations of unchanged predecessor files or scoped synthetic assertions rather than maintaining diverging copies of the canonical sources.

The local SHACL subset evaluator is **not** an independent SHACL processor and implements only the A6 shapes actually in the repository (cardinality, datatype and IRI node-kind tests).

## 4. Interpretation rules

- An A7/A8 schema reject is proof of a schema-level problem in the **mutated test document**, not a platform non-conformance finding.
- Unresolved A1 or external-identity reference is a machine-checkable model-integrity defect *within the fixture*. Explicit external authorities remain separate from A1 canonical architecture identities.
- A deliberately asserted contradiction (for example, `PRODUCT_ACCESS_CONFERS_DECISION_AUTHORIZATION`) is flagged as inconsistent with frozen M16/M17 meaning. It does not assert that such a contradiction exists outside the fixture.
- HYBRID/ASSESSMENT evidence gaps must remain indeterminate until an accountable assessment; missing evidence is not proof of compliance, nor automatically proof of architectural violation.
- `NOT_APPLICABLE` requires a bounded applicability rationale and acceptance. An unreviewed claim cannot bypass an invariant.
- Conformance does not transfer from a supplier, registry, Product family, hosting topology or adjacent specification.
- Later assessment must preserve the historical meaning and as-of governing versions of prior occurrences.
- The Data PDEP Stage 0–10 specialization must not be universalized to Information or Intelligence Products; SSCF is not a mandatory synchronous runtime pipeline.

## 5. Runner scope and reproducibility

From the repository root:

```bash
python static/specs/hdip-cla/0.1/a11/run_negative_boundary_tests.py --output static/specs/hdip-cla/0.1/a11/a11-test-results.json
```

The test runner applies each declared mutation **in memory**, uses existing A7/A8 JSON Schemas with Draft 2020-12, checks selected A1/A2/A9 reference assertions, evaluates three pre-existing A6 negative Turtle fixtures with a small local SHACL Core property-constraint subset, and flags only enumerated synthetic contradiction markers. It does not run a general M16 conformance engine and does not mutate the predecessor source documents. `jsonschema` and `rdflib` are runtime dependencies. An independent pySHACL engine and actual architecture judgement are outside A11.

## 6. Handoff to A12

A12 can consume A10 and A11 test suites, reuse the bounded diagnostic vocabulary, introduce robust runner versioning, publish evidence and reject unknown conditions without silently classifying them. Do not convert A11 synthetic fixture outcomes into live M16 conformance determinations. Preserve positive/negative/boundary test separation and real-subject evidence scope.
