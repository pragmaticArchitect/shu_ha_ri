---
id: hdip-cla-0.1-m05-responsibility-convergence-separation
title: HDIP-CLA 0.1 M05 - Responsibility Convergence & Separation Analysis
sidebar_label: M05 - Convergence & Separation
---

# HDIP-CLA 0.1 M05 - Responsibility Convergence & Separation Analysis

**Status:** COMPLETE

## 1. Purpose

M05 analyses the upstream responsibility corpus established in M02, the existing HDIP construct dispositions established in M03, and the principles/invariants established in M04 in order to determine **where HDIP responsibilities may converge, where they may share realization while remaining semantically distinct, where they must remain architecturally separate, and where they belong only to a domain/Product-family/profile specialization**.

M05 is the first stage at which the future HDIP logical architecture begins to emerge from the evidence, but it is still **not the Plane-derivation stage**.

```text
M02 source responsibilities
        +
M03 existing HDIP constructs
        +
M04 principles / invariants
        |
        v
M05 convergence & separation analysis
        |
        +-- convergent responsibility families
        +-- co-realization boundaries
        +-- separation locks
        +-- profile/specialization boundaries
        |
        v
M06 canonical logical Plane derivation
```

M05 therefore establishes **responsibility convergence families**, not final Planes, Overlays, ABBs, services or deployment components.

---

## 2. Analysis outcomes

M04 requires at least four possible outcomes. M05 uses them as follows.

| Outcome | M05 meaning |
|---|---|
| **CONVERGE** | The source responsibilities express materially the same enterprise-platform responsibility at a level where HDIP may define one shared logical responsibility family without erasing source semantics. |
| **CO-REALIZE BUT KEEP DISTINCT** | HDIP may supply shared implementation, tooling, experience or coordination, but the underlying responsibilities, semantic authorities or domain meanings must remain distinguishable. |
| **SEPARATE** | The responsibilities must remain explicitly separate because merging them would create semantic, authority, lifecycle or control ambiguity. Separate does **not** imply separate physical systems. |
| **PROFILE / SPECIALIZE** | The responsibility is legitimate only for a bounded Data, Information, Intelligence, Product-family, industry, operating-model or use-case specialization and must not be generalized into HDIP core merely for symmetry. |

A convergence decision is about **architectural responsibility**, not about whether two source terms look alike or can be implemented by the same technology.

---

## 3. Method

M05 applies the following tests to each recurring responsibility concern.

### 3.1 Responsibility-equivalence test

Two source obligations may converge only where their enduring enterprise-platform responsibility is materially equivalent after removing source-specific vocabulary.

### 3.2 Authority-preservation test

If convergence would transfer or obscure semantic, Product, policy, Data, Decision or ownership authority, the result cannot be `CONVERGE`.

### 3.3 Domain-distinction test

If the same implementation could support Data, Information and Intelligence but the domain behavior is intrinsically different, the result is normally `CO-REALIZE BUT KEEP DISTINCT`.

### 3.4 Topology-independence test

The decision must remain valid whether the eventual realization is centralized, federated, distributed, embedded, cloud-hosted or hybrid.

### 3.5 Lifecycle/experience test

A lifecycle, journey or UI projection is not treated as a Plane simply because it spans multiple responsibilities.

### 3.6 Profile test

A concern that exists only because of a Data-, Information-, Intelligence- or Product-family-specific semantic model is retained as `PROFILE / SPECIALIZE` unless independent evidence establishes a generic HDIP core responsibility.

### 3.7 Interaction-distance test

Where two responsibilities can legitimately converge, the convergence should reduce avoidable consumer/producer interaction distance without bypassing necessary authority, policy, evidence or accountability.

---

# 4. Canonical M05 Responsibility Convergence Families

M05 establishes **thirty responsibility convergence families (RCFs)** as analysis constructs for M06-M08.

> **Important:** An RCF is **not** a canonical HDIP Plane, Overlay or ABB. It is a stable convergence-analysis grouping used to derive those constructs later.

## 4.1 Intent, semantics, authority and governance

