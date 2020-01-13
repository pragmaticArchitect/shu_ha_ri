// Derived from owner-accepted experimental IPCH01–IPCH16 guide Section 7 tables.
// D41: documentary inventory reconciled with qualifications; not a normative release.
export const IPCH_GUIDANCE = [
  {
    "code": "IPCH01",
    "name": "Domain-Owned",
    "guide": "/docs/infopch/IPCH01",
    "criteria": [
      {
        "id": "OWN-M01",
        "label": "Identifiable Accountable Owner",
        "required": "An identifiable and effective accountable ownership arrangement exists for the assessed Product scope."
      },
      {
        "id": "OWN-M02",
        "label": "Legitimate Domain Mandate",
        "required": "The governing function is legitimately authorized to own the informational Promise."
      },
      {
        "id": "OWN-M03",
        "label": "Effective Decision Rights",
        "required": "The owner meaningfully governs Product purpose, intended use and scope within its mandate."
      },
      {
        "id": "OWN-M04",
        "label": "Outcome Accountability",
        "required": "Accountability for Product-level informational outcomes and relevant deficiencies is assigned and operative."
      },
      {
        "id": "OWN-M05",
        "label": "Evolution Authority",
        "required": "The owner governs material Product evolution, including change and lifecycle decisions through legitimate delegation."
      }
    ]
  },
  {
    "code": "IPCH02",
    "name": "Deployable",
    "guide": "/docs/infopch/IPCH02",
    "criteria": [
      {
        "id": "DEP-M01",
        "label": "Domain-Driven Lifecycle Agency",
        "required": "The authorized Product actor can initiate and govern the material Product lifecycle through self-service rather than merely request engineering delivery."
      },
      {
        "id": "DEP-M02",
        "label": "Intent-Native Product Definition",
        "required": "The actor can express the Product's informational/analytical meaning, purpose, assertions and constraints in domain-relevant concepts without authoring implementation instructions."
      },
      {
        "id": "DEP-M03",
        "label": "Implementation Abstraction",
        "required": "The actor is not required to select, build or configure technical realization mechanisms in order to exercise the Product lifecycle."
      },
      {
        "id": "DEP-M04",
        "label": "Independent Publication and Evolution",
        "required": "The actor can initiate and govern publication/update and material evolution without a mandatory per-change engineering translation or implementation hand-off."
      },
      {
        "id": "DEP-M05",
        "label": "Governed Self-Service",
        "required": "Competent semantic, policy, assurance and other authorization controls can operate within the lifecycle without routinely replacing self-service with an engineering delivery project."
      },
      {
        "id": "DEP-M06",
        "label": "Lifecycle Visibility and Control",
        "required": "The actor can inspect relevant lifecycle state, outcomes and failures and initiate appropriate governed corrective or follow-up action without recurring engineering dependency."
      }
    ]
  },
  {
    "code": "IPCH03",
    "name": "Declarative",
    "guide": "/docs/infopch/IPCH03",
    "criteria": [
      {
        "id": "DEC-M01",
        "label": "Intent-Native Declaration",
        "required": "The Product's informational purpose, Promise, intended outcomes and relevant assertions are expressed using domain-relevant concepts rather than procedural implementation instructions."
      },
      {
        "id": "DEC-M02",
        "label": "Structured Machine-Interpretable Definition",
        "required": "A structured Product declaration exists with an identifiable machine-interpretation basis, without reliance on humans to interpret its essential meaning for each realization."
      },
      {
        "id": "DEC-M03",
        "label": "Sufficient Product Definition",
        "required": "The declaration sufficiently describes applicable intent, semantic references, relevant inputs/outputs, consumption interfaces, constraints and assertions to determine permissible Product realization."
      },
      {
        "id": "DEC-M04",
        "label": "Authoritative Source of Product Intent",
        "required": "The declaration is the competent, governed source of truth for the assessed Product/Version; no hidden or competing procedural definition governs material Product intent."
      },
      {
        "id": "DEC-M05",
        "label": "Derived Realization Boundary",
        "required": "The declaration together with independently governed rules supports validation and determination of permissible realization without ad hoc human engineering translation of essential Product intent."
      },
      {
        "id": "DEC-M06",
        "label": "Domain-Governed Declaration Evolution",
        "required": "The legitimate Product Owner/delegate governs material changes to declaration intent without having to author procedural implementation artifacts."
      }
    ]
  },
  {
    "code": "IPCH04",
    "name": "Discoverable",
    "guide": "/docs/infopch/IPCH04",
    "criteria": [
      {
        "id": "DIS-M01",
        "label": "Intentional Governed Publication",
        "required": "The Information Product is intentionally published through a governed Product-level discovery mechanism under legitimate publication authority, whether publication is manual or authorized automation."
      },
      {
        "id": "DIS-M02",
        "label": "Independent Consumer Findability",
        "required": "An intended, authorized potential consumer can locate the Product without pre-existing knowledge of its producer, system of origin or direct access endpoint."
      },
      {
        "id": "DIS-M03",
        "label": "Product Identity and Family Integrity",
        "required": "The listing unambiguously represents the correct Product and relevant Version, and faithfully reflects independently established or qualified Product-family status rather than fabricating eligibility."
      },
      {
        "id": "DIS-M04",
        "label": "Informational Purpose and Context Transparency",
        "required": "The discovery experience communicates enough of the governing informational Promise, purpose, intended audience and analytical/informational context to enable a prospective consumer to assess relevance."
      },
      {
        "id": "DIS-M05",
        "label": "Currentness and Trust Transparency",
        "required": "Relevant Product lifecycle, qualification, assurance and trust information is current or explicitly qualified as stale, provisional or unresolved, so that discovery does not mislead the consumer."
      },
      {
        "id": "DIS-M06",
        "label": "Consumption and Access Orientation",
        "required": "The consumer can determine relevant consumption conditions, authorized uses, applicable restrictions, an available entitlement/access-request route where required and reasonable next steps toward permitted consumption."
      }
    ]
  },
  {
    "code": "IPCH05",
    "name": "Self-Describing",
    "guide": "/docs/infopch/IPCH05",
    "criteria": [
      {
        "id": "SDC-M01",
        "label": "Authoritative Informational Meaning",
        "required": "The Product-bound description explicitly explains the informational Promise, analytical purpose, domain concepts, scope and relevant business context using meaningful, governed terms."
      },
      {
        "id": "SDC-M02",
        "label": "Interpretable Outputs and Semantics",
        "required": "Relevant outputs and measures are explained with sufficient semantic and structural context, including applicable units, dimensions, time meaning, aggregation grain, assumptions and interpretive exclusions."
      },
      {
        "id": "SDC-M03",
        "label": "Provenance and Dependency Transparency",
        "required": "Material sources, major dependencies and conceptual derivation/transformation context are visible sufficiently to understand the produced information, without requiring technical pipeline disclosure."
      },
      {
        "id": "SDC-M04",
        "label": "Usage Context and Limitations",
        "required": "Intended uses, material limitations, constraints, freshness or update expectations, quality posture and interpretation boundaries are explicitly represented wherever applicable."
      },
      {
        "id": "SDC-M05",
        "label": "Product-Bound Structured Self-Description",
        "required": "Authoritative Product-associated description is accessible through governed Product artifacts, registries, APIs or version-resolved references and is sufficiently structured for machine interpretation; INFOPROD / applicable DPP are possible examples, not mandatory technologies."
      },
      {
        "id": "SDC-M06",
        "label": "Independent Consumer Interpretation",
        "required": "Competent authorized human and machine consumers can understand and evaluate relevant Product meaning and suitability from its Product-bound information without producer contact, external explanatory meetings or implementation reverse-engineering."
      },
      {
        "id": "SDC-M07",
        "label": "Version Alignment and Descriptive Integrity",
        "required": "The description applies to the exact Product/Version, remains governed through material changes and is not demonstrably stale or inconsistent with the Product's current informational definition."
      }
    ]
  },
  {
    "code": "IPCH06",
    "name": "Trustworthy",
    "guide": "/docs/infopch/IPCH06",
    "criteria": [
      {
        "id": "TRU-M01",
        "label": "Objective Evidence-Backed Trust",
        "required": "Relevant trust statements are substantiated by verifiable measurements, evaluations or independently attributable control evidence, not just producer assertions, labels or reputation."
      },
      {
        "id": "TRU-M02",
        "label": "Product-Level Trust Attribution",
        "required": "Evidence is defensibly tied to the exact Product/Version and material informational constitution, not merely to source tables, dashboards, individual jobs or unrelated implementations."
      },
      {
        "id": "TRU-M03",
        "label": "Currentness and Evidence Provenance",
        "required": "Material evidence is dated, attributable and appropriately refreshed, with effective status, provenance, expiry/supersession and material invalidation conditions identifiable."
      },
      {
        "id": "TRU-M04",
        "label": "Information-Appropriate Reliability Assurance",
        "required": "Evidence covers applicable quality, analytical validity, semantic/temporal interpretation, provenance/dependency and fitness-for-use risks appropriate to the Product's Promise and risk; no universal metric checklist is prescribed."
      },
      {
        "id": "TRU-M05",
        "label": "Governance, Control and Assurance Visibility",
        "required": "Applicable qualification, controls, risk obligations and assurance outcomes are faithfully represented or traceably referenced from their competent independent authorities, including unresolved states."
      },
      {
        "id": "TRU-M06",
        "label": "Governed Machine-Consumable Trust Exposure",
        "required": "Intended consumers and authorized governance automation can independently inspect a structured, machine-consumable, authoritative Product-bound trust record (e.g. applicable DPP or a record whose equivalence is independently governed), without assuming INFOPS has authorized a particular alternative."
      },
      {
        "id": "TRU-M07",
        "label": "Material Risk, Incident and Limitation Transparency",
        "required": "Known material incidents, failures, restrictions, invalidations, unresolved risks and evidence gaps are made visible or accurately qualified rather than suppressed by a blanket trustworthy label."
      }
    ]
  },
  {
    "code": "IPCH07",
    "name": "Reusable",
    "guide": "/docs/infopch/IPCH07",
    "criteria": [
      {
        "id": "REU-M01",
        "label": "Generalized Informational Capability",
        "required": "The Product has an intentionally reusable informational Promise and coherent domain-meaningful capability rather than being constituted solely as one predefined consumer's bespoke deliverable."
      },
      {
        "id": "REU-M02",
        "label": "Consumer-Independent Product Constitution",
        "required": "Its essential semantics, analytical interpretation, outputs and governing assertions are not structurally coupled to one consumer-specific application, visualization or implementation."
      },
      {
        "id": "REU-M03",
        "label": "Demonstrated Independent Adoption",
        "required": "Credible actual consumption has occurred across multiple distinguishable independent consumer contexts, beyond merely contemplated uses or invocations attributable to one context."
      },
      {
        "id": "REU-M04",
        "label": "No Bespoke Producer Reconstruction",
        "required": "Additional legitimate consumers adopt the existing Product without requiring producer redefinition of its informational Promise, consumer-specific derivation/pipelines or bespoke Product variants."
      },
      {
        "id": "REU-M05",
        "label": "Governed Repeatable Consumption",
        "required": "Legitimate consumers can undertake repeatable adoption through defined governed consumption mechanisms without indispensable producer-mediated engineering."
      },
      {
        "id": "REU-M06",
        "label": "Stable Semantic and Consumption Contracts",
        "required": "Consumption interfaces, semantic definitions, output expectations and material changes are sufficiently governed and stable to support predictable repeat adoption."
      },
      {
        "id": "REU-M07",
        "label": "Product-Level Reuse Evidence Integrity",
        "required": "Adoption evidence is attributable to the assessed Information Product/Version and separates actual independent Product reuse from shared components, repeated calls, duplicated identities and bespoke deliveries."
      }
    ]
  },
  {
    "code": "IPCH08",
    "name": "SLA–SLO Backed & Observable",
    "guide": "/docs/infopch/IPCH08",
    "criteria": [
      {
        "id": "OBS-M01",
        "label": "Explicit Measurable SLA–SLO Expectations",
        "required": "The Product has defined, governed and version-associated measurable expectations for its applicable operational and informational behaviour, including thresholds and meaningful evaluation windows."
      },
      {
        "id": "OBS-M02",
        "label": "Product-Level End-to-End Observability",
        "required": "Monitoring reflects the actual consumer-facing Information Product experience, outcomes and informational Promise, not merely the health of infrastructure, scripts, pipelines or components."
      },
      {
        "id": "OBS-M03",
        "label": "Continuous Measurement and Evaluation",
        "required": "Relevant runtime and informational signals are automatically collected and evaluated against the defined expectations at a cadence sufficient for material deviation detection given the Product's operating pattern and risk."
      },
      {
        "id": "OBS-M04",
        "label": "Information-Appropriate Behavioural Coverage",
        "required": "Applicable informational quality, freshness, analytical/derivation, dependency and degradation concerns material to the Product's Promise are included in the monitored evidence, with justified applicability."
      },
      {
        "id": "OBS-M05",
        "label": "Detectable and Actionable Deviations",
        "required": "Material SLA/SLO breaches, anomalies or degradation can be detected, attributed, surfaced and routed to competent investigation or remediation processes."
      },
      {
        "id": "OBS-M06",
        "label": "Automated Enterprise PMDD Maturity Observability",
        "required": "Independently governed enterprise mechanisms actually execute recurring applicable PMDD characteristic evaluations, emit dated attributable maturity snapshots and preserve regression evidence, not just test designs or manual attestations."
      },
      {
        "id": "OBS-M07",
        "label": "Governed Machine-Consumable Visibility",
        "required": "Product actors, authorized consumers, governance and appropriate enterprise mechanisms can inspect structured Product-linked observability outcomes and historical evidence through governed access."
      },
      {
        "id": "OBS-M08",
        "label": "Evidence Identity, Currentness and Historical Integrity",
        "required": "Monitoring and PMDD evidence identifies the applicable Product/Version, effective realization/occurrence and evaluation/criteria versions, with timestamps, history, comparability and explicit limitations."
      }
    ]
  },
  {
    "code": "IPCH09",
    "name": "Compliant by Design",
    "guide": "/docs/infopch/IPCH09",
    "criteria": [
      {
        "id": "CBD-M01",
        "label": "Federated Policy Authority and Applicability",
        "required": "Applicable policies are determined from competent enterprise/global, divisional where applicable, domain and Product governance authorities; higher-order constraints cannot be overridden by unauthorized Product choices."
      },
      {
        "id": "CBD-M02",
        "label": "Design-Time Policy Visibility",
        "required": "The authorized Product Owner/delegate can inspect applicable policy obligations, their relevant rationale and legitimately available decisions while defining or evolving the Product."
      },
      {
        "id": "CBD-M03",
        "label": "Product-Bound Declarative Controls",
        "required": "Applicable policy sets, classifications, entitlements and usage restrictions are explicitly and traceably bound to the assessed Product/Version throughout its governed lifecycle."
      },
      {
        "id": "CBD-M04",
        "label": "Machine-Interpretable Executable Policies",
        "required": "Applicable control obligations are represented in computationally interpretable and executable form, without a required manual translation or bespoke per-consumer engineering step for each enforcement context."
      },
      {
        "id": "CBD-M05",
        "label": "Automatic Runtime Enforcement",
        "required": "Applicable policy and entitlement controls actually execute at the relevant access, information processing, delivery and consumption boundaries, rather than relying on documentary compliance claims."
      },
      {
        "id": "CBD-M06",
        "label": "Consistent Product-Level Control Coverage",
        "required": "Controls remain effective across all applicable consumer interfaces, derived outputs and realization paths, with no material ungoverned bypass; uniform underlying technology is not compulsory."
      },
      {
        "id": "CBD-M07",
        "label": "Governed Product-Specific Constraints and Lifecycle Integrity",
        "required": "Authorized Product-specific restrictions can be declared and evolved within higher-order policy bounds, and required enforcement bindings remain intact through test, publication, change and realization."
      },
      {
        "id": "CBD-M08",
        "label": "Violation Detection and Enforcement Evidence",
        "required": "Material policy violations and control decisions can be detected, attributed and evidenced, with suitable enforcement, escalation or competent human oversight when applicable."
      }
    ]
  },
  {
    "code": "IPCH10",
    "name": "Addressable",
    "guide": "/docs/infopch/IPCH10",
    "criteria": [
      {
        "id": "ADR-M01",
        "label": "Explicit Product Output Port Definition",
        "required": "The Information Product declares identifiable, first-class output ports through which its informational capability is consumed."
      },
      {
        "id": "ADR-M02",
        "label": "Stable Documented Consumption Contracts",
        "required": "Every applicable port has a documented, governed, version-associated contract identifying access, relevant inputs/parameters, delivered outputs, semantics and usage conditions."
      },
      {
        "id": "ADR-M03",
        "label": "Capability-Level Semantic Encapsulation",
        "required": "Ports expose the governed Information Product capability without obliging consumers to reconstruct it from internal Data Products, tables, processing stages or implementation details."
      },
      {
        "id": "ADR-M04",
        "label": "Experience and Application Independence",
        "required": "The capability can be independently accessed without dependence on a particular dashboard, UI, embedded application or proprietary consumer experience."
      },
      {
        "id": "ADR-M05",
        "label": "Consumer-Appropriate Port Modalities",
        "required": "Available ports fit the Product's declared consumer contexts, without unsuitable access patterns or bespoke per-consumer reconstruction. No universal port count is required."
      },
      {
        "id": "ADR-M06",
        "label": "Governed Policy-Enforced Port Access",
        "required": "Applicable access, information-handling and usage controls are effectively enforced across relevant Product-port consumption paths."
      },
      {
        "id": "ADR-M07",
        "label": "Product and Contract Lifecycle Stability",
        "required": "Port identifiers and contract evolution are governed so internal implementation changes do not cause uncontrolled breaking changes for consumers."
      },
      {
        "id": "ADR-M08",
        "label": "Product-Level Addressability Evidence Integrity",
        "required": "Evidence correctly identifies the assessed Product/Version, declared ports, effective contracts, accessible mechanisms and related governance outcomes without conflating UI or internal component evidence."
      }
    ]
  },
  {
    "code": "IPCH11",
    "name": "Semantically Aligned",
    "guide": "/docs/infopch/IPCH11",
    "criteria": [
      {
        "id": "SEM-M01",
        "label": "Authoritative Shared Semantic Anchoring",
        "required": "Material business and informational concepts of the Product refer to independently governed enterprise or domain semantic definitions, not local words alone."
      },
      {
        "id": "SEM-M02",
        "label": "Explicit Machine-Referenceable Semantic Bindings",
        "required": "Concepts, measures and outputs have explicit structured relationships to competent authoritative meanings that machine-assisted processes can reference and examine."
      },
      {
        "id": "SEM-M03",
        "label": "Informational Promise and Analytical Meaning Alignment",
        "required": "Material measures, derivations, assumptions, context and intended interpretations have governed, unambiguous meaning aligned to applicable semantic authority."
      },
      {
        "id": "SEM-M04",
        "label": "Input, Output and Consumer Interpretation Consistency",
        "required": "Material source inputs, transformation outcomes, output-port representations and declared consumer meanings remain coherent or explicitly distinguished where different."
      },
      {
        "id": "SEM-M05",
        "label": "Governed Semantic Extensions and Deviations",
        "required": "Semantic extensions and deviations are explicit, justified, version-linked and within competent semantic-governance decisions, rather than unilateral local redefinition."
      },
      {
        "id": "SEM-M06",
        "label": "Semantic Stability and Governed Evolution",
        "required": "Changes to material meaning, source definition revisions and resulting compatibility effects are identified, version-governed and communicated to affected consumers."
      },
      {
        "id": "SEM-M07",
        "label": "Demonstrable Semantic Interoperability",
        "required": "Independent consumers or Products can interpret the declared information using authoritative references without undocumented negotiation, guesswork or manual reconciliation."
      },
      {
        "id": "SEM-M08",
        "label": "Product-Level Semantic Evidence Integrity",
        "required": "Evidence can be attributed to the exact Product/Version, authoritative semantic definition/version, relevant mappings and effective realization, with identified currentness and limitations."
      }
    ]
  },
  {
    "code": "IPCH12",
    "name": "Consumption-Driven Intent",
    "guide": "/docs/infopch/IPCH12",
    "criteria": [
      {
        "id": "INT-M01",
        "label": "Explicit Governed Consumption Intent",
        "required": "The Product has an authoritative, expressly governed purpose rather than an inferred or retrospective justification."
      },
      {
        "id": "INT-M02",
        "label": "Identified Consumers and Decision Contexts",
        "required": "Target consumer archetypes and relevant business, analytical, regulatory or operational decision contexts are sufficiently defined."
      },
      {
        "id": "INT-M03",
        "label": "Defined Intended Outcomes",
        "required": "Expected consuming outcomes or improvements and assessable effectiveness expectations are stated, allowing legitimate non-financial outcomes."
      },
      {
        "id": "INT-M04",
        "label": "Informational Promise Aligned to Intent",
        "required": "Measures, interpretation, analytical scope, granularity, time horizon and material assumptions are shaped by intended consumption."
      },
      {
        "id": "INT-M05",
        "label": "Consumption Requirements Reflected in Design",
        "required": "Applicable service, quality, interpretation, delivery-port and usage constraints trace to consumer needs."
      },
      {
        "id": "INT-M06",
        "label": "Consumer-Independent Core Intent Integrity",
        "required": "Legitimate variation across consumer contexts does not arbitrarily redefine or contradict the Product’s core informational purpose; no minimum number of active consumers is introduced."
      },
      {
        "id": "INT-M07",
        "label": "Consumption-Led Product Evolution",
        "required": "A governed mechanism uses relevant feedback, usage/outcome signals and changed business priorities in Product evolution decisions."
      },
      {
        "id": "INT-M08",
        "label": "Product-Level Intent Traceability and Evidence Integrity",
        "required": "Intent, consumers, outcomes, design/evolution evidence and effective dates are attributable to the exact assessed Product/Version."
      }
    ]
  },
  {
    "code": "IPCH13",
    "name": "Testable & Versioned",
    "guide": "/docs/infopch/IPCH13",
    "criteria": [
      {
        "id": "TAV-M01",
        "label": "Explicit Governed Product Version Identity",
        "required": "The assessed Product has identifiable, meaningful versions and attributable change history, distinct from component/realization revisions."
      },
      {
        "id": "TAV-M02",
        "label": "Product-Bound Testable Contracts",
        "required": "Material informational, semantic, structural, quality, consumption and applicable policy expectations are expressed as testable Product-level assertions."
      },
      {
        "id": "TAV-M03",
        "label": "Automated Reproducible Product-Level Tests",
        "required": "Governed tests actually execute automatically and reproducibly against identifiable Product versions and appropriate inputs, conditions and criteria."
      },
      {
        "id": "TAV-M04",
        "label": "Informational and Analytical Behaviour Validation",
        "required": "Executed tests verify material measures, derivations, analytical assumptions, informational invariants and consumer-facing outcomes, not merely technical operation."
      },
      {
        "id": "TAV-M05",
        "label": "Regression and Compatibility Protection",
        "required": "Product evolution is evaluated against applicable prior guarantees, with material inadvertent regressions detectable."
      },
      {
        "id": "TAV-M06",
        "label": "Governed Validation and Promotion Gates",
        "required": "Material consumer-facing version promotion is conditioned on appropriately evidenced validation and a competent governed disposition."
      },
      {
        "id": "TAV-M07",
        "label": "Consumer-Protective Version Evolution",
        "required": "Breaking/nonbreaking changes are identified, managed and communicated with appropriate migration, coexistence or compatibility controls."
      },
      {
        "id": "TAV-M08",
        "label": "Versioned Test and Evolution Evidence Integrity",
        "required": "The evidence binds Product/Version, test identity/version/execution, conditions, expected/actual results, dependencies, realization and promotion determination with current provenance."
      }
    ]
  },
  {
    "code": "IPCH14",
    "name": "Economically Accountable",
    "guide": "/docs/infopch/IPCH14",
    "criteria": [
      {
        "id": "ECO-M01",
        "label": "Governed Product-Level Economic Identity",
        "required": "The economically accountable subject is an identifiable governed Information Product/Version with traceable material cost, use and value evidence—not a project or unallocated platform aggregate."
      },
      {
        "id": "ECO-M02",
        "label": "Material Lifecycle Cost Visibility",
        "required": "Build/run/support/shared-service economics are measured or defensibly estimated at sufficient granularity, with materiality, allocation assumptions, time and uncertainty visible."
      },
      {
        "id": "ECO-M03",
        "label": "Consumption and Usage Visibility",
        "required": "Actual relevant consumer/archetype, port, workload, frequency or other usage signals are available at decision-useful granularity and period."
      },
      {
        "id": "ECO-M04",
        "label": "Contextual Fitness and Value Evidence",
        "required": "Evidence of fitness for material intended contexts and defensible intended/realized informational value; consumption alone is not value."
      },
      {
        "id": "ECO-M05",
        "label": "Explicit Economic and Attribution Accountability",
        "required": "Competent Product/producer/consumer/platform responsibility boundaries and qualified value-contribution or causal assumptions are explicit and governable."
      },
      {
        "id": "ECO-M06",
        "label": "Active Cost-to-Value Optimization",
        "required": "Periodic analysis and evidenced adjustments or justified non-action consider resources against informational fitness, quality and other obligations."
      },
      {
        "id": "ECO-M07",
        "label": "Economic Evidence in Product Lifecycle Decisions",
        "required": "Evidence informs relevant investment, operation, scaling, roadmap, redesign, continuation or retirement decisions through competent authority."
      },
      {
        "id": "ECO-M08",
        "label": "Product-Level Economic Evidence Integrity",
        "required": "Cost/usage/fitness/value records and decisions identify the right Product/Version, period, consumer context, realization and provenance; uncertainty and currency are traceable."
      }
    ]
  },
  {
    "code": "IPCH15",
    "name": "Explainable & Transparent",
    "guide": "/docs/infopch/IPCH15",
    "criteria": [
      {
        "id": "XTR-M01",
        "label": "Governed Explainability Scope and Purpose",
        "required": "Material result/output classes, intended consumers and oversight contexts, required explanation purpose and accountable scope are identified and governed."
      },
      {
        "id": "XTR-M02",
        "label": "Contextually Meaningful Informational Explanations",
        "required": "Material outputs can be interpreted in appropriate business/analytical terms, not merely technical code, feature IDs or internal processing vocabulary."
      },
      {
        "id": "XTR-M03",
        "label": "Transparent Derivation and Contributing Factors",
        "required": "Relevant source selection, calculations, transformations, assumptions, exclusions and material contribution factors are inspectable at an appropriate level without reconstructing implementation."
      },
      {
        "id": "XTR-M04",
        "label": "Product-Level Explanation Accessibility",
        "required": "Required explanations are available via governed Product interfaces or explicitly linked authorized explanation facilities; not confined to tribal knowledge or inaccessible internal tooling."
      },
      {
        "id": "XTR-M05",
        "label": "Structured and Machine-Referenceable Explanation Evidence",
        "required": "Material explanation claims are represented with enough structure/referenceability to support appropriate system, governance and audit interpretation, without mandating a technology."
      },
      {
        "id": "XTR-M06",
        "label": "Proportionate Explanation Depth and Limitations",
        "required": "Explanation depth fits material context, consequence and oversight; uncertainty, exclusions, caveats and limits are not misleadingly omitted."
      },
      {
        "id": "XTR-M07",
        "label": "Explanation Consistency and Verifiability",
        "required": "Explanation content is consistent with actual applicable derivation, semantic meaning and Product/Version behaviour, with meaningful means to inspect, challenge or verify claims."
      },
      {
        "id": "XTR-M08",
        "label": "Product-Level Explanation Provenance and Evidence Integrity",
        "required": "Explanation and evidence reliably bind exact Product/Version, result/occurrence where relevant, applicable semantic/method revisions, realization/effective time and evidence limitations."
      }
    ]
  },
  {
    "code": "IPCH16",
    "name": "Interoperable & Composable",
    "guide": "/docs/infopch/IPCH16",
    "criteria": [
      {
        "id": "IOC-M01",
        "label": "Governed Interoperability and Composition Contracts",
        "required": "Stable, sufficiently machine-understandable ports, schemas and contracts enable authorized independent use and applicable composition."
      },
      {
        "id": "IOC-M02",
        "label": "Semantic Compatibility for Safe Combination",
        "required": "Material informational concepts, measures, time bases, assumptions and interpretations are compatible or differences are explicitly governed and usable without unsafe equivalence."
      },
      {
        "id": "IOC-M03",
        "label": "Dependency and Provenance Preservation",
        "required": "Upstream Product identities, versions, currentness, dependency topology and material informational provenance remain identifiable through use and composition."
      },
      {
        "id": "IOC-M04",
        "label": "Policy and Consumer-Obligation Continuity",
        "required": "Applicable rights, permitted uses, confidentiality, security, privacy, licensing, retention and other obligations survive relevant integration modes."
      },
      {
        "id": "IOC-M05",
        "label": "Independent Consumption Without Implementation Coupling",
        "required": "Consumers can consume and, where applicable, combine through published governed contracts without undocumented internals, continuous bespoke producer help or per-consumer ungoverned integration."
      },
      {
        "id": "IOC-M06",
        "label": "Coherent Composition Modes and Product Boundaries",
        "required": "Direct use, federation/orchestration and intentional Productized Composition are correctly distinguished; coordination alone is not falsely asserted as Product creation."
      },
      {
        "id": "IOC-M07",
        "label": "Governed Derived-Product and Compound Boundaries",
        "required": "Any actually claimed new Product is independently qualified with relevant identity, owner, Promise and dependency topology, under appropriate Product-family/Compound competence; absent claims are not fabricated."
      },
      {
        "id": "IOC-M08",
        "label": "Product-Level Interoperability Evidence Integrity",
        "required": "Contracts, mappings, dependencies, policy continuity and composition evidence bind exact Product/Version, contract/dependency versions, realization/occurrence, context and effective time."
      }
    ]
  }
] as const;
