# IPCH15 — Explainable & Transparent: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH15-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Principal inspected source:** `AIPCH16 — Explainable & Transparent`; **corresponding DPCH15:** `NOT_FOUND_IN_SUPPLIED_DPCH_CATALOGUE`  
> **Decision authority:** `INFOPS-0.1-IPCH-P01-D37-F01 = APPROVED_EXPERIMENTAL_E0` (criteria baseline); `INFOPS-0.1-IPCH-P01-D38-F01 = APPROVED_EXPERIMENTAL_E0` (acceptance of this experimental draft only)  
> **Document status:** `DRAFT_PREPARED_ACCEPTED`; owner acceptance `APPROVED_EXPERIMENTAL_E0` under D38 (draft only)  
> **Overlay:** `PREPARED_VERIFIED` (documentation only); **deployment:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

**Nature of artifact.** This is a proposed, experimental First-Pass guidance document for assessing the *Explainable & Transparent* characteristic of a separately qualified Information Product. It is not an evaluation of an actual Product, executed explanation-fidelity validation, certified interpretability method, release approval, disclosure authorization or normative specification. D37 approved clauses F01.1–F01.16 and the XTR assessment baseline; D38 separately accepted this experimental document as `DRAFT_PREPARED_ACCEPTED`. The incremental overlay is now prepared and verified, without deployment, final approval or normative authority.

**Assessment subject.** The exact independently eligible Information Product/Version and its material informational outputs, explanation contracts and consumption contexts. Information Product qualification is determined elsewhere. Explanations may reference sources, analytical methods, semantics and realizations, but none is interchangeable with the assessed Product.

## 1. Characteristic identity and source lineage

| Field | First-Pass identification |
|---|---|
| Characteristic | `IPCH15 — Explainable & Transparent` |
| First-Pass baseline | D37-F01 `APPROVED_EXPERIMENTAL_E0` |
| Guide | `IPCH15.md / FIRST-PASS-DRAFT-01` |
| Principal directly inspected source | `AIPCH16 — Explainable & Transparent` in `AIPCH.zip`, `AIPCH-PMDD-guidance/16-AIPCH16.md` |
| Corresponding Data Product guidance | No `DPCH15` in the inspected supplied `DPCH.zip` catalogue; do not invent a counterpart |
| Mandatory | `XTR-M01`–`XTR-M08`, conjunctive |
| Negative | `XTR-N01`–`XTR-N09` |
| Evidence | `XTR-ES01`–`XTR-ES08` |
| Research | `XTR-R01`–`XTR-R08`, OPEN |
| Adversarial fixtures | `XTR-A01`–`XTR-A12`, proposed and UNEXECUTED |

**Direct source assertion.** AIPCH16 is not satisfied by feature importance alone. It calls for output-, action- and behaviour-level explanation understandable in context, enabling consumers and competent oversight parties to inspect and challenge why an AI Product produces particular results. It distinguishes **local** (individual output factors and uncertainty), **global** (overall Product behaviour and tendencies), and **contextual** (business meaning) explanations. It advocates explanation at the Product interface, human meaningfulness, machine-interpretable structure, proportional depth, and consistent/reproducible explanation. The source's illustrative edge findings include: technical LIME/SHAP attribution only `PARTIAL`; natural-language-only without structure `PARTIAL`; contextual structured explanation at API `MET`; and high-risk AI without adequate explanation `NOT_MET`.

**Source limitation and synthesis.** The supplied DPCH archive ends with DPCH14; there is no verified same-numbered Data Product counterpart for IPCH15. That absence does not mean Data Products lack documentation, transparency or lineage obligations. AIPCH16 concerns AI Products; its feature attribution, model behaviour and risk-tier R0–R4 specifics are **not** universal INFOPS requirements. The definition, tests and thresholds below are the **D37-approved experimental Information-family derivation**; any additional examples are proposed reasoning, not claims about a DPCH15 source or normative authority. Open tensions are expressly preserved in `XTR-R01`–`XTR-R08`.

## 2. What the characteristic really asserts

