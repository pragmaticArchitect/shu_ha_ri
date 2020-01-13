---
id: hdip-cla-0.1-m11-sscf-cep-architecture
title: HDIP-CLA 0.1 M11 - Product Consumption & Runtime Architecture - SSCF / CEP
sidebar_label: M11 - SSCF / CEP Architecture
---

# HDIP-CLA 0.1 M11 - Product Consumption & Runtime Architecture - SSCF / CEP

**Status:** COMPLETE

## 1. Purpose

M11 freezes the canonical HDIP architecture for governed **Product consumption and consumer runtime interaction** through **SSCF - Self-Service Consumption Flow** and **CEP - Consumer Experience Projection**.

M11 reconciles:

- the five canonical HDIP Planes from M06;
- the nine cross-cutting Overlays from M07;
- the twenty-two canonical logical ABBs from M08;
- the Registry, Catalog, Marketplace, descriptor and projection boundaries from M09;
- the PDEP publication/handoff architecture from M10;
- the existing eight-stage HDIP Product-consumption lifecycle;
- the historical `Consumer Experience Plane` terminology and persona-oriented consumer experience material.

M11 answers five primary questions:

1. How does a Product move from **published/available** to **governed consumer use**?
2. Which parts of consumption are lifecycle responsibilities and which are repeatable runtime responsibilities?
3. How are Product access, Product Ports, usage obligations and downstream Decision/Action authorization kept distinct?
4. What is CEP after M06 established P1-P5 as the canonical Plane model?
5. How do consumption evidence, cost, outcome/value and feedback return into PDEP without manufacturing Productness or rewriting history?

M11 does not redefine Product qualification, Product-family semantics, Data/Information/AI semantics, Product Port semantics owned by the applicable Product authority, or consequential Decision/Action authorization owned by applicable adjacent architectures and authorities.

---

# 2. Canonical SSCF positioning

SSCF is the canonical HDIP **logical Product-consumption lifecycle**.

```text
SSCF
  = Self-Service Consumption Flow

SSCF
  != canonical HDIP Plane
  != canonical HDIP Overlay
  != canonical HDIP ABB
  != mandatory synchronous runtime pipeline
  != Product qualification authority
  != universal lifecycle for every non-Product capability
```

Historical material sometimes expands SSCF as `Self-Service Product Consumption Flow`. M11 normalizes the canonical expansion to **Self-Service Consumption Flow** while retaining the historical wording as a descriptive alias where traceability is useful. The scope of M11 SSCF is Product consumption.

HDIP may also support direct governed use of non-Product Data, Information or Intelligence capabilities through applicable P4/P3 responsibilities. Such direct use is valid but is **not automatically SSCF Product consumption**.

---

# 3. Lifecycle versus runtime

M11 makes a strict distinction between the consumption lifecycle and repeatable runtime invocation.

## 3.1 SSCF lifecycle

The SSCF lifecycle establishes or changes governed consumer state:

```text
intent
  -> resolution
  -> fit/access decision
  -> purpose-bound provisioning
  -> consumption experience
  -> usage evidence
  -> outcome/economic/value evidence
  -> feedback / continuation / PDEP entry
```

## 3.2 Consumption runtime

Once current governed state exists, a repeatable consumption runtime may be substantially shorter:

```text
Consumer / PCON
      |
      | current Access Descriptor
      | + Usage Contract
      | + entitlement / purpose context
      v
HDIP-P4 Product Port / Interface Exposure
      |
      +--> Product/capability runtime may invoke typed P3 responsibility
      |
      v
Typed Product output / response / event / experience
      |
      +--> X3 evidence
      +--> X4 telemetry
      +--> X5 quality/fitness/trust evidence where applicable
      +--> X9 cost evidence where applicable
      |
      v
P5 outcome / feedback / evolution interpretation
```

A long-lived subscription, system integration, dashboard session, event consumer or agentic consumer therefore does not have to execute eight synchronous stages for every interaction.

Currentness remains governed. Material changes to Product Version, Product Port, purpose, identity, entitlement, policy, Usage Contract, assurance state or other applicable conditions may require re-evaluation or lifecycle re-entry.

---

# 4. Canonical eight-stage SSCF lifecycle

M11 freezes the existing eight-stage SSCF lifecycle as the canonical detailed HDIP Product-consumption lifecycle:

| Stage | Canonical SSCF stage | Principal architectural treatment |
|---|---|---|
| **1** | **Declare Consumption Intent** | Establish Consumption Intent Record (CIR) and governed use context. |
| **2** | **Resolve Product Set** | Discover and resolve eligible candidate Products with typed identity and fit rationale. |
| **3** | **Evaluate Product Fit and Request Access** | Evaluate suitability and produce a purpose-bound Product-access decision. |
| **4** | **Provision Purpose-Bound Access** | Bind entitlement/access state to already-defined Product Ports and consumption obligations. |
| **5** | **Consume Through CEP** | Consume through governed Product Ports using the appropriate Consumer Experience Projection. |
| **6** | **Capture Usage Signals** | Capture governed consumption telemetry and evidence. |
| **7** | **Compute and Observe Product Signals** | Derive and expose distinct cost, outcome/value and other consumption evidence without semantic collapse. |
| **8** | **Decision, Feedback & Creation Loop** | Continue, stop, provide feedback, select alternatives or enter PDEP for governed Product constitution/evolution. |

The numbered stages are lifecycle organization aids. They do not require one service per stage and do not imply that every runtime call traverses Stage 1 through Stage 8.

---

# 5. Canonical Plane composition

SSCF is a cross-Plane lifecycle composition.

