---
id: hdip-cla-0.1-a13-cross-artifact-reconciliation
title: HDIP-CLA 0.1 A13 - Cross-Artifact Reconciliation
sidebar_label: A13 - Cross-Artifact Reconciliation
---

# HDIP-CLA 0.1 A13 — Cross-Artifact Reconciliation

**Status:** COMPLETE — bounded machine-readable reconciliation; **not** an M16 conformance certification  
**Authoritative human-readable baseline:** M01–M17, frozen at M17  
**Predecessor:** A12 cumulative repository  
**Machine report:** `/specs/hdip-cla/0.1/a13/a13-reconciliation-report.json`  
**Runner:** `/specs/hdip-cla/0.1/a13/run_reconciliation.py`

## 1. Purpose and jurisdiction

A13 reconciles *representations of the frozen architecture*, not its meaning. If the executable artifacts and M17/M16 disagree, classify the difference as a **formalization defect**; do not silently correct the human-readable authority or introduce another architecture identity.

```text
Frozen M17 architecture meaning
       > A1/A2/A3 source-indexed representation
       > A4/A5 RDF and IRI serialization
       > A6/A7/A8 structural contracts
       > A9-A12 illustrative corpus and bounded test evidence
       > A13 reconciliation report
```

A13 is not a new semantic, Product, Data, policy, Decision or Profile authority. It neither certifies a Realization nor creates an alternative set of M16 invariant/result states. A machine PASS is limited to assertions that the reconciliation runner actually evaluates.

## 2. Source-led method

A13 retains and examines the preceding repository without rewriting it:

1. Read the **M17 frozen inventory section** and reconcile canonical IDs/counts with A1 element kinds. Verify Plane/Overlay/ABB identities, PDEP Data specialization and SSCF stage cardinalities, and CEP identity.
2. Read each **M16 invariant table row** and compare exact identifier, name, normative condition and assessment mode against A3; compare M04 ancestry against A2 and A1.
3. Verify the **A1, A2 and A3 RDF projections**: 209 A1 resource identifiers, 911 direct/reified A2 relationships, 332 reified A2 traceability assertions and 48 A3 invariant conditions/modes against A5 RDF.
4. Translate A4 provisional resources using the **A5 migration map** and verify graph isomorphism with the canonical A5 graph. Check canonical Turtle/JSON-LD/N-Triples equivalence without redefining authority or requiring `owl:sameAs`.
5. Validate existing A7 JSON schemas, A8 positive declaration fixtures and the parseability of A6 shape graph. The prior A6 local SHACL subset is re-run via A12; this is **not independent SHACL conformance**.
6. Reconcile A9 illustrative corpus and M15 flow coverage; re-run the A12 machine gates including A10/A11 regression and check the result boundary.
7. Preserve M17 historical/compatibility traceability, external-authority scoping, non-transitivity and the absence of a positive conditional conformance state.

The script uses real repository sources. Its generated report contains a deterministic SHA-256 source manifest and enumerated pass/failure check IDs.

## 3. Seven reconciliation gates

| Gate | Asserted surface | What PASS establishes |
|---|---|---|
| `FROZEN_M17_INVENTORY` | M17/A1 | Source-led canonical identities, cardinalities, stage and topology separations |
| `M16_A1_A2_A3_CONFORMANCE_SEMANTICS` | M16/A1/A2/A3 | Exact invariant text/mode parity, M04 ancestry, result vocabularies and Profile-operation disposition counts |
| `A1_A2_A3_A5_GRAPH_EXACT_REPRESENTATION` | A1–A3/A5 | Every checked identity, edge, traceability assertion and invariant annotation is represented in RDF |
| `A4_TO_A5_IRI_AND_RDF_EQUIVALENCE` | A4/A5 | Reversible namespace translation and RDF graph isomorphism across supported serializations |
| `A6_A7_A8_SCHEMA_AND_SHAPE_COHERENCE` | A6–A8 | Structural schema validation, shape parseability and representative declaration parity |
| `A9_A10_A11_A12_CORPUS_AND_RUNNER` | A9–A12 | Corpus/flow counts and ongoing positive, negative and guard-boundary runner behaviour |
| `M17_COMPATIBILITY_AUTHORITY_SEPARATION` | M17/A1–A3 | Frozen historical alias treatment, external reference isolation, non-equivalence/non-transitivity |

