---
id: hdip-cla-0.1-a12-automated-conformance-runner
title: HDIP-CLA 0.1 A12 - Automated Conformance Runner
sidebar_label: A12 - Automated Conformance Runner
---

# HDIP-CLA 0.1 A12 — Automated Conformance Runner

**Status:** COMPLETE — bounded formalization-evidence automation; **not** M16 architectural certification  
**Human-readable authority:** M01–M17, frozen at M17  
**Predecessor:** completed A11 cumulative repository  
**Primary executable:** `/specs/hdip-cla/0.1/a12/run_conformance.py`  
**Execution report:** `/specs/hdip-cla/0.1/a12/a12-execution-report.json`

## 1. Purpose and authority boundary

A12 provides a **reproducible, evidence-producing machine test runner** over the *already established* A1–A11 formalization. It accepts optional human-supplied M16 assessment metadata for completeness and consistency triage. It does not silently take over architectural, semantic, Product, Data, enterprise-policy or Decision authority.

```text
M17 human-readable authority
   > A1–A11 representation and tests
   > A12 evidence/orchestration

Machine gate PASS
   != M16 invariant SATISFIED
   != HDIP-CLA overall CONFORMANT
   != external specification conformance
   != certification
```

No machine-assigned invariant-level `SATISFIED`, `VIOLATED`, `NOT_APPLICABLE` or overall `CONFORMANT`, `NONCONFORMANT`, `INDETERMINATE` determination is produced from the tests. `NOT_ESTABLISHED` is a **runner evidence-boundary marker**, not a fourth M16 overall outcome. `NOT_EVALUATED` is similarly a test-reporting term, not a fifth M16 invariant result.

## 2. Five machine gates

| Gate | Source | What a machine PASS proves | What it does **not** prove |
|---|---|---|---|
| A1/A2/A3 integrity | Real registries | Frozen inventory cardinality, duplicate checks, resolvable relevant identifiers, assessment-mode distribution | Accuracy of real implementation or enterprise authority |
| A7 document schemas | Six existing canonical JSON/JSON-LD documents | Those documents satisfy existing A7 structural schemas | All runtime semantics or M16 invariants |
| A5 graph + A6 local subset | Canonical RDF Turtle/JSON-LD + A6 shapes | Both graphs are isomorphic with 13,727 triples; the implemented A6 local shape subset reports no defects | Independent SHACL standards conformance, OWL inference validity or architectural certification |
| A10 positive regression | Existing A10 suite and runner | 16/16 expected bounded positive structural results | That any illustrative A9 example is a conformant realization |
| A11 negative/boundary regression | Existing A11 suite and runner | 54/54 expected test dispositions (33 machine rejections, 11 synthetic contradiction flags, 10 indeterminate boundaries) | That a synthetic violation has occurred in an actual deployment |

Tests run against **actual repository files**, not rekeyed paraphrases of the frozen constructs. A12 does not alter the older runners or fixtures. The prior SHACL subset is explicitly reused; an independent SHACL engine remains an unmet verification dependency.

## 3. Result vocabularies are kept separate

**A12 machine gate:** `PASS`, `FAIL`, `ERROR`. These mean execution/structural test success, contradiction or execution error only.

**A10 machine test:** `PASS_STRUCTURAL_ONLY` or failure. **A11 fixture results:** `MACHINE_REJECTED`, `FLAGGED_DECLARED_CONTRADICTION`, `INDETERMINATE_REVIEW_REQUIRED`. These are synthetic test diagnostic dispositions.

**M16 invariant results** remain exactly: `SATISFIED`, `VIOLATED`, `INDETERMINATE`, `NOT_APPLICABLE`. **M16 overall outcomes** remain exactly: `CONFORMANT`, `NONCONFORMANT`, `INDETERMINATE`. No `CONDITIONALLY_CONFORMANT` state is introduced.

## 4. Optional assessment-intake boundary

The separate `assessment-intake.schema.json` validates a bounded submitted record with subject/version, class, claim type, scoped baseline, assessor identifier, assessment version/time and zero-to-48 specific invariant records. Partial evidence is allowed only as **review intake**, never positive conformance.

The triage layer checks:

- A3-defined invariant identity, result and applicability combinations; duplicate or missing assessments;
- mandatory accepted rationale for `NOT_APPLICABLE`, evidence for determinate results and judgement metadata for HYBRID/ASSESSMENT determinate results;
- inconsistency between **submitted** overall declarations and missing, unresolved or demonstrably violated records;
- Profile context for non-Core claims, event ordering and duplicate historical event identifiers.

It does **not** authenticate the assessor, verify evidence contents, approve NA justifications, prove completion of the 18 Conformance Evidence Package dimensions, establish Profile conformance, validate actual runtime behaviour or reconstruct full historical chain-of-custody from a supplied prior digest. Even an input declaring all 48 invariants `SATISFIED` cannot be promoted to machine-certified `CONFORMANT`.

The optional intake report carries `declaredOutcomeUnverified` as **submitted data**, and `verifiedOverall` remains `NOT_ESTABLISHED`.

## 5. Reproducible execution and provenance

From the repository root (Python 3.10+ with `jsonschema` and `rdflib`):

```bash
python static/specs/hdip-cla/0.1/a12/run_conformance.py \
  --output static/specs/hdip-cla/0.1/a12/a12-execution-report.json
```

For a review-only human assessment draft:

```bash
python static/specs/hdip-cla/0.1/a12/run_conformance.py \
  --assessment static/specs/hdip-cla/0.1/a12/fixtures/partial-review-required.json \
  --strict-review \
  --output /tmp/hdip-cla-a12-review.json
```

`--strict-review` exits **3** when human review remains outstanding; malformed or inconsistent submitted intake exits **4**; machine-gate failure exits **2**; otherwise **0**. A successful default machine run exits 0 **only** for machine evidence, never for architectural certification.

Each report includes the SHA-256 of all tracked consumed source artifacts and a deterministic snapshot fingerprint. Historical source files are read-only; prior assessments are not overwritten. The report intentionally omits the current wall-clock time to support byte-for-byte repeatability on unchanged sources; external storage should separately timestamp and sign the resulting evidence record if needed.

## 6. Package structure

```text
docs/architecture/executable/
  hdip-cla-0.1-a12-automated-conformance-runner.md

static/specs/hdip-cla/0.1/a12/
  run_conformance.py
  test_runner.py
  runner-policy.json
  assessment-intake.schema.json
  a12-execution-report.json
  a12-validation.json
  fixtures/
    partial-review-required.json
    invalid-undetermined-satisfied.json
```

The step-specific overlay includes **only** A12-added files plus updates to `docs/architecture/executable/hdip-cla-0.1-executable-programme.md` and `sidebars.ts`; the cumulative ZIP includes all predecessor files.

## 7. Known limitations / A13–A15 hand-off

1. A12 is intentionally a **bounded machine-evidence runner**, not a general M16 certification service.
2. Independent SHACL validation was not available; A6 local subset is narrower than a standards processor.
3. Assessment input is not cryptographically signed or checked against enterprise authorities; claimed evidence and review metadata remain external.
4. Application, deployment, policy, provider and runtime claims are not inspected directly.
5. A12 does not assert full cross-artifact reconciliation (A13), regression closure (A14), final executable release closure (A15) or Docusaurus build success.

**A12 complete** when its five machine gates and its judgement-boundary/fault-injection tests pass, repository SHA-256 preservation is verified, and both the A12-only overlay and cumulative repository ZIP are published.