| Plane | SSCF responsibility |
|---|---|
| **HDIP-P1 Governed Intent, Definition & Authority Context** | Capture/confirm consumption purpose, consumer/use context, relevant identity/accountability context and authoritative semantic/Product references needed to interpret intended use. |
| **HDIP-P2 Discovery, Composition & Realization** | Discover and resolve Products, navigate Catalog projections, preserve typed dependency/compatibility information and support fit/availability evaluation. |
| **HDIP-P3 Runtime, Formation & Execution** | Execute the typed Product/capability runtime behind or through the consumed Product Port where applicable; Data, Information and Intelligence runtime semantics remain distinct. |
| **HDIP-P4 Provision, Consumption & Integration** | Own the principal Product access, Product Port exposure, consumption, experience mediation and downstream integration responsibilities. |
| **HDIP-P5 Outcome, Value & Evolution** | Interpret usage/outcome/value evidence and feedback, support continuation/substitution decisions and trigger governed evolution/PDEP entry. |

SSCF primarily concentrates on P1/P2/P4/P5. P3 participates where Product consumption invokes or depends on a runtime realization; SSCF does not absorb Product-internal runtime semantics into the consumer lifecycle.

---

# 6. Canonical ABB participation

## 6.1 Stage-to-ABB mapping

| SSCF stage | Principal ABB participation |
|---|---|
| **1 Declare Consumption Intent** | `HDIP-P1-ABB-01` Governed Intent & Use Context Boundary; `HDIP-P1-ABB-03` where consumer/accountability context is material. |
| **2 Resolve Product Set** | `HDIP-P2-ABB-01` Governed Discovery & Navigation Boundary; `HDIP-P2-ABB-02` Dependency, Composition & Compatibility Boundary. |
| **3 Evaluate Fit / Request Access** | `HDIP-P2-ABB-01/02` for fit context plus `HDIP-P4-ABB-02` Consumer Access & Consumption Boundary for the Product-access decision. |
| **4 Provision Purpose-Bound Access** | `HDIP-P4-ABB-01` Provision & Interface Exposure Boundary plus `HDIP-P4-ABB-02` Consumer Access & Consumption Boundary. |
| **5 Consume Through CEP** | `HDIP-P4-ABB-01/02`; `HDIP-P4-ABB-03` where downstream workflow/integration mediation is material; typed P3 ABB invoked where the Product runtime requires it. |
| **6 Capture Usage Signals** | `HDIP-P4-ABB-02` with X3/X4 cross-cutting participation. |
| **7 Compute / Observe Product Signals** | `HDIP-P5-ABB-01` Outcome, Effectiveness & Feedback Boundary and `HDIP-P5-ABB-02` Value Assessment & Evolution Boundary, with X4/X5/X6/X9 as applicable. |
| **8 Decision / Feedback / Creation Loop** | `HDIP-P5-ABB-01/02` plus governed handoff/re-entry to P1/P2 through PDEP where a Product-development/evolution intent is created. |

## 6.2 No historical service-name inheritance

The existing SSCF material uses useful implementation-style labels such as:

- Intent Interpreter + Normalizer;
- Product Resolution Engine;
- Product Discovery Orchestrator;
- Policy Service;
- Access Provisioning Service;
- Entitlements Service;
- CEP Renderer;
- Usage Tracking Service;
- FinOps Engine;
- Value Computation Engine;
- Product Observability Engine;
- Feedback Processor.

M11 retains their legitimate responsibilities but **does not admit these names as canonical ABBs**. Their responsibilities map into the M08 ABBs and X1-X9 Overlays.

---

# 7. Cross-cutting Overlay participation

All nine canonical Overlays may apply to SSCF according to context.

| Overlay | SSCF role |
|---|---|
| **X1 Governance, Policy, Control & Compliance** | Resolve/propagate Product-access policy, usage obligations, exceptions and applicable controls without making HDIP the policy authority. |
| **X2 Security, Privacy, Identity & Entitlement** | Authenticate participants/workloads, evaluate and enforce entitlement, purpose limitation, privacy and protection obligations. |
| **X3 Provenance, Evidence & Traceability** | Correlate CIR, Product resolution, Access Decision, access provisioning, Product Version/Port, consumption occurrence, feedback and lifecycle evidence. |
| **X4 Observability, Telemetry & Auditability** | Capture operational/usage telemetry and make material consumption behavior observable. |
| **X5 Quality, Fitness & Trust Evidence** | Surface typed quality/fitness/trust evidence relevant to Product selection and use without collapsing it into one score. |
| **X6 Evaluation & Assurance** | Support fit/readiness/assurance assessment where required; telemetry or quality evidence alone does not prove assurance. |
| **X7 Lifecycle, Version, Currentness & Change** | Govern current Product/Port/access/contract/policy state, expiry, revocation, supersession and re-evaluation triggers. |
| **X8 Resilience, Safety, Failure & Recovery** | Govern degraded consumption, retries/fallbacks, failover/recovery and profile-specific safety obligations. |
| **X9 Economic & Cost Accountability** | Attribute and expose consumption cost/economic evidence while preserving `cost != usage != outcome != value`. |

Overlay application does not imply one centralized service per Overlay or one Overlay-specific step in SSCF.

---

# 8. PDEP publication to SSCF boundary

M10 ends Product development with a published/registered Product Version and governed exposure. M11 begins consumer-specific lifecycle activity.

```text
PDEP / publication side

qualified Product Version
+ Product Registry registration facts
+ Catalog projection
+ Marketplace availability where applicable
+ governed Product Ports
+ Product contract / usage constraints
+ HPD / DPP / evidence projections where applicable
             |
             | availability for governed discovery
             v
SSCF / consumer side

CIR
-> Product Resolution Set
-> Product selection / Access Decision
-> Access Descriptor + Usage Contract
-> governed access to Product Ports
-> consumption occurrences
-> signals / evidence / feedback
```