| ID | Responsibility family | Outcome | M05 decision |
|---|---|---|---|
| **RCF-01** | Governed Intent, Purpose & Use Context | **CONVERGE** | HDIP can provide one logical responsibility for capturing and carrying governed intent/purpose/use context across Data, Information and Intelligence. Domain-specific intent schemas and semantics remain typed. |
| **RCF-02** | Semantic Definition, Reference & Compatibility | **CO-REALIZE BUT KEEP DISTINCT** | Common semantic discovery, referencing, mapping and compatibility tooling may be shared, but GEDRM, GEARM, GEAIRM and enterprise/domain semantic authorities remain distinct. |
| **RCF-03** | Authority, Ownership, Accountability & Mandate | **CO-REALIZE BUT KEEP DISTINCT** | Identity/role/mandate infrastructure may be shared, but Data authority, Product ownership, delegated AI authority, policy authority and Decision authority are not interchangeable. |
| **RCF-04** | Governance, Policy, Control & Compliance | **CONVERGE** | Applicability resolution, control orchestration, exception handling, policy-aware execution and governance evidence form a shared platform responsibility; authoritative policy ownership remains external. |
| **RCF-05** | Security, Privacy, Identity & Entitlement | **CONVERGE** | Identity, authentication, entitlement, purpose limitation, privacy and protection responsibilities are platform-wide and may converge while retaining context-specific policies and scopes. |
| **RCF-06** | Product Qualification, Promise & Product-Family Semantics | **CO-REALIZE BUT KEEP DISTINCT** | HDIP may provide common Product identity/version/discovery/contract infrastructure, but Product qualification, PIN and family-specific semantics remain external to HDIP and distinct by family. |
| **RCF-07** | Product Development & Evolution Orchestration | **CO-REALIZE BUT KEEP DISTINCT** | A common HDIP development/evolution meta-lifecycle may coordinate intent, validation, compilation, deployment, publication and evolution, but detailed family lifecycles remain specialized; current Data PDEP Stage 0-10 is not universalized. |

## 4.2 Discovery, dependency, compilation and realization

| ID | Responsibility family | Outcome | M05 decision |
|---|---|---|---|
| **RCF-08** | Discovery & Governed Metadata Navigation | **CONVERGE** | Discovery of Products, capabilities, semantics, sources, contracts and eligible resources may share one governed discovery responsibility with typed results and authority-preserving references. |
| **RCF-09** | Dependency, Composition, Compatibility & Impact | **CONVERGE** | Dependency declaration/resolution, composition analysis, compatibility checks and change-impact analysis form a common logical responsibility, provided dependency types remain explicit. |
| **RCF-10** | Resolution, Validation & Compilation | **CONVERGE** | HDIP may provide a shared resolver/compiler responsibility that validates governed intent, resolves authoritative references, produces executable/operational projections and preserves decision evidence. Domain-specific compilation logic remains typed. |
| **RCF-11** | Deployment, Provisioning & Runtime Binding | **CONVERGE** | Generation of deployment/realization instructions, provisioning, runtime binding and promotion coordination may converge as platform engineering responsibility without making deployment a source of Productness or authority. |
| **RCF-12** | Data Processing, Information Formation & AI Execution | **CO-REALIZE BUT KEEP DISTINCT** | Common compute/orchestration/runtime infrastructure may co-realize these concerns, but Data transformation/movement, analytical Information formation and AI Execution have different semantics and must not become one generic execution concept. |
| **RCF-13** | AI Knowledge, Context & Grounding | **PROFILE / SPECIALIZE** | GEAIRA P2 responsibilities are legitimate Intelligence-domain responsibilities. They must not be generalized into a universal HDIP `Context` concern or equated with Data/Information semantics. |
| **RCF-14** | Intelligence Capability & Primitive Realization | **PROFILE / SPECIALIZE** | GEAIRA P3 capability/primitive responsibilities remain Intelligence-domain specializations; shared capability registries or runtime infrastructure do not turn all platform capabilities into AI Primitives. |

## 4.3 Serving, consumption and consequential integration

| ID | Responsibility family | Outcome | M05 decision |
|---|---|---|---|
| **RCF-15** | Serving, Provision, Ports & Interface Exposure | **CONVERGE** | Governed exposure through ports/interfaces, request/response or provision contracts, routing and result delivery may converge while preserving the intrinsic identity of the exposed capability/Product. |
| **RCF-16** | Consumer Onboarding, Access & Consumption | **CONVERGE** | Consumer discovery, onboarding, purpose/entitlement evaluation, access provisioning, consumption-event capture and consumption lifecycle management form a shared HDIP responsibility family. |
| **RCF-17** | Recommendation, Decision & Workflow Integration | **CO-REALIZE BUT KEEP DISTINCT** | Information/Intelligence may be integrated with decision/workflow environments through common integration mechanisms, but Recommendation, Decision and Action remain semantically distinct. |
| **RCF-18** | Decision Authorization, Consequential Action & Human Oversight | **PROFILE / SPECIALIZE** | GEAIRA P6 responsibilities remain a bounded Intelligence/automated-decision specialization. Point-of-use Authorization and consequential Action control must not be inferred as a universal requirement for every Data or Information consumption. |

## 4.4 Evidence, assurance, lifecycle and evolution

