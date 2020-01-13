---
id: hdip-product-consumption-stages
title: HDIP SSCF Product Consumption Stages Spec C
sidebar_label: HDIP © Product Consumption Stages
---

# 🧭 HDIP ©: SSCF Product Consumption Stages

![Diagram](/img/hdip/hdip-ap-dp-cep-specC.png)

---

# 🧭 HDIP ©: Product Consumption Stages - Detailed Stage by Stage

This page defines the **HDIP Self-Service Consumption Flow (SSCF)** for governed **Product consumption** by a **Product Consumer (PCON)**.

The flow applies to **any HDIP-supported product type**, including:

- Data Products
- Information Products
- AI Products
- Compound Products where established by BPS / PIN
- Other BPS-qualified Product Families supported by HDIP

The core principle is:

> **PCON consumes Products through governed, purpose-bound, evidence-producing consumption paths while Product access, downstream authorization, cost, usage, outcome, value, trust and assurance remain distinct.**


## M11 Architecture Alignment

This detailed SSCF page is synchronized with **HDIP-CLA 0.1 M11**.

Canonical interpretation:

```text
SSCF = Self-Service Consumption Flow
     = logical Product-consumption lifecycle
     != Plane / Overlay / ABB

CEP  = Consumer Experience Projection
     = governed consumer-facing projection/composition
     != Consumer Experience Plane in the canonical P1-P5 model
```

The principal lifecycle mapping is:

```text
Stage 1  -> P1 governed intent/use context
Stage 2  -> P2 discovery/resolution
Stage 3  -> P2 fit context + P4 Product-access decision
Stage 4  -> P4 access provisioning / Product Port binding
Stage 5  -> P4 consumption / CEP (+ typed P3 runtime where invoked)
Stage 6  -> X4 usage telemetry + X3 evidence correlation
Stage 7  -> P5 outcome/value + X4/X5/X6/X9 evidence
Stage 8  -> P5 feedback/evolution + governed PDEP handoff
```

**Runtime note:** established consumers MAY reuse current governed CIR/access/contract/entitlement state. The eight stages are not a synchronous per-call runtime pipeline.

**Legacy diagram note:** the retained Spec C image predates M11 terminology and may display historical `Consumer Experience Plane`/service-style labels. Interpret it as an experience projection only; the Markdown specification and HDIP-CLA M11 are canonical for architecture semantics.

---

## Canonical and Secondary Consumption Modes

The stages below describe the canonical HDIP consumption mode:

> **Canonical Mode 1 — Intent First**

In this mode, the PCON first declares a consumption intent. HDIP then normalizes that intent into a **Consumption Intent Record (CIR)** and uses it to resolve suitable products.

This does **not** make the secondary mode invalid.

> **Secondary Mode 2 — Browse First**

In simpler scenarios, the PCON may begin by browsing the Product Marketplace or Product Catalog. However, before access, consumption, observability, and feedback can proceed, HDIP must still infer or confirm a CIR.

Therefore:

> **Browse-first is a convenience entry mode; intent-first is the canonical HDIP mode.**

The eight SSCF stages define a **logical consumption lifecycle**, not a requirement that every Product interaction physically execute eight synchronous runtime steps. Existing subscriptions, automated consumers, or previously established governed access MAY reuse current CIR, Access Decision, Access Descriptor, Usage Contract, entitlement and Product/Port state where those remain governed-current. Material change MAY require re-evaluation or lifecycle re-entry.

> **Diagram note:** The Spec C diagram presents nine consumer-facing interaction steps as an experience-oriented projection of the eight canonical SSCF stages. The nine interaction steps are not a second competing lifecycle.

---

## 🔴 **Stage 1 — Declare Consumption Intent**

| Row Heading | Stage 1 Definition |
|------------|------------------|
| **Stage Number** | 1 |
| **Stage Name** | Declare Consumption Intent |
| **Lifecycle Phase** | Intent Declaration |
| **Purpose** | Capture what the PCON wants to achieve, why it is needed, and the context in which consumption will occur |
| **Outcome** | A formal **Consumption Intent Record (CIR)** capturing intent, purpose, context, and consumption archetype |
| **Context** | First stage of the canonical HDIP SSCF flow; assumes **Intent-First mode** |
| **Scope** | Business or operational intent; not technical product selection, access provisioning, or implementation details |
| **Primary Inputs** | PCON intent, purpose, context, expected outcome, consumption need |
| **External Dependencies** | HDIP-P1 governed intent/use-context capabilities; consumer/persona context where applicable |
| **Core Activities** | PCON declares intent; platform interprets and normalizes intent; CIR is generated |
| **Processing Type** | Human- or agent-driven declaration with platform normalization |
| **Output Artifacts** | CIR — Consumption Intent Record |
| **State Transition** | From “Unexpressed need” → “Computable consumption intent” |
| **Governance Controls** | Intent completeness, purpose clarity, governed consumption framing; declared purpose does not itself grant Product access or downstream action authorization |
| **Validation Mechanisms** | Intent structure validation, archetype alignment, missing-context checks |
| **PCON Responsibility** | Express the consumption need clearly in business, analytical, system, AI, or agentic terms |
| **Platform Responsibility (HDIP)** | Use `HDIP-P1-ABB-01` to normalize governed intent/use context and create/version the CIR; use `HDIP-P1-ABB-03` where consumer/accountability context is material |
| **Dependency Treatment** | No products have been selected yet; dependencies are not resolved at this stage |
| **Quality Sensitivity** | Very high — weak intent leads to poor product resolution and inappropriate access decisions |
| **Failure Modes / Risks** | Vague intent, missing purpose, over-technical expression, incorrect archetype inference |
| **Observability Signals** | Intent completeness score, CIR creation events, archetype confidence |
| **Feedback Loop** | CIR may be refined before product resolution |
| **Canonical / Secondary Mode Note** | This stage describes **Canonical Mode 1: Intent First**. In **Secondary Mode 2: Browse First**, marketplace browsing may precede this stage, but HDIP must still infer or confirm a CIR before governed access is granted |

