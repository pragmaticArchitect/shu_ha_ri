# IPCH07 — Reusable: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH07-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Source lineage:** `DPCH07` (Data Product) / `AIPCH08` (AI Product), separately interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D21-F01 = APPROVED_EXPERIMENTAL_E0` (baseline and preparation authorization only)  
> **Guide status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `APPROVED_EXPERIMENTAL_E0` under `INFOPS-0.1-IPCH-P01-D22-F01` (draft acceptance only)  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This guidance is a **proposed, machine- and human-assessable First-Pass draft**, not a conformance certificate, validated maturity threshold or policy permission. The owner retains sole accountable disposition authority within verified competence. The approved D21 baseline is **not** expanded or silently reconciled by this draft. `REU-R01–REU-R08` remain OPEN; `REU-A01–REU-A12` remain proposed and unexecuted. The original D05 dependency-informed sequence remains historically recorded; the owner-directed numerical First Pass governs drafting order without discharging Second-Pass review.

## 1. Characteristic identity and source lineage

| Field | First-Pass value |
|---|---|
| ID / characteristic | `IPCH07 — Reusable` |
| Assessment subject | One exact **Information Product / Version**, within its declared intended scope and consumer contexts |
| Principal sources | `DPCH07 — Reusable` and `AIPCH08 — Reusable`; no family-level authority transfer |
| Approved decision | `INFOPS-0.1-IPCH-P01-D21-F01` (F01.1–F01.16) |
| Mandatory criteria | `REU-M01–REU-M07` — all seven, conjunctive |
| Negative criteria | `REU-N01–REU-N08` |
| Evidence requirements | `REU-ES01–REU-ES07` |
| Challenge register | `REU-A01–REU-A12 = PROPOSED_E0_UNEXECUTED` |
| Research register | `REU-R01–REU-R08 = OPEN` |
| Determinations | D02 `MET`, `PARTIAL`, `NOT_MET`; independent `EVIDENCE_LIMITED` qualifier; authorized `NOT_APPLICABLE`; `NOT_ASSESSABLE` if ineligible |
| Numerical mapping | D03 characteristic-level `MET=1`, `PARTIAL=0.5`, `NOT_MET=0` only |

**Source distinctions are substantive.** DPCH07 argues that a Product must be designed beyond a single predefined consumer and demonstrably adopted across independent contexts; its special-case section nevertheless allows that a narrow regulatory Product *may* satisfy reuse with one consumer if generalized within its legitimate scope. Its general rule still demands independently demonstrated reuse. AIPCH08 requires independent actual adoption and no producer-led bespoke customization; it labels heavy per-consumer customization `NOT_MET`. DPCH07's onboarding edge case labels some producer-coordinated adoption `PARTIAL`. These are **not reconciled**: see `REU-R02` and `REU-R08`.

## 2. What the characteristic really asserts

> **IPCH07 — Reusable:** An Information Product is Reusable when it is intentionally designed as a stable, generalized informational capability that can serve multiple independent consumer contexts within its declared semantic and usage boundaries, and demonstrates actual independent adoption through governed consumption mechanisms without requiring bespoke producer-led redefinition, reconstruction or engineering for each consumer.

**Design enables reuse; independent adoption demonstrates it.** The characteristic has two non-substitutable dimensions: a generalizable informational Product constitution and credible evidence of actual independent use. “Might be reused” is not `MET`. High call volume from one consuming context is not independent adoption. Common underlying data, model, pipeline, calculation engine or dashboard code is not by itself evidence that the **same Information Product** is reused.

Independence refers to the consuming **context**, not necessarily a unique legal entity or technical login: a single enterprise may have multiple independently justified use cases or consuming groups. No fixed number of identities, API calls or domains is an assessment shortcut. A Product may be intentionally narrow, sensitive, pilot-stage or regulatory and still be structurally reusable within its legitimate scope; whether one-consumer exceptions support `MET` remains unresolved (`REU-R02`).

## 3. Information Product specialization

For Information Products, the reusable unit is the **governed informational Promise** together with the applicable meaning, analytical outputs, semantic references, constraints and repeatable consumption contract. Reuse is not simply downstream duplication of a chart, reuse of a physical source dataset or sharing the implementation of an analytic calculation.

