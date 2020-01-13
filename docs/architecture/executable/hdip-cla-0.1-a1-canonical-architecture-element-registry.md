---
id: hdip-cla-0.1-a1-canonical-architecture-element-registry
title: HDIP-CLA 0.1 A1 - Canonical Architecture Element Registry
sidebar_label: A1 - Architecture Element Registry
---

# HDIP-CLA 0.1 A1 — Canonical Architecture Element Registry

**Status:** COMPLETE  
**Programme:** HDIP-CLA 0.1 machine-readable / executable formalization  
**Human-readable authority:** M01-M17 frozen baseline  
**Primary machine artifact:** `/specs/hdip-cla/0.1/a1/architecture-element-registry.json`

## 1. Purpose

A1 establishes the canonical machine-readable identity registry for the frozen **HDIP Canonical Logical Architecture (HDIP-CLA) 0.1** baseline.

A1 answers one foundational question:

> **Which frozen HDIP-CLA constructs must later executable artifacts refer to by stable, typed and unambiguous machine identity?**

A1 does **not** derive new architecture. It inventories and types what M17 already froze, assigns representation-only machine identifiers where the human-readable baseline deliberately used a canonical name without a numbered identifier, and records historical compatibility mappings without restoring retired terminology as canonical architecture.

The governing rule is:

```text
human-readable frozen meaning
        precedes
machine-readable representation
```

A1 therefore provides the identity substrate for A2-A15. It is not an ontology, relationship model, conformance engine, runtime Registry or new semantic authority.

---

# 2. Source authority and fidelity boundary

M17 froze the human-readable HDIP-CLA 0.1 architecture and explicitly handed the following concerns to downstream formalization:

- canonical architecture element registry;
- source/upstream traceability;
- Planes, Foundation, Overlays and ABB relationships;
- Registry/projection/compilation artifacts;
- PDEP and SSCF/CEP lifecycle identities/projections;
- M12 Interaction Contracts;
- M13 Boundary Families/EBCs;
- M14 Realization/Profile declarations and mappings;
- M15 views/flows;
- M16 invariants and conformance structures;
- positive/negative test cases;
- deterministic reconciliation and regression.

A1 implements only the first identity layer plus the minimum controlled vocabulary needed to keep later stages consistent.

If an A1 record conflicts with the frozen human-readable source, the human-readable source governs and A1 must be corrected. A1 has no reverse authority to modify M01-M17 meaning.

---

# 3. A1 scope

A1 registers the following frozen construct families:

```text
logical structure
  Plane
  Foundation
  Overlay
  Architecture Building Block

registry / operational architecture
  logical Registry
  Registry specialization
  Catalog / Marketplace / Product Lens constructs
  projection / compilation artifact

lifecycle / experience
  PDEP
  PDEP projections
  Data PDEP stages
  SSCF
  SSCF stages
  CEP

interaction / boundary
  M12 interaction families
  M12 interactions
  M13 Boundary Classes
  M13 Boundary Families

realization / specialization / presentation
  M14 Realization Patterns
  M14 Profile Patterns
  M15 Reference Views
  M15 representative flows

conformance foundations
  M16 Architecture Invariants
  M16 Conformance Subject classes
```

A1 also seeds four controlled vocabularies from M16:

```text
assessment mode
invariant result
conformance outcome
conformance claim type
```

These values are included so downstream artifacts do not invent competing spellings. Their full executable semantics belong to A3.

---

# 4. What A1 deliberately does not formalize

A1 does **not** yet freeze:

- RDF/OWL classes or properties;
- canonical IRIs/URIs;
- JSON-LD terms;
- SHACL shapes;
- JSON Schema structures;
- canonical relationship predicates;
- source/upstream mapping edges;
- ABB-hosting or Plane-participation relationship semantics;
- EBC schema;
- Interaction Contract schema;
- PDEP/SSCF transition schema;
- Profile schema;
- executable invariant logic;
- machine PASS/FAIL algorithms;
- certification or assurance semantics;
- an enterprise runtime Registry implementation.

Those are later A2-A15 concerns.

---

# 5. Registry metamodel

Every A1 element record uses a common machine envelope:

