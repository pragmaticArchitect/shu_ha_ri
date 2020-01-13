---
id: hdip-cla-0.1-a3-invariant-conformance-catalogue
title: HDIP-CLA 0.1 A3 - Invariant & Conformance Catalogue
sidebar_label: A3 - Invariant & Conformance Catalogue
---

# HDIP-CLA 0.1 A3 — Invariant & Conformance Catalogue

**Status:** COMPLETE  
**Programme:** HDIP-CLA 0.1 machine-readable / executable formalization  
**Human-readable authority:** M16 + M17 frozen baseline  
**Primary machine artifact:** `/specs/hdip-cla/0.1/a3/invariant-conformance-catalogue.json`

## 1. Purpose

A3 formalizes the frozen M16 architecture-invariant and conformance model into one deterministic machine-readable catalogue.

> **A3 records what may be checked, what must be judged, and how a conformance claim is bounded; it does not convert architectural judgement into false machine certainty.**

A3 therefore formalizes:

- M16-I01..I48 and their seven families;
- STRUCTURAL, HYBRID and ASSESSMENT modes;
- invariant applicability and result vocabularies;
- CS1..CS6 Conformance Subject classes;
- Core, Profile and Realization Mapping claim types;
- CONFORMANT / NONCONFORMANT / INDETERMINATE overall outcomes;
- the eighteen-dimension Conformance Evidence Package;
- concrete Profile dimensions and permitted/prohibited specialization operations;
- Realization Mapping expectations;
- machine-checkability boundaries;
- historical claim lifecycle and the M16 assessment workflow.

A3 introduces no new HDIP architecture invariant, conformance outcome, authority, waiver state, certification body, scoring model or executable proof engine.

---

# 2. Authority and fidelity boundary

The frozen M16/M17 human-readable architecture remains authoritative. A1 supplies canonical machine identities; A2 supplies typed relationship/traceability coverage. A3 uses both, but neither relationship existence nor machine serialization establishes invariant satisfaction.

```text
A1 identity
   +
A2 relationship / traceability
   +
M16 conformance meaning
   |
   v
A3 invariant / conformance catalogue
```

If A3 conflicts with M16/M17 meaning, A3 is defective and must be corrected.

---

# 3. Invariant metamodel

Each invariant record contains:

```text
identity
canonical name
family
canonical condition
assessment mode
automation boundary
source invariant ancestry where applicable
A2 scope/coverage relationships where available
source-document provenance
```

The A2 `GOVERNS_ELEMENT` relation is scope/coverage evidence only. It is **not** an assertion that the invariant is satisfied.

---

# 4. Canonical invariant families and catalogue

A3 preserves all **48** M16 invariants in the same seven families.

## 4.1 Authority, semantics and jurisdiction

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I01** | Semantic authority preservation | **HYBRID** | HDIP-CLA SHALL NOT incompatibly redefine concepts, relationships or invariants owned by GEDRM, GEARM, GEAIRM or other applicable semantic authorities. |
| **M16-I02** | Product authority preservation | **HYBRID** | Generic Product identity, Product Intrinsic Nature and Product qualification SHALL remain governed by BPS/PIN rather than inferred by HDIP. |
| **M16-I03** | Product-family authority preservation | **HYBRID** | Data Product, Information Product, AI Product and other Product-family qualification/classification SHALL remain with the applicable Product-family authority. |
| **M16-I04** | Scoped authority | **HYBRID** | Authority used by HDIP SHALL be explicit for an applicable scope, role, purpose, lifecycle state and/or jurisdiction where those distinctions matter; platform participation SHALL NOT imply universal authority. |
| **M16-I05** | Shared-realization non-transfer | **HYBRID** | Co-location, shared storage, shared runtime, shared registry, shared UI or shared platform realization SHALL NOT by itself transfer semantic, Product, policy, decision or ownership authority. |
| **M16-I06** | Semantic-gap escalation | **HYBRID** | Where HDIP needs a semantic concept not owned by HDIP, the gap SHALL be referred to or extended through the appropriate semantic authority rather than silently minted as platform semantics. |
| **M16-I07** | Authority non-transitivity | **HYBRID** | Authority, approval, entitlement, policy applicability or ownership SHALL NOT become automatically transitive merely because a dependency, composition or interaction crosses an HDIP boundary. |