An illustrative *Customer Exposure Profile* Product may serve separately justified relationship-management, credit-risk and portfolio-monitoring purposes through the **same Product-level information capability**, provided its semantics remain consistent and consumer configuration stays within governed boundaries. Three teams building separate exposure calculations from one dataset instead represent component/data sharing, not necessarily IPCH07 Product reuse.

Legitimate parameterization — time windows, reporting currency, permitted segment filters, thresholds or display adaptations — is acceptable only if within the existing declared Product contract. A new output Promise, material redefinition of semantics, independent consumer-specific processing or new Product Version may be required if variation exceeds that boundary. Do not infer that a configured consumption is a new Product or that a named “same Product” actually has an unchanged meaning: establish this by evidence.

**DPP relevance:** An applicable Digital Product Passport or other authoritative Product-linked description may provide Product identity, consumption contracts, references, status and provenance useful to demonstrate reuse. This guide does **not** make a DPP implementation a separate mandatory `REU-M` criterion, or infer DPP conformance or actual independent adoption merely from a DPP's presence. Any applicable BPS DPP requirements and Product protocol authority remain independent.

## 4. Assessment subject and authority

Assess a defensibly identified Information Product and **exact Version** at a stated assessment time, with the declared informational Promise, authorized consumers, usage scope and constraints. Separately record:

1. **Product and eligibility:** Product ID, Version, proposed Information Product family and competent D02 eligibility (`EXPERIMENTAL_ELIGIBLE` or separately established normative eligibility). Without eligibility, record `NOT_ASSESSABLE` rather than a characteristic score.
2. **Constitution:** informational Promise, relevant semantic definition and Version, outputs, interfaces, authorized parameterization and material consumer-independent Product assertions.
3. **Adoption contexts:** the independent consuming purpose, organizational/application context where appropriate, authorization status, actual consumption event and period, with identity provenance that avoids counting repeated accounts as distinct contexts.
4. **Consumption behavior:** standard contracts/ports, allowed configuration, whether adoption required producer-led bespoke engineering, re-derivation, separate Product variants or direct producer mediation.
5. **Stability and change:** contract changes, semantic compatibility, broken consumption cases, effective Product Version and relevant consumer impact.
6. **Evidence:** provenance, issuer, timestamp, record/telemetry scope, access restrictions, staleness, counter-evidence and determination authority.
7. **Independent identifiers:** Product/Version, semantic-definition Version, realization revision, compilation identity, runtime occurrence and evidence/determination times must not be collapsed into a single generic “version.”

No IPCH07 finding grants generic Productness, Product-family or Compound qualification, semantic correctness, entitlement, deployment, legal permission, DPP conformance or consequential-action authority. Assessors may report outcomes, not self-authorize those separate determinations.

## 5. Applicability and N/A rules

**Default:** Reusable is applicable to D02-eligible Information Products. No generic whole-characteristic `NOT_APPLICABLE` exemption is established for internal, restricted, niche, regulatory, exploratory, time-limited or currently single-consumer Products. Niche status may determine **scope of legitimate reuse**, but cannot silently erase approved `REU-M03` independent adoption.

- A single-consumer Product designed for independent additional adoption can be `PARTIAL` if the structural evidence is adequate and no foundational failure is established. DPCH07's possible regulatory single-consumer exception is **not converted into an adopted IPCH07 exception** (`REU-R02` OPEN).
- An authorized pilot may lack adoption evidence. Proposed use cases are not consumption events; the assessment may be `PARTIAL` if design-for-reuse is genuinely established, or `EVIDENCE_LIMITED` if the evidence is insufficient to assess it.
- Restricted consumers, sensitive information, legal constraints and authorized access gates do not require open public consumption. The assessor must establish independent adoption **among legitimate potential consumers**.
- If the eligible consumer population is intrinsically singular, record the scope problem and preserve `REU-R02` without automatically declaring `MET` or whole-characteristic `N/A`.
- An exceptional `NOT_APPLICABLE` finding requires affirmative, separately competent D02 applicability authority and rationale; an ineligible Product is `NOT_ASSESSABLE`.

## 6. Distinctness and non-duplication