> **D37-approved definition:** An Information Product is Explainable & Transparent when its material informational outputs, analytical derivations, assumptions, interpretations and applicable limitations are accompanied by sufficiently accessible, structured, context-appropriate and evidence-linked explanations that allow intended consumers and competent oversight parties to understand how and why the information was produced, interpret its significance, inspect relevant contributing factors, and challenge its meaning or validity without requiring undocumented implementation knowledge.

The maturity claim is **contextual, product-level intelligibility, inspectability, challengeability and faithful provenance of material informational results**. Mere availability, documentation, semantic alignment or structural lineage cannot by itself establish an explanation that a consumer can understand and challenge. Conversely, this characteristic does not demand that the consumer view every underlying proprietary formula or confidential source record; independently competent disclosure authorities determine lawful access.

Three distinct explanation questions must be kept separate: **what** an output means (semantic context); **how** a particular result was produced (sources, analytical derivation, exclusions, assumptions and relevant computational factors); and **why** the construction and results matter to the intended consuming decision (interpretation and applicable limits). An explanation may refer to each, but none substitutes for the others.

**Illustrative, not assessed.** A liquidity position of 2.8 billion displayed on a dashboard may have a valid shared definition and an intact output schema, but be inexplicable to a treasury consumer if the contributing legal entities, restricted balances, cut-off time, conversion choices and reconciliation limitations cannot be understood. This is an illustration of the distinct IPCH15 claim, not an assertion about a real system.

## 3. Information Product specialization

An Information Product supplies **interpreted information**, potentially derived from Data Products, analytical functions, business rules, aggregation or AI/model dependencies. Explainability therefore concerns (a) relevant source context and selection, (b) transformations, derivations and analytical methods, (c) uncertainty or caveats, (d) consumer-facing business meaning and (e) appropriately verifiable evidence bindings. An AI model dependency is neither a prerequisite nor an excuse to omit these concerns. A deterministic count may also need its filter criteria, reporting period and included/excluded population explained.

**Local informational explanations** address an identifiable output or observation: why this amount, ranking, alert, index or calculated measure was reported, which material inputs/factors contributed, and the relevant time and assumptions. **Global Product explanations** communicate the reusable analytical methodology, general classification/aggregation behaviour, expected limitations and scope. **Contextual explanations** translate the result into terms appropriate for the consuming decision without claiming that an explanation automatically authorizes a decision. This local/global distinction is adapted from AIPCH16; model-centric feature weights and AI decision boundaries are not mandated.

A mature design may use a governed explanation contract linked to the Product plus result-specific material contribution and occurrence evidence. Whether every occurrence needs a fully separate explanation, or a reusable contract suffices for a class of outputs, remains OPEN (`XTR-R02`). **XTR-M05** proposes a machine-referenceable structure without mandating RDF, OWL, JSON, an API framework, a particular evidence ledger or a centralized explanation engine. Where machines or auditors need to parse the explanation, the structure must be useful for that actual contract, not merely a free-text label claiming 'structured'.

**Faithfulness matters.** A fluent narrative that attributes a variance to exchange-rate changes when the executed logic used a different source or assumption is not a valid explanation. Verifiability is about alignment with the true derivation and applicable Product/Version, not rhetorical plausibility. A transparency assessment does not independently approve source disclosure or release protected details.

## 4. Assessment subject and authority

1. **Establish eligibility separately.** Identify the exact Product/Version through BPS/PIN generic Productness and competent Information Product/Compound qualification. If this is unestablished, D02 yields `NOT_ASSESSABLE`; a high explainability score cannot make an artifact a Product.
2. **Identify material explanations.** Establish relevant consumers, ports/output types, interpretation and oversight contexts. Do not presume all columns, counts and runtime occurrences require identical explanation depth; retain `XTR-R02/R04`.
3. **Bind the explanation claim.** Record the relevant Product/Version, semantic-definition version, analytical method/revision, explanation-contract version, realization, output occurrence, evidence date and applicable caveats separately.
4. **Examine actual capability evidence.** A DPP schema or E0 design may establish intent to expose explanations but not that consumers can retrieve accurate explanations in operation. Do not silently promote design into executed capability.
5. **Respect independent competences.** GEARA/GEARM and domain authorities govern underlying meaning and analytical definitions; PFI/HDIP or other realization authorities implement services; privacy, information security and legal authorities determine disclosure. Assurance, review and consequential decisions remain with competent humans/institutions.

