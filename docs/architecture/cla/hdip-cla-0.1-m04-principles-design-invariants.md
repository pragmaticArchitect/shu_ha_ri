---
id: hdip-cla-0.1-m04-principles-design-invariants
title: HDIP-CLA 0.1 M04 - Canonical Architecture Principles & Design Invariants
sidebar_label: M04 - Principles & Invariants
---

# HDIP-CLA 0.1 M04 - Canonical Architecture Principles & Design Invariants

**Status:** COMPLETE

## 1. Purpose

M04 establishes the canonical architecture principles and design invariants that constrain the derivation of the **HDIP Canonical Logical Architecture (HDIP-CLA) 0.1**.

M04 sits between evidence collection and architecture derivation:

```text
M01  Authority / scope contract
  +
M02  Upstream responsibility intake
  +
M03  Existing HDIP construct dispositions
  |
  v
M04  Principles + design invariants
  |
  +--> constrain M05 convergence/separation
  +--> constrain M06 plane derivation
  +--> constrain M07 overlay derivation
  +--> constrain M08 ABB admission
  +--> constrain M09-M15 architecture elaboration
  |
  v
M16  formal invariant/conformance model
```

M04 does **not** freeze the final HDIP plane count, plane names, overlay catalogue, ABB catalogue, runtime topology, physical services, registry deployment topology or Product-family lifecycle structure.

---

## 2. Principle versus invariant

M04 deliberately distinguishes two architectural instruments.

### 2.1 Architecture Principle

An **Architecture Principle** states the preferred and enduring design direction for HDIP. A principle guides derivation and trade-off decisions but may contain contextual judgement.

### 2.2 Design Invariant

A **Design Invariant** is a condition that later HDIP-CLA derivation SHALL preserve unless the HDIP-CLA baseline itself is explicitly revised through governed change.

```text
Principle
  = direction for good HDIP architecture

Design Invariant
  = condition the derived architecture must not violate
```

M16 will later convert the applicable invariant set into a formal conformance model, including assessment modes, evidence requirements, applicability and violation consequences. M16 may refine or decompose M04 invariants where needed, but SHALL NOT silently weaken their meaning.

---

## 3. Derivation basis

M04 is derived from four evidence classes.

| Evidence class | M04 use |
|---|---|
| **M01 authority contract** | Establishes HDIP jurisdiction, semantic/Product authority boundaries, technology neutrality, responsibility-first derivation, projection non-authority and historical meaning. |
| **M02 upstream intake** | Preserves 336 source responsibility/obligation statements across GEDRA, GEARA and GEAIRA and prevents label-driven convergence. |
| **M03 existing HDIP inventory** | Preserves useful HDIP constructs while preventing historical boxes, service names, lifecycle aliases or implementation assumptions from becoming architecture by inheritance. |
| **Upstream architecture principles/invariants** | Supplies compatible generic constraints concerning scoped authority, logical planes, topology independence, governed self-service, evidence, lifecycle, interoperability and shared-platform non-merger. |

The M04 result is therefore an **HDIP architecture contract**, not a copy of any one source architecture's principle catalogue.

---

# 4. Canonical HDIP Architecture Principles

M04 establishes eighteen canonical architecture principles.

## M04-P01 - Federated Authority Preservation

HDIP should compose enterprise capability without centralizing semantic, Product, policy, decision or domain authority merely because the platform can technically host, index, execute or project the corresponding information.

> **Platform coordination is not authority consolidation.**

## M04-P02 - Holistic Co-Realization Without Domain Collapse

HDIP should provide one coherent platform experience across **Data, Information and Intelligence** while preserving the distinctions, semantic authorities and architecture responsibilities that make those domains different.

```text
one platform experience
    !=
one semantic model
    !=
one Product family
    !=
one architecture jurisdiction
```

## M04-P03 - Responsibility Before Structure

Canonical planes, overlays, ABBs, interactions and control points should be derived from enduring architectural responsibilities before choosing components, services, registries, teams, technologies or diagram boxes.

## M04-P04 - Logical Architecture Before Deployment Topology