| Neighbour | Independent maturity claim |
|---|---|
| **IPCH01 — Domain-Owned** | Accountable producer ownership versus actual Product adoption by independent consumers. |
| **IPCH02 — Deployable** | Product Owner's intent-native self-service lifecycle versus downstream consumer-independent repeat adoption. |
| **IPCH03 — Declarative** | Authoritative intent representation and derivability versus demonstrated use beyond the originating context. |
| **IPCH04 — Discoverable** | Independent finding/evaluation versus actual governed consumption across contexts. |
| **IPCH05 — Self-Describing** | Interpretability of Product meaning versus evidence that it was independently adopted. |
| **IPCH06 — Trustworthy** | Current evidence-backed trust posture versus adoption/reuse evidence. |
| **IPCH10 — Addressable** | Identifying/reaching Product/Version versus multiple consumer contexts using that Product. |
| **IPCH11 — Semantically Aligned** | Semantic conformance versus stable meaning as a condition enabling repeated reuse. |
| **IPCH12 — Consumption-Driven Intent** | Evolution responsive to consumer needs versus demonstrated independent adoption. |
| **IPCH13 — Testable & Versioned** | Tests/version discipline versus repeat-consumer contract stability as observed for reuse. |
| **IPCH16 — Interoperable & Composable** | Ability to interoperate/compose versus actual independent adoption. |

`IPCH-NDC-01`: Evidence may be referenced by multiple assessments **only for separate explicit claims**, not copied as conclusive scores. Catalogue visibility is not usage. API stability is not full version governance. Shared Data Product use does not prove Information Product reuse; interoperability does not prove adoption. An IPCH07 `MET` does not imply any neighbouring characteristic is `MET`.

## 7. Core mandatory positive criteria — `MET`

**All seven are mandatory, conjunctive and non-dilutable.** Full adherence requires evidence of **each** applicable claim. No criterion-level mean, partial credit arithmetic, substitute metrics or automatic critical cap.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **REU-M01** | **Generalized Informational Capability** | The Product has an intentionally reusable informational Promise and coherent domain-meaningful capability rather than being constituted solely as one predefined consumer's bespoke deliverable. |
| **REU-M02** | **Consumer-Independent Product Constitution** | Its essential semantics, analytical interpretation, outputs and governing assertions are not structurally coupled to one consumer-specific application, visualization or implementation. |
| **REU-M03** | **Demonstrated Independent Adoption** | Credible actual consumption has occurred across **multiple distinguishable independent consumer contexts**, beyond merely contemplated uses or invocations attributable to one context. |
| **REU-M04** | **No Bespoke Producer Reconstruction** | Additional legitimate consumers adopt the existing Product without requiring producer redefinition of its informational Promise, consumer-specific derivation/pipelines or bespoke Product variants. |
| **REU-M05** | **Governed Repeatable Consumption** | Legitimate consumers can undertake repeatable adoption through defined governed consumption mechanisms without indispensable producer-mediated engineering. |
| **REU-M06** | **Stable Semantic and Consumption Contracts** | Consumption interfaces, semantic definitions, output expectations and material changes are sufficiently governed and stable to support predictable repeat adoption. |
| **REU-M07** | **Product-Level Reuse Evidence Integrity** | Adoption evidence is attributable to the assessed Information Product/Version and separates actual independent Product reuse from shared components, repeated calls, duplicated identities and bespoke deliveries. |

**Qualification:** `REU-M03` retains the approved multiple-independent-context requirement for First-Pass `MET`. Any departure for niche/regulatory scope requires a future explicit competent decision, not an assumed DPCH07 exemption. Incidental documentation/support is distinguishable from essential bespoke engineering; the unresolved severity boundary is preserved under `REU-R08`.

## 8. Core negative criteria — `NOT_MET`

The following are **affirmative failure indicators**, subject to competent evidence. Their existence or severity must be evaluated; they are not a list of unexecuted automatic caps.