The boundary preserves these distinctions:

```text
published         != entitled
registered        != discoverable in every Catalog
catalogued        != available in every Marketplace
marketplace-listed != access-approved
access-approved   != access-provisioned
access-provisioned != downstream action-authorized
```

PDEP creates/publishes the Product realization and its Product Ports. SSCF provisions **consumer access to** applicable Product Ports; it does not create Product Ports merely because a consumer is onboarded.

---

# 9. Consumer identity and role model

## 9.1 Product Consumer (PCON)

`PCON` is the accountable consumer role in SSCF. A PCON may be represented by or interact through:

- a human business user;
- an analytical user/system;
- a software/system consumer;
- an AI-enabled consumer;
- an agentic/workflow consumer;
- another governed Product/capability acting as consumer where architecture permits.

The role describes participation in Product consumption; it does not imply Product ownership, Data authority, delegated authority or consequential Decision authority.

## 9.2 Human, system and agentic consumers

Automation does not remove SSCF obligations.

```text
human consumer
system consumer
agentic consumer
     |
     +--> all remain subject to applicable
          purpose, entitlement, contract,
          evidence, lifecycle and control obligations
```

Agentic consumption does **not** by itself establish delegated authority. Where an AI/Agent consumer performs a consequential Decision, Tool use, Digital Action or Physical Action, applicable GEAIRA/enterprise point-of-use authorization and human-oversight obligations remain separately applicable.

---

# 10. Canonical entry modes

## 10.1 Intent-first mode

**Intent-first** remains the canonical HDIP SSCF entry mode.

A consumer first expresses the desired outcome, purpose and use context. HDIP creates or validates a **Consumption Intent Record (CIR)** before governed Product resolution and access.

Benefits include:

- outcome-oriented discovery rather than keyword-only browsing;
- purpose-aware Product fit and access evaluation;
- explicit context for value/outcome interpretation;
- stronger evidence linkage from intent through consumption and feedback.

## 10.2 Browse-first mode

Browse-first remains a valid convenience entry mode.

A consumer may begin in a Catalog or Marketplace, but a CIR or equivalent confirmed governed intent context must exist before purpose-bound Product access is granted.

```text
browse first
   !=
intent absent
```

## 10.3 Established-state mode

M11 additionally recognizes a runtime reuse pattern for already-established consumers.

Where a current CIR, Access Decision, Access Descriptor, Usage Contract, entitlement state and Product/Port Version remain valid, repeat consumption may reuse that state rather than replaying discovery/onboarding on every call.

Reuse is conditional on X7 currentness and applicable policy/security controls.

---

# 11. Stage 1 - Consumption Intent architecture

Stage 1 establishes the governed consumer purpose/use context.

Canonical output:

> **CIR - Consumption Intent Record**

A CIR SHOULD identify, as applicable:

- consumer/PCON identity or accountable context;
- intended outcome/need;
- declared purpose;
- use context;
- consumer/persona category where useful;
- relevant constraints or preferences;
- requested time/currentness horizon;
- target environment/workflow context where material;
- traceability to the declaration/actor and CIR version.

CIR is an operational lifecycle artifact, not an access authorization or policy authority.

```text
CIR
  != entitlement
  != Access Decision
  != Product qualification
  != consequential Decision authorization
```

---

# 12. Stage 2 - Product resolution architecture

Stage 2 resolves candidate Products against CIR while preserving Product and source authority.

Canonical output:

> **Product Resolution Set**

A Product Resolution Set MAY include:

- Product and Product Version identifiers;
- Product Family/Kind references from authoritative Product semantics;
- applicable Product Ports / interface categories;
- Catalog/Marketplace availability context;
- fit/suitability rationale;
- compatibility notes;
- quality/fitness/trust evidence references;
- cost/economic indicators where appropriate;
- currentness/lifecycle state;
- constraints, caveats or missing-evidence warnings;
- resolution evidence explaining why candidates were included/excluded/ranked.

Resolution uses M09 distinctions:

```text
Product Registry
    -> governed registration facts / authoritative references

Catalog
    -> search / discovery / projection

Marketplace
    -> acquisition / subscription / consumer experience
```

Neither Catalog nor Marketplace presence establishes Productness or entitlement.

Ranking/fit logic SHALL NOT hide material constraints or treat an opaque score as proof of semantic compatibility, trust, fitness or assurance.

---

# 13. Stage 3 - Product fit and access-decision architecture

Stage 3 has two related but distinct responsibilities:

1. **Product fit/suitability evaluation** - does the Product appear appropriate for the CIR and declared use?
2. **Product-access decision** - may this consumer access the selected Product/Port for the declared purpose under applicable policy and entitlement?

Canonical access artifact:

> **SSCF Access Decision**

An Access Decision SHOULD identify, where applicable:

- consumer/subject identity;
- CIR identity/version and purpose;
- Product/Product Version and applicable Port scope;
- decision result (`ALLOW`, `DENY`, `CONDITIONAL` or governed equivalent);
- authoritative policy/entitlement references;
- conditions/limitations;
- effective/expiry/currentness information;
- accountable approval/judgement where required;
- evidence and rationale sufficient for later reconstruction.

The Access Decision boundary is strict:

```text
Product / Product Port Access Decision
               !=
Data authority
               !=
Product ownership
               !=
policy authority
               !=
GEAIRA point-of-use Authorization
               !=
consequential Decision / Action approval
```

---

# 14. Stage 4 - Purpose-bound access provisioning

Stage 4 materializes an approved/conditional Product-access decision.

Canonical outputs include:

- **Access Descriptor**;
- **Usage Contract** or equivalent consumption-binding artifact;
- entitlement/access bindings to applicable Product Ports.

## 14.1 Access Descriptor

