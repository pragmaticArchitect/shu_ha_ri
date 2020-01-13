# IPCH04 — Discoverable

**Information Product Characteristic (IPCH) | PMDD maturity guidance**  
**Artifact:** `IPCH04-PMDD-GUIDE-01`  
**Revision:** `FIRST-PASS-DRAFT-01`  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` — D15-F01 approved the First-Pass source and mandatory-criteria baseline; D16-F01 accepted `FIRST-PASS-DRAFT-01` as prepared experimental guidance. **This overlay has not been deployed or subjected to Second-Pass validation, empirical assessment or final guide approval.**  
**Authority:** Experimental E0 guidance only; not a normative Product qualification, marketplace-eligibility, semantic, policy, assurance, entitlement or release standard.  
**Lineage:** `INFOPS-0.1-IPCH-P01-D15-F01` and `INFOPS-0.1-IPCH-P01-D16-F01`; DPCH04 / AIPCH05; IPCH D02–D05 assessment/guidance controls; owner-directed First-Pass / Second-Pass strategy.

> **Core assertion:** An Information Product is *Discoverable* when it is intentionally published through a **governed Product-level discovery mechanism** where intended potential consumers can independently find, identify, understand and evaluate its governing informational Promise, purpose, applicable context, current Product identity, consumption conditions and relevant trust or qualification status **without prior knowledge of its producer**. Discoverability operates within legitimate intended-audience visibility restrictions and does not itself confer access or establish underlying Product quality.

## 1. Characteristic identity and source lineage

- **Characteristic:** `IPCH04 — Discoverable` in the Information Product family.
- **Direct sources:** `DPCH04 — Discoverable`, specifically *Registered in Data Marketplace or Catalog*; `AIPCH05 — Discoverable`, specifically current AI Product/Version discoverability through a governed discovery surface.
- **Directly sourced distinctions:** DPCH04 emphasizes intentional Product-level publication, independence from tribal knowledge and the inadequacy of technical-asset registration. AIPCH05 emphasizes correct Product/Version and family representation, qualification/trust currentness and consumption/entitlement orientation. AIPCH-specific AQE, AIPROD and ontology fields are **not** made INFOPS requirements by inheritance.
- **INFOPS specialization:** consumer evaluation of an informational Promise, analytical/informational context and intended audience, with faithful and appropriately qualified publication of independent Product-family, lifecycle and trust information.
- **Decision authority:** D15-F01 approved `DIS-M01–DIS-M06`, `DIS-N01–DIS-N07`, `DIS-ES01–DIS-ES06`, `DIS-R01–DIS-R06` OPEN, and `DIS-A01–DIS-A12` as proposed unexecuted research cases. D15 did not accept or deploy this Markdown draft; the subsequent D16-F01 owner disposition **accepted this prepared experimental draft only**, without publication, validation or final approval.
- **Common guidance:** D02 eligibility/applicability/evidence; D03 equal characteristic weighting and 1/0.5/0 experimental scoring; D04 `IPCH-PMDD-GT-01` sixteen-section template, `IPCH-ES-01`, `IPCH-NDC-01`; D05 controls historically preserved, with outstanding reviews deferred under the owner's two-pass direction.

## 2. What the characteristic really asserts

**Discoverability is intentional Product exposure, not accidental visibility.** An eligible potential consumer who does not already know the producing team, system of origin or direct Product location can find the Information Product and obtain sufficient, current, truthful Product-level context to judge its relevance and know the legitimate next step toward consumption.

A Product name in an index, a technical metadata record or a runtime endpoint does not by itself establish Discoverable. Conversely, a Product may be discoverable within a restricted audience even where accessing the Product requires a separate entitlement decision.

The characteristic tests the **discovery experience and fidelity of its Product representation**. It does not certify the Product's analytical correctness, establish Product-family qualification, grant consumption rights, or require that consumption actually succeeds.

## 3. Information Product specialization

The discovery representation must communicate the **governing informational Promise** and enough analytical/informational context for an intended consumer to assess fit for purpose. Depending on the Product, this may include an intended interpretation, subject area, relevant time horizon, limitations, audience, usage conditions and references to governed descriptions.

A sensitive Information Product can legitimately be discoverable only to approved audience segments. Evaluate *independent discoverability within the authorized intended audience*, without requiring exposure of protected metadata to unauthorized persons.

A discovery mechanism can be a marketplace, catalogue, semantic discovery service, AI concierge or equivalent governed interface. The technology does not determine adherence. An automatically created listing may count as **intentional publication** where authorized Product governance deliberately governs the publication policy and its resulting Product-level listing; accidental asset registration does not.

Qualification and trust claims in discovery must accurately represent the status of the **relevant competent sources**, including unresolved/provisional status, rather than being treated as new determinations made by the catalogue.

## 4. Assessment subject and authority

Assess the discovery state for **one exact Information Product and Version**, at a specified time, for a defined legitimate audience and configured enterprise assurance profile. Record:

1. Product identity, Version and the independent D02 eligibility basis (normative where independently established, or permitted experimental eligibility).
2. Discovery listing identity, scope, lifecycle/effective time and appropriate publication authority.
3. Product family/qualification claims and the specific competent evidence against which their fidelity is checked.
4. Informational Promise, intended audience, context and interpretation presented to potential consumers.
5. Discovery surface and representative findability route for a consumer without producer-specific knowledge.
6. Relevant status, trust/governance currentness and any qualified or unresolved claims.
7. Access/entitlement orientation and permitted-use conditions, without assuming actual entitlement.
8. Establishing, supporting, contrary, stale, disputed and missing evidence; assessed time and reviewer/agent role.

The discovery assessor does **not** confer BPS/PIN Productness, Product-family membership, semantic authority, trust certification, access rights or marketplace admission. A provisional Information Product profile must not be represented as a normatively qualified Product merely because it is listed.

## 5. Applicability and N/A rules

**Default:** IPCH04 applies to an eligible, constituted Information Product. No generic whole-characteristic `NOT_APPLICABLE` exception has been established.

A hidden Product, an absent catalogue entry, a single intended consumer, a highly restricted audience or unavailable listing evidence is **not automatically N/A**. Each requires an evidence-based finding or justified limitation. Legitimate restrictions on audience visibility are compatible with adherence when intended authorized consumers can independently discover the Product.

Individual *evidence mechanisms* may be inapplicable in context (for example, there may be no public catalogue; an authorized enterprise search or concierge may be used instead). The underlying six mandatory claims remain applicable. Any exceptional whole-characteristic N/A requires an affirmative determination from competent D02 applicability authority. A subject lacking required D02 Product/Version eligibility is `NOT_ASSESSABLE`, not `NOT_APPLICABLE` or `NOT_MET`.

## 6. Distinctness and non-duplication

| Neighbour | Independent maturity claim |
|---|---|
| **IPCH01 — Domain-Owned** | Legitimate ownership of the Product versus the authorized, effective act of Product discovery publication. |
| **IPCH05 — Self-Describing** | Intrinsic Product descriptive information versus what the discovery surface exposes to let a prospective consumer evaluate relevance. |
| **IPCH06 — Trustworthy** | Actual analytical and evidence-based trustworthiness versus faithful display of current/qualified trust information. |
| **IPCH07 — Reusable** | Reuse across relevant contexts versus the ability to find and assess a Product in discovery. |
| **IPCH09 — Compliant by Design** | Effectiveness of binding controls versus accurate communication of applicable permissions and restrictions. |
| **IPCH10 — Addressable** | Stable identification/reachability versus independent discovery without knowing identifiers in advance. |
| **IPCH11 — Semantically Aligned** | Correctness of semantics versus understandable description of the informational meaning. |
| **IPCH12 — Consumption-Driven Intent** | Responsiveness of Product intent to consumer needs versus disclosure allowing a potential consumer to assess relevance. |

The same Product listing or descriptor can support several claims, but **no characteristic is Met by implication from another**. Apply `IPCH-NDC-01` to distinct assessment claims and avoid double-counting.

## 7. Core mandatory positive criteria — `MET`

**All six applicable criteria are mandatory and conjunctive for `MET`. They are not individually weighted or arithmetically averaged.**

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **DIS-M01** | **Intentional Governed Publication** | The Information Product is intentionally published through a governed **Product-level** discovery mechanism under legitimate publication authority, whether publication is manual or authorized automation. |
| **DIS-M02** | **Independent Consumer Findability** | An intended, authorized potential consumer can locate the Product without pre-existing knowledge of its producer, system of origin or direct access endpoint. |
| **DIS-M03** | **Product Identity and Family Integrity** | The listing unambiguously represents the correct Product and relevant Version, and faithfully reflects independently established or qualified Product-family status rather than fabricating eligibility. |
| **DIS-M04** | **Informational Purpose and Context Transparency** | The discovery experience communicates enough of the governing informational Promise, purpose, intended audience and analytical/informational context to enable a prospective consumer to assess relevance. |
| **DIS-M05** | **Currentness and Trust Transparency** | Relevant Product lifecycle, qualification, assurance and trust information is current or explicitly qualified as stale, provisional or unresolved, so that discovery does not mislead the consumer. |
| **DIS-M06** | **Consumption and Access Orientation** | The consumer can determine relevant consumption conditions, authorized uses, applicable restrictions, an available entitlement/access-request route where required and reasonable next steps toward permitted consumption. |

For `DIS-M05`, the assessment examines **faithfulness of disclosure to competent records**, not whether underlying trustworthiness itself is Met. For `DIS-M06`, the available legitimate next step may be a governed request; actual entitlement or successful consumption is not required.

## 8. Core negative criteria — `NOT_MET`

| ID | Affirmatively demonstrated negative condition |
|---|---|
| **DIS-N01** | Consumers depend on personal contacts, producing-team identity or informal tribal knowledge to discover the Product. |
| **DIS-N02** | Only underlying technical assets (tables, files, technical endpoints, model services or pipelines) are discoverable, not the Information Product as a Product. |
| **DIS-N03** | Listing is an accidental/opaque registration without authorized Product-level publication or meaningful Product intent. |
| **DIS-N04** | The listing materially misrepresents Product identity, Version or Product Family relative to competent evidence. |
| **DIS-N05** | Discovery context is too incomplete or ambiguous for the intended consumer to evaluate the informational purpose or relevance. |
| **DIS-N06** | Materially stale, invalid or unresolved qualification, lifecycle or trust information is deceptively represented as current and reliable. |
| **DIS-N07** | Intended consumers cannot identify applicable consumption conditions or any legitimate request/next-step route, preventing informed consideration. |

An observed deficiency must be evaluated for **materiality and whether it defeats a foundational discovery claim**. Missing evidence does not automatically demonstrate a negative condition. A governed automatically published Product listing is not negative simply because no human manually pressed “Publish.”

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Evidence-supported condition | Candidate finding |
|---|---|
| All six applicable mandatory criteria adequately evidenced with no material foundational contrary evidence | `MET` |
| Genuine intentional Product-level discovery exists, but one or more non-foundational information or lifecycle-disclosure capabilities are demonstrably incomplete | `PARTIAL` |
| A foundational discovery requirement is demonstrably absent (for example, only assets listed, tribal discovery required, or materially false Product-family representation) | `NOT_MET` |
| Material evidence is stale, disputed, missing or contradictory such that the claimed maturity cannot defensibly be determined | `EVIDENCE_LIMITED` qualifier; **not** a maturity state |
| D02 assessment eligibility is not established | `NOT_ASSESSABLE`; no characteristic score |
| Competently established exceptional non-applicability | `NOT_APPLICABLE`; no generic exception established |

**Do not count satisfied criteria** to compute Partial or Met. Positive adherence across five criteria cannot compensate for a demonstrated foundational failure of the sixth. Conversely, an otherwise adequate Product-level listing lacking one nonessential contextual detail should not automatically be classified as fundamentally absent.

**Illustrative boundaries (not assessed cases):**

- Governed Product entry with insufficient relevance context: potentially `PARTIAL` if real discovery exists.
- Technical tables listed but no discoverable Product: `NOT_MET` when established.
- Correct listing visible only to its legitimately intended restricted audience: potentially `MET`.
- Listing cites a qualification determination that cannot be checked for currentness: retain an evidence limitation if material; do not invent current approval.
- AI concierge makes the Product findable through governed Product records: potentially `MET` despite no conventional catalogue UI.
- Correct listing but no consumption guidance: `PARTIAL` or `NOT_MET` depending on demonstrated severity and whether informed discovery remains viable.

Any assessor must explain its materiality judgment and disclose which exact Product/Version, audience and time are covered.

## 10. Evidence signals and sufficiency

| Rule | Mandatory claim | Establishing evidence examples | Material contrary evidence examples |
|---|---|---|---|
| **DIS-ES01** | DIS-M01 | Product listing and governed publication authority, authorized publication event/policy | Only accidental asset registration or unauthorized publication |
| **DIS-ES02** | DIS-M02 | Search/browse/concierge route demonstrated from intended consumer perspective without producer knowledge | Findability depends on direct team contact or prior system identification |
| **DIS-ES03** | DIS-M03 | Listing Product/Version references correlated with competent family/qualification records | Incorrect family, conflicting Product identities, false normative status |
| **DIS-ES04** | DIS-M04 | Published purpose, informational Promise, audience and context examined against governed Product information | Missing/misleading meaning or context precluding relevance assessment |
| **DIS-ES05** | DIS-M05 | Currentness and qualified status from competent lifecycle, qualification, governance/trust records | Stale qualification or assurance portrayed as valid/current |
| **DIS-ES06** | DIS-M06 | Published permitted-use conditions, restrictions and legitimate access/request process | No usable route or materially misleading consumption conditions |

**Evidence standard (`IPCH-ES-01`):**

- **Alignment:** Evidence corresponds to the exact Product, Version, audience, discovery channel and assessed time.
- **Competence:** Publication authority, family qualification, semantic meaning, trust status and entitlement decisions originate with their independently competent authorities.
- **Currentness:** Historical Product listings or qualification outcomes are not silently treated as current; distinguish effective dates of Product, semantic, qualification and trust records.
- **Contradictions:** Record current conflicting listings and determinations. Do not select a “correct” version based solely on timestamp or prominence without a competent authority basis.
- **Consumer perspective:** Findability should be demonstrated or sufficiently evidenced from a representative intended audience viewpoint, respecting visibility policy; producer-only screenshots may be insufficient.
- **Proportionality:** The evidence burden can vary by enterprise profile, sensitivity and lifecycle stage, but every mandatory claim still needs defensible support.
- **No dilution:** A relaxed enterprise assurance profile cannot erase `DIS-M01–DIS-M06` and still claim `MET` under the same guide.

No specific catalogue software, marketplace API, access-control product, interface, metadata schema or test automation is prescribed.

## 11. Agent-assisted or human assessment decision rule

1. **Verify eligibility** for the exact Product/Version under D02. If not established, return `NOT_ASSESSABLE` without a characteristic score.
2. **Determine applicability and audience.** IPCH04 ordinarily applies; define intended legitimate discoverers and restrictions. Exceptional whole-characteristic N/A requires competent affirmative justification.
3. **Identify governed Product publication.** Establish its authority, discovery channel, Product-level representation, Product identity and relevant Version.
4. **Evaluate DIS-M01–DIS-M06**, recording establishing, supporting and contrary evidence for each; specifically check findability without producer knowledge, truthful currentness and consumption orientation.
5. **Investigate DIS-N01–DIS-N07**, distinguishing material demonstrated defects from missing or inaccessible evidence.
6. **Examine contradictory/currentness claims** against the competent source for each claim; keep unresolved conflicts explicitly visible.
7. **Determine the overall finding:** `NOT_MET` for demonstrated foundational failure; `PARTIAL` for demonstrably genuine but materially incomplete non-foundational discoverability; `MET` only when all six applicable claims are supported. If uncertainty prevents a defensible result, retain `EVIDENCE_LIMITED` instead of inventing a state.
8. **Record the evidence trail:** Product/Version, audience, time, publication authority, criteria, relevant documents/observations, counter-evidence, confidence limits, rationale and competent review requirement.
9. **Apply D03 scoring only after a defensible characteristic finding**. Record independent critical assurance concerns separately.

The agent may assist evidence identification and argumentation, but cannot grant Product qualification, settle legal/semantic or access authority, manufacture trust certification, or substitute its inference for a competent owner's or assessor's accountable disposition.

## 12. PMDD scoring treatment

| Defensible characteristic finding | D03 experimental score contribution |
|---|---:|
| `MET` | 1.0 |
| `PARTIAL` | 0.5 |
| `NOT_MET` | 0.0 |
| Affirmatively established `NOT_APPLICABLE` | Excluded from applicable denominator |
| Material `EVIDENCE_LIMITED` unresolved | **No fabricated value**; apply D03 bounded uncertainty treatment where denominator is established |

All characteristics have equal weights under the D03 experimental baseline. Do not assign individual weights to the six DIS criteria or average “criteria met.” Independent critical conditions are not offset by a high maturity score. **No IPCH L0/L1/L2 thresholds, criterion-level aggregation scheme or automatic maturity caps are adopted.**

## 13. Critical assurance and governance boundaries

Discoverability may reveal governance failures, but it does not decide their institutional consequences. In particular:

- An incorrect Product-family listing may establish a Discoverability representation defect; the actual **qualification determination** remains with BPS/PIN and independently competent Product-family/Compound authorities.
- A listing that faithfully reports a qualified or unresolved trust state can satisfy relevant **trust transparency** while IPCH06 independently evaluates analytical trustworthiness.
- Publication can be restricted by applicable policy. `MET` does not require exposing sensitive Product data, protected metadata or entitled consumption to unauthorized consumers.
- Access/entitlement claims must reference competent policies and processes. The listing does not grant permission or approve consequential action.
- GEARA architectural responsibilities, GEARM semantic authority, DPP, INFOPROD/INFOPDS, PFI/HDIP, realization and operational occurrences remain independently governed.
- An experimental INFOPS profile match must not be presented as normative Product qualification or release readiness.

If material independent governance or assurance concerns arise, report them under the relevant competent processes and D03 critical-status categories; do not create a new automatic score cap or deployment prohibition in IPCH04.

## 14. Reassessment and evolution triggers

Reassess the relevant Product/Version and intended audience when material events change the discovery assertion, including:

- Product/Version change or new Product-family/qualification determination;
- change in governing informational Promise, audience or permitted use;
- discovery listing publication, withdrawal, suspension, retirement or substantial metadata revision;
- new audience restrictions, entitlement route or access-request process;
- material trust or qualification status change, including expiry or revocation;
- search/browse/concierge behavior changes affecting independent findability;
- contradictory discovery surfaces or stale listings;
- evidence becoming stale or competent governance mandates changing.

Preserve historical listing states and assessments rather than retroactively rewriting past determinations. A prior `MET` cannot be assumed for a later Product Version or changed audience.

## 15. Adversarial and boundary cases — First-Pass fixtures

**All scenarios below are proposed E0 fixtures and have not been executed against an actual Product.**

| Case | Challenge | Distinction to test |
|---|---|---|
| **DIS-A01** | Catalogue exists, but unknown consumers cannot find the Product | Listing existence versus independent findability |
| **DIS-A02** | Product only findable with producing-team name | Tribal knowledge versus Product discovery |
| **DIS-A03** | Gated visibility correctly limits intended audience | Discoverability versus unrestricted access |
| **DIS-A04** | Technical datasets appear, no Product listing | Asset discovery versus Product discovery |
| **DIS-A05** | Rich listing but wrong Product family | Representation fidelity versus qualification authority |
| **DIS-A06** | Listing refers to stale Product Version or trust record | Currentness and qualified status |
| **DIS-A07** | Fully governed automatic Product publication | Intentional authorization versus human button press |
| **DIS-A08** | Accidental automatic technical registration | Governed Product publishing versus incidental metadata |
| **DIS-A09** | AI concierge finds and correctly explains Product | Technology neutrality and grounded discovery |
| **DIS-A10** | Listing lacks a viable consumption/request route | Discovery versus consumption orientation |
| **DIS-A11** | Genuinely discoverable but analytically untrustworthy | Trust disclosure versus intrinsic trustworthiness |
| **DIS-A12** | Discovery surfaces disagree on current Product Version | Conflict handling and authoritative effective time |

Retain relevant source edge cases and explicitly distinguish modeled expected outcomes from executed evidence. Do not infer enterprise adherence from the illustrative scenarios.

## 16. Source provenance, open questions and status

### Source provenance and experimental authority

- **Directly inspected:** `pages/DPCH-PMDD-guidance/04-DPCH04.md` in DPCH.zip, and `AIPCH-PMDD-guidance/05-AIPCH05.md` in AIPCH.zip. Source concepts: intentional catalogue/marketplace publication, noncreator discovery and Product abstraction (DPCH04); current Product/version, correct Product Family, trust/qualification currentness and consumption orientation (AIPCH05).
- **Approved INFOPS specialization:** `INFOPS-0.1-IPCH-P01-D15-F01` approves the Information Product definition, six mandatory criteria, seven negative conditions, six evidence requirements, six open research questions and twelve unexecuted cases, while authorizing this draft's preparation only. `INFOPS-0.1-IPCH-P01-D16-F01` subsequently **accepted this prepared First-Pass draft only**, without final guide approval.
- **Assessment/guidance controls:** Previously approved D02–D05 experimental methodology and the owner-directed two-pass strategy. No upstream Product-family definition, ontology, marketplace rule or normative schema is amended by this guide.

### Open questions for Second Pass

| ID | Research question | Status |
|---|---|---|
| **DIS-R01** | How should independent findability be assessed for highly restricted audiences without unauthorized disclosure? | OPEN |
| **DIS-R02** | What informational context is sufficient for relevance evaluation without duplicating IPCH05 Self-Describing? | OPEN |
| **DIS-R03** | How is intentional publication established where a governed Product factory automatically publishes qualifying Products? | OPEN |
| **DIS-R04** | How should discovery currentness be assessed when Product, semantic, qualification and trust records have different effective times? | OPEN |
| **DIS-R05** | What minimum consumption orientation is required without requiring actual entitlement or consumption success? | OPEN |
| **DIS-R06** | How should AI concierge, semantic search and conventional catalogue discovery be assessed equivalently? | OPEN |

### Status and retained boundaries

- `IPCH04.md / FIRST-PASS-DRAFT-01 = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` under D16-F01; **this ZIP proposes experimental publication only, not final guide approval**.
- `DIS-A01–DIS-A12 = PROPOSED_UNEXECUTED`; `DIS-R01–DIS-R06 = OPEN`.
- First-Pass/Second-Pass separation is retained; G4–G6 and catalogue-wide review remain outstanding. IPCH01–IPCH03 experimental deployment and their open reviews remain unaffected.
- Parent programme: MVP-P01 D01–D08 approved, conceptual sequence stopped; Track B B01 completion `NOT_ESTABLISHED`, B02–B06 not authorized; prospective S04 conditional research closure and historical C06 safeguards retained; historical ledgers 65/6/7/7 and separate PC ledger unchanged; Q0–Q5 and F06/F14/F16 unresolved; 62 G06 E0 designs unexecuted, E1/E2 zero; G06-RO01–RO12 and G03-R01–R12 all 24 OPEN.
- **No repository modification, Docusaurus publication, empirical PMDD assessment, independent upstream authority audit, final individual-guide approval, obligation discharge or normative INFOPS release is claimed.**