| Field | Meaning |
|---|---|
| `id` | Unique A1 machine identifier. Existing frozen source identifiers are reused where available. |
| `canonicalName` | Frozen or representation-faithful canonical human-readable name. |
| `kind` | Typed A1 element category. |
| `canonicality` | Whether `id` is reused from the frozen source or assigned by A1 for an unnumbered frozen construct. |
| `status` | A1 registry lifecycle state; A1 currently registers active 0.1 elements. |
| `sourceId` | Frozen human-readable identifier where one exists. `null` where A1 assigns a representation-only identifier. |
| `sourceDocuments` | Repository documents from which the registered identity/meaning is derived. |
| `shortId` | Optional accepted short identifier such as `INT-01`. |
| `definition` | Compact source-faithful description where the source provides one. |
| `aliases` | Historical/compatibility labels and their disposition, where applicable. |
| `notes` | Non-authoritative implementation or assessment metadata needed for downstream formalization. |

The common envelope does **not** mean all element kinds are semantically interchangeable. `PLANE`, `OVERLAY`, `ARCHITECTURE_INVARIANT`, `REFERENCE_VIEW` and `LIFECYCLE_STAGE`, for example, remain different types with different later relationship and constraint rules.

---

# 6. Canonicality model

A1 uses two canonicality classes.

## 6.1 `FROZEN_SOURCE_ID`

The human-readable baseline already provides an explicit canonical identifier. A1 reuses it exactly.

Examples:

```text
HDIP-P1
HDIP-X4
HDIP-P2-ABB-03
HDIP-REG-01
HDIP-M12-INT-17
HDIP-BND-11
M14-RP-03
M14-PP-05
M15-V08
M15-FLOW-10
M16-I44
CS4
```

## 6.2 `FROZEN_CANONICAL_MACHINE_ID`

The human-readable baseline freezes a canonical construct/name but does not assign a unique numbered machine identifier. A1 assigns one solely so later artifacts can refer to that frozen construct deterministically.

Examples:

```text
HDIP-CLA-ART-HPD
HDIP-CLA-LIFECYCLE-PDEP
HDIP-CLA-PDEP-STAGE-08
HDIP-CLA-EXPERIENCE-CEP
HDIP-M12-F3
```

Such an identifier does **not** create a new architecture element beyond the frozen human-readable construct it denotes.

---

# 7. Identity rules

A1 follows these identity rules:

1. Existing frozen source identifiers are reused verbatim.
2. A1 machine identifiers are ASCII-stable and case-sensitive.
3. An identifier denotes one frozen 0.1 meaning and must not be reused for another meaning.
4. Machine identifiers are not IRIs; canonical IRI design belongs to A5.
5. Human labels may evolve editorially without changing identity only when M17 errata rules permit the wording change without changing meaning.
6. A historical alias is not a second canonical identity.
7. A specialized view or projection does not become identical to its parent construct merely because it has a machine identifier.
8. Registry membership does not establish Productness, authority, conformance or assurance.

---

# 8. A1 element-kind catalogue

A1 freezes the following twenty-two machine element kinds for the 0.1 executable programme:

| Kind | Count | Purpose |
|---|---:|---|
| `PLANE` | 5 | Canonical P1-P5 logical Plane identities. |
| `FOUNDATION` | 1 | HDIP-FND. |
| `OVERLAY` | 9 | X1-X9 cross-cutting responsibilities. |
| `ARCHITECTURE_BUILDING_BLOCK` | 22 | M08 canonical logical ABBs. |
| `LOGICAL_REGISTRY` | 5 | Core M09 Registry identities. |
| `REGISTRY_SPECIALIZATION` | 1 | Data-profile ADS Registry specialization. |
| `ARCHITECTURE_CONSTRUCT` | 3 | Product Lens, Catalog and Marketplace frozen constructs. |
| `PROJECTION_COMPILATION_ARTIFACT` | 7 | HPD, RRG, SYNCTX, RGB, Realization Plan, Blueprint Binding and Compilation Record. |
| `LIFECYCLE` | 2 | PDEP and SSCF. |
| `EXPERIENCE_PROJECTION` | 1 | CEP. |
| `LIFECYCLE_PROJECTION` | 3 | PDEP G0, Spec A and Spec C. |
| `LIFECYCLE_STAGE` | 19 | 11 Data PDEP stages plus 8 SSCF stages. |
| `INTERACTION_FAMILY` | 4 | M12 F1-F4 groupings. |
| `INTERACTION` | 21 | M12 canonical inter-Plane interactions. |
| `BOUNDARY_CLASS` | 6 | M13 BC1-BC6 groupings. |
| `BOUNDARY_FAMILY` | 12 | M13 canonical external/adjacent Boundary Families. |
| `REALIZATION_PATTERN` | 8 | M14 RP-01..08. |
| `PROFILE_PATTERN` | 6 | M14 PP-01..06. |
| `REFERENCE_VIEW` | 10 | M15 V01..V10. |
| `REPRESENTATIVE_FLOW` | 10 | M15 FLOW-01..10. |
| `ARCHITECTURE_INVARIANT` | 48 | M16 I01..I48. |
| `CONFORMANCE_SUBJECT_CLASS` | 6 | M16 CS1..CS6. |

