# IPCH16 — Interoperable & Composable: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH16-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Principal directly inspected source:** `AIPCH20 — Interoperable & Composable`; **corresponding DPCH characteristic:** `NOT_FOUND_IN_SUPPLIED_DPCH01-DPCH14_CATALOGUE`  
> **Decision authority:** `INFOPS-0.1-IPCH-P01-D39-F01 = APPROVED_EXPERIMENTAL_E0` (criteria baseline); `INFOPS-0.1-IPCH-P01-D40-F01 = APPROVED_EXPERIMENTAL_E0` (experimental draft acceptance only)  
> **Document status:** `DRAFT_PREPARED_ACCEPTED`; owner acceptance `APPROVED_EXPERIMENTAL_E0` under D40 (experimental draft only)  
> **Overlay:** `PREPARED_VERIFIED` (documentation-only ZIP); **deployment:** `NOT_DEPLOYED`; **First-Pass closure:** `NOT_AUTHORIZED`; **Second Pass:** `NOT_STARTED`; **final guide approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

**Nature of artifact.** This is experimental First-Pass guidance to assess interoperability and composability of a *separately qualified* Information Product/Version. It is not an assessment of a real Product, evidence that multi-Product composition has occurred, a qualification of a new Product, a Compound determination, a platform design, a policy waiver or a normative specification. The owner approved D39 F01.1–F01.16 as the experimental criteria baseline and authorized drafting this guidance. D40 separately accepted the prepared sixteen-section experimental draft as `DRAFT_PREPARED_ACCEPTED`. This ZIP is a prepared incremental documentation overlay only; no target-repository modification or deployment is claimed.

**Constitutive distinction.** Direct Product consumption, federated/orchestrated use of existing Products, and the intentional creation of a new Product through Productized Composition are separate events. Interoperability does not itself imply the third. Qualification and Product-family classification are independently governed. The criterion language below is an Information Product derivation; AIPCH20's specific Derived AI Product, AQE and APT rules are **not** automatically Information Product qualification requirements.

## 1. Characteristic identity and source lineage

| Field | First-Pass identity |
|---|---|
| Characteristic | `IPCH16 — Interoperable & Composable` |
| Authority for baseline | `D39-F01`, F01.1–F01.16 `APPROVED_EXPERIMENTAL_E0` |
| Prepared artifact | `IPCH16.md / FIRST-PASS-DRAFT-01` |
| Principal inspected source | `AIPCH.zip` → `AIPCH-PMDD-guidance/20-AIPCH20.md` |
| DPCH corresponding characteristic | None identified in supplied `DPCH.zip` DPCH01–DPCH14 catalogue |
| Mandatory criteria | `IOC-M01`–`IOC-M08`, conjunctive with applicable conditional derived-Product obligations |
| Negative criteria | `IOC-N01`–`IOC-N09` |
| Evidence requirements | `IOC-ES01`–`IOC-ES08` |
| Research obligations | `IOC-R01`–`IOC-R08` OPEN |
| Adversarial fixtures | `IOC-A01`–`IOC-A12` proposed, UNEXECUTED |

**Direct AIPCH20 assertion.** The source states: “The AI Product can participate safely in governed multi-product use and composition through stable semantic contracts.” It distinguishes direct use, federated/orchestrated consumption and a new Product formed using upstream Products. It warns: “Composition behavior does not automatically create another AI Product.” Its positive criteria specify stable, machine-understandable governed ports/contracts, sufficient semantic alignment, persistent dependency and policy boundaries, visible ownership/currentness during orchestration, separate owner/Product identity/AQE/APT for an actually created Derived AI Product, and correct use without internal implementation knowledge. Negative examples include bespoke glue code per integration, unsafe semantic mismatch, disappearing trust/policy boundaries, misregistered orchestration and missing genuine derived-Product dependency topology. Evidence signals include consumption ports/schemas, semantic mappings, dependency and currentness graphs, derivation topology, policy inheritance and composition tests.

**Source discipline.** AIPCH20 has no standalone scenario matrix defining `PARTIAL` for Information Products; the D02 qualitative interpretations herein are **D39-approved INFOPS experimental synthesis**, not a quotation or source-derived resolution. AIPCH20's mention of a Derived AI Product's distinct governed *intelligence proposition* and AQE/APT must not be recast as an automatic INFOPS derived/Compound Product classification. The absence of a DPCH named counterpart in the supplied catalogue does not establish that Data Products lack interoperability requirements elsewhere. See `IOC-R01`, `IOC-R05`, `IOC-R06`.

## 2. What the characteristic really asserts

