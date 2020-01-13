---
title: MPEC-01 Evidence Contract and Reproducibility
sidebar_label: Evidence contract
---

# MPEC-01 — Minimal Profile Evidence Contract

> Approved conceptual assessment design under MVP D07, consolidated in D08. **Not** an INFOPROD/INFOPDS schema, an implemented registry or adopted independent authority source pin.

## Ten conceptual fields

| Field | Required conceptual evidence |
|---|---|
| `product_ref` | Exact independently governed Product and subject scope |
| `product_version` | Applicable Product Version |
| `bps_productness_ref` | Independent PCE/BPS/PIN determination and its limits |
| `governing_promise_ref` | Constituted Promise and ACI evidence |
| `analytics_context_ref` | Declared Analytics context and GEARA applicability |
| `information_meaning_ref` | GEARM proposition, interpretive context, method, semantic authority and Version |
| `boundary_assessment_ref` | FBA/Compound evidence, applicable adjudication and limits |
| `profile_result` | Six-outcome result **where defensibly assignable**, else unset in draft |
| `evidence_limitations` | Missing facts, uncertainty, counterarguments and unverified authorities |
| `assessment_provenance` | Assessor, claim, accountable determination, evidence basis, time and applicability |

D04 refines `information_meaning_ref` with `information_proposition_ref`, `interpretive_context_ref`, `meaning_formation_ref`, `semantic_definition_ref`, and `semantic_evidence_limitations` as **conceptual evidence subelements**, not a separate normative schema.

D05 refines Productness/boundary evidence with `product_authority_ref`, `assessed_subject_scope`, `competing_family_claims`, `compound_assessment_ref` and authority provenance. Prefer **references** to source systems rather than duplicating upstream semantics.

## Reproducibility distinctions

- **R1 — Referential:** reconstruct subject, exact governing references and evidence Versions.
- **R2 — Reasoning:** reconstruct evidence-to-PCE/ACI/GIM/FBA findings and overall ODR rationale, including contrary evidence.
- **R3 — Independent repeatability:** an appropriately competent assessor reproduces or challenges the determination; **future verification, not demonstrated**.

| Check | Design expectation |
|---|---|
| MARC-01 | Subject reconstruction |
| MARC-02 | Evidence reconstruction |
| MARC-03 | Authority reconstruction |
| MARC-04 | Reasoning reconstruction |
| MARC-05 | Outcome and concurrent blockers reconstruction |
| MARC-06 | Historical temporal applicability versus present currentness |

A stable ID alone does not establish accessible or immutable evidence. A repeatable calculation does not establish correct semantic governance. A traceable assessment does not automatically establish its correctness.

## Illustrative incomplete assessment (not an actual Product qualification)

A hypothetical Intraday Liquidity Insight Product has a suggested Analytics Promise. Without an independent BPS/PIN determination, an applicable GEARM semantic reference, or B0 screening, the overall result remains **unset in the illustrative draft**. Do not fabricate source IDs or portray the example as an issued qualification.