## 4.2 Responsibility, structure and topology

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I08** | Responsibility before component | **HYBRID** | A canonical HDIP ABB or mandatory implementation responsibility SHALL be justified by explicit architectural responsibility; a noun, tool, service label or historical box alone is insufficient. |
| **M16-I09** | Logical plane semantics | **STRUCTURAL** | A future HDIP Plane SHALL represent a coherent logical responsibility grouping and SHALL NOT imply a mandatory system, deployment unit, network tier, team, organizational boundary or lifecycle step. |
| **M16-I10** | Topology independence | **ASSESSMENT** | HDIP-CLA conformance SHALL NOT depend on centralized, federated, distributed, edge, embedded, provider-managed or hybrid deployment topology unless a narrower Profile explicitly requires it. |
| **M16-I11** | Many-to-many realization | **STRUCTURAL** | One implementation MAY realize responsibilities from several HDIP logical structures, and one HDIP responsibility MAY be distributed across several implementations. |
| **M16-I12** | Source-plane non-equivalence | **HYBRID** | GEDRA, GEARA and GEAIRA plane numbering, placement or lexical similarity SHALL NOT force one-to-one HDIP plane mapping. |
| **M16-I13** | Cross-cutting visibility | **HYBRID** | A responsibility that is cross-cutting in an applicable source architecture SHALL NOT be silently localized into one future HDIP plane without explicit justification that preserves its cross-cutting obligations. |
| **M16-I14** | Foundation separation | **HYBRID** | Compute, storage, networking, messaging, identity infrastructure, orchestration and other utility capabilities SHALL NOT acquire semantic, Product, governance or domain authority merely because they enable those responsibilities. |
| **M16-I15** | Architecture traceability | **STRUCTURAL** | Every future canonical HDIP Plane, Overlay, ABB and material interaction SHALL trace to upstream responsibilities, explicit enterprise platform requirements and/or justified HDIP-specific coordination responsibilities. |

## 4.3 Data, Information, Intelligence and Product identity

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I16** | Domain distinction | **HYBRID** | Data, Information and Intelligence SHALL remain distinguishable architectural/semantic concerns even where one platform capability co-realizes responsibilities from more than one domain. |
| **M16-I17** | No cross-domain inheritance | **HYBRID** | A Data-specific, Information-specific or Intelligence-specific construct SHALL NOT automatically generalize to the other domains through shared implementation or naming similarity. |
| **M16-I18** | No automatic Productness | **HYBRID** | Composition, generation, transformation, persistence, deployment, publication, registration, cataloguing, marketplace presence, API exposure, repeated use or consumption SHALL NOT by itself establish Product identity. |
| **M16-I19** | Product-family distinction | **HYBRID** | Co-realization of Data Products, Information Products and AI Products SHALL NOT collapse them into one HDIP-local Product family or type. |
| **M16-I20** | Composition non-inheritance | **HYBRID** | Using, depending on, containing, deriving from or invoking a Product/capability SHALL NOT by itself transfer its Product family, ontology type, ownership or authority to the dependent/composed result. |
| **M16-I21** | Direct capability validity | **ASSESSMENT** | HDIP SHALL be able to support governed Data, Information or Intelligence capability use where Product qualification is not intended; Productization SHALL NOT be a mandatory gateway for every governed interaction. |

## 4.4 Governed self-service, lifecycle and experience

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I22** | Governed self-service | **HYBRID** | Self-service SHALL operate inside applicable authority, policy, security, privacy, quality, evidence and lifecycle constraints; self-service SHALL NOT mean unrestricted infrastructure or data access. |
| **M16-I23** | Intent/compilation separation | **HYBRID** | Participant-declared intent, business semantics and accountable judgement SHALL remain distinguishable from platform resolution, compilation, provisioning and automation. |
| **M16-I24** | Automation non-ownership | **HYBRID** | HDIP automation SHALL NOT transfer Product ownership, Data authority, policy authority or decision accountability to the compiler/runtime merely because the platform performs most technical work. |
| **M16-I25** | Judgement honesty | **ASSESSMENT** | Architecture/governance decisions requiring contextual or accountable judgement SHALL NOT be represented as machine-proven solely because metadata, telemetry, rules or model outputs exist. |
| **M16-I26** | PDEP canonical lifecycle identity | **STRUCTURAL** | PDEP SHALL remain the canonical HDIP Product Development and Evolution Process identity; historical SSPD terminology MAY remain only for traceability and SHALL NOT become a competing lifecycle. |
| **M16-I27** | Progressive PDEP projection | **HYBRID** | PDEP G0 and PDEP Spec A MAY compress/group canonical stages for progressive disclosure, while PDEP Spec C SHALL remain synchronized with the canonical applicable detailed PDEP lifecycle. |
| **M16-I28** | Experience non-authority | **HYBRID** | Interactive flow players, diagrams, dashboards and experience projections SHALL NOT independently create lifecycle stages, authority, Product identity, ABBs or architecture semantics. |