Total registered A1 elements:

```text
209
```

The count is an A1 machine-registry inventory, not a new architecture complexity metric.

---

# 9. Frozen source identifiers reused by A1

A1 reuses **170** existing frozen identifiers without renaming them.

The principal families are:

```text
HDIP-P1..P5
HDIP-FND
HDIP-X1..X9
22 M08 ABB identifiers
HDIP-REG-01..05
HDIP-REG-D01
HDIP-M12-INT-01..21
BC1..BC6
HDIP-BND-01..12
M14-RP-01..08
M14-PP-01..06
M15-V01..V10
M15-FLOW-01..10
M16-I01..I48
CS1..CS6
```

For interactions, the full canonical M12 identifier is retained (`HDIP-M12-INT-xx`) and the accepted M17 shorthand (`INT-xx`) is recorded as `shortId` rather than becoming a competing identity.

---

# 10. Machine identifiers assigned by A1

A1 assigns **39** representation-only identifiers to previously unnumbered frozen constructs.

## 10.1 Product/discovery constructs

```text
HDIP-CLA-CONSTRUCT-PRODUCT-LENS
HDIP-CLA-CONSTRUCT-CATALOG
HDIP-CLA-CONSTRUCT-MARKETPLACE
```

## 10.2 Projection / compilation artifacts

```text
HDIP-CLA-ART-HPD
HDIP-CLA-ART-RRG
HDIP-CLA-ART-SYNCTX
HDIP-CLA-ART-RGB
HDIP-CLA-ART-REALIZATION-PLAN
HDIP-CLA-ART-BLUEPRINT-BINDING
HDIP-CLA-ART-COMPILATION-RECORD
```

## 10.3 Lifecycle / experience constructs

```text
HDIP-CLA-LIFECYCLE-PDEP
HDIP-CLA-LIFECYCLE-SSCF
HDIP-CLA-EXPERIENCE-CEP

HDIP-CLA-PROJECTION-PDEP-G0
HDIP-CLA-PROJECTION-PDEP-SPEC-A
HDIP-CLA-PROJECTION-PDEP-SPEC-C
```

## 10.4 Lifecycle stages

```text
HDIP-CLA-PDEP-STAGE-00 .. HDIP-CLA-PDEP-STAGE-10
HDIP-CLA-SSCF-STAGE-01 .. HDIP-CLA-SSCF-STAGE-08
```

These machine stage identifiers do not turn lifecycle stages into services, ABBs or runtime calls.

## 10.5 Interaction-family identifiers

```text
HDIP-M12-F1  -> source family F1 — Governed Context & Authority
HDIP-M12-F2  -> source family F2 — Discovery, Realization & Publication
HDIP-M12-F3  -> source family F3 — Runtime & Provision
HDIP-M12-F4  -> source family F4 — Consumption, Outcome & Evolution
```

The F1-F4 families remain organizational groupings only; the machine identifiers do not create four integration buses or control layers.

---

# 11. Lifecycle registration discipline

A1 registers lifecycle constructs because later A8 schemas and A9-A12 tests need stable references, but their architectural status remains unchanged.

```text
PDEP != Plane
SSCF != Plane
CEP  != Plane
lifecycle stage != service
lifecycle stage != ABB
lifecycle stage != mandatory synchronous runtime hop
```

The Data PDEP specialization is registered as eleven stages:

```text
Stage 0 + Stages 1-10
```

The SSCF lifecycle is registered as eight stages:

```text
Stages 1-8
```

PDEP G0, Spec A and Spec C are registered separately from the lifecycle because they are progressive projections of the canonical lifecycle rather than alternative lifecycle identities.

---

# 12. Compatibility and alias registry

A1 encodes the frozen M17 compatibility ledger as mappings, not new canonical elements.

