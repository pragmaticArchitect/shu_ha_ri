---
id: hdip-cla-0.1-m12-canonical-inter-plane-interaction-model
title: HDIP-CLA 0.1 M12 - Canonical Inter-Plane Interaction Model
sidebar_label: M12 - Inter-Plane Interactions
---

# HDIP-CLA 0.1 M12 - Canonical Inter-Plane Interaction Model

**Status:** COMPLETE

## 1. Purpose

M12 defines and freezes the canonical logical interaction model between the five HDIP-CLA Planes established by M06.

M12 answers the question:

> **Which material architectural hand-offs must remain explicit between HDIP responsibilities, what must those hand-offs preserve, and how may they be realized without turning the Plane model into a mandatory runtime sequence?**

M12 is an **interaction-contract architecture** stage. It does not prescribe APIs, protocols, queues, event formats, databases, service meshes, brokers, integration products or deployment topology.

The five participating Planes remain:

```text
HDIP-P1  Governed Intent, Definition & Authority Context
HDIP-P2  Discovery, Composition & Realization
HDIP-P3  Runtime, Formation & Execution
HDIP-P4  Provision, Consumption & Integration
HDIP-P5  Outcome, Value & Evolution
```

The nine M07 Overlays qualify applicable interactions, and HDIP-FND may realize transport/runtime mechanisms, but neither Overlays nor the Foundation become an additional interaction Plane.

---

# 2. Derivation basis

M12 is constrained by the architecture frozen through M11:

- **M01** - authority and jurisdiction preservation;
- **M02** - source responsibility provenance;
- **M03** - historical construct disposition;
- **M04** - explicit contractual interoperability and evidence-by-construction principles;
- **M05** - convergence, separation locks and specialization boundaries;
- **M06** - five canonical logical Planes and non-sequential interpretation;
- **M07** - nine cross-cutting Overlays;
- **M08** - twenty-two canonical logical ABBs and principal contract-bearing boundaries;
- **M09** - Registry, projection, compilation and currentness architecture;
- **M10** - PDEP cross-Plane development/evolution lifecycle;
- **M11** - SSCF / CEP consumption and runtime lifecycle.

M08 already identified the principal contract-bearing boundaries, including P1 -> P2 governed design context, P2 -> P3 realization binding, P3 <-> P4 runtime/provision interactions and P4/P3 -> P5 evidence. M10 and M11 add lifecycle-specific interaction obligations that M12 now normalizes into one canonical model.

---

# 3. Interaction Contract definition

An **HDIP Interaction Contract** is the technology-neutral architectural agreement governing a material hand-off between HDIP logical responsibilities.

An Interaction Contract defines the meaning and obligations of the hand-off independently of whether it is realized as:

- in-process interaction;
- synchronous remote invocation;
- asynchronous message/event exchange;
- streaming interaction;
- batch exchange;
- shared governed state;
- file/artifact exchange;
- human-mediated workflow;
- federated exchange;
- embedded/local invocation;
- a combination of these.

An Interaction Contract is **not automatically**:

```text
API
message schema
event topic
queue
shared table
service
endpoint
Product Port
workflow task
integration platform
```

Those may realize part of a logical contract.

A material contract remains architecturally meaningful even when both responsibilities are implemented inside the same process or platform component.

---

# 4. Canonical Interaction Contract content model

A canonical HDIP Interaction Contract SHOULD define the following dimensions where material.

| Dimension | Architectural question |
|---|---|
| **Interaction identity** | Which canonical M12 interaction and interaction-contract version applies? |
| **Purpose** | What architectural outcome does this hand-off enable? |
| **Producer responsibility** | Which Plane / ABB is responsible for producing the hand-off? |
| **Consumer responsibility** | Which Plane / ABB consumes or acts on the hand-off? |
| **Subject identity** | Which Product, Product Version, capability, Data/Information/Intelligence subject or non-Product realization is involved? |
| **Product / Port context** | Which Product Version, Product Port or interface identity/version applies where Productization is relevant? |
| **Lifecycle context** | Which PDEP, SSCF, publication, evolution or other lifecycle occurrence is being correlated? |
| **Intent / purpose context** | Which governed intent, CIR, use purpose or expected outcome applies? |
| **Semantic references** | Which authoritative semantic identities define the meaning of material exchanged information? |
| **Authority / accountability context** | Which owner, authority, mandate, delegated responsibility or accountable actor references apply? |
| **Governance / policy context** | Which applicable policies, controls, exceptions or compliance obligations constrain the exchange? |
| **Security / privacy context** | Which identity, entitlement, purpose-limitation, confidentiality or minimization obligations apply? |
| **Registry / currentness context** | Which registered subject/version/currentness references were used? |
| **Compilation context** | Which RRG, HPD, SYNCTX, RGB, Realization Plan, Blueprint Binding or Compilation Record applies where relevant? |
| **Consumer / access context** | Which PCON, Access Decision, Access Descriptor and Usage Contract applies where relevant? |
| **Runtime occurrence context** | Which execution/processing/formation occurrence, request or result is being correlated? |
| **Content obligations** | Which information is required, conditional or optional? |
| **Identity / correlation** | Which identifiers must survive across retries, fan-out, composition and evidence correlation? |
| **Temporal semantics** | What event time, effective time, expiry, currentness, ordering or validity window applies? |
| **Interaction mode** | Which synchronous, asynchronous, stream, batch, shared-state, human-mediated or embedded modes are allowed? |
| **Delivery / processing semantics** | What acknowledgement, duplicate, replay, ordering, acceptance and completion semantics apply? |
| **Outcome semantics** | How are success, conditional acceptance, rejection, partial completion, failure or indeterminate state represented? |
| **Idempotency / side effects** | Is replay safe, and how are duplicate or unknown side effects detected/reconciled? |
| **Evidence / provenance** | Which evidence, trace, provenance and source identities must be retained? |
| **Quality / fitness / assurance** | Which quality, fitness, trust-evidence or assurance references constrain use or interpretation? |
| **Economic context** | Which cost attribution, budget, quota or consumer-accountability context applies? |
| **Compatibility / evolution** | How are contract versions, deprecation, semantic change, migration and compatibility governed? |
| **Failure / degradation** | What happens if producer, consumer, authority context, governing state, evidence or dependency is unavailable or indeterminate? |
| **Human obligations** | Where is accountable judgement, approval, notification, override or escalation required? |