The assessor may evaluate whether a Product makes an appropriate explanation available without acquiring powers to alter its meaning, access rules or downstream actions. An output occurrence from one realization or time is not proof that another release or result is explained equivalently.

## 5. Applicability and N/A rules

IPCH15 is presumptively applicable to independently qualified Information Products, whether batch, interactive, API-served, human-facing or machine-consumed, and whether calculations are deterministic, statistical or AI-assisted. Simple results need proportionate explanation, not necessarily elaborate reasoning traces; high-consequence decision support may demand deeper inspection under competent authority.

AIPCH16 discusses AI R0–R4 risk tiers, but **IPCH15 does not impose those tiers**. Any materiality/risk category used to select explanation depth must derive from applicable competent governance (`XTR-R04` OPEN). Human-facing natural language does not automatically exempt a Product from D37-approved machine-referenceable evidence criterion, even though the precise maturity boundary is open (`XTR-R03`). No generic whole-characteristic `NOT_APPLICABLE` is established. A restricted explanation may be delivered to authorized consumers/oversight parties via lawful means; prohibition on unrestricted disclosure is not itself an explainability failure.

`NOT_ASSESSABLE` is for independently ineligible/unestablished Product/Version subjects. `EVIDENCE_LIMITED` is an independent qualifier for gaps, conflicting versions, missing result linkage or stale evidence, not a shortcut to `MET` or `NOT_MET`. A proposed or approved E0 explanation design establishes neither a runtime interface nor evaluated fidelity.

## 6. Distinctness and non-duplication

| Distinct characteristic / authority | Boundary against IPCH15 |
|---|---|
| IPCH03 Declarative | Machine-governed Product specification versus accessible explanation of material results. |
| IPCH05 Self-Describing | Knowing what the Product is, exposes and promises versus why particular information was derived. |
| IPCH06 Trustworthy | Evidence-backed Product trust versus result intelligibility and challengeability. |
| IPCH08 SLA–SLO Backed & Observable | Operational behaviour and performance monitoring versus interpretable analytical derivation. |
| IPCH09 Compliant by Design | Applicable enforced policy control versus explanation of results within disclosure obligations. |
| IPCH10 Addressable | Access to governed outputs versus accessibility of accompanying explanations. |
| IPCH11 Semantically Aligned | Shared authoritative concepts and meanings versus how a material figure was obtained. |
| IPCH12 Consumption-Driven Intent | Why the Product exists for an intended decision versus why a particular output takes its value. |
| IPCH13 Testable & Versioned | Version-specific validation/regression contracts versus accurate human/system explanations; shared test evidence is not interchangeable. |
| BPS/PIN and Product-family qualification | Productness and Information Product qualification remain independently decided. |
| GEARA/GEARM | Definition of analytical and semantic meaning remains under independent competence. |
| Law/policy/security | Disclosure and oversight rights are not conferred by explainability maturity. |

A data-lineage graph may corroborate an explanation, but lineage alone does not demonstrate the consumer can interpret methodological assumptions. A self-description may say 'position is reconciled', but does not itself explain which material positions produced a given value. Likewise, testable explanations might support IPCH13, but a test framework being present cannot establish IPCH15's meaning and accessibility.

## 7. Core mandatory positive criteria — `MET`

**D37-approved mandatory and conjunctive baseline.** Every material claim requires adequate Product/Version-specific evidence. Do not individually score or average criteria.

