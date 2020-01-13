---
id: hdip-cla-0.1-a14-regression-suite
title: HDIP-CLA 0.1 A14 — Regression Suite
sidebar_label: A14 — Regression Suite
---

# HDIP-CLA 0.1 A14 — Regression Suite

**Stage:** A14 / complete  
**Baseline:** A13 cumulative repository  
**Source authority:** HDIP-CLA 0.1 M17 human-readable freeze  
**Executable suite:** `/specs/hdip-cla/0.1/a14/run_regression.py`  
**Policy:** `/specs/hdip-cla/0.1/a14/a14-regression-policy.json`  
**Evidence:** `/specs/hdip-cla/0.1/a14/a14-regression-report.json`

## 1. Purpose and limits

A14 is a **bounded cross-stage regression gate** over the frozen human-readable architecture and machine representations A1–A13. It catches known drift and tested classes of structural, semantic-representation, reference, historical-status and conformance-boundary defects. It does not automatically infer implementation conformance from test success.

```text
M17 human-readable authority > A1-A13 representations > A14 evidence
PASS_BOUNDED_REGRESSION != M16 CONFORMANT
PASS_BOUNDED_REGRESSION != semantic/Product/policy/Decision authority
```

All A14 execution verdicts concern **formalization integrity**. M16 HYBRID/ASSESSMENT remains subject to accountable architectural judgement; no M16 invariant becomes machine-SATISFIED because its metadata validates.

## 2. Source baseline and freezing

`a13-predecessor-lock.json` records SHA-256 of **243** files in the original A13 cumulative ZIP (245 files total). `sidebars.ts` and the executable programme status page are the only predecessor files intentionally changed by A14. The lock includes the original M01–M17 source documents, all A1–A13 registries, graphs, schemas, examples, runners, fixtures, evidence and source-led reconciler.

The lock is byte-exact and purposefully conservative. A harmless formatting change to a locked file also fails the regression until reviewed. A genuine source correction requires governed handling, not auto-updating the hash manifest. This is a provenance control **inside the package**, not a cryptographic third-party attestation or permission to modify frozen M17 architecture.

## 3. Integrated regression gates

| ID | Gate | Required result |
|---|---|---|
| 1 | A13 predecessor SHA-256 lock | 243 unchanged files |
| 2 | A10 positive test execution | 16/16 `PASS_STRUCTURAL_ONLY` |
| 3 | A11 negative/boundary execution | 54/54 expected dispositions, including 10 indeterminate cases |
| 4 | A12 integrated machine evidence | Five gates, validated snapshot digest, no M16 promotion |
| 5 | A13 source-led reconciliation | Seven gates, 1,715/1,715 assertions, zero defects |
| 6 | A8 positive/negative schema fixtures | Six positive acceptances, six negative rejections |
| 7 | A12 mutation/guard tests | 12 tests |
| 8 | A13 reconciliation mutation tests | 10 tests |
| 9 | A14 counterfactual guard tests | 16 tests |
| 10 | M16 machine-result boundary | Overall architectural conformance `NOT_ESTABLISHED` |

The A14 runner executes predecessor scripts from the checked-out repository and verifies their output semantics; it does not substitute stored green status documents for execution. Reports contain deterministic evidence, exit status and gate-specific findings, not a fabricated conformance certificate.

## 4. Counterfactual (mutation) coverage

The A14 16-test guard suite detects synthetic drift of frozen M17 bytes, A8 schema bytes, duplicate baseline entries, unsafe paths, A10 false `CONFORMANT` promotion, A11 erasure of indeterminacy, A12 false positive certification or corrupted source fingerprint, A13 missing assertions or missing verification limitations, and incorrect machine assignment of M16 outcomes. All mutations operate in memory; frozen files are never rewritten.

A12 and A13 guard suites remain separate and are rerun as part of A14. Thus successful unchanged-baseline tests are complemented by deliberately failing inputs that **must be detected**.

## 5. Run locally / in CI

From the repository root:

```bash
python static/specs/hdip-cla/0.1/a14/run_regression.py \
  --output static/specs/hdip-cla/0.1/a14/a14-regression-report.json
```

Dependencies: Python, `jsonschema`, `rdflib` (as already used by A12/A13). Return code `0` means all 10 bounded gates passed; nonzero (`2`) indicates failure/incompletion. The runner uses deterministic JSON output without a wall-clock timestamp. Unmodified inputs produce reproducible report bytes. CI should fail closed on missing dependencies or verification errors. No automated rebaseline mechanism exists.

Only the dedicated A14 report may be written within the source repository through the CLI; the runner does not overwrite frozen predecessor material.

## 6. Machine result versus M16 result

The runner uses `PASS_BOUNDED_REGRESSION` or `REGRESSION_FAILURE_OR_INCOMPLETE` as machine dispositions. It always reports:

```text
architectureConformance = NOT_ESTABLISHED
machineAssignedM16Results = 0
```

These are **not** additional invariant or overall M16 result states. `INDETERMINATE` applicability/evidence cases remain explicitly unresolved. There is no `CONDITIONALLY_CONFORMANT` workaround, waiver-to-pass, or implicit certification from platform technology, lifecycle, Product registry presence or Profile use.

## 7. Open verification dependencies for A15

- An **independent SHACL engine** has not certified A6 shapes; local subset checks are bounded.
- Full OWL entailment reasoning has not been independently demonstrated.
- Docusaurus production build has not been run as part of A14.
- Realization-specific M16 assessment, HYBRID/ASSESSMENT adjudication and accountable sign-off are outside the machine boundary.
- External semantic, Product-family, policy and Decision authority attestation is outside this executable programme.

These cannot be silently marked complete in A15. Release closure should distinguish executable packaging/traceability from governance/publication/certification.

## 8. Completion boundary

A14 is complete when the frozen A13 predecessor inventory is retained, the integrated 10-gate runner passes, all counterfactual guards pass, any exceptions/limitations are explicit, and the overlay contains only A14 additions plus allowed programme/sidebar edits. A14 completes **regression instrumentation**, not authority transfer or real-system conformance.