| ID | Responsibility family | Outcome | M05 decision |
|---|---|---|---|
| **RCF-19** | Provenance, Evidence & Traceability | **CONVERGE** | Evidence identity, correlation, provenance references, lineage and reconstruction responsibilities can converge as shared platform capability while preserving evidence type and source authority. |
| **RCF-20** | Observability, Telemetry & Auditability | **CONVERGE** | Operational and material interaction telemetry, monitoring and auditability are common platform responsibilities; observability does not become proof of assurance. |
| **RCF-21** | Quality, Fitness & Trust Evidence | **CO-REALIZE BUT KEEP DISTINCT** | Common evidence/assessment infrastructure may support Data quality, analytical quality, AI/model quality, Product quality and Fitness for Use, but those measures and authorities are not interchangeable and must not collapse into one opaque trust score. |
| **RCF-22** | Evaluation & Assurance | **CO-REALIZE BUT KEEP DISTINCT** | Evaluation and Assurance mechanics may share evidence infrastructure across domains, but Evaluation, control testing, assurance assessment and Product/AI-specific assurance retain distinct criteria and authority. |
| **RCF-23** | Lifecycle, Version, Currentness & Change | **CONVERGE** | Version identity, lifecycle state, currentness, compatibility, supersession, deprecation, migration and change propagation form a common platform responsibility with typed lifecycle semantics. |
| **RCF-24** | Outcome, Usage, Effectiveness & Feedback | **CONVERGE** | Usage/outcome evidence, consumer feedback, effectiveness assessment and evolution triggers form a common feedback responsibility; usage is not equated with value or success. |
| **RCF-25** | Resilience, Safety, Failure & Recovery | **CO-REALIZE BUT KEEP DISTINCT** | Resilience/failure handling can share platform mechanisms, while physical/AI safety, analytical degradation, Data delivery failure and service recovery keep context-specific semantics and controls. |

## 4.5 Shared foundation, registration and experience infrastructure

| ID | Responsibility family | Outcome | M05 decision |
|---|---|---|---|
| **RCF-26** | Shared Platform / Utility Foundation | **CONVERGE** | Compute, storage, network, messaging, orchestration, identity infrastructure, runtime hosting, secrets, deployment and telemetry transport form a shared enabling foundation without acquiring domain or semantic authority. |
| **RCF-27** | Registry & Governed Registration | **CO-REALIZE BUT KEEP DISTINCT** | Registry engines may be shared, but ADS, Product, Schema, Policy, Capability, Blueprint and later logical registry responsibilities retain distinct identities, ownership and authority semantics. |
| **RCF-28** | Catalog & Discovery Projection | **CONVERGE** | Catalog/search/index/projection responsibilities may converge across Product/capability types while remaining projections rather than qualification authorities. |
| **RCF-29** | Marketplace & Acquisition Experience | **CONVERGE** | Consumer-facing browse/evaluate/request/acquire/subscribe experiences may converge across eligible Products/capabilities while preserving Product-family and entitlement distinctions. |
| **RCF-30** | Cost & Economic Accountability | **SEPARATE** | Cost, chargeback/showback, resource economics and heavy-consumer accountability must remain distinct from Observability, Usage and Value. They may later co-realize operationally, but M05 rejects `Cost = Value = Observability`. |

---

# 5. Convergence outcome summary

The thirty RCFs yield the following M05 outcome distribution.

| Outcome | Count |
|---|---:|
| **CONVERGE** | 16 |
| **CO-REALIZE BUT KEEP DISTINCT** | 10 |
| **PROFILE / SPECIALIZE** | 3 |
| **SEPARATE** | 1 |
| **Total** | **30** |

The distribution is descriptive only. It is not a maturity score, weighting model or evidence that `CONVERGE` is preferable to another outcome.

The central M05 finding is:

> **HDIP convergence is strongest around reusable platform coordination, engineering, interaction, evidence and lifecycle responsibilities; it is weakest where the source architectures define intrinsic domain semantics, authority or consequential-control meaning.**

---

# 6. Canonical separation locks

The RCFs above identify positive convergence. M05 also establishes **sixteen separation locks** that M06-M15 must preserve even where implementation is shared.

| ID | Separation lock | Required distinction |
|---|---|---|
| **M05-SL01** | Semantic authority vs platform projection | Authoritative semantic models != HPD/SYNCTX/catalog/index/runtime projection. |
| **M05-SL02** | Product qualification vs platform participation | Product qualification != deployment != registration != publication != marketplace presence. |
| **M05-SL03** | Data authority vs Product ownership vs access authority | Authoritative Source/Source of Authority != Product Owner != consumer entitlement/Authorization. |
| **M05-SL04** | Policy authority vs resolution vs enforcement | Policy authoring/authority != applicability resolution/compilation != runtime enforcement. |
| **M05-SL05** | Semantic relationship vs executable binding | Semantic relationship != dependency edge != join/key binding != executable composition. |
| **M05-SL06** | Data processing vs Information formation vs AI Execution | Shared runtime does not make these one semantic execution type. |
| **M05-SL07** | Retrieval vs grounding vs authority/correctness | Retrieved resource != Grounding Source != authoritative source != correctness proof. |
| **M05-SL08** | AI Context vs Environment | Context material != execution Environment; environmental state may contribute to context without identity collapse. |
| **M05-SL09** | Recommendation vs Decision vs Authorization vs Action | Information/Intelligence effect != operative Decision != point-of-use Authorization != consequential Action. |
| **M05-SL10** | Quality vs trust vs Fitness for Use vs assurance | Quality evidence != trust conclusion != Fitness for Use != Assurance Finding. |
| **M05-SL11** | Provenance vs observability vs Control Evidence | Lineage/provenance != operational telemetry != proof that a control was effective. |
| **M05-SL12** | Registry vs Catalog vs Marketplace | Governed registration != discovery projection != consumer acquisition experience. |
| **M05-SL13** | Version vs latest vs current | A version may be newest without being governed-current or eligible for use. |
| **M05-SL14** | Usage vs outcome vs value vs cost | Use frequency != successful outcome != realized value != economic cost. |
| **M05-SL15** | Lifecycle/experience view vs architecture topology | PDEP/SSCF/flow-player stage or screen != Plane != Overlay != ABB. |
| **M05-SL16** | Utility foundation vs domain authority | Compute/storage/network/runtime/identity utility != Data/Information/Intelligence/Product/Governance authority. |

