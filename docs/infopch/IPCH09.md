# IPCH09 — Compliant by Design: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH09-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Source lineage:** `DPCH09` (Data Product) / `AIPCH10` (AI Product), separately interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D25-F01 = APPROVED_EXPERIMENTAL_E0` (baseline and preparation authorization only)  
> **Guide status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `APPROVED_EXPERIMENTAL_E0` under `INFOPS-0.1-IPCH-P01-D26-F01` (draft acceptance only)  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This sixteen-section guidance is a **draft experimental characteristic assessment**, not a certification of legal compliance, proof of an implemented policy platform, Product-family qualification or evidence of executed Product controls. D25 accepted the **criteria baseline**; D26 subsequently accepted this completed guide **as an experimental First-Pass draft only**, not as final guide approval or normative release. The accountable human owner alone supplies experimental dispositions within verified competence; AI drafting does not confer policy, legal, compliance or institutional governance authority. Earlier D05 ordering is historically preserved while the First-Pass numerical order governs this authoring exercise. All research questions remain OPEN and all adversarial cases remain PROPOSED_E0_UNEXECUTED.

## 1. Characteristic identity and source lineage

| Field | Experimental First-Pass value |
|---|---|
| Characteristic | `IPCH09 — Compliant by Design` |
| Guide | `IPCH09-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01` |
| Assessment subject | One exact eligible Information Product/Version, its declared informational Promise, applicable policy authority, control bindings, consumption paths and effective assessment interval |
| Principal sources | `DPCH09 — Compliant by Design` and `AIPCH10 — Compliant by Design` |
| Owner-approved criteria baseline | `INFOPS-0.1-IPCH-P01-D25-F01` clauses F01.1–F01.16 |
| Mandatory criteria | `CBD-M01–CBD-M08`, **all conjunctive** for `MET` |
| Negative criteria | `CBD-N01–CBD-N09` |
| Evidence requirements | `CBD-ES01–CBD-ES08` |
| Research | `CBD-R01–CBD-R08 = OPEN` |
| Adversarial cases | `CBD-A01–CBD-A12 = PROPOSED_E0_UNEXECUTED` |
| Findings | D02 `MET`, `PARTIAL`, `NOT_MET`; separate `EVIDENCE_LIMITED`; competent `NOT_APPLICABLE`; ineligible `NOT_ASSESSABLE` |
| Scoring | D03 characteristic-level `MET=1`, `PARTIAL=0.5`, `NOT_MET=0`; no averaging of mandatory criteria |

**Directly inspected lineage:** `DPCH.zip → pages/DPCH-PMDD-guidance/09-DPCH09.md` and `AIPCH.zip → AIPCH-PMDD-guidance/10-AIPCH10.md`. These are the primary source inputs, not evidence that all adjacent INFOPS, legal or policy authorities have been independently verified.

**DPCH09:** federated computational governance as **Global → Divisional → Domain → Product**; applicable policies visible to the DPRO at design time, bound through testing, deployment and publication, enforced computationally at runtime. Product-specific constraints cannot override higher-level policy. Its example of app-only RBAC is `Partial`; centrally applied policies after deployment are `Not met`. It identifies optional DPP trust-section linkage as supporting evidence.

**AIPCH10:** federated **Global → Domain → Product**; policies declared alongside AI Product intent, bound in creation/compilation, enforced automatically and consistently across consumers, with observable violations. Its high-risk human-oversight edge case is `Met` **if** oversight is part of policy enforcement, not a replacement for controls. Incomplete policy enforcement is `Partial`. AI-specific risk tiers, fairness and model-safety examples do **not** automatically become universal Information Product obligations.

**Unresolved source distinctions:** The four-layer versus three-layer representations do not establish a universally compulsory organizational hierarchy (`CBD-R01`); integrated human governance versus manual replacement of enforcement requires case-specific reasoning (`CBD-R02`). Both remain OPEN. The common canonical core is design-visible, Product-bound, machine-interpretable and enforced policy-as-code.

## 2. What the characteristic really asserts

> **IPCH09 — Compliant by Design:** An Information Product is Compliant by Design when all applicable governance, regulatory, access, information-handling and usage constraints are determined through competent federated policy authority, made visible during Product design, bound to its governed definition and lifecycle, and enforced consistently through machine-interpretable, executable controls across applicable consumption and runtime interactions, with violations detectable and attributable.

