---
id: hdip-cla-0.1-m01-charter
title: HDIP-CLA 0.1 M01 — Programme Charter, Scope & Authority Boundary
sidebar_label: M01 — Charter & Authority
---

# HDIP-CLA 0.1 M01 — Programme Charter, Scope & Authority Boundary

**Status:** Complete — accepted baseline for M02 onward.

## 1. Purpose

M01 establishes the architectural jurisdiction, authority boundaries and derivation discipline for the **HDIP Canonical Logical Architecture (HDIP-CLA) 0.1** programme.

HDIP means **Holistic Data, Information and Intelligence Platform**.

## 2. Foundational proposition

> **HDIP is an enterprise logical platform architecture that provides governed, interoperable and product-oriented capabilities across Data, Information and Intelligence by composing and realizing responsibilities defined by GEDRA, GEARA and GEAIRA, while preserving the semantic and Product authorities of GEDRM, GEARM, GEAIRM, BPS/PIN and applicable Product-family specifications.**

Short form:

> **GEDRA, GEARA and GEAIRA define generic architectural responsibilities; HDIP composes and realizes those responsibilities as one enterprise platform.**

## 3. Architecture level

```text
Semantic authorities
  GEDRM | GEARM | GEAIRM | BPS/PIN | family specifications
                          |
                          v
Generic reference architectures
              GEDRA | GEARA | GEAIRA
                          |
                          v
                      HDIP-CLA
          enterprise logical realization/composition
                          |
                          v
             technology/deployment realization
```

HDIP is therefore **not a fourth peer generic reference architecture**. It is an enterprise logical realization/composition architecture that may co-realize responsibilities from the generic reference architectures.

## 4. Authority boundaries

| Concern | Authority | HDIP-CLA treatment |
|---|---|---|
| Generic Product ontology / Product Intrinsic Nature | BPS / PIN | Consume and preserve; do not redefine. |
| Data semantics | GEDRM | Consume and preserve. |
| Data reference architecture | GEDRA | Intake and realize/profile responsibilities. |
| Information / Analytics semantics | GEARM | Consume and preserve. |
| Information / Analytics reference architecture | GEARA | Intake and realize/profile responsibilities. |
| Enterprise-AI semantics | GEAIRM | Consume and preserve. |
| Enterprise-AI reference architecture | GEAIRA | Intake and realize/profile responsibilities. |
| AI Product qualification/classification/governance | AIPS | Consume where applicable; do not infer locally. |
| Enterprise platform composition and coordination | HDIP-CLA | Canonical HDIP jurisdiction. |

## 5. Product as an orthogonal lens

Productization cuts across Data, Information and Intelligence. Therefore:

```text
Data         != Data Product automatically
Information  != Information Product automatically
AI capability != AI Product automatically
```

HDIP lifecycle, deployment, registration, publication, cataloguing, composition or consumption does not independently establish Productness.

## 6. Data Mesh boundary

HDIP is not synonymous with Data Mesh. Data Mesh may influence the realization and operating model of Data responsibilities, but it is not the parent architecture for Data, Information and Intelligence as a whole.

## 7. Responsibility-first derivation

HDIP-CLA SHALL derive planes and Architecture Building Blocks (ABBs) from responsibilities rather than inheriting historical HDIP boxes or vendor/product structures.

```text
GEDRA responsibilities
       +
GEARA responsibilities
       +
GEAIRA responsibilities
       +
justified HDIP-specific coordination responsibilities
       |
       v
convergence / separation analysis
       |
       v
logical planes, overlays and ABBs
```

## 8. Shared realization without semantic collapse

HDIP may co-realize responsibilities where operationally appropriate, but shared realization does not transfer semantic authority or collapse distinctions.

```text
shared implementation != shared semantics
co-location            != authority transfer
mapping                != ownership transfer
```

## 9. Projection and compilation boundary

HDIP-generated projections, descriptors and compiled artifacts may resolve, correlate and operationalize authoritative information but do not become the semantic authority for that information.

Examples include HPD and SYNCTX.

## 10. M01 normative architecture contract

**HDIP-CLA-M01-R01 — Platform Scope.** HDIP SHALL be defined as the **Holistic Data, Information and Intelligence Platform**.

**HDIP-CLA-M01-R02 — Enterprise Realization.** HDIP SHALL be treated as an enterprise logical platform architecture.

**HDIP-CLA-M01-R03 — Reference Architecture Intake.** HDIP SHALL consume architectural responsibilities from GEDRA, GEARA and GEAIRA without redefining their generic responsibilities.

**HDIP-CLA-M01-R04 — Semantic Authority Preservation.** HDIP SHALL preserve semantic authority boundaries established by GEDRM, GEARM, GEAIRM and other applicable authoritative models.

**HDIP-CLA-M01-R05 — Product Authority Preservation.** HDIP SHALL defer generic Product qualification and Product Intrinsic Nature to BPS/PIN.

**HDIP-CLA-M01-R06 — Product Family Authority.** HDIP SHALL defer family-specific Product qualification/classification to the applicable Product-family specification.

**HDIP-CLA-M01-R07 — No Automatic Productness.** HDIP composition, deployment, generation, registration, cataloguing or consumption SHALL NOT by itself establish Product identity.

**HDIP-CLA-M01-R08 — Logical Technology Neutrality.** HDIP-CLA SHALL define logical responsibilities and interactions independently of concrete technology products.

**HDIP-CLA-M01-R09 — Responsibility First.** Canonical HDIP planes and ABBs SHALL be derived from architectural responsibilities rather than inherited from historical platform diagrams.

**HDIP-CLA-M01-R10 — Shared Realization Without Semantic Collapse.** HDIP MAY co-realize compatible responsibilities across Data, Information and Intelligence but SHALL preserve semantic distinctions between those responsibilities.

**HDIP-CLA-M01-R11 — Projection Non-Authority.** HDIP-generated projections, descriptors or compiled artifacts SHALL NOT override their authoritative source semantics.

**HDIP-CLA-M01-R12 — Data Mesh Boundary.** HDIP SHALL NOT be defined as synonymous with Data Mesh; Data Mesh MAY be an applicable realization/operating-model influence for Data responsibilities.

**HDIP-CLA-M01-R13 — Lifecycle Non-Authority.** HDIP Product development, deployment and consumption lifecycles SHALL NOT independently determine Productness.

**HDIP-CLA-M01-R14 — Historical Meaning.** Versioned HDIP projections and artifacts SHALL preserve historical meaning; later upstream changes SHALL NOT silently rewrite prior state.

**HDIP-CLA-M01-R15 — Explicit Architecture Boundary.** Semantic-model concepts SHALL NOT automatically imply corresponding HDIP ABBs unless an architectural responsibility requires them.

**HDIP-CLA-M01-R16 — Architecture Traceability.** Every canonical HDIP plane, overlay and ABB SHALL ultimately be traceable to one or more upstream reference-architecture responsibilities, explicit enterprise platform requirements, or justified HDIP-specific coordination responsibilities.

## 11. Deliberately unresolved in M01

M01 does **not** freeze:

- HDIP plane count or plane names;
- survival of historical HDIP planes;
- whether PDEP, CEP or COVP are planes, overlays, experiences or ABB groupings;
- whether Governance is a plane or cross-cutting overlay;
- Utility / Infrastructure grouping;
- exact ABBs;
- runtime topology;
- physical deployment architecture;
- registry consolidation;
- concrete inter-plane interactions.

## 12. Completion state

**HDIP-CLA M01 — COMPLETE.**

M02 performs upstream architectural responsibility intake without convergence or plane derivation.