> **D39-approved experimental Information Product definition:** An Information Product is Interoperable & Composable when its governed informational capabilities can be independently discovered, accessed, interpreted and combined through stable, machine-understandable semantic and consumption contracts; material dependency, provenance, version, policy and consumer obligations remain identifiable and enforceable across integration and composition boundaries; and direct consumption, ordinary orchestration and the intentional creation of separately qualified derived or compound Products remain explicitly distinguishable without requiring consumers to reconstruct internal implementations.

The claim is **safe independent participation in governed Product ecosystems**, not merely a deployed API, schema conformity, broad actual adoption, or technical feasibility of joining outputs. An Information Product can be addressable (IPCH10) but semantically unsafe to combine, semantically aligned in isolation (IPCH11) but opaque concerning upstream dependencies, or reusable (IPCH07) but require undocumented bespoke integration. The question is whether its governed contracts permit reliable combination while preserving meaning, dependencies, policies and separate Product authority.

Composition must not erase Product provenance, introduce unapproved semantics or create unqualified Product identities. A consuming workflow can assemble several independently governed outputs without itself becoming a Product. A distinct informational proposition intentionally constituted as a Product requires independent generic Productness and Information-family/Compound determination; IPCH16 does not confer that status. **Design intent, deployed interface, observed consumption, actual multi-Product composition and independent new-Product qualification are different claims.**

## 3. Information Product specialization

Information Products convey interpreted/derived information: informational measures, contextual assumptions, time windows, classifications, analytical assertions and consumption-ready meanings. Consequently, schema compatibility alone cannot prove interoperability. Identical fields `Amount`, `Currency` and `AsOfTime` could represent unrelated liquidity, exposure or market-risk concepts; equal metric names could conceal inconsistent exclusions or calculation periods. Information-specific composition checks must inspect material semantics, analytical assumptions, time bases, granularity, jurisdiction, applicable versions and consumer interpretation. They must not secretly redefine upstream authoritative concepts.

**Three modes** should remain independently identified:

1. **Direct consumption:** a consumer accesses an existing Information Product via an authorized port and contract. No additional Product is inferred. Ordinary consumer-specific presentation or client-side transformation does not alone establish a new Product.
2. **Federated/orchestrated consumption:** two or more already governed Products are queried, routed, displayed or coordinated in one workflow or dashboard. Their source identities and restrictions survive; orchestration alone is not Productized Composition.
3. **Productized Composition:** a new independently constituted Product is claimed, with a distinct Promise, accountable owner, identities, ports/contracts, material dependency topology, currentness and competent qualification. A source Product may belong to Data, Information or AI families; the new Product's family follows independent authority, not automatic inheritance.

**Illustration, not assessment.** A treasury application combines intraday liquidity, counterparty exposure and market-risk Information Products in a dashboard. The dashboard's composition is not by itself a new Information Product. An intentionally constituted *Enterprise Liquidity-at-Risk* Information Product could be a candidate for independent qualification if it promises a distinct governed analytical capability; IPCH16 may evaluate its compositional interoperability only after the appropriate qualification boundary is respected.

**Technology neutrality.** Neither a universal semantic language, orchestration platform, API technology nor a single product registry is required by D39. Governed contract equivalence and meaningful machine-understanding are the evidentiary questions. Cross-family integration does not blend upstream Productness or policy authority.

## 4. Assessment subject and authority

**Subject.** The exact independently eligible Information Product/Version, its material output ports, governing consumption and semantic contracts, relevant consuming/composing contexts and composition-related obligations. Distinguish the assessed source Product from any consumer application, orchestrator, candidate new Product and upstream dependencies.

**Assessment procedure:**

1. Establish Product/Version eligibility under competent BPS/PIN and Information Product-family authorities. If eligibility is not established, use D02 `NOT_ASSESSABLE`, not a guessed IPCH16 maturity score.
2. Identify governing Product/Version, material ports, semantic-definition references, analytical/temporal assumptions, dependency versions and independently established policy constraints.
3. Classify the *actual* interaction mode: direct use, orchestration/federation, or separately claimed Productized Composition. Do not infer mode from tooling names such as “router,” “pipeline” or “dashboard.”
4. Evaluate each applicable IOC mandatory criterion using Product-bound observations and competent evidence; explicitly distinguish design-only E0 evidence from executed consumption/composition outcomes.
5. When a new Product is asserted, require separately competent generic Productness, Product-family/Compound and applicable governing decisions. IPCH16 can identify a missing determination but cannot issue the determination itself.
6. Link all evidence to exact subjects, versions, applicable times and realization/occurrence contexts. Record limits and contradictions rather than combining them into a fabricated conformance statement.