Authorized human governance decisions may participate in the control mechanism where required, but cannot substitute for otherwise mandatory computational enforcement.

The claim is about **compliance embedded in design and runtime enforcement**, not a report that the Product passed a compliance review. It requires three separable facts: applicable obligations and competent authority are established; policies are visible and bound to the Product; and controls actually execute across relevant paths. A compliance document or policy descriptor without enforcement is not enough. A technical permit decision alone does not establish substantive legal compliance.

For an Information Product, the applicable policy scope must reflect the *resulting informational capability*, including new constraints created by joining, aggregating, interpreting, redistributing or deriving information. Its underlying Data Products' controls remain relevant but are not sufficient merely by existence. Information-specific restrictions may include, **where applicable**, classification, privacy, legal basis, purpose, residency, retention, consumer entitlements, masking, disclosure, export and consequential-use limitations. Neither this list nor a particular policy taxonomy is universally mandatory.

## 3. Information Product specialization

An Information Product may produce a new interpretation, consolidated indicator, assessment, narrative or decision-support result from multiple sources. Governing that result is not reducible to the governance of each source independently. Determine whether competent policy authorities have specified constraints on **the produced information and its use**, as well as on sources and mechanisms. For example, an aggregated liquidity exposure report may combine lawfully available inputs yet create restricted client concentration information; the entitlement and permitted-use constraints for that derived output must be independently assessed and enforced as applicable.

Information Products may be realized through reports, scheduled releases, analytical APIs, subscriptions, conversational analytical interfaces or other paths. The assessment must identify **all applicable consumption and realization boundaries** and test the actual effect of controls, not assume that an upstream access check propagates automatically. Different ports may implement a common policy through different technical means; enforcing equivalent applicable obligations is the requirement, not one mandatory vendor platform.

The Product Owner can propose Product-specific conditions and choose among permitted alternatives where the competent governance model allows. The owner may **not** nullify a higher-level obligation by introducing a local policy. Information-specific analytical semantics and applicability remain under independently competent GEARA/GEARM, legal, policy, privacy, information-security or domain authority, not determined autonomously by the IPCH09 assessor.

**DPP boundary:** An applicable DPP, Product descriptor or other governed evidence carrier may reference policy sets, obligations, control evaluations or a compliance posture. This may support `CBD-ES03` or related evidence, but does not by itself establish that controls execute or that legal compliance has been determined. **No universal DPP conformance or implementation requirement is added.**

## 4. Assessment subject and authority

Before making any finding, establish and keep separate:

1. **Exact Product/Version and eligibility.** The independently qualified Information Product identity, version, declared intent and scope of its D02 assessment. If eligibility is unestablished, use `NOT_ASSESSABLE` rather than a maturity score.
2. **Applicable obligations and competent issuers.** Identify relevant jurisdiction, information classification, consumer roles, permitted purposes, enterprise/divisional/domain/Product policy, supersession/precedence and effective dates. The maturity assessor does not invent law, policy or waiver authority.
3. **Design-time view.** Determine what applicable policies and legitimate choices were visible to the authorized Product Owner/delegate before design or evolution decisions became effective.
4. **Product-bound control definition.** Identify declared policy set, entitlement/usage binding, Product/Version relationship, structured policy representation and relevant policy/evaluator versions. Separate definition from execution.
5. **Runtime and consumer paths.** Identify ports, access routes, derived outputs, realizations and materially equivalent consumption surfaces, including routes that might bypass controls.
6. **Enforcement results.** Gather actual policy decisions, controlled-denial evidence, relevant positive and negative test outcomes, violation signals and escalation context; preserve whether evidence is observed or merely specified.
7. **Governed lifecycle and identities.** Distinguish Product/Version; semantic definition/version; policy set/version; Product description/binding; realization revision; compilation identity; runtime occurrence; evaluation outcome; evidence issuer and time.
8. **Uncertainty and authority limits.** Explicitly record inaccessible telemetry, stale evidence, policy applicability disputes, contradictions, limits of coverage and competent outstanding decisions. Evidence is not replaced by a presumed compliance posture.

The accountable owner decides only on experimental research dispositions within verified competence. Legal applicability, valid policy exceptions, security control sufficiency, entitlement decisions, Production authority and consequential actions remain with the independently competent actors and mechanisms.

