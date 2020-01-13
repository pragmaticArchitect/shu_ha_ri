---
title: IPCH11 Experimental Guidance — Evidence and Status
---

# IPCH11 — First-Pass research and assessment boundaries

> **Experimental E0 guidance; not an operative semantic-conformance standard or normative adoption.** D29 accepted IPCH11's First-Pass criteria baseline; D30 accepted `IPCH11.md / FIRST-PASS-DRAFT-01` as an experimental guidance draft only. Packaging does not establish semantic authority, successful mapping execution, empirical independent interpretation, final approval or live documentation deployment.

## Source lineage and owner decisions

- [IPCH11 — Semantically Aligned](./IPCH11.md) — `IPCH11-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01`
- [IPCH catalogue](./overview.md) and [PMDD IPCH Maturity Guidance](../pmdd/ipch-maturity-guidance.md)
- Principal source lineage: **DPCH11 / AIPCH12**, interpreted separately
- `INFOPS-0.1-IPCH-P01-D29-F01 = APPROVED_EXPERIMENTAL_E0`: clauses F01.1–F01.16; mandatory conjunctive `SEM-M01–SEM-M08`, negative `SEM-N01–SEM-N09`, evidence `SEM-ES01–SEM-ES08`, twelve proposed unexecuted `SEM-A01–SEM-A12`, eight `SEM-R01–SEM-R08` OPEN
- `INFOPS-0.1-IPCH-P01-D30-F01 = APPROVED_EXPERIMENTAL_E0`: owner accepted the sixteen-section guide as `DRAFT_PREPARED_ACCEPTED` only; not finally or normatively approved

## Mandatory semantic and governance boundaries

**Authoritative meaning.** Shared enterprise/domain semantics go beyond similar names and schemas. Material source concepts, Information Product measures, analytical interpretations and consumer outcomes require authoritative semantic anchoring and machine-referenceable mapping. Source-Data-Product alignment does not establish aligned derived information by itself.

**Independent interpretation.** Governed semantic definitions, Product-specific derivation and consumer-facing outcomes must be interpretable across independent consumers without undocumented semantic negotiation. Representational differences do not necessarily mean different semantics; matching labels do not prove equivalence.

**Competent semantic authority.** GEARA/GEARM governance remains independent. Product-specific extensions and deviations cannot silently amend enterprise ontology or create Product Owner authority. No particular RDF/OWL/SKOS/JSON-LD stack, registry or engine is mandated.

**Source tensions preserved.** DPCH11's versioned-deviation `MET` and local-extension `PARTIAL` cases remain distinct (`SEM-R02`, `SEM-R04` OPEN). AIPCH12's schema-without-ontology `PARTIAL` case remains in tension with foundational shared semantic alignment (`SEM-R03` OPEN). No automatic exception or source reconciliation is adopted.

**Evidence integrity.** Distinguish assessed Product/Version, semantic-definition/version, mapping revision, output-port contract, realization revision, runtime occurrence, effective evidence time and determinations. Machine-referenceable design or an approved E0 plan is not an executed mapping or conformance finding.

## Research questions — ALL OPEN

| ID | Unresolved matter | Status |
| --- | --- | --- |
| SEM-R01 | Authoritative semantics of derived information measures and analytical interpretations | OPEN |
| SEM-R02 | Competent conditions allowing an explicit, versioned deviation to support MET | OPEN |
| SEM-R03 | AIPCH12 schema-only PARTIAL versus foundational shared semantic anchoring | OPEN |
| SEM-R04 | Legitimate local semantic extension versus unauthorized redefinition | OPEN |
| SEM-R05 | Product/Version, definition/version, mapping, port contract and realization attribution | OPEN |
| SEM-R06 | Independent interpretation evidence without prescribed ontology technology | OPEN |
| SEM-R07 | Meaning across derived measures, transformations, assumptions and representations | OPEN |
| SEM-R08 | Avoiding circular claims and duplicated semantics across neighbouring IPCH criteria | OPEN |

`SEM-A01–SEM-A12 = PROPOSED_E0_UNEXECUTED`. Second Pass remains `NOT_STARTED`.

## D02/D03 finding and scoring restrictions

`MET` requires all eight SEM mandatory criteria with sufficient Product/Version evidence. `PARTIAL` and `NOT_MET` require positive grounds for the respective determination; missing/stale/conflicting evidence remains the separate `EVIDENCE_LIMITED` qualifier. `NOT_ASSESSABLE` applies absent D02 eligibility; `NOT_APPLICABLE` needs competent specific scope disposition. D03 characteristic-level scores are MET=1, PARTIAL=0.5, NOT_MET=0, without criterion-level averaging, automatic caps or L0/L1/L2 bands. No empirical Information Product assessment has taken place.

## Publication and stage status

| Item | Status |
| --- | --- |
| IPCH11 guide | `DRAFT_PREPARED_ACCEPTED` (D30) |
| Incremental overlay | `PREPARED_VERIFIED`; deployment `NOT_DEPLOYED` |
| `SEM-R01–SEM-R08` | ALL OPEN |
| `SEM-A01–SEM-A12` | UNEXECUTED |
| Empirical assessment / independent semantic validation | NOT_EXECUTED |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| IPCH12–IPCH16 | NOT_INITIATED |

IPCH01–IPCH03 experimental documentation deployment was confirmed; IPCH04–IPCH10 overlays were prepared without confirmed live deployment. All IPCH01–IPCH10 reviews remain outstanding, and the original D05 authoring sequence remains historically preserved.

## Parent INFOPS research and governance holds

Parent Track B B01 completion `NOT_ESTABLISHED`; B02–B06 `NOT_AUTHORIZED`. Effective prospective S04 remains `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` and historical C06 `APPROVED_NOT_EFFECTIVE`; F01.6/F01.29 safeguards retained. Historical ledgers 65/6/7/7 and separate PC ledger unchanged; Q0–Q5 and F06/F14/F16 UNRESOLVED; 62 approved G06 E0 designs UNEXECUTED; E1/E2 execution 0/0; G06-RO01–RO12 and G03-R01–R12 all 24 OPEN. BPS/PIN Productness, GEARA/GEARM, Product-family/Compound, INFOPROD/INFOPDS, DPP, PFI/HDIP, policy/legal, assurance and consequential-action authorities remain independent. No Product/Version or semantic qualification, realization, compilation, occurrence or evidence finding is changed.