The report records the exact check count and each defect; a zero-defect result means **none of the tested representations disagreed**, not that all architectural conformance questions have been resolved.

## 4. Disposition vocabulary

A13 uses these **reconciliation-report terms only**, not M16 conformance outcomes:

- `PASS_BOUNDED_RECONCILIATION`: no disagreement detected among tested source/representation assertions;
- `RECONCILIATION_DEFECTS_OR_ERRORS`: a tested contradiction or execution failure exists;
- `FORMALIZATION_DEFECT`: a mismatch against source authority, with expected and observed evidence;
- `EXECUTION_ERROR`: a verification step could not complete;
- `NOT_INDEPENDENTLY_VERIFIED`, `NOT_RUN`, `OUTSIDE_MACHINE_BOUNDARY`: known verification limits, retained without a false PASS.

A13 cannot determine `SATISFIED`, `VIOLATED`, `NOT_APPLICABLE` or overall `CONFORMANT`. M16 still requires bounded subject applicability, evidence sufficiency and accountable judgement. A9 scenarios remain illustrative and are not promoted to real-world conformance claims.

## 5. Current A13 reconciliation evidence

The bundled deterministic report records **1,715/1,715 checked assertions across seven gates with zero detected formalization defects**. Ten in-memory positive/negative guard tests passed, including deliberate changes to M17 counts, M16 conditions and assessment modes, A1 Plane identity, A2 relationship target, RDF invariant annotation and A5 IRI base. No A1–A12 canonical files were modified to obtain this result.

Source coverage is deliberately finite, not an assertion of complete OWL/RDF semantics or exhaustively derived external authority truth. Current verified and unverified boundaries are enumerated in the machine-readable disposition ledger.

## 6. Outstanding verification limitations (not silently waived)

1. **Independent SHACL engine:** A6's local subset and parse checks are not a formal independent SHACL processor validation. A14/A15 should record whether this has been completed before executable release closure.
2. **Full OWL reasoning:** RDF graph parity is not a proof that every OWL entailment profile or external consumer reasoner behaves equivalently.
3. **Docusaurus build:** The generated A13 files are valid repository artifacts; an npm/Docusaurus build has not been run as part of A13.
4. **Accountable architecture conformance:** No actual realization has been adjudicated against all applicable M16 HYBRID/ASSESSMENT obligations.
5. **External authority attestation:** External semantic/Product-family/policy/Decision source truth was not independently certified in this repository-only reconciliation.

These are scoped limitations of the **verification campaign**, not newly introduced architecture invariants or permission to weaken M17.

## 7. Reproducible execution

From the repository root, with Python 3.10+, `rdflib` and `jsonschema`:

```bash
python static/specs/hdip-cla/0.1/a13/run_reconciliation.py \
  --output static/specs/hdip-cla/0.1/a13/a13-reconciliation-report.json
python static/specs/hdip-cla/0.1/a13/test_reconciliation.py
```

Exit status `0` is bounded machine reconciliation success; `2` means a defect or error was detected. Runner output is deterministic for unchanged sources, deliberately carries no current clock timestamp and does not mutate predecessor artifacts. External evidence-record signing and governance of release publication are outside A13.

## 8. Package conventions and next stage

```text
docs/architecture/executable/
  hdip-cla-0.1-a13-cross-artifact-reconciliation.md
  hdip-cla-0.1-executable-programme.md     (status change only)

static/specs/hdip-cla/0.1/a13/
  run_reconciliation.py
  test_reconciliation.py
  a13-reconciliation-policy.json
  a13-reconciliation-report.json
  a13-disposition-ledger.json
  a13-validation.json

sidebars.ts                                   (navigation change only)
```

A13 produces a **step-specific overlay** containing only these additions/changes, plus a cumulative complete ZIP. A14 may add broader mutation tests, continuous regression verification, independent SHACL verification where available and non-regression controls across releases. A15 is responsible for explicit executable 0.1 release closure, not A13.
