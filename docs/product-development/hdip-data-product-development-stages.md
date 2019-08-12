---
id: hdip-data-product-development-stages
title: HDIP Data PDEP Stages Spec C
sidebar_label: HDIP© Data PDEP Stages
---

# 🧭 HDIP©: Data PDEP Stages

![Diagram](/img/hdip/hdip-dp-pdep-specC.png)

---

# 🧭 HDIP©: Data PDEP Stages - Detailed Stage by Stage

---

## 🔴 **Stage 0 — Preconditions**

| Row Heading                             | Stage 0 Definition                                                                                                                       |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Stage Number**                        | 0                                                                                                                                        |
| **Stage Name**                          | Preconditions                                                                                                                            |
| **Lifecycle Phase**                     | Preconditions                                                                                                                            |
| **Purpose**                             | Ensure that the foundational capabilities, assets, and conditions required for data product creation exist before any intent is declared |
| **Outcome**                             | A validated environment where product creation can begin with sufficient semantic, technical, and governance readiness                   |
| **Context**                             | Occurs before any product-specific activity; establishes enterprise and domain readiness                                                 |
| **Scope**                               | Availability of ADS, canonical models, registries, platform services; not product-specific design                                        |
| **Primary Inputs**                      | Existing enterprise assets (ADS, schemas, ontologies, platform services)                                                                 |
| **External Dependencies**               | ADS Registry, Schema Registry, Ontology/EDM, Platform Infrastructure (TAP/HDIP baseline)                                                 |
| **Core Activities**                     | Validate existence of ADS, confirm canonical models (e.g. PCDM), ensure registries are populated, confirm platform availability          |
| **Processing Type**                     | Platform-assisted + governance-driven                                                                                                    |
| **Output Artifacts**                    | Readiness state (implicit), registered assets in registries                                                                              |
| **State Transition**                    | From “No context” → “Environment ready for intent declaration”                                                                           |
| **Governance Controls**                 | Enterprise standards enforcement (canonical models, registry completeness)                                                               |
| **Validation Mechanisms**               | Registry validation, schema availability checks, platform readiness checks                                                               |
| **DPRO Responsibility**                 | No product-specific responsibility; may surface missing prerequisites or readiness concerns                                                    |
| **Platform Responsibility (HDIP/DPFI)** | Maintain registries, ensure platform readiness, validate enterprise assets                                                               |
| **Dependency Treatment**                | Not applicable (no product dependencies yet)                                                                                             |
| **Quality Sensitivity**                 | Very high — poor registry quality leads to incorrect dependency resolution later                                                         |
| **Failure Modes / Risks**               | Missing ADS registration, inconsistent schemas, lack of canonical model, incomplete registries                                           |
| **Observability Signals**               | Registry completeness metrics, schema coverage, ADS availability                                                                         |
| **Feedback Loop**                       | Feeds into enterprise data governance and platform enablement teams                                                                      |

---

## 🔴 **Stage 1 — Intent Record**

| Row Heading                             | Stage 1 Definition                                                                      |
| --------------------------------------- | --------------------------------------------------------------------------------------- |
| **Stage Number**                        | 1                                                                                       |
| **Stage Name**                          | Intent Record                                                                           |
| **Lifecycle Phase**                     | Design (Intent)                                                                         |
| **Purpose**                             | Capture the business intent of the data product in a technology-agnostic manner         |
| **Outcome**                             | A formal Intent Record defining purpose, audience, and expected value                   |
| **Context**                             | First product-specific stage; defines WHAT the product should represent                 |
| **Scope**                               | Business intent, not implementation; no pipelines, no infrastructure                    |
| **Primary Inputs**                      | Business need, domain knowledge                                                         |
| **External Dependencies**               | None (conceptual stage)                                                                 |
| **Core Activities**                     | Define purpose, identify audience, articulate value, define usage expectations          |
| **Processing Type**                     | Human-driven (DPRO) with optional AI assistance                                         |
| **Output Artifacts**                    | Intent Record (FRD-level artifact)                                                      |
| **State Transition**                    | From “Idea” → “Defined product intent”                                                  |
| **Governance Controls**                 | Intent clarity and alignment with domain ownership                                      |
| **Validation Mechanisms**               | Review for clarity, completeness, and non-technical framing                             |
| **DPRO Responsibility**                 | Define intent clearly without referencing technical sources                             |
| **Platform Responsibility (HDIP/DPFI)** | Assist, validate structure, ensure no infra leakage                                     |
| **Dependency Treatment**                | Derived products: upstream Product dependencies may be declared where known; Foundational: no Product dependency need be declared at this stage, while authoritative source requirements may be resolved later |
| **Quality Sensitivity**                 | Extremely high — mis-specified intent leads to wrong product                            |
| **Failure Modes / Risks**               | Technical leakage (mentioning Kafka/PTDS), vague intent, unclear audience               |
| **Observability Signals**               | Intent completeness score, clarity metrics                                              |
| **Feedback Loop**                       | Iterative refinement with stakeholders                                                  |

---

## 🔴 **Stage 2 — Authority Confirmation**

