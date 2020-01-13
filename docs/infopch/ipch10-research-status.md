---
title: IPCH10 Experimental Guidance — Evidence and Status
---

# IPCH10 — First-Pass research and assessment boundaries

> **Experimental E0 guidance; not operative Product port conformance or normative adoption.** D27 approved the Addressable First-Pass criteria baseline; D28 accepted `IPCH10.md / FIRST-PASS-DRAFT-01` as an experimental guidance draft only. Packaging does not establish deployed ports, empirical consumption, tested enforcement, final guide approval or live documentation publication.

## Source lineage and owner decisions

- [IPCH10 — Addressable](./IPCH10.md) — `IPCH10-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01`
- [IPCH catalogue](./overview.md) and [PMDD IPCH Maturity Guidance](../pmdd/ipch-maturity-guidance.md)
- Principal canonical lineage: **DPCH10 / AIPCH11**, interpreted separately and without changing independent Product, semantic and policy authorities
- `INFOPS-0.1-IPCH-P01-D27-F01 = APPROVED_EXPERIMENTAL_E0`: eight mandatory conjunctive `ADR-M01–ADR-M08`, nine negatives `ADR-N01–ADR-N09`, eight evidence `ADR-ES01–ADR-ES08`, twelve proposed unexecuted `ADR-A01–ADR-A12`, eight research questions `ADR-R01–ADR-R08` OPEN
- `INFOPS-0.1-IPCH-P01-D28-F01 = APPROVED_EXPERIMENTAL_E0`: owner accepted sixteen-section guide as `DRAFT_PREPARED_ACCEPTED`, not as final approved or normative

## Mandatory Product-level addressability boundaries

`ADR-M01–ADR-M08` are **conjunctive for `MET`**. A port must be a first-class, identifiable, documented, stable, policy-controlled interface exposing the governed **Information Product capability**, independently of a specific UI, dashboard, application or implementation pipeline. Declared consumer context determines suitable interface modalities; **no universal number of ports** is required. A single suitable governed Product port may be sufficient, but technical endpoints, marketplace listings and internal API traffic do not automatically establish Product addressability.

**Independent Product ports versus experience interfaces:** DPCH10's UI-plus-internal-API `PARTIAL` transitional example and AIPCH11's UI-only `NOT_MET` case remain distinguishable, without automatically recognizing an internal API as a Product port (`ADR-R01`, `ADR-R03` OPEN). Appropriate single-port versus multimodal suitability remains open (`ADR-R02`).

**Capability-level semantics:** The informational Promise must be delivered by ports rather than reconstructed by consumers from Data Products or implementation internals. Independent GEARA/GEARM semantic authority remains untouched (`ADR-R04` OPEN).

**Policy:** Appropriate port access must enforce applicable governance, but IPCH10 does not create substantive legal/policy authority or substitute for IPCH09 (`ADR-R07` OPEN).

**Evidence identity:** Keep Product/Version, semantic-definition/version, output-port/contract version, realization revision, runtime occurrence and effective evidence distinct (`ADR-R05` OPEN). Gateway-mediated consumption and genuine Product-level evidence remain open (`ADR-R06`, `ADR-R08`).

## Open research and proposed challenges

- `ADR-R01–ADR-R08 = OPEN` — no source tensions or architectural/authority questions silently settled
- `ADR-A01–ADR-A12 = PROPOSED_E0_UNEXECUTED` — conceptual cases are not empirical port-conformance assessments
- `ADR-N01–ADR-N09` and `ADR-ES01–ADR-ES08` are approved First-Pass registers
- D02 independent Product/Version eligibility and applicability remain prerequisites; `EVIDENCE_LIMITED` remains an independent qualifier, not automatic `NOT_MET`
- D03 characteristic scores remain `MET=1`, `PARTIAL=0.5`, `NOT_MET=0`; no criterion averaging, automatic caps or IPCH L0/L1/L2 bands

## Publication and retained obligations

| Item | Status |
| --- | --- |
| IPCH10 guidance | `DRAFT_PREPARED_ACCEPTED` (D28) |
| Incremental overlay | `PREPARED_VERIFIED`; deployment `NOT_DEPLOYED` |
| `ADR-R01–ADR-R08` | ALL OPEN |
| `ADR-A01–ADR-A12` | UNEXECUTED |
| Empirical Product-port consumption / conformance | `NOT_EXECUTED` |
| Second Pass | `NOT_STARTED` |
| Final guide approval | `NOT_APPROVED` |
| Normative INFOPS release | `NOT_AUTHORIZED` |
| IPCH11–IPCH16 | `NOT_INITIATED` |

IPCH01–IPCH03 experimental documentation deployment confirmed; IPCH04–IPCH09 overlays prepared with live deployment unconfirmed. All earlier IPCH01–IPCH09 review obligations preserved; original D05 authoring sequence historically preserved.

## Parent INFOPS research and governance holds

Parent Track B B01 completion `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`. Effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE`; safeguards F01.6/F01.29 and original charter/audit limitations preserved. Historical ledgers **65 / 6 / 7 / 7**, separate PC ledger unchanged. Q0–Q5 and F06/F14/F16 unresolved. **62** approved G06 E0 designs remain **UNEXECUTED**, E1/E2 **0 / 0**, all **24** G06-RO01–RO12 and G03-R01–R12 obligations **OPEN**. Independent BPS/PIN, Product-family/Compound, GEARA/GEARM, INFOPROD/INFOPDS, DPP, PFI/HDIP, legal/policy, realization, consumption and assurance authorities retained. No Product assessment, qualification, normative adoption, enterprise control execution or live repository change is asserted.