**Authority partition.** BPS/PIN governs generic Productness; competent Product-family and Compound authorities govern qualification. GEARA/GEARM and domain authorities govern shared semantics and analytical meaning. INFOPROD/INFOPDS and DPP govern their separate Product/specification and protocol boundaries. PFI/HDIP and relevant platform authorities govern implementation/realization. Policy, privacy, security, legal and assurance authorities govern obligations and consequential approvals. AIPCH20's AQE/APT requirements are AI-family source-specific and **not** conferred on INFOPS by analogy.

## 5. Applicability and N/A rules

IPCH16 is presumptively applicable to an independently qualified Information Product regardless of whether it has so far participated in an observed multi-Product composition. **IOC-M07 is mandatory in its boundary-control function**, but its *new derived-Product* evidence branch is conditional on a genuine new-Product claim. Do not invent a derived Product to force evidence of a condition that has not occurred. Conversely, do not claim M07 is universally satisfied merely because no new Product is asserted: the assessor must still verify that ordinary consumption/orchestration is not misrepresented as Product creation and that applicable claims are correctly routed.

For `IOC-M01`–`IOC-M08`, **MET requires evidence adequate to all applicable mandatory assertions**. Whether unexecuted but well-defined composition contracts can suffice for full maturity, or whether at least one observed integration must exist, is unresolved as `IOC-R02`. No generic characteristic-level `NOT_APPLICABLE` is approved. Conditional M07 branch treatment is an applicability determination within the mandatory criterion, not a whole-IPCH exemption or an unauthorized scoring shortcut.

`NOT_ASSESSABLE` applies if Product/Version eligibility has not been independently established. `EVIDENCE_LIMITED` is a separate qualifier when evidence is absent, stale, conflicting or unbound, not a substitute score. `PARTIAL` requires a genuine demonstrated capability with a non-foundational deficiency, not the mere presence of an interface spec. Evidence from approved E0 architectural designs alone must not be promoted into actual composition test evidence or observed interoperability.

## 6. Distinctness and non-duplication

| Adjacent characteristic or authority | Independent claim; boundary of IPCH16 |
|---|---|
| IPCH03 Declarative | Product definition and governance-as-code versus safe inter-Product contract use and composition. |
| IPCH05 Self-Describing | Product documentation/discoverability of its meaning versus independently executable composition contracts. |
| IPCH06 Trustworthy | Product trust assurance versus preservation of trust-relevant dependencies and obligations when combining Products. |
| IPCH07 Reusable | Demonstrated multiple-context adoption versus contract-safe multi-Product participation; actual reuse alone does not establish safe composition. |
| IPCH09 Compliant by Design | Product's direct compliance obligations versus their survival across federated or composed use. |
| IPCH10 Addressable | Independent access through governed ports versus interoperable meaning and composite compatibility. |
| IPCH11 Semantically Aligned | Authoritative Product-level semantic anchoring versus semantic compatibility and stability *across* Products and consumption contexts. |
| IPCH12 Consumption-Driven Intent | Product purpose and evolution versus correctness of interaction among independently governed Products. |
| IPCH13 Testable & Versioned | Product change gates and regression tests versus specific cross-Product dependency/contract preservation; shared evidence may support separate claims. |
| IPCH15 Explainable & Transparent | Explainability of informational results versus safe dependency/provenance propagation across composition. |
| BPS/PIN Productness | Determines whether an independently qualified Product exists; IPCH16 cannot create Productness. |
| Product-family / Compound qualification | Determines family, Compound status and derived Product qualification; never inferred solely from orchestration. |
| GEARA/GEARM | Governs semantic and analytical meaning; IPCH16 cannot authorize ontology changes. |
| Policy/assurance authority | Establishes applicable controls and waivers; IPCH16 evaluates continuity only. |

**Anti-circularity.** IPCH16 `MET` must not be awarded because IPCH10/11/13 are claimed `MET`; each criterion needs direct composition-specific evidence where applicable. Nor does an IOC result retroactively prove those neighbouring characteristic scores. A composition that includes another Product family must not turn that family's qualification into an INFOPS maturity conclusion.

## 7. Core mandatory positive criteria — `MET`

**D39-approved mandatory, conjunctive baseline:** assessment evidence must support each applicable criterion for the exact eligible Product/Version. Conditional new-Product obligations under M07 depend upon applicable claims; the boundary-control criterion remains mandatory. There is no criterion-level score averaging.