| Row Heading                             | Stage 2 Definition                                                        |
| --------------------------------------- | ------------------------------------------------------------------------- |
| **Stage Number**                        | 2                                                                         |
| **Stage Name**                          | Authority Confirmation                                                    |
| **Lifecycle Phase**                     | Design (Governance)                                                       |
| **Purpose**                             | Confirm that the proposed Data Product is being constituted by an accountable Product owner with an appropriate mandate for the declared scope |
| **Outcome**                             | Confirmed Product ownership/accountability and mandate (DPRO), without inferring ownership of all underlying Data or authoritative sources     |
| **Context**                             | Ensures governance correctness before semantic definition                 |
| **Scope**                               | Product ownership/accountability and mandate validation; not semantic design and not underlying Data/source authority assignment                |
| **Primary Inputs**                      | Intent Record                                                             |
| **External Dependencies**               | Org structure registry, role/identity systems                             |
| **Core Activities**                     | Validate DPRO mandate to constitute, own, govern, publish, and where applicable compose the proposed Data Product within the declared scope      |
| **Processing Type**                     | Platform-assisted governance check                                        |
| **Output Artifacts**                    | Authority confirmation record                                             |
| **State Transition**                    | From “Unverified ownership” → “Authorized product definition”             |
| **Governance Controls**                 | Domain ownership rules, role validation                                   |
| **Validation Mechanisms**               | Role-based checks, domain mapping validation                              |
| **DPRO Responsibility**                 | Declare Product ownership/accountability and the mandate under which the Product is being constituted                                           |
| **Platform Responsibility (HDIP/DPFI)** | Validate the declared Product mandate against organizational/governance authority sources without inferring Data ownership or ADS status        |
| **Dependency Treatment**                | Not applicable                                                            |
| **Quality Sensitivity**                 | Very high — wrong ownership leads to invalid product                      |
| **Failure Modes / Risks**               | Misaligned ownership, cross-domain conflicts                              |
| **Observability Signals**               | Ownership validation logs                                                 |
| **Feedback Loop**                       | Escalation to governance bodies                                           |

---

## 🔴 **Stage 3 — Policy Intent**

| Row Heading                             | Stage 3 Definition                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------- |
| **Stage Number**                        | 3                                                                               |
| **Stage Name**                          | Policy Intent                                                                   |
| **Lifecycle Phase**                     | Design (Governance & Compliance)                                                |
| **Purpose**                             | Declare the governance, compliance, access, and business context that must be resolved against authoritative policy for the Data Product |
| **Outcome**                             | Policy intent describing sensitivity, access, residency, retention              |
| **Context**                             | Introduces governance constraints before semantic construction                  |
| **Scope**                               | Governance intent and applicability context; authoritative policy ownership remains with the relevant enterprise, domain, regulatory, or legal authority |
| **Primary Inputs**                      | Intent Record, domain policies                                                  |
| **External Dependencies**               | Policy Registry, regulatory frameworks                                          |
| **Core Activities**                     | Declare intended access posture, sensitivity, residency, retention, purpose, and compliance context; identify relevant authoritative policy sources |
| **Processing Type**                     | Human-driven with platform guidance                                             |
| **Output Artifacts**                    | Policy Intent Artifact                                                          |
| **State Transition**                    | From “Unconstrained product” → “Governance-aware product”                       |
| **Governance Controls**                 | Policy standards, regulatory alignment                                          |
| **Validation Mechanisms**               | Policy completeness checks, compliance validation                               |
| **DPRO Responsibility**                 | Declare governance intent and relevant business context                                                    |
| **Platform Responsibility (HDIP/DPFI)** | Resolve the declared intent/context against authoritative policies and compile applicable controls in later stages                             |
| **Dependency Treatment**                | Not applicable                                                                  |
| **Quality Sensitivity**                 | High — weak policy intent leads to governance risks                             |
| **Failure Modes / Risks**               | Missing compliance rules, over/under-restriction                                |
| **Observability Signals**               | Policy coverage metrics                                                         |
| **Feedback Loop**                       | Compliance review cycles                                                        |

---

## 🔴 **Stage 4 — Semantic Descriptor (DPROD Draft)**

| Row Heading                             | Stage 4 Definition                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Stage Number**                        | 4                                                                                                                              |
| **Stage Name**                          | Semantic Descriptor (DPROD Draft)                                                                                              |
| **Lifecycle Phase**                     | Design (Semantics)                                                                                                             |
| **Purpose**                             | Define the business meaning, structure, and conceptual model of the data product                                               |
| **Outcome**                             | A structured semantic descriptor (draft DPROD) describing entities, relationships, and meaning                                 |
| **Context**                             | First stage where intent is translated into formal semantic constructs                                                         |
| **Scope**                               | Entities, attributes, relationships, lifecycle concepts; no execution logic                                                    |
| **Primary Inputs**                      | Intent Record, domain knowledge                                                                                                |
| **External Dependencies**               | Business Dictionary, Ontology/EDM, Schema Registry                                                                             |
| **Core Activities**                     | Define entities (e.g. Payment, PaymentEvent), attributes, relationships, lifecycle states, map to canonical models (e.g. PCDM) |
| **Processing Type**                     | Human-driven with platform assistance                                                                                          |
| **Output Artifacts**                    | Draft DPROD (semantic model)                                                                                                   |
| **State Transition**                    | From “Intent” → “Structured semantic definition”                                                                               |
| **Governance Controls**                 | Alignment with enterprise ontology and canonical models                                                                        |
| **Validation Mechanisms**               | Semantic validation against ontology, naming standards, schema alignment checks                                                |
| **DPRO Responsibility**                 | Define the Product semantic proposition and structure, aligned with authoritative enterprise/domain semantic models where applicable           |
| **Platform Responsibility (HDIP/DPFI)** | Assist with ontology/model alignment and validate consistency without redefining authoritative enterprise/domain semantics                     |
| **Dependency Treatment**                | Foundational: semantics implicitly constrain ADS; Derived: semantics reference input DPRODs                                    |
| **Quality Sensitivity**                 | Critical — defines meaning of product; errors propagate to all downstream stages                                               |
| **Failure Modes / Risks**               | Misaligned semantics, duplication of concepts, unclear entity definitions                                                      |
| **Observability Signals**               | Semantic consistency metrics, ontology alignment score                                                                         |
| **Feedback Loop**                       | Iteration with domain experts and ontology governance                                                                          |