| ID | Mandatory criterion | Required demonstration |
|---|---|---|
| `XTR-M01` | **Governed Explainability Scope and Purpose** | Material result/output classes, intended consumers and oversight contexts, required explanation purpose and accountable scope are identified and governed. |
| `XTR-M02` | **Contextually Meaningful Informational Explanations** | Material outputs can be interpreted in appropriate business/analytical terms, not merely technical code, feature IDs or internal processing vocabulary. |
| `XTR-M03` | **Transparent Derivation and Contributing Factors** | Relevant source selection, calculations, transformations, assumptions, exclusions and material contribution factors are inspectable at an appropriate level without reconstructing implementation. |
| `XTR-M04` | **Product-Level Explanation Accessibility** | Required explanations are available via governed Product interfaces or explicitly linked authorized explanation facilities; not confined to tribal knowledge or inaccessible internal tooling. |
| `XTR-M05` | **Structured and Machine-Referenceable Explanation Evidence** | Material explanation claims are represented with enough structure/referenceability to support appropriate system, governance and audit interpretation, without mandating a technology. |
| `XTR-M06` | **Proportionate Explanation Depth and Limitations** | Explanation depth fits material context, consequence and oversight; uncertainty, exclusions, caveats and limits are not misleadingly omitted. |
| `XTR-M07` | **Explanation Consistency and Verifiability** | Explanation content is consistent with actual applicable derivation, semantic meaning and Product/Version behaviour, with meaningful means to inspect, challenge or verify claims. |
| `XTR-M08` | **Product-Level Explanation Provenance and Evidence Integrity** | Explanation and evidence reliably bind exact Product/Version, result/occurrence where relevant, applicable semantic/method revisions, realization/effective time and evidence limitations. |

**Conjunctive effect.** A clear prose explanation may support XTR-M02 but cannot by itself satisfy XTR-M03/M05/M07/M08. A provenance endpoint may support XTR-M03/M08 but not XTR-M02. A source-system diagram is not evidence that explanations are accessible to authorized consumers under XTR-M04. Product-Level evidence integrity is independent of whether the narrative sounds sensible. `XTR-R02/R03/R04` retain important thresholds and edge cases for Second Pass; their openness does not authorize unrecorded waivers of the mandatory baseline.

## 8. Core negative criteria — `NOT_MET`

| ID | Negative / counter-evidence condition |
|---|---|
| `XTR-N01` | Material informational outputs lack explanations necessary for their intended interpretation. |
| `XTR-N02` | Explanations consist only of technical details uninterpretable by the relevant consumers. |
| `XTR-N03` | Material derivations, analytical assumptions or contributing factors cannot be inspected at the required level. |
| `XTR-N04` | Required explanations are confined to inaccessible internal tools, tribal knowledge or undocumented access routes. |
| `XTR-N05` | A consuming machine or oversight contract requires structured explanatory evidence, but that evidence is unavailable. |
| `XTR-N06` | Material uncertainty, exclusions, assumptions, caveats or limitations are suppressed or misleadingly presented. |
| `XTR-N07` | Explanations materially contradict the executed method, governing semantics or actual Product behaviour. |
| `XTR-N08` | Material informational claims cannot be meaningfully inspected or challenged where required by context or competent authority. |
| `XTR-N09` | Explanations or evidence are misattributed, stale or not reliably bound to Product/Version, result or governing realization. |

**Interpretive safeguard.** A demonstrated foundational negative can support `NOT_MET`; a proven non-foundational deficiency can support `PARTIAL`, subject to the D02 test. Do not infer observed absence merely from a missing attachment. For example, if a system is known to publish false explanations despite a correct result, `XTR-N07` is not a mere evidence gap. Conversely, where the assessor lacks access to the explanation endpoint, that may be `EVIDENCE_LIMITED` until the relevant access or capability is established.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

- **`MET`:** all eight XTR-M01–XTR-M08 are adequately evidenced for the exact eligible Product/Version and material consumption contexts.
- **`PARTIAL`:** genuine contextual explainability exists with *demonstrated non-foundational* defects in structure, depth, availability, contribution detail or verification. Do not average criteria.
- **`NOT_MET`:** a foundational explanation requirement is demonstrably absent, such as opaque consequential results, explanations limited to uninterpretable technical details, or materially inaccurate explanations.
- **`EVIDENCE_LIMITED`:** independent uncertainty qualifier where evidence is missing, stale, incompatible or unlinked; this is neither automatic failure nor automatic success.
- **`NOT_ASSESSABLE`:** D02 Product/Version eligibility cannot be established.
- **`NOT_APPLICABLE`:** no general exemption established for IPCH15; specific explanation restrictions or modalities require independently competent treatment.