## 4.5 Projection, compilation, registry and discovery

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I29** | Projection non-authority | **HYBRID** | HPD, SYNCTX, resolved graphs, compiled governance bundles, compilation packs and similar HDIP-generated projections SHALL NOT override the authoritative semantics or governance sources they reference. |
| **M16-I30** | Compiler non-invention | **HYBRID** | HDIP resolution/compilation SHALL NOT manufacture semantic relationships, Product identity, policy authority, joinability, provenance, dependencies or obligations from weak evidence or naming similarity. |
| **M16-I31** | Logical registry independence | **STRUCTURAL** | ADS, Product, Schema, Policy, Capability and Blueprint registry responsibilities SHALL remain logically distinguishable even where one implementation realizes several of them. |
| **M16-I32** | Registry non-qualification | **HYBRID** | Registration SHALL NOT by itself prove authoritative status, Product status, control effectiveness, semantic correctness, fitness or HDIP conformance. |
| **M16-I33** | Registry/catalog/marketplace distinction | **STRUCTURAL** | Registry, Catalog and Marketplace responsibilities SHALL NOT be treated as architectural synonyms even when exposed through one user experience or implementation. |
| **M16-I34** | Shared registry realization allowed | **HYBRID** | HDIP MAY consolidate registry implementation where operationally useful provided logical identities, ownership, contracts, lifecycle and authority boundaries remain distinguishable. |

## 4.6 Evidence, trust, version and historical meaning

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I35** | Evidence by construction | **HYBRID** | Material HDIP interactions SHOULD emit or retain applicable provenance, control, quality, observability and lifecycle evidence sufficient for later reconstruction and assessment. |
| **M16-I36** | Trust is contextual | **ASSESSMENT** | Platform location, certification label, popularity, centralization, Product status or registry presence SHALL NOT be treated as universal proof of trust or fitness; trust assessment SHALL remain contextual and evidence-based. |
| **M16-I37** | Missing evidence is not positive evidence | **HYBRID** | Missing, stale, inaccessible or materially ambiguous evidence SHALL NOT be interpreted as positive assurance. |
| **M16-I38** | Version/currentness distinction | **HYBRID** | Version identity, latest/newest status and governed currentness SHALL remain distinguishable; newest SHALL NOT automatically mean current or approved. |
| **M16-I39** | Historical truth | **HYBRID** | Later supersession, revocation, re-evaluation, upstream change, rollback or re-publication SHALL NOT silently rewrite which semantics, Product Version, policy/control, dependency, context or realization governed a historical occurrence. |
| **M16-I40** | Provenance is not assurance | **HYBRID** | Provenance and lineage SHALL support traceability but SHALL NOT by themselves prove correctness, authorization, control effectiveness, assurance or Fitness for Use. |

## 4.7 Derived conformance closure

| ID | Name | Assessment mode | Canonical condition |
|---|---|---|---|
| **M16-I41** | Canonical structure integrity | **STRUCTURAL** | A conformant HDIP architecture SHALL preserve the canonical identity and responsibility meaning of P1-P5, X1-X9, HDIP-FND and the M08 ABB catalogue; implementation grouping, view projection or profile specialization SHALL NOT silently redefine those canonical structures. |
| **M16-I42** | Interaction-contract preservation | **HYBRID** | Material interactions SHALL preserve the applicable M12 Interaction Contract identity and obligations even when the participating responsibilities are co-located, embedded, distributed, provider-operated or implemented through a mechanism other than a network API. |
| **M16-I43** | External-boundary jurisdiction preservation | **HYBRID** | Material crossings of an M13 Boundary Family SHALL preserve the applicable external authority, jurisdiction, currentness, evidence and failure obligations; physical co-location or shared-provider realization SHALL NOT erase the logical boundary. |
| **M16-I44** | Product-access / consequence separation | **HYBRID** | Product or Product-Port access approval, entitlement or successful consumption SHALL NOT by itself authorize a downstream consequential Decision, Tool use, Digital Action or Physical Action where separate point-of-use authority is applicable. |
| **M16-I45** | Lifecycle / runtime non-equivalence | **HYBRID** | PDEP, SSCF and CEP SHALL remain lifecycle/experience compositions and SHALL NOT be interpreted as mandatory synchronous runtime pipelines; an established governed runtime MAY reuse current lifecycle state until material change requires re-evaluation. |
| **M16-I46** | Realization mapping traceability | **HYBRID** | A concrete realization claiming HDIP alignment SHALL retain traceability from applicable canonical responsibilities, ABBs, Interaction Contracts, Boundary Families and Profile obligations to the Realization Units, human processes or adjacent systems that satisfy them. |
| **M16-I47** | Adjacent-conformance independence | **HYBRID** | HDIP conformance SHALL NOT by itself establish conformance to GEDRA, GEARA, GEAIRA, BPS/PIN, a Product-family specification, an external standard or provider certification, and conformance to an adjacent specification SHALL NOT by itself establish HDIP conformance. |
| **M16-I48** | Profile monotonicity | **HYBRID** | An HDIP Profile MAY select, tighten, contextualize, specialize, narrow and extend the baseline for a bounded scope, but SHALL NOT weaken, waive or incompatibly redefine an applicable core invariant or transfer authority from an external semantic, Product, policy or Decision authority. |