A separation lock is semantic/architectural. It does **not** require separately deployed systems.

---

# 7. Profile and specialization boundaries

M05 identifies responsibilities that are valid but must remain explicitly bounded rather than being promoted into holistic HDIP core by analogy.

| ID | Specialization | M05 boundary |
|---|---|---|
| **M05-PS01** | ADS / ADO / ADD | Data-domain HDIP specializations of GEDRA/GEDRM roles; not generic Information/Intelligence roles. |
| **M05-PS02** | Data PDEP Stage 0-10 | Canonical detailed Data Product PDEP specialization; PDEP G0/Spec A/Spec C are projections of the applicable lifecycle, not proof that the same stages govern every Product family. |
| **M05-PS03** | Information semantics and analytical formation | GEARM/GEARA-owned Information/Analytics responsibilities remain Information-domain semantics even when HDIP supplies common discovery/compilation/runtime tooling. |
| **M05-PS04** | AI Knowledge / Context / Grounding | GEAIRM/GEAIRA Intelligence-domain specialization; not a universal platform context model. |
| **M05-PS05** | Intelligence Capability / AI Primitive | GEAIRM/AIPS/GEAIRA specialization; generic HDIP capabilities do not become AI Primitives through registry membership. |
| **M05-PS06** | AI Execution / Agentic / Environment | GEAIRA P4 specialization; shared orchestration/compute may realize it without redefining generic Data/Information runtime behavior. |
| **M05-PS07** | Decision / Action / Human Oversight | GEAIRA P6 specialization applied where consequential AI/automated decision control is materially required. |
| **M05-PS08** | SYNCTX | Synthetic-generation specialization compiled from governed Data Product/version/schema/contract/policy evidence; not universal context or generic Product architecture. |
| **M05-PS09** | Data Mesh | Optional Data-domain operating-model/profile influence; not HDIP core architecture. |
| **M05-PS10** | Family-specific Product descriptors/deployment specs | DPROD, DPDS, AIPDS and analogous family artifacts remain governed by their applicable Product/family authorities and are referenced by HDIP rather than absorbed as generic semantics. |

---

# 8. Source-architecture coverage matrix

This matrix shows how every M02 source responsibility group participates in the M05 analysis. Because M02 deliberately preserved source granularity, a source group may map to several RCFs.

## 8.1 GEDRA coverage

| GEDRA source structure | Principal M05 RCFs | Convergence interpretation |
|---|---|---|
| Semantic & Enterprise Ontology | RCF-02, RCF-08, RCF-19, RCF-23 | Semantic responsibility co-realizes with common discovery/evidence/lifecycle capability but does not merge authority. |
| Authority | RCF-03, RCF-19, RCF-23 | Data authority remains distinct while mandate/currentness/evidence infrastructure may be shared. |
| Processing, Provision & Movement | RCF-09, RCF-11, RCF-12, RCF-15, RCF-19, RCF-23, RCF-25 | Processing is domain-specific; provision, evidence, lifecycle and resilience have stronger cross-domain convergence. |
| Data Platform & Product | RCF-06, RCF-07, RCF-08, RCF-09, RCF-15, RCF-21, RCF-23, RCF-27, RCF-28, RCF-29 | Product/platform responsibilities contribute strongly but Product identity stays family-authoritative. |
| Consumption & Access | RCF-05, RCF-15, RCF-16, RCF-19, RCF-23, RCF-24 | Strong convergence around governed consumption and consumer evidence. |
| Value, Observability & Feedback | RCF-20, RCF-24, RCF-30 | M05 explicitly separates operational observability, outcome/value and economic cost. |
| Cross-Cutting Governance & Control | RCF-03, RCF-04, RCF-05, RCF-19, RCF-21, RCF-22, RCF-23 | Strong candidate cross-cutting convergence, subject to M07. |
| Technology / Utility Foundation | RCF-26, RCF-25 | Common enabling foundation; no semantic authority. |