An Access Descriptor identifies how the consumer may invoke/access the approved Product Port(s), including applicable endpoint/reference, scope, authentication/entitlement context, effective period and runtime restrictions.

It is a consumer-specific operational binding, not a Product Port definition.

## 14.2 Usage Contract

The SSCF Usage Contract captures consumer-specific allowed/expected consumption conditions such as:

- permitted purpose/scope;
- applicable Product/Port Version;
- usage modes;
- obligations and restrictions;
- quota/budget/rate constraints;
- freshness/currentness expectations where relevant;
- SLA/SLO or support expectations where applicable;
- evidence/telemetry obligations;
- expiry/review/currentness conditions.

The SSCF Usage Contract does not replace the Product's authoritative Product/Port contract. It binds consumer-specific conditions to that contract.

---

# 15. Canonical CEP architecture

## 15.1 Canonical term

M11 normalizes **CEP** to:

> **Consumer Experience Projection**

Historical HDIP material used **Consumer Experience Plane**. That expansion is retained only as a historical alias because M06 has already frozen P1-P5 as the canonical HDIP Plane model.

```text
CEP - Consumer Experience Projection

CEP
  != canonical HDIP Plane
  != canonical HDIP Overlay
  != canonical HDIP ABB
  != mandatory standalone renderer/service
```

## 15.2 Purpose

CEP is the governed consumer-facing projection/composition through which discovery, Product access, Product Port use, consumption evidence and feedback are presented or mediated for a consumer context/persona.

CEP principally composes:

- P2 discovery/navigation projections;
- P4 Product access, interface exposure, consumption and integration;
- P5 outcome/feedback/value views;
- applicable X1-X9 obligations/evidence.

## 15.3 Persona projections

CEP MAY adapt presentation and interaction for contexts such as:

- business;
- analytical;
- AI-enabled;
- system/API;
- agentic/workflow.

A persona projection changes **experience**, not Product identity or semantic authority.

```text
same Product / Port
       +
different consumer projection
       !=
new Product automatically
```

## 15.4 Transformation boundary

CEP SHALL NOT silently turn presentation into semantic transformation or Product constitution.

A dashboard that presents an existing Product output may be a CEP view. A process that materially joins, transforms, derives, persists or re-contracts outputs may create a separate governed asset/capability and may require PDEP/Product qualification if intentionally constituted as a Product.

Therefore:

```text
render / project existing Product output
        !=
materially derive new governed output
        !=
constitute new Product
```

## 15.5 Historical CEP Renderer

`CEP Renderer` remains a useful historical implementation label. Its responsibilities are now realized through P4 ABBs and client/platform experience mechanisms. M11 does not admit a canonical `CEP Renderer` ABB.

---

# 16. Product Port and runtime architecture

## 16.1 Product Port boundary

A Product Port is part of the governed Product interface/contract. SSCF consumes through applicable Product Ports; it does not define Product internals.

Product Port categories may include, where the applicable Product family allows:

- API/request-response interfaces;
- query endpoints;
- event/stream interfaces;
- file/object interfaces;
- analytical/reporting interfaces;
- AI/agent interfaces;
- workflow/integration interfaces;
- other governed Product-family-specific interfaces.

This list is illustrative, not a mandatory technology catalogue.

## 16.2 Encapsulation and evidence

Consumers SHOULD be protected from unnecessary internal implementation coupling, but this does not mean all dependency/provenance information is hidden.

```text
internal implementation encapsulation
        !=
provenance opacity
```

Contractually relevant dependencies, provenance, quality, currentness and assurance information may need to be exposed as evidence even when internal deployment mechanics remain encapsulated.

## 16.3 P3 / P4 boundary

P4 owns consumer-facing provision/consumption/integration responsibility. P3 owns typed Data-processing, Information-formation or Intelligence-execution runtime responsibility.

A Product invocation MAY cross P4 into P3, but consumption does not merge those responsibilities.

---

# 17. Stage 6 - Usage evidence architecture

Stage 6 captures governed consumption telemetry.

Canonical **Usage Signals** may include:

- Product Port invocation events;
- query/request/call counts;
- event/stream consumption;
- view/session interactions;
- volume/throughput/latency where relevant;
- workflow/agentic consumption occurrences;
- error/degraded/fallback signals;
- usage-contract contextual identifiers;
- consumer/purpose attribution where permitted and required.

Usage Signals are principally X4 observability telemetry. Material consumption occurrences and their correlation to Product Version, Port, CIR, Access Decision and Usage Contract may also require X3 evidence.

```text
Usage Signal
   != provenance by itself
   != value
   != assurance
   != Product success
```

Privacy/minimization obligations apply to consumer telemetry through X2.

---

# 18. Stage 7 - Product signal, cost and value architecture

Stage 7 converts raw usage/operational evidence into higher-order consumption evidence without collapsing distinct meanings.

## 18.1 Canonical evidence classes

M11 preserves at least:

```text
Usage Signals        -> X4
Cost Records         -> X9
Quality/Fitness/Trust Evidence -> X5 where applicable
Evaluation/Assurance Findings  -> X6 where applicable
Outcome / Effectiveness Evidence -> P5-ABB-01
Value Signals / Value Evidence   -> P5-ABB-02
```

## 18.2 Product Signal Bundle

The existing **Product Signal Bundle** is retained as a convenience projection that can correlate/bundle these evidence classes for a Product-consumption context.

It SHALL NOT merge their meanings or become a new authority.

```text
Product Signal Bundle
   = correlated projection / bundle

Product Signal Bundle
   != universal trust score
   != proof of causality
   != assurance finding
   != value authority
```

## 18.3 Cost/value separation

M11 preserves the M05/M07 separation:

```text
cost != usage != outcome != value
```