| Historical / earlier term | A1 disposition |
|---|---|
| `SSPD` | retired to PDEP identity |
| `Consumer Experience Plane` | historical expansion of CEP |
| `DPFI / Data Product Factory & Intelligence` | responsibilities map to P2 ABBs; no single replacement component |
| `COVP` | decomposed to X4, X9 and P5 responsibility areas |
| `Data Product Registry` | Data-profile view of Product Registry |
| `Resolved Product Graph` | Product-scoped view of RRG |
| `Unified Governance Bundle (UGB)` | historical alias of RGB |
| `Logical Execution Plan` | execution-focused specialized view of Realization Plan |
| `Selected Blueprint` | source/reference within Blueprint Binding |

Compatibility mappings are intentionally typed. `HISTORICAL_ALIAS_OF`, `DECOMPOSED_TO` and `PRODUCT_SCOPED_VIEW_OF` are not interchangeable assertions.

A2 will later formalize mapping relationships; A1 only preserves the frozen disposition faithfully.

---

# 13. Controlled vocabulary seed

A1 includes the following exact M16 tokens so later machine artifacts do not drift lexically:

## Assessment mode

```text
STRUCTURAL
HYBRID
ASSESSMENT
```

## Invariant result

```text
SATISFIED
VIOLATED
INDETERMINATE
NOT_APPLICABLE
```

## Overall conformance outcome

```text
CONFORMANT
NONCONFORMANT
INDETERMINATE
```

## Conformance claim type

```text
CORE_ARCHITECTURE_CONFORMANCE
PROFILE_CONFORMANCE
REALIZATION_MAPPING_CONFORMANCE
```

These are controlled machine tokens, not new architecture elements.

---

# 14. Authority boundaries in the registry

A1 does not register GEDRM, GEARM, GEAIRM, BPS/PIN, AIPS or other external authorities as HDIP-owned architecture elements.

Later A2 mappings may reference external authorities, but A1 preserves the M17 rule:

```text
reference != ownership
machine identifier != authority transfer
serialization != semantic annexation
```

The A1 registry must therefore never be interpreted as a universal ontology containing copied authoritative definitions from adjacent specifications.

---

# 15. Registry versus HDIP runtime Registries

The **A1 Architecture Element Registry** is a specification/formalization artifact.

It is not identical to any M09 runtime logical Registry:

```text
A1 Architecture Element Registry
    != HDIP-REG-01 Product Registry
    != HDIP-REG-02 Schema Registry
    != HDIP-REG-03 Policy Registry
    != HDIP-REG-04 Capability Registry
    != HDIP-REG-05 Blueprint Registry
    != HDIP-REG-D01 ADS Registry
```

The A1 registry records architecture identities. M09 Registries describe governed enterprise platform responsibilities.

---

# 16. Source-document discipline

Every A1 element must identify one or more repository source documents.

A1 source links serve three purposes:

1. allow deterministic reconciliation back to the human-readable baseline;
2. make later machine artifacts explainable;
3. prevent a machine label from becoming detached from the normative source meaning.

A2 will extend this into explicit source/upstream traceability relationships. A1 source documents are provenance pointers, not full relationship semantics.

---

# 17. Versioning and change policy

A1 is versioned as part of the HDIP-CLA 0.1 executable programme.

Within 0.1:

- an existing `FROZEN_SOURCE_ID` must not be repurposed;
- an A1 machine identifier must not be reassigned to a different frozen construct;
- non-semantic errata may correct labels/source pointers where M17 permits;
- material architecture change requires governed human-readable amendment/versioning first;
- A1 then reconciles to the revised authority rather than leading the change.

A1 status or serialization changes do not themselves change architecture currentness.

---

# 18. A1 structural validation requirements

A1 validation must establish at least:

- the registry JSON parses;
- all `id` values are unique;
- every element uses one of the frozen A1 element kinds;
- every element has a canonical name, canonicality class, status and source document;
- all reused source-ID families have expected counts;
- all A1 machine-ID families have expected counts;
- the five Planes, one Foundation, nine Overlays and twenty-two ABBs are present;
- all M09 Registry identities are present;
- all nineteen lifecycle stages are present;
- all twenty-one interactions are present;
- all twelve Boundary Families are present;
- all M14/M15 pattern/view/flow identifiers are present;
- all forty-eight M16 invariants are present;
- no duplicate short interaction identity creates a second canonical element;
- compatibility mappings target registered elements;
- the CSV projection contains the same element identities as JSON;
- no source document referenced by A1 is missing from the repository.