| ID | Established negative condition |
|---|---|
| **REU-N01** | Essential Product semantics or outputs are hard-wired to a downstream application or one consumer. |
| **REU-N02** | Each additional consumer requires a bespoke extract, transformation, analytical implementation or producer-built Product variant. |
| **REU-N03** | Claimed Product reuse is only sharing a dataset, model, pipeline or implementation component; the assessed Information Product is not itself adopted. |
| **REU-N04** | Independent reuse is asserted solely as prospective possibility without actual adoption evidence; this **precludes `MET`**, but structural reusability may support `PARTIAL`. |
| **REU-N05** | Adoption fundamentally depends on producer-mediated engineering or recreation of essential informational meaning. |
| **REU-N06** | Uncontrolled semantic/contract/interface change predictably prevents repeatable adoption. |
| **REU-N07** | Multiple-consumer claims actually represent one context, duplicate accounts or repeat invocations rather than independent adoption. |
| **REU-N08** | Material per-consumer variations create divergent Product meanings or constitutions but are represented as reuse of an unchanged Product. |

**Do not confuse absence of evidence with evidence of absence.** A well-established single consumer may establish `REU-N04` only as lack of demonstrated independent adoption; if design-for-reuse is genuinely demonstrated and no foundational failure is proven, the candidate finding remains `PARTIAL`, not automatically `NOT_MET`. If actual consumer logs were not inspected, record `EVIDENCE_LIMITED` instead of inferring zero adoption. If essential bespoke reconstruction is established, it can be a foundational `NOT_MET` even when many consumers exist.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Established condition | Candidate finding | Assessment rationale |
|---|---|---|
| All seven mandatory claims, including independent adoption, are adequately established | `MET` | Demonstrated Product-level repeat adoption without essential bespoke reconstruction. |
| Consumer-independent design demonstrably exists, but one currently verified consumer | `PARTIAL` | Structural reusability present; broader adoption not established; `REU-R02` stays OPEN for niche/regulatory contexts. |
| Two accounts or downstream jobs but one actual consuming context | `PARTIAL` or `NOT_MET` based on design evidence | Duplicate technical identities do not meet `REU-M03`; foundational coupling can support `NOT_MET`. |
| Different contexts consume the same capability without bespoke producer work | Potentially `MET` | Verify Product/Version attribution, contract stability and all seven criteria. |
| Multiple consumers, bespoke Product pipelines or new semantics required for each | `NOT_MET` where essential | Actual multiple consumption does not rescue failed Product abstraction. |
| Producer provides routine documentation or bounded introductory guidance | Context-dependent | Not necessarily bespoke engineering; source tension `REU-R08` remains OPEN. |
| Reuse asserted using a shared underlying Data Product only | `NOT_MET` for claimed Product-level reuse if established | The Information Product itself has not been shown reused. |
| Narrow regulatory Product, one legitimate consumer, generalized standard ports | `PARTIAL` under current First-Pass default | DPCH07 special qualification is unresolved; no silent `MET` waiver. |
| Product has apparently independent consumers, but evidence cannot resolve distinct contexts | `EVIDENCE_LIMITED` | Do not manufacture a scored outcome from ambiguous telemetry. |
| A platform publishes many consumer-specific forks under one marketing name | `NOT_MET` if divergence is material | Common branding is not a common Product constitution. |

`EVIDENCE_LIMITED` is an **independent qualifier**, not a fourth scored maturity level and not a synonym for `PARTIAL`. A proven foundational failure may coexist with uncertainty on subsidiary matters. Record the supported conclusion and qualify its limits. Do not infer `NOT_MET` from a missing document, nor `MET` from the presence of a marketplace badge.

## 10. Evidence signals and sufficiency

Evidence must substantiate **the exact claim**, be attributable, time-bounded where needed and distinguish independent consumer contexts. There is no mandated vendor, repository, telemetry system, minimum API-call count or consumer-identity taxonomy.

| ID | Claim-specific requirement | Examples of relevant evidence | Insufficiency/red flags |
|---|---|---|---|
| **REU-ES01** | Generalized informational Promise and capability (`REU-M01`) | Governed Product definition, intended scope, reusable use-case boundaries | Generic marketing description without a stable Product definition. |
| **REU-ES02** | Consumer-independent Product constitution (`REU-M02`) | Semantic/output contracts, design assertions, reviewed non-coupling evidence | Implementation hard-wired to one downstream format, undocumented custom variants. |
| **REU-ES03** | Independent adoption (`REU-M03`) | Distinct authorized consumers/use-case registrations; attributed usage or adoption events | Multiple logins/call volume from the same context, hypothetical adoption claims. |
| **REU-ES04** | No bespoke producer reconstruction (`REU-M04`) | Onboarding/change records, absence of required bespoke variants, consumer adoption history | Tickets for new per-consumer pipelines, transformations or Product forks. |
| **REU-ES05** | Governed repeatable consumption (`REU-M05`) | Consumer-facing adoption contract, entitlement/request route, repeat onboarding cases | Each use requires essential producer engineering or discretionary re-interpretation. |
| **REU-ES06** | Stable semantics/contracts (`REU-M06`) | Contract revision history, semantic reference versions, relevant compatibility and consumer impact records | Breaking changes or semantic drift not governed across consumers. |
| **REU-ES07** | Product-level, Version-specific adoption integrity (`REU-M07`) | Product IDs in telemetry, consumer-context provenance, Version resolution and case traceability | Only underlying component logs or unidentified aggregation. |