> M16-I01..I40 preserve M04-I01..I40. M16-I41..I48 are the downstream conformance-closure invariants. A3 preserves this ancestry rather than flattening all 48 into newly invented machine rules.

---

# 5. Assessment modes and automation ceilings

| Mode | Count | Machine role | Final assessment boundary |
|---|---:|---|---|
| **STRUCTURAL** | 7 | Deterministic structural checking may be material. | A machine may determine only what is fully represented by the formalized evidence; this is not runtime correctness or assurance. |
| **HYBRID** | 37 | Structural checks may support assessment. | Accountable architecture/evidence review remains necessary for final satisfaction. |
| **ASSESSMENT** | 4 | Machine checks may organize/support evidence. | Accountable judgement is primary; machine PASS cannot establish final satisfaction by itself. |

Assessment mode is not severity, maturity or optionality.

---

# 6. Applicability and invariant results

A3 preserves the M16 distinction between **applicability** and **result**.

## 6.1 Applicability states

```text
APPLICABLE
NOT_APPLICABLE
UNDETERMINED   # assessment-time applicability state
```

`NOT_APPLICABLE` requires scope-based rationale. It is not a waiver. `UNDETERMINED` is not a positive result; if material applicability remains unresolved at decision time the assessment cannot silently pass.

## 6.2 Final invariant results

```text
SATISFIED
VIOLATED
INDETERMINATE
NOT_APPLICABLE
```

Invalid shortcuts remain invalid: absence of observed failure, registry presence, latest version, certification or telemetry alone does not imply `SATISFIED`.

---

# 7. Conformance Subject model

| ID | Subject class | Meaning |
|---|---|---|
| **CS1** | Enterprise HDIP Architecture | Enterprise-wide or multi-domain HDIP target/current architecture. |
| **CS2** | Domain / Portfolio HDIP Architecture | A Data, Information, Intelligence or cross-domain bounded architecture. |
| **CS3** | Governed HDIP Profile | A concrete enterprise/domain/Product-family/high-assurance/Data-Mesh specialization. |
| **CS4** | Platform / Solution Architecture | A bounded platform, solution or capability architecture claiming HDIP alignment. |
| **CS5** | Product / Capability Realization Architecture | A bounded Product or non-Product capability realization using applicable PDEP/SSCF/runtime responsibilities. |
| **CS6** | Concrete Realization Mapping | The mapping from canonical/Profile architecture into actual deployed/human/provider Realization Units. |

Every claim must identify subject identity/version, claim type, scope, architecture boundary, HDIP baseline, applicable Profiles and assessment time/version. Conformance of one subject does not automatically propagate to another.

---

# 8. Conformance claim types

| Claim type | Meaning |
|---|---|
| **Core Architecture Conformance** | The subject preserves all applicable M16 core invariants and the applicable responsibilities/contracts of the HDIP-CLA 0.1 baseline. |
| **Profile Conformance** | The subject is Core-conformant and satisfies a named, governed, M16-valid HDIP Profile. |
| **Realization Mapping Conformance** | A concrete implementation mapping faithfully realizes the claimed Core/Profile architecture, including traceability to Realization Units, M12 contracts, M13 boundaries/EBCs, evidence responsibilities, currentness and failure/recovery obligations. |

Profile Conformance is stronger/narrower than Core Architecture Conformance; it is not an alternate route around Core obligations. Realization Mapping Conformance is separately evidenced and does not follow merely from an architecture declaration.

---

# 9. Overall conformance outcomes

| Outcome | Meaning |
|---|---|
| **CONFORMANT** | Every applicable core invariant is SATISFIED; N/A results have justified scope rationale; all obligations required by the claim type are satisfied. |
| **NONCONFORMANT** | At least one applicable core invariant is VIOLATED, or a mandatory claim-type obligation is demonstrably violated. |
| **INDETERMINATE** | No applicable core invariant is known to be violated, but one or more material applicable obligations cannot be determined with sufficient evidence. |

```text
applicable violation
    -> NONCONFORMANT

no violation + unresolved material evidence
    -> INDETERMINATE

all applicable obligations established
    -> CONFORMANT
```

A3 does **not** define `CONDITIONALLY_CONFORMANT`. Remediation, risk acceptance or exception workflow may be tracked elsewhere but does not alter the M16 outcome.

---

# 10. Conformance Evidence Package

A3 preserves the **18-dimension** logical evidence contract. It does not prescribe one evidence database, graph, certification portal or document format.

| # | Dimension | Minimum content |
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

The unambiguous label **Conformance Evidence Package** is preferred in user-facing material to avoid collision with M11 `CEP — Consumer Experience Projection`.

---

# 11. Profile specialization and conformance

A3 records **18 concrete Profile dimensions**: the fourteen M14 dimensions plus four M16 conformance additions.