A1 validation is structural. It does not prove that every architecture statement is semantically correct or that a concrete enterprise realization conforms to HDIP.

---

# 19. A1 anti-patterns

A1 freezes these identity/formalization anti-patterns:

1. **Machine-name redesign** — renaming frozen identifiers because another spelling is easier to serialize.
2. **IRI-before-identity** — allowing URI/IRI design to decide architecture identity before A5.
3. **One-generic-element collapse** — treating all registry records as semantically interchangeable because they share one JSON envelope.
4. **Alias resurrection** — issuing a new canonical element for a retired historical term.
5. **Stage-as-component** — turning PDEP/SSCF stages into services or ABBs because they now have IDs.
6. **Projection-as-authority** — treating HPD/RRG/SYNCTX/RGB machine identities as authority ownership.
7. **Registry-registry confusion** — confusing the A1 specification registry with M09 operational Registries.
8. **Short-ID duplication** — creating `INT-01` as a second element alongside `HDIP-M12-INT-01`.
9. **Boundary annexation** — registering external semantic/Product authorities as HDIP-owned elements.
10. **Controlled-value promotion** — turning result/status tokens into architecture elements without justification.
11. **Machine-ID Productness** — inferring Product identity because a construct has an A1 identifier.
12. **Serialization truth** — treating JSON output as more authoritative than M17 source meaning.
13. **Count-as-quality** — treating 209 registered elements as a maturity or conformance score.
14. **Definition invention** — filling an absent source definition with unsupported machine prose.
15. **Compatibility-as-equivalence** — treating all historical mappings as exact synonyms.
16. **Rule disappearance** — assuming rules not individually registered in A1 are no longer normative.
17. **Automated judgement creep** — treating A1 structural validation as proof of HYBRID/ASSESSMENT invariants.
18. **Cross-version identifier reuse** — reusing an identifier for materially different meaning after governed version change.

---

# 20. Canonical A1 normative rules

**HDIP-CLA-A1-R01 — Human-readable precedence.** The M17-frozen human-readable HDIP-CLA 0.1 baseline SHALL remain authoritative over A1 and all downstream machine-readable artifacts.

**HDIP-CLA-A1-R02 — Formalization only.** A1 SHALL register frozen architecture identity and SHALL NOT introduce new architecture semantics under the guise of machine readability.

**HDIP-CLA-A1-R03 — Source-ID reuse.** Where the frozen human-readable baseline already assigns a canonical identifier, A1 SHALL reuse that identifier rather than invent a replacement.

**HDIP-CLA-A1-R04 — Machine-ID restraint.** A1 MAY assign a machine identifier only to an already-frozen unnumbered canonical construct that requires deterministic downstream reference.

**HDIP-CLA-A1-R05 — Machine-ID non-authority.** An A1-assigned machine identifier SHALL NOT create new semantic, Product, policy, source, Decision or architecture authority.

**HDIP-CLA-A1-R06 — Identifier uniqueness.** Every A1 `id` SHALL be unique within the HDIP-CLA 0.1 Architecture Element Registry.

**HDIP-CLA-A1-R07 — Identifier immutability.** An A1 identifier SHALL NOT be reused for a materially different meaning within the same frozen 0.1 baseline.

**HDIP-CLA-A1-R08 — Canonical name fidelity.** `canonicalName` SHALL preserve the accepted human-readable term rather than normalize terminology in a way that changes architectural meaning.

**HDIP-CLA-A1-R09 — Typed identity.** Every A1 element SHALL declare an element `kind`; shared JSON structure SHALL NOT imply semantic equivalence between kinds.

**HDIP-CLA-A1-R10 — Source provenance.** Every A1 element SHALL reference at least one human-readable source document from which its identity/meaning is derived.

**HDIP-CLA-A1-R11 — Plane inventory.** A1 SHALL register exactly HDIP-P1 through HDIP-P5 as the five canonical Plane identities for 0.1.

**HDIP-CLA-A1-R12 — Foundation inventory.** A1 SHALL register HDIP-FND as the Shared Platform / Utility Foundation and SHALL NOT type it as a sixth Plane.

**HDIP-CLA-A1-R13 — Overlay inventory.** A1 SHALL register HDIP-X1 through HDIP-X9 as the nine canonical Overlay identities.

