---
id: hdip-cla-0.1-m16-architecture-invariants-conformance-model
title: HDIP-CLA 0.1 M16 - Architecture Invariants & Conformance Model
sidebar_label: M16 - Invariants & Conformance
---

# HDIP-CLA 0.1 M16 - Architecture Invariants & Conformance Model

**Status:** COMPLETE

## 1. Purpose

M16 consolidates the architectural commitments established in M01-M15 into a normative **Architecture Invariant and Conformance Model** for the **Holistic Data, Information and Intelligence Platform (HDIP)**.

M16 answers four questions:

1. **Which architectural conditions must remain true for an HDIP-aligned architecture?**
2. **What exactly is the bounded subject of a conformance claim?**
3. **What evidence and judgement are required before a subject may claim HDIP-CLA 0.1 conformance?**
4. **How may an HDIP Profile specialize the baseline without weakening it or capturing external authority?**

M16 does not add a new Plane, Overlay, ABB, Registry, lifecycle, Interaction Contract, Boundary Family, Realization Pattern, Profile Pattern, Reference View or End-to-End Flow. It establishes the assessment discipline over the architecture already frozen through M15.

The central rule is:

> **HDIP conformance is conformance to applicable architectural obligations and invariants, supported by sufficient traceable evidence; it is not similarity to a diagram, use of preferred technology, adoption of HDIP labels, or presence on an HDIP platform.**

---

## 2. Derivation and reconciliation basis

M16 is constrained by the complete M01-M15 baseline:

- **M01** — platform scope, enterprise-realization boundary and external-authority preservation;
- **M02** — upstream responsibility provenance and no false source-equivalence;
- **M03** — existing HDIP construct disposition and one-lifecycle/multiple-projection discipline;
- **M04** — 18 principles and 40 non-violable Design Invariants;
- **M05** — responsibility convergence/separation locks;
- **M06** — five canonical logical Planes plus HDIP-FND;
- **M07** — nine Cross-Cutting Overlays;
- **M08** — twenty-two canonical logical ABBs;
- **M09** — Registry, descriptor, projection and compilation architecture;
- **M10** — PDEP Product Development & Evolution architecture;
- **M11** — SSCF / CEP consumption and runtime architecture;
- **M12** — twenty-one canonical inter-Plane interactions and Interaction Contract discipline;
- **M13** — twelve external/adjacent Boundary Families and External Boundary Contract discipline;
- **M14** — eight Realization Pattern families and six Profile Pattern families;
- **M15** — ten canonical Reference Views and ten representative End-to-End Flows.

M04 explicitly required M16 to reconcile the final derived architecture against M04-I01..I40 and prohibited silent weakening. M16 therefore carries all forty M04 invariants forward with their canonical meaning intact and adds eight downstream closure invariants that became necessary only after interactions, external boundaries, lifecycle/runtime semantics, realization mapping and Profile rules were frozen.

### 2.1 M04 editorial reconciliation

M04 contained one non-semantic counting error: it stated that its forty invariants were grouped into **seven** families, while the actual document contains sections 5.1 through 5.6 — **six** invariant families. M16 corrects that wording in the M04 artifact. No M04 invariant identity or canonical invariant text changes.

```text
M04
  40 invariants
  6 actual families

M16
  M16-I01..I40  = M04 invariants carried forward
  M16-I41..I48  = downstream conformance closure invariants
  48 invariants total
  7 M16 families total
```

---

## 3. What conformance means

A positive HDIP-CLA conformance claim means that a **bounded Conformance Subject**:

- preserves every applicable core Architecture Invariant;
- accounts for every material HDIP responsibility applicable to its scope;
- preserves external semantic/Product/policy/Data/Decision authority;
- maintains traceability to canonical Planes, Overlays, ABBs, interactions, boundaries and Profile obligations as applicable;
- provides sufficient evidence for the claimed result;
- does not hide unresolved material conditions behind a score, waiver, diagram or technology badge.

Conformance is **not** a maturity model. A minimal conformant realization can be architecturally better than a complex nonconformant one.

Conformance is also not a requirement that every subject instantiate every canonical element. Applicability follows the bounded scope and architectural condition of the subject.

```text
conformance != diagram similarity
conformance != component naming
conformance != technology choice
conformance != platform membership
conformance != maturity score
conformance != registration
conformance != Product qualification
conformance != adjacent-specification conformance
```

---

# 4. Architecture Invariant metamodel

An **Architecture Invariant** is a condition that must remain true for every Conformance Subject to which the invariant applies if that subject is to claim HDIP conformance.

Each M16 invariant has four conceptual properties:

| Property | Meaning |
|---|---|
| **Identity** | Stable `M16-Ixx` identifier. |
| **Canonical condition** | The condition that must remain true. |
| **Applicability** | Whether the condition arises materially in the assessed subject/scope. |
| **Assessment mode** | The primary way satisfaction can safely be assessed. |

## 4.1 Assessment modes

M16 defines three assessment modes.

| Mode | Meaning | Typical evidence |
|---|---|---|
| **STRUCTURAL** | Material portions can be checked from declared architecture structure, identifiers, mappings or versioned configuration. | Architecture registry, mapping graph/table, declared lifecycle/profile structure, identifier/version checks. |
| **HYBRID** | Structural checks are useful but sufficient assessment also requires interpretation of authority, semantics, behavior, evidence or context. | Structural evidence plus architecture review, contract evidence, policy/currentness evidence, runtime samples. |
| **ASSESSMENT** | Accountable judgement is primary; machine checks can support but cannot safely determine the conclusion by themselves. | Architecture rationale, assurance review, contextual trust/fitness assessment, governance judgement. |

Assessment mode is **not** severity. A STRUCTURAL invariant is not weaker than an ASSESSMENT invariant.

M16 uses the following mode distribution:

```text
STRUCTURAL  7
HYBRID      37
ASSESSMENT  4
TOTAL       48
```

---

# 5. Canonical M16 Architecture Invariants

M16 freezes forty-eight core Architecture Invariants in seven families. M16-I01..I40 preserve the canonical meaning of M04-I01..I40. M16-I41..I48 close architecture obligations introduced by M12-M15.