## 5. Applicability and N/A rules

**Default:** IPCH09 applies to every D02-eligible Information Product. An internal, exploratory, narrowly distributed, low-risk, batch or non-real-time Product is **not automatically exempt** from applicable policy governance and enforcement. The actual obligations and proportionate control mechanisms vary by legitimate scope, not the requirement to establish and enforce those obligations.

- A Product with no special sensitivity still requires proof of the applicable general governance and usage controls, including an authoritative determination when a particular specialized control is inapplicable.
- A lawfully required human approval can be part of an executable mechanism when its recorded outcome is enforced. This is not an exemption from computational controls, nor authorization for the assessor to approve the human decision.
- Where a specific control does not apply, record the competent basis and reason. **Control-level non-applicability does not imply the entire IPCH09 characteristic is `NOT_APPLICABLE`.**
- A proposed E0 control architecture, policy bundle or DPP declaration without executed controls does not justify `MET`.
- Assess the applicable historical interval and Product/Version; control evidence in one realization is not assumed valid for all realizations or later Versions.
- Whole-characteristic `NOT_APPLICABLE` requires an **affirmative competent D02 decision**, not insufficient evidence or an assessor's preference. If the Product is ineligible, use `NOT_ASSESSABLE`.

## 6. Distinctness and non-duplication

| Adjacent characteristic or authority | Boundary retained for IPCH09 |
|---|---|
| IPCH01 — Domain-Owned | Accountable Product ownership is distinct from correct enforcement of policies. |
| IPCH02 — Deployable | Lifecycle agency/self-service is distinct from the policy authorization that constrains deployment and use. |
| IPCH03 — Declarative | Declarative intent is not proof that applicable controls are executable and enforced. |
| IPCH05 — Self-Describing | Published restrictions or conditions are not equivalent to enforcement. |
| IPCH06 — Trustworthy | Trust evidence and posture are separate from execution of substantive applicable policy controls. |
| IPCH08 — SLA–SLO Backed & Observable | Observation of policy-related signals is distinct from actual policy evaluation and enforcement. |
| IPCH10 — Addressable | Stable identity and access mechanism are distinct from authorized access and usage. |
| IPCH11 — Semantically Aligned | Competent semantic conformance defines meaning; policy claims may reference those semantics without usurping authority. |
| IPCH13 — Testable & Versioned | Test/version governance differs from lifecycle integrity of applied policy sets and enforced changes. |
| IPCH16 — Interoperable & Composable | Composability does not remove enforcement obligations across combined Product contexts. |
| BPS/PIN and Product-family authorities | Generic Productness and Information Product qualification are independent eligibility requirements. |
| GEARA/GEARM | Analytical architecture and semantic interpretation remain independently governed. |
| DPP and INFOPROD/INFOPDS | Product/evidence/description carriers are not equivalent to actual executable policy decisions. |
| PFI/HDIP and realization | Implementing a mechanism does not confer legal/policy authority or make the Product compliant by assertion. |

**No circular certification:** An IPCH09 assessor cannot declare legal compliance from a policy engine's `ALLOW` or from a trust badge. The evaluator must establish that the **competently issued applicable obligation** is represented and enforced; it cannot independently decide that the underlying obligation is legally correct or waive it. IPCH06/IPCH08 evidence may be reused for specifically justified facts only, not borrowed as a conformance verdict. A policy-evaluation log demonstrates the decision taken, not necessarily the legal validity of its policy version.

## 7. Core mandatory positive criteria — `MET`