**HDIP-CLA-A1-R14 — ABB inventory.** A1 SHALL register the twenty-two canonical M08 ABB identifiers without creating stage-, Registry-, artifact- or view-derived ABBs.

**HDIP-CLA-A1-R15 — Registry inventory.** A1 SHALL register HDIP-REG-01 through HDIP-REG-05 as core logical Registries and HDIP-REG-D01 as the Data-profile ADS Registry specialization.

**HDIP-CLA-A1-R16 — Registry non-qualification.** Inclusion of a construct in the A1 registry SHALL NOT establish Productness, source authority, policy authority, control effectiveness, fitness, assurance or HDIP conformance.

**HDIP-CLA-A1-R17 — Product-lens preservation.** The orthogonal Product Lens SHALL remain distinct from Planes, Overlays and runtime Registries in A1 typing.

**HDIP-CLA-A1-R18 — Catalog/Marketplace distinction.** Catalog and Marketplace SHALL receive distinct machine identities and SHALL NOT be collapsed into Registry merely because an implementation may co-realize them.

**HDIP-CLA-A1-R19 — Artifact inventory.** A1 SHALL register HPD, RRG, SYNCTX, RGB, Realization Plan, Blueprint Binding and Compilation Record as projection/compilation artifacts rather than ABBs or authorities.

**HDIP-CLA-A1-R20 — Projection non-authority.** Machine identity for a projection/compiled artifact SHALL NOT transfer authority from the semantic, Product, policy or source inputs it references.

**HDIP-CLA-A1-R21 — PDEP identity.** A1 SHALL register PDEP as the canonical Product Development & Evolution lifecycle and SHALL treat SSPD only according to its frozen historical disposition.

**HDIP-CLA-A1-R22 — Data PDEP stages.** A1 SHALL register the canonical Data PDEP specialization as Stage 0 plus Stages 1-10 and SHALL NOT generalize those stages to all Product families by registry design.

**HDIP-CLA-A1-R23 — PDEP projections.** PDEP G0, Spec A and Spec C SHALL be registered as lifecycle projections and SHALL NOT become competing lifecycle identities.

**HDIP-CLA-A1-R24 — SSCF identity.** A1 SHALL register SSCF as the canonical logical Product-consumption lifecycle with eight stages.

**HDIP-CLA-A1-R25 — CEP identity.** A1 SHALL register CEP as Consumer Experience Projection and SHALL NOT restore Consumer Experience Plane as canonical topology.

**HDIP-CLA-A1-R26 — Lifecycle non-runtime.** Assignment of machine IDs to lifecycle stages SHALL NOT imply mandatory synchronous runtime sequencing, a stage-per-service model or stage-per-ABB realization.

**HDIP-CLA-A1-R27 — Interaction identity.** A1 SHALL register HDIP-M12-INT-01 through HDIP-M12-INT-21 as the canonical interaction identities.

**HDIP-CLA-A1-R28 — Interaction shorthand.** `INT-01` through `INT-21` MAY be stored as shorthand but SHALL NOT become duplicate canonical interaction elements.

**HDIP-CLA-A1-R29 — Interaction-family scope.** A1 machine identifiers for F1-F4 SHALL represent organizational interaction families only and SHALL NOT imply buses, gateways or control tiers.

**HDIP-CLA-A1-R30 — Boundary classes.** A1 SHALL register BC1 through BC6 as Boundary Class groupings without interpreting them as gateway topology.

**HDIP-CLA-A1-R31 — Boundary families.** A1 SHALL register HDIP-BND-01 through HDIP-BND-12 as canonical Boundary Families and SHALL preserve their external-jurisdiction character.

**HDIP-CLA-A1-R32 — External-authority non-annexation.** A1 SHALL NOT reclassify adjacent semantic, Product, policy, source, peer-architecture or Decision authorities as HDIP-owned architecture elements.

**HDIP-CLA-A1-R33 — Realization-pattern inventory.** A1 SHALL register M14-RP-01 through M14-RP-08 as Realization Patterns rather than maturity levels or architecture elements that alter core meaning.

**HDIP-CLA-A1-R34 — Profile-pattern inventory.** A1 SHALL register M14-PP-01 through M14-PP-06 as Profile Pattern families and SHALL NOT treat a Profile as a waiver mechanism.