---

## 🔴 **Stage 2 — Resolve Product Set**

| Row Heading | Stage 2 Definition |
|------------|------------------|
| **Stage Number** | 2 |
| **Stage Name** | Resolve Product Set |
| **Lifecycle Phase** | Discovery & Resolution |
| **Purpose** | Translate the CIR into a ranked, explainable set of candidate products |
| **Outcome** | A **Product Resolution Set** containing candidate products, fit rationale, ranking, and resolution context |
| **Context** | Follows CIR creation; product resolution is driven by intent rather than manual search alone |
| **Scope** | Candidate product discovery, matching, ranking, and fit explanation |
| **Primary Inputs** | CIR, Product Catalog metadata, Marketplace listings, product semantics, trust metadata |
| **External Dependencies** | Product Registry authoritative references, Product Catalog projections, Product Marketplace where applicable, Product evidence/semantics |
| **Core Activities** | Query Catalog projections, resolve Product/Version identities through governed references, inspect Marketplace availability where applicable, evaluate fit against intent/evidence, construct explainable Product Resolution Set |
| **Processing Type** | Platform-driven with optional PCON exploration |
| **Output Artifacts** | Product Resolution Set |
| **State Transition** | From “Computable intent” → “Candidate product set” |
| **Governance Controls** | Product eligibility pre-checks, availability filtering, trust metadata visibility; catalog or marketplace presence does not itself establish Product qualification |
| **Validation Mechanisms** | Fit scoring, semantic matching, catalog lookup, marketplace availability checks |
| **PCON Responsibility** | Review candidate products if needed |
| **Platform Responsibility (HDIP)** | Use `HDIP-P2-ABB-01/02` to discover/resolve candidate Products while preserving typed Product identity, compatibility context, currentness and evidence references |
| **Dependency Treatment** | Product dependencies become visible as part of resolution, but are not yet provisioned |
| **Quality Sensitivity** | High — poor resolution may lead to irrelevant, unsafe, or unusable product selection |
| **Failure Modes / Risks** | Missing catalog metadata, poor semantic alignment, stale marketplace listing, over-reliance on keyword search |
| **Observability Signals** | Resolution success rate, candidate ranking confidence, no-match events |
| **Feedback Loop** | Failed or poor resolution may trigger CIR refinement or product marketplace improvement |

---

## 🔴 **Stage 3 — Evaluate Product Fit and Request Access**

| Row Heading | Stage 3 Definition |
|------------|------------------|
| **Stage Number** | 3 |
| **Stage Name** | Evaluate Product Fit and Request Access |
| **Lifecycle Phase** | Evaluation & Acquisition |
| **Purpose** | Allow the PCON to evaluate candidate products and request governed access to selected products |
| **Outcome** | An **Access Decision** and entitlement context for the selected Product set; this is a Product-access decision, not by itself authorization for a downstream consequential Decision or Action |
| **Context** | Follows product resolution; candidate products are assessed for meaning, trust, suitability, and permitted use |
| **Scope** | Product evaluation, trust review, selection, policy evaluation, entitlement decision |
| **Primary Inputs** | CIR, Product Resolution Set, Product Catalog metadata, DPP/trust signals, PCON identity/context |
| **External Dependencies** | X1 governance/policy/control, X2 identity/entitlement, Product Catalog/evidence projections, X5/X6 evidence where applicable |
| **Core Activities** | Evaluate product fit, review trust metadata, select/request products, evaluate policy, produce access decision |
| **Processing Type** | PCON-driven selection with platform-governed policy evaluation |
| **Output Artifacts** | Access Decision |
| **State Transition** | From “Candidate products” → “Approved, denied, or conditional access decision” |
| **Governance Controls** | Purpose-bound Product-access policies, entitlement rules, compliance constraints, Product-level access posture; downstream consequential action authorization remains separately governed where applicable |
| **Validation Mechanisms** | Policy checks against CIR, selected product set, PCON identity, and entitlement rules |
| **PCON Responsibility** | Select products and request access for the declared intent |
| **Platform Responsibility (HDIP)** | Coordinate fit context through P2 and produce the purpose-bound Product-access decision through `HDIP-P4-ABB-02` with applicable X1/X2/X5/X6/X7 obligations |
| **Dependency Treatment** | Selected products are treated as requested consumption targets; downstream access is not yet provisioned |
| **Quality Sensitivity** | Critical — access must reflect both the product and the declared purpose |
| **Failure Modes / Risks** | Access granted without purpose validation, entitlement mismatch, trust metadata ignored, inappropriate product use |
| **Observability Signals** | Access request events, policy decisions, denial reasons, conditional approval patterns |
| **Feedback Loop** | Denied or conditional access may trigger intent refinement, approval workflow, or Product substitution |