---

## 🔴 **Stage 5 — Business Assertions / Evidence Rules**

| Row Heading                             | Stage 5 Definition                                                                                   |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Stage Number**                        | 5                                                                                                    |
| **Stage Name**                          | Business Assertions / Evidence Rules                                                                 |
| **Lifecycle Phase**                     | Design (Logic & Validation)                                                                          |
| **Purpose**                             | Define business rules, validity conditions, and evidence requirements that support assessment of correctness, quality, and trust                |
| **Outcome**                             | A set of declarative business assertions; machine-decidable assertions may be compiled into executable validation/enforcement logic            |
| **Context**                             | Translates the semantic model into governed business validation conditions and evidence requirements                                          |
| **Scope**                               | Validation rules, lifecycle constraints, business conditions; no technical implementation            |
| **Primary Inputs**                      | Semantic Descriptor (Stage 4)                                                                        |
| **External Dependencies**               | Business rules repository, domain standards                                                          |
| **Core Activities**                     | Define rules (e.g. lifecycle sequencing, completeness, validity conditions), define confidence logic |
| **Processing Type**                     | Human-driven with platform assistance                                                                |
| **Output Artifacts**                    | Assertion set (Evidence Rules)                                                                       |
| **State Transition**                    | From “Defined semantics” → “Governed business validation model”                                                                                |
| **Governance Controls**                 | Rule consistency, domain validation                                                                  |
| **Validation Mechanisms**               | Logical validation, rule completeness checks                                                         |
| **DPRO Responsibility**                 | Define business assertions                                                                           |
| **Platform Responsibility (HDIP/DPFI)** | Determine which assertions are safely machine-evaluable, compile those into executable logic, and retain assessment-requiring obligations explicitly |
| **Dependency Treatment**                | Foundational: rules constrain ADS selection; Derived: rules apply across input products              |
| **Quality Sensitivity**                 | Extremely high — materially affects validation quality, evidence strength, and downstream trust assessments                                   |
| **Failure Modes / Risks**               | Missing rules, contradictory assertions, weak validation                                             |
| **Observability Signals**               | Rule coverage metrics, validation success/failure rates (post-deployment)                            |
| **Feedback Loop**                       | Continuous refinement based on runtime signals                                                       |

---

## 🔴 **Stage 6 — Usage Contract**

| Row Heading                             | Stage 6 Definition                                                                                             |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Stage Number**                        | 6                                                                                                              |
| **Stage Name**                          | Usage Contract                                                                                                 |
| **Lifecycle Phase**                     | Design (Consumption)                                                                                           |
| **Purpose**                             | Define how the data product will be consumed, including expectations for performance, freshness, and usability |
| **Outcome**                             | A usage contract specifying consumption modes, SLAs, and experience expectations                               |
| **Context**                             | Bridges product design with consumer needs                                                                     |
| **Scope**                               | Consumption modes, latency expectations, access patterns, explainability                                       |
| **Primary Inputs**                      | Intent Record, Semantic Descriptor                                                                             |
| **External Dependencies**               | Consumer personas, usage archetypes (CS/PU/MO/CT framework)                                                    |
| **Core Activities**                     | Define real-time vs batch needs, query patterns, API expectations, explainability requirements                 |
| **Processing Type**                     | Human-driven with platform guidance                                                                            |
| **Output Artifacts**                    | Usage Contract                                                                                                 |
| **State Transition**                    | From “Defined product” → “Consumer-ready specification”                                                        |
| **Governance Controls**                 | SLA policies, access expectations                                                                              |
| **Validation Mechanisms**               | Contract completeness checks, alignment with platform capabilities                                             |
| **DPRO Responsibility**                 | Define usage expectations                                                                                      |
| **Platform Responsibility (HDIP/DPFI)** | Validate feasibility, map to capabilities                                                                      |
| **Dependency Treatment**                | Indirect — influences execution plan but not dependency type                                                   |
| **Quality Sensitivity**                 | High — impacts performance, usability, and adoption                                                            |
| **Failure Modes / Risks**               | Unrealistic SLAs, unclear consumption patterns                                                                 |
| **Observability Signals**               | Usage metrics, latency, consumer satisfaction                                                                  |
| **Feedback Loop**                       | Consumer feedback, COVP signals                                                                                |

---

## 🔴 **Stage 7 — Product Preview (Abstract)**

| Row Heading                             | Stage 7 Definition                                                                  |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| **Stage Number**                        | 7                                                                                   |
| **Stage Name**                          | Product Preview (Abstract)                                                          |
| **Lifecycle Phase**                     | Design (Validation & Review)                                                        |
| **Purpose**                             | Provide a non-technical preview of the product for validation before compilation    |
| **Outcome**                             | A conceptual representation of the product as it will appear to consumers           |
| **Context**                             | Final checkpoint before entering automated compilation                              |
| **Scope**                               | Sample views, lifecycle representations, semantic correctness; no execution details |
| **Primary Inputs**                      | Semantic Descriptor, Assertions, Usage Contract                                     |
| **External Dependencies**               | Visualization tools, preview engines                                                |
| **Core Activities**                     | Generate sample outputs, visualize lifecycle, validate semantics with stakeholders  |
| **Processing Type**                     | Platform-generated with human validation                                            |
| **Output Artifacts**                    | Product preview (mock outputs, sample views)                                        |
| **State Transition**                    | From “Designed product” → “Validated product design”                                |
| **Governance Controls**                 | Semantic validation, stakeholder approval                                           |
| **Validation Mechanisms**               | Review sessions, semantic correctness checks                                        |
| **DPRO Responsibility**                 | Review and approve preview                                                          |
| **Platform Responsibility (HDIP/DPFI)** | Generate preview from declarative artifacts                                         |
| **Dependency Treatment**                | Not yet resolved; preview is independent of actual binding                          |
| **Quality Sensitivity**                 | High — major pre-compilation checkpoint for detecting semantic and design issues                      |
| **Failure Modes / Risks**               | Misinterpretation of semantics, incorrect preview                                   |
| **Observability Signals**               | Approval status, review feedback                                                    |
| **Feedback Loop**                       | Iteration back to Stages 4–6                                                        |