The table is a conceptual contract model, not a mandatory serialized schema.

---

# 5. Canonical interaction families

M12 organizes the canonical interaction catalogue into four families.

| Family | Purpose |
|---|---|
| **F1 - Governed Context & Authority** | Carry intent, definition, authority, governing constraints, clarification and evolution feedback. |
| **F2 - Discovery, Realization & Publication** | Carry resolved realizations, publication/provisioning context, binding feedback and change/invalidations. |
| **F3 - Runtime & Provision** | Correlate consumer-facing provision with typed Data/Information/Intelligence runtime invocation and results. |
| **F4 - Consumption, Outcome & Evolution** | Carry usage/integration evidence and consumer/value/evolution feedback. |

Interaction families are organizational groupings only. They do not imply four integration buses, gateways or deployment layers.

---

# 6. Canonical inter-Plane interaction catalogue

M12 freezes **twenty-one canonical HDIP inter-Plane interaction identities**.

## 6.1 F1 - Governed Context & Authority

| ID | Canonical interaction | Direction | Architectural purpose |
|---|---|---|---|
| **HDIP-M12-INT-01** | **Governed Design / Consumption Context Provision** | P1 -> P2 | Provide governed intent, purpose, semantic references, authority/accountability context and design/use obligations for discovery, resolution, composition and realization. |
| **HDIP-M12-INT-02** | **Governing Runtime Envelope** | P1 -> P3 | Constrain typed Data processing, Information formation or Intelligence execution by applicable purpose, authority, policy, quality, lifecycle and safety context. |
| **HDIP-M12-INT-03** | **Governing Provision & Consumption Context** | P1 -> P4 | Provide purpose, identity/mandate, Product/use context and governing constraints required for exposure, access, consumption and integration. |
| **HDIP-M12-INT-04** | **Outcome / Value Objective Context** | P1 -> P5 | Provide intended outcomes, value hypotheses, evaluation context and governing interpretation boundaries for later outcome/value assessment. |
| **HDIP-M12-INT-05** | **Resolution / Validation Clarification Feedback** | P2 -> P1 | Return ambiguity, missing intent, semantic incompatibility, authority gaps or design constraints requiring P1 refinement. |
| **HDIP-M12-INT-06** | **Access / Purpose Clarification Feedback** | P4 -> P1 | Return access, entitlement, purpose or consumption-context issues requiring P1 clarification or reframing. |
| **HDIP-M12-INT-07** | **Outcome / Evolution Feedback** | P5 -> P1 | Return outcome, effectiveness, consumer feedback or value evidence that may require intent, objectives, authority context or Product design evolution. |
| **HDIP-M12-INT-08** | **Governing Revocation / Supersession** | P1 -> affected P2-P5 | Propagate material change in governing purpose, authority, mandate or constraints to affected downstream responsibilities without rewriting historical occurrences. |

## 6.2 F2 - Discovery, Realization & Publication

| ID | Canonical interaction | Direction | Architectural purpose |
|---|---|---|---|
| **HDIP-M12-INT-09** | **Realization & Runtime Binding Provision** | P2 -> P3 | Provide the governed realization/binding context required to instantiate or invoke the applicable typed P3 runtime responsibility. |
| **HDIP-M12-INT-10** | **Runtime Readiness / Binding Feedback** | P3 -> P2 | Return runtime eligibility, readiness, binding, deployment, dependency or realization-state feedback required for correction or re-binding. |
| **HDIP-M12-INT-11** | **Product / Capability Resolution Set Provision** | P2 -> P4 | Provide typed candidate Product/capability resolution results and rationale for consumer evaluation, acquisition or access processing. |
| **HDIP-M12-INT-12** | **Provisioning / Access Constraint Feedback** | P4 -> P2 | Return Product/Port availability, access, compatibility or provisioning constraints requiring substitution, re-resolution or realization change. |
| **HDIP-M12-INT-13** | **Provisionable Interface / Publication Eligibility** | P2 -> P4 | Hand off an eligible/published realization and its governed interface/Port context for exposure and consumer onboarding. |
| **HDIP-M12-INT-14** | **Realization / Change-Impact Context** | P2 -> P5 | Provide realization, dependency, compatibility and change-impact context needed to interpret outcomes and evolution consequences. |
| **HDIP-M12-INT-15** | **Evolution / Recompilation / Rebinding Request** | P5 -> P2 | Request governed reassessment, recompilation, re-binding, substitution or realization change based on outcome/evolution evidence. |
| **HDIP-M12-INT-16** | **Realization Change / Invalidation Notification** | P2 -> affected P3/P4/P5 | Propagate material realization, dependency, Blueprint, binding or interface change to affected runtime, provision and outcome responsibilities. |