> **Authorization boundary:** An SSCF Access Decision governs Product / Product Port access. It does not, by itself, authorize a consequential downstream Decision, Digital Action, Physical Action, Tool use, or other effect that requires separate point-of-use authorization.

---

## 🔴 **Stage 4 — Provision Purpose-Bound Access**

| Row Heading | Stage 4 Definition |
|------------|------------------|
| **Stage Number** | 4 |
| **Stage Name** | Provision Purpose-Bound Access |
| **Lifecycle Phase** | Access Provisioning |
| **Purpose** | Materialize governed access to selected products based on the access decision, entitlements, CIR, and product resolution set |
| **Outcome** | Access Descriptor, Usage Contract, and governed access to applicable Product Ports provisioned for consumption |
| **Context** | Follows access approval or conditional approval |
| **Scope** | Access binding, entitlement materialization, Product Port access provisioning, usage contract generation |
| **Primary Inputs** | CIR, Product Resolution Set, Access Decision, Entitlements |
| **External Dependencies** | `HDIP-P4-ABB-01/02`, X2 identity/entitlement mechanisms, Product Port access infrastructure, current Product/Port contract state |
| **Core Activities** | Bind entitlements, provision access descriptors, expose governed access to applicable Product Ports, create usage contract |
| **Processing Type** | Platform-driven |
| **Output Artifacts** | Access Descriptor, Usage Contract, Product Port access binding / entitlement context |
| **State Transition** | From “Approved access decision” → “Governed access ready for consumption” |
| **Governance Controls** | Purpose-bound access, policy-shaped provisioning, entitlement enforcement, port-level controls |
| **Validation Mechanisms** | Entitlement binding checks, port exposure validation, access descriptor validation |
| **PCON Responsibility** | None beyond accepting or initiating provisioned access |
| **Platform Responsibility (HDIP)** | Bind approved consumer state to already-defined Product Ports through `HDIP-P4-ABB-01/02`, producing Access Descriptor and consumer-specific Usage Contract conditions |
| **Dependency Treatment** | Selected products are bound through governed ports; internal implementation is not exposed |
| **Quality Sensitivity** | Very high — incorrect provisioning can bypass governance or block legitimate use |
| **Failure Modes / Risks** | Incorrect entitlement binding, over-broad access, missing usage contract, broken product ports |
| **Observability Signals** | Provisioning events, port activation status, entitlement binding logs |
| **Feedback Loop** | Provisioning failures feed back to access governance and platform operations |

---

## 🔴 **Stage 5 — Consume Through CEP**

| Row Heading | Stage 5 Definition |
|------------|------------------|
| **Stage Number** | 5 |
| **Stage Name** | Consume Through CEP |
| **Lifecycle Phase** | Consumption & Experience |
| **Purpose** | Enable the PCON to consume Products through the **Consumer Experience Projection (CEP)** using governed Product Ports |
| **Outcome** | Persona-appropriate consumption views or experiences |
| **Context** | Follows access provisioning; product ports, usage contract, and access descriptor are available |
| **Scope** | Product consumption through dashboards, SQL, APIs, streams, feature pipelines, or agentic workflows |
| **Primary Inputs** | Product Ports, Access Descriptor, Usage Contract |
| **External Dependencies** | `HDIP-P4-ABB-01/02`; `HDIP-P4-ABB-03` where downstream integration is material; typed P3 runtime where the Product invocation requires it |
| **Core Activities** | Invoke governed Product Ports, select/present persona-appropriate experience projections, mediate downstream integration where applicable, generate consumption views without silently creating new Product semantics |
| **Processing Type** | PCON-initiated, platform-mediated |
| **Output Artifacts** | Consumption Views |
| **State Transition** | From “Access ready” → “Product actively consumed through CEP” |
| **Governance Controls** | Port-level controls, usage contract enforcement, access descriptor constraints |
| **Validation Mechanisms** | Port invocation checks, CEP rendering checks, access enforcement at runtime |
| **PCON Responsibility** | Consume product through the appropriate experience mode |
| **Platform Responsibility (HDIP)** | Project/mediate Product consumption through P4 while preserving Product/Port contracts, access conditions and applicable evidence; no standalone CEP Renderer ABB is implied |
| **Dependency Treatment** | Internal deployment mechanics remain encapsulated behind Product Ports; contractually/governance-relevant dependency, provenance, quality and currentness evidence MAY still be exposed |
| **Quality Sensitivity** | High — poor experience weakens adoption even when product is technically valid |
| **Failure Modes / Risks** | Broken CEP rendering, inaccessible ports, unclear views, persona mismatch |
| **Observability Signals** | View interactions, port usage, CEP rendering events |
| **Feedback Loop** | Consumption experience feeds usage tracking and later feedback |

---

## 🔴 **Stage 6 — Capture Usage Signals**

