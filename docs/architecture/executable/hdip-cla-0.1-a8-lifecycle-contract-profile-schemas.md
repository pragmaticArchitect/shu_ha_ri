---
id: hdip-cla-0.1-a8-lifecycle-contract-profile-schemas
title: HDIP-CLA 0.1 A8 - Lifecycle, Contract & Profile Schemas
sidebar_label: A8 - Lifecycle, Contract & Profile Schemas
---

# HDIP-CLA 0.1 A8 — Lifecycle, Contract & Profile Schemas

**Status:** COMPLETE (declaration schemas; no architectural conformance certificate)  
**Authority:** M17 frozen human-readable baseline; M10 PDEP, M11 SSCF/CEP, M12 Interaction Contracts, M13 EBC, M14 realization/Profile, M16 conformance.  
**Primary artifacts:** `/specs/hdip-cla/0.1/a8/`

## 1. Authority and purpose

A8 provides six bounded structural declaration schemas using JSON Schema Draft 2020-12. They do **not** amend the frozen definitions, assign Product qualification, confer authority or determine M16 conformance. A passing schema means only that a submitted declaration fits the declared structure. When frozen normative text is more demanding than these structural projections, the frozen text prevails. A8 does not introduce new A1 architectural identities.

## 2. Six schemas

| Schema | Responsibility |
|---|---|
| `lifecycle-declaration.schema.json` | PDEP / SSCF declarations, with Data PDEP Stage 0–10, SSCF 1–8, and family-specific PDEP separation. |
| `interaction-contract-declaration.schema.json` | Versioned M12 interaction context, Planes, evidence and delivery semantics. |
| `external-boundary-contract-declaration.schema.json` | M13 EBC and external authority separation. |
| `profile-declaration.schema.json` | M14/M16 concrete Profile dimensions and monotonic permitted operations. |
| `consumer-experience-projection-declaration.schema.json` | CEP as an SSCF projection, not a Plane or ABB. |
| `realization-profile-binding-declaration.schema.json` | Many-to-many-capable logical mapping between realization patterns, profiles and responsibilities. |

## 3. Non-negotiable boundaries

- **PDEP is not a Plane, ABB or Product-qualification test.** The frozen Data specialization is Stage 0 plus Stages 1–10. Information/Intelligence/Compound specializations must follow their own relevant authority rather than inherit Data stage numbering.
- **SSCF has eight logical stages.** The schema preserves their numbering and does not imply an eight-hop synchronous execution pipeline.
- **CEP is Consumer Experience Projection**, not Consumer Experience Plane.
- **M12 Interaction Contracts are logical contracts**, not API, event, service, queue or schema mandates. Outcomes, retries, currentness, temporal semantics and evidence obligations remain contextual.
- **M13 EBC specializes M12 discipline** at external/adjacent boundaries; Product access and consequential Decision/Action permission are separate authorities.
- **Profiles are monotonic specializations, not waivers.** All 18 Profile dimensions have named structural slots. The nine permitted operation classes are selectable; prohibited operation names do not validate.
- **Realization Pattern is not a Profile.** A selected topology is no shortcut to architecture conformance.

## 4. What A8 checks and does not check

The schemas validate controlled enumerations, required fields, scope statements, typed lists and specific topology/authority separation markers. They cannot decide whether evidence is adequate, obligations truly apply, policy decisions are lawful, a Profile is semantically monotonic, or a human assessment is correct. Empty Profile dimension objects are structurally acceptable placeholders, **not** proof that those dimensions are adequately fulfilled.

A8 illustrative fixtures are local examples to test schema boundary behavior; they are not the A9 canonical example corpus or A10/A11 certification suites. The structural validation record is `a8-validation.json`.

## 5. Repository and fidelity

The A8 overlay introduces only this document, the new `a8/` static artifacts and programme/sidebar updates. All other A1–A7 predecessor file bytes are preserved. A8 canonical IDs and stages are pulled from the frozen M10–M16 source and the A1/A2 inventories, not assigned anew. A9 may develop richer canonical examples, and A12 may execute bounded conformant checks; neither authority is claimed by A8.