## 6.3 F3 - Runtime & Provision

| ID | Canonical interaction | Direction | Architectural purpose |
|---|---|---|---|
| **HDIP-M12-INT-17** | **Runtime Invocation / Consumption Request** | P4 -> P3 | Request or invoke typed Data processing, Information formation or Intelligence execution through a governed provision/consumption boundary. |
| **HDIP-M12-INT-18** | **Runtime Result / Output Provision** | P3 -> P4 | Return typed runtime result, output, status or effect for governed exposure, consumption or downstream integration. |
| **HDIP-M12-INT-19** | **Runtime Outcome / Execution Evidence Contribution** | P3 -> P5 | Supply runtime outcome/effectiveness evidence and execution context needed for outcome/value/evolution interpretation. |

## 6.4 F4 - Consumption, Outcome & Evolution

| ID | Canonical interaction | Direction | Architectural purpose |
|---|---|---|---|
| **HDIP-M12-INT-20** | **Consumption / Usage / Integration Evidence Contribution** | P4 -> P5 | Supply governed consumption, usage, delivery and integration evidence for outcome, value and lifecycle interpretation. |
| **HDIP-M12-INT-21** | **Consumption Continuation / Substitution / Experience Feedback** | P5 -> P4 | Inform continued use, substitution, changed experience, consumer feedback or other consumption-path adjustment without directly redefining Product semantics. |

The catalogue is intentionally **not a complete directed mesh**. Absence of a direct canonical interaction does not prevent implementation communication where necessary; it means M12 has not identified a stable independent architecture contract that must exist between those Plane responsibilities.

---

# 7. Canonical interaction view

```text
                    +-------------------------+
                    |         HDIP-P1         |
                    | Intent / Definition /   |
                    | Authority Context       |
                    +-------------------------+
                     |  \        |        /
          INT-01 ----+   \02     |03     /04
                     v    v       v      v
             +-----------+   +-----------+      +-----------+
             |  HDIP-P2  |   |  HDIP-P3  |      |  HDIP-P4  |
             | Discovery |   | Runtime   |      | Provision |
             | Realize   |   | Execute   |      | Consume   |
             +-----------+   +-----------+      +-----------+
              ^   |  \          ^   |              ^   |
         05 --+   |09 \11       |17 |18       12/21|   |20
                  v     \        |   v              |   v
               runtime   \-------+------------------+ +-----------+
               binding            provision/runtime  |  HDIP-P5  |
                                                     | Outcome / |
                   P2 --14-------------------------->| Value /   |
                   P5 --15-------------------------->| Evolution |
                   P5 --07-------------------------> P1         |
                                                     +-----------+

INT-08 and INT-16 are governed change / invalidation fan-out interactions.
```

The diagram is illustrative. It does not establish a mandatory traversal sequence.

---

# 8. Interaction direction and reciprocity

Canonical direction identifies the responsibility that originates the architectural hand-off. It does **not** imply that the implementation uses one-way transport.

For example:

```text
P4 -> P3  INT-17 Runtime Invocation / Consumption Request
P3 -> P4  INT-18 Runtime Result / Output Provision
```

are two independently meaningful contracts, not merely request and response halves of one API.

Likewise:

```text
P2 -> P4  INT-11 Product / Capability Resolution Set Provision
P4 -> P2  INT-12 Provisioning / Access Constraint Feedback
```

express distinct responsibility and failure semantics.

A contract MAY be implemented through a bidirectional protocol while retaining distinct logical interaction identities.

---

# 9. Identity, causality and correlation

Material interactions must preserve enough identity to reconstruct the architectural occurrence without requiring one universal identifier for everything.

Depending on the interaction, correlation may include:

- Product / Product Version identity;
- Product Port / interface version;
- non-Product capability identity/version;
- PDEP lifecycle/version occurrence;
- SSCF/CIR occurrence;
- consumer/PCON or workload identity;
- Access Decision / Access Descriptor / Usage Contract identity;
- RRG / HPD / SYNCTX / RGB / Realization Plan / Blueprint Binding identity;
- Compilation Record identity;
- runtime execution/processing/formation occurrence identity;
- evidence/provenance correlation identity;
- policy/control/assurance reference identity;
- outcome/feedback/evolution occurrence identity.

Correlation does not imply identity collapse:

```text
Product Version != Runtime Occurrence
CIR             != Access Decision
Compilation Record != Deployment Occurrence
Usage Signal    != Outcome
Outcome         != Value
```

A causal link SHOULD be asserted only where supported by appropriate evidence. Mere temporal succession or shared correlation identifiers do not establish causation.

---

# 10. Authority and governing-context propagation

Interaction Contracts may carry authority, ownership, mandate, policy or entitlement **references**. Carrying such references does not transfer the underlying authority to the producer, consumer or transport mechanism.

M12 preserves the following distinctions:

```text
Data authority
    != Product ownership
    != policy authority
    != entitlement
    != access authorization
    != consequential Decision/Action authorization
```