```text
01 identity/version
02 scope
03 parent baseline
04 external authorities
05 applicable Planes/ABBs
06 applicable Overlays
07 lifecycle specialization
08 registry/projection specialization
09 interaction specialization
10 boundary specialization
11 allowed realization patterns
12 evidence/assurance
13 non-applicability rationale
14 conformance claim
15 invariant applicability matrix
16 specialization-operation record
17 Profile composition/conflict record
18 Profile assessment/evidence state
```

## 11.1 Permitted Profile operations

| Operation | Meaning |
|---|---|
| **SELECT** | Select an applicable baseline option or pattern. |
| **REQUIRE** | Make an optional/conditional baseline responsibility mandatory within Profile scope. |
| **TIGHTEN** | Strengthen a threshold, control, evidence or lifecycle obligation. |
| **CONTEXTUALIZE** | Bind a baseline concept to a bounded enterprise/domain context without redefining it. |
| **SPECIALIZE** | Introduce a family/domain specialization consistent with the parent authority. |
| **NARROW** | Reduce allowed choices or topology/interaction options for a bounded risk/context reason. |
| **EXTEND** | Add local obligations/fields/controls that do not conflict with core meaning. |
| **ADD_EVIDENCE** | Require stronger/additional evidence, assurance or human review. |
| **RESTRICT_REALIZATION** | Constrain permitted M14 patterns/localities/providers for the bounded Profile. |

## 11.2 Prohibited Profile operations

| Operation | Meaning |
|---|---|
| **WEAKEN_CORE** | Reduce an applicable core invariant or mandatory baseline obligation. |
| **WAIVE_TO_PASS** | Waive a violation and still report Profile/Core conformance. |
| **REDEFINE_EXTERNAL_SEMANTICS** | Take ownership of GEDRM/GEARM/GEAIRM or other external semantics. |
| **REDEFINE_PRODUCTNESS** | Redefine BPS/PIN Product qualification or Product Intrinsic Nature. |
| **TRANSFER_AUTHORITY** | Infer Data, Product, policy or Decision authority from platform participation. |
| **COLLAPSE_PRODUCT_FAMILIES** | Erase Data/Information/AI Product-family distinctions. |
| **UNIVERSALIZE_SPECIALIZATION** | Impose a Data-, Information- or Intelligence-specific lifecycle/construct on all families without authority/evidence. |
| **REMOVE_APPLICABLE_OVERLAY** | Suppress an applicable X1-X9 obligation because implementation is inconvenient. |
| **REMOVE_EVIDENCE_OBLIGATION** | Eliminate material evidence/currentness/history requirements needed by the parent baseline. |
| **REDEFINE_CANONICAL_STRUCTURE** | Silently rename/redefine P1-P5, X1-X9, ABBs or M12/M13 identities as different architecture semantics. |
| **CONFLATE_REGISTRY_CATALOG_MARKETPLACE** | Erase their canonical responsibility distinction. |
| **INFER_PRODUCTNESS** | Create Product status from registration, publication, deployment, exposure or repeated use. |
| **REWRITE_HISTORY** | Project latest Profile/policy/topology state backwards onto earlier occurrences. |
| **N/A_BY_CONVENIENCE** | Mark a material core obligation not applicable merely to avoid remediation. |

The governing principle remains `Profile = monotonic specialization`, not waiver or local fork.

---

# 12. Realization Mapping Conformance

A3 preserves many-to-many realization. A conformant mapping may map one Realization Unit to many responsibilities and one responsibility to many units. The minimum conceptual mapping retains:

```text
canonical/Profile responsibility
Realization Unit(s) / human process / adjacent system
locality / provider / admin owner
M12 contract(s)
M13 boundary/EBC(s)
evidence/currentness producer
failure/recovery behavior
applicable Profile(s)
```

Component-count symmetry is not required; responsibility coverage, contract/boundary integrity and evidence are.

---

# 13. Adjacent conformance independence

A3 preserves the frozen rule:

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

Multiple claims may coexist for one solution, but each retains its own subject, version, scope, authority and evidence.

---

# 14. Machine-checkability boundary

## 14.1 Safely automatable examples

- identifier presence/uniqueness
- declared version relationships
- required field presence
- declared Plane/Overlay/ABB coverage
- M12 interaction identifier/reference consistency
- M13 Boundary/EBC declaration completeness
- Profile parent/version declaration
- prohibited direct identifier collisions
- selected lifecycle stage/projection synchronization where mechanically represented
- evidence-reference presence and staleness flags where time semantics are explicit

## 14.2 Hybrid examples

- whether a local semantic extension has captured external authority
- whether two implementations truly preserve Product-family distinction
- whether compilation has manufactured a relationship from weak evidence
- whether an Access Decision has leaked into consequential-action authority
- whether a provider substitution is semantically/contractually safe
- whether historical reconstruction is materially sufficient