**Sufficiency test:** (a) establish Product identity and eligibility; (b) establish generalization and semantic non-coupling; (c) identify actual independent contexts; (d) show consumption without essential bespoke producer work; (e) verify stable repeatable contracts; (f) tie evidence to Product/Version. The assessor may use a Product passport, catalogue, discovery record or consumption API as supporting evidence, but **DPP presence, listing or endpoint alone cannot demonstrate actual reuse**. Where evidence is only design-time or preproduction, do not invent consumer adoption events; determine whether a bounded `PARTIAL` is defensible or qualify evidence uncertainty.

## 11. Agent-assisted or human assessment decision rule

Apply these decision steps **in order**, maintaining `IPCH-ES-01` evidence lineage and `IPCH-NDC-01` distinctness:

1. **Identify** one exact eligible Product/Version, intended scope, assessment time and competent evidence sources; if not eligible, `NOT_ASSESSABLE`.
2. **Check applicability** using D02. No generic whole-IPCH07 `N/A`; retain any claimed narrow-scope exception as unresolved `REU-R02` absent independent authority.
3. **Establish substantive constitution** against `REU-M01–M02` with appropriate real Product evidence, not marketing or shared-infrastructure claims.
4. **Resolve independent consumption** against `REU-M03` and `REU-M07`: identify distinguishable actual consumer contexts and verify the same Product/Version rather than duplicated accounts or bespoke Products.
5. **Evaluate producer independence and repeatability** against `REU-M04–M06`, distinguishing permitted configuration and incidental guidance from essential reconstruction. Flag `REU-R08` ambiguity rather than making an unauthorized universal ruling.
6. **Inspect affirmative negatives**, including hard-coded coupling, per-consumer forks, producer-built pipelines and uncontrolled semantic changes. Confirm their evidence and materiality.
7. **Determine qualitatively:** `MET` only with evidence for every `REU-M01–M07`; `PARTIAL` when genuine generalizable Product capability is established but bounded non-foundational adoption/repeatability gaps remain; `NOT_MET` for a proven foundational failure; otherwise state supported uncertainty `EVIDENCE_LIMITED`. Do not force unverified source conflicts into a score.
8. **Record evidence provenance** and open conflicts; reference independent control decisions without asserting them; map the resulting characteristic finding to D03 only if assessment eligibility and evidence suffice.

**Compact test:** Is the **same governed Information Product** demonstrably adopted across multiple genuinely independent contexts, by standard repeatable means, without essential per-consumer producer reconstruction or semantic/contract divergence?

## 12. PMDD scoring treatment

Only after an evidence-supported D02 qualitative characteristic determination, the approved D03 experimental mapping is:

| Characteristic determination | Score |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |

Affirmative competent whole-characteristic `NOT_APPLICABLE` may be removed from the applicable denominator under D02/D03; no general IPCH07 exception is established. `NOT_ASSESSABLE` is not scored. `EVIDENCE_LIMITED` separately states uncertainty and may support only D03-permitted bounded scores **where** eligibility/denominator are demonstrable; no guessed facts or automatic assignment.

Equal weighting applies **between applicable characteristics**, not between `REU-M01–REU-M07`. There is no seven-criterion average, no threshold based on number of consumers or call volume, no automatic critical cap, and no IPCH L0/L1/L2 scale. Independent critical assurance restrictions cannot be overridden by a high experimental score.

## 13. Critical assurance and governance boundaries

