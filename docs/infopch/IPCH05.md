# IPCH05 — Self-Describing

**Information Product Characteristic (IPCH) | PMDD maturity guidance**  
**Artifact:** `IPCH05-PMDD-GUIDE-01`  
**Revision:** `FIRST-PASS-DRAFT-01`  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` — D17-F01 approved the First-Pass baseline; D18-F01 accepted this prepared experimental First-Pass draft only. **Deployment, adversarial validation, empirical assessment and final guide approval have not occurred.**  
**Authority:** E0 research and experimental guidance only; no normative Product-family, semantic, DPP-conformance, policy, assurance or deployment approval.  
**Lineage:** `INFOPS-0.1-IPCH-P01-D17-F01` and `INFOPS-0.1-IPCH-P01-D18-F01`; DPCH05 / AIPCH06; IPCH D02–D05; owner-directed First-Pass/Second-Pass strategy.

> **Core assertion:** An Information Product is *Self-Describing* when its governing Product-level description carries sufficient **authoritative, structured and machine-interpretable** information about its informational Promise, analytical meaning, outputs, context, provenance, dependencies, constraints and intended use to enable authorized human and machine consumers to independently understand and evaluate the Product without relying on producer explanations, procedural reverse-engineering or disconnected documentation. The self-description is associated with the exact assessed Product/Version and remains aligned through material Product evolution.

## 1. Characteristic identity and source lineage

- **Characteristic:** `IPCH05 — Self-Describing` (Information Product family).
- **Source DPCH05:** *Rich Metadata Embedded*. Explicit business meaning, explained structure, major provenance/lineage, usage constraints and consumer independence; a schema or storage-level metadata alone is insufficient. The source regards a rich contextual Product page as a possible Met example.
- **Source AIPCH06:** *Rich Capability Metadata Embedded*. Structured, machine-interpretable, Product-bound metadata for purpose, behaviour, constraints, dependencies, usage and independent evaluation, with version alignment. It cites **AIPROD / DPP** as illustrative Product artifacts and **DPP (Digital Product Passport)** as an authoritative evidence signal, *not* as a new mandatory characteristic or automatic proof of maturity.
- **Information specialization:** informational Promise; measures, dimensions, temporal/aggregation interpretations; relevant provenance, analytical assumptions and usage restrictions. AI-specific behaviour, model-card obligations and AI-specific Product-family qualification are not silently imported.
- **Decision status:** D17-F01 approved `SDC-M01–SDC-M07` mandatory conjunctive criteria, `SDC-N01–SDC-N08` negatives, `SDC-ES01–SDC-ES07` evidence, `SDC-A01–SDC-A12` proposed unexecuted cases and `SDC-R01–SDC-R07` OPEN. This draft was separately accepted under D18-F01 for **experimental guidance preparation only**; no final guide approval or validation is implied.
- **Common rules:** D02 eligibility, applicability and independent `EVIDENCE_LIMITED` qualifier; D03 experimental 1/0.5/0 characteristic scores; D04 sixteen-section template (`IPCH-PMDD-GT-01`), evidence `IPCH-ES-01` and nonduplication `IPCH-NDC-01`; historic D05 wave sequence preserved while First Pass proceeds numerically.

## 2. What the characteristic really asserts

Self-Describing does **not** mean that some metadata fields are populated, a schema exists, an attractive dashboard has labels or the producer can explain a report on demand. The relevant Information Product must explain its **own meaning and conditions of interpretation**, using governed Product-bound information rather than tribal knowledge, pipeline inspection or detached presentations.

The requirement is independently meaningful for both human and machine consumers: an authorized consumer should understand the informational purpose, salient output semantics, important derivation context, intended uses and known limits. Machine-assisted evaluation requires structure sufficient for interpretation, query and validation; purely free-form narrative is not enough by itself.

Completeness is contextual and proportionate to the **governing informational Promise**, but context sensitivity is not a discretionary waiver of the seven mandatory claims. A competent assessor identifies which dimensions are materially relevant and examines the Product's actual metadata rather than inferring it from a name or document title.

This characteristic tests faithful, independently interpretable **description**. It does not certify the truth of a represented quality statement, create semantics, qualify a Product family or grant entitlement.

## 3. Information Product specialization

Information can be misleading despite well-labelled technical outputs. A description of *customer profitability* might require measure definition, calculation or analytical interpretation, aggregation grain, time period, currency assumptions, exclusions, origin and limitations. For a different Information Product, different interpretive details may be material. These are **examples**, not mandatory universal field names.

**Product-bound means governed association, not one mandatory physical file.** An authoritative Information Product descriptor (such as an applicable INFOPROD representation), an applicable **Digital Product Passport (DPP)**, or version-resolved Product-associated registry/API metadata may carry or expose the description. Referenced enterprise semantic definitions and provenance records can satisfy a claim when their competent authority, effective version, accessibility and relevance can be established. An ungoverned external slide deck is not equivalent.

**DPP treatment follows AIPCH06's level of articulation:** DPP may carry Product-bound structured meaning, trust or constraint metadata and may be examined as evidence. It is **not** required as a particular implementation, an eighth adherence criterion, a universal schema, a mandatory conformance gate or proof of `MET` merely because a DPP exists. Any independent BPS DPP conformance determination remains under its own authority. Do not presume an INFOPS-specific DPP profile is normatively established.

For interpretation purposes, analytical expressions that define domain meaning (such as a governed measure formula) may be legitimate self-description; procedural implementation code or physical query plans are not substitutes for understandable meaning.

## 4. Assessment subject and authority

Evaluate **one exact Information Product and Version**, as of a defined assessment time and within the authorized consumer/assurance context. Record independently:

1. Product identity/Version, asserted Product family and D02 evidence of actual experimental eligibility (`EXPERIMENTAL_ELIGIBLE`) or separately verified normative eligibility; otherwise `NOT_ASSESSABLE`.
2. The authoritative Product definition and semantic-definition/version references, without treating the assessor as the authority that created them.
3. The Product-bound description(s), how they are resolved, version/effective times and asserted authority.
4. The informational Promise, purpose, scope and contextual business definitions.
5. Relevant outputs/measures, dimensions, units, temporal and aggregation semantics, assumptions and known exclusions.
6. Relevant source provenance, major dependencies and conceptual derivation intent.
7. Declared intended use, limitations, update/freshness and quality expectations, constraints and evidence of relevant currentness.
8. Representative human/machine interpretation mechanism and any contrary, missing, stale or disputed evidence.
9. Separation of Product Version, semantic-definition Version, realization revision, compilation identity and execution occurrence; **do not silently equate them**.

Assessment yields a bounded experimental characteristic finding, **not** Product qualification, an independent semantic adjudication, a DPP certificate, a policy approval, realization conformance or consequential-action authority.

## 5. Applicability and N/A rules

**Default:** Self-Describing applies to any D02-eligible Information Product. No generic whole-characteristic `NOT_APPLICABLE` exception has been approved. Small scope, internal consumption, a single measure, a restricted audience or human-oriented presentation does not itself establish N/A.

Relevant semantic details depend on the actual informational Promise. For example, a non-monetary result need not describe currency treatment, and a non-aggregated event may not require an aggregation specification. That does **not** make SDC-M02 optional; the assessor determines the relevant interpretive dimensions and requires sufficient evidence for them.

A non-applicable *evidence example* (such as DPP not being used) is not a whole-characteristic N/A. A particular metadata technology or artifact is never universally mandatory. Exceptional N/A requires an affirmative competent D02 applicability determination; lack of D02 Product/Version eligibility yields `NOT_ASSESSABLE`, not a maturity score.

## 6. Distinctness and non-duplication

| Neighbour | Independent maturity claim |
|---|---|
| **IPCH01 — Domain-Owned** | Legitimate ownership and control versus independently interpretable Product meaning. |
| **IPCH02 — Deployable** | Governed domain self-service lifecycle versus descriptive sufficiency. |
| **IPCH03 — Declarative** | Authoritative definition from which realization can be derived versus consumer-facing explanation of meaning and interpretation. |
| **IPCH04 — Discoverable** | Ability to find and initially evaluate the Product versus rich Product-bound self-description. |
| **IPCH06 — Trustworthy** | Truth/quality and competent assurance versus accurate *description* of trust claims and limitations. |
| **IPCH07 — Reusable** | Cross-context fitness and actual reuse affordances versus information supporting a consumer's judgement. |
| **IPCH08 — SLA–SLO Backed & Observable** | Operated measurements and observability versus stated expectations or freshness claims. |
| **IPCH10 — Addressable** | Stable identification and reachability versus explanation of what the Product means. |
| **IPCH11 — Semantically Aligned** | Competent semantic conformance versus meaningful disclosure and resolvable semantic references. |
| **IPCH13 — Testable & Versioned** | Actual testing/version governance versus self-description aligned to a Product/Version. |

A Product descriptor, DPP or registry record can support several distinct evidence claims, but cannot make adjacent characteristics `MET` by implication. `IPCH-NDC-01` governs nonduplication. DPP **presence** is neither the definition of Self-Describing nor its own independently scored criterion.

## 7. Core mandatory positive criteria — `MET`

**All seven are mandatory, conjunctive and non-dilutable.** A `MET` finding requires adequate evidence for **each** claim; there are no criterion weights or numerical averaging.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **SDC-M01** | **Authoritative Informational Meaning** | The Product-bound description explicitly explains the informational Promise, analytical purpose, domain concepts, scope and relevant business context using meaningful, governed terms. |
| **SDC-M02** | **Interpretable Outputs and Semantics** | Relevant outputs and measures are explained with sufficient semantic and structural context, including applicable units, dimensions, time meaning, aggregation grain, assumptions and interpretive exclusions. |
| **SDC-M03** | **Provenance and Dependency Transparency** | Material sources, major dependencies and conceptual derivation/transformation context are visible sufficiently to understand the produced information, without requiring technical pipeline disclosure. |
| **SDC-M04** | **Usage Context and Limitations** | Intended uses, material limitations, constraints, freshness or update expectations, quality posture and interpretation boundaries are explicitly represented wherever applicable. |
| **SDC-M05** | **Product-Bound Structured Self-Description** | Authoritative Product-associated description is accessible through governed Product artifacts, registries, APIs or version-resolved references and is sufficiently structured for machine interpretation; **INFOPROD / applicable DPP are possible examples, not mandatory technologies**. |
| **SDC-M06** | **Independent Consumer Interpretation** | Competent authorized human and machine consumers can understand and evaluate relevant Product meaning and suitability from its Product-bound information without producer contact, external explanatory meetings or implementation reverse-engineering. |
| **SDC-M07** | **Version Alignment and Descriptive Integrity** | The description applies to the exact Product/Version, remains governed through material changes and is not demonstrably stale or inconsistent with the Product's current informational definition. |

SDC-M07 does **not** assert that every runtime occurrence has been empirically validated; independently governed realization and execution evidence remains separate. SDC-M06 requires adequate independent interpretation, not that every conceivable consumer persona agrees or that access/consumption has succeeded.

## 8. Core negative criteria — `NOT_MET`

| ID | Affirmatively demonstrated counter-evidence condition |
|---|---|
| **SDC-N01** | Metadata consists mainly of technical identifiers, opaque fields or unexplained abbreviations without adequate informational meaning. |
| **SDC-N02** | Essential business/analytical meaning is obtainable only through producer conversations, disconnected documents or implementation reverse-engineering. |
| **SDC-N03** | Material outputs, measures, time/aggregation semantics or required assumptions are unexplained. |
| **SDC-N04** | Provenance, dependencies or derivation context essential for interpretation is absent, inaccurate or misleading. |
| **SDC-N05** | Material applicable usage limits, intended context, freshness/quality expectations or interpretation boundaries are missing. |
| **SDC-N06** | Metadata is unstructured, unresolvable or otherwise insufficient for meaningful machine-assisted interpretation. |
| **SDC-N07** | The description materially misidentifies the Product/Version, has become stale or contradicts the governing informational definition. |
| **SDC-N08** | Automatically generated technical metadata is treated as complete self-description despite the absence of curated domain meaning or applicable constraints. |

Negative conditions are **evidence-based challenges**, not automatic maturity states. A missing screenshot or unavailable artifact is not proof the Product lacks the described capability. A known failure must be assessed for materiality and whether it defeats the foundational assertion; only actual, adequate counter-evidence supports `NOT_MET`.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Established condition | Candidate classification |
|---|---|
| All seven applicable mandatory claims adequately evidenced, no foundational contradictory evidence | `MET` |
| Genuine Product-bound descriptive capability supports meaningful independent understanding, with evidenced **non-foundational** deficiencies | `PARTIAL` |
| Foundational self-description absent or ineffective (e.g., only raw schema, only producer explanations, or no reliable meaning) | `NOT_MET` |
| Material evidence missing, disputed, stale, insufficient or mutually contradictory | `EVIDENCE_LIMITED` as an **independent evidence qualifier**, not a scored state |
| D02 eligible subject not established | `NOT_ASSESSABLE`; no maturity score |
| Exceptional whole-characteristic inapplicability established under competent D02 authority | `NOT_APPLICABLE`; denominator treatment only as authorized |

**Do not infer `PARTIAL` by counting satisfied mandatory criteria.** Six of seven satisfied is not automatically Partial. A foundational failure cannot be offset by sophisticated metadata elsewhere; likewise a minor genuine shortfall does not necessarily defeat a meaningful Product description.

**Source edge cases, specialized without automatic adjudication:** DPCH05 suggests documented schema with unclear meaning can be Partial, but purely auto-generated metadata lacking semantics is Not Met. AIPCH06 presents rich but non-machine-readable metadata as Partial and complete AIPROD + DPP metadata as Met; in INFOPS, any comparable INFOPROD/DPP case still requires **all seven** SDC criteria and D02 eligibility. Metadata generated automatically **and curated with governed meaning** may satisfy the criterion; automation itself is neither positive nor negative.

**Illustrative non-empirical cases:** a dashboard with excellent visuals and unexplained measures; an INFOPROD-like description that resolves governed semantic references; a DPP with trust metadata but no measure semantics; complete explanatory narrative in disconnected PDFs; a version-resolved Product descriptor coupled with competent semantic/provenance registries. These examples are not executed assessments.

## 10. Evidence signals and sufficiency

| ID | Criterion | Required evidentiary assertion |
|---|---|---|
| **SDC-ES01** | SDC-M01 | The authoritative Product-bound description explains informational Promise, scope, domain meaning and analytical purpose. |
| **SDC-ES02** | SDC-M02 | Applicable outputs, measures and their units, temporal/aggregation and other interpretive semantics are described sufficiently. |
| **SDC-ES03** | SDC-M03 | Material source provenance, major dependencies and conceptual derivation context can be established from authoritative Product-linked information. |
| **SDC-ES04** | SDC-M04 | Appropriate intended use, limitations, freshness/quality posture, constraints and interpretation boundaries are represented. |
| **SDC-ES05** | SDC-M05 | Machine-interpretable self-description is accessible via authoritative Product-bound or version-resolved means, with actual content inspected. |
| **SDC-ES06** | SDC-M06 | A representative intended consumer or competent machine-assisted interpretation can understand/evaluate the Product from the description without producer contact. |
| **SDC-ES07** | SDC-M07 | Description identity, governing effective time and relevant Product/Version alignment and maintenance can be established; no material contradictory drift is known. |

**Potential authoritative evidence** includes an INFOPROD description where independently applicable, Product-bound structured metadata, a **DPP (Digital Product Passport) carrying relevant trust/constraint or descriptive metadata**, or accessible Product metadata from a governed registry/API. This mirrors AIPCH06's *example* treatment. **No DPP schema, deployment, certification or conformance is mandated by IPCH05.** If DPP exists, its actual contents and competent version/authority must be inspected; its mere presence cannot prove any SDC claim.

**Supporting evidence:** version-resolved enterprise glossary/GEARM semantic references, schemas with explanations, lineage summaries, dependency graphs, usage examples, quality/freshness statements, metadata review records, representative consumer interpretation trials. None substitutes for its corresponding mandatory adherence claim.

**Red flags:** storage names presented as semantics, machine-generated descriptions without curated meaning, disconnected slide decks, misleading confidence/trust claims, broken semantic references, obsolete description versions or ambiguous measures.

**Evidence integrity:** register source/authority, exact Product/Version, semantic-definition/version, date/effective time, evidence URI or artifact identity, observation limits and conflicts. Distinguish an artifact's existence from its adequacy and a governance assertion from actual validation. Do not treat evidence absence as proven failure.

## 11. Agent-assisted or human assessment decision rule

1. **Eligibility gate:** Resolve D02 eligibility and exact Product/Version; if not established, return `NOT_ASSESSABLE` with no D03 score.
2. **Applicability gate:** Apply default characteristic applicability; do not infer N/A because a specific schema, DPP or registry is absent.
3. **Evidence inventory:** Identify Product-bound structured description and accessible authority/version-resolved references; identify any applicable INFOPROD or DPP only as potential evidence.
4. **Seven-claim assessment:** Evaluate SDC-M01–SDC-M07 **individually as documentary claims**, recording positive, contrary, missing and disputed evidence without assigning numerical criterion scores.
5. **Counter-evidence:** Challenge SDC-N01–SDC-N08; distinguish genuine foundational failures from uncertainty or lesser deficiencies.
6. **Consumer independence:** Ask whether authorized human and machine evaluation can proceed without producer explanation or code inspection, based on relevant Product-bound context.
7. **Independent authority check:** Do not substitute the assessor's judgement for competent semantic, qualification, policy, trust, DPP or realization authorities.
8. **Finding:** Issue `MET`, `PARTIAL` or `NOT_MET` only where defensible; otherwise retain an `EVIDENCE_LIMITED` qualifier and unresolved issues as required by D02. Preserve time, scope and competent decision-maker.
9. **Score after finding:** Use D03 at *characteristic* level only; do not derive a score from seven individual binary values.

**Simplified source-aligned challenge:** Can a competent intended consumer independently determine what the Information Product means and how its outputs should be interpreted and used from its governed structured Product-bound description? If not, identify whether demonstrable absence, partial capability or evidentiary uncertainty is the reason.

## 12. PMDD scoring treatment

The D03 experimental mapping applies **only after** eligibility and the defensible characteristic-level finding:

| Characteristic finding | Experimental D03 value |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |

Under D03, characteristics are equally weighted in the experimental aggregate; an affirmatively justified `NOT_APPLICABLE` may be excluded from the denominator under competent D02 rules. `EVIDENCE_LIMITED` is an independent qualification and is **not** a fourth numerical maturity level; incomplete denominator/evidence affects score certainty and may require bounds or withholding a definitive composite result. `NOT_ASSESSABLE` yields no IPCH05 score.

There are **no seven-criterion weights, criterion-level averages, new critical caps or IPCH L0/L1/L2 bands**. Independent critical assurance/qualification is not inferred from a favourable PMDD score.

## 13. Critical assurance and governance boundaries

- **BPS/PIN** owns generic Productness and applicable family/Compound authority; IPCH05 cannot qualify an Information Product by itself.
- **GEARM** governs semantic definitions and relevant semantic versions; IPCH05 tests descriptive accessibility and faithful reference to those semantics, not independent semantic correctness.
- **GEARA** retains analytical architecture authority; Product-bound explanation is not architecture certification.
- **INFOPROD / INFOPDS** retain distinct Product-definition and realization/deployment-specification boundaries where independently established. Mentioning artifacts does not promote a research draft to a normative schema.
- **DPP (Digital Product Passport):** AIPCH06 uses DPP as an example of Product-bound structured metadata and potential evidence, not as a self-description compliance criterion. Applicable BPS DPP specifications/conformance remain independently governed. No new INFOPS DPP profile is authorized here.
- **PFI/HDIP, DPP, policy, legal, entitlement, trust and assurance** assertions remain under competent independent controls. Publication or description of a claim does not prove it.
- **Product/Version vs semantic version vs realization revision vs compilation vs occurrence:** preserve exact subject/effective-time separation and evidence lineage. Description may refer to a realization but cannot certify its execution.
- **Scope of approval:** D17 approved a bounded experimental baseline. This guide preparation neither executes parent G06 E0 designs nor establishes Track B/S04 authority.

## 14. Reassessment and evolution triggers

Reassess the same exact Product/Version or initiate the appropriate new Product/Version assessment when there is relevant change in:

- Information Product Promise, intended audience, analytical scope, measure definitions, dimensions, grain, units, temporal meaning or calculation interpretation.
- Source provenance, major dependencies, conceptual derivation, limitations, usage constraints or asserted quality/freshness posture.
- Referenced semantic definitions/versions, lineage records or their governed resolvability.
- Product-bound descriptor, registry/API, INFOPROD-like artifact or applicable DPP evidence currentness or availability.
- Actual description-to-definition correspondence, including demonstrated material drift or contradictory Product/Version identity.
- Assessor evidence profile, competent authority record or newly discovered adverse information.

Do not silently carry a `MET` finding from one Product/Version to a successor or from a textual guide to a realized runtime occurrence. Record the new assessment time, subject and source evidence. Reassessment is research guidance, not authorization to execute release workflows.

## 15. Adversarial and boundary cases — First-Pass fixtures

**The following are proposed research fixtures ONLY (`SDC-A01–SDC-A12 = PROPOSED_E0_UNEXECUTED`). Their presence in this document does not mean they have been exercised, passed or validated.**

| Case | Future challenge | Principal boundary to test |
|---|---|---|
| **SDC-A01** | Schema complete; business meaning absent | Structure is not informational meaning. |
| **SDC-A02** | Rich narrative exists only in detached documentation | Human documentation versus governed Product-bound metadata. |
| **SDC-A03** | Product descriptor resolves competent semantic-registry references | Product-bound authoritative reference versus physical embedding. |
| **SDC-A04** | Semantic link points to wrong ontology version | Resolvability, authority and Product/Version alignment. |
| **SDC-A05** | Measures defined but aggregation grain ambiguous | Material output interpretability. |
| **SDC-A06** | Provenance available only in technical pipeline logs | Conceptual provenance independent of reverse-engineering. |
| **SDC-A07** | Conceptual provenance complete without physical pipelines | Non-prescription of implementation details. |
| **SDC-A08** | Auto-generated metadata lacks curated meaning | Automation versus adequate semantic description. |
| **SDC-A09** | Description current but realization differs materially | Product meaning versus independently governed realization. |
| **SDC-A10** | Machine-readable descriptor is unintelligible to relevant humans | Dual human/machine interpretability. |
| **SDC-A11** | Product self-describes well but is undiscoverable | IPCH05 versus IPCH04 distinctness. |
| **SDC-A12** | DPP or Product description asserts unverified trustworthiness | Evidence of description versus independent trust/assurance. |

Suggested future adversarial procedure: record exact evidence, independently assess mandatory claims, challenge contrary records, preserve unresolved authority conflicts and obtain accountable owner disposition. **No such procedure is executed by this draft.**

## 16. Source provenance, open questions and status

**Primary source artifacts directly read:**

- `DPCH.zip` → `pages/DPCH-PMDD-guidance/05-DPCH05.md`, **DPCH05 — Self-Describing**, *Rich Metadata Embedded*. Source claims about business meaning, explained structure, lineage, context, consumer independence and technical-only metadata were inherited as specified above.
- `AIPCH.zip` → `AIPCH-PMDD-guidance/06-AIPCH06.md`, **AIPCH06 — Self-Describing**, *Rich Capability Metadata Embedded*. Source claims about structured/machine-readable Product-bound metadata, version alignment and **AIPROD / DPP examples** were inherited at their original level. Its AI-specific obligations were not transposed as Information-family normative requirements.
- Owner-approved `INFOPS-0.1-IPCH-P01-D17-F01` (F01.1–F01.16); earlier D02–D05 experimental assessment/guidance decisions. This draft does **not** represent a new D17 amendment or approval.

**Research questions — ALL OPEN for Second Pass:**

| ID | Unresolved research question | Status |
|---|---|---|
| **SDC-R01** | Minimum sufficient Information Product description across informational/analytical patterns? | OPEN |
| **SDC-R02** | When do authoritative, version-resolved external semantic references satisfy Product-bound description rather than external-document dependence? | OPEN |
| **SDC-R03** | Minimum machine interpretability without mandating one metadata technology? | OPEN |
| **SDC-R04** | Boundary among Self-Describing, Declarative and Semantically Aligned? | OPEN |
| **SDC-R05** | Description/realization drift where Product definition and runtime occurrences differ in effective time? | OPEN |
| **SDC-R06** | Foundational `NOT_MET` versus `PARTIAL` for mixed machine/human description? | OPEN |
| **SDC-R07** | Evidence of independent consumer understanding without arbitrary universal persona testing? | OPEN |

**No `SDC-R08` is created** for DPP; DPP is treated exactly as a potential Product-bound representation and evidence example, following AIPCH06.

**Version/status:** `IPCH05-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01 = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` under D18-F01. `OWNER_DRAFT_ACCEPTANCE=APPROVED_EXPERIMENTAL_E0`; `PUBLICATION=NOT_DEPLOYED`; `EMPIRICAL_ASSESSMENT=NOT_EXECUTED`; `ADVERSARIAL_VALIDATION=NOT_EXECUTED`; `SECOND_PASS=NOT_STARTED`; `FINAL_GUIDE_APPROVAL=NOT_APPROVED`; `NORMATIVE_ADOPTION=NOT_AUTHORIZED`.

**Preserved programme holds:** IPCH01 G4–G6 unexecuted; IPCH02–IPCH04 reviews outstanding (IPCH04 overlay packaged, deployment not confirmed); D01–D17 preserved. Parent MVP-P01 D01–D08 approved but draft not verified; Track B B01 completion NOT_ESTABLISHED and B02–B06 NOT_AUTHORIZED; effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE` with F01.6/F01.29 safeguards; historical ledgers 65/6/7/7 and separate PC unchanged; Q0–Q5 and F06/F14/F16 unresolved; G06 62 approved E0 designs unexecuted; E1/E2 executions zero; G06-RO01–RO12 and G03-R01–R12 (24 obligations) OPEN. No repository modification, IPCH06 initiation or normative release is effected.