---

## 🔴 **Stage 8 — Compilation (DPFI Core)** 

| Row Heading                             | Stage 8 Definition                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stage Number**                        | 8                                                                                                                                                                                                                                                                                                                                        |
| **Stage Name**                          | Compilation                                                                                                                                                                                                                                                                                                                              |
| **Lifecycle Phase**                     | Compilation                                                                                                                                                                                                                                                                                                                              |
| **Purpose**                             | Transform declarative Product intent, semantics, governance, assertions, and usage expectations into a sufficiently resolved, executable, context-aware Product design for the selected realization profile                                                                                                                             |
| **Outcome**                             | A **Resolved Product Graph**, **Synthetic Context (SYNCTX)** (if applicable), **HDIP Product Descriptor (HPD)**, Logical Execution Plan, and Selected Blueprint                                                                                                                                                                          |
| **Context**                             | First fully automated stage; converts all declarative artifacts into computable graph structures and execution-ready designs                                                                                                                                                                                                             |
| **Scope**                               | Dependency resolution, semantic graph construction, SYNCTX inference, policy compilation, execution planning, HPD generation, blueprint selection                                                                                                                                                                                        |
| **Primary Inputs**                      | Intent Record, Semantic Descriptor (DPROD draft), Business Assertions, Policy Intent, Usage Contract                                                                                                                                                                                                                                     |
| **External Dependencies**               | ADS Registry, Data Product Catalog, Capability Registry, Policy Registry, Blueprint Library, Ontology / EDM                                                                                                                                                                                                                              |
| **Core Activities**                     | 1. Resolve and classify applicable dependencies (ADS, upstream Products, governance/provenance dependencies)<br/>2. Construct semantic graph<br/>3. Compile safely machine-evaluable assertions and retain assessment obligations<br/>4. Resolve authoritative policies and compile/bind applicable governance controls<br/>5. **Infer Synthetic Context (SYNCTX) where required**<br/>6. Generate Logical Execution Plan<br/>7. Select appropriate blueprint<br/>8. **Generate HDIP Product Descriptor (HPD)** |
| **Processing Type**                     | Fully automated (DPFI-driven)                                                                                                                                                                                                                                                                                                            |
| **Output Artifacts**                    | • Resolved Product Graph<br/>• Dependency Graph<br/>• Logical Execution Plan<br/>• Selected Blueprint<br/>• **Synthetic Context (SYNCTX)** (conditional)<br/>• **HDIP Product Descriptor (HPD)**                                                                                                                                         |
| **State Transition**                    | From “Declarative Product Definition” → “Executable & Context-Aware Product Design”                                                                                                                                                                                                                                                      |
| **Governance Controls**                 | Policy resolution/control binding, semantic validation, dependency validation, synthetic-boundary validation                                                                                                                                                                                                                              |
| **Validation Mechanisms**               | Schema compatibility checks, assertion validation, policy consistency checks, dependency resolution validation, **SYNCTX consistency validation (joinability, relationship integrity)**                                                                                                                                                  |
| **DPRO Responsibility**                 | No routine compilation action; review or accountable intervention where required by unresolved ambiguity or governance gates                                                                                                                                                                                                             |
| **Platform Responsibility (HDIP/DPFI)** | Perform full compilation, resolve dependencies, construct semantic and relational graphs, infer SYNCTX, generate HPD, produce execution-ready design                                                                                                                                                                                     |
| **Dependency Treatment**                | Dependencies are resolved and classified by role. Applicable dependencies may become execution inputs, governance/provenance references, semantic relationships, or SYNCTX participants; no dependency role is inferred solely from dependency existence                                                                                                                                                |
| **Quality Sensitivity**                 | Critical — materially affects Product semantics, dependency binding, execution design, governance realization, and any synthetic behavior                                                                                                                                                                                                 |
| **Failure Modes / Risks**               | Incorrect dependency resolution, semantic mismatch, incorrect SYNCTX inference, wrong blueprint selection, incomplete policy compilation                                                                                                                                                                                                 |
| **Observability Signals**               | Compilation logs, dependency resolution trace, SYNCTX inference trace, blueprint selection rationale, validation results                                                                                                                                                                                                                 |
| **Feedback Loop**                       | Feeds back to Stage 1–7 for correction (intent, semantics, assertions, policy, usage)                                                                                                                                                                                                                                                    |

---

## 🔴 **Stage 9 — Deployment (DPDS Generation & Execution)**

