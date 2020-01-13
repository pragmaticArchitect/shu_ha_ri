# IPCH03 — Declarative

**Information Product Characteristic (IPCH) | PMDD maturity guidance**  
**Artifact:** `IPCH03-PMDD-GUIDE-01`  
**Revision:** `FIRST-PASS-DRAFT-01`  
**Status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` — D13-F01 approved the source/criteria baseline, and D14-F01 accepted this `FIRST-PASS-DRAFT-01` as an experimental prepared guide. **Publication via this overlay is proposed, not yet deployed; the guide has not been finally approved or adversarially validated.**  
**Authority:** Experimental E0 guidance only; not a normative Product qualification, semantic, compilation, policy or release standard.  
**Lineage:** `INFOPS-0.1-IPCH-P01-D13-F01` and `INFOPS-0.1-IPCH-P01-D14-F01`; DPCH03 / AIPCH03; IPCH D02–D05 assessment and guidance controls; owner-directed First-Pass / Second-Pass strategy.

> **Core assertion:** An Information Product is *Declarative* when its governing informational Promise, analytical context, intended outcomes, interfaces, constraints and applicable assertions are expressed through an **authoritative, structured, machine-interpretable Product definition in domain-relevant concepts**, sufficiently complete for governed validation and derivation of permissible realization, **without procedural implementation becoming the source of Product meaning**. Its authorized owner/delegate can govern essential declaration intent without engineering translation.

## 1. Characteristic identity and source lineage

- **Characteristic:** `IPCH03` — **Declarative**, Information Product family.
- **Direct source:** `DPCH03 — Declarative`, which requires domain-authored, business-intent-native declaration, not engineering-as-configuration, sufficient for platform derivation; **AIPCH03 — Declarative Specification**, which requires structured, sufficiently complete, authoritative, machine-interpretable Product specification for validation and compilation.
- **Source distinction:** DPCH03 primarily tests *who expresses what intent*, and whether engineering translation is avoided. AIPCH03 primarily tests *the structured, computable, authoritative representation of the Product*. Both concerns are retained; neither is silently reduced to a file format.
- **First-Pass authority:** D13-F01 approves six mandatory positive criteria `DEC-M01–DEC-M06`, seven negative criteria `DEC-N01–DEC-N07`, six evidence requirements `DEC-ES01–DEC-ES06`, and `DEC-R01–DEC-R06` as open research questions.
- **General assessment controls:** D02 Product/Version eligibility, applicability, evidence and findings; D03 experimental characteristic score mapping; D04 sixteen-section `IPCH-PMDD-GT-01`, evidence standard `IPCH-ES-01`, and non-duplication control `IPCH-NDC-01`.

## 2. What the characteristic asserts

A Product's essential informational identity must be **declared** rather than reconstructed from scripts, notebooks, pipelines, runtime configurations or documentation understood only by humans. The declaration must be capable of competent machine interpretation and sufficiently specify its Product-level Promise and conditions to support governed validation and derivation of a permissible realization.

A declaration is **intent-declarative**, not merely *technology-declarative*: YAML, JSON or any equivalent representation is insufficient when its primary meaning is an orchestration or infrastructure procedure. A valid declaration can include authoritative semantic references, analytical definitions, constraints and outcome assertions, without dictating physical execution plans.

The authorized Product Owner or delegate must be able to govern changes to the essential declared Product intent. This does **not** mean the owner must implement compilers or deployment systems or unilaterally override independently competent authority.

This characteristic does **not** by itself establish actual successful deployment (IPCH02), semantic correctness (IPCH11), runtime trustworthiness (IPCH06), compliance effectiveness (IPCH09), or complete testing/version maturity (IPCH13).

## 3. Information Product specialization

The declaration's governing subject is the **Information Product's informational Promise**: its analytical or informational purpose, intended consumers and uses, relevant measures/interpretations, contextual meaning, outcome expectations, applicable references and constraints, and declared consumption surfaces as appropriate to the Product.

The declaration may refer to externally governed semantics and dependencies; **referencing** an authoritative semantic definition is not the same as acquiring authority to redefine it. Information Product definition, semantic-definition Version, potential deployment specification, realization revision, compilation event and runtime occurrence remain distinguishable.

**Illustrative distinction:** Declaring the business definition of *liquidity coverage* (including applicable measures, temporal scope and interpretation) can be legitimate Product intent. Requiring the business Product Owner to supply a physical SQL join plan or pipeline DAG is typically technical implementation, not intent-native declaration. Whether a given analytical expression is domain semantics or procedural execution remains open under `DEC-R04`.

No particular descriptor naming, parser, DSL, execution engine, schema technology or platform is prescribed. This document does not adopt new normative INFOPROD/INFOPDS schemas or compilation mandates.

## 4. Assessment subject and authority

Assess **one identifiable Product and Version** with a particular governing declaration, assessed time and applicable enterprise profile. Document:

1. Exact Product identity, Version and independent D02 eligibility basis.
2. Applicable informational Promise and intended scope.
3. Declaration identity, Version/currentness and competent governing actor.
4. Machine-interpretation/validation basis and supported Product realization claim.
5. Relevant semantic references and independently governed constraints.
6. Evidence for owner/delegate control of material declaration evolution.
7. Establishing, supporting, contrary, missing, stale or disputed evidence and the assessment date.

Distinguish evidence about a *Product definition* from evidence of its *deployment specification*, compiled artifact, operational implementation or instance. The assessor (human or agent) must not independently confer Productness, semantic authority, binding approvals or final institutional maturity sign-off.

## 5. Applicability and N/A rules

**Default:** IPCH03 applies to an eligible, constituted Information Product. There is no generally established whole-characteristic `NOT_APPLICABLE` exception. Lack of a descriptor, missing ownership evidence, unimplemented compiler, or a reliance on scripts does **not** make the characteristic inapplicable.

Particular evidence methods can be not applicable in context: a Product with no production runtime may not have historical regeneration records; a Product without externally sourced dependencies may not need dependency-reference examples. The **underlying mandatory criterion** must still be evidenced by other appropriate, current means, where possible.

Any exceptional whole-characteristic `NOT_APPLICABLE` finding requires an affirmative competent D02 determination. A subject without required Product/Version eligibility is `NOT_ASSESSABLE`, not `NOT_MET` or `NOT_APPLICABLE`.

## 6. Distinctness and non-duplication

| Neighbour | Separate assessment claim |
|---|---|
| **IPCH01 — Domain-Owned** | Whether ownership/mandate is legitimate and effective; IPCH03 examines whether authorized Product intent governs an actual declaration. |
| **IPCH02 — Deployable** | Whether the actor can exercise lifecycle self-service; IPCH03 examines the computable, authoritative Product definition even where deployment remains manual. |
| **IPCH05 — Self-Describing** | Whether Product information is understandable/available to consumers; IPCH03 requires a governing machine-interpretable definition. |
| **IPCH09 — Compliant by Design** | Whether applicable controls are enforced; IPCH03 concerns declared policy posture and constraints. |
| **IPCH11 — Semantically Aligned** | Whether actual semantics conform; IPCH03 concerns competent declaration/references of meaning. |
| **IPCH13 — Testable & Versioned** | Whether testing/version governance is mature; IPCH03 needs an identifiable authoritative declaration for a Product/Version. |
| **IPCH16 — Interoperable & Composable** | Whether Products can actually interoperate/compose; IPCH03 may declare interfaces and dependencies. |

Common evidence may support more than one maturity claim; the reasoning and findings must remain independently established per `IPCH-NDC-01`.

## 7. Core mandatory positive criteria — `MET`

**All six applicable criteria are mandatory and conjunctive for `MET`. They are not individually weighted or averaged.**

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **DEC-M01** | **Intent-Native Declaration** | The Product's informational purpose, Promise, intended outcomes and relevant assertions are expressed using domain-relevant concepts rather than procedural implementation instructions. |
| **DEC-M02** | **Structured Machine-Interpretable Definition** | A structured Product declaration exists with an identifiable machine-interpretation basis, without reliance on humans to interpret its essential meaning for each realization. |
| **DEC-M03** | **Sufficient Product Definition** | The declaration sufficiently describes applicable intent, semantic references, relevant inputs/outputs, consumption interfaces, constraints and assertions to determine permissible Product realization. |
| **DEC-M04** | **Authoritative Source of Product Intent** | The declaration is the competent, governed source of truth for the assessed Product/Version; no hidden or competing procedural definition governs material Product intent. |
| **DEC-M05** | **Derived Realization Boundary** | The declaration together with independently governed rules supports validation and determination of permissible realization without ad hoc human engineering translation of essential Product intent. |
| **DEC-M06** | **Domain-Governed Declaration Evolution** | The legitimate Product Owner/delegate governs material changes to declaration intent without having to author procedural implementation artifacts. |

**Materiality:** An essential absence of authoritative, structured, domain-meaningful declaration cannot be offset by stronger evidence for other criteria. Conversely, each claimant must be assessed using competent evidence of the actual Product scope; formatting preferences or nonessential metadata discrepancies alone are not proof of foundational failure.

## 8. Core negative criteria — `NOT_MET`

| ID | Affirmatively demonstrated negative condition |
|---|---|
| **DEC-N01** | Essential Product meaning is primarily determined by procedural SQL, scripts, notebooks, pipelines or equivalent implementation rather than the declaration. |
| **DEC-N02** | The alleged domain declaration requires authoring technical pipeline, infrastructure, engine or orchestration configuration instead of expressing informational intent. |
| **DEC-N03** | Essential Product meaning, interfaces, constraints or assertions are materially absent from the purported declaration and cannot be derived under governed references. |
| **DEC-N04** | The Product is described only in human-readable documentation requiring recurring manual engineering interpretation to become a Product realization. |
| **DEC-N05** | Actual authoritative Product behaviour is determined by hidden implementation logic that materially contradicts or bypasses declared intent. |
| **DEC-N06** | The authorized Product actor cannot govern essential declaration changes without engineers translating or authoring its Product meaning. |
| **DEC-N07** | Declaration identity, Version or competent governing authority is indeterminate, so no authoritative declaration for the assessed Product/Version can be established. |

A negative indicator requires affirmative supporting evidence. Missing records alone do not establish `NOT_MET`; determine whether evidence is insufficient or a material deficiency has actually been demonstrated.

## 9. `PARTIAL`, `NOT_MET` and evidence-limited decisions

| Condition supported by sufficient evidence | Candidate result |
|---|---|
| All six mandatory applicable assertions are met and no material foundational counter-evidence defeats the claim | `MET` |
| A genuinely structured, domain-meaningful declaration exists, but material *non-foundational* completeness, control, interpretation or derivation capabilities are demonstrably incomplete | `PARTIAL` |
| A fundamental declarative condition is demonstrably absent (e.g. code is the authoritative Product definition, or no meaningful machine-interpretable declaration exists) | `NOT_MET` |
| Material uncertainty, contested source authority, staleness or contradictory evidence prevents a defensible conclusion | `EVIDENCE_LIMITED` (evidence qualifier, **not** a fifth maturity state) |
| Independent D02 Product/Version eligibility unestablished | `NOT_ASSESSABLE` |
| Competently justified exceptional whole-characteristic exclusion | `NOT_APPLICABLE`; no generic exception established here |

**Decision order:** Eligibility → applicability → each mandatory claim and contrary evidence → significance of outstanding uncertainty → foundational failure versus genuine partially functioning declaration → overall characteristic finding.

Do **not** use a simple number-of-criteria-met threshold for Partial or Met. A structured file generated from procedural code can be evidence of progress, but may fail authoritative source-of-truth requirements. A missing deployment event alone is not proof of IPCH03 failure if competent evidence establishes declaration-driven derivability.

## 10. Evidence signals and sufficiency

| Rule | Mandatory claim | Establishing evidence possibilities | Counter-evidence examples |
|---|---|---|---|
| **DEC-ES01** | DEC-M01 — Intent-native | Representative governed informational declaration, competent semantics and intended-purpose assertions | Declaration primarily specifies technical execution steps |
| **DEC-ES02** | DEC-M02 — Machine interpretation | Structured artifact plus interpretation/validation demonstration or equivalent competent evidence | Meaning is determined by manual reading of an informal document |
| **DEC-ES03** | DEC-M03 — Completeness | Clause/coverage analysis for governing Promise, references, interfaces, constraints and assertions in scope | Essential Product-level meaning remains implicit |
| **DEC-ES04** | DEC-M04 — Authority | Current, competent source-of-truth assignment for exact Product/Version plus consistency/correlation evidence | Hidden authoritative code or competing incompatible declarations |
| **DEC-ES05** | DEC-M05 — Derived realization | Governed validation and derivation demonstration/design evidence appropriate to lifecycle stage | Each realization needs ad hoc engineering reinterpretation of Product intent |
| **DEC-ES06** | DEC-M06 — Governed evolution | Owner/delegate change rights, representative declaration revisions or reproducible exercise | Engineers must author Product intent on the owner's behalf |

**Cross-cutting evidence rules:**

- **Subject alignment:** Evidence must identify exact Product/Version, declaration revision, relevant semantic-definition Version where applicable, realization basis and effective time. Do not mistake an implementation revision for a Product definition change.
- **Competence:** Check that each artifact or decision source is authoritative for its claim. A machine parser's existence does not establish semantic or Product-family authority.
- **Sufficiency:** Combine establishing, supporting and contrary evidence according to the claim and enterprise assurance profile; no universal required file type or product platform.
- **Currentness:** Historical successful compilation does not automatically establish present authoritative declaration or current applicability.
- **Contradictions:** Preserve unresolved materially conflicting definitions, versions or source-of-truth claims; do not silently choose a declaration by filename or timestamp alone.
- **Proportionality:** A permitted, reproducible design-stage validation/derivation demonstration may support the specified capability. Do not claim actual deployed outcomes where none occurred.
- **No dilution:** An enterprise may demand higher corroboration or shorter validity windows but cannot waive one of DEC-M01–M06 while claiming `MET` under the same guide.

## 11. Agent-assisted or human assessment decision rule

1. **Check D02 eligibility** for the specific Product/Version. If not established, return `NOT_ASSESSABLE` without a characteristic score.
2. **Establish applicability** using D02; absent an affirmative competent exception, treat IPCH03 as applicable.
3. **Identify the governing declaration** and its exact identity/Version, interpreted meaning, mandate and relationship to Product-level intent.
4. **Evaluate DEC-M01–DEC-M06 separately**, recording supporting, contrary, absent, stale and disputed evidence for each, using DEC-ES01–ES06.
5. **Check DEC-N01–DEC-N07** for demonstrable foundational failures; distinguish them from missing documentation or legitimate analytical expressions describing domain meaning.
6. **Resolve evidence conflicts only within valid competence.** Retain material disagreements about declaration authority or semantic definitions as unresolved when independent authority has not adjudicated them.
7. **Choose the characteristic finding:** all required claims adequately supported → `MET`; genuine declaration with demonstrable non-foundational gaps → `PARTIAL`; demonstrated foundational failure → `NOT_MET`; otherwise retain `EVIDENCE_LIMITED` if uncertainty prevents conclusion.
8. **Record the assessment rationale:** subject, guide revision, enterprise profile, claims, evidence/counter-evidence, limitations, assessment date and competent human review/sign-off as applicable.
9. **Only after a defensible characteristic finding**, apply D03 score mapping. Do not independently determine Product-family qualification, normative conformance or release authorization.

This sequence is implementation-neutral guidance. It is **not executable agent code** and does not prescribe AI models, prompts, scoring engines, schemas, APIs or workflow technology.

## 12. PMDD scoring treatment

| Characteristic finding | D03 experimental score contribution |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |
| Competently established `NOT_APPLICABLE` | Excluded from applicable denominator |
| Unresolved evidence (`EVIDENCE_LIMITED`) | No invented point score; preserve D03 uncertainty treatment/bounds where applicable |
| `NOT_ASSESSABLE` | No characteristic score |

The five dimensions of a maturity decision must not be confused with the six *criteria*: there are **six mandatory criteria and one overall characteristic finding**. No per-criterion averaging, automatic critical cap, L0/L1/L2 thresholds or normative release gates are created here. D03's independent critical-condition categories remain applicable as already approved.

## 13. Critical assurance and governance boundaries

**Declaration quality is not independent institutional permission.** The following authorities are retained:

| Boundary | Not conferred by IPCH03 |
|---|---|
| BPS/PIN and Product-family/Compound authorities | Generic Productness and competing-family qualification |
| GEARA | Analytics architecture responsibility |
| GEARM | Competent informational semantics, definitions and semantic governance |
| INFOPROD/INFOPDS and other DPP/realization constructs | Independently specified definition/deployment/realization and compilation responsibilities |
| PFI/HDIP | Platform realization and operational implementation |
| Legal/policy/assurance/consequential-action governance | Binding permissions, controls, review or institutional sign-off |

An owner may author an intent-native Product definition while being constrained by independent semantic, policy and realization governance. Such constraints are not themselves failures of IPCH03.

A materially inconsistent or non-authoritative declaration may also implicate independent assurance concerns; the agent must report these separately under the approved D03 critical-status framework, not infer institutional consequences from the characteristic score.

## 14. Reassessment and evolution triggers

Consider reassessment when: the governing declaration or Product Version materially changes; the informational Promise, consumer scope or declared constraints change; relevant semantic-definition Versions or external dependencies change; the owner/declaration authority changes; a compiler or interpretation basis materially changes; implementation-to-declaration divergence appears; new contrary evidence questions the source of truth; or the enterprise's valid assurance profile changes.

Historical results retain their own Product, Version, declaration revision, evidence effective-time and applicable assessment profile. Reassessment does not overwrite previous findings or treat a deployment occurrence as a redefinition of Product meaning.

## 15. Adversarial and boundary cases — First-Pass fixtures

**Proposed conceptual cases only; all are `UNEXECUTED`.** They do not claim empirical conformance or G4 completion.

| Case | Counterfactual challenge | Intended distinction |
|---|---|---|
| `DEC-A01` | YAML lists SQL statements, DAGs and engines | Machine-readable technology configuration ≠ intent declaration |
| `DEC-A02` | A non-engineer can edit a business-like Product form but engineers reinterpret its meaning every release | Intent-native UI alone ≠ authoritative computable definition |
| `DEC-A03` | Complete structured domain declaration exists, but deployment is engineer-operated | IPCH03 versus IPCH02 separation |
| `DEC-A04` | Human-readable Product description has excellent semantics but no machine interpretation basis | Human documentation ≠ computable declaration |
| `DEC-A05` | Structured specification is generated from procedural code; code governs changes | Artifact existence ≠ authoritative source of Product intent |
| `DEC-A06` | Product intent declaration omits material consumption constraints | Sufficient definition and evidence of a non-foundational versus foundational gap |
| `DEC-A07` | Relevant domain formula appears in an otherwise valid declaration | Domain expression versus procedural implementation; DEC-R04 |
| `DEC-A08` | Declaration cites an independently GEARM-governed meaning with valid Version reference | Declaration versus semantic authority |
| `DEC-A09` | Two current incompatible declarations claim authority for the same Product/Version | Evidence-limited versus demonstrated contradiction |
| `DEC-A10` | A historical declaration compiled, but current runtime diverges materially | Provenance and currentness versus hidden implementation authority |
| `DEC-A11` | Domain can govern intent changes, but publication needs legitimate policy approval | Declarative maturity versus governance approval |
| `DEC-A12` | Product meets all declaration criteria but has ineffective testing and version operations | IPCH03 versus IPCH13 non-duplication |

## 16. Source provenance, open questions and status

### Source and authorization register

| Reference | Contribution | Authority status |
|---|---|---|
| `DPCH03` (canonical `03-DPCH03.md`) | Domain-authored business-intent declaration; rejection of engineering-as-configuration; generated technical realization | Upstream Data Product guidance, not amended |
| `AIPCH03` (canonical `03-AIPCH03.md`) | Structured, authoritative, sufficiently complete, machine-interpretable Product specification | Upstream AI Product guidance, not amended |
| `INFOPS-0.1-IPCH-P01-D13-F01` | Approved experimental IPCH03 assertion and DEC-M/N/ES baseline; open questions | First-Pass E0 guidance preparation only |
| `INFOPS-0.1-IPCH-P01-D14-F01` | Accepted `IPCH03.md / FIRST-PASS-DRAFT-01` as experimental prepared guidance only | No final guide, adversarial or normative approval |
| `D02/D03/D04/D05` | Eligibility, evidence, scoring, guidance template and review control | Approved experimental controls; no new normative authority |
| First-Pass/Second-Pass owner direction | Publish usable experimental coverage first, defer outstanding deep review to Second Pass | Does not waive reviews or normative boundaries |

### Open Second-Pass research questions

| ID | Research question | Status |
|---|---|---|
| `DEC-R01` | What is sufficient declaration completeness across differing Information Product realization patterns? | OPEN |
| `DEC-R02` | How to substantiate machine interpretation and deterministic validation without prescribing a universal compiler? | OPEN |
| `DEC-R03` | How to establish authority when declarations and generated artifacts evolve at different rates? | OPEN |
| `DEC-R04` | Where is the boundary between legitimate analytical definitions/formulas and procedural implementation logic? | OPEN |
| `DEC-R05` | When does a genuine but incomplete declaration warrant `PARTIAL` versus foundational `NOT_MET`? | OPEN |
| `DEC-R06` | How to prevent duplicate maturity claims across semantic alignment, testability and self-description? | OPEN |

### Status and provenance limits

- `IPCH03.md = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED` under owner-approved D14; the specific First-Pass draft is accepted, **not finally approved**.
- **Publication:** `NOT_DEPLOYED`; no INFOPS repository modification made by producing this file.
- **First Pass:** active; IPCH01/IPCH02 are deployed experimentally as reported by the owner; IPCH03 is the next draft.
- **Second Pass:** not started; G4/G5/G6 and cross-catalogue adversarial validation remain outstanding.
- **Source/authority limits:** No independent new verification of all primary BPS/PIN, GEARA, GEARM, INFOPROD/INFOPDS or parent programme authority is claimed.
- **Programme constraints:** The stopped MVP D01–D08, parent Track B B01 completion `NOT_ESTABLISHED`, conditional S04 research closure, historical C06 safeguards/ledgers (65/6/7/7, PC ledger separate), Q0–Q5 and F06/F14/F16 unresolved, 62 G06 E0 designs unexecuted, E1/E2 = 0, all 24 G06-RO/G03-R obligations OPEN and normative release `NOT_AUTHORIZED` remain unchanged.

---

## Enterprise assessment profiles — configurability without dilution

The enterprise determines the implementation technology, declaration format, interpretation mechanisms, evidence corroboration, freshness and assurance rigor. This document does not mandate a specific Product factory, source repository, interface, parser or execution system.

**Non-dilution invariant:** Enterprise policy may make it harder to substantiate `MET`, or set additional local obligations, but it may not remove or redefine `DEC-M01–DEC-M06` and still claim the same IPCH03 characteristic is `MET`. A documented, legitimate enterprise assessment profile is part of the assessment provenance, not a replacement for the common characteristic definition.