**All eight criteria are necessary, conjunctive and non-dilutable.** An evidence-backed finding on one cannot substitute for absence of another. No mandatory-criterion weights, means, automatic caps or maturity bands are authorized.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **CBD-M01** | **Federated Policy Authority and Applicability** | Applicable policies are determined from competent enterprise/global, divisional where applicable, domain and Product governance authorities; higher-order constraints cannot be overridden by unauthorized Product choices. |
| **CBD-M02** | **Design-Time Policy Visibility** | The authorized Product Owner/delegate can inspect applicable policy obligations, their relevant rationale and legitimately available decisions while defining or evolving the Product. |
| **CBD-M03** | **Product-Bound Declarative Controls** | Applicable policy sets, classifications, entitlements and usage restrictions are explicitly and traceably bound to the assessed Product/Version throughout its governed lifecycle. |
| **CBD-M04** | **Machine-Interpretable Executable Policies** | Applicable control obligations are represented in computationally interpretable and executable form, without a required manual translation or bespoke per-consumer engineering step for each enforcement context. |
| **CBD-M05** | **Automatic Runtime Enforcement** | Applicable policy and entitlement controls actually execute at the relevant access, information processing, delivery and consumption boundaries, rather than relying on documentary compliance claims. |
| **CBD-M06** | **Consistent Product-Level Control Coverage** | Controls remain effective across all applicable consumer interfaces, derived outputs and realization paths, with no material ungoverned bypass; uniform underlying technology is not compulsory. |
| **CBD-M07** | **Governed Product-Specific Constraints and Lifecycle Integrity** | Authorized Product-specific restrictions can be declared and evolved within higher-order policy bounds, and required enforcement bindings remain intact through test, publication, change and realization. |
| **CBD-M08** | **Violation Detection and Enforcement Evidence** | Material policy violations and control decisions can be detected, attributed and evidenced, with suitable enforcement, escalation or competent human oversight when applicable. |

**Conjunction versus maturity uncertainty:** For `MET`, affirmative evidence for each criterion is necessary. A missing, uncertain or contradictory evidence item is not by itself proof of `NOT_MET`; the full D02 assessment must separately qualify sufficiency and established deficiency. `CBD-R07` holds unresolved finer distinctions involving incomplete computational enforcement and `PARTIAL`/`NOT_MET` boundaries.

## 8. Core negative criteria — `NOT_MET`

Each is an **adverse indicator where demonstrated**. They do not function as mechanical scoring caps or transform a missing document automatically into proof of failure.

| ID | Established counter-indicator |
|---|---|
| **CBD-N01** | Applicable policies are hidden from Product design actors until after relevant design, implementation or publication decisions. |
| **CBD-N02** | Compliance principally relies on policy documents, checklists, attestations, manual reviews or sign-offs instead of executable controls. |
| **CBD-N03** | Required policy bindings are absent, incomplete or cannot be reliably related to the exact Product/Version. |
| **CBD-N04** | Documented access, usage, privacy or handling restrictions are not enforced computationally when applicable. |
| **CBD-N05** | Enforcement is delegated to selected consuming applications or interfaces and materially equivalent access paths bypass controls. |
| **CBD-N06** | A Product-specific rule effectively overrides a higher-order obligation without competent authority. |
| **CBD-N07** | Applicable information-specific restrictions arising from derivation, aggregation, release or disclosure are not evaluated or enforced. |
| **CBD-N08** | Lifecycle changes produce ungoverned or stale policy bindings, unenforced Product states or unexamined realization paths. |
| **CBD-N09** | Material enforcement decisions or violations cannot be detected, attributed or evidenced as required for the applicable governance obligation. |

Examples of source-grounded failure include DPCH09 policies applied centrally only **after deployment**, or AIPCH10 policies described in documentation but not implemented in runtime policy checks. AIPCH10 also treats genuinely **incomplete enforcement** as potentially `Partial`; therefore do not assume that any single negative indicator always determines `NOT_MET` without examining the substantive foundational versus non-foundational deficiency under D02 and `CBD-R07`.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Circumstance | Candidate First-Pass handling | Necessary qualification |
|---|---|---|
| Policies visible, Product-bound, executable and enforced across all material paths; evidence of applicable violations and decisions | Potential `MET` | Must affirmatively support **CBD-M01–M08**, not just illustrative conditions |
| Only application-level RBAC protects a Product; no demonstrated Product-level federated constraints | `PARTIAL` in DPCH09's specific edge case; more severe finding possible in INFOPS if foundational Product-level enforcement is demonstrably absent | Preserve source case and `CBD-R07`; no automatic transfer of outcome |
| Genuine policy-as-code controls operate but a bounded non-foundational control dimension is incomplete | Potential `PARTIAL` | AIPCH10's incomplete coverage example; test materiality and Product applicability |
| Policies are applied only after deployment | `NOT_MET` when proven | The design-time and lifecycle claims fail fundamentally |
| Product relies solely on manual tickets or after-the-fact sign-offs for enforcing mandatory use conditions | `NOT_MET` when proven | Manual substitute for executable enforcement |
| Legitimate human approval is captured in and enforced by a policy mechanism | Potential `MET` | Other criteria must be evidenced; source AIPCH10 high-risk example is not a universal exemption |
| Derived output violates an applicable restriction even though every source is separately guarded | `NOT_MET` for proven foundational enforcement gap | Determine competent obligation and actual failure |
| DPP asserts compliance but no independent runtime enforcement records are available | `EVIDENCE_LIMITED` unless stronger failure evidence exists | Descriptor assertion cannot prove execution |
| Selected consumers are controlled while a material equivalent interface bypasses the restriction | `NOT_MET` where demonstrated | Actual Product-level enforcement failure |
| Control evidence has inconsistent Product/Version or policy-version attribution | `EVIDENCE_LIMITED` or substantiated failure based on facts | No blanket presumption |
| Applicability of a jurisdictional rule is disputed between competent authorities | `EVIDENCE_LIMITED` on that unresolved claim | An IPCH assessor must not adjudicate law |