| Row Heading                             | Stage 9 Definition                                                                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Stage Number**                        | 9                                                                                                                                                                              |
| **Stage Name**                          | Deployment                                                                                                                                                                     |
| **Lifecycle Phase**                     | Deployment                                                                                                                                                                     |
| **Purpose**                             | Materialize the compiled product design into a running, provisioned, and operational data product                                                                              |
| **Outcome**                             | A deployed data product with active pipelines, storage, and output ports                                                                                                       |
| **Context**                             | Executes the blueprint and execution plan generated in Stage 8                                                                                                                 |
| **Scope**                               | DPDS generation, infrastructure provisioning, pipeline execution, output port creation, observability setup                                                                    |
| **Primary Inputs**                      | Resolved Product Graph, Execution Plan, Selected Blueprint                                                                                                                     |
| **External Dependencies**               | Approved compute, storage, processing, streaming, runtime, security, and hosting environments                                                                                                                |
| **Core Activities**                     | Generate DPDS, provision resources (schemas, compute, storage), connect inputs, execute transformations, enforce assertions, materialize output ports, configure observability |
| **Processing Type**                     | Platform-driven and automated by default, subject to applicable promotion, governance, and operational gates                                                                                                |
| **Output Artifacts**                    | Deployed pipelines, provisioned infrastructure, active output ports, observability configuration                                                                               |
| **State Transition**                    | From “Executable Design” → “Running Data Product”                                                                                                                              |
| **Governance Controls**                 | Runtime policy enforcement, access control enforcement                                                                                                                         |
| **Validation Mechanisms**               | Deployment success checks, runtime validation, pipeline health checks                                                                                                          |
| **DPRO Responsibility**                 | No routine deployment action; accountable review/approval where required by Product governance or promotion gates                                                                                           |
| **Platform Responsibility (HDIP/DPFI)** | Execute deployment, provision infrastructure, ensure correct execution                                                                                                         |
| **Dependency Treatment**                | Dependencies are **bound and connected** (ADS streams or product ports)                                                                                                        |
| **Quality Sensitivity**                 | Fully dependent on Stage 8; faithfully executes whatever was compiled                                                                                                          |
| **Failure Modes / Risks**               | Deployment failures, misconfigured pipelines, incorrect bindings, runtime errors                                                                                               |
| **Observability Signals**               | Deployment logs, pipeline metrics, latency, error rates, resource utilization                                                                                                  |
| **Feedback Loop**                       | Feeds back to Stage 8 (blueprint/execution correction)                                                                                                                         |

---

## 🔴 **Stage 10 — DPROD Finalization & Registration**

| Row Heading                             | Stage 10 Definition                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Stage Number**                        | 10                                                                                              |
| **Stage Name**                          | DPROD Finalization & Registration                                                               |
| **Lifecycle Phase**                     | Publication                                                                                     |
| **Purpose**                             | Finalize and publish the already-constituted Data Product Version as a discoverable, governed, and consumable HDIP Product realization          |
| **Outcome**                             | A published/registered Data Product Version with final DPROD, DPP, lineage/provenance, and accessible output ports                            |
| **Context**                             | Final publication/registration stage in which the Product Version becomes discoverable within the HDIP ecosystem; registration does not create Productness |
| **Scope**                               | DPROD finalization, catalog registration, lineage capture, DPP generation, marketplace exposure |
| **Primary Inputs**                      | Deployed product (from Stage 9), final semantic and policy artifacts                            |
| **External Dependencies**               | Data Catalog, Marketplace, Lineage Service, Knowledge Graph, DPP framework                      |
| **Core Activities**                     | Finalize DPROD, register product, capture lineage, generate DPP, enable discoverability         |
| **Processing Type**                     | Fully automated with optional governance oversight                                              |
| **Output Artifacts**                    | Final DPROD, DPP (Digital Product Passport), catalog entry, lineage graph                       |
| **State Transition**                    | From “Deployed Product realization” → “Published / registered / discoverable Product Version”                                                |
| **Governance Controls**                 | Product registration standards, compliance validation, trust signals                            |
| **Validation Mechanisms**               | Registration checks, lineage validation, DPP completeness checks                                |
| **DPRO Responsibility**                 | Review and accept published product                                                             |
| **Platform Responsibility (HDIP/DPFI)** | Finalize artifacts, register product, expose in marketplace                                     |
| **Dependency Treatment**                | Operational dependencies remain active where required and are additionally registered/exposed for lineage, provenance, impact analysis, currentness, and lifecycle management |
| **Quality Sensitivity**                 | Dependent on Stage 9 realization quality and the completeness/currentness of publication, lineage, provenance, and trust metadata             |
| **Failure Modes / Risks**               | Incorrect lineage, incomplete metadata, broken discoverability                                  |
| **Observability Signals**               | Product usage metrics, access patterns, lineage queries, consumer feedback                      |
| **Feedback Loop**                       | Feeds into continuous assurance (post-publication evolution)                                    |

### Product evolution and PDEP re-entry

For an existing Product Version, PDEP evolution SHOULD re-enter at the earliest stage materially affected by the proposed change rather than automatically restarting the whole lifecycle. For example, a semantic change may require re-entry at Stage 4 or earlier, a governance-policy change may re-enter through Stage 3 and applicable compilation, a usage-contract change may re-enter at Stage 6, and an implementation-only change may begin at Stage 8 or Stage 9 where upstream intent/semantics remain valid. Re-entry remains subject to applicable currentness, impact-analysis, governance, and promotion controls.

Evolution/re-entry MUST preserve historical Product-Version truth: later changes may alter future realization/currentness without rewriting the semantics, dependencies, controls, or evidence that applied to an earlier Product Version.

---

# HDIP SSPD PDEP Spec C Glossary

This glossary defines the key terms used in the **HDIP Self-Service Product Development / Product Development and Evolution Process (SSPD / PDEP) Spec C** flow for **Data Products**.

Spec C is the lifecycle-accurate view of how a **Data Product Owner (DPRO)** declares business-native intent and how the HDIP platform validates, compiles, governs, deploys, registers, observes, and evolves the resulting Data Product.

