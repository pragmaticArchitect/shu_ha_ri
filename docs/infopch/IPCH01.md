# IPCH01 — Domain-Owned

**Information Product Characteristic (IPCH) | PMDD guidance**  
**Artifact:** `IPCH01-PMDD-GUIDE-01`  
**Revision:** `DRAFT-02` (Markdown expression; no new substantive revision)  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED` — documentary G2 `PASS`; G3 `PASS_WITH_QUALIFICATIONS`; G4/G5/G6 `NOT_EXECUTED`  
**Authority:** Research guidance only; neither normative Product-family qualification nor enterprise policy.  
**Lineage:** INFOPS-0.1-IPCH-P01 D01–D10; canonical DPCH01 and AIPCH01 guidance.

> **Core invariant:** An Information Product is Domain-Owned to the extent that a legitimate governing domain has identifiable, accountable, **effective** authority over the Product's informational Promise, outcomes and material evolution. Nominal ownership, building, hosting or consuming the Product does not by itself satisfy this characteristic.

## 1. Characteristic identity and source lineage

- **ID:** `IPCH01`; **name:** Domain-Owned; **family:** Information Product.
- **Source inheritance:** `DPCH01` (Authoritative Domain Test: authority over meaning/capability, outcome accountability, evolution control) and `AIPCH01` (explicit, effective, traceable Product ownership as a *maturity* claim).
- **Internal standards:** `IPCH-PMDD-GT-01` (16-section guidance), `IPCH-ES-01` (evidence), `IPCH-NDC-01` (non-duplication), approved D02 assessment vocabulary and D03 scoring.
- **Unresolved source tension:** DPCH01 employs strict Data Mesh qualification language; AIPCH01 separates Product qualification from ownership maturity. IPCH01 assesses **maturity only** under the experimental INFOPS D02 framework. This does not amend either upstream source or establish Product-family qualification rules.
- **Verification limitation:** Primary BPS/PIN, GEARA and GEARM authority documents have not been independently reverified under the IPCH01 research sequence.

## 2. What the characteristic asserts

An eligible Information Product demonstrates Domain-Owned maturity where its governing **informational Promise** is subject to (a) a legitimate domain mandate, (b) identifiable and traceable accountability, and (c) effective governing decision rights over Product purpose and material evolution, subject to the authority of independently competent functions.

The **Authority–Accountability–Control (AAC)** test applies to the Product's own governing scope:

1. **Authority:** Who has the legitimate mandate to govern the informational Promise and intended use?
2. **Accountability:** Who is answerable for Product-level informational outcomes, deficiencies and response obligations?
3. **Control:** Who can govern material Product scope, version, lifecycle and evolution through valid decision rights and delegations?

The owner need not personally implement, host, monitor or approve every component. Nor must the owner be able to override independent semantic, architecture, policy or release authorities. An owner designated only in a metadata field, with no substantive mandate or effective control, is insufficient.

## 3. Information Product specialization

The Product's informational Promise—not automatically its source data, execution engine or consumer—is the object of ownership. The authoritative owner of Payments Data, for example, need not own a separate Treasury liquidity-forecast Information Product built using those data. The latter requires its own legitimate governing mandate.

Keep distinct:

| Governing concern | Competent responsibility |
|---|---|
| Information Product Promise, intended scope and Product-level outcomes | Legitimate Information Product ownership function |
| Upstream Data Product meaning/obligations | Source Data Product authority |
| Governing semantic definitions | GEARM / competent semantic authority |
| Analytical architectural responsibilities | GEARA / competent architecture authority |
| Product-family or Compound qualification | Independent BPS/PIN and competent family authority |
| Engineering, runtime, deployment | Applicable realization and operations authority |
| Binding controls and consequential actions | Competent legal, policy, assurance and consumer authorities |

An enabling or technology-related domain **can** be a legitimate Product owner where it substantively governs the relevant informational capability; an implementation team is not an owner merely because it builds or hosts the Product.

## 4. Assessment subject and authority

Every proposed assessment must identify the **exact Product and Version**, qualifying/experimental eligibility basis, informational Promise, assessed time, applicable ownership scope, evidence currentness and competent reviewers.

Distinguish:

- **Governing domain function:** institution/function with the legitimate mandate for the Promise.
- **Accountable representative:** identifiable person or constituted accountable role that can be held answerable for governing decisions and outcomes.
- **Delegated decision authority:** validly assigned authority, with scope, limits and retained accountability traceable.

Federated ownership is possible where decision rights, final accountability for each relevant decision, escalation and delegations are effective. A departmental label or Product registry entry by itself proves neither legitimate mandate nor effective control. PMDD assessors and agents cannot create, transfer or arbitrate institutional authority.

## 5. Applicability and N/A rules

**Presumption:** IPCH01 is applicable to an eligible, constituted Information Product. No generic whole-characteristic `NOT_APPLICABLE` case has been established.

Absence of an owner, missing records, third-party operation, ownership disputes, or transition do **not** make the characteristic N/A. A specific *evidence mechanism* may be inapplicable (no incident history, no relevant change event, no federated arrangement or a different valid roadmap format), but the underlying accountable-ownership obligation remains. Whole-characteristic N/A requires separately competent, affirmative justification under D02. Missing Product/Version eligibility means `NOT_ASSESSABLE`, **not** N/A or a zero score.

## 6. Distinctness and non-duplication

IPCH01 evaluates **who legitimately and effectively governs** the Information Product. It does not automatically establish:

- IPCH12 **Consumption-Driven Intent**: genuine consumer-driven purpose;
- IPCH11 **Semantically Aligned**: conformance of meaning;
- IPCH03 **Declarative**: governed specification expression;
- IPCH09 **Compliant by Design**: operative policy controls;
- IPCH14 **Economically Accountable**: evidenced Product economics;
- IPCH06 **Trustworthy**: analytical or evidential validity.

The same document may be evidence for distinct claims, but its existence cannot be counted as proof of all of them. The claim supported by each evidence item must be specified.

## 7. Core mandatory positive criteria — `MET`

All five criteria below are **mandatory to demonstrate a `MET` finding within this experimental IPCH01 guidance**. Enterprises may demand stronger or fresher evidence but cannot waive a criterion while continuing to report unqualified IPCH01 `MET` against this guide.

| ID | Mandatory assessment claim | Sufficient evidence must establish |
|---|---|---|
| **OWN-M01 — Identifiable Accountable Owner** | An identifiable and effective accountable ownership arrangement exists for the assessed Product scope. | A current competent ownership assignment, with traceable accountable representation for the exact Product/Version or valid logical scope. |
| **OWN-M02 — Legitimate Domain Mandate** | The governing function is legitimately authorized to own the informational Promise. | A valid mandate or delegation covering that Promise, rather than merely the function's title or technical responsibilities. |
| **OWN-M03 — Effective Decision Rights** | The owner meaningfully governs Product purpose, intended use and scope within its mandate. | A competent decision-rights basis plus proportionate evidence of operational effectiveness/readiness; not just ceremonial sign-off. |
| **OWN-M04 — Outcome Accountability** | Accountability for Product-level informational outcomes and relevant deficiencies is assigned and operative. | A traceable responsibility, response and escalation arrangement; distinguish Product obligations from independently governed downstream actions. |
| **OWN-M05 — Evolution Authority** | The owner governs material Product evolution, including change and lifecycle decisions through legitimate delegation. | Authorized lifecycle/change powers and proportionate evidence of functioning control or readiness when no change event occurred. |

**AAC is not an arithmetic checklist.** Five criteria support a single reasoned characteristic finding. There are no individual criterion weights, no two-of-three shortcut and no average of criterion scores.

## 8. Core negative criteria — `NOT_MET`

Evidence of these conditions can establish a genuine ownership deficiency:

| ID | Demonstrated condition |
|---|---|
| **OWN-N01** | No legitimate accountable Product owner exists. |
| **OWN-N02** | The claimed owner has no substantive governing domain mandate. |
| **OWN-N03** | Ownership is ceremonial; effective authority is absent. |
| **OWN-N04** | Material changes to Product purpose or intended use bypass legitimate owner authority. |
| **OWN-N05** | Product-level outcome accountability is demonstrably absent. |
| **OWN-N06** | Unrelated delivery priorities control Product evolution without effective authorized ownership. |
| **OWN-N07** | Cross-domain responsibility is fragmented and has no functioning decision/accountability arrangement. |

A **demonstrated foundational AAC defect** can justify `NOT_MET` notwithstanding otherwise strong administrative evidence. Mere lack of an artifact, a delegated operational step, or an unrelated administrative inconsistency does not automatically demonstrate such a defect. Explain materiality and cite the actual evidence.

## 9. `PARTIAL`, `NOT_MET` and evidence-limited decisions

| Finding | Required qualitative conclusion |
|---|---|
| **MET** | All five applicable core ownership claims are adequately supported; no material unresolved contradiction prevents this conclusion. |
| **PARTIAL** | Legitimate ownership is established and material capabilities are demonstrably functioning, but one or more relevant capabilities are demonstrably incomplete **without** an established foundational AAC absence. |
| **NOT_MET** | Competent, current evidence demonstrates the absence of a foundational legitimacy, accountability or effective-control requirement. |
| **EVIDENCE_LIMITED** | Material lack, staleness, dispute or conflict prevents a defensible characteristic finding. This is an **evidence qualifier**, not a fifth maturity score. |
| **NOT_APPLICABLE** | Only upon independent affirmative applicability justification; no generic IPCH01 whole-characteristic exception is established. |
| **NOT_ASSESSABLE** | D02 eligibility is not established; outside characteristic maturity scoring. |

**Precedence:** Verify eligibility → verify applicability → inspect claims, evidence and conflicts → decide whether a defensible finding is possible → distinguish demonstrated foundational failure from evidenced partial capability → report `MET` only if all mandatory claims are established. Where material uncertainty prevents the particular conclusion, retain it. Conversely, a separate demonstrably negative ownership claim must not be hidden behind an unrelated ownership dispute. This mixed-evidence interaction remains an unexecuted G4 challenge.

A proposed remediation plan does not count as present maturity. No numeric averaging of the five claims is authorized.

## 10. Evidence signals and sufficiency

| Claim | Establishing evidence (examples) | Corroborating / contrary signals |
|---|---|---|
| OWN-M01 | Competent appointment/assignment for Product scope | Registry; competing current owner appointments |
| OWN-M02 | Domain mandate or valid delegation over Promise | Charter; evidence mandate belongs elsewhere |
| OWN-M03 | Authorized decision-rights model | Decision/exercise records; systematic bypass |
| OWN-M04 | Accountable outcome, response and escalation arrangement | Incident/readiness evidence; disclaimed accountability |
| OWN-M05 | Product lifecycle/change mandate | Roadmap/change decisions; unauthorized material changes |

**Mandatory evidence evaluation rules:**

- **ES-D01 — Identity alignment:** Exact Product, Version, scope and relevant effective time.
- **ES-D02 — Mandate verification:** Legitimate, competent authority rather than labels alone.
- **ES-D03 — Effective authority:** Constitutional rights and proportionate evidence of effectiveness/readiness.
- **ES-D04 — Accountability traceability:** Product-level responsibility separated from upstream/consumer responsibility.
- **ES-D05 — Currentness:** Historical authority is not automatically current authority.
- **ES-D06 — Contradictions:** Record material disputes, provenance, applicability and resolution status.
- **ES-D07 — Proportionality:** Equivalent credible evidence may suffice; absence of incidents or past change events is not itself an ownership failure.

No universal evidence document, technology, registry, ticketing system or platform is mandatory. Sufficiency is **claim-specific**, and evidence may be authoritative, supporting, contrary, missing, stale or disputed.

**Conflict handling (research-local evidence dispositions, not maturity states):**

1. `RECONCILED`: Competent evidence and effective times resolve the apparent conflict.
2. `NON_MATERIAL`: Recorded conflict does not affect the material ownership claim.
3. `MATERIAL_UNRESOLVED`: The conflict prevents a defensible finding on a material claim.
4. `DEMONSTRATED_DEFECT`: Competent evidence establishes an actual ownership failure, rather than mere uncertainty.

An agent or assessor must not invent a hierarchy among disputed authorities or resolve a dispute outside its mandate.

## 11. Agent-assisted or human assessment decision rule

The *same claims and meaning* apply to manual, rules-based and agent-assisted assessment. A conforming experimental assessment must:

1. Establish Product/Version assessment eligibility under D02; otherwise return `NOT_ASSESSABLE`.
2. Establish applicability; do not turn an absent owner into N/A.
3. Evaluate all OWN-M01–OWN-M05 and applicable OWN-N01–OWN-N07 against claim-specific, dated evidence.
4. Examine delegations and federated accountability, while preserving independent semantic, architectural, policy and realization authorities.
5. Record and disposition material evidence contradictions using the four research-local categories.
6. Determine whether evidence permits a defensible `MET`, `PARTIAL` or `NOT_MET` finding under Section 9; otherwise report the unresolved claim with `EVIDENCE_LIMITED`.
7. Record the governing assessment profile, evidence provenance, contrary evidence, effective date, rationale and accountable review disposition.
8. Report potential critical-governance concerns separately; do not conflate them with the maturity score.

An agent may propose a finding and explain it. It does not thereby gain the authority to determine institutional mandates, qualify Product families or approve normative release.

## 12. PMDD scoring treatment

Apply the **existing D03 experimental characteristic-level mapping**, only *after* a supported finding:

| Characteristic finding | Experimental contribution |
|---|---:|
| MET | 1.0 |
| PARTIAL | 0.5 |
| NOT_MET | 0.0 |
| Competently justified NOT_APPLICABLE | Exclude from applicable denominator |
| Evidence-limited unresolved | No fabricated score; apply D03 bounded uncertainty where denominator is established |

Experimental IPCH scoring uses equal characteristic weights. Individual OWN-M criteria are **not separately weighted or averaged**. No IPCH L0/L1/L2 bands, automatic maturity caps or obligation-to-characteristic numeric aggregation are established.

## 13. Critical assurance and governance boundaries

A foundational ownership defect may also raise an independently governed assurance or policy issue, but IPCH01 maturity does not itself authorize an institutional consequence, deployment block, Product disqualification or remediation order. Preserve the four independent D03 critical-status categories and applicable competent-authority determinations. `MET` in Domain-Owned does not establish Trustworthy, Compliant by Design, semantic alignment or authorized consequential action.

## 14. Reassessment and evolution triggers

Reconsider IPCH01 where owner/mandate changes, delegation or federated arrangements change, Product scope or Promise materially evolves, responsibility transfers, a significant failure exposes ineffective accountability, relevant authority evidence expires, or current records conflict. Preserve historical decisions against the exact subject, Version and effective time. No universal reassessment schedule is imposed here.

## 15. Adversarial and boundary cases

The following cases are **research fixtures, not executed tests**:

| ID | Challenge |
|---|---|
| DO-01 | Platform operation mistaken for ownership |
| DO-02 | Ceremonial registry owner |
| DO-03 | Consumer use mistaken for ownership transfer |
| DO-04 | Source Data versus Information Promise ownership |
| DO-05 | Federated accountability and escalation |
| DO-06 | Legitimate enabling/technology domain mandate |
| DO-07 | Product-family eligibility versus ownership maturity |
| DO-08 | Owner constrained by independent semantic/policy powers |
| DO-09 | Independent downstream misuse and consequence attribution |
| DO-10 | Transitional ownership and evidence-backed Partial |
| DO-11 | Effective ownership alongside poor informational quality |
| DO-12 | Apparently conflicting records with distinct valid effective periods |
| DO-13 | Two current authorities asserting incompatible mandates |
| DO-14 | Legitimate owner cannot override GEARM/enterprise policy |
| DO-15 | Legitimate ownership with transitional lifecycle control |

Additional **unexecuted G4 carry-forwards**: `G4-C01` — distinguish unresolved mandate evidence from independently demonstrated AAC failure; `G4-C02` — test accountable representation and delegated/federated decision rights without imposing unilateral control. No G4 result is claimed.

## 16. Source provenance, open questions and status

**Canonical source files consulted:**

- `DPCH.zip/pages/DPCH-PMDD-guidance/01-DPCH01.md`: authoritative domain AAC test, not a mere owner field; recognizes substantive enabling-domain mandates and rejects technical implementation as authority by default.
- `AIPCH.zip/AIPCH-PMDD-guidance/01-AIPCH01.md`: effective accountable owner and traceable authority; ownership maturity separated from AI Product qualification.

**Research lineage:** D06 bounded G1 source intake; D07 DRAFT-01 accepted; D08 G2 qualified pass/G3 remediation required; D09 DRAFT-02 prepared; D10 G2 PASS/G3 PASS WITH QUALIFICATIONS and DR-01–DR-08 `DOCUMENTARY_REMEDIATION_VERIFIED` only. These decisions are preserved, not retrospectively rewritten.

**Open:** R01 legitimate authoritative domain; R02 federated accountability; R03 attribution of downstream consequences; R04 DPCH01/AIPCH01 qualification-language tension. BPS/PIN/GEARA/GEARM primary authority re-verification remains outstanding.

**Guide lifecycle:** `EXPERIMENTAL_DRAFT_PREPARED`; **G4, G5, G6 `NOT_EXECUTED`; final individual-guide approval `NOT_APPROVED`; no empirical Product assessments; no repository modifications; no normative INFOPS release.**

---

## Enterprise assessment profiles — permitted flexibility without dilution

An enterprise may select stronger or more proportionate **evidential** requirements, review roles, freshness windows, corroboration expectations, sampling and assurance controls. It may implement assessment manually, deterministically, agentically or using a combination.

An enterprise **must not silently waive** OWN-M01–OWN-M05, reinterpret a demonstrated foundational absence as `MET`, treat missing evidence as `NOT_MET`, invent an unapproved N/A, override D02 eligibility, or substitute averaging for the D03 characteristic-level decision rule while claiming adherence to *this* experimental IPCH01 guide. An organization choosing different substantive definitions or criteria must identify its assessment as a **separate enterprise profile/variant**, not unqualified conformance to this guide.

**Assessment portability:** Record the guide revision, enterprise assessment-profile identifier/version, exact Product/Version, governing Promise, date, claims and evidence, material contradictions, finding/limitation, and authorized accountable reviewer. Different enterprise stringency can lead to different evidence-based outcomes; comparability requires disclosure of the applied profile.

> **Boundary:** The guide defines *what* a Domain-Owned maturity claim requires and *how* it is evidentially justified. The enterprise chooses *how* to implement both the Product and its assessment. No implementation technology is prescribed.