| Row Heading | Stage 6 Definition |
|------------|------------------|
| **Stage Number** | 6 |
| **Stage Name** | Capture Usage Signals |
| **Lifecycle Phase** | Usage Instrumentation |
| **Purpose** | Capture telemetry generated by governed product consumption |
| **Outcome** | Usage Signals artifact |
| **Context** | Occurs automatically as products are consumed through product ports and CEP |
| **Scope** | Port usage, CEP interaction, view interaction, contract-contextualized consumption telemetry |
| **Primary Inputs** | Product Ports, CEP interaction/Consumption Views, Usage Contract |
| **External Dependencies** | X4 observability/telemetry capability, X3 evidence/correlation where material, Product Port/CEP instrumentation |
| **Core Activities** | Capture Product Port usage and CEP interaction telemetry, correlate material consumption events to Product/Port/CIR/access/contract context where required, apply privacy/minimization obligations |
| **Processing Type** | Automated platform instrumentation |
| **Output Artifacts** | Usage Signals |
| **State Transition** | From “Consumption activity” → “Measured product usage” |
| **Governance Controls** | Usage contract context, privacy controls, telemetry minimization policies |
| **Validation Mechanisms** | Telemetry completeness checks, usage-event validation, contract-context binding |
| **PCON Responsibility** | None; usage capture is automatic |
| **Platform Responsibility (HDIP)** | Capture X4 Usage Signals and applicable X3 correlation evidence without requiring manual reporting by the PCON |
| **Dependency Treatment** | Consumption dependencies are reflected in usage signals only at governed product boundary level |
| **Quality Sensitivity** | High — inaccurate usage signals distort cost attribution, outcome/value interpretation, observability and feedback loops |
| **Failure Modes / Risks** | Missing telemetry, double counting, unbound usage events, privacy leakage |
| **Observability Signals** | Usage event count, port usage metrics, view interaction metrics |
| **Feedback Loop** | Usage signals feed cost, value, observability, and product signal bundle generation |

---

## 🔴 **Stage 7 — Compute and Observe Product Signals**

| Row Heading | Stage 7 Definition |
|------------|------------------|
| **Stage Number** | 7 |
| **Stage Name** | Compute and Observe Product Signals |
| **Lifecycle Phase** | Value Realization & Observability |
| **Purpose** | Derive and expose distinct economic, outcome/value, quality/fitness/trust and assurance evidence from governed consumption signals where applicable |
| **Outcome** | Cost Records, Value/Outcome Signals, Product Signal Bundle, Product Consumption Observability, plus typed X5/X6 evidence where applicable |
| **Context** | Follows usage signal capture; interprets consumption evidence without collapsing usage, cost, outcome, value, trust or assurance |
| **Scope** | Cost attribution, outcome/value measurement under declared models, evidence correlation, Product-consumption observability |
| **Primary Inputs** | Usage Signals, CIR, Usage Contract |
| **External Dependencies** | X9 economic/cost capability, P5 outcome/value responsibilities, X4 observability and X5/X6 evidence/assurance capabilities where applicable |
| **Core Activities** | Compute/attribute Cost Records, derive Value/Outcome Signals under explicit measurement models, correlate evidence into Product Signal Bundle, expose governed consumption observability |
| **Processing Type** | Automated platform computation with PCON-visible observability |
| **Output Artifacts** | Cost Records, Value Signals, Product Signal Bundle |
| **State Transition** | From “Measured usage” → “Observable consumption evidence, economic posture and outcome/value evidence” |
| **Governance Controls** | FinOps policies, value measurement rules, observability access policies |
| **Validation Mechanisms** | Cost-attribution checks, value/outcome-model validation, evidence provenance/correlation checks, signal-bundle completeness and applicable quality/assurance checks |
| **PCON Responsibility** | Observe usage and value posture where relevant |
| **Platform Responsibility (HDIP)** | Coordinate P5/X4/X5/X6/X9 evidence and make Product-consumption posture observable without treating one signal class as proof of another |
| **Dependency Treatment** | Product dependency effects may be reflected in aggregate cost and value signals |
| **Quality Sensitivity** | Very high — poor cost/value computation misleads product decisions and marketplace evolution |
| **Failure Modes / Risks** | Misattributed cost, weak value model, unsupported causal/value claims, missing signal aggregation, misleading observability |
| **Observability Signals** | Product Signal Bundle, ROI trends, cost trends, usage trends, value realization metrics |
| **Feedback Loop** | Signals feed PCON continuation/substitution decisions, feedback, governed Marketplace learning where applicable, and Product evolution |

> **Value-evidence boundary:** Usage, Cost, and Value Signals are evidence under their declared measurement/attribution models. They do not automatically establish causality, realized ROI, trustworthiness, or assurance.

---

## 🔴 **Stage 8 — Decision, Feedback & Creation Loop**

| Row Heading | Stage 8 Definition |
|------------|------------------|
| **Stage Number** | 8 |
| **Stage Name** | Decision, Feedback & Creation Loop |
| **Lifecycle Phase** | Decision & Evolution |
| **Purpose** | Use Product signals to determine whether to continue, stop, provide feedback, or initiate PDEP for potential new Product constitution, composition, or evolution |
| **Outcome** | Decision Context, Feedback Record, or transition into PDEP for governed Product constitution, composition, or evolution where applicable |
| **Context** | Final stage of SSCF; closes the consumption loop and enables recursive product ecosystems |
| **Scope** | Consumer decisioning, feedback capture, signal-informed improvement, optional PDEP entry |
| **Primary Inputs** | Product Signal Bundle, PCON decision, explicit feedback |
| **External Dependencies** | `HDIP-P5-ABB-01/02`, PDEP entry/re-entry, Product lifecycle capabilities, applicable X3/X7 evidence/currentness |
| **Core Activities** | Create Decision Context, process explicit feedback, generate CFR, route Product constitution/composition/evolution intent to PDEP if needed |
| **Processing Type** | PCON-driven with platform processing |
| **Output Artifacts** | Decision Context, CFR — Consumption Feedback Record |
| **State Transition** | From “Observed product value” → “Continue / stop / feedback / create” |
| **Governance Controls** | Feedback governance, product evolution controls, creation intent routing |
| **Validation Mechanisms** | Feedback validation, signal-feedback correlation, PDEP entry validation |
| **PCON Responsibility** | Decide whether to continue, stop, give feedback, or initiate a governed PDEP path for potential Product constitution/composition/evolution |
| **Platform Responsibility (HDIP)** | Correlate feedback/evidence and create governed continuation, substitution, evolution or PDEP-entry lifecycle events without creating Productness |
| **Dependency Treatment** | If PDEP entry is triggered, consumed Products MAY become governed dependencies in the new Product design; composition alone does not create a new Product identity |
| **Quality Sensitivity** | Critical — this stage drives product improvement, marketplace learning, and recursive product creation |
| **Failure Modes / Risks** | Feedback ignored, weak decision context, poor signal interpretation, broken PDEP transition |
| **Observability Signals** | Feedback volume, continuation rate, churn rate, creation triggers, composition triggers |
| **Feedback Loop** | Feeds Product evolution, governed Marketplace/Catalog learning where applicable, and PDEP |