This glossary uses HDIP-specific terms for the Data PDEP realization. Generic Product semantics remain governed by BPS/PIN; generic Data semantic and architecture authority remains with GEDRM/GEDRA. HDIP terms such as ADS, DPROD, DPDS, HPD, DPFI, and Unified Governance Bundle specialize or realize those authorities rather than redefining them.

---

## Access & Entitlements

The enterprise service responsible for managing who or what may access a Data Product, product output, governed runtime view, or related product capability.

In the Spec C flow, Access & Entitlements is used by the Governance Compiler to bind policy intent to executable access controls such as RBAC and ABAC.

---

## Assertion Compiler

The HDIP platform service that validates business assertions and compiles the safely machine-evaluable subset into deterministic, executable, tool-agnostic validation and enforcement logic.

It checks that assertions are complete, non-contradictory, semantically bound, and compatible with the Unified Governance Bundle, while retaining assessment-requiring assertions as explicit governed obligations.

---

## Assertion Set

A versioned artifact containing the consolidated business assertions for the Data Product.

The Assertion Set captures business rules, precedence, missing-data behavior, validity conditions, and evidence expectations. Machine-evaluable assertions may be compiled into executable validation/enforcement logic; assessment-requiring assertions remain explicit governed obligations.

---

## Assertion Validation Report

An artifact produced by the Assertion Compiler that records whether business assertions are deterministic, complete, logically consistent, and compatible with product semantics and governance constraints.

---

## Authority Context

The DPRO-declared context describing the mandate, role-hat, and legitimacy under which the DPRO is acting.

Authority Context helps the platform determine whether the DPRO has the right to create, publish, or compose the Data Product.

---

## Authority Decision

A platform-generated artifact recording the result of authority validation.

It may contain PASS, CONDITIONAL, or FAIL evidence and can enrich the Intent Record with mandate and composability evidence.

---

## Authority Validator

The HDIP platform service that validates whether the DPRO has the appropriate mandate to define and publish the Data Product.

It may also validate input product composability through IPCC-style checks.

---

## Blueprint Binding

A versioned artifact that records the selected blueprint and runtime binding choices for the Data Product.

It may include patterns such as RBB, RCM, RERP, and RMP, and captures how the compiled product plan is bound to platform capabilities, environments, cost constraints, and operational posture.

---

## Blueprint Resolver

The HDIP platform service that selects an appropriate implementation blueprint for the Data Product.

In this Spec C flow, it resolves a daily-batch optimized blueprint using the Compilation Pack, governance constraints, usage contract, exposure decision, capability registry, environment registry, and cost model.

---

## Business Assertions

Business-authored rules that define validity conditions, expected behavior, and evidence requirements relevant to correctness, quality, and trust assessment for the Data Product.

Business assertions are expressed by the DPRO in business terms. The platform compiles only the safely machine-evaluable subset into deterministic validation/enforcement logic and preserves assessment-requiring obligations explicitly.

---

## Business Dictionary

An enterprise service containing approved business terms, definitions, synonyms, and domain vocabulary.

In the flow, the Semantic Grounding service uses the Business Dictionary to align Data Product meaning with shared enterprise language.

---

## Capability Registry

An enterprise registry of platform capabilities available for product development and deployment.

It is used during preconditions checking and blueprint resolution to determine whether the platform has the capabilities needed to compile, provision, and operate the Data Product.

---

## Catalog

See **Data Catalog**.

---

## Compilation Pack

A versioned artifact generated by the Compilation Pack Generator.

It bundles the logical execution and enforcement plans required to translate declarative product design into a feasible platform-realizable product. In this flow, it may include LEG, GEP, DQEP, DCEP, RVS, OSP, and EAP.

---

## Compilation Pack Generator

The HDIP platform service that compiles the full declarative product definition into a platform-realizable package.

It consumes the Intent Record, Authority Decision, Unified Governance Bundle, Semantic Descriptor, Assertion Set, Usage Contract, and Exposure Decision to produce the Compilation Pack.

---

## Compile Preview

A DPRO-facing review step that shows what the platform intends to build before deployment.

The preview remains business-native and does not expose tools, pipelines, infrastructure, or engineering implementation detail.

---

## Cost Model / FinOps

The enterprise capability used to evaluate and optimize the economic feasibility of product deployment and operation.

In the flow, the Blueprint Resolver uses the Cost Model / FinOps service to assess cost feasibility for the selected implementation pattern.

---

## Daily Batch Posture

The DPRO-declared or platform-recognized operational posture for the Data Product.

In this flow, it indicates that the Data Product is optimized for daily batch operation, including evidence-ledger behavior, schedules, freshness expectations, and replay posture.

---

## Data Catalog

The enterprise discovery and registration service for Data Products.

It stores product metadata, semantic descriptors, governance posture, trust information, discoverability information, and registration state.

---

## Data Controls

See **DC Services**.

---

## Data Product

A BPS-qualified Product whose applicable Product-family semantics identify it as a Data Product. Within HDIP PDEP, the Data Product is realized through HDIP-specific semantic, governance, deployment, publication, observability, and lifecycle artifacts.

HDIP PDEP does not create Productness by registration or deployment; it realizes and operationalizes the intentionally constituted Data Product and its governed Product Version.

---

## Data Product Owner

See **DPRO**.

---

## DC Services

Enterprise Data Control services that support runtime control enforcement and control validation.

In this flow, DC Services participate in the Unified Governance Bundle and help ensure that product controls are executable and enforceable.

---

## Deployable Specification

A platform-facing specification used to deploy the Data Product.

