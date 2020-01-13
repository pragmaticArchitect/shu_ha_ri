---
id: hdip-cla-0.1-a9-canonical-example-corpus
title: HDIP-CLA 0.1 A9 - Canonical Example Corpus
sidebar_label: A9 - Canonical Example Corpus
---

# HDIP-CLA 0.1 A9 — Canonical Example Corpus

**Status:** COMPLETE — Illustrative corpus, not a conformance certificate.  
**Authority precedence:** Frozen M17 human-readable architecture > A1–A8 formalizations > A9 illustrations.

## 1. Purpose

A9 supplies scenario-based, executable-format **examples** whose declarations validate against the actual A8 JSON Schemas. These examples cannot establish Product qualification, architectural conformance, entitlement, or consequential Decision permission. They are not an extension of normative M17 architecture.

## 2. Corpus inventory

| ID | Scenario | Family | Declaration files |
|---|---|---|---:|
| HDIP-CLA-A9-01 | Data Product Development, Realization & Publication | DATA | 3 |
| HDIP-CLA-A9-02 | Information Product Formation from Governed Products/Capabilities | INFORMATION | 3 |
| HDIP-CLA-A9-03 | AI Product / Intelligence Capability Realization with External Provider | INTELLIGENCE | 4 |
| HDIP-CLA-A9-04 | Intent-First Product Consumption | NOT_APPLICABLE | 3 |
| HDIP-CLA-A9-05 | Established-State Repeated Runtime Consumption | NOT_APPLICABLE | 3 |
| HDIP-CLA-A9-06 | Access Denial, Constraint & Product Substitution | NOT_APPLICABLE | 3 |
| HDIP-CLA-A9-07 | Governing Revocation During Active Operation | NOT_APPLICABLE | 3 |
| HDIP-CLA-A9-08 | Outcome / Value Feedback into Product Evolution | DATA | 3 |
| HDIP-CLA-A9-09 | Federated Cross-Domain Product Consumption | NOT_APPLICABLE | 4 |
| HDIP-CLA-A9-10 | Provider Failure, Migration, Rebinding & Recovery | INTELLIGENCE | 3 |
| HDIP-CLA-A9-11 | Compound Data / Information / Intelligence Product Composition | COMPOUND | 3 |

## 3. Fidelity controls

- The ten M15 representative flows are exercised across eleven examples; the additional compound example is explicitly illustrative.
- The Data PDEP 0–10 stages are retained only in Data-family declarations. Information, Intelligence and Compound examples use an explicitly illustrative family-governed checkpoint, not a newly prescribed lifecycle.
- SSCF 1–8 is a logical sequence, not a synchronous eight-hop pipeline. CEP remains a projection.
- M12 interaction references are logical assertions, never prescribed API/event topology. Schema-valid placeholder plane bindings are not verified interaction semantics.
- M13 boundaries preserve distinct external decision and access authorizations.
- Profile shape completion or realization binding does not establish M16 conformance.
- Historical truth remains reconstructable against the governing version at occurrence time.
- Every manifest has NOT_ASSESSED and INDETERMINATE status.

## 4. Validation scope

Validation checks: JSON Schema Draft 2020-12 positive acceptance for each declaration, scoped A1 ID resolution for Flow/Interaction/Boundary/Profile/Pattern references, basic non-certification controls, inventory completeness, unchanged predecessor byte hashes, and intentional malformed negative corpus checks.

A9 does **not** perform A10 positive conformance assertions, A11 adversarial conformance tests or A12 runtime evaluation.

## 5. Files

- `/specs/hdip-cla/0.1/a9/example-corpus.json`
- `/specs/hdip-cla/0.1/a9/examples/a9-NN-*/manifest.json`
- `/specs/hdip-cla/0.1/a9/examples/a9-NN-*/*.json`
- `/specs/hdip-cla/0.1/a9/a9-validation.json`
