# IPCH06 — Trustworthy

**Information Product Characteristic (IPCH) | PMDD maturity guidance**  
**Artifact:** `IPCH06-PMDD-GUIDE-01`  
**Revision:** `FIRST-PASS-DRAFT-01`  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` — D19-F01 approved the First-Pass baseline; D20-F01 accepted this prepared experimental First-Pass draft only. **Deployment, empirical assessment, adversarial validation and final guide approval have not occurred.**  
**Authority:** Experimental E0 guidance only; no normative Product-family qualification, DPP equivalence or conformance, semantic, control, assurance or deployment authority.  
**Lineage:** `INFOPS-0.1-IPCH-P01-D19-F01` and `INFOPS-0.1-IPCH-P01-D20-F01`; DPCH06 / AIPCH07; IPCH D02–D05; owner-directed First-Pass/Second-Pass strategy.

> **Core assertion:** An Information Product is **Trustworthy** when its current, exact-Product/Version trust posture can be independently established from **objective, attributable, machine-consumable and verifiable evidence** relevant to informational reliability, provenance, dependencies, applicable governance controls, assurance status, intended use, risk and material limitations. Trust evidence is exposed via an authoritative governed Product-bound trust record, without assuming that any particular INFOPS DPP equivalence or conformance authority has been established.

## 1. Characteristic identity and source lineage

- **Characteristic:** `IPCH06 — Trustworthy` in the experimental Information Product characteristic family.
- **DPCH06:** *Trustworthy (via Trust Signals)* / “Emits Trust Signals.” A Data Product continuously exposes objective, measurable, current and machine-consumable trust signals at **Product level**, independently inspectable without personal producer relationships. Its **Digital Product Passport (DPP)** is explicitly the **canonical carrier** that assembles and exposes signals; the source's canonical statement says signals are **exposed via a DPP**. The DPP does not generate or validate the underlying evidence.
- **AIPCH07:** *Trustworthy*. A Product/Version exposes current evidence appropriate to its **actual constitution and risk**, including qualification, dependencies, governance, assurance and material incidents/restrictions. Its positive criteria accept an **AIPS-DPP or equivalent governed trust record**. AI-specific model/agent/physical-AI examples and AIPS AQE/obligation-profile structures are source context, **not directly imported INFOPS obligations**.
- **Source difference intentionally unresolved:** DPCH06's canonical DPP requirement and AIPCH07's alternative governed-record allowance are not identical. This E0 Information-family draft adopts the D19-approved **Product-bound, structured, machine-consumable trust-record** claim, preserving both upstream positions and leaving INFOPS equivalence/conformance unresolved as `TRU-R03`.
- **D19 scope:** Approved `TRU-M01–TRU-M07`, `TRU-N01–TRU-N08`, `TRU-ES01–TRU-ES07`, proposed unexecuted `TRU-A01–TRU-A12`, and OPEN `TRU-R01–TRU-R07`. D19 approved the criteria baseline, **not** this draft or any Product assessment.
- **Shared governance:** D02 assessment eligibility, applicability and independent `EVIDENCE_LIMITED`; D03 experimental 1/0.5/0 characteristic scoring; D04 sixteen-section `IPCH-PMDD-GT-01`, `IPCH-ES-01`, `IPCH-NDC-01`. D05 historical wave order remains recorded; owner First Pass proceeds numerically, Second Pass separately.

## 2. What the characteristic really asserts

Trust is **earned and inspectable**, not a word in a label or an endorsement by a reputable team. The assessor must be able to establish a bounded, relevant trust posture using evidence that can be independently retrieved, interpreted, attributed and challenged. The trust posture may include failures or restrictions: **transparent disclosure is mandatory, but does not itself make an unsafe Product trustworthy**.

The Product-level assertion matters. Passing source-data checks or an isolated pipeline test does not prove that the Information Product's own derived measures, analytic interpretation, time semantics or outputs are reliable. Conversely, trust assurance is **appropriate to Product constitution, intended use and risk**; it must not become one universal metric checklist or a blanket guarantee of correctness.

The record exposing trust signals must not be mistaken for the assurance bodies, evaluations or controls that produce the evidence. A DPP, alternative record, dashboard or label may report competent results, but does not create qualification, policy compliance, semantic conformance or assurance authority. A machine-readable assertion without a verifiable basis is still only an assertion.

## 3. Information Product specialization

A consumer of Information Products may rely on derived measures, classifications, analytical inferences or decision-support interpretations. Relevant trust domains can therefore include **analytical validity**, **source and dependency integrity**, **semantic/temporal context**, **freshness and reliability**, and **applicable governance, incident and assurance status**. These are illustrative evidence dimensions, not a new mandatory fixed list of tests for every Product.

For example, a regulatory reporting Information Product might require reconciliations, cut-off/time consistency and authoritative control evidence. An exploratory market-insight Product may require data-source provenance, methodology, uncertainty disclosure and risk-appropriate evaluation. The necessary assurance basis is determined by the actual informational Promise, risk and competent authorities; **TRU-M04 remains mandatory** regardless of chosen evidence methods.

**DPP role:** Under DPCH06, the DPP is the canonical Data Product carrier of trust signals; under AIPCH07, AIPS-DPP **or a governed equivalent** is eligible. For experimental IPCH06, a governed machine-consumable Product-bound trust record is required, while the exact DPP profile or equivalence decision is **not established** by this guide. A record may aggregate authoritative references, but references must resolve, be current enough for their claims and be attributable. `TRU-R03` remains OPEN.

No evidence in this document itself authorizes an INFOPS DPP schema, BPS conformance waiver, alternative protocol or a new trust-issuance authority.

## 4. Assessment subject and authority

Assess **one exact Information Product and Version** at an explicit assessment timestamp and intended use/risk context. Keep the following separations in the assessment record:

1. **Eligibility and identity:** Product, Version, asserted family, D02 `EXPERIMENTAL_ELIGIBLE` or independently established normative eligibility; otherwise `NOT_ASSESSABLE`.
2. **Promise and constitution:** relevant information outputs, transformations/derivations, semantic definitions, intended users, risks and material limitations.
3. **Trust signals:** actual results, evaluation methods, thresholds where applicable, issuer, governing authority, evaluation/as-of/effective dates and evidence links.
4. **Attribution path:** which signals establish Product-level claims, including applicable upstream dependencies, output validity, semantic versions and realisation context.
5. **Exposure:** exact governed trust record, retrieval/interpretation mechanism, applicable access restrictions and trust-record Version/currentness.
6. **Control/assurance sources:** independently governed qualification, policy, governance obligations, assurance evidence, restrictions, incidents and invalidations.
7. **Time and ontology:** preserve distinct Product Version, semantic-definition Version, realization revision, compilation identity, runtime occurrence, evidence evaluation time and determination time. Evidence for one occurrence must not silently be generalized to another.
8. **Uncertainty:** record missing, stale, contradictory or disputed evidence separately from positively established failures.

The assessor evaluates an **experimental characteristic**; it does not grant Product qualification, semantics, legal permission, trust certification, DPP conformance, control effectiveness, runtime authorization or consequential-action rights.

## 5. Applicability and N/A rules

**Default:** Trustworthy is applicable to D02-eligible Information Products. No generic whole-characteristic `NOT_APPLICABLE` exception is approved for low-risk, internal, pilot, human-consumed or exploratory Products. Risk appropriateness determines **which evidence is relevant and how much assurance is justified**, not whether objective trust, currentness and verifiability are required.

A model-drift signal is not applicable to a Product without the relevant model dependency; absence of that *particular example* does not exempt `TRU-M04` or the characteristic. Similarly, a specific DPP implementation may be absent without thereby deciding the unresolved INFOPS equivalence question. Exceptional whole-characteristic N/A requires independent competent D02 applicability authority; missing eligibility yields `NOT_ASSESSABLE`, **not** `NOT_MET`.

Access restrictions protecting sensitive assurance evidence are permitted where governed mechanisms still allow the **intended legitimate consumers or governance agents** independently to inspect an adequately meaningful trust posture; public visibility to everyone is not assumed. Whether exposure is sufficient is evidence-dependent and may be `EVIDENCE_LIMITED`.

## 6. Distinctness and non-duplication

| Neighbour | Independent maturity claim |
|---|---|
| **IPCH01 — Domain-Owned** | Accountable ownership versus objective, independently inspectable trust evidence. |
| **IPCH02 — Deployable** | Governed self-service lifecycle versus current trust assurance. |
| **IPCH03 — Declarative** | Formal governing intent versus real evidence of reliability of actual informational effects. |
| **IPCH04 — Discoverable** | Faithful publication of trust posture versus establishing its evidence basis. |
| **IPCH05 — Self-Describing** | Description of quality, provenance and constraints versus objective trust evaluations and current signals. |
| **IPCH08 — SLA–SLO Backed & Observable** | Runtime measures, SLO/SLA operation and observation versus evidence-backed fitness/trust posture. |
| **IPCH09 — Compliant by Design** | Design/enforcement of mandated controls versus inspection of competent control and assurance results. |
| **IPCH11 — Semantically Aligned** | Semantic conformance authority versus current trust claims referencing that authority. |
| **IPCH13 — Testable & Versioned** | Test/version practices versus trustworthy current evaluations and Product-level attribution. |
| **IPCH16 — Interoperable & Composable** | Composition/interoperation versus portability/consumption of trust evidence. |

`IPCH-NDC-01` prohibits circular or duplicate scoring. The *same* externally issued control result may be cited by different characteristic assessments only for **different explicitly stated claims**. A `MET` on this characteristic does not imply an adjacent `MET`, nor does it independently certify policy, semantic or assurance conformance.

## 7. Core mandatory positive criteria — `MET`

**All seven are mandatory, conjunctive and non-dilutable.** `MET` requires credible evidence for **each** applicable mandatory claim; no numerical criterion weighting or averaging.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **TRU-M01** | **Objective Evidence-Backed Trust** | Relevant trust statements are substantiated by verifiable measurements, evaluations or independently attributable control evidence, not just producer assertions, labels or reputation. |
| **TRU-M02** | **Product-Level Trust Attribution** | Evidence is defensibly tied to the exact Product/Version and material informational constitution, not merely to source tables, dashboards, individual jobs or unrelated implementations. |
| **TRU-M03** | **Currentness and Evidence Provenance** | Material evidence is dated, attributable and appropriately refreshed, with effective status, provenance, expiry/supersession and material invalidation conditions identifiable. |
| **TRU-M04** | **Information-Appropriate Reliability Assurance** | Evidence covers applicable quality, analytical validity, semantic/temporal interpretation, provenance/dependency and fitness-for-use risks **appropriate to the Product's Promise and risk**; no universal metric checklist is prescribed. |
| **TRU-M05** | **Governance, Control and Assurance Visibility** | Applicable qualification, controls, risk obligations and assurance outcomes are faithfully represented or traceably referenced **from their competent independent authorities**, including unresolved states. |
| **TRU-M06** | **Governed Machine-Consumable Trust Exposure** | Intended consumers and authorized governance automation can independently inspect a structured, machine-consumable, authoritative **Product-bound trust record** (e.g. applicable DPP or a record whose equivalence is independently governed), without assuming INFOPS has authorized a particular alternative. |
| **TRU-M07** | **Material Risk, Incident and Limitation Transparency** | Known material incidents, failures, restrictions, invalidations, unresolved risks and evidence gaps are made visible or accurately qualified rather than suppressed by a blanket trustworthy label. |

For `TRU-M06`, **existence of a DPP or a record named “trust passport” is not enough**: it must expose real, sufficiently current and attributable trust information. `TRU-M07` requires transparency but cannot convert an unresolved critical risk into competent positive assurance by disclosure alone. `TRU-M05` reports independently issued statuses; IPCH06 does not issue them.

## 8. Core negative criteria — `NOT_MET`

| ID | Affirmatively established failure condition |
|---|---|
| **TRU-N01** | The trust claim relies on personal confidence, reputation, labels or producer assurances without objective validation. |
| **TRU-N02** | Available metrics describe isolated technical assets but have no defensible correspondence to the assessed Product/Version. |
| **TRU-N03** | Material trust evidence is stale, untraceable, undated or presented as current after material invalidation. |
| **TRU-N04** | Technical input data quality is shown but material analytical, semantic or informational risks intrinsic to the Product remain unassessed. |
| **TRU-N05** | Applicable mandatory control, governance or assurance evidence is demonstrably absent, invalid or materially misrepresented. |
| **TRU-N06** | Intended independent consumers cannot access or interpret relevant trust signals through any adequate governed machine-consumable Product-bound mechanism. |
| **TRU-N07** | Known material incidents, restrictions, evidence gaps or limitations are concealed or contradicted by the published trust posture. |
| **TRU-N08** | A DPP or purported equivalent contains only unsupported certifications/assertions rather than attributable and verifiable evidence. |

A *proven* fundamental failure may support `NOT_MET`; an unavailable or uninspected record may instead require `EVIDENCE_LIMITED`. Evaluate materiality and assessment context before concluding. Neither the negative list nor the seven positive criteria creates an unauthorized fixed numerical cap or shortcut in D02 determination.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Established condition | Candidate assessment | Reason |
|---|---|---|
| Every mandatory trust claim evidenced; current governed Product-bound trust record and no material contradiction | `MET` | Product-level trust independently defensible; all seven claims examined. |
| Real Product-level, independently inspectable evidence exists, but a non-foundational domain or presentation gap remains | `PARTIAL` | Genuine trust basis with demonstrated bounded deficiencies. |
| Only producer says “certified” or only an unverified DPP label exists | `NOT_MET` | Foundational objective trust-evidence failure demonstrated. |
| Source data quality passes, but material derived risk calculations are demonstrably wrong or unassessed despite competent inquiry | `NOT_MET` or `PARTIAL`, depending on foundationality | Input quality does not validate Information Product outputs. |
| Current quality results exist; uninspected governance record cannot be accessed | `EVIDENCE_LIMITED` if no failure established | Inability to assess is not automatically an actual control failure. |
| A material invalidation exists but is transparently disclosed | Context-dependent, may be `NOT_MET` | Disclosure is necessary, not sufficient to establish fitness or permissible trust posture. |
| Structurally valid DPP carries only producer attestations | `NOT_MET` | The container is not evidence. |
| Product-level trust record other than DPP is demonstrably sufficient | Experimental candidate; `TRU-R03` remains OPEN | AIPCH07 permits equivalent; INFOPS equivalence/conformance not authorized by this guide. |
| Evidence from runtime occurrence A is presented as assurance for materially different occurrence B | `EVIDENCE_LIMITED` or `NOT_MET` on established misattribution | Occurrence and Product/Version attribution must remain separate. |

Distinguish **incomplete evidence about a capability** from **evidence that the capability is absent**. `EVIDENCE_LIMITED` is an **independent qualifier**, not a fourth point on the MET/PARTIAL/NOT_MET ordinal scale. Candidate cases are instructional thought experiments, not executed Product assessments or approved automatic classifications.

## 10. Evidence signals and sufficiency

`TRU-ES01–TRU-ES07` are **claim-specific evidence requirements**. Enterprises may choose credible evidence methods and assurance depth appropriate to constitution/risk, but cannot remove a mandatory assertion.

| Evidence ID | Maps to | Required evidence claim; possible evidence examples |
|---|---|---|
| **TRU-ES01** | TRU-M01 | Independently attributable evaluation/measurement/control result; verifiable method, result, issuer and underlying evidence path. |
| **TRU-ES02** | TRU-M02 | Binding between evaluated Product/Version and relevant outputs, source dependencies, transformations and effective semantic/realization context. |
| **TRU-ES03** | TRU-M03 | Evidence timestamp, evaluation time, validity/currentness basis, effective interval, expiry/invalidation and supersession where relevant. |
| **TRU-ES04** | TRU-M04 | Product-appropriate analytical validation, reconciliation, semantic/temporal checking, source/lineage verification or equivalent risk-relevant evaluations. |
| **TRU-ES05** | TRU-M05 | Competently issued qualification, control, governance, assurance and risk decisions or version-resolved authoritative references; do not issue them within this assessment. |
| **TRU-ES06** | TRU-M06 | Retrievable structured trust record: **DPP is DPCH06's canonical carrier**; **AIPCH07 permits AIPS-DPP or equivalent**; any INFOPS equivalence/conformance remains to be established independently. Show actual machine interpretation and traceable evidence references. |
| **TRU-ES07** | TRU-M07 | Current incident, restriction, limitation, invalidation and unresolved-gap information; disclosure and treatment status as applicable. |

**Evidence priority:** actual current authoritative results and their provenance; Product/Version binding; valid record/interface; incident/assurance currentness. Supporting material may include dashboards, lineage visualizations, control registries, incidents and evaluation logs, but a screenshot, wiki page or certification badge alone does not establish all claims. Automated retrieval can assist, yet agent-produced summaries are not substitutes for source evidence.

**Evidence ledger:** record claim ID, evidence identifier, issuer, competence, validity, assessed subject/Version, time, provenance path, contrary evidence, observed limitation and independent determination. Keep semantic definition Version, realization revision, compilation and runtime occurrence distinct. Evidence-to-claim sufficiency is adjudicated, not inferred from artifact naming.

## 11. Agent-assisted or human assessment decision rule

1. **Gate eligibility:** identify exact Product/Version and D02 eligibility; if unestablished, `NOT_ASSESSABLE` with supporting reason and no characteristic score.
2. **Establish applicability:** no blanket N/A; select constitution/risk-relevant evidence, document any competent exception and avoid treating an inapplicable *example* as an inapplicable characteristic.
3. **Collect evidence:** resolve `TRU-ES01–TRU-ES07` for every mandatory `TRU-M01–TRU-M07`, including actual trust-record content and independent evidence authorities.
4. **Validate provenance and currentness:** verify issuer, Product/Version binding, timestamps, effective statuses, dependency and incident state; distinguish evidence from producer characterization.
5. **Challenge negatives:** inspect `TRU-N01–TRU-N08` and contradictions; where evidence is absent versus failure confirmed, record the distinction.
6. **Determine at characteristic level:** `MET` only if all seven adequate; `PARTIAL` only if real trust capability is established with demonstrably non-foundational gaps; `NOT_MET` for proven foundational failure. Record `EVIDENCE_LIMITED` independently whenever support is insufficient or conflicting; do not assign unsupported certainty.
7. **Preserve separate assurance:** do not self-issue control certification, Product-family qualification, DPP equivalence, semantic conformance, deployment approval or actionable trust permissions.
8. **Report:** characteristic finding, D02 status, evidence qualifier, critical-assurance caveats, risks, unresolved `TRU-R01–R07`, currentness and reassessment triggers.

**Compact test:** Can a legitimate consumer/agent independently substantiate a **current, risk-appropriate trust posture** for this exact Product/Version from an authoritative machine-consumable Product trust record and competent evidence, without relying on producer assurances?

## 12. PMDD scoring treatment

Only after an evidence-supported D02 assessment result is determined, D03 permits characteristic-level experimental scores:

| Characteristic outcome | Experimental score |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |

`NOT_APPLICABLE` requires an affirmative independent determination and can be excluded from the applicable denominator; `NOT_ASSESSABLE` is not scored. `EVIDENCE_LIMITED` is an uncertainty qualification, **not a score**. Where D03 permits a bounded score range because evidence is incomplete, apply that existing rule only when the denominator and assessment scope are defensible; do not invent certainty or average guessed states.

Across IPCH characteristics D03 uses **equal characteristic weights**. This does not create criterion-level weights, seven-item mean scores, automatic critical caps, or an IPCH L0/L1/L2 band. Any separate critical assurance restrictions remain independent; a high experimental score cannot override them.

## 13. Critical assurance and governance boundaries

- **BPS/PIN:** generic Productness and competing Product-family/Compound qualifications require their own competent determinations.
- **GEARA/GEARM:** analytical-architecture and semantic meaning/conformance authorities respectively are not replaced by IPCH06.
- **INFOPROD/INFOPDS:** keep semantic definition and deployment/realization specification distinct; no invented normative descriptor or qualification profile.
- **DPP:** DPCH06 says canonical carrier; AIPCH07 allows DPP/equivalent. D19 does **not** resolve the INFOPS equivalence, mandate a new BPS profile, grant conformance or amend either source. `TRU-R03` remains OPEN. A record merely exposing claims is not assurance.
- **PFI/HDIP and execution:** realization rules, compilation, deployment, runtime occurrence and operational controls remain independently governed; evidence attached to one cannot be indiscriminately generalized to others.
- **Legal/policy/assurance:** competent issuers retain authority for obligation interpretation, certifications, governance approvals, incident classification and consequent restrictions. Experimental Trustworthy maturity cannot grant permission for consequential action.
- **Evidence integrity:** distinguish actual source records, provenance and adjudications; proposed tests are not executed evidence; E0 design is not E1/E2 implementation.

## 14. Reassessment and evolution triggers

Reassess the relevant claims when evidence could become inaccurate or less credible, including:

- Product/Version change, changed informational Promise, new analytic derivation or materially changed measures;
- semantic definition/version, data input or upstream dependency changes affecting meaning or trust;
- new realization revision, compilation or runtime occurrence with material differences;
- evaluation expiry, quality/freshness deterioration, altered assurance coverage or invalidated certification;
- newly identified incidents, risk restrictions, policy obligations or changes to applicable intended use;
- changed trust-record exposure, issuer authority, evidence resolution, access or trust-data integrity.

Reassessment must retain prior evidence, historic effective dates and supersession/invalidations, with fresh issuer-competence and Product/Version attribution checks. A later trusted record must not silently rewrite an earlier historical determination. No universally prescribed refresh interval is adopted here.

## 15. Adversarial and boundary cases — First-Pass fixtures

**All cases are proposals for Second Pass, not executed evaluation or validation.** They probe positive/negative criteria, source DPP tensions and evidence sufficiency.

| ID | Unexecuted challenge | Main contested boundary |
|---|---|---|
| **TRU-A01** | Producer claims “certified” without competent supporting evidence. | TRU-M01 / TRU-N01 / asserted status. |
| **TRU-A02** | Source quality passes while a derived measure is demonstrably invalid. | TRU-M04 / Product-level trust. |
| **TRU-A03** | Current assurance exists but applies to a different Product Version. | TRU-M02 / TRU-M03. |
| **TRU-A04** | DPP is syntactically valid yet aggregates unverified assertions. | TRU-M01 / TRU-M06 / TRU-N08. |
| **TRU-A05** | Complete trustworthy evidence is exposed via a governed non-DPP record. | DPCH06 versus AIPCH07 / `TRU-R03` OPEN. |
| **TRU-A06** | Quality metrics are current but material dependency-lineage evidence is stale. | Currentness and evidence domains. |
| **TRU-A07** | Material trust incident is disclosed with an enforceable restriction. | Transparency versus actual trust fitness. |
| **TRU-A08** | Strong competent assurance exists but signals are unavailable to intended independent consumers. | TRU-M06 / legitimate access. |
| **TRU-A09** | Analytical formula is validated, but an authoritative semantic definition changes. | Semantic currentness and authority. |
| **TRU-A10** | Policy-control record contradicts published trustworthy status. | TRU-M05 / governance authority. |
| **TRU-A11** | Many current signals exist but none covers material fitness for intended use. | TRU-M04 / non-dilution. |
| **TRU-A12** | Trust results from runtime occurrence A are used for materially different occurrence B. | Product/Version versus runtime occurrence attribution. |

`TRU-A01–TRU-A12 = PROPOSED_E0_UNEXECUTED`. No replay, independent empirical test, G4–G6 validation or final guide approval occurs by listing these fixtures.

## 16. Source provenance, open questions and status

**Direct source documents consulted for this draft:**

1. `DPCH.zip` → `pages/DPCH-PMDD-guidance/06-DPCH06.md`, *DPCH06 — Trustworthy (via Trust Signals)*. Key original concepts: continuous objective verifiable signals; independent inspection; Product-wide evidence; DPP as canonical signal carrier; fragmented/nonstandard signals as Partial examples; unsupported claim as Not Met.
2. `AIPCH.zip` → `AIPCH-PMDD-guidance/07-AIPCH07.md`, *AIPCH07 — Trustworthy*. Key original concepts: constitution/risk-appropriate trust evidence; qualification/dependency/governance/assurance currentness; incidents and restrictions; AIPS-DPP **or equivalent**; machine-consumable trust. AI-specific evidence structures are not made INFOPS normative.
3. `INFOPS-0.1-IPCH-P01-D19-F01`, approved owner finding, F01.1–F01.16. D02–D05 approved baseline and owner-directed numerical First Pass are independently retained.

**Open Second-Pass questions (no closure is inferred):**

| ID | Research obligation | Status |
|---|---|---|
| **TRU-R01** | Minimum risk-/constitution-appropriate Information Product evidence coverage without a universal metric list? | OPEN |
| **TRU-R02** | How to evidence analytical correctness independently of input quality for complex derived information? | OPEN |
| **TRU-R03** | Which competent INFOPS authority governs DPP/equivalent trust records, and how should DPCH06's canonical-DPP requirement be reconciled with AIPCH07's equivalent-record allowance? | **OPEN** |
| **TRU-R04** | How to establish evidence currentness across Product, semantic, dependency, assurance and occurrence effective times? | OPEN |
| **TRU-R05** | How do disclosed incidents/restrictions affect finding without unauthorized automatic maturity caps? | OPEN |
| **TRU-R06** | Boundary between IPCH06 trust, IPCH08 observability and IPCH09 control/compliance assurance? | OPEN |
| **TRU-R07** | Distinguish `PARTIAL`, foundational `NOT_MET` and `EVIDENCE_LIMITED` for missing but potentially material assurance? | OPEN |

**Document status:** `IPCH06-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01 = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; `D20_OWNER_DRAFT_ACCEPTANCE=APPROVED_EXPERIMENTAL_E0`; `PUBLICATION=NOT_DEPLOYED`; `EMPIRICAL_ASSESSMENT=NOT_EXECUTED`; `ADVERSARIAL_VALIDATION=NOT_EXECUTED`; `SECOND_PASS=NOT_STARTED`; `FINAL_GUIDE_APPROVAL=NOT_APPROVED`; `NORMATIVE_RELEASE=NOT_AUTHORIZED`.

**Outstanding characteristic reviews:** IPCH01 G4–G6 NOT_EXECUTED; IPCH02–IPCH05 Second-Pass obligations retained. IPCH01–IPCH03 experimental guides confirmed deployed; IPCH04 and IPCH05 overlays prepared but deployment unconfirmed. IPCH07–IPCH16 not initiated.

**Parent programme safeguards preserved:** MVP-P01 D01–D08 approved, conceptual design stopped; MVP experimental specification `DRAFT_PREPARED_NOT_VERIFIED`. Parent Track B B01 completion `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`. Effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE` with F01.6/F01.29 safeguards, original charter/audit NOT_VERIFIED; historical ledgers 65/6/7/7, separate PC ledger UNCHANGED. Q0–Q5 and F06/F14/F16 UNRESOLVED. G06's 62 E0 designs approved but UNEXECUTED, E1/E2 executions zero; G06-RO01–RO12 and G03-R01–R12 (24 obligations) ALL_OPEN. No repository modification, IPCH07 initiation, independent authority change or normative release is enacted by this draft.
