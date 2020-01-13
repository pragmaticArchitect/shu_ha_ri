# IPCH12 — Consumption-Driven Intent: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH12-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Principal sources:** `DPCH12` (Data Product) and `AIPCH13` (AI Product), individually interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D31-F01 = APPROVED_EXPERIMENTAL_E0` — approved criteria baseline; `INFOPS-0.1-IPCH-P01-D32-F01 = APPROVED_EXPERIMENTAL_E0` — owner acceptance of this experimental draft only  
> **Guide status:** `DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `APPROVED_EXPERIMENTAL_E0` (D32, draft only)  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This is a **prepared, non-normative, experimental First-Pass assessment guide**, not an executed assessment, a qualified Information Product determination, an authorization to create or deploy a Product, or a governance mandate. D32 owner acceptance concerns this experimental draft only; packaging does not establish live publication, testing, empirical observations, adversarial execution or any progression to IPCH13. The accountable human owner alone may accept this draft, within verified competence. Original D05 sequence is preserved historically; numerical First Pass is an owner-directed progression.

## 1. Characteristic identity and source lineage

| Field | Experimental First-Pass value |
|---|---|
| Characteristic | `IPCH12 — Consumption-Driven Intent` |
| Guide | `IPCH12-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01` |
| Assessment subject | An independently eligible Information Product/Version, its declared informational Promise, relevant consumer contexts, design and evolution evidence in an effective assessment interval |
| Approved decision | `INFOPS-0.1-IPCH-P01-D31-F01`, F01.1–F01.16 |
| Principal lineage | `DPCH12 — Consumption-Driven Intent` / `AIPCH13 — Consumption-Driven Intent` |
| Mandatory conjunctive criteria | `INT-M01–INT-M08` |
| Negative conditions | `INT-N01–INT-N09` |
| Evidence requirements | `INT-ES01–INT-ES08` |
| Unexecuted adversarial cases | `INT-A01–INT-A12` |
| Open Second-Pass questions | `INT-R01–INT-R08` |
| Qualitative assessment | D02 `MET`, `PARTIAL`, `NOT_MET`, independent `EVIDENCE_LIMITED`, competent `NOT_APPLICABLE`, eligibility-dependent `NOT_ASSESSABLE` |
| Experimental characteristic scoring | D03 `MET=1`, `PARTIAL=0.5`, `NOT_MET=0`; no criterion averaging, maturity bands or automatic caps |

**Exact principal files independently reopened for this draft:** `DPCH.zip → pages/DPCH-PMDD-guidance/12-DPCH12.md` and `AIPCH.zip → AIPCH-PMDD-guidance/13-AIPCH13.md`. DPCH archive entry also includes succeeding DPCH13/14 material; **only its DPCH12 segment** is a principal source here. Their characterizations are sources of Product-characteristic guidance, not proof that any individual Information Product is qualified or that external governance decisions exist.

**DPCH12 — source assertions:** the Product is intentionally designed, governed and evolved around explicit consumers and outcomes, rather than the sources or producer. The declared purpose, structure/aggregation/freshness/ports and subsequent feedback-driven change must be traceable. Source-driven dumps, generic “for analytics” purposes and post-hoc invented consumers are negative. Its single-known-consumer case is expressly `Partial`; multiple consumers with different intents, served through appropriate abstraction, are `Met`; declared intent ignored in design is `Not met`.

**AIPCH13 — source assertions:** the Product's behaviour, outputs and constraints trace to explicit consumer needs, decision contexts and outcomes. Target roles, decision or action context, expected effect and relevant performance/explainability/usage expectations are recorded; evolution responds to usage and outcomes, not model upgrades alone. Its clearly defined single-use-case case is **`Met`**, multiple potential but undefined uses `Not met`, generalized real consumption `Met`, exploratory model without defined consumption intent `Not met`. This model-specific analogy does **not** make model dependency a requirement of an Information Product.

**Unresolved principal tension:** DPCH12 single consumer `Partial` versus AIPCH13 single consumer `Met`; `INT-R01 = OPEN`. DPCH12 does not itself provide a conclusive rule for information-specific early-lifecycle evidence. Do not silently resolve this by introducing IPCH07 reuse prerequisites or treating the AI source as binding authority.

## 2. What the characteristic really asserts

> **IPCH12 — Consumption-Driven Intent:** An Information Product is Consumption-Driven when its purpose, target consumers, decision or analytical contexts and intended outcomes are explicitly established in its governed Product definition; its informational Promise, analytical construction, consumption contracts and applicable constraints are demonstrably shaped by those needs; and its evolution remains traceable to changing consumer requirements, observed consumption signals and outcome effectiveness rather than source availability or producer convenience.

This **D31-approved experimental definition** separates a *purpose constitutive of the Product* from an aspiration or a retrospective business case. “Useful data,” “enterprise reporting” and “decision support” alone are insufficient to establish why particular measures, reporting windows or interpretation rules were chosen. Actual consumer context must shape the informational capability itself, including its outcomes and important constraints.

Consumer and outcome intent is not necessarily a promised quantitative financial return: legitimate information products may support statutory returns, risk interpretation, advisory decisions or legally required disclosures where an appropriate indicator is timeliness, completeness, decision suitability or a documented compliance outcome. Competent authorities still determine the actual legal or policy obligation; this guide does not.

The characteristic concerns purposeful Product constitution and evolution, not numerical breadth of adoption. Demonstrated independent reuse is evaluated by IPCH07. An eligible Product might meet one and not the other, but the **source maturity treatment of a single consumer is still unresolved** (`INT-R01`). Products with multiple user types must maintain a coherent Product intent rather than accumulate unrelated purposes under a vague title (`INT-R02`).

## 3. Information Product specialization

In an Information Product, meaning and context are part of the delivered capability. A consuming decision therefore influences **what is calculated, aggregated or interpreted; when information is considered current; which populations and time horizons apply; how uncertainty is conveyed; and how the output should be consumed**. Source availability may constrain implementation but does not substitute for declared intent.

**Who:** identified consumer archetypes such as treasury operations, an analyst, reporting function, automated service or agent. A person's name alone does not specify the consumption context. **Why:** named decision, analytical question, statutory reporting purpose or operational outcome. **What:** a testable or assessable informational effect, not merely “insights.” **How:** relevant granularity, semantic definitions, cut-offs, quality, freshness, accessibility, interpretability and policy constraints. **Evolution:** governed assessment of changed needs, usage/outcomes and deliberate lifecycle choices.

**Illustrative example — consolidated intraday liquidity:** A producer might publish every available account and ledger field merely because the sources exist. Another producer may begin with the liquidity management decision, defined entity/currency scope, restriction handling, information cutoff, interpretation and delivery interval, and construct the informational Promise accordingly. Only the latter illustrates traceable consumption purpose; this is not an assessment of any real Product or a declaration that a specific banking measure is authoritative.

**AIPCH13 analogy:** the AI source requires behaviour, outputs, constraints and relevant explainability to follow defined consumption. Here the analogous Information Product elements are analytical measures, interpretations, scope, constraints and delivery characteristics. Importing AI-specific behaviours, model dependence or AI-product-family status is prohibited without independent qualification.

**Early lifecycle caution:** a new Product may have well-governed intent and a real feedback mechanism while lacking observed consumption history. That is a potential evidence or maturity boundary, not an automatic `MET` or `NOT_MET` rule (`INT-R05 = OPEN`). Legitimate infrastructure updates may preserve consumer purpose even though triggered by technology; the source warning is against **technology-only** evolution that disregards consumer outcomes (`INT-R06 = OPEN`).

## 4. Assessment subject and authority

Keep these distinct in all determinations:

1. **Product/Version eligibility:** the exact subject must independently meet BPS/PIN generic Productness, applicable Information Product-family/Compound qualification and D02 eligibility before maturity assessment. IPCH12 does not qualify a Product.
2. **Governed consumption intent:** authoritative intent and its effective revision, relevant Product Owner responsibility, declared consumers, decisions, outcome expectations and scope. A Product Owner declaration is not evidence that expected outcomes have been achieved.
3. **Information definition:** Product's informational Promise, semantic-definition/version, measures, assumptions, derived assertions, delivery expectations and active consumption contracts. Authoritative shared meaning remains governed through GEARA/GEARM.
4. **Implementation realization:** platform profile, realization revision, compilation or deployment facts may support design traceability but are distinct from Product/Version and purpose. Do not classify a delivery project as the Product.
5. **Consumption evidence:** actual or prospective consumer records, adoption signals, feedback, outcome observations and context. Evidence of planned adoption is not observed adoption.
6. **Decisions and uncertainty:** owner-authorized Product evolution decisions, provenance, timing and evidence limitations. Human governance authority is not delegated to an AI guide or evaluator.

An IPCH12 finding judges whether consumption intent shaped Product constitution/evolution, not whether a legal decision was valid, whether semantic standards were amended, or whether the Product actually achieved commercial success. The competence to approve such matters belongs elsewhere.

## 5. Applicability and N/A rules

The characteristic applies to any **independently eligible** Information Product/Version, including specialized regulatory, internal, analytical or advisory Products. A single consumer is not in itself proof of inapplicability; it is an explicit unresolved **maturity** question under `INT-R01`. A low-volume Product may still possess clear intentional constitution. Broad potential readership, conversely, cannot substitute for defined users and outcomes.

A newly created Product may lack historical feedback; do not create an automatic whole-characteristic exemption. Assess verified intent, governed feedback/evolution mechanisms and the temporal limitations separately. `INT-R05` preserves whether the deficit in history leads to an evidence qualifier, a non-foundational partial finding or some other competent rule.

`NOT_APPLICABLE` requires competent, case-specific D02 disposition; **none** is conferred by this guide. `NOT_ASSESSABLE` applies where independent Product/Version eligibility is not established. `EVIDENCE_LIMITED` is a **separate evidence qualifier** for disputed, incomplete, stale or misattributed evidence. Lack of a preferred artifact type is not automatically demonstrated noncompliance.

## 6. Distinctness and non-duplication

| Neighbour or authority | Independent assessment claim |
|---|---|
| IPCH01 Domain-Owned | Accountable domain ownership is separate from whether the informational capability is constituted for explicit consumers/outcomes. |
| IPCH03 Declarative | Machine-governed statement of intent is distinct from whether consumer needs genuinely shape informational construction and evolution. |
| IPCH04 Discoverable | Being discoverable to consumers does not prove a Product was designed around their needs. |
| IPCH05 Self-Describing | Communicating a purpose is not proof that the purpose governed decisions. |
| IPCH06 Trustworthy | Trusted information need not be relevant to a specified consuming decision. |
| IPCH07 Reusable | Actual independent adoption/generalized reuse is distinct from single or multiple consumers' **purpose** shaping a Product. Do not import its threshold into INT-M06. |
| IPCH08 SLA–SLO Backed & Observable | Operational performance observations are evidence inputs; they do not themselves define consuming intent. |
| IPCH09 Compliant by Design | Applicable policy enforcement is distinct from why a Product is created for legitimate use. |
| IPCH10 Addressable | Accessible output ports are distinct from consumer intent that motivates their selection. |
| IPCH11 Semantically Aligned | Authoritative meaning of a measure is distinct from whether that measure is relevant to the consuming decision. |
| IPCH13 Testable & Versioned | Change protection is distinct from whether changes serve consumer needs. |
| IPCH14 Economically Accountable | Cost/value accountability may consume outcome signals but does not replace declared consumption purpose. |
| BPS/PIN / Information-family / Compound | Productness and family qualification are independent of maturity. |
| GEARA/GEARM; DPP; INFOPROD/INFOPDS; PFI/HDIP | Separate semantic, descriptor, Product and realization authorities; no adoption or execution presumed. |

The same artifact may support several distinct assessment claims only where its actual evidence suffices for each. Avoid circular inference from a self-description, generic purpose field, catalogue listing, usage telemetry or D03 maturity score to `MET` consumption-driven intent.

## 7. Core mandatory positive criteria — `MET`

The D31-approved `INT-M01–INT-M08` are **mandatory and conjunctive**. No single criterion earns points, substitutes for another or authorizes a different Product-family test.

| ID | Criterion | Mandatory assertion |
|---|---|---|
| **INT-M01** | **Explicit Governed Consumption Intent** | The Product has an authoritative, expressly governed purpose rather than an inferred or retrospective justification. |
| **INT-M02** | **Identified Consumers and Decision Contexts** | Target consumer archetypes and relevant business, analytical, regulatory or operational decision contexts are sufficiently defined. |
| **INT-M03** | **Defined Intended Outcomes** | Expected consuming outcomes or improvements and assessable effectiveness expectations are stated, allowing legitimate non-financial outcomes. |
| **INT-M04** | **Informational Promise Aligned to Intent** | Measures, interpretation, analytical scope, granularity, time horizon and material assumptions are shaped by intended consumption. |
| **INT-M05** | **Consumption Requirements Reflected in Design** | Applicable service, quality, interpretation, delivery-port and usage constraints trace to consumer needs. |
| **INT-M06** | **Consumer-Independent Core Intent Integrity** | Legitimate variation across consumer contexts does not arbitrarily redefine or contradict the Product’s core informational purpose; no minimum number of active consumers is introduced. |
| **INT-M07** | **Consumption-Led Product Evolution** | A governed mechanism uses relevant feedback, usage/outcome signals and changed business priorities in Product evolution decisions. |
| **INT-M08** | **Product-Level Intent Traceability and Evidence Integrity** | Intent, consumers, outcomes, design/evolution evidence and effective dates are attributable to the exact assessed Product/Version. |

**Assessment consequence:** `MET` is supported only when all eight are adequately evidenced for the assessed Product/Version and interval. In particular, INT-M06 asserts core-intent coherence; **it does not settle the single-consumer maturity conflict** or mandate multiple active consumers. INT-M07 requires a governed mechanism and relevant evidence of consumption-led decisions, with early-stage execution/history sufficiency still open. Evidence must demonstrate actual intent-to-design linkages, not simply the existence of a requirements document.

## 8. Core negative criteria — `NOT_MET`

The following `INT-N01–INT-N09` identify **potential disconfirming evidence**. Their presence must be established, attributed and evaluated under D02; do not mechanically convert missing documents into proven failures.

| ID | Negative condition |
|---|---|
| **INT-N01** | Source data, infrastructure, models or available analytical technology supply the primary Product justification rather than consumption need. |
| **INT-N02** | Purpose is vague, such as “for analytics,” “for reporting,” or “supports decision-making,” without specific context. |
| **INT-N03** | Intended consumers or decision contexts are unknown, reconstructed after production or held only as tribal knowledge. |
| **INT-N04** | Product measures, assumptions, interpretations or outputs materially contradict its declared consumer purpose. |
| **INT-N05** | Design follows producer convenience or source-system shape despite known incompatible consumption requirements. |
| **INT-N06** | Quality, freshness, interpretation, output modes or constraints ignore material declared consumer requirements. |
| **INT-N07** | Material Product evolution is driven exclusively by engineering or upstream changes without examining consumer needs. |
| **INT-N08** | Different consumer contexts cause uncontrolled and contradictory changes to the claimed core Product intent. |
| **INT-N09** | Claims cannot be traced to the assessed Product/Version, or rely on obsolete and misattributed intent/evolution evidence. |

**Illustrative difference:** A Product that was built solely because a source extract is available can demonstrate a foundational absence of intent. A Product whose consumer workshop records are temporarily unavailable may instead warrant `EVIDENCE_LIMITED`; the evidence cannot be manufactured or assumed.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Finding | Bounded First-Pass interpretation |
|---|---|
| `MET` | All `INT-M01–INT-M08` adequately evidenced; do not infer from a purpose label or usage alone. |
| `PARTIAL` | Genuine consumption-driven constitution is present, but demonstrated **non-foundational** deficiencies remain in traceability, outcome evidencing, alignment or feedback integration. |
| `NOT_MET` | Foundational consuming purpose absent, or real stated purpose demonstrably ignored in Product construction/evolution. |
| `EVIDENCE_LIMITED` | Separate qualifier for gaps, stale or contradictory evidence; not an automatic failure. |
| `NOT_APPLICABLE` | Only through competent D02 specific scope disposition; no blanket exception. |
| `NOT_ASSESSABLE` | Product/Version eligibility not independently established. |

**Explicit source tension:** DPCH12 says a *single known consumer, clearly defined* is `Partial` because breadth of consumption is not established, even though purpose is real. AIPCH13 says a *single defined use case with clear consumer* is `Met` because intent and aligned behaviour suffice. The D31 baseline preserves both and declares `INT-R01 = OPEN`. An assessor may not resolve that case by silently importing IPCH07 reuse criteria, or by assuming one source is universally superior.

**Multi-consumer intent:** DPCH12 calls genuinely designed multiple different intents `Met`; AIPCH13 emphasizes a general capability retaining explicit core purpose. Neither establishes that unrelated uses grouped after the fact become a coherent Product (`INT-R02 = OPEN`).

**Early lifecycle:** distinguish a demonstrated feedback process, a process merely designed but never used, and observed outcomes absent due to newly launched status (`INT-R05 = OPEN`). **Technology change:** legitimate maintenance can preserve intent; upgrades without reference to consuming needs are a warning (`INT-R06 = OPEN`). Uncertainty must remain visible until competent Second Pass decisions.

## 10. Evidence signals and sufficiency

D31-approved `INT-ES01–INT-ES08` specify **claims**, not compulsory formats or systems. For each criterion identify the exact source, Product/Version, effective period, provenance, supporting/contradicting evidence and evidence limitation.

| ID | Supports | Evidence requirement |
|---|---|---|
| **INT-ES01** | `INT-M01` | Authoritative Product-bound intent and purpose declaration, current effective context and competent owner identification. |
| **INT-ES02** | `INT-M02` | Specified consumer archetypes, their decisions/analytical contexts and applicable use scope. |
| **INT-ES03** | `INT-M03` | Stated intended outcomes and appropriately assessable success/effectiveness expectations, including regulatory or advisory outcomes where appropriate. |
| **INT-ES04** | `INT-M04` | Trace between intent and informational measures, semantic interpretations, derivations, scope and assumptions. |
| **INT-ES05** | `INT-M05` | Trace between needs and material service levels, freshness, interpretability, appropriate output ports and usage restrictions. |
| **INT-ES06** | `INT-M06` | Stable core purpose and coherent treatment of applicable consumer contexts, distinguishing potential consumers from observed independent reuse. |
| **INT-ES07** | `INT-M07` | Governed consumption-feedback/usage/outcome signals and documented Product-evolution reasoning; early-lifecycle limits expressly qualified. |
| **INT-ES08** | `INT-M08` | Exact Product/Version, intent revision, effective dates, source/provenance, semantic-definition/consumption-contract links and evidence limitations. |

**Authoritative candidate evidence:** governed Product intent and outcomes, named consumer/decision contexts, Product-linked design rationale, relevant semantic and consumption contract references, approved Product decisions. **Supporting candidate evidence:** user research, consumer requests, usage patterns tied to purpose, accountable evolution records, outcomes/feedback and reporting obligations. These examples cannot be declared present or authoritative without inspection.

**Red flags:** generic “for analytics” labels; undifferentiated persona lists; Product metrics reflecting source structure alone; “future use cases TBD”; copied specifications; feedback records without consumers, effective context or Product version; post-hoc purpose added without evidence of design effect.

An experimental template, design mockup, unexecuted test or descriptor claim is not operational proof. Neither an independently controlled DPP nor a particular backlog or analytics vendor is made mandatory. Where an artifact references independent authority, verify the authority and content, not the reference label alone.

## 11. Agent-assisted or human assessment decision rule

Use a transparent **bounded evidence procedure**, never self-certification:

1. **Establish eligible subject:** independently verify assessed Product/Version and D02 applicability; if unestablished, use `NOT_ASSESSABLE` rather than scoring a non-Product.
2. **Fix the effective context:** identify assessment interval, intent revision, authorized owner, consumers and decision contexts; distinguish planned from actual use.
3. **Establish declared purpose:** verify an authoritative, non-generic intent describing who/why/what/how and expected outcomes (`INT-M01–M03`).
4. **Trace design back to intent:** examine measures, semantics, scope, assumptions, quality, freshness, access, constraints and decision records (`INT-M04–M05`). Do not accept a purpose paragraph as sufficient.
5. **Check coherence:** examine the core Product purpose under its legitimate consumer contexts (`INT-M06`) without requiring a universal consumer count or presuming cross-consumer reuse.
6. **Check evolution:** inspect governance process, feedback/outcome evidence and its effect on decisions (`INT-M07`). Explicitly state early-life historical gaps and open rule `INT-R05`.
7. **Bind exact evidence:** distinguish Product/Version, intent revision, semantic definitions, output/consumption contract, realization revision, runtime observation and assessment determination (`INT-M08`).
8. **Test negative evidence:** examine `INT-N01–N09`, contradictions and independent qualifications. A proved foundational failure is distinct from unavailable evidence.
9. **Preserve source tensions:** where single-consumer, multi-consumer or early-lifecycle ambiguity is material, label `INT-R01/R02/R05` rather than silently resolving it.
10. **Determine bounded finding:** record qualitative D02 assessment, independent `EVIDENCE_LIMITED` qualifier where required, rejected alternative claims, provenance and competent human review. Apply D03 only to a defensible characteristic-level finding.

**Agent limits:** AI may challenge evidence, identify contradictions and prepare a draft recommendation. It cannot grant Product qualification, infer real adoption from a persona, invent outcome metrics or approve legal, policy, semantic or maturity decisions on behalf of the human owner. No authority or runtime mechanisms are created by this guide.

**Simplified negative source logic:** both sources reject a Product whose structure, behaviour or evolution cannot be traced to a declared consumer purpose. They do *not* jointly resolve DPCH12/AIPCH13's single-consumer maturity classification.

## 12. PMDD scoring treatment

Only an **overall characteristic finding**, once properly determined under D02, maps through D03:

| Qualitative characteristic finding | Experimental score |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |

This is not a weighted eight-item checklist. Do not compute `5/8`, average criterion marks, impose a new ceiling for a single consumer, or manufacture numerical risk adjustments. `EVIDENCE_LIMITED` is separate from evidence of failure; `NOT_APPLICABLE` and `NOT_ASSESSABLE` do not automatically receive zero. There are **no adopted IPCH L0/L1/L2 maturity bands**.

D03 characteristic weights are equal in the existing **experimental** scheme, subject to the separate approved assessment constraints. No overall maturity result or Product qualification is determined by this draft. Preserve INT-R01 before assigning a universal score to a single-consumer scenario.

## 13. Critical assurance and governance boundaries

- **Human authority:** D31 is criteria approval only. Final acceptance of this guide is pending; subsequent publication or operational implementation requires separate authorization within independently verified competence.
- **Productness/family:** BPS/PIN generic Productness, Information Product and Compound qualification, and upstream assessment eligibility are independent. An intentional idea does not automatically become a qualified Product.
- **Semantics:** GEARA/GEARM control authoritative meanings. An Information Product Owner's intent declaration cannot redefine an enterprise measure or override semantic requirements.
- **Information/realization artifacts:** INFOPROD/INFOPDS, DPP and PFI/HDIP play distinct governed roles; no particular artifact implementation or enterprise execution is inferred from this guide.
- **Policy and consequential use:** relevant policy/legal/assurance bodies remain competent for regulatory obligations, authorization, decision rights and actual outcomes. A clear intended decision is not permission to take that decision.
- **Product/Version evidence:** keep intent revision, semantic-definition version, port contract, realization revision, compilation, occurrence, feedback and observed outcomes separate. Product purpose may be stable across realization changes.
- **No circularity:** an owner-approved intent, a Product listing, a PMDD score or an engineering activity alone does not demonstrate full consumption-driven alignment.
- **No execution authority:** parent INFOPS E0 design approval is not E1/E2 execution or empirical Product observation. Second Pass remains unexecuted and out of scope.

## 14. Reassessment and evolution triggers

A responsible reassessment may be prompted by a change in target consumers or decision context, material change of intended outcomes, newly required informational semantics/assumptions, changed granularity or cutoffs, significant new feedback, declining actual suitability, changed usage patterns, revised statutory purpose, an important contract or quality change, or an intentional change of Product intent revision.

Technology migration alone is neither automatic evidence of lost intent nor an exemption from examining consumers. The question is whether purpose and affected requirements remain governed and traceable. A change in realization revision does not necessarily entail new Product/Version or intent revision, and an intent revision does not automatically imply semantic-definition change; these determinations require separately competent governance.

Capture **reason for reassessment**, affected Product/Version, historical intent and new intent, evidence periods, changed assumptions, decision makers, consumer implications and limitations. Do not silently overwrite earlier determinations or claim an enterprise-wide automated workflow operates. Reassessment cadence and experimental evidence sufficiency remain governed by D02/Second-Pass study, not invented here.

## 15. Adversarial and boundary cases — First-Pass fixtures

`INT-A01–INT-A12` are **proposed fixtures only**. None has been replayed, empirically validated or graded; candidate observations are hypotheses for future competent Second Pass.

| Case | Unexecuted adversarial challenge | Distinction to test |
|---|---|---|
| `INT-A01` | One real consumer with clear decision intent, demonstrably aligned Product design and a governed feedback mechanism. | DPCH12 PARTIAL vs AIPCH13 MET; INT-R01 |
| `INT-A02` | Several actual independent consumers whose different uses are accommodated by one coherent purpose. | Intent generalization vs reuse; INT-R02 |
| `INT-A03` | Numerous hypothetical consumers but no specific consumer context or intended outcome. | Potential consumers do not evidence explicit intent |
| `INT-A04` | Source extract first, post-hoc purpose statement later. | Post-hoc purpose versus constitutive purpose |
| `INT-A05` | Clear intent document contradicted by the Product’s measures, assumptions and output design. | Design contradiction despite declared purpose |
| `INT-A06` | Single legitimate regulatory reporting recipient with clearly specified reporting obligation. | Regulatory single-consumer and source tension |
| `INT-A07` | Unrelated use cases bundled under the vague phrase “enterprise analytics.” | Artificial multi-use umbrella lacking coherent core intent |
| `INT-A08` | Clear decision context but inappropriate freshness and output interpretability. | Requirement-to-design disconnect |
| `INT-A09` | New Product with defined consumer need and feedback process but no adoption or outcome history. | Early-lifecycle evidence without invented usage; INT-R05 |
| `INT-A10` | Infrastructure migration justified with explicit impact on consumption outcomes and stable informational Promise. | Legitimate implementation evolution; INT-R06 |
| `INT-A11` | Pure technology upgrade and no consideration of changed consumer intent. | Technology-only evolution versus value-driven evolution |
| `INT-A12` | Extensive requirement documents but no version-linked evidence tracing decisions to Product design. | Exact Product/Version traceability vs generic documentation |

Do not infer from a case description that a real Product conforms or fails. Keep source disagreements and alternative findings visible during any future replay. A genuine single consumer can still be an eligible Product context, but the general `MET` vs `PARTIAL` maturity rule remains unadopted.

## 16. Source provenance, open questions and status

### Principal primary-source extraction

- `DPCH.zip → pages/DPCH-PMDD-guidance/12-DPCH12.md` — inspected section **DPCH12 — Consumption-Driven Intent**. That archive member also contains succeeding DPCH characteristic content, which is **not** treated as direct DPCH12 authority.
- `AIPCH.zip → AIPCH-PMDD-guidance/13-AIPCH13.md` — inspected **AIPCH13 — Consumption-Driven Intent**. AI-specific model/product behaviours are used by bounded analogy only.
- `INFOPS-0.1-IPCH-P01-D31-F01` — accountable human owner APPROVED clauses F01.1–F01.16 and the experimental criteria baseline; `INFOPS-0.1-IPCH-P01-D32-F01` — owner APPROVED acceptance of this completed experimental draft only. Earlier D02/D03/D04/D05 rules remain in force.

The approved research and unexecuted adversarial registers are reproduced below. No upstream source tension is silently settled by document drafting.

| Question | Research topic | Status |
|---|---|---|
| **INT-R01** | **Single-consumer maturity conflict.** Should a single genuine consumer with fully evidenced purposeful design qualify as MET, reconciling DPCH12 PARTIAL with AIPCH13 MET without duplicating IPCH07 Reusable? | **OPEN** |
| **INT-R02** | **Generalization of consuming purposes.** How may multiple legitimate consumer intents coexist while retaining one coherent Product informational Promise and independently qualified Product boundary? | **OPEN** |
| **INT-R03** | **Assessable intended outcomes.** What counts as meaningful, appropriately assessable outcomes in regulatory, advisory or decision-support uses where direct financial KPIs are unsuitable? | **OPEN** |
| **INT-R04** | **Intent-to-design evidence sufficiency.** What evidence suffices to trace consumption intent to measures, assumptions, semantics, informational quality, freshness and output ports? | **OPEN** |
| **INT-R05** | **Early-lifecycle feedback boundary.** How should new, experimental or low-adoption Products demonstrate consumption-led evolution when meaningful feedback or outcome history is limited? | **OPEN** |
| **INT-R06** | **Legitimate technology-driven changes.** When may infrastructure or upstream changes legitimately drive evolution while remaining accountable to declared consuming intent? | **OPEN** |
| **INT-R07** | **Identity and temporal attribution.** How should Product/Version, intent revision, semantic definition, consumer contract, realization revision and outcome evidence be independently bound? | **OPEN** |
| **INT-R08** | **Nonduplication and authority.** How should IPCH12 interact with IPCH03/05/07/08/10/11/13 and independent qualification/assurance authority without circular claims? | **OPEN** |

### Programme integrity and exact stopping point

| Programme control | Preserved status |
|---|---|
| `INFOPS-0.1-IPCH-P01-D31-F01` | `APPROVED_EXPERIMENTAL_E0` — definition/criteria only |
| `INFOPS-0.1-IPCH-P01-D32-F01` | `APPROVED_EXPERIMENTAL_E0` — draft acceptance only |
| `IPCH12.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` — D32; not finally approved |
| `INT-M01–INT-M08` | APPROVED mandatory conjunctive |
| `INT-N01–INT-N09`; `INT-ES01–INT-ES08` | APPROVED First-Pass baseline |
| `INT-A01–INT-A12` | PROPOSED E0, **UNEXECUTED** |
| `INT-R01–INT-R08` | **ALL OPEN**, particularly R01/R02/R05/R06 |
| Earlier IPCH01–IPCH11 | Outstanding review obligations and previously accepted guides preserved |
| IPCH12 overlay / deployment | `PREPARED_VERIFIED` / `NOT_DEPLOYED` (documentation packaging only) |
| IPCH13–IPCH16 | `NOT_INITIATED` |
| First Pass / Second Pass | `ACTIVE` / `NOT_STARTED` |
| Historical IPCH D01–D32 | Approved decisions preserved; original D05 sequence historically preserved |
| Parent Track B B01 completion; B02–B06 | `NOT_ESTABLISHED`; `NOT_AUTHORIZED` |
| Effective prospective S04 | `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` |
| Historical C06; safeguards | `APPROVED_NOT_EFFECTIVE`; F01.6/F01.29 retained |
| Historical approval ledgers | `65 / 6 / 7 / 7`; independent PC ledger unchanged |
| Q0–Q5; F06/F14/F16 | UNRESOLVED |
| G06 E0 designs | 62 approved, UNEXECUTED |
| E1/E2 executions | `0 / 0` |
| G06-RO01–RO12; G03-R01–R12 | **ALL 24 OPEN** |
| Normative INFOPS adoption/release | `NOT_AUTHORIZED` |

**Final guide-status statement:** `IPCH12.md / FIRST-PASS-DRAFT-01 = DRAFT_PREPARED_ACCEPTED` under owner decision D32. The incremental documentation overlay is `PREPARED_VERIFIED`, not deployed. This acceptance does not authorize repository deployment, semantic/legal/qualification decisions, PMDD execution, adversarial validation, final guide approval, normative release or IPCH13.