Specific rules include:

- P1 may provide authority/mandate context without becoming the authority source.
- P2 may resolve/compile policies without becoming policy owner.
- P3 may enforce applicable runtime constraints without becoming policy authority.
- P4 may issue/consume Product-access decisions without granting unrelated consequential action authority.
- P5 may recommend evolution based on evidence without unilaterally changing Product/semantic authority.

A governing reference that is revoked, superseded or no longer current must trigger appropriate M12 change/currentness handling rather than silent continued use.

---

# 11. Semantic and Product boundary preservation

An Interaction Contract may carry semantic identifiers, Product metadata or Product-family information but SHALL NOT redefine them.

Protocol/schema compatibility is insufficient to prove:

- semantic equivalence;
- Product equivalence;
- capability equivalence;
- permissible composition;
- Fitness for Use;
- governance compatibility;
- assurance.

Likewise:

```text
message contains Product ID
      != message is a Product

interface exposed through P4
      != interface is Product-qualified

runtime output consumed repeatedly
      != new Product exists
```

Product identity remains governed by BPS/PIN and applicable Product-family authority.

---

# 12. Interaction modes and temporal semantics

M12 does not privilege synchronous request/response.

A canonical interaction may be realized through:

```text
synchronous
asynchronous
stream
event-driven
batch
shared governed state
human-mediated
embedded/in-process
federated
```

The chosen mode must preserve the interaction's identity, authority, currentness, outcome and evidence obligations.

Temporal semantics SHOULD distinguish where material:

- event/occurrence time;
- effective time;
- processing time;
- expiry;
- currentness evaluation time;
- validity interval;
- ordering guarantee;
- replay window;
- lifecycle state at time of use.

The newest available artifact is not automatically the governed-current artifact.

---

# 13. Delivery, duplication, retry and side effects

M12 does not assume exactly-once physical delivery.

Each material Interaction Contract SHOULD state whether:

- duplicate delivery is possible;
- replay is permitted;
- processing is idempotent;
- ordering is required;
- acknowledgement means receipt, validation, acceptance or completion;
- a retry may repeat side effects;
- duplicate/unknown side effects can be reconciled.

For a side-effecting interaction, loss of acknowledgement must not be treated automatically as proof that the operation did not occur.

An `INDETERMINATE` outcome is preferable to inventing success/failure where evidence is insufficient.

---

# 14. Canonical interaction outcome model

Interaction-specific states may vary, but material contracts SHOULD be able to distinguish the following outcome classes where applicable:

| Outcome class | Meaning |
|---|---|
| **ACCEPTED** | Accepted for processing/use under the stated contract. |
| **CONDITIONAL** | Accepted only subject to explicit conditions, gates or missing obligations. |
| **REJECTED** | Not accepted under the applicable contract/context. |
| **DEFERRED** | Not yet resolved; further input, approval, dependency or time condition is required. |
| **COMPLETED** | Contracted architectural outcome completed. |
| **PARTIAL** | Some but not all contracted outcome completed; residual obligations remain explicit. |
| **FAILED** | Attempted processing failed with a known failure state. |
| **INDETERMINATE** | Available evidence cannot establish a safe definitive outcome. |
| **CANCELLED / SUPERSEDED** | Processing or applicability ceased because it was cancelled, revoked, replaced or superseded. |

An implementation may use different local states if it preserves a clear architectural mapping.

---

# 15. Evidence and provenance propagation

Evidence is a first-class obligation of material interactions, not an after-the-fact logging exercise.

A contract may require evidence of:

- source identity/version;
- governing context;
- resolution/validation decisions;
- policy/control evaluation;
- compilation/binding;
- runtime invocation and result;
- access/provisioning decision;
- consumer/Port interaction;
- failure/degradation/retry;
- cost attribution;
- outcome/evolution feedback.

M12 preserves:

```text
telemetry != provenance
evidence presence != correctness
provenance != assurance
successful delivery != Fitness for Use
```

X3 and X4 may consume some of the same operational facts but retain distinct evidence semantics.

---

# 16. Cross-cutting Overlay obligations on Interaction Contracts

The nine M07 Overlays qualify applicable M12 interactions as follows.

| Overlay | Typical interaction-contract obligation |
|---|---|
| **X1 Governance, Policy, Control & Compliance** | policy/control applicability, exception/approval state, enforcement/result evidence |
| **X2 Security, Privacy, Identity & Entitlement** | actor/workload identity, authentication/entitlement, purpose limitation, confidentiality/minimization |
| **X3 Provenance, Evidence & Traceability** | source/version/evidence identity, lineage/correlation, historical reconstruction |
| **X4 Observability, Telemetry & Auditability** | metrics/logs/traces, operational status, audit-relevant occurrence records |
| **X5 Quality, Fitness & Trust Evidence** | quality/fitness criteria, trust evidence, suitability constraints |
| **X6 Evaluation & Assurance** | evaluation/assurance criteria, findings, indeterminate states, accountable assessment |
| **X7 Lifecycle, Version, Currentness & Change** | version/currentness, effective time, deprecation, supersession, migration/change triggers |
| **X8 Resilience, Safety, Failure & Recovery** | degraded-mode semantics, fallback/recovery, safety constraints, failure propagation |
| **X9 Economic & Cost Accountability** | cost attribution, quota/budget/consumer context, economic evidence |