| ID | Mandatory criterion | Required Product-level demonstration |
|---|---|---|
| `IOC-M01` | **Governed Interoperability and Composition Contracts** | Stable, sufficiently machine-understandable ports, schemas and contracts enable authorized independent use and applicable composition. |
| `IOC-M02` | **Semantic Compatibility for Safe Combination** | Material informational concepts, measures, time bases, assumptions and interpretations are compatible or differences are explicitly governed and usable without unsafe equivalence. |
| `IOC-M03` | **Dependency and Provenance Preservation** | Upstream Product identities, versions, currentness, dependency topology and material informational provenance remain identifiable through use and composition. |
| `IOC-M04` | **Policy and Consumer-Obligation Continuity** | Applicable rights, permitted uses, confidentiality, security, privacy, licensing, retention and other obligations survive relevant integration modes. |
| `IOC-M05` | **Independent Consumption Without Implementation Coupling** | Consumers can consume and, where applicable, combine through published governed contracts without undocumented internals, continuous bespoke producer help or per-consumer ungoverned integration. |
| `IOC-M06` | **Coherent Composition Modes and Product Boundaries** | Direct use, federation/orchestration and intentional Productized Composition are correctly distinguished; coordination alone is not falsely asserted as Product creation. |
| `IOC-M07` | **Governed Derived-Product and Compound Boundaries** | Any actually claimed new Product is independently qualified with relevant identity, owner, Promise and dependency topology, under appropriate Product-family/Compound competence; absent claims are not fabricated. |
| `IOC-M08` | **Product-Level Interoperability Evidence Integrity** | Contracts, mappings, dependencies, policy continuity and composition evidence bind exact Product/Version, contract/dependency versions, realization/occurrence, context and effective time. |

**Foundational tests of reasoning.** A single machine-readable schema may meet only part of M01, not the full conjunction. A semantic registry link does not prove M02 in an incompatible consuming context. A dependency diagram is not proof that provenance survives actual multi-Product use. A new-Product registration without separate competent qualification is not evidence for M07. Each assertion must be established through suitable evidence without deriving one criterion's result from another's presumed status.

**Modes do not imply a universal execution requirement.** M06/07 must preserve accurate distinctions and competent authority in the actual scope. Whether additional observed multi-Product use is required for MET remains `IOC-R02` OPEN; no experimental maturity shortcut is created here.

## 8. Core negative criteria — `NOT_MET`

D39-approved negative conditions identify potential demonstrated failure. Their presence must be evaluated for materiality and evidence credibility under D02, not counted arithmetically or inferred from mere missing artifacts.

| ID | Negative counter-evidence | Why it matters |
|---|---|---|
| `IOC-N01` | Every new integration requires undocumented bespoke glue, implementation coupling or direct producer intervention. | No genuinely independent interoperable contract exists. |
| `IOC-N02` | Technical schema compatibility conceals material semantic or temporal mismatch creating unsafe results. | Syntactic fit is not informational interoperability. |
| `IOC-N03` | Composition obscures upstream Product identities, versions, material dependencies or provenance. | Trust/currentness cannot be established across boundaries. |
| `IOC-N04` | Applicable privacy, purpose, access, licensing or security obligations are lost or improperly relaxed. | Policy continuity fails; no waiver authority is inferred. |
| `IOC-N05` | Consumers need undocumented internals or producer-specific conventions to use the Product correctly. | The contract is not independently consumable. |
| `IOC-N06` | Router, dashboard or orchestrator is declared a new Information Product solely because outputs were assembled. | Invalid Product boundary/qualification inference. |
| `IOC-N07` | Claimed derived/Compound Product lacks separately established owner, identity, Promise, topology or competent qualification. | Productized Composition is falsely or incompletely established. |
| `IOC-N08` | Material contract/dependency evolution breaks legitimate compositions without governed compatibility disposition. | Multi-Product safety degrades under change. |
| `IOC-N09` | Composition evidence is attributed to the wrong Product/Version, semantic/port contract, dependency or occurrence. | The asserted conformance has no reliable evidence subject. |

**Evidence discipline.** A missing dependency graph is not by itself proof that one does not exist; it can be an evidence limitation. Demonstrably discarded upstream policy obligations are an actual negative, not merely missing documentation. Where a consumer builds custom transformations by choice despite a capable published Product contract, distinguish the consumer implementation from inherent Product coupling; relevant factual evidence is required.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

AIPCH20 does not directly prescribe a separate `PARTIAL` matrix for Information Products. The following is **INFOPS D39-approved First-Pass interpretation only** and not a claim of observed outcomes.