## 5.1 Authority, semantics and jurisdiction

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I01** | **Semantic authority preservation** | HDIP-CLA SHALL NOT incompatibly redefine concepts, relationships or invariants owned by GEDRM, GEARM, GEAIRM or other applicable semantic authorities. | **HYBRID** |
| **M16-I02** | **Product authority preservation** | Generic Product identity, Product Intrinsic Nature and Product qualification SHALL remain governed by BPS/PIN rather than inferred by HDIP. | **HYBRID** |
| **M16-I03** | **Product-family authority preservation** | Data Product, Information Product, AI Product and other Product-family qualification/classification SHALL remain with the applicable Product-family authority. | **HYBRID** |
| **M16-I04** | **Scoped authority** | Authority used by HDIP SHALL be explicit for an applicable scope, role, purpose, lifecycle state and/or jurisdiction where those distinctions matter; platform participation SHALL NOT imply universal authority. | **HYBRID** |
| **M16-I05** | **Shared-realization non-transfer** | Co-location, shared storage, shared runtime, shared registry, shared UI or shared platform realization SHALL NOT by itself transfer semantic, Product, policy, decision or ownership authority. | **HYBRID** |
| **M16-I06** | **Semantic-gap escalation** | Where HDIP needs a semantic concept not owned by HDIP, the gap SHALL be referred to or extended through the appropriate semantic authority rather than silently minted as platform semantics. | **HYBRID** |
| **M16-I07** | **Authority non-transitivity** | Authority, approval, entitlement, policy applicability or ownership SHALL NOT become automatically transitive merely because a dependency, composition or interaction crosses an HDIP boundary. | **HYBRID** |

## 5.2 Responsibility, structure and topology

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I08** | **Responsibility before component** | A canonical HDIP ABB or mandatory implementation responsibility SHALL be justified by explicit architectural responsibility; a noun, tool, service label or historical box alone is insufficient. | **HYBRID** |
| **M16-I09** | **Logical plane semantics** | A future HDIP Plane SHALL represent a coherent logical responsibility grouping and SHALL NOT imply a mandatory system, deployment unit, network tier, team, organizational boundary or lifecycle step. | **STRUCTURAL** |
| **M16-I10** | **Topology independence** | HDIP-CLA conformance SHALL NOT depend on centralized, federated, distributed, edge, embedded, provider-managed or hybrid deployment topology unless a narrower Profile explicitly requires it. | **ASSESSMENT** |
| **M16-I11** | **Many-to-many realization** | One implementation MAY realize responsibilities from several HDIP logical structures, and one HDIP responsibility MAY be distributed across several implementations. | **STRUCTURAL** |
| **M16-I12** | **Source-plane non-equivalence** | GEDRA, GEARA and GEAIRA plane numbering, placement or lexical similarity SHALL NOT force one-to-one HDIP plane mapping. | **HYBRID** |
| **M16-I13** | **Cross-cutting visibility** | A responsibility that is cross-cutting in an applicable source architecture SHALL NOT be silently localized into one future HDIP plane without explicit justification that preserves its cross-cutting obligations. | **HYBRID** |
| **M16-I14** | **Foundation separation** | Compute, storage, networking, messaging, identity infrastructure, orchestration and other utility capabilities SHALL NOT acquire semantic, Product, governance or domain authority merely because they enable those responsibilities. | **HYBRID** |
| **M16-I15** | **Architecture traceability** | Every future canonical HDIP Plane, Overlay, ABB and material interaction SHALL trace to upstream responsibilities, explicit enterprise platform requirements and/or justified HDIP-specific coordination responsibilities. | **STRUCTURAL** |

## 5.3 Data, Information, Intelligence and Product identity

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I16** | **Domain distinction** | Data, Information and Intelligence SHALL remain distinguishable architectural/semantic concerns even where one platform capability co-realizes responsibilities from more than one domain. | **HYBRID** |
| **M16-I17** | **No cross-domain inheritance** | A Data-specific, Information-specific or Intelligence-specific construct SHALL NOT automatically generalize to the other domains through shared implementation or naming similarity. | **HYBRID** |
| **M16-I18** | **No automatic Productness** | Composition, generation, transformation, persistence, deployment, publication, registration, cataloguing, marketplace presence, API exposure, repeated use or consumption SHALL NOT by itself establish Product identity. | **HYBRID** |
| **M16-I19** | **Product-family distinction** | Co-realization of Data Products, Information Products and AI Products SHALL NOT collapse them into one HDIP-local Product family or type. | **HYBRID** |
| **M16-I20** | **Composition non-inheritance** | Using, depending on, containing, deriving from or invoking a Product/capability SHALL NOT by itself transfer its Product family, ontology type, ownership or authority to the dependent/composed result. | **HYBRID** |
| **M16-I21** | **Direct capability validity** | HDIP SHALL be able to support governed Data, Information or Intelligence capability use where Product qualification is not intended; Productization SHALL NOT be a mandatory gateway for every governed interaction. | **ASSESSMENT** |

## 5.4 Governed self-service, lifecycle and experience

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I22** | **Governed self-service** | Self-service SHALL operate inside applicable authority, policy, security, privacy, quality, evidence and lifecycle constraints; self-service SHALL NOT mean unrestricted infrastructure or data access. | **HYBRID** |
| **M16-I23** | **Intent/compilation separation** | Participant-declared intent, business semantics and accountable judgement SHALL remain distinguishable from platform resolution, compilation, provisioning and automation. | **HYBRID** |
| **M16-I24** | **Automation non-ownership** | HDIP automation SHALL NOT transfer Product ownership, Data authority, policy authority or decision accountability to the compiler/runtime merely because the platform performs most technical work. | **HYBRID** |
| **M16-I25** | **Judgement honesty** | Architecture/governance decisions requiring contextual or accountable judgement SHALL NOT be represented as machine-proven solely because metadata, telemetry, rules or model outputs exist. | **ASSESSMENT** |
| **M16-I26** | **PDEP canonical lifecycle identity** | PDEP SHALL remain the canonical HDIP Product Development and Evolution Process identity; historical SSPD terminology MAY remain only for traceability and SHALL NOT become a competing lifecycle. | **STRUCTURAL** |
| **M16-I27** | **Progressive PDEP projection** | PDEP G0 and PDEP Spec A MAY compress/group canonical stages for progressive disclosure, while PDEP Spec C SHALL remain synchronized with the canonical applicable detailed PDEP lifecycle. | **HYBRID** |
| **M16-I28** | **Experience non-authority** | Interactive flow players, diagrams, dashboards and experience projections SHALL NOT independently create lifecycle stages, authority, Product identity, ABBs or architecture semantics. | **HYBRID** |

## 5.5 Projection, compilation, registry and discovery

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I29** | **Projection non-authority** | HPD, SYNCTX, resolved graphs, compiled governance bundles, compilation packs and similar HDIP-generated projections SHALL NOT override the authoritative semantics or governance sources they reference. | **HYBRID** |
| **M16-I30** | **Compiler non-invention** | HDIP resolution/compilation SHALL NOT manufacture semantic relationships, Product identity, policy authority, joinability, provenance, dependencies or obligations from weak evidence or naming similarity. | **HYBRID** |
| **M16-I31** | **Logical registry independence** | ADS, Product, Schema, Policy, Capability and Blueprint registry responsibilities SHALL remain logically distinguishable even where one implementation realizes several of them. | **STRUCTURAL** |
| **M16-I32** | **Registry non-qualification** | Registration SHALL NOT by itself prove authoritative status, Product status, control effectiveness, semantic correctness, fitness or HDIP conformance. | **HYBRID** |
| **M16-I33** | **Registry/catalog/marketplace distinction** | Registry, Catalog and Marketplace responsibilities SHALL NOT be treated as architectural synonyms even when exposed through one user experience or implementation. | **STRUCTURAL** |
| **M16-I34** | **Shared registry realization allowed** | HDIP MAY consolidate registry implementation where operationally useful provided logical identities, ownership, contracts, lifecycle and authority boundaries remain distinguishable. | **HYBRID** |