> **Product-constitution boundary:** Composition, orchestration, or combined consumption does not automatically create a new Product. A new Product exists only where intentional Product constitution and the applicable BPS / PIN and Product-family qualification are satisfied.

> **Decision boundary:** SSCF Decision Context supports the consumer lifecycle. It is not, by itself, a GEAIRA point-of-use Authorization or a universal enterprise Decision semantic.

---

# To Summarize HDIP © SSCF

HDIP SSCF is not a simple consumption journey.

It is a governed product consumption lifecycle where:

> **Intent leads to Product resolution, Product resolution leads to governed access, governed access leads to CEP-mediated consumption, consumption produces Product signals, and Product signals drive feedback, continuation, or potential Product constitution/evolution through PDEP.**

This is what makes HDIP a recursive product ecosystem rather than a static platform.

---
# HDIP © Product Consumption Glossary

This glossary defines the key terms used in the **HDIP Self-Service Consumption Flow (SSCF)** for governed **Product consumption** by a **Product Consumer (PCON)**.

The glossary applies to consumption of any HDIP-supported Product type, including Data Products, Information Products, AI Products, Compound Products where established by BPS / PIN, and other BPS-qualified Product Families supported by HDIP.

---

## Access & Entitlements

The cross-cutting X2 responsibility for determining and enforcing who or what may access a Product, Product Port, interface or consumption capability for an applicable purpose. Identity/entitlement mechanisms may implement this responsibility, but they do not become Product/Data/policy/Decision authority. Product entitlement does not, by itself, authorize a downstream consequential Decision or Action.

---

## Access Decision

A formal artifact produced by the Policy & Entitlement Evaluation stage that records whether a PCON is allowed, denied, or conditionally allowed to access a selected product set.

The Access Decision is purpose-bound and must consider the CIR, selected Products, consumer context, policy rules, and entitlement state. It governs access to the Product / Product Port and does not, by itself, constitute GEAIRA point-of-use Authorization for a consequential Decision or Action performed using the Product.

---

## Access Descriptor

An artifact describing how a PCON may access approved product ports.

It may include endpoint references, access mode, authentication context, entitlement binding, usage constraints, and runtime access conditions.

---

## Access Provisioning

The P4 responsibility for materializing governed consumer access after an Access Decision is approved or conditionally approved. It creates/binds Access Descriptors, Usage Contracts and entitlement/access state **to already-defined Product Ports**. Consumer onboarding does not create Product Port identity.

---

## Acquire / Onboard

The PCON stage where the consumer requests access, subscribes, purchases, or otherwise initiates onboarding to a selected product or product set.

This does not itself grant access; it triggers policy and entitlement evaluation.

---

## Agentic Persona

A CEP persona projection representing an agent, workflow, autonomous process, or AI-enabled orchestration layer consuming products to perform tasks or create downstream outcomes.

Typical agentic consumption modes include workflow orchestration, Product composition, and automated task execution. Agentic consumption does not, by itself, establish Delegated Authority or point-of-use Authorization.

---

## Analytical Persona

A CEP persona projection representing analysts, data scientists, quantitative users, or analytical systems consuming products through query, exploration, or analytical tooling.

Typical analytical consumption modes include SQL, Trino, BigQuery, notebooks, and joined datasets.

---

## Browse-First Mode

A secondary HDIP consumption mode where a PCON begins by browsing the Product Marketplace or Product Catalog before explicitly declaring intent.

Browse-first mode is valid for simpler use cases, but it must still result in an inferred or confirmed CIR before governed access, consumption, observability, and feedback proceed.

---

## Business Persona

A CEP persona projection representing business consumers who experience products through business-oriented interfaces such as dashboards, KPIs, scorecards, summaries, or decision-support views.

---

## Catalog

See **Product Catalog**.

---

## CEP

See **Consumer Experience Projection**. Historical material may expand CEP as `Consumer Experience Projection`; M11 canonically expands it as `Consumer Experience Projection`.

---

## CEP Persona Projection

A persona/context-specific experience projection that changes how Product consumption is presented or mediated while preserving Product identity, Product Port contract, entitlement and semantic authority.

In the SSCF, the same product consumption flow may appear differently depending on whether the PCON is business, analytical, AI, system, or agentic.

Example overlays include:

| CEP Node | Business | Analytical | AI | System | Agentic |
|---|---|---|---|---|---|
| Consume | Dashboard | SQL / Trino / BQ | Feature pipeline | API / stream | Workflow orchestration |
| Views | Aggregated KPIs | Joined datasets | Feature datasets | JSON / events | Workflow outputs |
| Usage | Consumption patterns | Query logs | Training usage | API calls | Workflow runs |
| Value | ROI | Data utility | Model uplift | Service performance | Outcome efficiency |

> **Persona projection boundary:** entries in this table are examples of experience/interaction modes only. A joined dataset, feature dataset, workflow output or other materially derived output is not automatically a mere CEP view; where derivation changes semantics/contracts or creates a governed asset, it must be treated according to its actual architecture and Product qualification status.

---

## CEP Renderer

A historical implementation label for capabilities that present or mediate persona-appropriate Product consumption. M11 does **not** admit a canonical CEP Renderer ABB; the responsibility is realized through P4 ABBs and applicable client/platform experience mechanisms.

CEP experience capabilities use Product Ports, Access Descriptors, Usage Contracts and consumer/persona context to present or mediate Consumption Views. Material derivation/transformation is not mere rendering and must be governed according to its actual architectural nature.

---

## CFR

See **Consumption Feedback Record**.

---

## CIR

See **Consumption Intent Record**.

---

## Compound Product / Product Composition

Generic Compound Product and Product-composition semantics are governed by BPS / PIN. Composition of one or more existing Products, capabilities, assets, APIs, or other resources does **not** automatically create a new Product identity.

In HDIP, consumption may lead to a PDEP entry where a PCON becomes a producer and may intentionally constitute a new Product subject to BPS / PIN and the applicable Product-family qualification.

---

## Consume / Experience

The stage where a PCON uses a Product through the Consumer Experience Projection (CEP).

Consumption occurs through governed product ports, access descriptors, and usage contracts. It may result in dashboards, queries, APIs, streams, feature pipelines, workflow outputs, or other persona-specific experiences.

---

## Consumer Experience Projection

The canonical M11 meaning of **CEP**. It is the governed consumer-facing projection/composition through which discovery, Product access, Product Port use, consumption evidence and feedback are presented or mediated for a persona/context. Historical `Consumer Experience Plane` wording is retained only as a compatibility alias and does not create a canonical HDIP Plane.

---

## Consumption Feedback Record

A formal artifact capturing feedback from product consumption.

The CFR may include explicit PCON feedback, issues, ratings, satisfaction, adoption signals, improvement requests, or signal-informed feedback derived from observed usage, cost, and value patterns.

---

## Consumption Intent Record

A computable artifact capturing the PCON’s declared consumption intent.

The CIR records what the consumer wants, why it is needed, the context of use, relevant consumption archetype, and purpose-bound framing. It drives product resolution, access evaluation, value measurement, and feedback interpretation.

---

## Consumption Intent

The PCON’s expression of desired outcome, need, purpose, and context.

In canonical HDIP consumption, intent is declared before products are selected. This allows the platform to resolve products based on desired outcome rather than forcing consumers to search manually.

---

## Consumption Views

Consumer-facing experience projections over governed Product Ports and Product outputs. Examples may include dashboards, query experiences, API/stream interaction views, summaries or workflow views. A Consumption View does not silently authorize semantic transformation, persistence or derivation; material derivation must be governed according to its actual architectural nature.

---

## Cost Records

Artifacts capturing the economic cost of product consumption.

Cost records may include query cost, API call cost, inference cost, compute cost, storage/read cost, chargeback, showback, or cost attribution by consumer, product, purpose, or usage contract.

---

## Data Product

A BPS-qualified Product whose applicable Product-family semantics identify it as a Data Product. HDIP does not infer Data Product status merely from catalog registration, reuse, or exposure.

In the PCON flow, Data Products participate in the same intent, resolution, access, CEP, observability, and feedback lifecycle, subject to their governed Product contracts and Data-specific obligations.

---

## Information Product

A BPS-qualified Product whose applicable Information Product-family semantics identify it as an Information Product. HDIP does not infer Information Product status merely from analytical output, publication, reuse, or interface exposure.

Within SSCF, Information Products participate in the same intent, discovery, access, consumption, observability, and feedback lifecycle subject to their Product contract and applicable Information/Analytics architecture obligations.

---

## Decide Next

The PCON stage where the consumer decides whether to continue consuming, stop consuming, provide feedback, request alternatives, or initiate creation/composition of a new product.

This stage closes the consumption loop and may trigger PDEP.

---

## Decision Context

An SSCF lifecycle artifact capturing the basis/options for the PCON's next consumption decision, such as continue, stop, substitute, provide feedback, escalate or enter PDEP. It is informed by consumption evidence but is not, by itself, a GEAIRA point-of-use Authorization or universal enterprise Decision semantic.

---

## Discover Products

The SSCF activity where candidate Products are discovered/resolved against the CIR. Canonically it uses `HDIP-P2-ABB-01/02` with Product Registry references, Catalog projections, Marketplace availability where applicable, Product semantics and relevant evidence. Historical Product Resolution Engine/Discovery Orchestrator labels are implementation aliases, not canonical ABBs.

---

## Entitlement Binding

The process of associating an approved access decision with concrete access rights, roles, credentials, scopes, or runtime permissions.

Entitlement binding ensures that approved access is enforceable at product-port level.

---

## Evaluate Product Fit