**Preserved AIPCH16 edge examples (not yet INFOPS verdicts):** LIME/SHAP feature importance alone `PARTIAL`; natural-language-only without structure `PARTIAL`; contextual and structured API-accessible explanation `MET`; high-risk AI without sufficient explanation `NOT_MET`. These examples use AI-specific conditions; do not import their labels mechanically into an Information Product case. The human-readable-but-unstructured case is especially unresolved for Information contexts (`XTR-R03`). The risk reference is not authorization for an AI R0–R4 classification mandate (`XTR-R04`).

**Per-result versus reusable explanation**: a deterministic calculation might be explained through a product-level governing methodology and per-result inputs. Whether reusable contract evidence can satisfy an output-specific requirement remains `XTR-R02` OPEN. **Explanation that is technically accurate yet materially useless**: mere equation publication or model weights may not satisfy the contextually meaningful claim. **Protected sources**: a lawful restricted explanation may be sufficient when the authorized consumer or oversight party can obtain necessary meaning; neither blanket disclosure nor blanket suppression is established by the current baseline (`XTR-R08`).

## 10. Evidence signals and sufficiency

**D37-approved evidence register:**

| Evidence ID | Supports | Sufficiently attributable evidence claim |
|---|---|---|
| `XTR-ES01` | XTR-M01 | Product-bound explanation scope, relevant consumers/material results, versioned obligations and competent governance context. |
| `XTR-ES02` | XTR-M02 | Representative actual consumer-facing explanations demonstrating contextually intelligible meaning and limitations. |
| `XTR-ES03` | XTR-M03 | Contributing sources, material derivations, analytical choices, exclusions and assumptions traceable to results. |
| `XTR-ES04` | XTR-M04 | Governed Product explanation ports/linked facilities, access contracts and evidence of actual availability to applicable consumers. |
| `XTR-ES05` | XTR-M05 | Structured explanation fields, descriptors, governed references and evidence of machine/oversight interpretability where applicable. |
| `XTR-ES06` | XTR-M06 | Approved context-dependent depth, uncertainty, omissions and limitations with evidence of appropriate disclosure. |
| `XTR-ES07` | XTR-M07 | Faithfulness/consistency checks, result-method alignment and challenge/inspection mechanism evidence. |
| `XTR-ES08` | XTR-M08 | Exact Product/Version, semantic and method revisions, explanation-contract identity, result/occurrence, realization/time and evidence provenance. |

**Evidence strength.** A sample Product output and its actual explanation are more directly relevant than a slide promising future explanations. A valid explanation API contract supports accessibility design, while independent exercised interface evidence supports actual accessibility. Structured fields are not enough if they contain invented or irrelevant rationale. A technically correct lineage trace may be supporting evidence rather than sufficient contextual explanation.

**Relevant fields without mandated schema:** Product identifier and Version; output class/result identity; consumer or oversight context; relevant meaning and analytical-method revisions; explanation fields and human interpretation; contributing factors and caveats; explanation source and timestamp; realization and occurrence; assurance/test evidence and its currency; permitted access/redaction status. The guide does not prescribe an explanation ontology, runtime API shape or test harness.

**No fabricated assurance:** an approved D37 criterion, a formalized XTR test proposition or a design-only record must not be reported as an executed fidelity check. Report exactly which explanation fields or effects were observed and which remain inferential. A representative result from one Product Version does not prove a different Version's explanations remain valid.

## 11. Agent-assisted or human assessment decision rule

An authorized assessor may follow this **proposed research decision procedure**, without executing it in First Pass:

1. Verify independently eligible **Information Product/Version**. If unestablished, `NOT_ASSESSABLE` under D02; do not qualify the Product through IPCH15.
2. Establish material output classes, designated consumers, consuming decision contexts and competent transparency/disclosure obligations. Distinguish local/result-specific and global/methodological explanation requirements.
3. Fix the evidence identities: Product/Version, meaning definition, analytical method revision, explanation contract, realization and output/occurrence identity where relevant. Do not substitute service endpoint version for Product Version.
4. Inspect all `XTR-ES01`–`XTR-ES08` independently and associate evidence with `XTR-M01`–`XTR-M08`. Identify direct observed explanation results versus future designs and assertions.
5. Probe applicability and negative evidence (`XTR-N01`–`XTR-N09`), including meaninglessness of technical-only explanations, missing material assumptions, inaccessible explanations and contradiction between stated rationale and actual derivation.
6. Test contextual adequacy of representative material explanations through the perspectives of intended users and competent oversight; do not require AI model explanations when there is no AI model.
7. Preserve all OPEN research: `XTR-R02` per-output granularity, `XTR-R03` text-only partial, `XTR-R04` risk/context depth, `XTR-R05` derivation detail, `XTR-R06` fidelity and `XTR-R08` protected disclosure. Do not adjudicate source tensions without owner-led Second Pass.
8. Form the D02 qualitative result from the conjunction and established counter-evidence. State separate `EVIDENCE_LIMITED` uncertainty rather than silently inventing access, assertions or test results.
9. Apply D03's experimental **characteristic-level** score only after the categorical finding; no arithmetic averaging of XTR criteria.
10. Record provenance, unresolved objections, re-assessment triggers and any referral to semantic, policy, privacy, legal or assurance authorities. The human owner or competent assessor retains accountability.

**Simplified rule:** `MET` requires the assessed Product to make relevant explanatory content actually understandable, accessible, structured, proportionate, faithful and attributable. A Product that is merely well documented or richly instrumented is not automatically explainable; no design-only assurance can establish an operating conclusion.

## 12. PMDD scoring treatment

| D02 outcome | D03 experimental characteristic-level treatment | Prohibition/qualifier |
|---|---|---|
| `MET` | `1.0` | Requires adequate evidence for all eight mandatory claims. |
| `PARTIAL` | `0.5` | Genuine implementation with established non-foundational deficiencies; source edge outcomes remain research hypotheses. |
| `NOT_MET` | `0.0` | Requires demonstrated foundational non-adherence; not merely lack of a reviewed file. |
| `EVIDENCE_LIMITED` | Independent uncertainty qualifier | Not a substitute score or maturity finding. |
| `NOT_ASSESSABLE` | No characteristic score | Product/Version qualification has not been established. |
| `NOT_APPLICABLE` | No generic whole-characteristic exception | Any narrow exception requires competent authority and evidence. |

No per-criterion scoring, weighted average, arithmetic substitution of `PARTIAL`, automatic maturity cap, L0–L2 maturity band, imported AI risk scale, XAI-technology adoption threshold or new normative grading rule is approved. AIPCH16's illustrative PARTIAL cases are retained for challenge, not mechanically imposed as IPCH15 decisions.

## 13. Critical assurance and governance boundaries

**Productness.** BPS/PIN generic Productness, Information Product-family and Compound qualification, and INFOPROD/INFOPDS relationships remain independently authoritative. Explainability scoring cannot promote an arbitrary report or model to a Product.

**Semantics and computation.** GEARA/GEARM and competent domain authorities govern material semantic/analytical definitions. XTR evidence must reference applicable versions but does not authorize local revision or reinterpretation of those definitions. Analytical-method revision, code and implementation choice are not simply Product-Version synonyms.

**Product contracts and implementation.** DPP may supply explanation contracts, metadata or evidence references; PFI/HDIP may realize explanation and evidence services. These architectures and design-only research do not alone prove deployed or faithful explanations. Tests, evidence and operational assurance require their independently authorized execution.

**Access and protected information.** Competent legal, privacy, security, confidentiality, IP and policy authorities control permitted disclosures. An assessor cannot demand illegal disclosure or infer a blanket right to reveal proprietary sources. Nor may an operator use confidentiality as a blanket excuse for materially misleading explanations where a legitimate authorized explanation is required. `XTR-R08` remains open.