## 5.6 Evidence, trust, version and historical meaning

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I35** | **Evidence by construction** | Material HDIP interactions SHOULD emit or retain applicable provenance, control, quality, observability and lifecycle evidence sufficient for later reconstruction and assessment. | **HYBRID** |
| **M16-I36** | **Trust is contextual** | Platform location, certification label, popularity, centralization, Product status or registry presence SHALL NOT be treated as universal proof of trust or fitness; trust assessment SHALL remain contextual and evidence-based. | **ASSESSMENT** |
| **M16-I37** | **Missing evidence is not positive evidence** | Missing, stale, inaccessible or materially ambiguous evidence SHALL NOT be interpreted as positive assurance. | **HYBRID** |
| **M16-I38** | **Version/currentness distinction** | Version identity, latest/newest status and governed currentness SHALL remain distinguishable; newest SHALL NOT automatically mean current or approved. | **HYBRID** |
| **M16-I39** | **Historical truth** | Later supersession, revocation, re-evaluation, upstream change, rollback or re-publication SHALL NOT silently rewrite which semantics, Product Version, policy/control, dependency, context or realization governed a historical occurrence. | **HYBRID** |
| **M16-I40** | **Provenance is not assurance** | Provenance and lineage SHALL support traceability but SHALL NOT by themselves prove correctness, authorization, control effectiveness, assurance or Fitness for Use. | **HYBRID** |

> **M04 preservation:** M16-I01..I40 retain the M04 invariant meaning. Assessment-mode metadata added here is conformance metadata, not a semantic rewrite.

## 5.7 Derived conformance closure

| ID | Name | Canonical M16 invariant | Assessment mode |
|---|---|---|---|
| **M16-I41** | **Canonical structure integrity** | A conformant HDIP architecture SHALL preserve the canonical identity and responsibility meaning of P1-P5, X1-X9, HDIP-FND and the M08 ABB catalogue; implementation grouping, view projection or profile specialization SHALL NOT silently redefine those canonical structures. | **STRUCTURAL** |
| **M16-I42** | **Interaction-contract preservation** | Material interactions SHALL preserve the applicable M12 Interaction Contract identity and obligations even when the participating responsibilities are co-located, embedded, distributed, provider-operated or implemented through a mechanism other than a network API. | **HYBRID** |
| **M16-I43** | **External-boundary jurisdiction preservation** | Material crossings of an M13 Boundary Family SHALL preserve the applicable external authority, jurisdiction, currentness, evidence and failure obligations; physical co-location or shared-provider realization SHALL NOT erase the logical boundary. | **HYBRID** |
| **M16-I44** | **Product-access / consequence separation** | Product or Product-Port access approval, entitlement or successful consumption SHALL NOT by itself authorize a downstream consequential Decision, Tool use, Digital Action or Physical Action where separate point-of-use authority is applicable. | **HYBRID** |
| **M16-I45** | **Lifecycle / runtime non-equivalence** | PDEP, SSCF and CEP SHALL remain lifecycle/experience compositions and SHALL NOT be interpreted as mandatory synchronous runtime pipelines; an established governed runtime MAY reuse current lifecycle state until material change requires re-evaluation. | **HYBRID** |
| **M16-I46** | **Realization mapping traceability** | A concrete realization claiming HDIP alignment SHALL retain traceability from applicable canonical responsibilities, ABBs, Interaction Contracts, Boundary Families and Profile obligations to the Realization Units, human processes or adjacent systems that satisfy them. | **HYBRID** |
| **M16-I47** | **Adjacent-conformance independence** | HDIP conformance SHALL NOT by itself establish conformance to GEDRA, GEARA, GEAIRA, BPS/PIN, a Product-family specification, an external standard or provider certification, and conformance to an adjacent specification SHALL NOT by itself establish HDIP conformance. | **HYBRID** |
| **M16-I48** | **Profile monotonicity** | An HDIP Profile MAY select, tighten, contextualize, specialize, narrow and extend the baseline for a bounded scope, but SHALL NOT weaken, waive or incompatibly redefine an applicable core invariant or transfer authority from an external semantic, Product, policy or Decision authority. | **HYBRID** |

The closure invariants do not replace earlier invariants. They make explicit the additional conformance obligations that became testable only after M12-M15 established Interaction Contracts, external boundaries, lifecycle/runtime separation, realization mapping and governed Profile semantics.

---

# 6. Invariant applicability and result model

M16 distinguishes **applicability** from **result**.

## 6.1 Applicability

An invariant is:

- **APPLICABLE** when its architectural condition materially arises within the assessed subject/scope;
- **NOT_APPLICABLE** only when the condition genuinely does not arise in the bounded scope and that conclusion is justified;
- **UNDETERMINED** during assessment when applicability itself cannot yet be established.

`NOT_APPLICABLE` is not a waiver. A subject cannot mark an inconvenient invariant N/A merely because the chosen implementation does not currently satisfy it.

## 6.2 Final invariant result

For an applicable invariant, the final result is one of:

```text
SATISFIED
VIOLATED
INDETERMINATE
```

For a genuinely non-applicable invariant:

```text
NOT_APPLICABLE
```

`INDETERMINATE` is an intentional honest outcome. It applies where available evidence cannot establish satisfaction or violation with the confidence required by the invariant.

## 6.3 No silent-positive inference

The following are invalid shortcuts:

```text
no observed failure        -> SATISFIED       [invalid]
no evidence                -> SATISFIED       [invalid]
platform certified         -> SATISFIED       [invalid]
registry entry exists      -> SATISFIED       [invalid]
latest version             -> current         [invalid]
telemetry exists           -> assured         [invalid]
```

---

# 7. Conformance Subject model

A **Conformance Subject** is the bounded architecture artifact or realized architecture for which an HDIP conformance claim is made.

M16 recognizes six principal subject classes:

| ID | Conformance Subject class | Examples |
|---|---|---|
| **CS1** | **Enterprise HDIP Architecture** | Enterprise-wide or multi-domain HDIP target/current architecture. |
| **CS2** | **Domain / Portfolio HDIP Architecture** | A Data, Information, Intelligence or cross-domain bounded architecture. |
| **CS3** | **Governed HDIP Profile** | A concrete enterprise/domain/Product-family/high-assurance/Data-Mesh specialization. |
| **CS4** | **Platform / Solution Architecture** | A bounded platform, solution or capability architecture claiming HDIP alignment. |
| **CS5** | **Product / Capability Realization Architecture** | A bounded Product or non-Product capability realization using applicable PDEP/SSCF/runtime responsibilities. |
| **CS6** | **Concrete Realization Mapping** | The mapping from canonical/Profile architecture into actual deployed/human/provider Realization Units. |