- **BPS/PIN:** Generic Productness, independently applicable Product-family and Compound determination, and authority for relevant generic Product contracts are unchanged. Reuse of a technical component is not automatic qualification of an Information Product.
- **GEARA/GEARM:** Independent analytical-architecture and semantic meaning/conformance authorities are not delegated to the Reusable assessment. Stable references support reuse claims without granting semantic certification.
- **INFOPROD/INFOPDS:** Product semantic definition and deployment/realization specification remain separate. No new normative descriptor profile or compile contract is created by this guide.
- **DPP:** An applicable Product passport may expose identity, consumption and provenance records. IPCH07 does not itself grant DPP conformance, mandate a new DPP protocol profile, or make DPP presence a proxy for actual independent adoption.
- **Consumer contracts/entitlement:** Legitimate restricted consumption is permitted, but reuse assessment does not grant access approval or relax policy; competent authorities manage identity and rights.
- **PFI/HDIP/realization:** Product realization revisions, compilation, deployment, runtime occurrences and consumption telemetry retain separate identities. Reuse evidence for one Product Version or occurrence is not automatically evidence for another.
- **Legal, control and assurance:** Regulatory/niche scope and permitted consumer population are respected without creating unauthorized maturity exceptions or consequential permissions.
- **Research boundary:** `REU-R02` (narrow/regulatory single-consumer) and `REU-R08` (producer assistance severity) remain OPEN despite any suggestive examples. Proposed cases are not empirical results.

## 14. Reassessment and evolution triggers

Reassess the supported claims when material evidence changes, including:

- emergence of new independently distinguishable consumers or withdrawal of the only external adoption;
- discovery that purportedly independent consumers share a single context or that telemetry double-counted identities;
- evidence of bespoke producer intervention, forks, per-consumer extraction, analytical redefinition or changed authorized parameter boundaries;
- changed Product Promise, semantic definition/Version, reporting period conventions, consumption interface or compatibility behavior;
- Product Version or applicable realization/compilation/occurrence changes impacting evidence attribution;
- changed access policies, regulatory audience/scope or external legal constraints relevant to legitimate consumer independence;
- stale consumption evidence, changed data-retention conditions or new reliability concerns affecting the factual adoption record.

Keep historic results, time-scoped consumption evidence, source identity, prior determinations and reasons for supersession. Product evolution does not retroactively establish adoption in an earlier Version. No universal calendar reassessment interval is prescribed.

## 15. Adversarial and boundary cases — First-Pass fixtures

**All twelve are merely proposed, unexecuted Second-Pass challenges.** They are not empirical findings, a G4/G5/G6 pass or a maturity validation.

| ID | Proposed challenge | Boundary to test |
|---|---|---|
| **REU-A01** | One consumer, clearly generalized Product design | Structural reuse versus lack of actual adoption evidence. |
| **REU-A02** | Several consumer identities, only one consuming context | Real independence and attribution (`REU-M03/M07`). |
| **REU-A03** | Multiple independent consumers adopt the same Product without bespoke producer work | Positive `MET` sufficiency across all criteria. |
| **REU-A04** | Multiple consumers, separately engineered implementations per consumer | Producer reconstruction (`REU-M04`, `REU-N02/N08`). |
| **REU-A05** | Common underlying Data Product; each consumer has a distinct Information Product | Product-level identity versus component sharing. |
| **REU-A06** | Consumers vary reporting parameters under the same governed contract | Legitimate configuration versus Product redefinition. |
| **REU-A07** | Producer provides documentation and introductory advice, but no bespoke engineering | `REU-R08` borderline assistance treatment. |
| **REU-A08** | Producer must reinterpret essential analytical meaning for each consumer | Essential reconstruction and independence failure. |
| **REU-A09** | Standardized regulatory Product with only one legitimate regulator consumer | `REU-R02` narrow-audience/canonical adoption tension. |
| **REU-A10** | Time-bounded experimental Product architected for independent adoption | Pilot scope versus demonstrated reuse. |
| **REU-A11** | Strong aggregate usage metrics; consumer contexts cannot be proven distinct | `EVIDENCE_LIMITED` versus speculative adoption. |
| **REU-A12** | Independently adopted Product experiences breaking semantics across Versions | Repeatability, semantic contract stability and Version attribution. |