## 8.2 GEARA coverage

| GEARA source structure | Principal M05 RCFs | Convergence interpretation |
|---|---|---|
| P1 Intent, Semantics & Design | RCF-01, RCF-02, RCF-03, RCF-06, RCF-07, RCF-23 | Intent converges; semantic/Product meanings co-realize without merger. |
| P2 Discovery, Composition & Realization | RCF-08, RCF-09, RCF-10, RCF-11, RCF-23, RCF-27 | Strong convergence around self-service resolution/realization. |
| P3 Analytical Runtime & Information Formation | RCF-12, RCF-19, RCF-20, RCF-21, RCF-25 | Runtime infrastructure can be shared but analytical formation remains Information-domain meaning. |
| P4 Provision, Consumption & Decision Integration | RCF-15, RCF-16, RCF-17, RCF-19, RCF-20, RCF-23 | Serving/consumption converge; Decision integration remains distinct from Decision authority. |
| P5 Outcome, Value & Evolution | RCF-20, RCF-21, RCF-22, RCF-23, RCF-24 | Strong feedback/evolution convergence. |
| Governance / Policy / Assurance Fabric | RCF-04, RCF-22 | Governance converges; assurance remains distinguishable from policy/control. |
| Security / Privacy / Entitlement Fabric | RCF-05 | Strong common platform concern. |
| Provenance / Evidence / Observability Fabric | RCF-19, RCF-20 | Shared evidence/observability family with typed provenance. |
| Quality / Trust Fabric | RCF-21, RCF-22 | Co-realized assessment/evidence; no universal trust score. |
| Lifecycle / Version / Change Fabric | RCF-23 | Strong common platform concern. |
| Shared Platform / Utility Foundation | RCF-26, RCF-25 | Common foundation and resilience capability. |

## 8.3 GEAIRA coverage

| GEAIRA source structure | Principal M05 RCFs | Convergence interpretation |
|---|---|---|
| P1 AI Intent, Purpose & Authority | RCF-01, RCF-03, RCF-04, RCF-19, RCF-22, RCF-23 | Purpose handling can converge; delegated/AI authority remains typed. |
| P2 Knowledge, Context & Grounding | RCF-13, RCF-05, RCF-19, RCF-21, RCF-23, RCF-25 | Intelligence specialization with shared governance/evidence/lifecycle mechanisms. |
| P3 Intelligence Capability & Primitive | RCF-14, RCF-08, RCF-09, RCF-21, RCF-22, RCF-23, RCF-25 | Intelligence specialization using common discovery/evidence/lifecycle capabilities. |
| P4 AI Execution, Agentic & Environment | RCF-12, RCF-18, RCF-19, RCF-20, RCF-25 | AI Execution remains distinct while runtime/evidence/resilience infrastructure may be shared. |
| P5 AI Serving, Product & Integration | RCF-06, RCF-15, RCF-16, RCF-19, RCF-23, RCF-24 | Strong serving/consumption convergence with external Product-family authority preserved. |
| P6 Decision, Action & Human Oversight | RCF-17, RCF-18, RCF-19, RCF-22, RCF-23, RCF-25 | Consequential-control specialization; cannot collapse into ordinary serving/execution. |
| P7 Evaluation, Assurance, Observability & Evolution | RCF-19, RCF-20, RCF-21, RCF-22, RCF-23, RCF-24, RCF-25 | Strong cross-domain evidence/evolution convergence with Evaluation/Assurance distinctions preserved. |
| X1 Security, Privacy & Trust Boundaries | RCF-05, RCF-21, RCF-25 | Shared cross-cutting concern with AI-specific safety/trust context. |
| X2 Identity, Authority & Policy Enforcement | RCF-03, RCF-04, RCF-05, RCF-18 | Common identity/policy infrastructure; point-of-use AI authorization remains specialized. |
| X3 Evidence, Provenance & Traceability | RCF-19 | Strong common concern. |
| X4 Observability, Telemetry & Auditability | RCF-20 | Strong common concern. |
| X5 Resilience, Safety & Failure Management | RCF-25 | Common resilience mechanisms with specialized safety meaning. |
| X6 Lifecycle, Version, Currentness & Change | RCF-23 | Strong common concern. |
| X7 Interoperability, Contracts & Semantic Compatibility | RCF-02, RCF-09, RCF-15, RCF-23 | Contracts/compatibility can share infrastructure without semantic merger. |
| X8 Governance, Human Accountability & Compliance | RCF-03, RCF-04, RCF-18, RCF-22 | Shared governance infrastructure with context-specific accountability/oversight. |

This matrix accounts for the M02 corpus at its preserved source-group granularity. It does not claim that every statement inside a source group has the same outcome; the RCF-level rules and separation locks govern the finer interpretation.