A claim MAY cover more than one class, but the scope must remain explicit. For example, an enterprise architecture claim does not automatically certify every Product realization deployed beneath it.

## 7.1 Scope minimum

Every claim SHALL identify at least:

```text
subject identity
subject version
claim type
organizational / solution scope
architecture boundary
HDIP-CLA baseline version
applicable Profile(s)
assessment time / version
```

---

# 8. Conformance claim types

M16 defines three primary claim types.

## 8.1 Core Architecture Conformance

A claim that the subject preserves all applicable M16 core invariants and the applicable responsibilities/contracts of the HDIP-CLA 0.1 baseline.

## 8.2 Profile Conformance

A claim that the subject is Core-conformant **and** satisfies a named, governed, M16-valid HDIP Profile.

A Profile claim is therefore stronger/narrower than a Core claim, not an alternate path around Core conformance.

## 8.3 Realization Mapping Conformance

A claim that a concrete implementation mapping faithfully realizes the claimed Core/Profile architecture, including traceability to Realization Units, M12 contracts, M13 boundaries/EBCs, evidence responsibilities, currentness and failure/recovery obligations.

```text
Core Architecture Conformance
            |
            +--> Profile Conformance
            |
            +--> Realization Mapping Conformance
```

The claim types are complementary. They do not automatically imply one another unless their required evidence has actually been assessed.

---

# 9. Overall conformance outcomes

M16 defines exactly three normative overall outcomes:

| Outcome | Meaning |
|---|---|
| **CONFORMANT** | Every applicable core invariant is SATISFIED; N/A results have justified scope rationale; all obligations required by the claim type are satisfied. |
| **NONCONFORMANT** | At least one applicable core invariant is VIOLATED, or a mandatory claim-type obligation is demonstrably violated. |
| **INDETERMINATE** | No applicable core invariant is known to be violated, but one or more material applicable obligations cannot be determined with sufficient evidence. |

M16 does not define `CONDITIONALLY CONFORMANT` as a positive outcome.

```text
one material core violation
        -> NONCONFORMANT

no violation + unresolved material evidence
        -> INDETERMINATE

all applicable core obligations satisfied
        -> CONFORMANT
```

An enterprise governance process may track remediation, risk acceptance or exception state separately, but that administrative state does not change the M16 conformance outcome.

---

# 10. Minimum Conformance Evidence Package

A positive HDIP claim SHOULD be supported by a versioned **Conformance Evidence Package (HDIP-CEP)**. This acronym is local to M16 and SHALL NOT be confused with M11 **CEP — Consumer Experience Projection**; implementations SHOULD therefore prefer the unambiguous label **Conformance Evidence Package** in user-facing artifacts.

To avoid that collision altogether, M16 uses the short form **CEPkg** below.

A minimum CEPkg contains eighteen dimensions:

| # | Evidence dimension | Minimum content |
|---:|---|---|
| 1 | **Subject identity/version** | Stable subject ID and assessed version. |
| 2 | **Claim type** | Core, Profile or Realization Mapping. |
| 3 | **Scope / architecture boundary** | Organizational, solution, Product/capability and logical boundary. |
| 4 | **HDIP baseline** | HDIP-CLA version used for assessment. |
| 5 | **Profile identity/version** | Applicable concrete Profile(s), if any. |
| 6 | **External authority map** | GEDRM/GEARM/GEAIRM, BPS/PIN, Product-family, policy/legal, Decision/action and other authorities relied upon. |
| 7 | **Plane responsibility coverage** | Applicable P1-P5 responsibility coverage. |
| 8 | **Overlay applicability** | X1-X9 applicability and evidence/control responsibilities. |
| 9 | **ABB / responsibility mapping** | Canonical/specialized ABB and embedded responsibility realization. |
| 10 | **Registry / projection / compilation map** | Applicable M09 Registries, HPD/RRG/SYNCTX/RGB/Realization Plan/Blueprint Binding/Compilation Record responsibilities. |
| 11 | **Lifecycle / experience map** | PDEP, SSCF and CEP applicability/specialization. |
| 12 | **Interaction Contract map** | Material M12 interactions and contract obligations. |
| 13 | **External Boundary map** | Material M13 Boundary Families, Boundary Instances and EBCs. |
| 14 | **Realization / Profile map** | M14 Realization Pattern(s), Realization Units and Profile obligations. |
| 15 | **Version/currentness/historical state** | Material versions, effective/currentness state and assessment time. |
| 16 | **Invariant assessment record** | Applicability, mode, result, rationale and evidence references for M16-I01..I48. |
| 17 | **Limitations / N/A / unresolved evidence** | Explicit gaps, N/A rationale, indeterminate conditions and unresolved dependencies. |
| 18 | **Accountability / retention** | Accountable assessor/authority, assessment version/time and retained evidence location/reference. |

The evidence package is a logical evidence contract, not a requirement for one database, graph, document format or certification portal.

---

# 11. HDIP Profile conformance model

M14 defined the Profile as a governed specialization. M16 adds the conformance discipline needed to assess a concrete Profile.

A conformant concrete Profile SHOULD declare at least the fourteen M14 Profile dimensions plus four conformance-specific dimensions:

```text
M14 profile dimensions (14)
  identity/version
  scope
  parent baseline
  external authorities
  applicable Planes/ABBs
  applicable Overlays
  lifecycle specialization
  registry/projection specialization
  interaction specialization
  boundary specialization
  allowed realization patterns
  evidence/assurance
  non-applicability rationale
  conformance claim

M16 conformance additions (4)
  invariant applicability matrix
  specialization-operation record
  Profile composition/conflict record
  Profile assessment/evidence state
```

## 11.1 Permitted Profile operations

M16 permits nine specialization operation classes:

1. **SELECT** — select an applicable baseline option or pattern.
2. **REQUIRE** — make an optional/conditional baseline responsibility mandatory within Profile scope.
3. **TIGHTEN** — strengthen a threshold, control, evidence or lifecycle obligation.
4. **CONTEXTUALIZE** — bind a baseline concept to a bounded enterprise/domain context without redefining it.
5. **SPECIALIZE** — introduce a family/domain specialization consistent with the parent authority.
6. **NARROW** — reduce allowed choices or topology/interaction options for a bounded risk/context reason.
7. **EXTEND** — add local obligations/fields/controls that do not conflict with core meaning.
8. **ADD_EVIDENCE** — require stronger/additional evidence, assurance or human review.
9. **RESTRICT_REALIZATION** — constrain permitted M14 patterns/localities/providers for the bounded Profile.

## 11.2 Prohibited Profile operations

A Profile SHALL NOT use any of the following as a conformance-preserving operation:

1. **WEAKEN_CORE** — reduce an applicable core invariant or mandatory baseline obligation.
2. **WAIVE_TO_PASS** — waive a violation and still report Profile/Core conformance.
3. **REDEFINE_EXTERNAL_SEMANTICS** — take ownership of GEDRM/GEARM/GEAIRM or other external semantics.
4. **REDEFINE_PRODUCTNESS** — redefine BPS/PIN Product qualification or Product Intrinsic Nature.
5. **TRANSFER_AUTHORITY** — infer Data, Product, policy or Decision authority from platform participation.
6. **COLLAPSE_PRODUCT_FAMILIES** — erase Data/Information/AI Product-family distinctions.
7. **UNIVERSALIZE_SPECIALIZATION** — impose a Data-, Information- or Intelligence-specific lifecycle/construct on all families without authority/evidence.
8. **REMOVE_APPLICABLE_OVERLAY** — suppress an applicable X1-X9 obligation because implementation is inconvenient.
9. **REMOVE_EVIDENCE_OBLIGATION** — eliminate material evidence/currentness/history requirements needed by the parent baseline.
10. **REDEFINE_CANONICAL_STRUCTURE** — silently rename/redefine P1-P5, X1-X9, ABBs or M12/M13 identities as different architecture semantics.
11. **CONFLATE_REGISTRY_CATALOG_MARKETPLACE** — erase their canonical responsibility distinction.
12. **INFER_PRODUCTNESS** — create Product status from registration, publication, deployment, exposure or repeated use.
13. **REWRITE_HISTORY** — project latest Profile/policy/topology state backwards onto earlier occurrences.
14. **N/A_BY_CONVENIENCE** — mark a material core obligation not applicable merely to avoid remediation.

---

# 12. Realization Mapping Conformance

A concrete realization does not need one deployable component per ABB or one service per Plane/Overlay. It does need a traceable mapping.

Minimum conceptual mapping:

```text
canonical/Profile responsibility
        |
        v
Realization Unit(s) / human process / adjacent system
        |
        +-- locality / provider / admin owner
        +-- M12 contract(s)
        +-- M13 boundary/EBC(s)
        +-- evidence/currentness producer
        +-- failure/recovery behavior
        +-- applicable Profile(s)
```

The mapping may be tabular, graph-based or machine-readable. M16 does not prescribe a serialization.

## 12.1 Many-to-many is normal

```text
one Realization Unit
    -> many ABB/responsibility identities

one ABB/responsibility
    -> many Realization Units
```

Conformance review therefore assesses responsibility coverage and boundary integrity, not component-count symmetry.

---

# 13. Adjacent conformance and authority boundaries

HDIP operates in a specification ecosystem. M13 already established that logical jurisdiction survives physical co-location. M16 adds the conformance consequence:

```text
HDIP conformance
    != GEDRA conformance
    != GEARA conformance
    != GEAIRA conformance
    != BPS/PIN Product qualification
    != Product-family conformance
    != external-standard conformance
    != provider certification
```

A solution may legitimately hold several claims at once. Each claim must remain bounded to its own subject, version, scope, authority and evidence.

A shared enterprise platform may realize GEDRA, GEARA, GEAIRA and HDIP responsibilities simultaneously. That co-realization does not merge their conformance jurisdictions.

---

# 14. Machine-checkability and future executable formalization

M16 deliberately distinguishes **automation assistance** from **architecture judgement**.

## 14.1 Safely automatable examples

A future executable conformance implementation may safely automate checks such as:

- identifier presence/uniqueness;
- declared version relationships;
- required field presence;
- declared Plane/Overlay/ABB coverage;
- M12 interaction identifier/reference consistency;
- M13 Boundary/EBC declaration completeness;
- Profile parent/version declaration;
- prohibited direct identifier collisions;
- selected lifecycle stage/projection synchronization where mechanically represented;
- evidence-reference presence and staleness flags where time semantics are explicit.

## 14.2 Hybrid examples

Automation may assist but not fully decide questions such as:

- whether a local semantic extension has captured external authority;
- whether two implementations truly preserve Product-family distinction;
- whether compilation has manufactured a relationship from weak evidence;
- whether an Access Decision has leaked into consequential-action authority;
- whether a provider substitution is semantically/contractually safe;
- whether historical reconstruction is materially sufficient.

## 14.3 Assessment-only examples

Primarily accountable judgement is required for matters such as:

- contextual trust / Fitness for Use;
- adequacy of accountable human judgement;
- architecture significance of a semantic/authority gap;
- proportionality of a high-assurance Profile;
- whether a complex realization introduces unacceptable hidden authority or evidence coupling.

The governing principle remains:

> **Machine-checkable structure may support conformance; it must not simulate certainty where architecture judgement is required.**

---

# 15. Historical conformance and claim lifecycle

A conformance result is itself versioned and time-bound.

Later events may include:

```text
reassessment
supersession
withdrawal
expiration
scope narrowing
Profile version change
architecture version change
provider migration
policy revocation
```

Those events do not rewrite the earlier claim.

Example:

```text
T1: Solution v3 assessed CONFORMANT to HDIP-CLA 0.1 + Profile A v1
T2: policy changes
T3: Profile A v2 becomes current
T4: Solution v3 reassessed -> NONCONFORMANT until remediated

Historical fact remains:
  at T1, v3 held the T1 conformance claim under the evidence and rules then assessed.
```

This historical discipline is consistent with M04-I39, M07 lifecycle/currentness rules, M09 Compilation Record semantics and M13/M14 topology/provider migration rules.

---

# 16. Conformance assessment workflow

A practical HDIP-CLA 0.1 conformance assessment SHOULD proceed as follows:

```text
1. Identify Conformance Subject, version, scope and claim type.
2. Identify HDIP-CLA baseline and applicable concrete Profile(s).
3. Identify external semantic/Product/policy/Data/Decision authorities.
4. Determine applicable P1-P5 responsibilities and X1-X9 Overlays.
5. Trace canonical/specialized ABB and embedded responsibility realization.
6. Identify applicable M09 Registry/projection/compilation responsibilities.
7. Identify PDEP / SSCF / CEP lifecycle/experience applicability.
8. Identify material M12 Interaction Contracts.
9. Identify material M13 Boundary Families / EBCs.
10. Record M14 Realization Pattern(s), Profile(s) and Realization Mapping.
11. Select the smallest useful M15 Reference View/Flow set for review.
12. Assess M16-I01..I48 applicability.
13. Gather STRUCTURAL, HYBRID and ASSESSMENT evidence.
14. Record invariant results with rationale/evidence references.
15. Determine overall outcome: CONFORMANT / NONCONFORMANT / INDETERMINATE.
16. Record accountable assessor/authority, assessment version and time.
17. Preserve the Conformance Evidence Package for historical reconstruction.
18. Define change triggers that require scoped reassessment.
```

A Reference View or End-to-End Flow can help organize review, but visual resemblance to the view/flow is never itself conformance evidence.

---