HDIP-CLA should describe what must be enabled, governed, preserved, observed and coordinated independently of whether realization is centralized, federated, distributed, embedded, cloud-hosted, on-premise or hybrid.

## M04-P05 - Meaning and Intent Before Realization

Business meaning, governed intent, applicable authority and required outcomes should be explicit before technical realization choices are allowed to dominate the architecture.

For Data, this preserves GEDRA's meaning-before-movement discipline. For Information and Intelligence, the same principle preserves governed intent/context before runtime realization.

## M04-P06 - Product Qualification Is Orthogonal

Productization should remain an intentional qualification governed by BPS/PIN and applicable Product-family specifications. HDIP should support both Products and governed non-Product capabilities without manufacturing Productness from deployment, persistence, publication, API exposure, registration or reuse.

## M04-P07 - Governed Self-Service

HDIP should reduce unnecessary organizational and engineering mediation while keeping policy, authority, accountability, evidence and material judgement explicit.

Self-service means **bounded autonomy with guardrails**, not ungoverned infrastructure access.

## M04-P08 - Platform-Supplied Engineering

Where a participant can express governed intent declaratively, HDIP should supply avoidable engineering effort through discovery, validation, resolution, compilation, provisioning and automation rather than forcing each participant to reconstruct platform mechanics.

This principle does not remove accountable human judgement where judgement is genuinely required.

## M04-P09 - Interaction-Distance Reduction

HDIP should reduce the effective organizational, technological, semantic and governance distance between independent Product/capability participants and their consumers.

This is the architectural principle underlying the **DII Wormhole** analogy:

> **The platform does not eliminate participant independence; it makes unnecessary distance less consequential to governed interaction and value realization.**

## M04-P10 - Explicit Contractual Interoperability

Material interactions should cross boundaries through explicit, version-aware architectural contracts rather than hidden coupling or shared implementation assumptions.

An architectural contract need not map one-to-one to a single API, protocol or schema.

## M04-P11 - Evidence by Construction

Material lifecycle, compilation, deployment, consumption and runtime interactions should produce applicable provenance, policy/control, quality, observability and outcome evidence as a natural consequence of operation rather than as an after-the-fact documentation exercise.

## M04-P12 - Evidencable and Contextual Trust

Trust should be supported by relevant evidence for a declared purpose and context. Platform location, popularity, centralization, registration or a generic score should not substitute for evidence of fitness, provenance, currentness, assurance or applicable controls.

## M04-P13 - Projection and Compilation Without Authority Capture

HDIP-generated artifacts may make authoritative information computable, correlated and operationally useful, but projection or compilation should not silently become a new source of semantic or governance authority.

Examples include HPD, SYNCTX, resolved graphs, compilation packs and resolved governance bundles.

## M04-P14 - Cross-Cutting Obligations Remain Visible

Governance, security/privacy, provenance/evidence, quality/trust, lifecycle/change and related cross-cutting responsibilities should remain visible across whichever logical planes later emerge. A convenient implementation location should not hide their cross-cutting applicability.

## M04-P15 - Registry, Catalog and Marketplace Separation

HDIP should distinguish:

```text
Registry
  governed registration / identity responsibility

Catalog
  discovery / search / projection responsibility

Marketplace
  consumer-facing discovery / acquisition experience
```

They may share implementation, but their architectural meanings should remain distinct.

## M04-P16 - Versioned Evolution and Historical Interpretability

HDIP should treat semantic, Product, contract, interface, process/logic, realization, deployment, policy/control, evidence and assurance evolution as distinguishable dimensions and preserve the historical meaning of material occurrences.

## M04-P17 - Progressive Experience Without Competing Semantics

HDIP may provide multiple experience projections of one canonical lifecycle or architecture - for example PDEP G0, PDEP Spec A and PDEP Spec C - but simplified views should remain projections of the canonical model rather than competing sources of lifecycle semantics.

## M04-P18 - Monotonic Specialization

Domain, Product-family, industry and enterprise profiles may tighten, contextualize and extend HDIP where appropriate, but specialization should preserve applicable parent meaning and invariants rather than weaken or redefine them incompatibly.

