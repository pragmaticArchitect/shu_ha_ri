# IPCH02 — Deployable

**Information Product Characteristic (IPCH) | PMDD maturity guidance**  
**Artifact:** `IPCH02-PMDD-GUIDE-01`  
**Revision:** `FIRST-PASS-DRAFT-01`  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED` — source/criteria baseline approved under `INFOPS-0.1-IPCH-P01-D11-F01`; this FIRST-PASS-DRAFT-01 was accepted for experimental guidance under `INFOPS-0.1-IPCH-P01-D12-F01`; it is not finally approved. Publication in the INFOPS site is documentation availability, not normative adoption.  
**Authority:** Experimental guidance; no normative Product qualification, institutional mandate, deployment authorization, or final guide approval.  
**Lineage:** IPCH D01–D12; DPCH02 and AIPCH02; D02/D03 assessment architecture; D04 sixteen-section template; owner-directed two-pass authoring strategy.

> **Core assertion:** Deployable means that the authorized Information Product Owner or delegate can drive creation, publication and material evolution of the informational capability through **intent-driven, governed self-service**, without having to perform technical implementation or rely on recurring engineering translation. A system being technically deployable by engineers is not sufficient.

## 1. Characteristic identity and source lineage

- **ID:** `IPCH02`; **name:** Deployable; **Product family:** Information Product.
- **Direct sources:** `DPCH02 — Deployable` (domain-driven end-to-end self-service; business-native intent; technology constructs compiled away) and `AIPCH02 — Deployable` (intent-driven self-service; domain agency; abstracted realization; no engineering translation layer).
- **Approved First-Pass baseline:** `D11-F01`, clauses F01.1–F01.16: six mandatory positive criteria (`DEP-M01–M06`), seven negative criteria (`DEP-N01–N07`), six evidence requirements (`DEP-ES01–ES06`), five open research questions (`DEP-R01–R05`).
- **Assessment standards:** experimental `IPCH-PMDD-GT-01`, `IPCH-ES-01`, `IPCH-NDC-01`, D02 eligibility/applicability and D03 characteristic-level scoring.
- **Source-derived versus specialized:** lifecycle self-service, intent-native interactions and technical abstraction are inherited; the informational Promise, analytical context, semantic dependencies and specific IPCH02 criteria are the proposed Information-family specialization approved for First Pass.

## 2. What the characteristic asserts

An eligible Information Product satisfies **Deployable** when an authorized Product actor can initiate and govern its relevant lifecycle through **governed, intent-driven self-service**: expressing *what* informational capability is required, invoking its creation or material evolution, publishing or updating it, and observing lifecycle outcomes without being required to engineer *how* it works.

This is a claim about **domain lifecycle agency**, not simply automated execution or the existence of a deployment pipeline. Engineering maintains and improves underlying platform capabilities; it should not act as a mandatory human translator of each Product's intent. Competent human governance approvals may remain necessary and do not, by themselves, invalidate self-service.

The assertion does **not** require any particular portal, compiler, cloud, product factory, interface modality, code format or deployment topology.

## 3. Information Product specialization

The Product actor expresses informational and analytical purpose, intended consumers and uses, governing informational Promise, applicable semantic references, expected informational assertions and constraints. The domain need not define SQL, joins, DAGs, infrastructure parameters, execution engines or integration implementation to realize the Product.

**Logical separation of concerns:**

| Concern | Responsibility |
|---|---|
| Information Product intent, purpose and material evolution | Legitimate Information Product Owner or authorized delegate |
| Authoritative semantic meaning | GEARM / competent semantic authority |
| Analytical architectural responsibilities | GEARA / competent architecture authority |
| Compilation, implementation, infrastructure and operations | Appropriate realization/platform functions |
| Productness, Product-family/Compound status | Independent BPS/PIN and competent family authorities |
| Policy, legal, assurance and consequential-action controls | Their independently competent authorities |

Self-service capability must not be confused with authorization to override these independent authorities. The owner may request a governed realization without personally making realization choices.

## 4. Assessment subject and authority

Assess the **exact Information Product and Version**, declared informational Promise and relevant lifecycle scope, authorized Product actor/delegation, assessed environment and time, and the applicable enterprise assessment profile. Record the evidence for real or reproducibly demonstrated capability, not merely architectural intention.

Separate: (a) Product intent and authority, (b) specification/descriptor and its version, (c) realization implementation/revision, (d) deployment or publication event, and (e) runtime occurrence. A successful technical deployment event by itself does not prove that a domain actor could have driven the lifecycle without engineering translation.

No agent or assessor may independently confer Product-family eligibility, mandate, governance approval or normative conformance.

## 5. Applicability and N/A rules

**Default:** IPCH02 applies to an eligible Information Product. No generic whole-characteristic `NOT_APPLICABLE` exemption is established. Absence of a self-service mechanism is not an N/A reason; nor is a Product's early lifecycle stage, outsourced platform, or technical complexity.

A **specific evidence mechanism** can be inapplicable (e.g., no historical production incidents or no prior material version change), while the underlying capability remains assessable through appropriate evidence or demonstrations. Exceptional whole-characteristic N/A requires affirmative, competent D02 applicability determination. Failure to establish Product/Version eligibility means `NOT_ASSESSABLE`, not `NOT_MET` or `NOT_APPLICABLE`.

## 6. Distinctness and non-duplication

| Other characteristic | Independent maturity claim |
|---|---|
| IPCH01 — Domain-Owned | The legitimacy and effectiveness of ownership; IPCH02 evaluates the owner's *ability to exercise lifecycle agency* |
| IPCH03 — Declarative | Quality/governance of declarative Product specification; IPCH02 evaluates self-service lifecycle driven by intent |
| IPCH08 — SLA–SLO Backed & Observable | Runtime service objectives and observability; IPCH02 requires Product actor access to lifecycle status and exceptions |
| IPCH09 — Compliant by Design | Efficacy of compliance controls; IPCH02 requires legitimate governance not to become engineering translation |
| IPCH13 — Testable & Versioned | Tests and version discipline; IPCH02 requires authorized ability to initiate evolution |
| IPCH16 — Interoperable & Composable | Correct cross-Product interaction/composition; IPCH02 evaluates access to composition as a lifecycle action if relevant |

An artifact can support several claims but does not automatically establish each. No characteristic is scored by duplicating another characteristic's conclusions.

## 7. Core mandatory positive criteria — `MET`

**All six mandatory claims must be adequately supported for `MET`.** The criteria are conjunctive, *not* a weighted checklist.

| ID | Mandatory criterion | What adherence requires |
|---|---|---|
| **DEP-M01** | **Domain-Driven Lifecycle Agency** | The authorized Product actor can initiate and govern the material Product lifecycle through self-service rather than merely request engineering delivery. |
| **DEP-M02** | **Intent-Native Product Definition** | The actor can express the Product's informational/analytical meaning, purpose, assertions and constraints in domain-relevant concepts without authoring implementation instructions. |
| **DEP-M03** | **Implementation Abstraction** | The actor is not required to select, build or configure technical realization mechanisms in order to exercise the Product lifecycle. |
| **DEP-M04** | **Independent Publication and Evolution** | The actor can initiate and govern publication/update and material evolution without a mandatory per-change engineering translation or implementation hand-off. |
| **DEP-M05** | **Governed Self-Service** | Competent semantic, policy, assurance and other authorization controls can operate within the lifecycle without routinely replacing self-service with an engineering delivery project. |
| **DEP-M06** | **Lifecycle Visibility and Control** | The actor can inspect relevant lifecycle state, outcomes and failures and initiate appropriate governed corrective or follow-up action without recurring engineering dependency. |

An enterprise cannot waive any of these six claims while describing the same IPCH02 guide as fully met. A particular tool or artifact format is not mandatory where equivalent sufficient evidence establishes the claim.

## 8. Core negative criteria — `NOT_MET`

| ID | Demonstrated failure condition |
|---|---|
| **DEP-N01** | Product creation or publication intrinsically depends on engineers implementing or translating domain requirements. |
| **DEP-N02** | The intended domain actor must write code, pipelines, queries, infrastructure definitions or equivalent technical implementation material to express Product intent. |
| **DEP-N03** | Material evolution intrinsically requires an engineering backlog/project hand-off instead of actor-controlled governed self-service. |
| **DEP-N04** | A purported self-service interface merely delegates technical design or configuration to domain actors. |
| **DEP-N05** | An authorized actor cannot initiate a material publication or lifecycle management action in the otherwise applicable lifecycle scope. |
| **DEP-N06** | Each necessary governance step routinely requires an engineer to implement or translate Product intent, rather than a competent governance decision. |
| **DEP-N07** | The actor cannot discover material lifecycle outcomes or initiate appropriate follow-up without recurring engineering mediation. |

These are **counter-evidence conditions**, not automatic consequences of missing records. Distinguish foundational failure from a bounded transitional gap. A duly authorized human *governance* sign-off is not a prohibited engineering hand-off.

## 9. `PARTIAL`, `NOT_MET` and evidence-limited decisions

| Evidence-supported condition | Proposed characteristic finding |
|---|---|
| All six criteria demonstrably satisfied; no foundational counter-evidence | `MET` |
| Genuine, operational intent-native self-service and abstraction already exist, but one or more material lifecycle capabilities are demonstrably incomplete without defeating the core claim | `PARTIAL` |
| Competent evidence establishes a foundational lack of intent-native agency or required dependence on domain technical implementation / human engineering translation | `NOT_MET` |
| Material missing, contradictory, stale or insufficient evidence prevents the particular defensible maturity conclusion | `EVIDENCE_LIMITED` (evidence qualifier; **not** a fifth maturity state) |
| Eligible subject not established | `NOT_ASSESSABLE` under D02; outside maturity scoring |
| Whole-characteristic N/A affirmatively justified by competent authority | `NOT_APPLICABLE` under D02; no generic case established here |

**Precedence:** Establish eligibility and applicability → review claims and contrary evidence → retain material uncertainty → distinguish demonstrable foundational failure from materially incomplete operational capability → assign the characteristic finding only when justified. An actual, demonstrable foundational failure is not cancelled by success on other criteria. Conversely, uncertainty about one claim does not erase a separate, independently demonstrated defect.

A future roadmap, polished portal screenshot, successful engineer-led deployment or a self-service label does not prove current end-to-end capability. Mere partial automation is not necessarily `PARTIAL` if the domain remains intrinsically dependent on engineers to translate the Product Promise.

## 10. Evidence signals and sufficiency

| Rule | Claim | Establishing evidence patterns (non-prescriptive) | Contrary signals |
|---|---|---|---|
| **DEP-ES01** | DEP-M01 lifecycle agency | Authorized actor journey or repeatable demonstration of material lifecycle actions | Domain can only submit engineering requests |
| **DEP-ES02** | DEP-M02 intent-native definition | Representative intent expression in informational/analytical concepts | Mandatory SQL, pipeline, orchestration or infrastructure authoring |
| **DEP-ES03** | DEP-M03 implementation abstraction | Realization boundary and demonstrated separation of domain choices from implementation choices | Domain must configure technical internals |
| **DEP-ES04** | DEP-M04 publication/evolution | Demonstrated publication and material-change initiation; operating records or representative exercises | Recurring engineering translation/release backlog dependency |
| **DEP-ES05** | DEP-M05 governed self-service | Evidence that competent approvals and controls bind to the self-service process | Policy approvals rely on engineering implementation for each Product change |
| **DEP-ES06** | DEP-M06 visibility and control | Actor-visible state/exception demonstration and permitted follow-up route | Lifecycle errors only surfaced or remediated through engineering mediation |

**Evidence rules:**

- **Identity:** Tie every claim to the assessed Product, Version, relevant lifecycle action, authorized actor, assessment profile and date.
- **Authority:** Distinguish Product actor rights, valid governance sign-off, platform role and deployment operation.
- **Operational sufficiency:** Prefer direct, reproducible demonstrations or credible current operating records over unsupported architecture claims; evidence can be appropriately pre-production where the assessed claim is bounded accordingly.
- **Proportionality:** No universal production incident, historical upgrade, click-through UI or platform technology is required. Where no event occurred, defensible readiness evidence can be considered.
- **Contradictions:** Preserve material contrary, stale, disputed and missing evidence. Never interpret absent evidence automatically as `NOT_MET` or ignore a demonstrably failed foundation.
- **Assurance profile:** An enterprise can demand stronger corroboration/currentness but may not remove mandatory criteria or lower their semantic meaning and still claim unchanged IPCH02 adherence.

These rules are guidance for claim-specific sufficiency, not deployment implementation instructions or requirements to use particular document formats.

## 11. Agent-assisted or human assessment decision rule

The same claim definitions and evidence requirements apply whether an assessment is manual, deterministic or agent-assisted.

1. Establish **D02** Product/Version eligibility; otherwise return `NOT_ASSESSABLE`.
2. Establish IPCH02 applicability; require affirmative evidence for any exceptional N/A.
3. Identify the authorized Product actor, informational Promise and applicable enterprise assessment profile/version.
4. Evaluate all `DEP-M01–DEP-M06` using `DEP-ES01–DEP-ES06`; inspect all relevant `DEP-N01–DEP-N07` counter-evidence.
5. Separate intent expression, generated specification, technical realization, publication/deployment and actual runtime occurrence.
6. Classify missing/contradictory evidence and determine whether it prevents a defensible claim. Do not resolve institutional mandates outside competent authority.
7. Propose `MET` only when every mandatory criterion is adequately evidenced; `PARTIAL` only when genuine foundational self-service is operating but materially incomplete; `NOT_MET` when a foundational violation is demonstrated; otherwise retain `EVIDENCE_LIMITED` and no fabricated characteristic result.
8. Record exact Product/Version, evidence sources, contrary evidence, uncertainty, governance limitations, profile, assessment time, rationale and accountable reviewer.
9. Report independently governed critical assurance issues separately from maturity.

An agent proposes and explains a finding; it does not gain independent institutional decision, policy, Product-family qualification or release authority.

## 12. PMDD scoring treatment

Apply the approved **D03 experimental characteristic-level mapping** only after a defensible finding:

| Finding | Contribution |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |
| Competently established `NOT_APPLICABLE` | Excluded from applicable denominator |
| Unresolved `EVIDENCE_LIMITED` | No manufactured score; D03 bounded uncertainty treatment where denominator established |

IPCH characteristics have equal experimental weights; individual DEP-M criteria are **not** averaged or weighted. No IPCH L0/L1/L2 thresholds, automatic caps or obligation-level aggregation are adopted.

## 13. Critical assurance and governance boundaries

Deployability maturity does not determine whether a Product qualifies as an Information Product, whether its semantic definitions conform, whether it is compliant by design, whether deployment is authorized or whether consequential actions are permitted. Required competent reviews may be synchronous, asynchronous or manual and do not in themselves make self-service deficient. A mandatory technical build/translation dependency is different from a competent approval.

Report any critical governance/assurance concerns under the independent D03 categories. A `MET` result does not override a deployment hold or authorize normative release; a `NOT_MET` result does not automatically establish an institutional prohibition.

## 14. Reassessment and evolution triggers

Reassess on material changes to the authorized Product actor or delegation, informational Promise, lifecycle path, publication/evolution method, implementation abstraction, competent governance steps, actor-facing status/control capability, or evidence currentness. A platform release that removes self-service or introduces a mandatory engineering hand-off can invalidate prior findings. Preserve the historical exact Product/Version, assessment profile and effective time; do not automatically inherit results across materially different realizations.

## 15. Adversarial and boundary cases — First-Pass fixtures

**The following are proposed thought-experiment fixtures, not executed tests:**

| ID | Scenario | Principal boundary |
|---|---|---|
| DEP-A01 | Automated engineer-led deployment | Technical automation ≠ domain self-service |
| DEP-A02 | Domain must author SQL/joins to create its Product | Technical authoring violates intent-native agency |
| DEP-A03 | Low-code portal exposes pipelines, DAGs or compute selection | Engineering disguised as interface |
| DEP-A04 | Domain declares the Promise and platform generates realization, with governed publish and feedback | Candidate MET if all six claims evidenced |
| DEP-A05 | Domain can publish initially, but material updates require engineering backlog | Evaluate foundational versus transitional dependency |
| DEP-A06 | Competent semantic/policy authority must manually approve publication | Approval is not automatically engineering dependency |
| DEP-A07 | Product technically deploys but actor cannot see state/errors or request recovery | DEP-M06 and overall maturity materiality |
| DEP-A08 | Product never deployed to production, but has reproducible pre-production self-service evidence | Evidence proportionality and assessed scope |
| DEP-A09 | Actor can compose informational dependencies by intent, but interoperable contracts are defective | IPCH02 versus IPCH16 independent claims |
| DEP-A10 | Agent executes self-service on behalf of authorized Product actor | Delegation, accountability and actual actor agency |
| DEP-A11 | Product succeeds in one realization pattern but requires manual engineering in another | Exact assessed Product/Version and scope |
| DEP-A12 | Evidence says portal is self-service; operating records show every update needs engineer translation | Contradictory evidence and failure attribution |

No result is inferred from a scenario label. All cases are deferred to the Second Pass for explicit, authorized review.

## 16. Source provenance, open questions and status

### Directly inspected canonical source guidance

- `DPCH.zip/pages/DPCH-PMDD-guidance/02-DPCH02.md`: domain lifecycle self-service, business-native intent, abstraction of technical constructs, engineer dependency failures and partial self-service example.
- `AIPCH.zip/AIPCH-PMDD-guidance/02-AIPCH02.md`: intent-driven AI lifecycle agency, platform abstraction, avoidance of a human engineering translation layer, and distinction between competent governance approval and engineering dependency.

These references establish *source provenance*, not a normative adoption of DPCH/AIPCH requirements into the Information Product family. The source's specific Data/AI implementation vocabulary is not transplanted as mandatory Information Product technology.

### First-Pass decision provenance

- `INFOPS-0.1-IPCH-P01-D11-F01 = APPROVED_EXPERIMENTAL_E0`: source-derived assertion and the six positive, seven negative and six evidence-rule baselines approved for experimental guidance preparation.
- This Markdown is a **prepared draft**, not a subsequent owner decision or completed guide gate. Original D05 authoring order remains historically preserved; the owner-directed First-Pass IPCH01–IPCH16 progression controls current research publishing priorities.

### Open research questions — Second Pass

| Ref | Open question |
|---|---|
| **DEP-R01** | What proves end-to-end lifecycle agency absent production deployment history? |
| **DEP-R02** | Where is the boundary between legitimate human governance review and human implementation dependency? |
| **DEP-R03** | When is partial lifecycle self-service genuinely Partial versus foundationally Not Met? |
| **DEP-R04** | What part of composition belongs to Deployable rather than Interoperable & Composable? |
| **DEP-R05** | How is Product-level lifecycle agency distinguished from successful technical deployment across realization patterns? |

**Status:** `EXPERIMENTAL_DRAFT_PREPARED`; **publication:** `NOT_DEPLOYED`; **individual-guide final approval:** `NOT_APPROVED`; **adversarial and empirical validation:** `NOT_EXECUTED`. All inherited parent MVP, Track B, S04, Q0–Q5, unresolved F06/F14/F16 and 24 open-obligation restrictions remain unchanged. No normative authority or release permission is created.

---

## Enterprise assessment profiles — flexibility without dilution

The enterprise chooses how to implement intent-driven self-service and whether an assessment is human, deterministic, agentic or hybrid. It may require more stringent proof of actor agency, currentness, reproducibility, governance effectiveness and lifecycle scope. It may not waive `DEP-M01–DEP-M06`, treat a mandatory engineer hand-off as self-service, average criteria to disguise a foundational defect, invent a whole-characteristic N/A, or claim equivalent maturity under this guide after substantively weakening the criteria.

**Assessment portability:** record the exact guide revision, enterprise profile/version, Product/Version, authorized actor, lifecycle scope, evidence and counter-evidence, time and reasoned disposition. Different profile stringencies can change evidence-based results; they must remain disclosed.

> **Boundary:** This guide defines *what* Deployable adherence requires and what evidence supports the maturity finding. Enterprise policy determines the rigor of proof, and enterprise engineering determines *how* to realize the capability. Neither may silently dilute the six mandatory claims.