## 14.3 Assessment-primary examples

- contextual trust / Fitness for Use
- adequacy of accountable human judgement
- architecture significance of a semantic/authority gap
- proportionality of a high-assurance Profile
- whether a complex realization introduces unacceptable hidden authority or evidence coupling

> **Machine-checkable structure may support conformance; it must not simulate certainty where architecture judgement is required.**

---

# 15. Historical claim lifecycle

A conformance claim is versioned and time-bound. Later reassessment, supersession, withdrawal, expiration, Profile change, provider migration or policy revocation may alter future status but must not rewrite the earlier claim/evidence that actually governed at that time.

The machine catalogue lists lifecycle-event examples as **illustrative, not exhaustive**; it does not create a new frozen state machine.

---

# 16. Assessment workflow

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

---

# 17. A3 anti-patterns

1. **Diagram Match Conformance**
2. **Technology Badge Conformance**
3. **Terminology Conformance**
4. **Percentage Conformance**
5. **Waiver-to-Pass**
6. **Not-Applicable Shopping**
7. **Inherited Platform Conformance**
8. **Profile Rewrites Core**
9. **Profile Owns External Semantics**
10. **Vendor Becomes ABB**
11. **Structural-Only Assurance**
12. **Telemetry-Only Evidence Package**
13. **Latest-Only Assessment**
14. **One Global Claim**
15. **Adjacent Conformance Leakage**
16. **Pattern Means Conformant**
17. **Maturity Equals Conformance**
18. **Automated Judgement Theatre**
19. **Gate-Count Conformance**
20. **Registration/Productness Conformance**

---

# 18. Canonical A3 normative rules