Lower cost does not prove higher value. High usage does not prove successful outcome. A value estimate does not prove causal attribution unless the declared measurement method genuinely supports that conclusion.

---

# 19. Stage 8 - feedback, continuation and PDEP loop

Stage 8 closes the consumer lifecycle.

Canonical outputs may include:

- **SSCF Decision Context**;
- **CFR - Consumption Feedback Record**;
- continuation/stop/substitution state;
- governed evolution request;
- PDEP-entry intent for Product constitution/composition/evolution.

## 19.1 SSCF Decision Context boundary

The SSCF Decision Context records the basis/options for a consumer lifecycle choice such as continue, stop, substitute, provide feedback or enter PDEP.

It is not, by itself:

- a generic enterprise `Decision` semantic;
- GEAIRA point-of-use Authorization;
- a consequential action approval;
- Product qualification.

## 19.2 Consumption Feedback Record

CFR SHOULD preserve, where applicable:

- Product/Product Version and Port context;
- consumer/CIR context;
- explicit feedback;
- referenced usage/cost/outcome/value evidence;
- issue/satisfaction/improvement signals;
- requested action/evolution;
- evidence/provenance/currentness context.

## 19.3 PDEP handoff

A consumer may become a Product-development participant when consumption reveals a new need or intentional composition/evolution opportunity.

```text
consumption / orchestration / composition
              !=
new Product automatically

explicit Product constitution intent
+ BPS/PIN qualification
+ applicable Product-family qualification
+ PDEP
              ->
possible new/evolved Product
```

Consumed Products MAY become governed dependencies of a later PDEP design, but dependency/composition/provenance relationships remain typed and distinct.

---

# 20. Family and domain specialization

SSCF core is intentionally Product-family neutral, but Product-family and domain obligations remain applicable.

## 20.1 Data Products

Data Product consumption remains subject to applicable GEDRM/GEDRA and Data Product contract, Data authority, quality, lineage, privacy and control obligations.

## 20.2 Information Products

Information Product consumption remains subject to applicable GEARM/GEARA analytical meaning, Fitness for Use, provenance and analytical assurance obligations.

## 20.3 AI Products

AI Product consumption remains subject to applicable GEAIRM/GEAIRA/AIPS semantics, AI Product qualification, assurance/currentness, serving/integration, and where relevant Decision/Action/human-oversight obligations.

Product entitlement to an AI Product does not automatically authorize every downstream AI-mediated Decision or Action.

## 20.4 Compound Products

Compound Product identity and composition semantics remain governed by BPS/PIN and applicable Product-family specifications. SSCF may consume a Compound Product as a Product but does not infer Compound Product status merely because several Products are consumed together.

---

# 21. SSCF canonical artifact model

| Artifact | Purpose | Authority/boundary |
|---|---|---|
| **CIR - Consumption Intent Record** | Capture consumer purpose, need and use context. | Lifecycle artifact; not entitlement or Product authority. |
| **Product Resolution Set** | Record eligible/ranked candidate Products and resolution rationale. | Projection from authoritative Product/Catalog/evidence references; not Product qualification. |
| **SSCF Access Decision** | Record purpose-bound Product/Port access decision. | Access authorization only; not Data/Product ownership or consequential Decision/Action authorization. |
| **Access Descriptor** | Bind approved consumer to Product Port access conditions. | Consumer-specific operational binding; does not define Product Port. |
| **Usage Contract** | Bind consumer-specific consumption obligations to Product/Port contract. | Does not replace Product/Port authority. |
| **Consumption View / Experience Projection** | Present or mediate Product consumption for a persona/context. | Presentation/experience artifact; does not create Product semantics. |
| **Usage Signals** | Capture consumption telemetry. | X4 telemetry; not assurance/value by itself. |
| **Cost Records** | Capture economic attribution. | X9 evidence; not value. |
| **Value/Outcome Signals** | Capture modelled/measured outcome/value evidence. | P5 evidence under declared method; causality not assumed. |
| **Product Signal Bundle** | Correlate consumption evidence classes for Product interpretation. | Convenience projection; does not merge meanings/authority. |
| **SSCF Decision Context** | Support continue/stop/substitute/feedback/PDEP choice. | Consumer-lifecycle context; not universal Decision/Authorization. |
| **CFR - Consumption Feedback Record** | Preserve explicit/signal-informed feedback and requested evolution. | Feedback/evidence artifact; may trigger PDEP but does not create Productness. |

All material artifacts SHOULD be versioned or otherwise historically reconstructible where X7/X3 obligations require it.

---

# 22. Interaction obligations carried to M12

M11 does not freeze the canonical M12 inter-Plane Interaction Contract catalogue, but it establishes obligations that M12 must preserve.

Material consumption interactions must be able to carry, where applicable:

- subject/Product/Product Version identity;
- Product Port/interface identity/version;
- CIR/purpose/use context;
- consumer/actor/workload identity;
- Access Decision and entitlement context;
- Usage Contract / conditions;
- policy/control/security references;
- lifecycle/currentness state;
- correlation/provenance/evidence identifiers;
- quality/fitness/trust/assurance references;
- failure/degraded/retry semantics;
- cost attribution context;
- outcome/feedback correlation.

An M12 Interaction Contract will be architectural and MUST NOT be assumed to equal one API, protocol or message schema.

---

# 23. Canonical SSCF/CEP anti-patterns

M11 rejects the following anti-patterns:

1. **SSCF-as-Plane** - treating the lifecycle as a sixth/separate canonical HDIP Plane.
2. **Eight-stage runtime pipeline** - requiring every Product call to execute all eight lifecycle stages synchronously.
3. **Stage-per-service** - manufacturing a standalone service because a lifecycle stage exists.
4. **Marketplace-first absolutism** - requiring every consumer to start from a Marketplace UI.
5. **Intent-free browse access** - granting purpose-bound Product access without an inferred/confirmed governed intent context.
6. **Catalog-is-Registry** - collapsing Catalog projection with governed Registry responsibility.
7. **Marketplace-is-qualification** - treating listing/availability as Product qualification.
8. **Publication-equals-entitlement** - assuming a published Product is automatically accessible to a consumer.
9. **Access-equals-action-authorization** - treating Product access as consequential Decision/Action authorization.
10. **Provisioning-creates-Port** - creating Product Port identity from consumer onboarding rather than consuming an existing governed Product interface.
11. **CEP-as-Plane** - preserving historical Consumer Experience Plane as a peer canonical Plane after M06.
12. **CEP-renderer reflex** - requiring a centralized CEP Renderer service/ABB.
13. **Persona-changes-Product** - treating a persona-specific experience projection as a new Product identity.
14. **Presentation-hidden-transformation** - materially transforming/deriving outputs under the label of rendering without governed realization/constitution.
15. **Agentic-entitlement-equals-delegated-authority** - assuming an agent can take consequential actions merely because it can access a Product.
16. **Telemetry-equals-provenance** - treating usage logs alone as complete provenance/evidence.
17. **Usage-equals-value** - treating high consumption as realized value or successful outcome.
18. **Cost-equals-value** - treating economic cost as synonymous with value.
19. **Trust-score collapse** - replacing contextual quality/fitness/trust/assurance evidence with one opaque universal score.
20. **Feedback-creates-Product** - treating a creation request or Product composition as a qualified Product before BPS/PIN/family qualification and PDEP.
21. **Latest-equals-current-access** - assuming the newest Product/Port/policy/contract version is automatically current and authorized for an existing consumer.
22. **Historical rewrite** - applying later access/policy/Product state retroactively to what governed a historical consumption occurrence.

---

# 24. Canonical M11 architecture rules

**HDIP-CLA-M11-R01 - SSCF identity.** `SSCF` SHALL canonically mean `Self-Service Consumption Flow` in HDIP-CLA 0.1; historical `Self-Service Product Consumption Flow` wording MAY remain as a traceability alias.

**HDIP-CLA-M11-R02 - SSCF lifecycle status.** SSCF SHALL be treated as a logical Product-consumption lifecycle and SHALL NOT be treated as a canonical Plane, Overlay or ABB.

**HDIP-CLA-M11-R03 - Eight-stage freeze.** The canonical detailed SSCF lifecycle SHALL contain Stages 1 through 8 as defined by M11 unless changed through governed versioning.

**HDIP-CLA-M11-R04 - Non-synchronous interpretation.** SSCF stage order SHALL NOT imply that every Product runtime invocation must synchronously execute all eight stages.

**HDIP-CLA-M11-R05 - Product scope.** SSCF core SHALL govern intentional consumption of BPS/PIN-qualified Products supported by HDIP; direct non-Product capability use MAY use P4/P3 responsibilities without being misclassified as Product consumption.

**HDIP-CLA-M11-R06 - Product authority preservation.** SSCF SHALL NOT qualify Products or redefine Product-family semantics through discovery, access, consumption, popularity, usage or feedback.

**HDIP-CLA-M11-R07 - Intent-first canonical mode.** Intent-first SHALL remain the canonical SSCF entry mode and SHALL establish/confirm a CIR before governed Product access.

**HDIP-CLA-M11-R08 - Browse-first validity.** Browse-first MAY precede explicit intent declaration but SHALL establish or confirm equivalent governed CIR/use context before purpose-bound access is granted.

**HDIP-CLA-M11-R09 - CIR non-entitlement.** A CIR SHALL NOT by itself grant Product access, entitlement or consequential Decision/Action authority.

**HDIP-CLA-M11-R10 - Consumer context preservation.** Consumer identity, purpose, use context and applicable accountability context SHALL remain explicit enough for governed resolution, access and evidence.

**HDIP-CLA-M11-R11 - Typed Product discovery.** Product resolution MAY converge across Product families but SHALL preserve Product identity, Product Family/Kind, version and authoritative references.

**HDIP-CLA-M11-R12 - Catalog non-authority.** Catalog/search/index presence SHALL NOT establish Product qualification, authority, entitlement, fitness or assurance.

**HDIP-CLA-M11-R13 - Marketplace non-authority.** Marketplace listing, ranking, purchase/subscription affordance or popularity SHALL NOT establish Product qualification, access approval, trust or Fitness for Use.

**HDIP-CLA-M11-R14 - Registry/Catalog/Marketplace distinction.** SSCF SHALL preserve the M09 logical distinction among Registry, Catalog and Marketplace even when one implementation presents them together.

**HDIP-CLA-M11-R15 - Resolution explainability.** Material Product resolution/ranking SHOULD retain rationale, constraints and evidence sufficient to explain candidate selection without asserting unsupported semantic equivalence or trust.

**HDIP-CLA-M11-R16 - Fit/access distinction.** Product suitability/fit evaluation SHALL remain distinguishable from the Product-access decision.

**HDIP-CLA-M11-R17 - Purpose-bound Access Decision.** An SSCF Access Decision SHALL bind the relevant consumer, CIR/purpose, Product/Product Version/Port scope, applicable policy/entitlement context and decision conditions.

**HDIP-CLA-M11-R18 - Access/authority separation.** Product access authorization SHALL NOT be treated as Data authority, Product ownership, policy authority, delegated authority or universal Decision authority.

**HDIP-CLA-M11-R19 - Consequential authorization boundary.** An SSCF Access Decision SHALL NOT by itself authorize a consequential Decision, Digital Action, Physical Action, Tool use or other effect requiring separate point-of-use authorization.