| Candidate finding | Qualitative evidence meaning |
|---|---|
| `MET` | All eight mandatory criteria adequately evidenced, with M07 conditional obligations evaluated against actual Productized Composition claims; unresolved `IOC-R02` limits premature full-maturity assertions. |
| `PARTIAL` | Genuine governed interoperability established but specific, evidenced **non-foundational** deficiencies remain in coverage, portability, mapping, provenance, compatibility or evidence practices. |
| `NOT_MET` | Demonstrated foundational failure such as unsafe semantics, illegitimate Product qualification claim, material policy loss or systematic implementation coupling. |
| `EVIDENCE_LIMITED` | Separate qualifier for missing/stale/inconsistent evidence; cannot be converted mechanically to `PARTIAL` or `NOT_MET`. |
| `NOT_APPLICABLE` | No generic whole-IPCH exemption; determine condition-specific applicability under competent authority. |
| `NOT_ASSESSABLE` | Exact independently eligible Product/Version not established under D02. |

**Boundary examples (unexecuted):** (a) a reusable stable port with no observed composition raises `IOC-R02` and must not automatically be marked MET or NOT_MET; (b) two similarly named measures with incompatible as-of conventions may demonstrate foundational failure if consumers combine them unsafely; (c) a correctly labelled orchestrated workflow is not an unqualified derived Product; (d) genuine separately qualified derived information may be assessed for contract and policy preservation without IPCH16 granting qualification. The relative thresholds between `PARTIAL`, foundational `NOT_MET` and evidence-limited remain subject to future admissible Second-Pass research and case-specific evidence; criteria are not averaged.

## 10. Evidence signals and sufficiency

The D39-approved `IOC-ES01`–`IOC-ES08` register comprises **claim-specific** evidence requirements. No universal registry or specific document format is mandated. Source signals from AIPCH20 are separated from the INFOPS experimental elaborations.

| ID | Supports | Evidence expected | Evidentiary caveat |
|---|---|---|---|
| `IOC-ES01` | M01 | Product-bound governed ports, machine-readable consumption schemas, contracts and compatibility commitments | Contract existence ≠ deployed compatibility or actual use. |
| `IOC-ES02` | M02 | Referenced semantics, domain mappings, temporal/analytical interpretation, governed deviations and compatibility evaluation | Similar names or schemas do not establish semantic equivalence. |
| `IOC-ES03` | M03 | Upstream graph with Product/Version identities, provenance, revision/currentness and dependency context | Diagram without current/actual links is limited evidence. |
| `IOC-ES04` | M04 | Independently established usage/access/privacy/licensing obligations, inheritance mechanisms and appropriate control evidence | Policy must come from competent authority; implementation claims need support. |
| `IOC-ES05` | M05 | Independent consumption/integration evidence showing usable contracts without undocumented implementation knowledge | Design evidence does not establish observed operational success. |
| `IOC-ES06` | M06 | Explicit classification of direct, federated/orchestrated and intentional Productized Composition modes with supporting factual rationale | Labels cannot substitute for actual ontological/product-boundary determination. |
| `IOC-ES07` | M07 | Where legitimately applicable, separately competent new-Product identity, ownership, Promise, qualifying determinations and derived topology | AQE/APT are AIPCH20's AI-specific source examples, not universal INFOPS artifacts. |
| `IOC-ES08` | M08 | Exact subject/Version, contract revision, semantic-definition version, upstream versions, composition config, realization, time, occurrence and evidence provenance | Evidence from one version/occurrence does not automatically cover another. |

**Evidence sufficiency questions:** Which claims have direct observed evidence? Which are based only on approved E0 designs or specifications? Which dependent Product versions and policy scopes were active? Are semantics reconciled explicitly or merely assumed? Is there a consumer validation report, compatibility test or executed composition record where necessary? Is there independent qualification for a **new** Product claim? Are negative conditions disproved, not simply absent from documents?

**Source signals versus approved requirements.** AIPCH20 explicitly lists ports/schemas, ontology mappings, currentness/dependency graphs, AQE/APT derivation topology for Derived AI Product creation, policy inheritance and composition tests. INFOPS evidence identities and Information-family qualification boundaries are the D39 experimental specialization; they are not attributed as textual assertions of AIPCH20.

## 11. Agent-assisted or human assessment decision rule

**Proposed decision sequence — E0 research guidance, not an autonomously authoritative agent procedure:**