# 17. Coverage expectations across the canonical architecture

M16 does not require every subject to instantiate every element. It does require the conformance method to be capable of assessing the complete baseline where applicable.

| Architecture area | M16 conformance expectation |
|---|---|
| **P1-P5** | Applicable primary responsibility coverage must be accounted for. |
| **X1-X9** | Applicable cross-cutting obligations must remain visible and evidenced. |
| **22 ABBs** | Applicable responsibility boundaries must be traceable; no component-per-ABB requirement. |
| **M09 Registries / projections / compilation** | Authority and currentness boundaries must remain explicit where used. |
| **PDEP** | Product development/evolution conformance must preserve family specialization and projection fidelity where applicable. |
| **SSCF / CEP** | Product-access, established-state runtime and experience-projection rules must remain intact where consumption applies. |
| **21 M12 interactions** | Material interactions must preserve applicable contract obligations. |
| **12 M13 Boundary Families** | Material external crossings must preserve jurisdiction and EBC obligations. |
| **8 M14 Realization Patterns** | Topology choice must not alter logical obligations; only selected patterns require realization evidence. |
| **6 M14 Profile Pattern families** | Concrete Profiles must be governed specializations; pattern identity alone is not a conformance claim. |
| **10 M15 Reference Views** | Review aids only; no view creates architecture ownership. |
| **10 M15 Flows** | Representative traversals only; no flow becomes a universal pipeline. |

---

# 18. Conformance/Profile anti-patterns

M16 freezes twenty anti-patterns:

1. **Diagram Match Conformance** — declaring conformance because a solution diagram resembles M15.
2. **Technology Badge Conformance** — declaring conformance because a preferred platform/framework/tool is used.
3. **Terminology Conformance** — renaming components with HDIP labels without preserving responsibility semantics.
4. **Percentage Conformance** — using an aggregate score to hide a failed core invariant.
5. **Waiver-to-Pass** — accepting a core violation while still reporting positive conformance.
6. **Not-Applicable Shopping** — marking difficult obligations N/A without scope-based rationale.
7. **Inherited Platform Conformance** — assuming every workload/Product is conformant because a shared platform is conformant.
8. **Profile Rewrites Core** — using a Profile to redefine a canonical invariant or structure.
9. **Profile Owns External Semantics** — copying external authoritative semantics into local Profile ownership.
10. **Vendor Becomes ABB** — treating a local vendor/service/component as a canonical ABB by naming convention.
11. **Structural-Only Assurance** — treating schema/configuration validity as proof of architecture judgement or assurance.
12. **Telemetry-Only Evidence Package** — using logs/metrics as the entire conformance basis.
13. **Latest-Only Assessment** — losing the versions/currentness that governed a historical claim.
14. **One Global Claim** — issuing one enterprise-wide claim that obscures unassessed domains/solutions/Products.
15. **Adjacent Conformance Leakage** — inferring GEDRA/GEARA/GEAIRA/BPS/Product-family conformance from HDIP conformance or vice versa.
16. **Pattern Means Conformant** — claiming conformance because an M14 Realization/Profile Pattern was selected.
17. **Maturity Equals Conformance** — substituting capability maturity or decentralization for invariant satisfaction.
18. **Automated Judgement Theatre** — presenting a rules engine as definitive proof of HYBRID/ASSESSMENT invariants.
19. **Gate-Count Conformance** — equating more lifecycle gates/manual approvals with stronger architecture conformance.
20. **Registration/Productness Conformance** — treating Registry/Catalog/Marketplace presence or successful deployment as proof of Product status or HDIP conformance.

---

# 19. Canonical M16 architecture rules

**HDIP-CLA-M16-R01 - Obligation-based conformance.** An HDIP conformance claim SHALL be based on satisfaction of applicable architectural invariants and traceable responsibilities rather than terminology, branding, diagram similarity or technology selection.

**HDIP-CLA-M16-R02 - No new semantic authority.** M16 SHALL NOT create semantic, Product, Data, policy, Decision or external-standard authority that belongs outside HDIP.

**HDIP-CLA-M16-R03 - Frozen architecture preservation.** M16 SHALL preserve the canonical structures frozen through M15 and SHALL NOT use conformance modelling to redefine them.

**HDIP-CLA-M16-R04 - No conformance-by-implementation.** Use of a vendor, cloud, framework, registry product, data platform, analytics engine, AI platform or other implementation technology SHALL NOT by itself establish HDIP conformance.

**HDIP-CLA-M16-R05 - M04 reconciliation.** M16-I01 through M16-I40 SHALL preserve the canonical meaning of M04-I01 through M04-I40; refinements in assessment metadata SHALL NOT weaken those invariants.

**HDIP-CLA-M16-R06 - M04 editorial correction.** The M04 invariant-family count SHALL be read as six families; the earlier phrase 'seven families' was an editorial counting error and did not change invariant identity or wording.

**HDIP-CLA-M16-R07 - Downstream closure invariants.** M16-I41 through M16-I48 SHALL capture conformance obligations that became explicit only after M12-M15 froze interactions, boundaries, lifecycle/runtime, realization and Profile semantics.

**HDIP-CLA-M16-R08 - Invariant precedence.** A Realization Pattern, Profile, local standard, implementation constraint or operating-model preference SHALL NOT override an applicable M16 core invariant.

**HDIP-CLA-M16-R09 - Core invariant status.** M16-I01 through M16-I48 SHALL be the core HDIP-CLA 0.1 Architecture Invariants evaluated when applicable to a conformance subject.

**HDIP-CLA-M16-R10 - Assessment-mode status.** Every M16 invariant SHALL declare one primary assessment mode: STRUCTURAL, HYBRID or ASSESSMENT.

**HDIP-CLA-M16-R11 - Structural mode restraint.** STRUCTURAL classification SHALL mean that material portions can be checked from declarative architecture artifacts; it SHALL NOT be interpreted as proof of runtime correctness or assurance.

**HDIP-CLA-M16-R12 - Hybrid mode discipline.** HYBRID classification SHALL combine machine-checkable structure where useful with accountable architecture interpretation and evidence review.

**HDIP-CLA-M16-R13 - Assessment mode honesty.** ASSESSMENT classification SHALL require accountable judgement and SHALL NOT be represented as definitively machine-proven solely because metadata or automated scores exist.

**HDIP-CLA-M16-R14 - Mode is not severity.** Assessment mode SHALL NOT be interpreted as invariant importance, criticality or optionality.

**HDIP-CLA-M16-R15 - Invariant traceability.** Each invariant assessment SHOULD retain traceability to relevant M01-M15 elements, source authorities, interactions, boundaries, evidence and Profile rules.

**HDIP-CLA-M16-R16 - No invariant percentage substitution.** Aggregate percentages or maturity scores SHALL NOT substitute for the result of an applicable core invariant.

**HDIP-CLA-M16-R17 - Bounded subject.** Every conformance claim SHALL identify a bounded Conformance Subject, version, scope and architecture boundary.