---

# 9. Existing HDIP construct consequences

M05 now provides firmer architectural interpretation for the important M03 constructs.

## 9.1 PDEP

PDEP is a **lifecycle/experience composition across several RCFs**, principally:

```text
RCF-01  Intent
RCF-03  Authority / accountability
RCF-04  Governance / policy / control
RCF-06  Product semantics
RCF-07  Development / evolution orchestration
RCF-08  Discovery
RCF-09  Dependency / compatibility
RCF-10  Resolution / compilation
RCF-11  Deployment / provisioning
RCF-19  Evidence
RCF-21  Quality / fitness
RCF-23  Lifecycle / version / change
RCF-24  Outcome / feedback
```

Therefore:

```text
PDEP spans responsibility families
    !=
PDEP is automatically one canonical Plane
```

The Data PDEP Stage 0-10 model remains a Product-family specialization under `M05-PS02`.

## 9.2 SSCF and CEP

SSCF/CEP principally project:

```text
RCF-05  Security / entitlement
RCF-08  Discovery
RCF-15  Serving / provision
RCF-16  Consumer onboarding / consumption
RCF-19  Evidence
RCF-20  Observability
RCF-23  Lifecycle / change
RCF-24  Outcome / feedback
RCF-28  Catalog
RCF-29  Marketplace
```

SSCF is therefore a logical consumption lifecycle and CEP an experience responsibility composition. Neither earns Plane status merely from historical naming.

## 9.3 COVP

M05 resolves the most important COVP ambiguity by decomposing the acronym into distinct responsibility families:

```text
Cost           -> RCF-30
Observability  -> RCF-20
Value/Outcome  -> RCF-24
```

These concerns may be presented together to consumers or realized by shared infrastructure, but M05 explicitly rejects semantic equivalence among them.

The historical COVP acronym therefore remains **non-canonical pending M06/M07 naming/topology decisions**.

## 9.4 DPFI

The useful DPFI responsibility decomposes principally into:

```text
RCF-08  Discovery
RCF-09  Dependency / composition / compatibility
RCF-10  Resolution / validation / compilation
RCF-11  Realization / runtime binding
RCF-19  Evidence / traceability
RCF-23  Lifecycle / change
```

M05 therefore strengthens the decision that the underlying resolver/compiler responsibility survives while the historical expansion `Data Product Factory & Intelligence` does not determine canonical architecture naming.

## 9.5 HPD

HPD is not a responsibility family. It is a compiled operational projection supporting several families including RCF-06, RCF-08, RCF-09, RCF-19, RCF-20, RCF-23, RCF-27 and RCF-28.

## 9.6 SYNCTX

SYNCTX remains the `M05-PS08` synthetic-generation specialization. It participates in RCF-09/RCF-10 and may reference RCF-02/RCF-04/RCF-19/RCF-23 information, but it is not a generic Context responsibility and is not GEAIRA P2 AI Context.

## 9.7 Governance and Utility

Governance maps across several cross-cutting RCFs and remains a strong **M07 overlay candidate**, not an automatically preserved historical Plane.

Utility strongly converges into RCF-26 and remains an enabling foundation candidate rather than a semantic/domain Plane.

## 9.8 Registries, Catalog and Marketplace

M05 confirms three different concerns:

```text
RCF-27 Registry & Governed Registration
RCF-28 Catalog & Discovery Projection
RCF-29 Marketplace & Acquisition Experience
```

They may be delivered through one experience or platform implementation, but `M05-SL12` prevents their architectural collapse.

---

# 10. Emerging architecture signals for M06 and M07

M05 does not freeze Planes or Overlays, but the convergence evidence is now strong enough to identify **signals** that M06/M07 must test.

## 10.1 Primary-responsibility signals

The strongest recurring non-cross-cutting clusters are around:

1. **governed intent / semantics / authority / Product context**;
2. **discovery / dependency / composition / compilation / realization**;
3. **domain runtime / formation / execution**;
4. **serving / provision / consumer interaction**;
5. **outcome / feedback / evolution**.

These are evidence signals only. M06 must still test cohesion, boundary strength, non-redundancy and traceability before admitting any Plane.

## 10.2 Cross-cutting signals

The strongest recurring cross-cutting concerns are:

- governance / policy / control / compliance;
- security / privacy / identity / entitlement;
- provenance / evidence / traceability;
- observability / telemetry / auditability;
- quality / trust / assurance;
- lifecycle / version / currentness / change;
- resilience / safety / failure management;
- interoperability / contracts / semantic compatibility.

M07 must determine which of these become canonical HDIP Overlays, which remain interaction-contract properties, and which belong to the foundation or to Profile specialization.

## 10.3 Foundation signal

RCF-26 shows strong evidence for a shared Utility/Foundation concern, but M06 must determine whether HDIP represents that as a Foundation rather than a peer Plane.

## 10.4 Orthogonal Product lens signal

