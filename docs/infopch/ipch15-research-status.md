---
title: IPCH15 Experimental Guidance — Evidence and Status
---

# IPCH15 — First-Pass explainability and transparency research boundaries

> **Experimental E0 documentation only.** D37 approved the IPCH15 criteria and draft-preparation authority; D38 accepted `IPCH15.md / FIRST-PASS-DRAFT-01` as `DRAFT_PREPARED_ACCEPTED`. Neither decision approves a normative Product requirement, empirical assessment, explanation-fidelity execution, live website deployment or final guide.

## Source lineage and approval provenance

- [IPCH15 — Explainable & Transparent](./IPCH15.md) — `IPCH15-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01`.
- [IPCH catalogue](./overview.md) and [PMDD Maturity Guidance](../pmdd/ipch-maturity-guidance.md).
- The directly inspected principal precedent is **AIPCH16 — Explainable & Transparent** (AI Product family). The supplied DPCH catalogue ends at **DPCH14**: no corresponding DPCH15 was identified. This is a source coverage limitation, not evidence that Data Products lack transparency obligations.
- `INFOPS-0.1-IPCH-P01-D37-F01 = APPROVED_EXPERIMENTAL_E0` approved F01.1–F01.16, `XTR-M01–XTR-M08` mandatory conjunctive, `XTR-N01–XTR-N09` negative, `XTR-ES01–XTR-ES08` evidence, `XTR-A01–XTR-A12` proposed UNEXECUTED and `XTR-R01–XTR-R08` OPEN.
- `INFOPS-0.1-IPCH-P01-D38-F01 = APPROVED_EXPERIMENTAL_E0` accepted the sixteen-section experimental *draft only*; not operational or normative.

## Governing distinctions and evidence constraints

**Informational explanations.** Material outputs require contextually meaningful information about what a result means, relevant derivations/contributing factors, assumptions, limitations and authorized channels for inspection and challenge. Local output-specific and global Product-method explanations are conceptually distinct. Explanations must be faithful to actual information derivation, not merely plausible narratives.

**Access and representation.** Product-level explanation accessibility and structured, machine-referenceable explanation evidence are D37-approved criteria. The AIPCH16 natural-language-only `PARTIAL` example remains a source tension, particularly for human-only consumption; no universal exemption or required JSON/RDF/API implementation has been adopted. The precise per-result versus reusable explanation-contract boundary is OPEN.

**Proportionality and protected disclosure.** Explainability depth must be appropriate to context and consequences, determined under competent authority. Do not mandate LIME/SHAP, AI R0–R4 risk tiers, proprietary implementation disclosure or unrestricted release of personal, protected or confidential material.

**D02/D03.** `XTR-M01–XTR-M08` remain conjunctive for `MET`. Findings are qualitative `MET`, `PARTIAL`, `NOT_MET`, with independent `EVIDENCE_LIMITED`, eligibility-dependent `NOT_ASSESSABLE` and no generic `NOT_APPLICABLE`. D03 characteristic-level score mapping remains `1 / 0.5 / 0` without criterion averaging, automatic caps or L0–L2 bands. Design assertions do not constitute executed explanation-fidelity evidence.

## Unresolved Second-Pass register

| ID | Research boundary | Status |
|---|---|---|
| **XTR-R01** | Information-specific explanation requirements without a verified corresponding DPCH15 source | OPEN |
| **XTR-R02** | Per-result explanations versus governed reusable explanation contracts | OPEN |
| **XTR-R03** | AIPCH16 natural-language-only `PARTIAL` versus possible sufficient human-context explanation | OPEN |
| **XTR-R04** | Depth relative to information context and consequence without universal AI risk tiers | OPEN |
| **XTR-R05** | Minimum derivation detail versus protected implementation disclosure | OPEN |
| **XTR-R06** | Faithfulness of explanations to actual information derivation and behaviour | OPEN |
| **XTR-R07** | Exact Product/Version, semantic, method, explanation contract, realization, occurrence and evidence identities | OPEN |
| **XTR-R08** | Privacy/security restrictions and independent noncircular assessment | OPEN |

**`XTR-A01–XTR-A12 = PROPOSED_E0_UNEXECUTED`**. No adversarial explanation or Product conformance exercise has been performed.

## Parent programme and documentation checkpoint

| Control | State |
|---|---|
| IPCH15 guidance | `FIRST-PASS-DRAFT-01 / DRAFT_PREPARED_ACCEPTED` — D38 |
| IPCH15 incremental overlay | `PREPARED_VERIFIED`, `NOT_DEPLOYED` |
| Operational explanation / fidelity tests | `NOT_EXECUTED` |
| Empirical Product assessments / Second Pass | `NOT_EXECUTED` / `NOT_STARTED` |
| Final guidance approval / normative INFOPS release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| IPCH16 | `NOT_INITIATED` |
| IPCH01–IPCH14 review and research obligations | PRESERVED |
| IPCH01–IPCH03 deployment | `DEPLOYED_EXPERIMENTAL`, owner-confirmed |
| IPCH04–IPCH14 deployment | UNCONFIRMED |
| Parent Track B B01 completion / B02–B06 | `NOT_ESTABLISHED` / `NOT_AUTHORIZED` |
| Effective prospective S04 | `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` |
| Historical C06 | `APPROVED_NOT_EFFECTIVE`, F01.6/F01.29 preserved |
| Historical approval ledgers / independent PC ledger | `65/6/7/7` / unchanged |
| Q0–Q5; F06/F14/F16 | UNRESOLVED |
| G06 E0 designs / E1 / E2 | `62_APPROVED_UNEXECUTED` / `0` / `0` |
| G06-RO01–RO12 and G03-R01–R12 | ALL 24 OPEN |

BPS/PIN, GEARA/GEARM, Product-family/Compound, INFOPROD/INFOPDS, DPP, PFI/HDIP, privacy, policy and assurance remain independently authoritative. No actual Product, release, documentation-site build or normative INFOPS adoption is asserted.