**HDIP-CLA-M16-R18 - Subject-class declaration.** A claim SHALL declare the applicable M16 Conformance Subject class or a governed specialization of one.

**HDIP-CLA-M16-R19 - No enterprise-wide inference.** Conformance of one domain, solution, Product realization or shared platform SHALL NOT imply conformance of the entire enterprise or every workload using it.

**HDIP-CLA-M16-R20 - Applicable responsibility completeness.** A Conformance Subject SHALL account for every material HDIP responsibility applicable to its claimed scope, whether explicit, embedded, human-mediated, delegated or provided through an adjacent system/shared platform.

**HDIP-CLA-M16-R21 - Omission rationale.** Omission of a normally relevant Plane, Overlay, ABB, interaction, boundary or lifecycle responsibility SHALL be justified by scope/applicability rather than implementation convenience.

**HDIP-CLA-M16-R22 - Embedded realization permitted.** Embedded or co-located realization MAY conform where canonical responsibility, authority, contract and evidence obligations remain traceable.

**HDIP-CLA-M16-R23 - Applicability is contextual.** An invariant MAY be marked NOT_APPLICABLE only when the architectural condition genuinely does not arise in the bounded subject scope.

**HDIP-CLA-M16-R24 - Not-applicable evidence.** Every material NOT_APPLICABLE result SHALL include an explicit scope-based rationale and supporting evidence where applicable.

**HDIP-CLA-M16-R25 - Invariant result vocabulary.** Final invariant results SHALL use SATISFIED, VIOLATED, INDETERMINATE or NOT_APPLICABLE.

**HDIP-CLA-M16-R26 - No silent pass.** An invariant SHALL NOT be treated as SATISFIED merely because no violation was observed or evidence was unavailable.

**HDIP-CLA-M16-R27 - Indeterminate honesty.** Where material evidence is missing, stale, inaccessible or contradictory such that satisfaction cannot be established, the invariant result SHALL be INDETERMINATE rather than SATISFIED.

**HDIP-CLA-M16-R28 - Violation consequence.** A VIOLATED applicable core invariant SHALL make a Core Architecture Conformance claim NONCONFORMANT for the assessed subject/version/scope.

**HDIP-CLA-M16-R29 - Conformant outcome.** CONFORMANT SHALL require every applicable core invariant to be SATISFIED and every NOT_APPLICABLE result to have an acceptable scope rationale.

**HDIP-CLA-M16-R30 - Indeterminate outcome.** If no applicable core invariant is VIOLATED but one or more material applicable invariants remain INDETERMINATE, the overall claim SHALL be INDETERMINATE.

**HDIP-CLA-M16-R31 - No conditional-pass state.** M16 SHALL NOT define a positive 'conditionally conformant' outcome that permits unresolved or violated core invariants to be presented as conformance.

**HDIP-CLA-M16-R32 - Outcome versioning.** Every overall conformance outcome SHALL be bound to the assessed subject version, HDIP baseline version, Profile version where applicable, scope and assessment time.

**HDIP-CLA-M16-R33 - Core claim type.** Core Architecture Conformance SHALL mean that the subject preserves all applicable M16 core invariants and applicable HDIP responsibilities/contracts for the declared scope.

**HDIP-CLA-M16-R34 - Profile claim type.** Profile Conformance SHALL require Core Architecture Conformance plus satisfaction of all applicable obligations in the named governed Profile.

**HDIP-CLA-M16-R35 - Realization claim type.** Realization Mapping Conformance SHALL require traceable mapping from the claimed architecture/Profile into the concrete Realization Units, boundaries, contracts and evidence obligations that implement it.

**HDIP-CLA-M16-R36 - Claim type non-substitution.** A Realization Mapping claim SHALL NOT substitute for Core/Profile conformance and a Core/Profile claim SHALL NOT by itself prove implementation fidelity.

**HDIP-CLA-M16-R37 - Evidence package required.** A positive conformance claim SHOULD be supported by a retained Conformance Evidence Package sufficient for independent reconstruction of the assessment.

**HDIP-CLA-M16-R38 - Evidence identity.** The evidence package SHALL identify the Conformance Subject, version, claim type, scope, HDIP baseline and applicable Profile version.

**HDIP-CLA-M16-R39 - Responsibility coverage evidence.** The evidence package SHALL include applicable P1-P5, X1-X9 and ABB responsibility coverage or an equivalent traceable representation.

**HDIP-CLA-M16-R40 - Lifecycle/registry evidence.** Where applicable, the evidence package SHALL identify Registry/projection/compilation architecture and PDEP/SSCF/CEP lifecycle responsibilities relevant to the subject.

**HDIP-CLA-M16-R41 - Interaction/boundary evidence.** The evidence package SHALL identify material M12 Interaction Contracts and M13 Boundary Families/EBCs relevant to the subject.

**HDIP-CLA-M16-R42 - Realization/profile evidence.** The evidence package SHALL identify applicable M14 Realization Patterns, Profile(s), Realization Mapping and material topology/provider boundaries.

**HDIP-CLA-M16-R43 - Currentness evidence.** Conformance evidence SHALL identify the material semantic, Product, policy, contract, Profile and realization versions/currentness that governed the assessment.

**HDIP-CLA-M16-R44 - Assessment rationale.** Each invariant result SHALL retain sufficient rationale and evidence references for an independent reviewer to understand why the result was reached.

**HDIP-CLA-M16-R45 - Evidence provenance.** Evidence used for conformance SHALL retain source/provider identity and occurrence/version context where material.

**HDIP-CLA-M16-R46 - Evidence non-self-validation.** Logs, telemetry, certificates, registry state, provider attestations or generated reports SHALL NOT be treated as self-validating proof of correctness, trust or assurance.

**HDIP-CLA-M16-R47 - Assessor accountability.** The conformance package SHALL identify the accountable assessor or authority for judgement-dependent results and the assessment time/version.

**HDIP-CLA-M16-R48 - Retention/historical traceability.** Conformance evidence and outcomes SHALL be retained sufficiently to reconstruct the historical claim even after later architecture, policy or Profile change.

**HDIP-CLA-M16-R49 - Profile identity.** A concrete HDIP Profile SHALL have a stable identity, governed version, bounded scope and declared parent HDIP baseline/Profile.

**HDIP-CLA-M16-R50 - Profile monotonicity.** A Profile MAY strengthen or narrow the baseline but SHALL NOT weaken, waive or incompatibly redefine an applicable core invariant.

**HDIP-CLA-M16-R51 - Profile external authority.** A Profile SHALL preserve external semantic, Product-family, policy, Data, Decision and peer-architecture authorities rather than copying them into local ownership.

**HDIP-CLA-M16-R52 - Profile applicability matrix.** A Profile SHOULD state applicable Planes, Overlays, ABBs, lifecycle specializations, interaction/boundary obligations and invariant applicability for its scope.

