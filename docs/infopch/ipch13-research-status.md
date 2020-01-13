---
title: IPCH13 Experimental Guidance — Evidence and Status
---

# IPCH13 — First-Pass research and assessment boundaries

> **Experimental E0 guidance; not an operative Product maturity standard or normative adoption.** D33 approved the IPCH13 First-Pass criteria; D34 accepted `IPCH13.md / FIRST-PASS-DRAFT-01` as an experimental guidance draft only. Overlay packaging is not evidence that tests ran, a promotion gate operated, consumers migrated, a repository deployment occurred or a Product matured.

## Principal lineage and accountable owner decisions

- [IPCH13 — Testable & Versioned](./IPCH13.md) — `IPCH13-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01`.
- [IPCH catalogue](./overview.md) and [PMDD IPCH Maturity Guidance](../pmdd/ipch-maturity-guidance.md).
- **DPCH13 / AIPCH14**, interpreted separately. AI-specific model and learning constructs are source analogies, not Information Product qualification requirements.
- `INFOPS-0.1-IPCH-P01-D33-F01 = APPROVED_EXPERIMENTAL_E0`: owner approved F01.1–F01.16, Information-specific definition, mandatory conjunctive `TAV-M01–TAV-M08`, negatives `TAV-N01–TAV-N09`, evidence claims `TAV-ES01–TAV-ES08`, twelve proposed unexecuted adversarial cases `TAV-A01–TAV-A12` and eight open research questions `TAV-R01–TAV-R08`.
- `INFOPS-0.1-IPCH-P01-D34-F01 = APPROVED_EXPERIMENTAL_E0`: owner accepted the sixteen-section experimental guide as `DRAFT_PREPARED_ACCEPTED` only, not finally or normatively approved.

## Mandatory Product version, testing and consumer protection boundaries

**Version the Product capability, not merely the implementation.** Preserve authoritative, meaningful Product Versions and change provenance, distinct from semantic definitions, component, dependency, realization, compilation and runtime versions. A pipeline version or code commit alone does not satisfy `TAV-M01`.

**Automated reproducible Product-level testing.** Protect informational meaning, material analytical measures, consumer contracts, quality, and applicable policy assertions. Executed, attributable test results are different from proposed or approved test designs. Tests require controlled inputs, expected outcomes and appropriate reproducibility evidence; time-sensitive and nondeterministic conditions remain subject to `TAV-R05`.

**Governed Product evolution.** Material change should undergo evidence-backed validation and promotion gates, regression/compatibility review, and applicable consumer transition protection. Breaking changes are not categorically prohibited when governed and appropriately communicated. A promotion-gate blueprint is not evidence that the gate operated.

**D02/D03 safeguards.** All eight `TAV-M01–TAV-M08` are conjunctive for `MET`. `MET`, `PARTIAL`, `NOT_MET`, independent `EVIDENCE_LIMITED`, competent `NOT_APPLICABLE`, eligibility-dependent `NOT_ASSESSABLE` remain unchanged. D03 experimental characteristic scores remain `1 / 0.5 / 0` without criterion averaging, caps or IPCH L0/L1/L2 maturity bands.

**Independent authorities and identity.** Keep Product/Version, semantic-definition/version, test definition/version and executed occurrence, output-port contract, dependencies, realization revision, compilation, runtime occurrence and evidence distinct. Productness under BPS/PIN, Information-family/Compound qualification, GEARA/GEARM semantics, INFOPROD/INFOPDS, DPP, PFI/HDIP, policy/legal, assurance and consequential-action authority remain independent. The presence of test designs does not independently establish compliance or Product qualification.

## Open Second-Pass research register

| ID | Question | Status |
|---|---|---|
| **TAV-R01** | Product Version versus semantic-definition, realization, dependency, compilation and runtime state under AIPCH14's every-change requirement | OPEN |
| **TAV-R02** | DPCH13 schema-only testing `PARTIAL` versus consumer-facing semantic protection | OPEN |
| **TAV-R03** | AIPCH14 unreproducible tests `PARTIAL` versus mandatory reproducibility | OPEN |
| **TAV-R04** | Information-specific risk-/Promise-proportionate coverage and contract assertions | OPEN |
| **TAV-R05** | Reproducibility for evolving/time-sensitive/nondeterministic data and dependencies | OPEN |
| **TAV-R06** | Correct version/evidence relationships among Product, tests, semantics, ports, realization and occurrence | OPEN |
| **TAV-R07** | Change classification, compatibility, rollback/coexistence, consumer notices and exceptional promotions | OPEN |
| **TAV-R08** | Nonduplicative relationship to Product qualification and IPCH06/08/09/11/12 | OPEN |

## Adversarial and evidence states

`TAV-A01–TAV-A12` — **PROPOSED_E0_UNEXECUTED**. No Product-level automated suite, adversarial replay, promotion test or empirical case disposition was executed by this overlay preparation.

## Programme and publication checkpoint

| Control | Status |
|---|---|
| IPCH13 guidance | `FIRST-PASS-DRAFT-01 / DRAFT_PREPARED_ACCEPTED` under D34 |
| Incremental IPCH13 overlay | `PREPARED_VERIFIED`, `NOT_DEPLOYED` |
| Product-level operational test / promotion gate | `NOT_EXECUTED` |
| Second Pass / empirical maturity assessment | `NOT_STARTED` / `NOT_EXECUTED` |
| Final guide approval | `NOT_APPROVED` |
| IPCH14–IPCH16 | `NOT_INITIATED` |
| Prior IPCH01–IPCH12 review obligations | PRESERVED |
| IPCH01–IPCH03 documentation deployment | `DEPLOYED_EXPERIMENTAL`, owner-confirmed |
| IPCH04–IPCH12 overlay deployment | Unconfirmed |
| Parent Track B B01 / B02–B06 | `NOT_ESTABLISHED` / `NOT_AUTHORIZED` |
| Effective prospective S04 | `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` |
| Historical C06 / safeguards | `APPROVED_NOT_EFFECTIVE`; F01.6/F01.29 preserved |
| Historical ledgers / separate PC ledger | `65/6/7/7` / unchanged |
| Q0–Q5 / F06/F14/F16 | UNRESOLVED |
| G06 E0 designs / E1 / E2 | `62_APPROVED_UNEXECUTED` / `0` / `0` |
| G06-RO01–RO12 and G03-R01–R12 | ALL 24 OPEN |
| Normative INFOPS release | `NOT_AUTHORIZED` |

This page is an **experimental research documentation record**. No live build, deployed content, empirical conformance, semantic/policy qualification or normative INFOPS adoption is asserted.