`REU-A01–REU-A12 = PROPOSED_E0_UNEXECUTED`. Future assessors must specify hypotheses, Product/Version and acceptance evidence before any execution; this draft itself does not execute challenges.

## 16. Source provenance, open questions and status

**Exact canonical files examined:**

1. `DPCH.zip` → `pages/DPCH-PMDD-guidance/07-DPCH07.md`, **DPCH07 — Reusable**, including “Designed for Reuse and Demonstrably Reused Across Use Cases or Domains”, the refined decision rule, narrow/regulatory/time-bounded section, single-consumer and producer-coordinated edge cases, and its canonical statement.
2. `AIPCH.zip` → `AIPCH-PMDD-guidance/08-AIPCH08.md`, **AIPCH08 — Reusable**, including generalizable capability, independently observed adoption, no producer-led bespoke customization, parameterized-use edge case and its canonical statement. AIPCH08's AI-specific models/agents/behaviour examples are **not** imported as mandatory Information Product mechanisms.
3. `INFOPS-0.1-IPCH-P01-D21-F01`, owner-approved experimental baseline clauses F01.1–F01.16; D02/D03/D04/D05 and First-Pass/Second-Pass authority boundaries retained independently.

**Unresolved research register:**

| ID | Research question | Status |
|---|---|---|
| **REU-R01** | How are distinguishable independent consumer contexts established without equating accounts or invocations with consumers? | OPEN |
| **REU-R02** | How should DPCH07's narrow/regulatory/time-bounded qualification be reconciled with its canonical independent-adoption requirement? | **OPEN — SOURCE TENSION** |
| **REU-R03** | What separates acceptable producer onboarding support from essential bespoke reconstruction? | OPEN |
| **REU-R04** | What Product configuration/parameterization can occur without consumer-specific Product redefinition? | OPEN |
| **REU-R05** | How can evidence distinguish actual Information Product reuse from common Data Product/analytics/implementation reuse? | OPEN |
| **REU-R06** | How should reuse be attributed across Product Versions, semantic-definition versions and different realizations? | OPEN |
| **REU-R07** | How are contract stability and access friction assessed without duplicating IPCH10, IPCH13 or IPCH16? | OPEN |
| **REU-R08** | How should differences between DPCH07 and AIPCH08 for producer-assisted multiple-consumer adoption affect `PARTIAL` versus `NOT_MET`? | **OPEN — SOURCE TENSION** |

**Document status:** `IPCH07-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01 = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; `D22_OWNER_DRAFT_ACCEPTANCE=APPROVED_EXPERIMENTAL_E0`; `PUBLICATION=NOT_DEPLOYED`; `EMPIRICAL_ASSESSMENT=NOT_EXECUTED`; `ADVERSARIAL_VALIDATION=NOT_EXECUTED`; `SECOND_PASS=NOT_STARTED`; `FINAL_GUIDE_APPROVAL=NOT_APPROVED`; `NORMATIVE_RELEASE=NOT_AUTHORIZED`.

**Owner acceptance:** `INFOPS-0.1-IPCH-P01-D22-F01 = APPROVED_EXPERIMENTAL_E0` accepts this sixteen-section experimental First-Pass draft only; it does not discharge Second-Pass review or authorize final approval or release.

**Earlier characteristic obligations:** IPCH01 G4–G6 remain NOT_EXECUTED; IPCH02–IPCH06 outstanding reviews retained. IPCH01–IPCH03 experimental guides confirmed deployed; IPCH04–IPCH06 overlays previously prepared with deployment not confirmed. IPCH08–IPCH16 not initiated.

**Parent programme safeguards retained:** MVP-P01 D01–D08 approved with conceptual design stopped and experimental specification `DRAFT_PREPARED_NOT_VERIFIED`; parent Track B B01 completion `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`; effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE` preserving F01.6/F01.29 and original charter/audit NOT_VERIFIED; historical approvals 65/6/7/7 with separate PC ledger UNCHANGED. Q0–Q5 and F06/F14/F16 UNRESOLVED. G06's 62 approved E0 designs are UNEXECUTED; E1/E2 executions zero; G06-RO01–RO12 and G03-R01–R12 (24 obligations) ALL_OPEN. No independent authority change, repository modification, normative release or IPCH08 work is effected by this artifact.