In the Data Product flow, this is represented by **DPDS**.

---

## Deployer

The HDIP platform service responsible for provisioning and deploying the Data Product.

It consumes DPDS, Blueprint Binding, governance constraints, and usage expectations to create governed runtime views, schedules, runtime bindings, and promotion-gate evidence.

---

## DPRO

Data Product Owner.

The DPRO is the accountable business/domain owner of the Data Product’s purpose, Product Promise, semantic proposition, usage expectations, value posture, and business assertions. The role does not require the DPRO to be a data engineer and does not by itself confer ownership of all underlying Data or authoritative sources.

---

## DPROD

Data Product semantic descriptor.

DPROD is the HDIP Data Product semantic/operational descriptor that captures the Product Version’s semantic proposition, governance posture, usage expectations, lineage/provenance context, trust information, and discoverability metadata. It references authoritative Product/Data semantics and does not itself establish generic Product qualification.

---

## DPROD Publisher

The HDIP platform service responsible for finalizing and publishing the DPROD.

It registers the product into the Data Catalog and Marketplace and surfaces the product’s semantic, governance, runtime, lineage, and trust context.

---

## DPDS

Data Product Deployment Specification.

DPDS is the platform-facing deployable specification generated by HDIP. It describes how the Data Product should be provisioned, deployed, configured, scheduled, governed, and operated.

---

## DPDS Generator

The HDIP platform service that generates the DPDS.

It consumes the Compilation Pack, Blueprint Binding, Unified Governance Bundle, Usage Contract, and related compiled artifacts to produce a versioned deployment specification.

---

## DQ Services

Enterprise Data Quality services that support quality rule definition, execution, monitoring, and reporting.

In this flow, DQ Services are incorporated into the Unified Governance Bundle and later help enforce promotion and runtime quality gates.

---

## EDM

See **Enterprise Data Model**.

---

## Entitlements

See **Access & Entitlements**.

---

## Environment Registry

An enterprise registry describing available runtime environments, deployment targets, routing constraints, residency zones, and environment readiness.

It is used during preconditions checking and blueprint resolution.

---

## Enterprise Data Model

The enterprise-level conceptual or logical model used to standardize key business entities, relationships, and data structures.

In the flow, the Semantic Grounding service uses the Enterprise Data Model to align the Data Product’s semantic descriptor with enterprise meaning.

---

## Enterprise Ontology

The enterprise semantic graph or conceptual ontology that defines entities, relationships, taxonomies, and meaning across domains.

The Semantic Grounding service uses the Enterprise Ontology to validate product semantics and detect conflicts or ambiguity.

---

## Enterprise Services

The shared platform and governance capabilities used by HDIP to create, govern, deploy, register, observe, and evolve Data Products.

Examples include Catalog, Marketplace, Business Dictionary, EDM, Ontology, Policy Service, DQ Services, DC Services, Observability, Lineage, and Cost Model / FinOps.

---

## Evolve

The DPRO-facing lifecycle step where product signals are used to improve, correct, extend, or retire a Data Product.

Evolution is driven by operational, usage, DQ, compliance, drift, and consumer feedback signals.

---

## Exposure Decision

An artifact produced by the Usage Contract Validator.

It defines the allowed scopes, product views, consumption surfaces, exposure constraints, and usage boundaries for the Data Product.

---

## Gate: Assertions

A deterministic validation gate that checks whether the compiled business assertions are complete, deterministic, and semantically valid.

It may return PASS, CONDITIONAL, or FAIL depending on validation outcome.

---

## Gate: Authority

A validation gate that determines whether the DPRO has sufficient mandate and composability authority to proceed.

It may return PASS, CONDITIONAL, or FAIL.

---

## Gate: Blueprint

A validation gate that determines whether the selected blueprint is feasible in terms of cost, residency, environment routing, and platform capability.

---

## Gate: Feasibility

A validation gate that determines whether the Compilation Pack is technically and operationally feasible.

It validates whether the compiled product plan can be realized by available platform capabilities.

---

## Gate: Governance

A validation gate that determines whether the governance intent has been resolved into enforceable policy, DQ, and DC controls.

---

## Gate: Intent

A validation gate that determines whether the Intent Record is sufficiently complete and publishable.

It checks clarity, business framing, product purpose, inputs, consumers, and sensitivity information.

---

## Gate: Preconditions

A validation gate that determines whether the ecosystem is ready for product creation.

It checks capability readiness, environment readiness, and availability of required governance and platform fabric.

---

## Gate: Promotion

A deployment and publication gate that determines whether the Data Product can be promoted to a published or operational state.

It checks runtime policy, DQ/DC, and governance gates before final promotion.

---

## Gate: Semantics

A validation gate that determines whether the semantic descriptor is conflict-free and aligned with enterprise vocabulary, EDM, and ontology.

---

## Gate: Usage

A validation gate that determines whether the usage contract is governable, realistic, and usable.

It checks exposure, SLA, freshness, replay, and consumption expectations.

---

## Governance Compiler

The HDIP platform service that resolves DPRO-declared governance intent/context against applicable authoritative enterprise, domain, legal, and regulatory policies and compiles/binds the resulting controls into a Unified Governance Bundle.

It resolves policy, data quality, data control, privacy, residency, retention, and entitlement requirements.

---

## Governance Intent

The DPRO-authored declaration of governance expectations and business context for the Data Product; it is an input to authoritative policy resolution rather than an authoritative policy source by itself.

It includes privacy, residency, retention, entitlement posture, sensitivity, and compliance expectations.

---

## Governed Runtime Views

Runtime artifacts created by the Deployer that expose the Data Product through governed, policy-shaped views.