An Overlay obligation may be realized by shared mechanisms, embedded behavior or several components. M12 does not create an Overlay bus or one middleware service per Overlay.

---

# 17. Contract versioning, compatibility and evolution

Interaction Contract versioning is independent from Product, Port, semantic-model, policy, runtime and deployment versioning.

A material contract change SHOULD be versioned when it changes, for example:

- required meaning/content;
- identity/correlation obligations;
- governing/authority semantics;
- outcome/failure semantics;
- side-effect/retry behavior;
- security/privacy obligations;
- currentness/evidence expectations;
- compatibility expectations.

A payload schema change does not automatically require a new Interaction Contract version if architectural meaning is unchanged; conversely, an architectural meaning change may require a new contract version even when the wire schema remains syntactically compatible.

Compatibility must therefore be assessed beyond syntax.

Historical occurrences remain governed by the contract/version/currentness state that actually applied at the occurrence time.

---

# 18. Governing revocation, invalidation and change propagation

M12 distinguishes three common change classes.

## 18.1 Governing change - INT-08

Examples:

- purpose revoked;
- mandate changed;
- policy constraint materially changed;
- Product/consumer use no longer permitted.

P1 propagates the relevant governing change to affected P2-P5 responsibilities.

## 18.2 Realization change - INT-16

Examples:

- dependency replaced;
- Blueprint Binding changed;
- interface/Port version changed;
- realization invalidated;
- runtime binding superseded.

P2 propagates affected realization/currentness consequences to P3/P4/P5.

## 18.3 Evolution request - INT-15 / INT-07

Outcome, value or consumer evidence may trigger P5 requests for recompilation/re-binding through P2 and/or intent/Product evolution through P1/PDEP.

Change propagation does not rewrite historical execution or consumption evidence.

---

# 19. PDEP mapping to canonical M12 interactions

M12 does not redefine PDEP. It provides the interaction contracts through which PDEP traverses the canonical architecture.

| PDEP concern | Principal M12 interactions |
|---|---|
| Intent / authority / semantic design | INT-01, INT-05 |
| Runtime governing constraints | INT-02 |
| Compilation -> realization binding | INT-09 |
| Runtime/deployment readiness feedback | INT-10 |
| Publication / interface eligibility | INT-13 |
| Realization/change impact | INT-14 |
| Outcome-driven Product evolution | INT-07, INT-15 |
| Revocation / supersession | INT-08, INT-16 |

For the Data PDEP Stage 0-10 specialization, Stage 8 compilation is principally within P2, Stage 9 crosses P2 -> P3 through INT-09/10, and Stage 10 establishes the provisionable publication boundary principally through INT-13.

---

# 20. SSCF / CEP mapping to canonical M12 interactions

M12 similarly preserves the eight-stage SSCF lifecycle without making each stage a runtime call.

| SSCF concern | Principal M12 interactions |
|---|---|
| Stage 1 - consumption intent | INT-01 |
| Stage 2 - resolve Product set | INT-11, with INT-05 where clarification is required |
| Stage 3 - fit/access evaluation | INT-03, INT-06, INT-12 |
| Stage 4 - purpose-bound access provisioning | INT-03, INT-13, INT-12 |
| Stage 5 - consume through CEP | INT-17, INT-18 |
| Stage 6 - capture usage | INT-20 plus applicable X3/X4 obligations |
| Stage 7 - cost/outcome/value interpretation | INT-19, INT-20, INT-04, INT-14 |
| Stage 8 - continue/stop/substitute/feedback/PDEP | INT-21, INT-07, INT-15 |

A long-lived consumer may repeatedly use INT-17/18 while reusing current governed state. It does not replay the whole SSCF lifecycle for every runtime invocation.

---

# 21. Representative interaction scenarios

## 21.1 PDEP compile, realize and publish

```text
P1 -- INT-01 --> P2
                   |
                   | compile / resolve / bind
                   v
P2 -- INT-09 --> P3
P3 -- INT-10 --> P2
P2 -- INT-13 --> P4
```

The hand-offs preserve Product/version, Compilation Record, RRG/Plan/Binding, governing context and currentness where applicable.

## 21.2 Intent-first Product consumption

```text
P1 -- INT-01 --> P2
P2 -- INT-11 --> P4
P1 -- INT-03 --> P4
P4 -- INT-17 --> P3
P3 -- INT-18 --> P4
P4 -- INT-20 --> P5
P5 -- INT-21 --> P4
```

The runtime loop may repeat without repeating discovery/access if current governed state remains valid.

## 21.3 Access denial and substitution

```text
P4 -- INT-06 --> P1   purpose/context clarification
P4 -- INT-12 --> P2   provisioning/access constraint
P2 -- INT-11 --> P4   substitute candidate set
```

Denial does not create a new Product requirement automatically; it may result in substitution, escalation or PDEP entry depending on consumer intent.

## 21.4 Outcome-driven Product evolution

```text
P3 -- INT-19 --> P5
P4 -- INT-20 --> P5
P5 -- INT-07 --> P1
P5 -- INT-15 --> P2
```

P5 provides evidence-informed evolution signals; Product constitution/authority remains governed through P1/PDEP/BPS/PIN.

## 21.5 Governing revocation during operation

```text
P1 -- INT-08 --> affected P2 / P3 / P4 / P5
```