1. **Eligibility gate:** Independently verify exact Product/Version and family eligibility. Otherwise `NOT_ASSESSABLE`. Do not convert a router, workflow or raw data join into a Product by assigning a maturity score.
2. **Scope and mode:** Establish the Product's governed ports, consumers and material contexts. Classify direct consumption, ordinary orchestration or actual claim of new Productized Composition. Preserve the fact that these modes may coexist.
3. **Contract and meaning:** Examine machine-understandable contracts and material shared-semantic/analytical compatibility, including time, grain and consumer interpretation (`M01`, `M02`).
4. **Provenance and obligations:** Verify dependency identity/currentness and independently governed policy continuity (`M03`, `M04`). Do not claim authority to modify policy.
5. **Independent consumption:** Seek admissible evidence that contracts can be used without hidden internals or producer-specific intervention (`M05`). Record whether observed integration exists; `IOC-R02` remains OPEN.
6. **Product boundary:** Inspect accurate mode labelling (`M06`). If and only if a new Product is claimed, examine independently competent identity, owner, Promise, qualification and topology (`M07`). The assessor never issues that qualification.
7. **Evidence attribution:** Bind contracts, dependencies, policy and any execution/observation to exact Product/Version and realization/occurrence evidence (`M08`). Do not mix revisions or unsupported dates.
8. **Determine and qualify:** Evaluate D02 `MET`, `PARTIAL`, `NOT_MET`, `NOT_ASSESSABLE`, and `EVIDENCE_LIMITED` independently. Apply the D03 characteristic score only to justified scored findings. Record unresolved holds and decision authority.

**No autonomous governance.** ChatGPT or another assessment agent may be a research partner, evidence organizer, skeptical challenger and scribe. The accountable human owner/competent body alone makes the relevant governing disposition. A Product maturity score is neither normative approval nor permission for real-world consequential Product composition.

## 12. PMDD scoring treatment

**D03-approved experimental characteristic score:**

| Determination | Score | Basis |
|---|---:|---|
| `MET` | `1.0` | Adequate evidence for all mandatory conjunctive assertions, within applicable claims. |
| `PARTIAL` | `0.5` | Demonstrated real capability with non-foundational deficits; not an averaged number of criteria. |
| `NOT_MET` | `0.0` | Demonstrated foundational non-adherence. |
| `EVIDENCE_LIMITED` | No automatic numeric score | Independent confidence/coverage qualifier requiring accurate presentation. |
| `NOT_ASSESSABLE` | Not scored | Exact independently qualified Product/Version eligibility not established. |
| `NOT_APPLICABLE` | No default whole-IPCH exemption | A competent determination is required for actual applicability. |

No count-based ratio such as “six of eight criteria equals 0.75,” no automatic cap, and no characteristic L0/L1/L2 sublevels have been approved. One material negative condition may undermine a foundational claim, but the assessor must establish fact, applicability and materiality rather than automatically subtract a fixed amount. Source AIPCH20's positive/negative examples do not authorize numerical criterion weights.

**Cross-characteristic non-duplication.** Do not combine assumed IPCH07 reuse, IPCH10 addressability and IPCH11 semantic alignment scores as proof of IOC maturity. Evidence may be reused with proper provenance, but the claim assessed by each characteristic remains distinct. Overall PMDD aggregation, if any, is governed separately by D03; this guidance changes no such authority.

## 13. Critical assurance and governance boundaries

- **Generic Productness, Product families and Compound:** BPS/PIN and separately competent Product-family/Compound authority determine whether a candidate is a new Product and which family applies. An IPCH16 finding cannot register or qualify a new Product.
- **Cross-family dependence:** An Information Product may consume Data or AI Products, but their rights, semantic provenance and Product qualifications remain distinct. An AI-derived capability is not classified as an Information Product merely because it is orchestrated with one.
- **AI source qualifications:** AIPCH20's AQE/APT, *Derived AI Product* and materially distinct intelligence-proposition conditions are source-specific. They inform boundary research (`IOC-R06`) but are not transplanted into INFOPS authority.
- **Semantic/analytical competence:** GEARA/GEARM and competent domains control authoritative definitions, deviations and analytical meanings. Similar contract shapes do not authorize equivalence or redefinition.
- **Policy inheritance:** Privacy, security, usage purposes, licenses and retention requirements must be respected across contracts and composition. IPCH16 neither waives them nor grants unauthorized downstream access.
- **Separate Product/specification/protocol:** INFOPROD, INFOPDS and DPP roles are preserved; an API, descriptor or topology artifact is not synonymous with the Product or its realization.
- **Realization/compilation/runtime:** PFI/HDIP or other authorized platforms may implement contracts and collect evidence; design-only E0 approvals are not E1/E2 execution or conformance tests.
- **Human authority:** The owner is the sole accountable signatory within verified competence; AI co-design and record-keeping confer no institutional governance authority.