**HDIP-CLA-M16-R53 - Profile operation declaration.** Material Profile changes SHOULD identify which permitted specialization operation is being applied and to which baseline obligation.

**HDIP-CLA-M16-R54 - Profile conflict handling.** Incompatible Profile obligations SHALL be explicitly reconciled through governed narrowing/change; conflict SHALL NOT be resolved by silently dropping the stricter applicable obligation.

**HDIP-CLA-M16-R55 - Profile composition.** Multiple Profiles MAY be composed only where their authorities, scopes and strengthened obligations remain compatible and traceable.

**HDIP-CLA-M16-R56 - Profile N/A restraint.** A Profile SHALL NOT use NOT_APPLICABLE as a generalized waiver mechanism for difficult baseline obligations.

**HDIP-CLA-M16-R57 - Realization mapping completeness.** A Realization Mapping SHALL identify how applicable canonical responsibilities are realized by Realization Units, human processes or adjacent systems and where material M12/M13 boundaries occur.

**HDIP-CLA-M16-R58 - Many-to-many realization.** Conformance SHALL permit many-to-many mapping between canonical ABB/responsibility identities and concrete Realization Units.

**HDIP-CLA-M16-R59 - Topology neutrality.** Core HDIP conformance SHALL remain independent of M14 Realization Pattern choice unless a narrower Profile explicitly constrains topology/locality.

**HDIP-CLA-M16-R60 - Shared-platform non-inheritance.** Conformance of a shared platform SHALL NOT automatically confer conformance on every Product, domain, workload or adjacent architecture realized on that platform.

**HDIP-CLA-M16-R61 - Adjacent conformance independence.** HDIP conformance SHALL be assessed independently from conformance to GEDRA, GEARA, GEAIRA, BPS/PIN, Product-family specifications and external standards.

**HDIP-CLA-M16-R62 - External authority evidence.** Where a claim depends on an adjacent authority/specification, the conformance package SHALL identify the applicable adjacent subject/version and the nature of the dependency without asserting inherited conformance.

**HDIP-CLA-M16-R63 - Boundary preservation.** A realization SHALL preserve M13 logical jurisdiction boundaries even when adjacent responsibilities are physically co-located or provider-hosted.

**HDIP-CLA-M16-R64 - Access/consequence preservation.** Conformance SHALL verify the Product-access versus consequential Decision/Action authorization distinction wherever the subject crosses BND-10/BND-11 responsibilities.

**HDIP-CLA-M16-R65 - Automation scope.** Future executable conformance tooling MAY automate structural checks, identifier/version consistency, declared mappings and other safely decidable constraints.

**HDIP-CLA-M16-R66 - No automated judgement theatre.** Automation SHALL NOT claim definitive satisfaction of HYBRID or ASSESSMENT invariants when material judgement/evidence remains outside the machine-evaluable boundary.

**HDIP-CLA-M16-R67 - Explainable automation.** Automated conformance results SHOULD identify the rule, input evidence/version and reasoning category used so that accountable human review remains possible.

**HDIP-CLA-M16-R68 - Historical non-rewrite.** Later reassessment, supersession, Profile change or conformance withdrawal SHALL NOT rewrite the outcome/evidence that governed an earlier historical claim.

**HDIP-CLA-M16-R69 - Claim lifecycle.** A conformance claim MAY be superseded, withdrawn, expire or become stale, but its prior identity, scope, evidence and status SHALL remain historically traceable.

**HDIP-CLA-M16-R70 - Change-triggered reassessment.** Material change to semantics, Product family, policy/control, lifecycle, Interaction Contract, Boundary Contract, Profile or realization SHOULD trigger scoped conformance impact analysis and reassessment where affected.

**HDIP-CLA-M16-R71 - M17 reconciliation handoff.** M17 SHALL reconcile M16 invariant counts, identifiers, assessment modes, claim/outcome semantics and evidence/Profile rules against the complete M01-M16 baseline before 0.1 freeze.

**HDIP-CLA-M16-R72 - No premature executable standard.** M16 SHALL NOT prescribe a machine-readable conformance schema, certification service, scoring engine or universal evidence store; such formalization may follow the M17 human-readable baseline freeze.

---

# 20. What M16 deliberately does not decide

M16 does not prescribe:

- a certification body or organizational approval forum;
- a conformance percentage/score or maturity model;
- an enterprise risk-acceptance process;
- a machine-readable conformance schema;
- a universal evidence database/graph;
- a vendor conformance tool;
- a central control plane;
- one architecture-review workflow tool;
- implementation-specific policy-as-code technology;
- concrete thresholds for every Profile/risk class;
- whether a particular enterprise claim must be externally audited;
- the final cross-artifact reconciliation/freeze decisions that belong to M17.

M16 also does not make every invariant automatically machine-enforceable. Formal executable conformance may follow M17, but it must preserve the assessment-mode boundary established here.

---

# 21. M16 completion state

**HDIP-CLA M16 - COMPLETE.**

M16 establishes:

- **48 core Architecture Invariants (`M16-I01..I48`)**;
- preservation of all **40 M04 Design Invariants** plus **8 downstream conformance-closure invariants**;
- correction of the M04 invariant-family editorial count from seven to **six** without changing invariant meaning;
- **3 assessment modes** — STRUCTURAL, HYBRID and ASSESSMENT;
- **6 Conformance Subject classes**;
- **3 primary conformance claim types**;
- **4 invariant-level result states** — SATISFIED, VIOLATED, INDETERMINATE and NOT_APPLICABLE;
- **3 normative overall outcomes** — CONFORMANT, NONCONFORMANT and INDETERMINATE;
- an **18-dimension Conformance Evidence Package** model;
- an **18-dimension concrete Profile declaration/conformance model** (14 M14 dimensions + 4 M16 additions);
- **9 permitted Profile specialization operations**;
- **14 prohibited Profile operations**;
- a Realization Mapping Conformance model;
- explicit adjacent-conformance independence;
- explicit machine-checkability boundaries;
- historical conformance/claim lifecycle rules;
- **20 conformance/Profile anti-patterns**;
- **72 normative M16 rules**;
- **0 new canonical Planes**;
- **0 new canonical Overlays**;
- **0 new canonical ABBs**;
- **0 new Registries**;
- **0 new M12 interactions**;
- **0 new M13 Boundary Families**;
- **0 new M14 Realization/Profile Pattern families**;
- **0 new M15 Reference Views or Flows**.

M16 provides the normative basis from which a later executable HDIP conformance programme may safely automate structural portions without pretending to automate architectural judgement.

### Next stage

> **M17 - Cross-Artifact Reconciliation & HDIP-CLA 0.1 Freeze**

M17 will reconcile M01-M16 end to end, verify frozen identifiers/counts and cross-stage boundaries, close residual contradictions or terminology drift, establish the canonical human-readable HDIP-CLA 0.1 baseline and define the fidelity contract for any later machine-readable/executable formalization.