**HDIP-CLA-A3-R01 — Source authority.** A3 SHALL treat the frozen M16/M17 human-readable baseline as authoritative over machine representation.
**HDIP-CLA-A3-R02 — No redesign.** A3 SHALL formalize conformance meaning and SHALL NOT introduce a new architecture invariant, authority, Product rule or conformance state.
**HDIP-CLA-A3-R03 — A1 identity reuse.** A3 SHALL reuse A1 identities for M16-I01..I48 and CS1..CS6.
**HDIP-CLA-A3-R04 — A2 relationship reuse.** A3 SHALL reference A2 scope/traceability where useful and SHALL NOT reinterpret relationship existence as invariant satisfaction.
**HDIP-CLA-A3-R05 — Catalogue determinism.** The canonical A3 JSON SHALL serialize the same conformance catalogue deterministically for later reconciliation.
**HDIP-CLA-A3-R06 — Human-readable precedence.** Where A3 conflicts with M16/M17, A3 SHALL be corrected rather than used to reinterpret the human-readable baseline.
**HDIP-CLA-A3-R07 — No certification authority.** A3 SHALL NOT create a certification body, approval forum or universal conformance service.
**HDIP-CLA-A3-R08 — No score.** A3 SHALL NOT introduce an aggregate percentage or maturity score as a substitute for invariant results.
**HDIP-CLA-A3-R09 — Forty-eight invariants.** A3 SHALL register exactly M16-I01..I48 as the core HDIP-CLA 0.1 invariant catalogue.
**HDIP-CLA-A3-R10 — Seven families.** A3 SHALL preserve the seven M16 invariant families and their invariant membership.
**HDIP-CLA-A3-R11 — Canonical condition fidelity.** Each invariant record SHALL preserve the canonical M16 condition without weakening or paraphrase-based semantic substitution.
**HDIP-CLA-A3-R12 — Assessment mode fidelity.** Each invariant SHALL retain exactly one M16 primary assessment mode: STRUCTURAL, HYBRID or ASSESSMENT.
**HDIP-CLA-A3-R13 — M04 ancestry.** M16-I01..I40 SHALL preserve traceability to M04-I01..I40 through A2 ancestry records.
**HDIP-CLA-A3-R14 — Closure invariant distinction.** M16-I41..I48 SHALL remain downstream closure invariants rather than be falsely assigned M04 ancestry.
**HDIP-CLA-A3-R15 — Scope relation non-proof.** A2 GOVERNS_ELEMENT relationships SHALL indicate invariant coverage only and SHALL NOT assert SATISFIED status.
**HDIP-CLA-A3-R16 — Mode not severity.** Assessment mode SHALL NOT be interpreted as invariant criticality, severity, optionality or maturity.
**HDIP-CLA-A3-R17 — Structural restraint.** STRUCTURAL mode SHALL permit machine checking only for conditions actually represented in formal evidence and SHALL NOT imply runtime correctness or assurance.
**HDIP-CLA-A3-R18 — Hybrid restraint.** HYBRID mode SHALL require accountable review for final satisfaction where interpretation/evidence remains material.
**HDIP-CLA-A3-R19 — Assessment honesty.** ASSESSMENT mode SHALL keep accountable judgement primary and SHALL NOT be represented as definitively machine-proven.
**HDIP-CLA-A3-R20 — Explainable automation.** Machine-supported results SHOULD identify invariant, input evidence/version and evaluation category for accountable review.
**HDIP-CLA-A3-R21 — Applicability vocabulary.** A3 SHALL preserve APPLICABLE, NOT_APPLICABLE and UNDETERMINED as the applicability-state vocabulary.
**HDIP-CLA-A3-R22 — N/A non-waiver.** NOT_APPLICABLE SHALL require a bounded scope rationale and SHALL NOT operate as a waiver.
**HDIP-CLA-A3-R23 — Undetermined applicability.** UNDETERMINED SHALL remain an assessment-time state and SHALL NOT be converted into a positive final result.
**HDIP-CLA-A3-R24 — Invariant result vocabulary.** A3 SHALL preserve SATISFIED, VIOLATED, INDETERMINATE and NOT_APPLICABLE as final invariant-result tokens.
**HDIP-CLA-A3-R25 — No silent positive.** Absence of failure/evidence, certification, Registry presence, latest version or telemetry SHALL NOT be machine-translated into SATISFIED.
**HDIP-CLA-A3-R26 — Evidence insufficiency.** Materially insufficient evidence SHALL remain INDETERMINATE rather than be coerced to SATISFIED.
**HDIP-CLA-A3-R27 — No conditional pass.** A3 SHALL NOT define CONDITIONALLY_CONFORMANT or another positive outcome absent from M16.
**HDIP-CLA-A3-R28 — Result/applicability separation.** Applicability and final result SHALL remain separately represented so N/A and uncertainty cannot be conflated.
**HDIP-CLA-A3-R29 — Three outcomes.** A3 SHALL preserve exactly CONFORMANT, NONCONFORMANT and INDETERMINATE as normative overall outcomes.
**HDIP-CLA-A3-R30 — Conformant outcome.** CONFORMANT SHALL require all applicable core invariants to be SATISFIED plus all claim-type obligations, with justified N/A results.
**HDIP-CLA-A3-R31 — Nonconformant outcome.** Any applicable core invariant VIOLATED or mandatory claim obligation violated SHALL result in NONCONFORMANT.
**HDIP-CLA-A3-R32 — Indeterminate outcome.** Where no violation is known but material applicable obligations remain unresolved, overall outcome SHALL be INDETERMINATE.
**HDIP-CLA-A3-R33 — Administrative state separation.** Risk acceptance, remediation or exception workflow SHALL remain separate from the normative conformance outcome.
**HDIP-CLA-A3-R34 — Six subject classes.** A3 SHALL preserve CS1..CS6 as the six principal M16 Conformance Subject classes.
**HDIP-CLA-A3-R35 — Bounded claim scope.** Every claim SHALL retain subject identity/version, claim type, scope, architecture boundary, HDIP baseline, applicable Profiles and assessment time/version.
**HDIP-CLA-A3-R36 — No enterprise inference.** Conformance of one subject SHALL NOT imply enterprise-wide, domain-wide, Product-wide or workload-wide conformance beyond the assessed scope.
**HDIP-CLA-A3-R37 — Three claim types.** A3 SHALL preserve Core Architecture, Profile and Realization Mapping as the three primary claim types.
**HDIP-CLA-A3-R38 — Profile claim strength.** Profile Conformance SHALL require Core conformance plus the named governed Profile obligations.
**HDIP-CLA-A3-R39 — Realization mapping claim.** Realization Mapping Conformance SHALL require evidence that concrete realization faithfully maps the claimed Core/Profile architecture.
**HDIP-CLA-A3-R40 — Claim non-implication.** Claim types SHALL NOT automatically imply each other unless their required evidence has actually been assessed.
**HDIP-CLA-A3-R41 — Eighteen evidence dimensions.** A3 SHALL preserve all eighteen M16 Conformance Evidence Package dimensions.
**HDIP-CLA-A3-R42 — Evidence package logicality.** The Conformance Evidence Package SHALL remain a logical evidence contract and SHALL NOT require one database, graph, portal or document format.
**HDIP-CLA-A3-R43 — External authority evidence.** The evidence package SHALL preserve external authority mapping where applicable and SHALL NOT annex external authority.
**HDIP-CLA-A3-R44 — Invariant assessment record.** Evidence SHALL be able to record invariant applicability, mode, result, rationale and evidence references.
**HDIP-CLA-A3-R45 — N/A and limitation evidence.** N/A rationales, unresolved evidence, gaps and dependencies SHALL remain explicit in the evidence package.
**HDIP-CLA-A3-R46 — Accountability retention.** Positive claims SHALL retain accountable assessor/authority, assessment version/time and evidence location/reference.
**HDIP-CLA-A3-R47 — Version/currentness evidence.** Evidence SHALL preserve versions, currentness/effective-time and historical context where material.
**HDIP-CLA-A3-R48 — Eighteen Profile dimensions.** A3 SHALL preserve the fourteen M14 Profile dimensions plus four M16 conformance additions as an eighteen-dimension concrete Profile model.
**HDIP-CLA-A3-R49 — Permitted operations.** A3 SHALL preserve exactly the nine permitted M16 Profile operation classes.
**HDIP-CLA-A3-R50 — Prohibited operations.** A3 SHALL preserve exactly the fourteen prohibited M16 Profile operation classes.
**HDIP-CLA-A3-R51 — Profile non-waiver.** A Profile SHALL NOT weaken or waive an applicable core invariant while retaining a positive conformance claim.
**HDIP-CLA-A3-R52 — Profile authority restraint.** Profile specialization SHALL NOT transfer or redefine external semantic, Product, policy, Data or Decision authority.
**HDIP-CLA-A3-R53 — Many-to-many realization.** Realization Mapping SHALL allow many-to-many mapping between canonical/Profile responsibilities and Realization Units.
**HDIP-CLA-A3-R54 — Responsibility evidence.** Realization Mapping Conformance SHALL assess responsibility coverage and boundary integrity rather than component-count symmetry.
**HDIP-CLA-A3-R55 — Adjacent conformance independence.** HDIP conformance and adjacent-specification/Product/provider conformance SHALL remain independently scoped claims.
**HDIP-CLA-A3-R56 — Historical non-rewrite.** Later reassessment, Profile change, provider migration or withdrawal SHALL NOT rewrite the prior claim/evidence that governed historically.
**HDIP-CLA-A3-R57 — Claim lifecycle traceability.** Superseded, withdrawn, expired, stale or reassessed claims SHALL retain prior identity, scope, evidence and outcome for historical reconstruction.
**HDIP-CLA-A3-R58 — Scoped reassessment.** Material change SHOULD trigger scoped conformance impact analysis and reassessment where affected.
**HDIP-CLA-A3-R59 — A6 handoff.** A6 SHACL MAY encode safely structural constraints but SHALL NOT encode HYBRID/ASSESSMENT judgement as definitive graph conformance.
**HDIP-CLA-A3-R60 — A7/A8 handoff.** A7/A8 schemas MAY validate structure and required declarations but SHALL NOT make schema validity synonymous with HDIP conformance.
**HDIP-CLA-A3-R61 — A9-A11 handoff.** A9-A11 examples and tests SHALL trace expected results to A3 invariant/claim semantics and shall distinguish structural from judgement-dependent expectations.
**HDIP-CLA-A3-R62 — A12 execution boundary.** A12 automated conformance runner SHALL report only machine-validatable conclusions and SHALL surface HYBRID/ASSESSMENT obligations for accountable review.
**HDIP-CLA-A3-R63 — A13/A14 reconciliation.** A13/A14 SHALL reconcile A3 counts, tokens, invariant conditions, A1 identities and A2 traceability deterministically.
**HDIP-CLA-A3-R64 — A4 graph handoff.** A4 RDF/OWL SHALL project A3 conformance entities and classifications without making assessment-mode or outcome semantics stronger than M16 permits.