**Inherited parent restraints.** Parent Track B B01 completion `NOT_ESTABLISHED`; B02–B06 `NOT_AUTHORIZED`. Prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` and historical C06 `APPROVED_NOT_EFFECTIVE`, with F01.6/F01.29 safeguards. Original independent charter verification remains unresolved. Historical approval ledgers **65 / 6 / 7 / 7**, separate PC ledger unchanged; Q0–Q5 and F06/F14/F16 unresolved. All **62 G06 E0** designs approved but unexecuted; E1/E2 execution counts **0/0**. G06-RO01–RO12 and G03-R01–R12 remain **24 OPEN**. No release or test is implied.

## 14. Reassessment and evolution triggers

Reassess the exact Product/Version and material composition contexts when any of the following occurs:

- Material port schema, consumption contract, authentication or permitted-use change.
- Shared semantic-definition, mapping, analytical measure, time-window or interpretation change affecting compatibility.
- Upstream Product/Version, dependency topology, effective time, data source or currentness changes.
- New consumer integration requiring undocumented implementation knowledge or revealing per-consumer bespoke transformation.
- Material changes to privacy, licensing, purpose restrictions, retention or other policy obligations.
- A consuming orchestrator becomes a candidate for separate Productized Composition, or an existing derived Product claims altered owner, Promise or family classification.
- A breaking change, regression, policy inheritance issue, discovered unsafe semantics, stale evidence, or real-world incident affecting multi-Product consumption.
- Changed realization, compilation or runtime occurrence that affects observed interoperability; keep those revisions distinct from Product Version.
- New competent governance determination or admissible Second-Pass research clarifying IOC-R01–R08; no retroactive claim that those questions were resolved in First Pass.

A trigger calls for examination and attribution, not an automatic Product Version increment or an automatic maturity downgrade. Decisions about compatibility, release, Product qualification and policy remain with their separate competent authorities.

## 15. Adversarial and boundary cases — First-Pass fixtures

All twelve D39-retained cases are **conceptual unexecuted adversarial fixtures**. Illustrative outcomes are not test results, certified determinations or adopted exceptions.

| ID | Fixture | Assessment challenge / required discrimination |
|---|---|---|
| `IOC-A01` | Stable machine-understandable contract; no observed multi-Product composition | Contract capability versus observed composition; `IOC-R02` OPEN; no invented execution. |
| `IOC-A02` | Identical schemas with incompatible business meaning | Detect unsafe semantic equivalence, not mistake syntactic match for M02. |
| `IOC-A03` | Semantic compatibility but bespoke glue code per integration | Determine whether M05 foundational independent-consumption failure is evidenced. |
| `IOC-A04` | Dashboard orchestrates several Products without a new Product claim | Correctly treat as consumption; no extra Product qualification. |
| `IOC-A05` | Router registered as Derived Information Product solely for routing | Challenge false Product creation; independent qualification required. |
| `IOC-A06` | Candidate new Information Product with distinct Promise and independent qualification | Verify competent determination and dependency topology rather than assuming it. |
| `IOC-A07` | Composition loses upstream purpose restriction | Establish actual policy discontinuity under M04 without self-authorizing a waiver. |
| `IOC-A08` | Composition obscures upstream Product/Version | Test provenance and temporal integrity; avoid invented dependency lineage. |
| `IOC-A09` | Cross-family Products form a candidate new capability; family unresolved | Preserve family and Compound qualification; no automatic inheritance. |
| `IOC-A10` | Upstream contract/version changes without compatibility evaluation | Examine M01/M03/M08 and contractual protections without inventing test outcomes. |
| `IOC-A11` | Consumer needs undocumented Product internals | Examine contract sufficiency and M05 failure versus merely optional custom work. |
| `IOC-A12` | Composition results cannot be attributed to exact Product/Versions and occurrences | Distinguish evidence-limited case from demonstrated misattribution/failure. |

**Explicit nonexecution:** No real Product integration was run, no semantics reconciled operationally, no policy inherited at runtime under this research, no Product qualified, no E1/E2 assurance performed and no Second-Pass adversarial replay authorized. Proposed case outcomes must remain conditional on future admitted evidence and competent assessment.

## 16. Source provenance, open questions and status

### Open research register — `IOC-R01`–`IOC-R08`

| ID | D39-retained research obligation | Status |
|---|---|---|
| `IOC-R01` | What is a sufficient Information Product interoperability baseline when AIPCH20 is the direct source and the supplied DPCH catalogue has no corresponding characteristic? | **OPEN** |
| `IOC-R02` | What distinguishes a declared interoperability contract, demonstrated independent use and observed Productized Composition, particularly before composition has occurred? | **OPEN** |
| `IOC-R03` | How are semantic compatibility, informational measures, analytical assumptions, temporal contexts and cross-family meanings assessed without duplicating IPCH11? | **OPEN** |
| `IOC-R04` | How do dependency versions/currentness, upstream provenance and competent consumer/policy obligations survive federation and Productized Composition? | **OPEN** |
| `IOC-R05` | What exactly separates direct consumption, federated/orchestrated use, new Derived Information Product creation and separately qualified Compound Products? | **OPEN** |
| `IOC-R06` | How can AIPCH20's AQE/APT-specific Derived AI Product conditions inform Information-family evidence without importing AI-family authority? | **OPEN** |
| `IOC-R07` | How are exact Product/Version, semantic-definition version, port-contract revision, dependency versions, composition configuration, realization, compilation, runtime occurrence and evidence bound and distinguished? | **OPEN** |
| `IOC-R08` | How should IPCH16 interact with IPCH07/09/10/11/13, BPS/PIN, GEARA/GEARM, Product-family/Compound and policy inheritance without double-counting or circular determinations? | **OPEN** |

### Sources, approved authority and derivation limits

- **Direct inspected source:** `AIPCH.zip` → `AIPCH-PMDD-guidance/20-AIPCH20.md`. AIPCH20's exact conceptual scope, positive/negative examples, evidence signals and agent decision rule are the principal precedent. It does not supply a distinct `PARTIAL` assessment matrix for Information Products.
- **Corresponding-source limitation:** the supplied `DPCH.zip` contains `pages/DPCH-PMDD-guidance/01-DPCH01.md` through `14-DPCH14.md` and no named *Interoperable & Composable* counterpart; this is not proof none exists elsewhere or that Data Products have no relevant obligations.
- **Owner approved source specialization:** `INFOPS-0.1-IPCH-P01-D39-F01`, F01.1–F01.16, approved the Information-specific definition and IOC baselines and authorized draft preparation; `INFOPS-0.1-IPCH-P01-D40-F01` subsequently accepted the experimental guide only. All research questions remain OPEN and adversarial fixtures UNEXECUTED.
- **Document format:** D04 sixteen-section guide, applied in owner-directed numerical First-Pass sequence while D05 original order remains historically preserved.
- **Interpretation caution:** Assertions about Information-specific semantic granularity, Composition/Compound authority, conditional applicability and D02 PARTIAL/NOT_MET are the approved *research-stage derivation*; do not present them as text from AIPCH20 or as universal normative requirements.

### Exact decision and execution statuses

| Subject | Status |
|---|---|
| D39 criteria and drafting authority | `APPROVED_EXPERIMENTAL_E0` |
| `IPCH16.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` under D40 (experimental only) |
| Guide owner acceptance (D40) | `APPROVED_EXPERIMENTAL_E0` (draft only) |
| `IOC-M01`–`IOC-M08` | APPROVED mandatory conjunctive; applicable derived-Product branch conditional |
| `IOC-N01`–`IOC-N09`; `IOC-ES01`–`IOC-ES08` | APPROVED First-Pass registers |
| `IOC-A01`–`IOC-A12` | Proposed, **UNEXECUTED** |
| `IOC-R01`–`IOC-R08` | All **OPEN** |
| Overlay and repository publication | `PREPARED_VERIFIED` / `NOT_DEPLOYED` |
| Empirical composition / adversarial replay | `NOT_EXECUTED` / `NOT_EXECUTED` |
| First-Pass closure | `NOT_AUTHORIZED` |
| Second Pass | `NOT_STARTED` |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |

**First-Pass checkpoint:** IPCH01–IPCH16 experimental guidance drafts prepared and owner-accepted (16/16), but **First Pass remains ACTIVE and NOT_CLOSED**. IPCH01–IPCH03 experimental deployment previously confirmed; IPCH04–IPCH16 incremental overlays prepared, with IPCH04–IPCH15 deployments unconfirmed and IPCH16 NOT_DEPLOYED. Parent INFOPS restrictions and all preceding obligations remain unaffected.

**Stop condition:** D40 accepted the draft and the IPCH16 incremental overlay is `PREPARED_VERIFIED`, `NOT_DEPLOYED`. No First-Pass closure, Second-Pass initiation, empirical interoperability/composition, adversarial replay, independent Product qualification, final guide approval or normative release is authorized.