Product responsibilities cut across intent, development, compilation, serving, consumption, evidence and evolution. The evidence therefore supports continuing to treat **Product as an orthogonal qualification/lifecycle lens**, not automatically as one isolated Plane.

---

# 11. M05 normative rules

**HDIP-CLA-M05-R01 - Convergence is responsibility-based.** M05 convergence SHALL be based on enduring architectural responsibility and authority boundary, not label similarity, source Plane number, implementation co-location or historical diagram placement.

**HDIP-CLA-M05-R02 - RCF analysis status.** RCF-01 through RCF-30 SHALL be treated as canonical M05 convergence-analysis families and SHALL NOT by themselves be represented as canonical HDIP Planes, Overlays or ABBs.

**HDIP-CLA-M05-R03 - Outcome preservation.** M06-M08 SHALL preserve the M05 convergence outcome of an RCF unless a documented evidence-based revision explicitly reconciles the affected M04 invariants and source responsibilities.

**HDIP-CLA-M05-R04 - Convergence non-authority.** `CONVERGE` SHALL NOT transfer semantic, Product, policy, Data, Decision or ownership authority to HDIP.

**HDIP-CLA-M05-R05 - Co-realization distinction.** `CO-REALIZE BUT KEEP DISTINCT` SHALL permit shared implementation/tooling/experience while requiring the underlying responsibilities and identities to remain distinguishable.

**HDIP-CLA-M05-R06 - Separation non-topology.** `SEPARATE` SHALL require semantic/architectural separation but SHALL NOT automatically require separate deployable systems.

**HDIP-CLA-M05-R07 - Specialization restraint.** `PROFILE / SPECIALIZE` responsibilities SHALL NOT be generalized into HDIP core merely to create symmetry across Data, Information and Intelligence.

**HDIP-CLA-M05-R08 - Intent convergence.** HDIP MAY converge governed intent/purpose capture and propagation while preserving domain-specific intent semantics and authority.

**HDIP-CLA-M05-R09 - Semantic co-realization.** Semantic repositories, discovery and mapping capabilities MAY be shared, but GEDRM/GEARM/GEAIRM and applicable enterprise/domain semantic authorities SHALL remain distinct.

**HDIP-CLA-M05-R10 - Authority type separation.** Data authority, Product ownership, delegated authority, policy authority, entitlement and Decision/Action Authorization SHALL NOT be treated as one generic `authority` state.

**HDIP-CLA-M05-R11 - Governance convergence.** Governance applicability, policy-aware orchestration, control coordination and governance evidence MAY converge as HDIP platform responsibilities while upstream policy/control authority remains external.

**HDIP-CLA-M05-R12 - Product-family non-merger.** Common Product platform capability SHALL NOT collapse Data Product, Information Product, AI Product or other Product-family semantics into an HDIP-local Product type.

**HDIP-CLA-M05-R13 - PDEP family boundary.** PDEP MAY define a common development/evolution meta-lifecycle, but the current detailed Data PDEP Stage 0-10 sequence SHALL remain a Data Product specialization unless equivalent family-specific evidence is established.

**HDIP-CLA-M05-R14 - Discovery convergence with typed results.** Discovery MAY converge across Products, capabilities, semantics, sources and contracts provided returned identity/type/authority remains explicit.

**HDIP-CLA-M05-R15 - Dependency typing.** Dependency/composition convergence SHALL preserve distinctions among provenance, derivation, semantic relationship, Product composition, runtime input, provider dependency and executable binding.

**HDIP-CLA-M05-R16 - Compiler non-invention.** Converged resolution/compilation responsibilities SHALL preserve M04-I30 and SHALL NOT invent semantics, Productness, policy authority, joinability or obligations from weak evidence.

**HDIP-CLA-M05-R17 - Runtime domain distinction.** Shared runtime infrastructure SHALL NOT collapse Data processing, Information formation and AI Execution into one semantic runtime type.

**HDIP-CLA-M05-R18 - AI context specialization.** GEAIRA Knowledge/Context/Grounding responsibilities SHALL remain an Intelligence-domain specialization and SHALL NOT redefine SYNCTX, Data context, analytical input semantics or generic platform state.

**HDIP-CLA-M05-R19 - Intelligence primitive specialization.** AI Primitive/Intelligence Capability responsibilities SHALL remain governed by applicable Intelligence/AIPS/GEAIRA semantics and SHALL NOT be inferred from generic capability registration.

**HDIP-CLA-M05-R20 - Serving convergence.** HDIP MAY converge provision/serving/port/interface infrastructure while preserving Product/capability identity, contract semantics and provider/consumer authority boundaries.

**HDIP-CLA-M05-R21 - Consumption convergence.** Consumer onboarding, entitlement-aware access and consumption lifecycle responsibilities MAY converge across Data, Information and Intelligence without requiring every consumed capability to be a Product.