Implementation may propagate the change through distributed mechanisms, but the logical contract must preserve effective time, affected scope, authority source, currentness and evidence.

---

# 22. Interaction anti-patterns

M12 rejects the following anti-patterns:

1. **Plane-sequence pipeline** - assuming every occurrence must traverse P1 -> P2 -> P3 -> P4 -> P5.
2. **API-equals-contract** - treating an OpenAPI/message/schema document as the complete architectural interaction contract.
3. **Contractless co-location** - removing logical hand-off semantics because producer and consumer live in one component.
4. **Shared-table coupling** - relying on undocumented shared database state without ownership/currentness/failure semantics.
5. **Universal interaction bus** - requiring all canonical interactions to pass through one central broker/gateway/platform.
6. **Overlay bus** - creating a separate X1-X9 middleware path rather than applying Overlay obligations to material interactions.
7. **Direction-equals-authority** - assuming the producer owns the semantics/authority of every reference carried in an interaction.
8. **Schema-equals-semantics** - treating syntactic compatibility as semantic or governance compatibility.
9. **Product-by-payload** - treating an exchanged artifact as a Product merely because Product metadata appears in the payload.
10. **Access-equals-action-authorization** - treating SSCF Product access approval as consequential Decision/Action authorization.
11. **Evidence-equals-assurance** - treating interaction logs or provenance as proof of correctness, fitness or assurance.
12. **Latest-equals-current** - silently using the newest available version without governed-current determination.
13. **Correlation-equals-causation** - inferring causal contribution from shared identifiers or temporal order alone.
14. **Correlation collapse** - forcing Product, request, runtime, access, evidence and outcome into one universal identifier.
15. **Retry-is-safe assumption** - retrying side-effecting interactions without explicit idempotency/reconciliation semantics.
16. **Unknown-means-failed** - reporting failure when the actual outcome is indeterminate because acknowledgement/evidence is missing.
17. **Fan-out-means-broadcast-all** - propagating revocation/change indiscriminately rather than to materially affected responsibilities.
18. **Silent compatibility drift** - changing contract meaning without versioning/reassessment because the wire format still parses.
19. **Historical rewrite** - mutating old occurrence evidence when policies, Products, contracts or realizations later change.
20. **SSCF-per-call** - replaying all eight SSCF stages for every runtime invocation regardless of current governed state.
21. **PDEP-stage-as-interaction** - creating one canonical interaction simply because a lifecycle stage exists.
22. **Interaction-per-service-call** - inflating the canonical catalogue to mirror implementation endpoints or microservices.

---

# 23. Canonical M12 architecture rules

**HDIP-CLA-M12-R01 - Interaction Contract status.** M12 Interaction Contracts SHALL be treated as logical architectural agreements governing material hand-offs between HDIP responsibilities.

**HDIP-CLA-M12-R02 - Contract technology neutrality.** A canonical Interaction Contract SHALL remain meaningful independently of API, messaging, storage, runtime, broker, vendor or deployment technology.

**HDIP-CLA-M12-R03 - Contract survives co-location.** Co-location of producer and consumer responsibilities SHALL NOT remove the logical contract where a material architectural hand-off exists.

**HDIP-CLA-M12-R04 - API non-equivalence.** An API, event schema or message format MAY realize part of a contract but SHALL NOT be treated as the full architectural contract solely because its syntax is documented.

**HDIP-CLA-M12-R05 - Shared-state discipline.** Shared-state realization MAY be used only where ownership, meaning, access, currentness, lifecycle and failure semantics remain explicit.

**HDIP-CLA-M12-R06 - No universal sequence.** The canonical interaction catalogue SHALL NOT be interpreted as a mandatory P1 -> P2 -> P3 -> P4 -> P5 runtime or project sequence.

**HDIP-CLA-M12-R07 - Interaction-family non-deployment.** F1-F4 SHALL NOT imply dedicated integration products, buses, gateways or teams.

**HDIP-CLA-M12-R08 - Interaction minimality.** A canonical interaction SHALL represent a stable material hand-off and SHALL NOT be created merely to mirror lifecycle steps, service calls or diagram arrows.

**HDIP-CLA-M12-R09 - Twenty-one interaction freeze.** HDIP-M12-INT-01 through HDIP-M12-INT-21 SHALL be the canonical HDIP-CLA 0.1 inter-Plane interaction identities unless changed through governed versioning.

**HDIP-CLA-M12-R10 - Direction semantics.** Canonical direction SHALL identify the originating architectural responsibility and SHALL NOT imply one-way physical transport.

**HDIP-CLA-M12-R11 - Reciprocity non-collapse.** Opposite-direction interactions SHALL remain independently meaningful where their responsibility, outcome or failure semantics differ.

**HDIP-CLA-M12-R12 - Fan-out scoping.** INT-08 and INT-16 fan-out SHALL target materially affected responsibilities rather than default to indiscriminate broadcast.

**HDIP-CLA-M12-R13 - No mesh requirement.** Absence of a canonical direct interaction between two Planes SHALL NOT require or prohibit implementation communication; it means no independent material M12 contract is frozen for that pair.

**HDIP-CLA-M12-R14 - ABB traceability.** Each canonical interaction SHALL be traceable to relevant M08 ABB responsibilities even where several ABBs participate.

**HDIP-CLA-M12-R15 - Lifecycle traceability.** PDEP and SSCF/CEP use of canonical interactions SHALL remain traceable to M10/M11 lifecycle responsibilities without turning stages into interaction identities.