The PCON stage where candidate products are assessed for relevance, meaning, trust, cost, usability, and suitability against the declared intent.

Evaluation uses the Product Catalog, Product Resolution Set, DPP/trust metadata, and product semantics.

---

## Feedback

The explicit or signal-informed response from a PCON after consuming a product.

Feedback may include issues, ratings, improvement suggestions, discontinuation reasons, satisfaction signals, or creation/composition intent.

---

## Feedback Processor

A historical implementation label for P5/X3/X7 responsibilities that correlate explicit and signal-informed feedback into a CFR and governed lifecycle events. M11 does not require one standalone Feedback Processor ABB. Feedback may inform Product evolution, substitution, governed Catalog/Marketplace learning or PDEP initiation.

---

## FinOps

The X9 economic/cost-accountability capability for measuring, attributing, optimizing and governing economic cost of Product consumption. It may support cost transparency, showback, chargeback, budgets or heavy-consumer accountability. Cost evidence remains distinct from usage, outcome and value.

---

## FinOps Engine

A historical implementation label for X9 economic/cost-accountability capability that derives Cost Records from usage evidence, contracts and governed economic rules. It is not a canonical ABB.

The FinOps Engine explains economic consumption; it does not, by itself, fully compute business value.

---

## Governed Access

Access that is purpose-bound, policy-shaped, entitlement-backed, and enforced through product ports and access descriptors.

Governed access is not generic permission to use a Product; it is permission to access a Product for a declared purpose under specific constraints. For AI-enabled or consequential downstream use, Product entitlement does not replace any separately applicable Decision/Action authorization requirement.

---

## HDIP

Holistic Data, Information and Intelligence Platform.

HDIP is an enterprise logical platform architecture for governed Data, Information, and Intelligence capabilities, including intentional Product creation/consumption where BPS / PIN and the applicable Product-family semantics establish Product status.

---

## Intent-First Mode

The canonical HDIP SSCF entry mode. The PCON first declares/communicates what they want to achieve and the applicable purpose/use context. HDIP establishes a CIR through P1 responsibilities and then resolves suitable Products through P2. The mode does not require one literal intent-interpreter service.

---

## Intent Interpreter + Normalizer

A historical implementation label for P1 governed intent/use-context capabilities that structure, validate and normalize consumer intent into a CIR. M11 does not admit a canonical Intent Interpreter ABB; implementations may use human-guided forms, rules, AI assistance or other mechanisms subject to applicable controls.

---

## Marketplace

See **Product Marketplace**.

---

## Observability

The X4 responsibility for making operational and consumption telemetry visible, queryable and monitorable. Observability supports diagnosis and evidence generation but does not by itself prove correctness, Fitness for Use, trust or assurance.

---

## Observability Engine

A historical implementation label for X4 observability/telemetry responsibilities and related consumer observability surfaces. M11 does not require one centralized Observability Engine ABB. Observability may present Usage Signals and references to other evidence classes while preserving `telemetry != provenance != trust != assurance != value`.

---

## PCON

Product Consumer. PCON is the accountable consumption role played by a human, system, agent or other governed actor when consuming a Product. The role does not by itself confer Product ownership, Data authority, delegated authority or consequential Decision/Action authority. A PCON may later participate in PDEP where an intentional new/evolved Product is proposed.

---

## PDEP

Product Development & Evolution Process. PDEP is the canonical HDIP cross-Plane lifecycle architecture for governed Product development, realization, publication and evolution. SSCF may enter or re-enter PDEP when consumption evidence creates an intentional Product-development/evolution need; entry does not itself establish Productness.

---

## PDEP Entry

The transition point from consumption into product creation or composition.

In the PCON flow, PDEP Entry is triggered when the Decision Context indicates that the PCON wants to create, compose, or evolve a Product. PDEP entry initiates governed Product design/constitution; composition alone does not create Product identity.

---

## Platform Observability

An HDIP projection of X4 operational/consumption telemetry across applicable platform responsibilities. It may correlate runtime, access, Port and consumption signals but does not become provenance or assurance authority.

---

## Policy & Entitlement Evaluation

The governed access-decision responsibility that evaluates CIR/purpose, selected Product/Port, consumer identity/context, authoritative policy references and entitlement state. It is realized principally through `HDIP-P4-ABB-02` with X1/X2 participation and produces an SSCF Access Decision. It does not make the evaluator the underlying policy authority.

---

## Policy Service

A historical/implementation capability label. Policy evaluation/distribution may realize X1 responsibilities, but the service is not the authoritative owner of the underlying enterprise, domain, legal or regulatory policy and is not a canonical M08 ABB merely by name.

---

## Product

A Product qualified under BPS / PIN and, where applicable, the relevant Product-family specification. HDIP adds platform-specific discovery, access, consumption, observability, and lifecycle realization; exposure through HDIP does not itself establish Product Intrinsic Nature or Product Family.

HDIP may support Data Products, Information Products, AI Products, Compound Products where defined by BPS / PIN, and other BPS-qualified Product Families.

---

## Product Catalog

The governed **Catalog projection** used for Product discovery/search/navigation. It references Product Registry and authoritative Product metadata/evidence but is not itself Product qualification authority. Catalog presence does not establish entitlement, Fitness for Use or Marketplace availability.

---

## Product Catalog and Product Registry