**HDIP-CLA-M11-R20 - Access currentness.** Entitlement/access state SHALL be subject to currentness, expiry, revocation and applicable re-evaluation when Product, Port, policy, purpose, identity or Usage Contract conditions materially change.

**HDIP-CLA-M11-R21 - Provision-access-not-Port.** Stage 4 SHALL provision governed access **to** applicable Product Ports and SHALL NOT create Product Port identity merely because a consumer is onboarded.

**HDIP-CLA-M11-R22 - Access Descriptor status.** Access Descriptor SHALL be a consumer-specific operational binding and SHALL NOT redefine the Product or Product Port contract.

**HDIP-CLA-M11-R23 - Usage Contract status.** SSCF Usage Contract SHALL bind consumer-specific usage conditions to applicable Product/Port contracts and SHALL NOT replace their authoritative semantics.

**HDIP-CLA-M11-R24 - CEP canonical identity.** `CEP` SHALL canonically mean `Consumer Experience Projection` in HDIP-CLA 0.1.

**HDIP-CLA-M11-R25 - Historical CEP alias.** Historical `Consumer Experience Plane` wording MAY remain only for traceability and SHALL NOT be interpreted as a sixth/peer canonical HDIP Plane.

**HDIP-CLA-M11-R26 - CEP composition status.** CEP SHALL be treated as a consumer-facing projection/composition primarily over P2/P4/P5 plus applicable Overlays, not as an independent semantic authority.

**HDIP-CLA-M11-R27 - Persona non-authority.** Business, analytical, AI-enabled, system and agentic persona projections SHALL change experience only and SHALL NOT independently change Product identity, semantic authority or entitlement.

**HDIP-CLA-M11-R28 - CEP transformation restraint.** CEP SHALL NOT hide material derivation/transformation/composition behind presentation semantics; materially derived outputs SHALL be governed according to their actual architectural nature.

**HDIP-CLA-M11-R29 - CEP Renderer non-admission.** Historical `CEP Renderer` SHALL NOT become a canonical ABB merely because persona-specific presentation or mediation is required.

**HDIP-CLA-M11-R30 - Runtime/lifecycle separation.** Repeat Product invocation MAY reuse current governed consumer state and SHALL NOT be forced through the full SSCF lifecycle for every runtime occurrence.

**HDIP-CLA-M11-R31 - P3/P4 separation.** Product-internal Data processing, Information formation or Intelligence execution SHALL remain P3 responsibility even when invoked through P4 Product-consumption interfaces.

**HDIP-CLA-M11-R32 - Product encapsulation with evidence.** SSCF MAY encapsulate internal implementation mechanics while still exposing contractually/governance-relevant provenance, dependency, quality, currentness and assurance evidence.

**HDIP-CLA-M11-R33 - Agentic consumption non-authority.** Agentic Product consumption SHALL NOT by itself establish delegated authority or point-of-use authorization for consequential actions.

**HDIP-CLA-M11-R34 - Automated consumer equivalence.** System/automated consumers SHALL remain subject to applicable purpose, entitlement, contract, security, evidence and lifecycle obligations even where no human performs each invocation.

**HDIP-CLA-M11-R35 - Usage telemetry identity.** Usage Signals SHALL be treated principally as X4 telemetry and SHALL NOT by themselves constitute complete provenance, assurance, outcome or value evidence.

**HDIP-CLA-M11-R36 - Evidence correlation.** Material consumption occurrences SHOULD retain X3 correlation to relevant Product Version/Port, CIR, Access Decision, Usage Contract and consumer context where required for reconstruction.

**HDIP-CLA-M11-R37 - Telemetry privacy.** Usage/consumer telemetry SHALL remain subject to X2 privacy, minimization and protection obligations.

**HDIP-CLA-M11-R38 - Cost distinction.** Cost Records SHALL remain X9 economic evidence and SHALL NOT be treated as Value Signals or Product-success evidence.

**HDIP-CLA-M11-R39 - Usage/outcome/value distinction.** Usage, Outcome, Effectiveness and Value SHALL remain distinguishable even where one Product Signal Bundle correlates evidence across them.

**HDIP-CLA-M11-R40 - Value causality restraint.** Value/Outcome signals SHALL state or reference their measurement/attribution basis and SHALL NOT imply causal proof where the evidence/model does not support it.

**HDIP-CLA-M11-R41 - Quality/trust/assurance distinction.** Quality, Fitness for Use, Trust Evidence and Assurance Findings SHALL remain distinguishable during Product selection and consumption interpretation.

**HDIP-CLA-M11-R42 - Product Signal Bundle non-authority.** Product Signal Bundle MAY correlate multiple evidence classes but SHALL NOT become a universal trust/value score or independent authority.

**HDIP-CLA-M11-R43 - SSCF Decision Context boundary.** SSCF Decision Context SHALL remain a Product-consumption lifecycle artifact and SHALL NOT be treated as universal enterprise Decision semantics or point-of-use Authorization.

**HDIP-CLA-M11-R44 - Feedback evidence.** CFR and signal-informed feedback SHOULD retain Product/Version/Port, CIR and evidence context sufficient to support lifecycle interpretation without rewriting history.

**HDIP-CLA-M11-R45 - PDEP entry boundary.** SSCF MAY initiate PDEP for Product constitution, composition or evolution but PDEP entry SHALL NOT itself establish Product qualification.

**HDIP-CLA-M11-R46 - Composition non-productness.** Combined consumption/orchestration/composition of Products SHALL NOT automatically create a new Product; BPS/PIN and applicable family qualification remain required.

**HDIP-CLA-M11-R47 - Established-state reuse.** Existing consumers MAY reuse current CIR/access/contract/entitlement state where applicable, subject to X7 currentness and applicable policy/security checks.