**AI and decision authority.** AIPCH16's LIME/SHAP examples, R0–R4 risk tiers and AI model explanations are not imposed on non-AI Information Products. Explanations support interpretation and review; they are not independent authorization for a regulatory, credit, treasury or other consequential action. AI can assist with evidence analysis and drafting but has no autonomous institutional authority.

**Parent holds unchanged.** D01–D38 history retained. Parent Track B B01 completion `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`. Effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE`, safeguards F01.6/F01.29; distinct historical approval ledgers **65/6/7/7**, independent PC ledger unchanged; Q0–Q5 and F06/F14/F16 unresolved; 62 approved G06 E0 research designs **UNEXECUTED**; E1/E2 executions 0/0; G06-RO01–RO12 and G03-R01–R12 all 24 OPEN. No normative or Second-Pass authorization is implied.

## 14. Reassessment and evolution triggers

Reassess explanatory sufficiency when a material Product Version, analytical or semantic definition, transformation method, inclusion/exclusion rule, intended consumer, port/output modality, explanation contract, realization dependency, data availability, uncertainty or policy obligation changes. A new result population or consequential use context may require new examples even when the global explanation contract remains unchanged.

A change to an upstream Data Product may alter the contributing factors, data quality and caveats without immediately altering the Information Product's governed Version. The assessor must preserve the exact evidence and relevant revisions rather than assume every source change is a Product Version change. Conversely, a material informational-meaning change must not be obscured in a technical revision. Reassessment triggers do not confer semantic-change authority.

An explanation that was accurate under one method revision may become inaccurate after a derivation change. Revalidating its faithfulness may require authorized operational tests; this E0 guidance cannot claim they occurred. Historical explanation evidence should remain explicitly time- and occurrence-linked, with limitations, rather than silently rolled forward.

## 15. Adversarial and boundary cases — First-Pass fixtures

These **D37-retained research fixtures are proposed and UNEXECUTED**. They are not empirical maturity findings; proposed review directions are hypotheses for future authorized Second Pass.

| Fixture | Adversarial challenge | Expected research distinction |
|---|---|---|
| `XTR-A01` | Trusted measure reported without adequate derivation explanation | Trust and semantic meaning do not automatically establish interpretability of the result. |
| `XTR-A02` | Shared semantic alignment, opaque calculations | IPCH11 source meaning versus IPCH15 output derivation. |
| `XTR-A03` | Accurate human-readable prose but no structured explanation | AIPCH16 `PARTIAL` versus human-only context adequacy; `XTR-R03` OPEN. |
| `XTR-A04` | Structured contextual explanation through governed output port | Candidate full conformance, subject to fidelity and all eight claims. |
| `XTR-A05` | Explanation only in an internal engineer notebook | Product-level accessibility versus isolated internal documentation. |
| `XTR-A06` | Deterministic count uses one reusable, versioned explanation contract | Per-result provenance versus global contract; `XTR-R02` OPEN. |
| `XTR-A07` | Explanation uses specialist features or jargon | Technical visibility versus consumer comprehension. |
| `XTR-A08` | Material exclusions/assumptions omitted | Required interpretive uncertainty and transparency depth. |
| `XTR-A09` | Fluent narrative materially contradicts executed calculations | Explanation consistency/fidelity versus plausible but incorrect narrative. |
| `XTR-A10` | Consequential information with weak uncertainty explanation | Competent proportionality and protected disclosure, without adopting AIPS R0–R4. |
| `XTR-A11` | Legitimate confidentiality restricts some evidence | Authorized challengeability versus unrestricted disclosure; `XTR-R08` OPEN. |
| `XTR-A12` | Explanation exists but is attached to wrong Product Version/output | Evidence identity and temporal correctness precede maturity conclusions. |

AIPCH16's four illustrated edge-case findings are source evidence for research design, not evidence that these INFOPS fixtures have been run or that their outcomes are settled. No E1/E2 execution, operational explanation endpoint query, real Product assessment or adversarial test has been performed.

## 16. Source provenance, open questions and status

### Open research register — `XTR-R01`–`XTR-R08`

| ID | D37-retained research question | Status |
|---|---|---|
| `XTR-R01` | What minimum Information Product explainability requirements follow from AIPCH16 when no corresponding DPCH15 source exists in the supplied catalogue? | **OPEN** |
| `XTR-R02` | When must explanations accompany individual informational results versus a reusable versioned explanation contract? | **OPEN** |
| `XTR-R03` | Can natural-language-only explanations support MET in a human-only context despite AIPCH16's `PARTIAL` example, or is structured machine-referenceability universally required? | **OPEN** |
| `XTR-R04` | How is explanation depth proportionate to context, competence and consequence without unapproved AI R0–R4 risk tiers? | **OPEN** |
| `XTR-R05` | How much derivation detail and analytical provenance is sufficient without universal disclosure of protected implementation internals? | **OPEN** |
| `XTR-R06` | How should faithfulness to actual calculations, source evidence and runtime behaviour be established for deterministic, nondeterministic or AI-assisted derivations? | **OPEN** |
| `XTR-R07` | How are exact Product/Version, semantic definition, analytical method, explanation contract, realization, output occurrence and evidence distinguished and linked? | **OPEN** |
| `XTR-R08` | How should explainability coexist with privacy/security/confidentiality, IPCH05/06/09/11/13 and separate competent authorities without circularity? | **OPEN** |

### Sources, approved authority and interpretation limits

- **Direct source:** `AIPCH.zip` → `AIPCH-PMDD-guidance/16-AIPCH16.md`. AIPCH16 describes local/global/contextual explanations, product interface accessibility, structured machine use, proportionality, consistency and the four named AI Product edge cases. Its original AI behaviour and model-centric statements are not automatically universal Information Product requirements.
- **Missing corresponding source:** Directly inspected `DPCH.zip` catalogue includes DPCH01–DPCH14; no corresponding DPCH15. Absence is a *catalogue coverage limitation*, not proof of nonexistence anywhere or of absence of Data Product transparency obligations.
- **Owner authority:** `INFOPS-0.1-IPCH-P01-D37-F01`, F01.1–F01.16 `APPROVED_EXPERIMENTAL_E0`: approved Information-specific definition, XTR-M01–M08 mandatory conjunction, XTR-N01–N09, XTR-ES01–ES08, XTR-A01–A12 unexecuted and XTR-R01–R08 OPEN; authorized preparing this document; D38 separately accepted the experimental draft only.
- **Guidance pattern:** D04 sixteen-section template; D05 original order preserved historically despite the accountable owner's numerical First-Pass progression.

### Exact decision and execution statuses

| Subject | Status |
|---|---|
| D37 criteria/authority | `APPROVED_EXPERIMENTAL_E0` |
| `IPCH15.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` (D38; experimental only) |
| Guide owner acceptance (D38) | `APPROVED_EXPERIMENTAL_E0` (draft only) |
| XTR-M01–M08 | D37-approved **mandatory conjunctive** |
| XTR-N01–N09 and XTR-ES01–ES08 | D37-approved First-Pass registers |
| XTR-A01–A12 | Proposed **UNEXECUTED** |
| XTR-R01–R08 | **OPEN** |
| IPCH15 overlay and repository deployment | `PREPARED_VERIFIED` / `NOT_DEPLOYED` |
| Empirical explanation assessment / Second Pass | `NOT_EXECUTED` / `NOT_STARTED` |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| IPCH16 | `NOT_INITIATED` |

**First-Pass checkpoint:** IPCH01–IPCH15 guides prepared and owner-accepted (15/16). IPCH01–IPCH03 experimental deployments previously confirmed; IPCH04–IPCH15 overlay packages prepared, with IPCH04–IPCH14 deployments unconfirmed and IPCH15 not deployed. All outstanding IPCH01–IPCH14 research, review and authority limitations remain preserved.

**Stop condition:** D38 accepted the experimental draft and the incremental IPCH15 overlay is `PREPARED_VERIFIED`, `NOT_DEPLOYED`. Do not infer deployment, real Product assessment, adversarial or fidelity execution, IPCH16 initiation or normative-release authority.