**Deprecated combined label.** M09/M11 require the two responsibilities to remain distinct even when one implementation presents them together. **Product Registry** carries governed registration facts and authoritative references; **Product Catalog** is a discovery/search/projection surface. Neither registration nor Catalog presence by itself establishes Product qualification, access approval, Fitness for Use or assurance.

---

## Product Consumption Observability

A consumer/Product-oriented view over X4 telemetry and relevant X3/X5/X6/X9 evidence. It supports interpretation of consumption behavior without collapsing usage, cost, quality, assurance, outcome or value into one signal.

---

## Product Discovery Orchestrator

A historical implementation label for governed Product discovery/resolution coordination. The canonical responsibility is represented principally by `HDIP-P2-ABB-01/02`; M11 does not require a standalone Product Discovery Orchestrator ABB.

---

## Product Marketplace

The consumer-facing acquisition/subscription/discovery experience for eligible Products. It may use Catalog and Registry information but remains distinct from both. Marketplace listing, ranking or popularity does not establish Product qualification, access approval, trust or Fitness for Use.

---

## Product Ports

Governed Product access interfaces exposed under the applicable Product/Port contract. Product Ports may include APIs, query endpoints, streams/events, files/objects, analytical interfaces, AI/agent interfaces or other family-specific mechanisms. SSCF provisions **access to** applicable Product Ports; onboarding does not create them. Internal implementation may be encapsulated while contractually/governance-relevant provenance, quality and currentness evidence remains exposable.

---

## Product Resolution Engine

A historical implementation label for responsibilities now primarily mapped to `HDIP-P2-ABB-01/02` (and validation/compilation responsibilities where needed). It maps a CIR to candidate Products but is not a canonical M08 ABB.

It uses product metadata, semantics, trust information, marketplace availability, policy context, and fit scoring to produce a Product Resolution Set.

---

## Product Resolution Set

A versioned/traceable projection of candidate Products resolved against the CIR. It may include Product/Version identifiers, Product-family references, fit rationale, ranking, compatibility/currentness notes, evidence references and constraints. Ranking does not prove semantic equivalence, trust or assurance.

---

## Product Signal Bundle

A convenience projection that correlates Product-consumption evidence such as Usage Signals, Cost Records, Value/Outcome Signals and references to Quality/Fitness/Trust or Assurance evidence where applicable. It supports observability, SSCF Decision Context, feedback and Product evolution but does not merge those evidence types or become a universal trust/value score.

---

## Product Signals

A general term for measured signals generated by product consumption.

In the SSCF, Product Signals are represented as Usage Signals, Cost Records, Value Signals, and the aggregated Product Signal Bundle.

---

## Purpose-Bound Access

Access granted for a declared and governed purpose.

In HDIP, access is not merely about who the PCON is or what product they selected. It also depends on why the product is being consumed and under what declared context.

---

## Resolve Product Set

The stage where HDIP translates the CIR into candidate products.

Resolution is intent-driven and uses catalog metadata, marketplace information, semantics, and product fit logic.

---

## Self-Service Consumption Flow

The canonical M11 expansion of **SSCF**: the HDIP logical Product-consumption lifecycle that allows PCONs to declare/confirm intent, resolve Products, evaluate fit, obtain purpose-bound access, consume through CEP, capture evidence and provide feedback or enter PDEP. Historical `Self-Service Product Consumption Flow` wording may remain as a descriptive alias.

---

## Signals

See **Product Signal Bundle**.

---

## SSCF

Self-Service Consumption Flow.

The canonical HDIP logical Product-consumption lifecycle for PCONs. It defines the journey from governed intent through Product resolution, purpose-bound access, CEP-mediated consumption, evidence/signals, feedback and potential PDEP entry; it is not a mandatory synchronous runtime pipeline.

---

## System Persona

A CEP persona projection representing a software system, API client, automation process, integration runtime, or service consuming products programmatically.

Typical system consumption modes include APIs, streams, events, and JSON payloads.

---

## Usage Contract

A consumer-specific artifact describing the allowed, expected and measurable conditions of Product consumption. It may capture permitted purpose/scope, Product/Port Version, usage mode, obligations, quotas/budgets, freshness/currentness expectations, SLA/SLO where applicable, telemetry/evidence obligations and expiry/review conditions. It binds consumer conditions to the authoritative Product/Port contract and does not replace it.

---

## Usage Signals

Artifacts capturing measured product consumption.

Usage Signals may include port usage, API calls, SQL queries, dashboard views, model calls, workflow runs, feature consumption, view interactions, and contract-contextualized telemetry.

---

## Usage Tracking

A historical implementation label for X4/P4 responsibilities that capture and normalize usage telemetry from Product Ports, CEP interactions, views and Usage Contract context. It is not a canonical ABB.

---

## Value Computation

The P5 capability for producing governed measurements, estimates or attribution outputs concerning contribution, utility, impact, uplift, efficiency or ROI under an explicit value/outcome model. It is distinct from X9 cost attribution, and its outputs do not inherently establish causal proof.

---

## Value Computation Engine

A historical implementation label for P5 value/outcome assessment capability. M11 does not require one universal value engine or model.

Implementations may derive Value Signals from Usage Signals, CIR, Usage Contract, Product context and governed value/outcome models, but the implementation does not become a universal value authority.

---

## Value Signals

Governed measurements, estimates or evidence concerning outcome contribution/value under an explicit measurement/attribution model. Value Signals remain distinct from usage, cost, quality, trust and assurance and SHALL NOT imply causal proof unless the evidence/model supports it.

---