---

# 5. Canonical M04 Design Invariants

M04 establishes forty design invariants grouped into six families.

## 5.1 Authority, semantics and jurisdiction

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I01** | Semantic authority preservation | HDIP-CLA SHALL NOT incompatibly redefine concepts, relationships or invariants owned by GEDRM, GEARM, GEAIRM or other applicable semantic authorities. |
| **M04-I02** | Product authority preservation | Generic Product identity, Product Intrinsic Nature and Product qualification SHALL remain governed by BPS/PIN rather than inferred by HDIP. |
| **M04-I03** | Product-family authority preservation | Data Product, Information Product, AI Product and other Product-family qualification/classification SHALL remain with the applicable Product-family authority. |
| **M04-I04** | Scoped authority | Authority used by HDIP SHALL be explicit for an applicable scope, role, purpose, lifecycle state and/or jurisdiction where those distinctions matter; platform participation SHALL NOT imply universal authority. |
| **M04-I05** | Shared-realization non-transfer | Co-location, shared storage, shared runtime, shared registry, shared UI or shared platform realization SHALL NOT by itself transfer semantic, Product, policy, decision or ownership authority. |
| **M04-I06** | Semantic-gap escalation | Where HDIP needs a semantic concept not owned by HDIP, the gap SHALL be referred to or extended through the appropriate semantic authority rather than silently minted as platform semantics. |
| **M04-I07** | Authority non-transitivity | Authority, approval, entitlement, policy applicability or ownership SHALL NOT become automatically transitive merely because a dependency, composition or interaction crosses an HDIP boundary. |

## 5.2 Responsibility, structure and topology

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I08** | Responsibility before component | A canonical HDIP ABB or mandatory implementation responsibility SHALL be justified by explicit architectural responsibility; a noun, tool, service label or historical box alone is insufficient. |
| **M04-I09** | Logical plane semantics | A future HDIP Plane SHALL represent a coherent logical responsibility grouping and SHALL NOT imply a mandatory system, deployment unit, network tier, team, organizational boundary or lifecycle step. |
| **M04-I10** | Topology independence | HDIP-CLA conformance SHALL NOT depend on centralized, federated, distributed, edge, embedded, provider-managed or hybrid deployment topology unless a narrower Profile explicitly requires it. |
| **M04-I11** | Many-to-many realization | One implementation MAY realize responsibilities from several HDIP logical structures, and one HDIP responsibility MAY be distributed across several implementations. |
| **M04-I12** | Source-plane non-equivalence | GEDRA, GEARA and GEAIRA plane numbering, placement or lexical similarity SHALL NOT force one-to-one HDIP plane mapping. |
| **M04-I13** | Cross-cutting visibility | A responsibility that is cross-cutting in an applicable source architecture SHALL NOT be silently localized into one future HDIP plane without explicit justification that preserves its cross-cutting obligations. |
| **M04-I14** | Foundation separation | Compute, storage, networking, messaging, identity infrastructure, orchestration and other utility capabilities SHALL NOT acquire semantic, Product, governance or domain authority merely because they enable those responsibilities. |
| **M04-I15** | Architecture traceability | Every future canonical HDIP Plane, Overlay, ABB and material interaction SHALL trace to upstream responsibilities, explicit enterprise platform requirements and/or justified HDIP-specific coordination responsibilities. |

## 5.3 Data, Information, Intelligence and Product identity

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I16** | Domain distinction | Data, Information and Intelligence SHALL remain distinguishable architectural/semantic concerns even where one platform capability co-realizes responsibilities from more than one domain. |
| **M04-I17** | No cross-domain inheritance | A Data-specific, Information-specific or Intelligence-specific construct SHALL NOT automatically generalize to the other domains through shared implementation or naming similarity. |
| **M04-I18** | No automatic Productness | Composition, generation, transformation, persistence, deployment, publication, registration, cataloguing, marketplace presence, API exposure, repeated use or consumption SHALL NOT by itself establish Product identity. |
| **M04-I19** | Product-family distinction | Co-realization of Data Products, Information Products and AI Products SHALL NOT collapse them into one HDIP-local Product family or type. |
| **M04-I20** | Composition non-inheritance | Using, depending on, containing, deriving from or invoking a Product/capability SHALL NOT by itself transfer its Product family, ontology type, ownership or authority to the dependent/composed result. |
| **M04-I21** | Direct capability validity | HDIP SHALL be able to support governed Data, Information or Intelligence capability use where Product qualification is not intended; Productization SHALL NOT be a mandatory gateway for every governed interaction. |

