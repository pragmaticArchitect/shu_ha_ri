---
id: hdip-cla-0.1-a10-positive-conformance-tests
title: HDIP-CLA 0.1 A10 — Positive Conformance Tests
sidebar_label: A10 — Positive Conformance Tests
---

# HDIP-CLA 0.1 — A10 Positive Conformance Tests

**Status:** COMPLETE (bounded structural-test coverage)  
**Frozen authority:** M17 human-readable baseline  
**Sources:** A1–A9, notably A8 schemas and A9 illustrative corpus  
**Machine inputs:** `/specs/hdip-cla/0.1/a10/positive-test-suite.json`  
**Execution:** `python static/specs/hdip-cla/0.1/a10/run_positive_tests.py` (requires `jsonschema`)

## 1. Purpose and authority

A10 demonstrates **positive, safely decidable tests** on machine-readable declaration and reference artifacts. It does not prove that an actual HDIP product, Profile, platform, deployment, access arrangement, AI model, consequential action or subject conforms to HDIP-CLA. M17 always has semantic precedence. All A9 scenarios remain *illustrative only*.

A10 test names use the programme label *Positive Conformance Tests*, but a positive machine assertion is only `PASS_STRUCTURAL_ONLY`. A10 deliberately does not emit M16 `SATISFIED` or overall `CONFORMANT`; it preserves the separate M16 vocabulary rather than redefining it. No score or positive conditional conformance exists.

## 2. Scope

The suite contains 16 positive test cases: 11 scenario declaration-set tests, one for each A9 scenario, and 5 cross-corpus structural tests. It checks A8 JSON Schema Draft 2020-12 validation, A1 reference resolution for scenario-level M12/M13/M14/M15 references, M15 flow coverage, declaration-type coverage, and the prohibition of implied certification. Each scenario has an explicit `NOT_ASSESSED` + `INDETERMINATE` illustrative claim boundary.

An A9 schema may permit broader data than a canonical realisation would: a PASS therefore proves only the stated structural assertions, never their real-world applicability, evidence sufficiency, or authority correctness.

## 3. Evaluation semantics

| A10 evaluation field | Meaning |
|---|---|
| `PASS_STRUCTURAL_ONLY` | Declared A10 machine checks passed on the supplied artifacts. |
| `FAIL` | One or more declared tests failed; no architectural inference follows. |
| `ERROR` | Reserved for orchestration failures in future execution. |
| `architectureConformance: NOT_ESTABLISHED` | No M16 outcome has been assessed or established by A10. |

A10 is **not** a positive M16 invariant-by-invariant evaluation engine. The 7 STRUCTURAL, 37 HYBRID and 4 ASSESSMENT modes frozen by M16 remain unchanged. Where machine-checkable evidence supports a HYBRID invariant, it still does not exhaust the accountable architecture judgement. NOT_APPLICABLE cannot be inferred from missing declarations; a governed scope rationale is required in later conformance assessment.

## 4. Corpus coverage

| Test ID | Source | Expected machine result |
|---|---|---|
| POS-001–POS-011 | A9-01 through A9-11 manifests and 35 A8 declarations | `PASS_STRUCTURAL_ONLY` |
| POS-012 | Coverage of M15-FLOW-01 through -10 | `PASS_STRUCTURAL_ONLY` |
| POS-013 | All six A8 schema declaration types used | `PASS_STRUCTURAL_ONLY` |
| POS-014 | A1 identity resolution for scenario references | `PASS_STRUCTURAL_ONLY` |
| POS-015 | No A9/example claim promotion | `PASS_STRUCTURAL_ONLY` |
| POS-016 | M17 source authority and illustrative status | `PASS_STRUCTURAL_ONLY` |

Data PDEP Stage 0–10 is not universalised to Information/Intelligence/Compound. SSCF is a logical lifecycle, not eight synchronous hops. CEP is Consumer Experience Projection, not a Plane. M12 logical interaction contracts are not APIs. External authority boundaries and Productness are not proven by a schema. Profile declaration and Realization binding are not equivalent to conformance. Historical evidence is not overwritten by reassessment.

## 5. Evidence and reproducibility

- `positive-test-suite.json` — machine-addressable bounded expectations.
- `run_positive_tests.py` — executable positive test harness.
- `a10-validation.json` — observed results, reproducibility details and preservation checks.

A10 is intentionally prior to A11 negative/boundary corpus, A12 generalized conformance runner, A13 reconciliation and A14 regression. A10's local fault-injection probe tests rejection of malformed schema fields but does not replace those future stages. This release does not claim Docusaurus build success or independent SHACL engine testing.

## 6. Frozen fidelity

This stage introduces zero new canonical Planes, Overlays, ABBs, Registries, M12 interactions, M13 Boundary Families, M14 Patterns, M15 Views/Flows or M16 invariants. A10 tests record assertions about existing artifacts rather than invent new normative interpretation. All prior files are byte-preserved except the expected executable programme document and `sidebars.ts` edits.