**HDIP-CLA-M12-R16 - Subject identity preservation.** Material interactions SHALL preserve typed subject identity sufficient to distinguish Product, Product Version, Product Port, capability and non-Product realization where applicable.

**HDIP-CLA-M12-R17 - Product/version distinction.** Product identity and Product Version identity SHALL remain distinguishable in interactions where version-specific realization or consumption matters.

**HDIP-CLA-M12-R18 - Port identity preservation.** Product Port/interface identity and version SHALL remain explicit where provision/consumption depends on a specific governed interface.

**HDIP-CLA-M12-R19 - Lifecycle occurrence identity.** PDEP, SSCF and runtime occurrences SHALL remain separately correlatable where material and SHALL NOT be collapsed into Product identity.

**HDIP-CLA-M12-R20 - Consumer/access identity.** PCON/workload identity, Access Decision, Access Descriptor and Usage Contract SHALL remain distinguishable where applicable.

**HDIP-CLA-M12-R21 - Compilation correlation.** RRG, HPD, SYNCTX, RGB, Realization Plan, Blueprint Binding and Compilation Record identities SHALL remain traceable where they materially govern a realization hand-off.

**HDIP-CLA-M12-R22 - Correlation non-causality.** Shared correlation identity or temporal adjacency SHALL NOT by itself establish causation, provenance, derivation or value contribution.

**HDIP-CLA-M12-R23 - Semantic authority preservation.** Interaction payloads/references SHALL NOT redefine semantics owned by GEDRM, GEARM, GEAIRM or other applicable authorities.

**HDIP-CLA-M12-R24 - Product authority preservation.** Interaction participation, payload exchange, exposure, invocation or reuse SHALL NOT independently establish Productness or Product-family classification.

**HDIP-CLA-M12-R25 - Authority reference non-transfer.** Carrying owner/authority/mandate references SHALL NOT transfer the underlying authority to the producer, consumer, compiler, runtime or transport mechanism.

**HDIP-CLA-M12-R26 - Policy authority non-transfer.** Policy resolution, compilation, propagation or enforcement SHALL NOT make the implementing responsibility the policy authority.

**HDIP-CLA-M12-R27 - Access/Decision authorization distinction.** SSCF Product/Port access authorization SHALL NOT be treated as consequential Decision/Action authorization where separate point-of-use authorization applies.

**HDIP-CLA-M12-R28 - Compatibility beyond schema.** Schema/protocol compatibility SHALL NOT be sufficient proof of semantic, Product, governance, quality, fitness or assurance compatibility.

**HDIP-CLA-M12-R29 - Composition non-Productness.** Multi-Product/capability interaction or orchestration SHALL NOT automatically constitute a new Product.

**HDIP-CLA-M12-R30 - Direct-capability support.** Canonical interactions SHALL support governed non-Product capabilities where PDEP/Product semantics are not applicable.

**HDIP-CLA-M12-R31 - Interaction-mode neutrality.** Canonical contracts MAY be realized synchronously, asynchronously, by stream, batch, shared state, human workflow, embedded invocation or federation where obligations remain preserved.

**HDIP-CLA-M12-R32 - Temporal semantics.** Material contracts SHALL distinguish event/effective/currentness/expiry/order semantics where those distinctions affect correctness or governance.

**HDIP-CLA-M12-R33 - Latest/current distinction.** The newest available subject, contract, policy, binding or interface version SHALL NOT automatically be treated as governed-current.

**HDIP-CLA-M12-R34 - Delivery semantics explicitness.** Material interactions SHALL state acknowledgement/acceptance/completion/duplicate/replay semantics where ambiguity could alter architectural outcome.

**HDIP-CLA-M12-R35 - Idempotency explicitness.** Side-effecting or retryable interactions SHALL define whether repetition is safe and how duplicate or unknown side effects are reconciled.

**HDIP-CLA-M12-R36 - Indeterminate outcome honesty.** Where evidence is insufficient to prove success or failure, an interaction outcome SHALL remain indeterminate rather than be guessed.

**HDIP-CLA-M12-R37 - Partial outcome visibility.** Partial completion SHALL preserve residual obligations/failures rather than be reported as complete success.

**HDIP-CLA-M12-R38 - Failure/degradation semantics.** Material contracts SHALL make relevant failure, degradation, fallback and recovery behavior explicit rather than treating absence of response as one universal failure meaning.

**HDIP-CLA-M12-R39 - Evidence by construction.** Material interactions SHOULD emit/retain applicable provenance, control, observability, quality, lifecycle and outcome evidence as part of operation.

**HDIP-CLA-M12-R40 - Evidence/provenance distinction.** Telemetry, provenance, Control Evidence, quality evidence and assurance findings SHALL remain distinguishable even when correlated.

**HDIP-CLA-M12-R41 - Evidence non-assurance.** Successful interaction or evidence presence SHALL NOT by itself establish correctness, Fitness for Use, trust or assurance.

**HDIP-CLA-M12-R42 - Overlay applicability.** X1-X9 obligations SHALL apply to each interaction according to material context and SHALL NOT be waived merely because an Overlay is omitted from a simplified diagram.

**HDIP-CLA-M12-R43 - No Overlay bus.** X1-X9 cross-cutting treatment SHALL NOT imply one centralized middleware path or service through which all interactions must pass.