## 5.4 Governed self-service, lifecycle and experience

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I22** | Governed self-service | Self-service SHALL operate inside applicable authority, policy, security, privacy, quality, evidence and lifecycle constraints; self-service SHALL NOT mean unrestricted infrastructure or data access. |
| **M04-I23** | Intent/compilation separation | Participant-declared intent, business semantics and accountable judgement SHALL remain distinguishable from platform resolution, compilation, provisioning and automation. |
| **M04-I24** | Automation non-ownership | HDIP automation SHALL NOT transfer Product ownership, Data authority, policy authority or decision accountability to the compiler/runtime merely because the platform performs most technical work. |
| **M04-I25** | Judgement honesty | Architecture/governance decisions requiring contextual or accountable judgement SHALL NOT be represented as machine-proven solely because metadata, telemetry, rules or model outputs exist. |
| **M04-I26** | PDEP canonical lifecycle identity | PDEP SHALL remain the canonical HDIP Product Development and Evolution Process identity; historical SSPD terminology MAY remain only for traceability and SHALL NOT become a competing lifecycle. |
| **M04-I27** | Progressive PDEP projection | PDEP G0 and PDEP Spec A MAY compress/group canonical stages for progressive disclosure, while PDEP Spec C SHALL remain synchronized with the canonical applicable detailed PDEP lifecycle. |
| **M04-I28** | Experience non-authority | Interactive flow players, diagrams, dashboards and experience projections SHALL NOT independently create lifecycle stages, authority, Product identity, ABBs or architecture semantics. |

## 5.5 Projection, compilation, registry and discovery

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I29** | Projection non-authority | HPD, SYNCTX, resolved graphs, compiled governance bundles, compilation packs and similar HDIP-generated projections SHALL NOT override the authoritative semantics or governance sources they reference. |
| **M04-I30** | Compiler non-invention | HDIP resolution/compilation SHALL NOT manufacture semantic relationships, Product identity, policy authority, joinability, provenance, dependencies or obligations from weak evidence or naming similarity. |
| **M04-I31** | Logical registry independence | ADS, Product, Schema, Policy, Capability and Blueprint registry responsibilities SHALL remain logically distinguishable even where one implementation realizes several of them. |
| **M04-I32** | Registry non-qualification | Registration SHALL NOT by itself prove authoritative status, Product status, control effectiveness, semantic correctness, fitness or HDIP conformance. |
| **M04-I33** | Registry/catalog/marketplace distinction | Registry, Catalog and Marketplace responsibilities SHALL NOT be treated as architectural synonyms even when exposed through one user experience or implementation. |
| **M04-I34** | Shared registry realization allowed | HDIP MAY consolidate registry implementation where operationally useful provided logical identities, ownership, contracts, lifecycle and authority boundaries remain distinguishable. |

## 5.6 Evidence, trust, version and historical meaning

| ID | Name | Canonical design invariant |
|---|---|---|
| **M04-I35** | Evidence by construction | Material HDIP interactions SHOULD emit or retain applicable provenance, control, quality, observability and lifecycle evidence sufficient for later reconstruction and assessment. |
| **M04-I36** | Trust is contextual | Platform location, certification label, popularity, centralization, Product status or registry presence SHALL NOT be treated as universal proof of trust or fitness; trust assessment SHALL remain contextual and evidence-based. |
| **M04-I37** | Missing evidence is not positive evidence | Missing, stale, inaccessible or materially ambiguous evidence SHALL NOT be interpreted as positive assurance. |
| **M04-I38** | Version/currentness distinction | Version identity, latest/newest status and governed currentness SHALL remain distinguishable; newest SHALL NOT automatically mean current or approved. |
| **M04-I39** | Historical truth | Later supersession, revocation, re-evaluation, upstream change, rollback or re-publication SHALL NOT silently rewrite which semantics, Product Version, policy/control, dependency, context or realization governed a historical occurrence. |
| **M04-I40** | Provenance is not assurance | Provenance and lineage SHALL support traceability but SHALL NOT by themselves prove correctness, authorization, control effectiveness, assurance or Fitness for Use. |