**HDIP-CLA-M11-R48 - Policy-change re-evaluation.** Material governing policy/control change SHALL trigger applicable access, contract, control or assurance re-evaluation rather than silent continuation.

**HDIP-CLA-M11-R49 - Product-version compatibility.** A new/latest Product or Port version SHALL NOT automatically replace the governed version used by an existing consumer; compatibility/currentness/migration rules SHALL apply.

**HDIP-CLA-M11-R50 - Revocation/expiry semantics.** Revocation, expiry, suspension and conditional access state SHALL remain explicit and enforceable without rewriting the evidence of historical authorized consumption.

**HDIP-CLA-M11-R51 - Historical consumption truth.** Later Product, policy, access or assurance changes SHALL NOT retroactively alter which versions and conditions governed a historical consumption occurrence.

**HDIP-CLA-M11-R52 - Cross-Plane lifecycle.** SSCF SHALL remain a cross-Plane lifecycle spanning applicable P1/P2/P4/P5 and typed P3 runtime participation rather than being localized into one Plane.

**HDIP-CLA-M11-R53 - Overlay applicability.** X1-X9 SHALL apply to SSCF according to material context and SHALL NOT be reduced to lifecycle checkboxes or one centralized control service.

**HDIP-CLA-M11-R54 - Family specialization.** Product-family-specific SSCF obligations MAY tighten or extend core consumption rules but SHALL NOT weaken parent authority, access, evidence or historical-meaning invariants.

**HDIP-CLA-M11-R55 - AI Product downstream control.** Consumption of an AI Product SHALL preserve applicable GEAIRM/GEAIRA/AIPS serving, assurance/currentness and Decision/Action control boundaries; Product entitlement SHALL NOT substitute for consequential point-of-use authorization.

**HDIP-CLA-M11-R56 - Data/Information semantics preservation.** Data Product and Information Product consumption SHALL preserve applicable GEDRM/GEDRA and GEARM/GEARA semantics, contracts and evidence obligations respectively.

**HDIP-CLA-M11-R57 - No historical service ABB inheritance.** Product Resolution Engine, Product Discovery Orchestrator, Policy Service, Access Provisioning Service, CEP Renderer, Usage Tracking Service, FinOps Engine, Value Computation Engine, Product Observability Engine and Feedback Processor SHALL NOT gain canonical ABB status by historical use alone.

**HDIP-CLA-M11-R58 - No stage-per-service.** A canonical SSCF stage SHALL NOT imply a mandatory dedicated service/component with the same name.

**HDIP-CLA-M11-R59 - No Marketplace requirement for every path.** A Marketplace experience MAY support acquisition but SHALL NOT be mandatory for every Product-consumption path where direct governed resolution/access is valid.

**HDIP-CLA-M11-R60 - No universal trust score.** HDIP SHALL NOT reduce Product suitability, quality, Fitness for Use, trust, assurance, cost and value to one universal scalar merely to simplify consumer selection.

**HDIP-CLA-M11-R61 - Publication non-entitlement.** Successful PDEP publication/registration/exposure SHALL NOT by itself grant any consumer access to the Product.

**HDIP-CLA-M11-R62 - M12 contract deferral.** M11 SHALL establish material consumption interaction obligations but SHALL NOT freeze canonical inter-Plane Interaction Contract identities, which belong to M12.

**HDIP-CLA-M11-R63 - No new ABBs.** M11 SHALL use the M08 ABB catalogue and SHALL NOT create additional canonical ABBs solely to mirror SSCF stages, personas or artifacts.

**HDIP-CLA-M11-R64 - Canonical documentation synchronization.** The detailed SSCF specification and any interactive/experience rendering SHALL remain semantically synchronized with M11 stage identity, CEP terminology, access boundaries and evidence distinctions; presentation drift SHALL NOT acquire canonical authority.

---

# 25. What M11 deliberately does not decide

M11 does not freeze:

- the M12 canonical inter-Plane Interaction Contract catalogue;
- concrete API/protocol/message schemas;
- physical IAM/entitlement implementation;
- physical Catalog/Marketplace deployment topology;
- physical Product Port implementation technologies;
- one universal CEP UI framework;
- one universal value model or cost allocation method;
- physical evidence/observability stores;
- family-specific Decision/Action control models beyond preserving their boundaries;
- final external/adjacent-system boundary catalogue (M13);
- realization/profile patterns (M14);
- canonical reference views (M15);
- conformance modes and machine-checkability (M16).

---

# 26. M11 completion state

**HDIP-CLA M11 - COMPLETE.**

M11 establishes:

- **SSCF - Self-Service Consumption Flow** as the canonical logical HDIP Product-consumption lifecycle;
- **8 canonical SSCF stages**;
- explicit lifecycle-versus-runtime separation;
- explicit PDEP-publication-to-SSCF consumption handoff;
- **CEP - Consumer Experience Projection** as the canonical M11 expansion, retiring `Consumer Experience Plane` as a canonical topology claim;
- explicit Product-access versus consequential Decision/Action authorization separation;
- explicit Product Port, Access Descriptor and Usage Contract boundaries;
- an established-state runtime reuse model;
- explicit Usage/Cost/Outcome/Value/Trust/Assurance separation;
- an SSCF artifact model covering CIR through CFR;
- Product-family specialization boundaries for Data, Information, AI and Compound Products;
- **22 consumption/CEP anti-patterns**;
- **64 normative M11 rules**;
- **0 new canonical Planes**;
- **0 new canonical Overlays**;
- **0 new canonical ABBs**.

### Next stage

> **M12 - Canonical Inter-Plane Interaction Model**

M12 will freeze the material interaction identities/contracts among P1-P5, cross-cutting evidence/control obligations, the Product lens, Registry/Projection architecture, PDEP and SSCF while preserving the non-sequential and authority-preserving rules established through M11.