**HDIP-CLA-M12-R44 - Security/privacy propagation.** Identity, entitlement, confidentiality, minimization and purpose-limitation obligations SHALL be preserved across relevant interaction boundaries.

**HDIP-CLA-M12-R45 - Economic evidence distinction.** Cost/quota/budget context MAY travel with material interactions but SHALL remain distinct from Usage, Outcome and Value.

**HDIP-CLA-M12-R46 - Human judgement honesty.** Interaction outcomes requiring accountable judgement SHALL NOT be represented as machine-proven solely because rules, metadata or telemetry are available.

**HDIP-CLA-M12-R47 - Contract/version independence.** Interaction Contract version SHALL remain distinguishable from Product, Port, semantic, policy, runtime, deployment and payload-schema versions.

**HDIP-CLA-M12-R48 - Meaning-change versioning.** A material change to interaction meaning, authority, outcome, side-effect, evidence or failure semantics SHALL trigger governed contract change/versioning even where wire syntax remains compatible.

**HDIP-CLA-M12-R49 - Syntax-change restraint.** A syntactic payload change SHALL NOT automatically create a new canonical interaction identity where architectural meaning and obligations remain compatible.

**HDIP-CLA-M12-R50 - Historical contract preservation.** Later contract, policy, Product, Port or realization changes SHALL NOT rewrite which contract/version governed a historical occurrence.

**HDIP-CLA-M12-R51 - Governing change propagation.** INT-08 SHALL preserve scope, effective time, authority source and affected obligations when propagating revocation/supersession.

**HDIP-CLA-M12-R52 - Realization change propagation.** INT-16 SHALL preserve affected dependency/binding/interface/currentness context rather than silently rebinding downstream responsibilities.

**HDIP-CLA-M12-R53 - Evolution request non-authority.** INT-07 and INT-15 MAY initiate Product/design/realization evolution but SHALL NOT themselves alter semantic/Product authority or constitute a new Product Version without the applicable lifecycle/governance process.

**HDIP-CLA-M12-R54 - Reassessment on material change.** Material governing, semantic, dependency, Product, contract or realization change SHALL trigger applicable compatibility, re-resolution, reassessment, recompilation, migration or access review rather than silent adoption.

**HDIP-CLA-M12-R55 - PDEP interaction composition.** PDEP SHALL use canonical M12 interactions as cross-Plane hand-offs without turning the interaction catalogue into a mandatory linear lifecycle.

**HDIP-CLA-M12-R56 - SSCF established-state reuse.** Established governed consumer state MAY support repeated INT-17/18 runtime cycles without replaying all SSCF stages while currentness/access/contract obligations remain valid.

**HDIP-CLA-M12-R57 - CEP projection boundary.** CEP experience mediation MAY realize P4-facing aspects of M12 interactions but SHALL NOT become interaction authority or create new Product semantics through presentation.

**HDIP-CLA-M12-R58 - External-boundary deferral.** Interactions with external/adjacent systems or authorities SHALL be formalized in M13 and SHALL NOT be silently treated as internal P1-P5 contracts.

**HDIP-CLA-M12-R59 - No deployment topology.** M12 SHALL NOT prescribe centralized, federated, distributed, cloud, on-premise, edge or hybrid realization topology.

**HDIP-CLA-M12-R60 - No new structural elements.** M12 SHALL NOT introduce new canonical Planes, Overlays or ABBs merely to realize interactions.

---

# 24. What M12 deliberately does not decide

M12 does not freeze:

- external and adjacent-system boundary contracts (M13);
- centralized/federated/distributed deployment topology;
- API, event, schema or protocol formats;
- service mesh, broker, gateway or integration-product choices;
- physical retry/delivery guarantees of a particular technology;
- concrete Product Port protocols;
- external semantic-authority transport mechanisms;
- external policy/identity/provider integration;
- external AI provider/Agent/Tool boundaries;
- canonical realization/Profile patterns (M14);
- stakeholder/reference views (M15);
- final machine-checkable conformance rules and evidence sufficiency criteria (M16).

---

# 25. M12 completion state

**HDIP-CLA M12 - COMPLETE.**

M12 establishes:

- one canonical technology-neutral Interaction Contract model;
- **4 canonical interaction families**;
- **21 canonical inter-Plane interaction identities**;
- direction/reciprocity rules without imposing a universal Plane sequence;
- explicit identity/correlation and causality discipline;
- authority/Product/policy/access boundary preservation;
- interaction-mode and temporal semantics;
- delivery, replay, idempotency and side-effect semantics;
- a canonical outcome-class model;
- evidence/provenance obligations by construction;
- X1-X9 Overlay applicability to contracts without an Overlay bus;
- contract versioning/currentness/change rules;
- explicit PDEP and SSCF/CEP mappings to canonical interactions;
- five representative interaction scenarios;
- **22 interaction anti-patterns**;
- **60 normative M12 architecture rules**;
- **0 new canonical Planes**;
- **0 new canonical Overlays**;
- **0 new canonical ABBs**.

### Next stage

> **M13 - External & Adjacent-System Boundary Model**

M13 will define how the internal P1-P5 interaction model crosses boundaries to semantic authorities, Product-family authorities, enterprise systems, providers, external runtimes, consumers and other adjacent architectures without transferring jurisdiction or conformance implicitly.