---

# 6. DII Wormhole architectural interpretation

The DII Wormhole remains an **evocative non-normative model**, but M04 establishes the architecture properties that make the analogy legitimate.

```text
Conventional interaction
  participant
      |
      +-- organizational mediation
      +-- bespoke engineering
      +-- hidden semantics
      +-- manual governance navigation
      +-- discovery friction
      +-- repeated integration
      |
      v
  consumer

HDIP interaction
  independent participant
      |
      +-- discoverable governed capability/Product
      +-- explicit contract
      +-- authoritative references
      +-- policy-aware access/consumption
      +-- platform-supplied engineering
      +-- evidencable trust
      |
      v
  independent consumer
```

The architectural objective is therefore **interaction-distance reduction**, not removal of participant independence or governance boundaries.

```text
shorter effective distance
    !=
bypass authority
    !=
bypass policy
    !=
semantic collapse
    !=
automatic trust
```

This interpretation provides a useful test for later architecture derivation:

> A canonical HDIP structure should exist because it reduces avoidable interaction cost, preserves necessary independence/authority, or supplies reusable governance/evidence/engineering capability - not because an older diagram happened to contain a box for it.

---

# 7. Design consequences for M05-M08

M04 directly constrains the next four derivation stages.

## 7.1 M05 - Responsibility Convergence & Separation

M05 SHALL distinguish at least four outcomes when comparing source responsibilities:

```text
CONVERGE
  materially same enterprise platform responsibility can be co-realized

CO-REALIZE BUT KEEP DISTINCT
  operational realization may be shared, but semantic/authority responsibility remains distinct

SEPARATE
  distinct responsibilities require explicit architectural separation

PROFILE / SPECIALIZE
  responsibility is legitimate only for a domain, Product family or context
```

Lexical similarity alone is insufficient for `CONVERGE`.

## 7.2 M06 - Plane Derivation

A Plane candidate must demonstrate:

- coherent enduring responsibilities;
- meaningful architectural boundary;
- non-redundancy with other candidate Planes;
- source traceability;
- technology/topology independence;
- compatibility with cross-cutting obligations;
- usefulness beyond one historical implementation diagram.

M06 SHALL NOT create a Plane merely to preserve PDEP, Governance, Utility, CEP, COVP or any other historical label.

## 7.3 M07 - Overlay Derivation

M07 must explicitly test recurring concerns such as:

- governance / policy / assurance;
- security / privacy / entitlement;
- provenance / evidence / observability;
- quality / trust;
- lifecycle / version / change;
- economic / cost concerns where cross-cutting evidence supports them.

The presence of similar upstream Fabrics/Overlays is strong evidence but not an automatic HDIP overlay decision.

## 7.4 M08 - ABB Admission

A canonical ABB candidate must be justified by a cohesive responsibility set and must remain:

- technology-neutral;
- realization-independent;
- traceable;
- non-duplicative;
- architecturally useful to name independently.

Historical labels such as `Policy Service`, `Assertion Compiler`, `Blueprint Resolver`, `Deployer`, `CEP Renderer`, `Observability Engine` or `Value Computation Engine` do not pass this test merely by existing in prior flows.

---

# 8. M04 normative rules

The principles and invariants above are themselves canonical M04 architecture constructs. The following rules govern how later stages use them.

**HDIP-CLA-M04-R01 - Principle status.** M04-P01 through M04-P18 SHALL be treated as canonical HDIP-CLA 0.1 architecture principles for downstream derivation.