**HDIP-CLA-M05-R22 - Decision-control separation.** Recommendation/Information/Intelligence integration SHALL remain distinct from operative Decision, point-of-use Authorization and consequential Action control.

**HDIP-CLA-M05-R23 - Evidence convergence with type preservation.** Provenance, evidence and correlation infrastructure MAY converge while preserving evidence type, source authority, temporal context and the distinction from assurance conclusions.

**HDIP-CLA-M05-R24 - Observability non-assurance.** Converged observability/telemetry SHALL NOT by itself establish control effectiveness, correctness, trust, Fitness for Use or assurance.

**HDIP-CLA-M05-R25 - Quality/trust distinction.** Shared quality/trust infrastructure SHALL preserve domain-specific metrics and SHALL NOT reduce Quality, Trust, Fitness for Use and Assurance to one universal score.

**HDIP-CLA-M05-R26 - Lifecycle convergence with typed state.** Version/currentness/change infrastructure MAY converge while preserving the lifecycle semantics of Products, semantic models, contracts, policies, runtime realizations, evidence and assurance artifacts.

**HDIP-CLA-M05-R27 - COVP decomposition.** Cost, Observability and Value/Outcome SHALL remain distinct responsibility families even if presented or implemented together; the historical COVP acronym SHALL NOT override that separation.

**HDIP-CLA-M05-R28 - Registry logical independence.** Registry implementation MAY converge operationally, but logical registry responsibilities and authority semantics SHALL remain distinguishable and Catalog/Marketplace SHALL remain separate concerns.

**HDIP-CLA-M05-R29 - Foundation non-authority.** Shared Platform/Utility Foundation convergence SHALL NOT grant semantic, Product, governance, Data or Decision authority to enabling technology.

**HDIP-CLA-M05-R30 - Separation-lock status.** M05-SL01 through M05-SL16 SHALL constrain M06-M15 derivation and MAY be strengthened but SHALL NOT be silently removed by topology or implementation choices.

**HDIP-CLA-M05-R31 - Profile-boundary status.** M05-PS01 through M05-PS10 SHALL remain explicit specialization boundaries unless later programme evidence justifies promotion or further restriction.

**HDIP-CLA-M05-R32 - Source traceability.** Every M06 Plane candidate SHALL trace through one or more RCFs to the M02 source structures and M04 principles/invariants that justify it.

**HDIP-CLA-M05-R33 - No Plane freeze.** M05 SHALL NOT be interpreted as freezing the number, names or boundaries of HDIP Planes.

**HDIP-CLA-M05-R34 - No Overlay freeze.** M05 cross-cutting signals SHALL NOT be interpreted as freezing the number, names or boundaries of HDIP Overlays before M07.

**HDIP-CLA-M05-R35 - No ABB admission.** An RCF or historical HDIP construct SHALL NOT become a canonical ABB without satisfying the M08 admission discipline.

---

# 12. What M05 deliberately does not decide

M05 does **not** decide:

- final HDIP Plane count or names;
- whether intent, design, discovery, compilation or deployment belong to one or several Planes;
- whether runtime is represented as one shared Plane or multiple domain responsibility views;
- final governance/assurance/security/evidence/lifecycle Overlay boundaries;
- whether Utility is represented as a Foundation, Overlay or other canonical structure;
- final ABB identities;
- physical registry consolidation;
- whether DPFI survives as an acronym/name;
- final COVP replacement terminology;
- final Product Registry generalization model;
- final Blueprint Registry/Library terminology;
- physical deployment topology;
- concrete inter-plane interactions;
- final PDEP family profiles;
- conformance modes or machine-checkability.

These remain downstream decisions.

---

# 13. M05 completion state

**HDIP-CLA M05 - COMPLETE.**

M05 establishes:

- **30** canonical responsibility convergence families for derivation analysis;
- **16 CONVERGE** outcomes;
- **10 CO-REALIZE BUT KEEP DISTINCT** outcomes;
- **3 PROFILE / SPECIALIZE** outcomes;
- **1 SEPARATE** outcome;
- **16 canonical separation locks**;
- **10 explicit profile/specialization boundaries**;
- source-architecture coverage across all M02 GEDRA, GEARA and GEAIRA responsibility groups;
- explicit decomposition of PDEP, SSCF/CEP, COVP, DPFI, HPD, SYNCTX, Governance, Utility and Registry/Catalog/Marketplace into responsibility-level architecture concerns;
- **35 normative M05 rules**;
- **0 canonical HDIP Planes**;
- **0 canonical HDIP Overlays**;
- **0 canonical HDIP ABBs**.

### Next stage

> **M06 - Canonical Logical Plane Derivation**

M06 will test the M05 responsibility convergence families for cohesion, boundary strength, non-redundancy, cross-cutting character and architectural usefulness in order to derive the smallest defensible set of canonical HDIP logical Planes without inheriting historical boxes or forcing one-to-one source-architecture mappings.