`MET`, `PARTIAL` and `NOT_MET` remain findings about established characteristic adherence, **not** confidence ratings. `EVIDENCE_LIMITED` is a separately recorded qualifier for uncertainty. `NOT_APPLICABLE` needs competent affirmative D02 authority; `NOT_ASSESSABLE` reflects missing D02 subject eligibility. The precise line between meaningful-but-incomplete computational enforcement and foundational failure remains `CBD-R07 = OPEN`.

## 10. Evidence signals and sufficiency

Evidence is assessed for **identity, authority, applicability, observed enforcement, coverage, time and provenance**. Descriptors and control designs establish intent and binding; runtime audit/decision evidence establishes actual operations. Neither alone automatically proves the whole characteristic.

| ID | Criterion | Claim-specific evidence expectation |
|---|---|---|
| **CBD-ES01** | CBD-M01 | Competent policy authority map, applicable obligations, precedence, inheritance and permitted Product-specific additions. |
| **CBD-ES02** | CBD-M02 | Evidence of applicable policy visibility, relevant rationale and permitted choices during Product intent/design or evolution. |
| **CBD-ES03** | CBD-M03 | Traceable Product/Version-specific policy set, classifications, entitlement model, usage restrictions and applicable lifecycle associations. |
| **CBD-ES04** | CBD-M04 | Structured executable policy definitions, interpretable control rules, policy versions and governed evaluation mechanisms. |
| **CBD-ES05** | CBD-M05 | Actual runtime policy evaluations, authorization/denial outcomes, control execution records or valid observed enforcement tests for material interactions. |
| **CBD-ES06** | CBD-M06 | Coverage analysis and substantiating evidence across applicable ports, consumers, derived outputs and realization paths, including material bypass tests. |
| **CBD-ES07** | CBD-M07 | Governed Product-specific additions, higher-order non-overriding checks and lifecycle propagation/change evidence. |
| **CBD-ES08** | CBD-M08 | Attributable violation records, policy decisions, relevant audit/monitoring signals and enforcement or competent escalation events. |

**Authority qualification:** Validate issuer, policy version, authorization to enact rules, Product/Version reference, realization/occurrence, time windows, enforcement scope and limitations. A control decision record is not by itself a legal opinion. A policy registry entry does not prove the evaluator used the correct version. A negative test result with unclear scope is not universal evidence of enforced policy.

**Possible evidence carriers:** policy registry, governed policy bundle, Product descriptor, entitlement configuration, runtime policy evaluation log, conformance test, access-denial trace, information disclosure check, change audit, policy version lineage or governed DPP reference. The **claim** is mandatory; no particular carrier, vendor or portal implementation is mandated by the experimental criteria. Design/compilation plans and unexecuted E0 artifacts may support design-intent claims only, not executed enforcement claims.

## 11. Agent-assisted or human assessment decision rule

Apply in order, preserving artifacts, authority and evidence separately:

1. **Eligibility:** Establish the precise Product/Version and D02 status. If subject eligibility has not been independently established, return `NOT_ASSESSABLE` with reasons, not an invented score.
2. **Applicability:** Obtain competent policy determination for jurisdiction, classification, information lineage, derived obligations, consumer contexts and usage restrictions. Do not invent exemptions.
3. **Authority/precedence:** Evaluate `CBD-M01` and `CBD-M07` without treating the assessor, owner or Product descriptor as autonomous policy authority.
4. **Design and Product binding:** Establish `CBD-M02`, `CBD-M03`, `CBD-M04` using design-time evidence, policies, Product/Version bindings and executable rules.
5. **Executed operation:** Independently verify `CBD-M05`, `CBD-M06`, `CBD-M08` against applicable runtime/consumption paths, observed decisions, violation signals and material control outcomes.
6. **Counterevidence:** Test `CBD-N01–CBD-N09` as evidence-based challenges, noting what is demonstrated versus merely unobserved.
7. **Uncertainty:** Record each evidence gap, contradiction, staleness, version mismatch and legal/policy dispute separately. Use `EVIDENCE_LIMITED` as a qualifier; do not silently assume satisfaction or failure.
8. **Finding:** `MET` only if all eight M claims are affirmatively evidenced. Consider `PARTIAL` for real but incomplete computational governance without proven foundational absence, `NOT_MET` for demonstrable foundational failure, and carry unresolved `CBD-R07` boundary cases explicitly.
9. **Scoring:** Apply D03 *only* to an adequately established characteristic finding; do not arithmetically average CBD-M claims.
10. **Record:** Keep the authority-derived requirement set, Product/Version, policy/semantic/realization/occurrence versions, assessment time, evidence references and human disposition distinctly traceable.

**Do not** execute controls, grant entitlements, amend policy, declare legal conformance, publish a normative Product assessment or initiate adversarial replay merely by following this guidance. Such activities require separate competent authority and actual evidence.

## 12. PMDD scoring treatment

| D02 maturity finding | D03 experimental characteristic score | Meaning |
|---|---:|---|
| `MET` | `1` | All eight mandatory criteria affirmatively evidenced |
| `PARTIAL` | `0.5` | Genuine Product-bound computational governance with evidenced non-foundational deficiencies |
| `NOT_MET` | `0` | Demonstrated foundational characteristic failure |
| `EVIDENCE_LIMITED` | Not a score | Separate evidence qualifier; report which maturity conclusions lack support |
| `NOT_APPLICABLE` | No generic automatic score | Requires a separately competent affirmative applicability determination |
| `NOT_ASSESSABLE` | No score | Assessment eligibility has not been established |

The score is one **characteristic-level** experimental number; the eight mandatory criteria are **conjunctive**, not eight additive features. Enterprise-specific policy implementation or evidential assurance levels may vary, **but cannot dilute CBD-M01–CBD-M08**. There are no automatic maturity caps, score overrides, IPCH L0/L1/L2 bands, invented implementation thresholds or universal exemptions. No enterprise maturity score is computed by this guide. D02 eligibility, assurance and governance authority remain separate from D03 numerical expression.

A `MET` finding on this characteristic never represents legal certification or independent regulatory assurance. The assessment reports maturity of the Product's compliant-by-design mechanisms relative to **competently established obligations**. A condition such as *app-only RBAC* must not be mechanically translated from DPCH09's example into a universal INFOPS `PARTIAL` without examining the Product's actual enforcement boundaries.

## 13. Critical assurance and governance boundaries