**HDIP-CLA-A1-R35 — View inventory.** A1 SHALL register M15-V01 through M15-V10 as Reference Views and SHALL NOT create view-specific copies of canonical architecture identities.

**HDIP-CLA-A1-R36 — Flow inventory.** A1 SHALL register M15-FLOW-01 through M15-FLOW-10 as representative flows and SHALL NOT turn any flow into a universal lifecycle.

**HDIP-CLA-A1-R37 — Invariant inventory.** A1 SHALL register M16-I01 through M16-I48 exactly once and SHALL retain their assessment-mode metadata for A3 handoff.

**HDIP-CLA-A1-R38 — Conformance-subject inventory.** A1 SHALL register CS1 through CS6 as Conformance Subject classes without asserting that any particular subject is conformant.

**HDIP-CLA-A1-R39 — Controlled-token fidelity.** A1 SHALL preserve exact M16 controlled tokens for assessment modes, invariant results and overall conformance outcomes.

**HDIP-CLA-A1-R40 — No conditional-pass invention.** A1 SHALL NOT introduce `CONDITIONALLY_CONFORMANT` or another positive conformance outcome absent from the frozen M16 model.

**HDIP-CLA-A1-R41 — Compatibility mapping typing.** Historical terminology mappings SHALL record their disposition type and SHALL NOT treat decomposition, specialization, scoped view and exact alias as equivalent relations.

**HDIP-CLA-A1-R42 — Alias non-resurrection.** Historical aliases SHALL NOT acquire canonical status merely because A1 records them for migration or traceability.

**HDIP-CLA-A1-R43 — Normative-rule preservation.** M01-M17 normative rules remain normative even though A1 does not register all 818 rules as architecture elements; later traceability/formalization SHALL preserve their applicability.

**HDIP-CLA-A1-R44 — IRI deferral.** A1 machine IDs SHALL NOT be represented as final canonical IRIs; namespace/IRI design belongs to A5.

**HDIP-CLA-A1-R45 — Relationship deferral.** A1 source pointers and compatibility mappings SHALL NOT substitute for the canonical relationship/traceability model to be defined in A2.

**HDIP-CLA-A1-R46 — Conformance-execution deferral.** A1 structural validation SHALL NOT be represented as executable proof of HYBRID or ASSESSMENT invariants; executable conformance belongs to A3/A6/A12 as applicable.

**HDIP-CLA-A1-R47 — Deterministic serialization.** The canonical A1 JSON registry SHALL serialize the same registered identity set deterministically so that later reconciliation/regression can detect drift.

**HDIP-CLA-A1-R48 — A2 handoff.** A2 SHALL build the canonical Relationship & Traceability Registry from A1 identities while preserving all M17 authority, distinction and non-equivalence boundaries.

---

# 21. A1 completion state

**HDIP-CLA A1 — COMPLETE.**

A1 establishes:

- one canonical Architecture Element Registry;
- **209** registered machine-addressable frozen elements;
- **22** element kinds;
- **170** reused frozen source identifiers;
- **39** representation-only machine identifiers for previously unnumbered frozen constructs;
- exact registration of **5 Planes + 1 Foundation + 9 Overlays + 22 ABBs**;
- **5** core logical Registries plus **1** Data-profile Registry specialization;
- **7** canonical projection/compilation artifacts;
- PDEP, SSCF and CEP machine identities;
- **19** lifecycle-stage identities;
- **4** M12 interaction-family identities and **21** canonical interactions;
- **6** M13 Boundary Classes and **12** Boundary Families;
- **8** M14 Realization Patterns and **6** Profile Patterns;
- **10** M15 Reference Views and **10** representative flows;
- **48** M16 Architecture Invariants and **6** Conformance Subject classes;
- four seeded M16 controlled vocabularies;
- **9** typed compatibility/historical terminology mappings;
- **18** A1 anti-patterns;
- **48** normative A1 rules.

A1 introduces no new HDIP Plane, Foundation, Overlay, ABB, Registry responsibility, lifecycle meaning, M12 interaction, M13 Boundary Family, M14 pattern, M15 view/flow or M16 invariant.

### Next stage

> **A2 — Canonical Relationship & Traceability Registry**

A2 will define the typed machine relationships among A1 identities: containment/hosting, applicability, projection, specialization, lifecycle membership, interaction direction/participation, Boundary classification, realization/profile usage, view/flow projection, invariant coverage and explicit source/upstream authority traceability — without turning mapping into equivalence or authority transfer.