They may include masking, row-level filters, column-level filters, ABAC enforcement, and consumer-specific runtime constraints.

---

## HDIP

Holistic Data, Information and Intelligence Platform.

HDIP is the enterprise logical platform architecture that enables governed realization, deployment, discovery, consumption, observability, and evolution of Data, Information, and Intelligence capabilities and applicable BPS-qualified Products, including Data Products, Information Products, and AI Products.

---

## HDIP Platform

The automated productization layer that validates, compiles, deploys, registers, and observes Data Products.

In Spec C, it acts as an automated technology organization that transforms business-native artifacts into a governed, running product.

---

## Intent Record

A versioned artifact capturing the DPRO’s business-native product intent.

It includes purpose, expected value, inputs, target consumers, sensitivity, context, and later enrichment from authority validation.

---

## Intent Service

The HDIP platform service that captures, structures, validates, and enriches the DPRO’s intent.

It produces the Intent Record and validates whether the intent is publishable.

---

## IPCC

Input Product Composability Check.

IPCC is the validation of whether input products, marketplace-listed products, or reusable product dependencies can legitimately be composed into the new Data Product.

---

## LEG

Logical Execution Graph.

A compiled execution representation that describes how product logic should be executed in a way agnostic of the tooling.

---

## Lineage

The enterprise service that captures and exposes relationships among source assets, transformations, runtime views, generated artifacts, and published Data Products.

Lineage supports traceability, auditability, trust, and impact analysis.

---

## Marketplace

The enterprise product marketplace where Data Products are published, discovered, evaluated, subscribed to, or reused.

In this flow, DPROD publication makes the Data Product available in the Marketplace.

---

## Observability

The enterprise capability that makes product health, runtime behavior, DQ, compliance, usage, drift, and operational signals visible.

In the PDEP flow, Observability surfaces product signals that support evolution and trust.

---

## One-Click Publish

The DPRO-facing action that triggers platform-managed DPDS generation, provisioning, deployment, DPROD finalization, catalog registration, and marketplace publication.

One-click publish does not mean uncontrolled deployment; it triggers gated automated productization.

---

## Ontology

See **Enterprise Ontology**.

---

## PackGen

See **Compilation Pack Generator**.

---

## PDEP

Product Development and Evolution Process.

PDEP is the lifecycle through which a product is created, validated, compiled, deployed, published, observed, and evolved.

---

## Policy Service

The enterprise service/capability that stores, evaluates, and exposes executable policy rules. It realizes policy evaluation/distribution responsibilities but is not, by itself, the authoritative owner of the underlying enterprise, domain, legal, or regulatory policy.

Policies may include access, privacy, residency, retention, purpose limitation, regulatory constraints, and product-specific governance obligations.

---

## Precondition Report

An artifact produced by the Preconditions Checker.

It records the readiness state of required capabilities, environments, registries, and governance fabric before product creation proceeds.

---

## Preconditions Checker

The HDIP platform service that verifies whether the ecosystem is ready for product creation.

It checks capability readiness, environment readiness, and availability of required enterprise services.

---

## Product Catalog

See **Data Catalog**.

---

## Product Signals

See **Signals**.

---

## Provision & Deploy

The HDIP platform service step that provisions environments, runtime views, schedules, controls, and execution bindings for the Data Product.

It uses DPDS, Blueprint Binding, governance constraints, and usage expectations.

---

## Publisher

See **DPROD Publisher**.

---

## Runtime Views

See **Governed Runtime Views**.

---

## Semantic Conflict Report

An artifact produced by Semantic Grounding that records semantic blockers, conflicts, ambiguity, warnings, or ontology alignment issues.

It helps prevent inconsistent or duplicated product meaning.

---

## Semantic Descriptor

A versioned artifact that captures the resolved business meaning of the Data Product.

It defines entities, events, measures, relationships, vocabularies, and ontology alignment.

---

## Semantic Draft

The DPRO-authored business meaning draft.

It describes the product’s intended entities, events, measures, relationships, and vocabulary before platform grounding.

---

## Semantic Grounding

The HDIP Data Semantic Grounding service that aligns the DPRO’s semantic draft with the Business Dictionary, Enterprise Data Model, and Enterprise Ontology. This is an HDIP Data-domain alignment construct and is distinct from GEAIRM AI Context/Grounding semantics.

It produces the Semantic Descriptor and Semantic Conflict Report.

---

## Signals

A product evolution artifact containing observable runtime and trust signals.

In this flow, Signals may include data quality, drift, usage, compliance, runtime telemetry, promotion evidence, and other product health indicators.

---

## SSPD

Self-Service Product Development.

SSPD is the HDIP approach where a product owner declares intent, meaning, governance, assertions, and usage expectations in business terms, while the platform handles compilation, deployment, registration, and operation.

---

## Start New Product

The DPRO-facing step that initiates the self-service product creation journey.

It triggers precondition checks before detailed intent declaration begins.

---

## Unified Governance Bundle

A versioned artifact containing compiled/bound governance controls for the Data Product. The bundle does not become the authoritative source of the underlying policies from which those controls were derived.

It combines policy, DQ, DC, privacy, residency, retention, entitlement, and compliance constraints into a form that later stages can validate and enforce.

---

## Usage Contract

A versioned artifact describing how the Data Product is expected to be consumed.

It may include freshness, replay, explainability, exposure, SLA/SLO, consumer guarantees, usage mode, and operational posture.

---

## Usage Contract Validator

The HDIP platform service that validates the DPRO’s usage expectations.

It produces the Usage Contract and Exposure Decision and checks whether the product can be made governable and usable under the declared expectations.

---