- **Policy authority:** Global, divisional when applicable, domain and Product governance layers are as independently established. No fixed new hierarchy and no Product Owner authority to override competent higher-order policy are created.
- **Legal/regulatory:** Jurisdictional classification, regulatory interpretation, lawful processing grounds, exceptions and assurance sign-off require competent human/institutional authority. A `MET` characteristic assessment does not confer them.
- **Productness/qualification:** BPS/PIN generic Productness and independent Product-family/Compound and INFOPROD/INFOPDS boundaries are preconditions/adjacent determinations, not established by IPCH09.
- **Semantics:** GEARA analytical structure and GEARM semantic definitions govern meaning and relevant information classifications; IPCH09 assesses enforcement against competent policy, not semantic adjudication.
- **DPP:** Possible Product-bound evidence/linkage, never automatic proof of runtime control execution or a newly mandated DPP conformance criterion.
- **Human oversight:** A competent human decision integrated into a machine-enforced control can be compatible; manual substitution for otherwise mandatory enforceable controls is not. `CBD-R02` OPEN.
- **Reused evidence:** IPCH06 trust claims and IPCH08 monitoring signals can support specific corroborated facts but cannot substitute for IPCH09 policy authority or runtime enforcement.
- **Identity integrity:** Separate Product/Version, semantic definition/version, policy version, Product descriptor, realization revision, compilation, runtime occurrence, dated enforcement decision and assessment determination. Do not compress them into one identifier.
- **Consequential actions:** Access grants, denials, legal determinations, regulatory reporting or remediation actions follow independent competently authorized mechanisms; the maturity guide does not execute or approve them.
- **Research holds:** Parent INFOPS Track B B01 completion `NOT_ESTABLISHED`; B02–B06 `NOT_AUTHORIZED`; effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE` and F01.6/F01.29 safeguards retained. Q0–Q5, F06/F14/F16 unresolved. Historical ledgers `65/6/7/7` separate from unchanged PC ledger; 62 G06 E0 designs approved/unexecuted, E1/E2 executions `0/0`; all 24 G06-RO01–RO12 and G03-R01–R12 OPEN. None is changed here.

## 14. Reassessment and evolution triggers

Re-evaluate applicable IPCH09 claims when **material** changes occur; distinguish the authority to make a change from the evidence that enforcement remains correct:

1. Competent global, divisional, domain or Product policy scope, priority, interpretation or effective version changes.
2. Product/Version or informational Promise changes, including semantic-definition or classification changes.
3. A new information combination, derivation, aggregation, materialization, recipient audience or consequential-use pattern creates potential additional obligations.
4. A consumer interface, export route, subscription, report delivery or realization path is added or materially modified.
5. Entitlement structure, identity provider, policy decision point, enforcement mechanism or policy compiler changes.
6. A previously detected control bypass, adverse policy decision, unexpected permitted consumption or material violation occurs.
7. Human-approval integration, exceptional authorization or override handling changes under competent authority.
8. Policy binding, enforcement logs, audit/violation monitoring or evidence lineage becomes stale or unavailable.
9. Product, policy, semantic-definition, realization, compilation or runtime-occurrence identifiers lose traceability or comparability.
10. Source research or Second-Pass review later refines a maturity edge case—**only if separately owner-approved**, without retroactively assuming new authority.

A reassessment trigger does not itself revoke a Product entitlement, amend a law, instantiate a control or reclassify a historical qualification. Preserve old and new evidence/decision effective intervals and explicitly record the authority deciding a change.

## 15. Adversarial and boundary cases — First-Pass fixtures

The following are **proposed scenarios only**. No test execution, verdict, conformance or operational evidence is claimed.

| ID | Fixture / challenge | What must be distinguished |
|---|---|---|
| **CBD-A01** | Policies documented but no runtime enforcement | Written obligation versus executed control; source foundational failure |
| **CBD-A02** | Applicable policies are visible only after Product implementation | Design-time self-service governance versus retrospective review |
| **CBD-A03** | Federated model includes global/divisional/domain/Product levels | DPCH09 source pattern and actual competent precedence |
| **CBD-A04** | Federated model has global/domain/Product but no divisional layer | AIPCH10 source pattern; no artificial universal four-layer requirement |
| **CBD-A05** | A legitimate human authorization is recorded and enforced by policy mechanism | Oversight as governed control component versus manual substitute |
| **CBD-A06** | Manual ticket approval is used instead of an available/required enforcement mechanism | Procedural governance versus automatic runtime enforcement |
| **CBD-A07** | Upstream Data Products enforce controls but derived Information Product does not | Independent obligations on resulting information and output |
| **CBD-A08** | Product-local restriction attempts to override binding higher-order policy | Non-overridable competent precedence versus unauthorized bypass |
| **CBD-A09** | One consumer port enforces while another materially equivalent path bypasses | Consistent Product-level control coverage |
| **CBD-A10** | Product changes after publication while old policy binding remains | Lifecycle/version propagation and effective enforcement |
| **CBD-A11** | DPP reports compliant posture but actual runtime evidence missing/contradictory | Supporting assertion versus independent executed enforcement |
| **CBD-A12** | Enforcement decisions cannot be bound to Product/Version and policy version | Evidence identity, historical integrity and admissibility |

`CBD-A01–CBD-A12 = PROPOSED_E0_UNEXECUTED`. No adversarial replay, evidentiary adjudication, policy-engine test run or legal determination has been performed. Cases inform future Second Pass and cannot silently resolve the owner-approved open questions.

## 16. Source provenance, open questions and status

### Source lineage and bounded interpretation

| Source | Direct-source claims preserved | Information-specific First-Pass adaptation |
|---|---|---|
| `DPCH09` (`pages/DPCH-PMDD-guidance/09-DPCH09.md`) | Global→divisional→domain→Product; self-service design-time visibility; lifecycle binding; automated runtime policy-as-code and entitlements; optional DPP trust evidence; app-only RBAC `Partial`; after-deployment policy `Not met`. | Federated competence/precedence, applicable Information Product-level controls and enforcement across actual informational outputs, without mandatory fixed division layer or universal DPP artifact. |
| `AIPCH10` (`AIPCH-PMDD-guidance/10-AIPCH10.md`) | Global→domain→Product; policy intent and compilation binding; machine-interpretable runtime controls; consistent consumer treatment; violation detection; incomplete enforcement `Partial`; human oversight integrated with controls may be `Met`. | Information-specific access, usage and derived-information governance; retain distinction between integrated authorized human decision and manual enforcement substitution; do not import AI-only risk tiers as universal controls. |
| `INFOPS-0.1-IPCH-P01-D25-F01` | Owner-approved F01.1–F01.16: eight conjunctive criteria, nine negatives, eight evidence requirements, eight OPEN research questions and twelve unexecuted adversarial cases. | Experimental E0 authority to draft this guide, **not** owner acceptance of completed draft or normative status. |

### Second-Pass research register — all OPEN

| ID | Open research question |
|---|---|
| **CBD-R01** | How should DPCH09's four-layer and AIPCH10's three-layer federated policy models map to enterprises with different competent intermediate authorities? |
| **CBD-R02** | What precisely separates legitimate human authorization/oversight integrated into enforced controls from a prohibited manual process substituting for mandatory computational enforcement? |
| **CBD-R03** | What evidence establishes that a derived/aggregated Information Product respects inherited and additional applicable information-handling constraints? |
| **CBD-R04** | What evidence establishes Product-local policy additions are consistent with higher-order constraints without granting the Product Owner new policy authority? |
| **CBD-R05** | What minimum proof demonstrates consistent enforcement across heterogeneous consumption ports, exported/materialized outputs and realization patterns? |
| **CBD-R06** | How should Product/Version, semantic version, policy version, realization revision, compilation and runtime occurrence remain independently traceable in policy evaluation evidence? |
| **CBD-R07** | What is the defensible `PARTIAL` versus `NOT_MET` boundary when genuine computational controls exist but material enforcement coverage or violation detection is deficient? |
| **CBD-R08** | How does IPCH09 enforcement evidence relate to IPCH06 trust, IPCH08 monitoring and independent policy/legal assurance without circular claims? |

### Programme status and next authorization

| Item | Status |
|---|---|
| `D25-F01` baseline | `APPROVED_EXPERIMENTAL_E0` |
| `IPCH09.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` (D26 experimental E0) |
| Owner acceptance of draft | `APPROVED_EXPERIMENTAL_E0` under D26, experimental draft acceptance only |
| Mandatory criteria `CBD-M01–CBD-M08` | D25-approved; conjunctive |
| Negative `CBD-N01–CBD-N09`, evidence `CBD-ES01–CBD-ES08` | D25-approved |
| Adversarial `CBD-A01–CBD-A12` | `PROPOSED_E0_UNEXECUTED` |
| Research `CBD-R01–CBD-R08` | `OPEN` |
| IPCH01–IPCH08 outstanding reviews | Preserved, not closed or executed |
| D01–D25 and D02/D03/D04/D05 | Preserved unchanged |
| Second Pass | `NOT_STARTED` |
| Overlay preparation / deployment | `PREPARED_FOR_OPERATOR_REVIEW` / `NOT_DEPLOYED` |
| Empirical assessment / policy-control execution | `NOT_EXECUTED` by this research activity |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| IPCH10 | `NOT_INITIATED` |

**Stop boundary:** This sixteen-section experimental guidance is **owner-accepted as a First-Pass draft under D26 only**. This incremental overlay is prepared for operator review but is not verified as deployed. Draft acceptance and packaging are not final approval, empirical validation, normative adoption, Second-Pass execution or initiation of IPCH10. All parent Track B/S04 safeguards, historical 65/6/7/7 ledgers, Q0–Q5, F06/F14/F16, 62 unexecuted G06 E0 designs, E1/E2 zero and 24 open G06/G03 obligations remain unaltered.