**HDIP-CLA-M04-R02 - Invariant status.** M04-I01 through M04-I40 SHALL constrain M05-M15 architecture derivation unless the HDIP-CLA baseline is explicitly revised through governed change.

**HDIP-CLA-M04-R03 - Invariant precedence over convenience.** Implementation convenience, existing tooling, historical diagrams or organizational ownership SHALL NOT justify violation of an applicable M04 design invariant.

**HDIP-CLA-M04-R04 - No premature topology.** M04 SHALL NOT be interpreted as freezing a Plane count, Overlay count, ABB count, physical topology, service decomposition or registry deployment topology.

**HDIP-CLA-M04-R05 - No authority backflow.** A later HDIP architecture decision SHALL NOT use M04 as justification to redefine an upstream semantic or Product authority.

**HDIP-CLA-M04-R06 - Convergence evidence.** M05 convergence decisions SHALL reference responsibility meaning and authority boundaries, not merely similar labels or co-location opportunities.

**HDIP-CLA-M04-R07 - Derivation traceability.** M05-M15 decisions SHOULD record which M04 principles/invariants materially constrained the decision in addition to upstream source traceability.

**HDIP-CLA-M04-R08 - Stronger specialization allowed.** A later HDIP Profile MAY impose stricter requirements than M04 where those requirements do not weaken another applicable principle/invariant or redefine upstream authority.

**HDIP-CLA-M04-R09 - Experience projection discipline.** Simplified or interactive views MAY omit internal detail for audience appropriateness but SHALL preserve the meaning and ordering constraints that are material to the canonical architecture/lifecycle they project.

**HDIP-CLA-M04-R10 - Machine-decidability restraint.** Later executable formalization SHALL distinguish structurally machine-checkable conditions from architecture/governance judgements and SHALL NOT simulate certainty where evidence or judgement is required.

**HDIP-CLA-M04-R11 - M16 reconciliation obligation.** M16 SHALL reconcile the final derived architecture against M04-I01..I40 and may refine/decompose/add invariants for conformance purposes, but SHALL NOT silently weaken an M04 invariant.

**HDIP-CLA-M04-R12 - Historical traceability.** If an M04 principle or invariant is materially revised before the 0.1 freeze, the change SHALL preserve traceability to the superseded wording and identify the architecture decisions affected.

---

# 9. What M04 deliberately does not decide

M04 does not decide:

- the number or names of canonical HDIP Planes;
- whether PDEP, CEP, COVP, Governance or Utility become Planes, Overlays, experience surfaces, lifecycle views or ABB groupings;
- the final COVP expansion/name;
- the future DPFI name or ABB status;
- the canonical ABB catalogue;
- whether registry responsibilities are realized by one or many deployed registry technologies;
- one universal Product-family lifecycle;
- a single Data Mesh operating model;
- a physical deployment topology;
- a universal trust score;
- a universal policy engine;
- a universal graph/store/runtime technology;
- M16 conformance modes or assessment evidence schemas.

These remain downstream decisions.

---

# 10. M04 completion state

**HDIP-CLA M04 - COMPLETE.**

M04 establishes:

- **18 canonical Architecture Principles** (`M04-P01..P18`);
- **40 canonical Design Invariants** (`M04-I01..I40`);
- **12 normative M04 derivation rules** (`HDIP-CLA-M04-R01..R12`);
- an explicit distinction between guiding principles and non-violable derivation invariants;
- a normative interpretation of governed self-service without restoring SSPD as a competing lifecycle;
- an architecture interpretation of the DII Wormhole as interaction-distance reduction without authority/governance bypass;
- explicit constraints for M05 convergence/separation, M06 Plane derivation, M07 Overlay derivation and M08 ABB admission;
- **0 new canonical HDIP Planes**;
- **0 new canonical HDIP Overlays**;
- **0 canonical HDIP ABBs**.

### Next stage

> **M05 - Responsibility Convergence & Separation Analysis**

M05 will apply M04 to the M02 source corpus and M03 retained/reshaped constructs to identify which responsibilities may converge, which may share realization while remaining semantically distinct, which require separation, and which belong only to domain/Product-family Profiles.