---

# 19. Validation expectations

A3 validation checks the invariant identity/mode catalogue, controlled vocabularies, subject/claim/outcome counts, evidence/Profile dimensions, operation sets, A1/A2 reference integrity, deterministic CSV/JSON projections, Docusaurus IDs/sidebar references and predecessor-byte preservation.

Passing A3 structural validation does **not** assert that a concrete Conformance Subject is HDIP-conformant.

---

# 20. A3 completion state

**HDIP-CLA A3 — COMPLETE.**

A3 establishes:

- **48** machine-readable Architecture Invariants in **7** families;
- exact **7 STRUCTURAL / 37 HYBRID / 4 ASSESSMENT** mode distribution;
- **3** applicability states;
- **4** invariant-result tokens;
- **6** Conformance Subject classes;
- **3** primary conformance claim types;
- **3** normative overall outcomes;
- the **18-dimension Conformance Evidence Package**;
- the **18-dimension concrete Profile model**;
- **9** permitted and **14** prohibited Profile operations;
- Realization Mapping and adjacent-conformance boundaries;
- machine-checkability examples and automation ceilings;
- historical claim-lifecycle preservation;
- the **18-step** assessment workflow;
- **20** conformance/Profile anti-patterns;
- **64** normative A3 formalization rules.

A3 introduces no new human-readable HDIP architecture semantics and does not create an executable certification result by itself.

### Next stage

> **A4 — RDF/OWL Architecture Graph**

A4 will project A1 identities, A2 typed relationships and A3 invariant/conformance classifications into an RDF/OWL graph while preserving authority, non-equivalence, non-transitivity and machine-judgement boundaries.
