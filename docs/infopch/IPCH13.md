# IPCH13 — Testable & Versioned: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH13-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Principal sources:** `DPCH13` (Data Product) and `AIPCH14` (AI Product), separately interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D33-F01 = APPROVED_EXPERIMENTAL_E0` — criteria baseline; `INFOPS-0.1-IPCH-P01-D34-F01 = APPROVED_EXPERIMENTAL_E0` — owner acceptance of this experimental draft only  
> **Guide status:** `DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `APPROVED_EXPERIMENTAL_E0` (D34, draft only)  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This is a **prepared, non-normative experimental First-Pass guidance artifact**, not a record that a qualified Product was tested, that automated suites ran, that an exception was issued, that a promotion gate operated or that any Product release occurred. D34 owner acceptance of this experimental draft is recorded; packaging does not establish live publication, operational testing or final approval. Human competent authorities retain their independently established decision rights. Original D05 sequence remains historically preserved; the numerical First-Pass sequence is owner-directed.

## 1. Characteristic identity and source lineage

| Field | Experimental First-Pass position |
|---|---|
| Characteristic | `IPCH13 — Testable & Versioned` |
| Guide | `IPCH13-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01` |
| Approved decision | `INFOPS-0.1-IPCH-P01-D33-F01`, F01.1–F01.16 |
| Assessment subject | Independently eligible Information Product/Version, its governed informational Promise, applicable testable assertions, evolution/consumer contracts and attributable evidence at assessment time |
| Principal source lineage | `DPCH13 — Testable & Versioned` / `AIPCH14 — Testable & Versioned` |
| Mandatory conjunctive criteria | `TAV-M01–TAV-M08` |
| Negative criteria | `TAV-N01–TAV-N09` |
| Evidence requirements | `TAV-ES01–TAV-ES08` |
| Unexecuted challenge designs | `TAV-A01–TAV-A12` |
| Open research | `TAV-R01–TAV-R08` |
| D02 | `MET`, `PARTIAL`, `NOT_MET`, independent `EVIDENCE_LIMITED`; competent `NOT_APPLICABLE`; eligibility-dependent `NOT_ASSESSABLE` |
| D03 scoring | `MET=1`, `PARTIAL=0.5`, `NOT_MET=0` at characteristic level only |

**Exact principal sources reopened for preparation:** `DPCH.zip → pages/DPCH-PMDD-guidance/13-DPCH13.md` and `AIPCH.zip → AIPCH-PMDD-guidance/14-AIPCH14.md`, extracted as `dpch13_source.md` and `aipch14_source.md`. These documents inform the IPCH13 proposed specialization; they do not independently authorize INFOPS qualification, operational tests or semantic/policy amendments.

**DPCH13:** “Version-Controlled and Contract-Tested” concerns intentional, visible Product evolution through explicit meaningful versions and automated consumer-facing contracts. Those contracts include structure, meaning/units/invariants, quality such as freshness, and applicable policy obligations. Pre- and post-publication validation, breaking-change visibility and consumer protection matter. Versioned pipelines alone, SQL execution tests alone and silently broken consumer expectations are insufficient. Source examples: schema tests without semantics `Partial`; versioned releases and contract tests `Met`; manual coordination in lieu of automation `Not met`.

**AIPCH14:** “Version-Controlled and Behaviorally Testable” requires explicitly traceable Product states, reproducible automated behavioural tests, validation gates, regression protection and managed consumer compatibility. It calls for the entire AI Product—behaviour, specification and dependencies—to be versioned; mere model versioning is insufficient. Source examples: model versioned but not Product `Not met`; existing but unreproducible tests `Partial`; Product versions and automated behavioural tests `Met`; continuous learning without version control `Not met`. Its AIPROD/AIPDS and model examples remain AI-specific analogies, not Information Product-family obligations.

**Material source tensions remain open:** DPCH13 schema-only tests `Partial` versus mandatory semantics protection (`TAV-R02`); AIPCH14 nonreproducible tests `Partial` versus its reproducibility precondition (`TAV-R03`); AIPCH14 every-change-versioned-state language versus separately qualified Information Product/Version, dependency and realization identities (`TAV-R01`). Do not silently resolve them.

## 2. What the characteristic really asserts

> **IPCH13 — Testable & Versioned:** An Information Product is Testable & Versioned when its governed informational capability evolves through explicitly identifiable and traceable Product versions, whose material changes are evaluated through automated, reproducible, Product-level tests of its declared intent, informational meaning, analytical behaviour, quality expectations, consumption contracts and applicable constraints; promotion and continued consumption are governed to detect regressions, control compatibility and prevent unannounced changes to consumer expectations.

This is the **D33-approved experimental Information-specific definition**. Versioning does not mean “the transformation code is in Git,” and testing does not mean “a query executes successfully.” Both must address what the Product promises to consumers and the changes that could break it. The protected subject is a **governed informational capability**, not the stability of one component.

Two distinct claims must be proven for mature operation. First, an authoritative and attributable Product version identity exists, and its contract history tells consumers what has or has not changed. Second, tests actually exercise material Product-level informational promises with results traceable to the relevant version and governed promotion decision. Describing a future automated test facility is an E0 *design*, not evidence of either execution or operating effectiveness.

Compatibility is not the same as prohibiting every breaking change. A material breaking change may be legitimate if explicitly identified, validly governed and accompanied by appropriate consumer protections. Silent, unassessed changes to a calculation, measure meaning, interpretation rule or consumer contract cannot be inferred to be safe merely because the output shape remains stable.

## 3. Information Product specialization

For an Information Product, the consumer-observable capability can include calculated informational measures, classifications, derived assertions, analytical frames, population boundaries, time cutoffs, assumptions, units and confidence/limitation disclosures. Those attributes can change *meaning* without changing transport schema. Tests therefore need Product-bound assertions on **what the resulting information means and how it is derived**, not only on row counts, successful SQL execution or endpoint availability.

**Illustrative example — intraday liquidity information.** A Product produces “available liquidity” per legal entity and currency. A transformation update includes a new contingent-funding category. The API field name, data type and response shape are unchanged. A technical regression suite may pass while the business interpretation shifts. A consumer-protective test regime checks governed measure definition, permitted inputs, valuation or cut-off assumptions, invariants, changes against prior guarantees and explicitly agreed compatibility handling. This is a teaching illustration, not a verified enterprise rule or Product assessment.

**Product-bound analytical assertions** may express calculation invariants, expected outputs on controlled input fixtures, temporal consistency, cross-output reconciliation, aggregation invariants, segment inclusion/exclusion, semantic definition bindings, error/uncertainty representations and quality thresholds where they are material and legitimately specified. No universal assertion list or technology is prescribed. Tests should be suited to the actual informational Promise and approved contracts.

**Versioned reproducibility** may depend on historical source snapshots, reference data, semantic revisions, test inputs, time, feature flags, realization dependencies and expected outputs. A Product whose result is legitimately time-sensitive need not produce the same value from different populations. Reproducibility means reconstructing appropriately controlled test conditions and judging observed outcomes against the relevant deterministic, bounded or other justified expectations; exact thresholds remain `TAV-R05 = OPEN`.

**Consumer-facing change:** a corrected analytical calculation may constitute a breaking change if downstream interpretation changes, even when it fixes a defect. Conversely, an infrastructure revision preserving the Product Promise may not require a new business Product Version under a future competent rule; the need to keep versioned Product states and realization revisions distinct remains `TAV-R01 = OPEN`.

## 4. Assessment subject and authority

Keep the following identification and authority domains separate before drawing any maturity conclusion:

1. **Qualification and D02 eligibility:** establish the exact independently eligible Product/Version through BPS/PIN generic Productness and competent Information-family/Compound determination. IPCH13 maturity does not qualify the Product or confer an execution mandate.
2. **Governing Product state:** Product identity, Product Version, approved informational Promise, Product-bound contracts, material change history and effective applicability. A repository tag or release label without competent Product attribution is not sufficient.
3. **Semantic and analytical definitions:** independently governed semantic-definition/version, measure derivations and analytical assumptions. GEARA/GEARM semantic competence is not displaced by test automation or the IPCH assessor.
4. **Test specification:** test-suite identity/version, assertion scope, oracle/expected-result authority, test data, controlled assumptions and applicability. Test code is not a legal or semantic approval.
5. **Test executions:** actual automated occurrences, inputs, environment, observed results, defects, date and time, and their link to an exact assessed Product/Version. A test plan is not a test run.
6. **Realization and dependencies:** realization revision, external component/dependency versions, compilation pack, deployment profile and occurrence context. None alone becomes Product Version by implication.
7. **Governed promotion and consumer communication:** validation gate evidence, competent disposition, compatibility classification, notice, coexistence or migration where appropriate. Human authority and applicable organizational process must independently be established.
8. **Evidence and assessor finding:** source, provenance, currency, limitations and inference scope. Research approval is not evidence of an operational release gate, an executed test or consumer experience.

A valid IPCH13 claim is restricted to the testability/versioning maturity of the assessed Product/Version. It cannot independently certify compliance, source data quality, semantic validity, safe outcomes or Product-family qualification merely because a set of tests passed.

## 5. Applicability and N/A rules

The characteristic is presumptively relevant to an **independently eligible** Information Product/Version wherever consumer promises may evolve, including batch, interactive, near-real-time, regulatory and internally consumed analytical Products. Static or rarely changed Products still need defensible Product identity and controls over prospective changes; low change frequency alone does not establish `NOT_APPLICABLE` or `MET`.

Legacy Products may have meaningful existing Product version histories but insufficient automated testing; assess the proven condition without retrospectively inventing test executions. A first release may lack a substantive prior version for regression comparison, but still requires relevant baseline tests and prospective version/change-control commitments. How to assess first-release compatibility and limited history is a research boundary, not a blanket maturity waiver.

`NOT_ASSESSABLE` follows when independent Product/Version eligibility fails or is not established. `NOT_APPLICABLE` requires competent D02 case-specific authorization; this guide grants **no general exception**. `EVIDENCE_LIMITED` is an independent uncertainty qualification when evidence is absent, ambiguous, out of date or mismatched—do not treat lack of evidence automatically as proof the underlying control does not exist. Conversely, never infer test execution from the existence of an approved test design, a CI configuration or an unverified passing badge.

## 6. Distinctness and non-duplication

| Characteristic or authority | Independent claim to preserve |
|---|---|
| IPCH02 Deployable | Product deployment and evolution capability versus evidence of versioned tests protecting consumer guarantees. |
| IPCH03 Declarative | Stated governed Product intent versus actual executable contract protection of that intent. |
| IPCH05 Self-Describing | Publication of meaningful Product/Version descriptions versus tested adherence to those descriptions. |
| IPCH06 Trustworthy | Evidence-backed Product trust versus mechanisms and executions validating change; neither characteristic automatically proves the other. |
| IPCH08 SLA–SLO Backed & Observable | Runtime observations/commitments versus version-gated testing and regression protection; telemetry may supply admissible evidence for both without circularity. |
| IPCH09 Compliant by Design | Actual competent policy controls versus test coverage and results for applicable obligations; test passage does not confer policy authority. |
| IPCH10 Addressable | Reachable consumption ports versus compatibility tests and version-controlled change to their contracts. |
| IPCH11 Semantically Aligned | Authoritatively grounded semantic meaning versus tests detecting deviation from it; a test cannot establish ontology authority. |
| IPCH12 Consumption-Driven Intent | Consumer-directed Product constitution/evolution versus validation of versioned changes against that purpose. |
| IPCH16 Interoperable & Composable | Actual compositional ability versus regression protections of versioned composition interfaces. |
| BPS/PIN / Product-family / Compound | Productness and family qualification remain independent eligibility decisions. |
| GEARA/GEARM; DPP; INFOPROD/INFOPDS; PFI/HDIP | Independent semantic, descriptor, Product definition and realization competences are not appropriated by testing guidance. |

An artifact may support more than one *distinct* claim if its contents genuinely do so, but a maturity score, Product catalogue entry, CI badge, deployed API, approved DPP design or model evaluation does not automatically entail `MET` for IPCH13.

## 7. Core mandatory positive criteria — `MET`

`TAV-M01–TAV-M08` are the **D33-approved mandatory conjunctive criteria**. Every criterion must be adequately evidenced for a `MET` determination. No criterion has an independent numerical score or compensatory weight.

| ID | Mandatory criterion | Required assertion |
|---|---|---|
| **TAV-M01** | **Explicit Governed Product Version Identity** | The assessed Product has identifiable, meaningful versions and attributable change history, distinct from component/realization revisions. |
| **TAV-M02** | **Product-Bound Testable Contracts** | Material informational, semantic, structural, quality, consumption and applicable policy expectations are expressed as testable Product-level assertions. |
| **TAV-M03** | **Automated Reproducible Product-Level Tests** | Governed tests actually execute automatically and reproducibly against identifiable Product versions and appropriate inputs, conditions and criteria. |
| **TAV-M04** | **Informational and Analytical Behaviour Validation** | Executed tests verify material measures, derivations, analytical assumptions, informational invariants and consumer-facing outcomes, not merely technical operation. |
| **TAV-M05** | **Regression and Compatibility Protection** | Product evolution is evaluated against applicable prior guarantees, with material inadvertent regressions detectable. |
| **TAV-M06** | **Governed Validation and Promotion Gates** | Material consumer-facing version promotion is conditioned on appropriately evidenced validation and a competent governed disposition. |
| **TAV-M07** | **Consumer-Protective Version Evolution** | Breaking/nonbreaking changes are identified, managed and communicated with appropriate migration, coexistence or compatibility controls. |
| **TAV-M08** | **Versioned Test and Evolution Evidence Integrity** | The evidence binds Product/Version, test identity/version/execution, conditions, expected/actual results, dependencies, realization and promotion determination with current provenance. |

### How to interpret the eight conjunctions

**TAV-M01:** A version must be meaningful in the Product's consumer and governance context. A pipeline release hash can be traceable evidence for realization, but does not by itself establish a Product Version. **TAV-M02:** testable assertions should be as close as practicable to approved Product obligations; technically precise assertions that omit material consumer meaning do not suffice. **TAV-M03:** an automation *design* is not an automated *execution*; identifiable test oracles and controlled conditions matter.

**TAV-M04:** analytical test coverage must be adequate to material information risks, not just transport schema. **TAV-M05:** compare applicable prior guarantees; do not assume every previous Product state must remain simultaneously available. **TAV-M06:** distinguish a gate specification from evidence that a real promotion was governed. **TAV-M07:** not every breaking change is forbidden, but consumers cannot be left unaware of material changes. **TAV-M08:** tested definition, executing realization, runtime occurrence and observed result must be correctly related, not conflated.

The exact boundary for schema-only `PARTIAL` (`TAV-R02`) and unreproducible-tests `PARTIAL` (`TAV-R03`) is deliberately unresolved; neither source case creates an automatic exemption from these mandatory claims.

## 8. Core negative criteria — `NOT_MET`

These are approved **counter-evidence conditions**, not a rule that every missing document automatically proves failure.

| ID | Negative condition |
|---|---|
| **TAV-N01** | Only technical code, pipeline, table, model, infrastructure or deployment revisions exist; meaningful Product/Version identity is absent. |
| **TAV-N02** | Tests validate only technical execution/components, never consumer-facing informational behaviour. |
| **TAV-N03** | Material semantic, analytical, quality or contract changes occur without explicit Product-version governance. |
| **TAV-N04** | Material validation is exclusively manual, ad hoc, unreproducible by design or dependent on undocumented producer knowledge. |
| **TAV-N05** | Test executions cannot be related to the correct assessed Product/Version or test definition. |
| **TAV-N06** | Consumer-facing versions can be promoted despite missing required validation or competent disposition. |
| **TAV-N07** | Consumers experience breaking changes without applicable notice, compatibility handling or controlled transition. |
| **TAV-N08** | Material semantic/analytical consumer-facing obligations are excluded from test coverage while full conformance is asserted. |
| **TAV-N09** | Regression, change, test or promotion records are stale, contradictory, incomplete or misattributed so that evolution cannot be reliably reconstructed. |

**Source-grounded adversarial distinction:** A source-provided `Partial` case should not be reclassified to `NOT_MET` solely for being an imperfect implementation of one requirement. Equally, a demonstrated foundational absence cannot be labelled `PARTIAL` merely because a technical testing activity exists. Assess severity, source tension and independent evidence under D02, leaving `TAV-R02/R03` open.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Scenario | First-Pass handling | Key reservation |
|---|---|---|
| Meaningful Product versions, automated schema tests, semantics untested | Candidate `PARTIAL` per DPCH13 | `TAV-R02` OPEN: material semantic absence may be foundational in some conditions. |
| Product tests exist but results cannot be reproduced consistently | Candidate `PARTIAL` per AIPCH14 | `TAV-R03` OPEN: no automatic treatment for a materially unsafe or inoperable test mechanism. |
| Model/pipeline versioned but Product lacks Product/Version | `NOT_MET` where demonstrated | Technical versioning does not qualify the Product as versioned. |
| No automated Product-level validation; only manual producer coordination | `NOT_MET` where demonstrated | DPCH13 expressly treats manual substitute as insufficient. |
| Entire Product versioned, automated appropriate tests executed, promotion controlled and consumer safety evidenced | Candidate `MET` | All eight mandatory criteria still require sufficient evidence. |
| Versioned Product, no regression comparison with applicable prior commitments | Candidate `NOT_MET` or `PARTIAL` depending on foundation | Degree of coverage and actual protected obligations must be assessed. |
| Product first release, no prior version exists | Evidence-specific, no general exemption | Baseline testing still required; meaning of historical regression depends on applicability. |
| Controlled infrastructure revision with unchanged consumer Promise | Not automatically `NOT_MET` | Product-Version versus realization versioning under `TAV-R01`. |
| Time-varying source population makes raw outputs differ | Cannot infer test failure from non-identity | Reproducibility conditions under `TAV-R05`. |
| Test suite design approved under E0, never run | No claim of exercised assurance; `EVIDENCE_LIMITED` or demonstrated deficiency as supported | Do not convert design acceptance into execution proof. |
| Breaking change appropriately versioned, authorized and migrated | Potentially conformant | Competent consumer-protection obligations apply. |
| Consumer-facing semantic drift occurs without any declaration | `NOT_MET` when adequately evidenced | Material Product change is uncontrolled. |

`PARTIAL` is not the arithmetic average of passed criteria. It means demonstrable real compliance with material elements while non-foundational deficiencies remain; unresolved foundational boundaries are explicit in `TAV-R02/R03`. `EVIDENCE_LIMITED` addresses what can be known, rather than lowering the applicable maturity bar. D02 must establish the assessment subject before any score.

## 10. Evidence signals and sufficiency

The D33-approved evidence set is a set of **claims to substantiate**, not a mandatory file-format prescription.

| ID | Criterion | Minimum evidence claim |
|---|---|---|
| **TAV-ES01** | TAV-M01 | Authoritative Product version identifiers, change classifications and history with Product attribution. |
| **TAV-ES02** | TAV-M02 | Product-bound testable consumer-facing contracts, informational assertions and applicable constraints. |
| **TAV-ES03** | TAV-M03 | Automated test specification/version plus *executed* results with input and environmental context supporting reproducibility. |
| **TAV-ES04** | TAV-M04 | Executed semantic/analytical/informational behaviour tests and attributable outcomes. |
| **TAV-ES05** | TAV-M05 | Regression and compatibility comparison against material earlier Product guarantees. |
| **TAV-ES06** | TAV-M06 | Promotion gate definition, actual validation results and competent release/exception disposition. |
| **TAV-ES07** | TAV-M07 | Change classifications, consumer-facing version contracts, relevant notices, coexistence or migration evidence. |
| **TAV-ES08** | TAV-M08 | Product/Version, semantic definition, test-suite revision, test-execution event, dependency, realization, compilation, runtime occurrence and provenance/currentness links. |

**Authoritative versus supporting evidence:** a competent Product version register and Product-level test result ledger, when available and verified, provide direct support. Changelogs, platform CI badges, repository tags, component release notes, dashboards or engineer testimony can support investigation but are insufficient on their own if the Product binding or executed assurance remains unproven. Conflicting sources trigger an evidence limitation and a request for competent reconciliation, not a guessed answer.

**Representative evidence graph (illustrative, not a required technology):**

`Product/Version → Promise/Contracts → TestSuiteRevision → TestExecution → Result → GateDisposition`

A separate relationship associates `TestExecution → InputFixture/Snapshot → SemanticDefinitionRevision → RealizationRevision → DependencyVersions → RuntimeContext`; consumer notices and migration paths associate with version-change determinations. Each edge needs an attributable, context-valid evidence claim before use in scoring. The existence of source-system lineage or CI provenance alone does not prove the Product's semantic contracts were tested.

**Operational observation caution:** a passing test result can become stale following a dependency or Product-contract revision. Post-publication monitoring may show degradation even though earlier validation passed. Trigger re-evaluation at material changes; the precise frequency, risk thresholds and source of authority belong to applicable governance and open research (`TAV-R04–R07`).

## 11. Agent-assisted or human assessment decision rule

A human assessor or advisory AI agent should apply this **non-executing assessment process**:

1. **Establish eligibility:** identify the exact independent Product/Version and confirmed Information Product-family qualification. If not established, use `NOT_ASSESSABLE`; do not infer qualification from a maturity assessment.
2. **Capture authoritative Promise:** identify applicable Product intent, consumer contracts, semantic definitions, quality/policy constraints and effective dates without independently rewriting their meaning.
3. **Validate version identity:** distinguish the Product version register from code commits, model versions, realization revisions, compilation identities and runtime occurrences (`TAV-M01`).
4. **Map testable assertions:** identify what material informational and consumer-facing commitments actually need validation; check claim-specific contracts (`TAV-M02`, `TAV-M04`).
5. **Inspect execution evidence:** trace test definitions, relevant inputs, environments, actual executions/results and reproducibility to the assessed Product/Version (`TAV-M03`, `TAV-M08`).
6. **Inspect evolution safety:** examine regression checks, backward-compatibility decisions, gate evidence, consumer communication and competent promotion outcomes (`TAV-M05–M07`).
7. **Evaluate counter-evidence:** review `TAV-N01–N09`. Separate demonstrated foundational failure from gaps in available evidence and from source-described non-foundational partial cases.
8. **Record open research effects:** retain `TAV-R01–R08`, especially schema-only and unreproducible-test `PARTIAL` tensions. Do not introduce silent scoring exceptions or a new mandatory versioning technology.
9. **Issue bounded finding:** `MET`, `PARTIAL` or `NOT_MET` only where evidence supports it, with independent evidence limitations, subject/version/effective date, cited source claims and unresolved dissent. Do not perform release, policy or semantic governance decisions.

**Illustrative decision pseudocode, not an adopted decision engine:**

```text
if independent_Product_Version_eligibility_not_established:
    return NOT_ASSESSABLE
if competent_case_specific_not_applicable_decision_exists:
    return NOT_APPLICABLE
inspect source_bound evidence for TAV-M01..M08 and TAV-N01..N09
if foundational_absence_is_demonstrated:
    candidate = NOT_MET
elif all_eight_mandatory_criteria_adequately_evidenced:
    candidate = MET
elif genuine_product_level_versioned_testability_demonstrated
     and deficiencies_are_demonstrably_non_foundational:
    candidate = PARTIAL
else:
    candidate = UNDETERMINED_WITH_EVIDENCE_LIMITED
preserve open TAV-R01/R02/R03 source tensions, authority and timestamps
return bounded_human_review_finding(candidate)
```

The pseudocode is deliberately **not executable governance logic**. It gives no new category permission beyond D02 and does not compel an empirical assessment under E0.

## 12. PMDD scoring treatment

D03 assigns an experimental characteristic-level value only *after* a supported D02 qualitative maturity finding:

| Finding | Characteristic score | Interpretation |
|---|---:|---|
| `MET` | **1.0** | All eight conjunctive mandatory criteria adequately evidenced. |
| `PARTIAL` | **0.5** | Genuine versioned testing present, with demonstrated non-foundational deficiencies, subject to open source boundaries. |
| `NOT_MET` | **0.0** | Foundational protection demonstrably absent or ineffectual. |
| `EVIDENCE_LIMITED` | **No numeric score by itself** | Separate qualifier for admissibility, attribution or currentness uncertainty. |
| `NOT_APPLICABLE` | **No automatic numeric score** | Requires competent case-specific D02 disposition. |
| `NOT_ASSESSABLE` | **No maturity score** | Independent Product/Version eligibility lacking. |

A system must **not** compute a maturity result as `(number of TAV-M criteria satisfied)/8`; neither missing assertion nor failed assertion can be compensated by passing a different criterion. No new threshold, maturity cap, IPCH L0/L1/L2 maturity bands, aggregate PMDD release or evidence override is authorized. If evidence does not support a defensible qualitative finding, record evidence limits rather than fabricate a scalar.

## 13. Critical assurance and governance boundaries

- **BPS/PIN generic Productness and Information-family/Compound authority:** qualification is independent and must precede maturity scoring. A Product with excellent test automation does not qualify merely by being well engineered.
- **INFOPROD/INFOPDS/DPP boundaries:** declaration, qualification, Product specification, descriptor and deployment or realization records remain distinct. No new normative descriptor fields are imposed by this guide.
- **GEARA/GEARM semantic competence:** test oracles must reference competent semantic definitions; a passing test does not independently approve a measure, local deviation or ontology amendment.
- **Policies and legal/compliance requirements:** automated checking is an assessment technique, not independent authority to define, override, waive or assert satisfaction of obligations.
- **PFI/HDIP and platform engines:** CI/CD, compilation, release, data quality and monitoring capabilities may supply realization/evidence where independently established. A platform design does not establish operational availability or historical executions.
- **Human owner accountability:** the human owner approves this experimental guide, future changes, and research dispositions within verified competence. An AI collaborator may draft, check references and challenge evidence but cannot confer institutional authorization.
- **Version/occurrence integrity:** do not silently merge Product/Version, semantic-definition revision, test-suite revision, test execution, dependency revision, output contract, realization, compilation or runtime occurrence into one opaque “release” identifier.
- **S04/Track B and E0/E1/E2 restrictions:** First-Pass analysis is E0 research. Neither governance status nor approval of any research design proves an implementation, certification, release or external execution.

Any purported authoritative exception, Product release or normative adoption requires its own competent decision outside this document. `TAV-R01–R08` remain *open research*, not defects the drafting assistant can close.

## 14. Reassessment and evolution triggers

Reassessment should be considered when materially relevant evidence changes, including:

- A governed Product Version is proposed, published, retired, rolled back or made available to a different consumer population.
- A consumer-facing schema, semantic definition, analytical derivation, measure threshold, population inclusion rule or information-quality promise changes.
- A realization or dependency revision can materially change analytical behaviour while an existing Product Version label remains in use.
- A test suite, oracle, fixture, expected-result definition, automated execution context or validation gate changes materially.
- Reproducibility, test execution attribution or regression comparison becomes uncertain or invalid.
- A breaking change, compatibility decision, consumer notice or migration plan is introduced, challenged or found ineffective.
- An observed production issue, semantic drift, data quality failure or consumer complaint challenges earlier test results.
- Competent authorities resolve one of `TAV-R01–R08`, amend D02/D03 or change the source characterization.

Triggers are **guidance for evidence currency**, not an authorized enterprise testing schedule or an automatic deployment/rollback engine. The future validated assessment must record which Product/Version and effective time the evidence addresses.

## 15. Adversarial and boundary cases — First-Pass fixtures

`TAV-A01–TAV-A12` are **proposed E0 conceptual case designs only**, not executed tests, replay results or empirically scored Products.

| ID | Case | Expected challenge to the rule | Execution |
|---|---|---|---|
| **TAV-A01** | Pipeline and code are versioned; Product Version absent. | Component versioning cannot establish `TAV-M01`. | UNEXECUTED |
| **TAV-A02** | Product Version is declared; only SQL-success tests exist. | Technical execution does not demonstrate informational contract validation. | UNEXECUTED |
| **TAV-A03** | Schema tests execute; material semantics remain untested. | DPCH13 `Partial` versus foundational semantic protection; `TAV-R02`. | UNEXECUTED |
| **TAV-A04** | Tests exist but outcomes cannot be reliably reproduced. | AIPCH14 `Partial` versus reproducibility requirement; `TAV-R03`. | UNEXECUTED |
| **TAV-A05** | Full Product-bound informational tests and governed version promotion. | Candidate `MET` must still demonstrate all eight and current evidence. | UNEXECUTED |
| **TAV-A06** | Analytical measure meaning changes silently. | Semantic breakage without Product version governance. | UNEXECUTED |
| **TAV-A07** | Implementation revision changes, Promise unchanged; regression evidence available. | Separate realization version from Product Version; `TAV-R01`. | UNEXECUTED |
| **TAV-A08** | Upstream dependency revision causes informational drift with unchanged Product code. | Product-level regression and dependency provenance. | UNEXECUTED |
| **TAV-A09** | Breaking change is explicitly versioned with governed coexistence/migration. | Consumer protection does not require banning all breaking change. | UNEXECUTED |
| **TAV-A10** | Producers coordinate compatibility entirely manually. | DPCH13 negative source case; automated self-service protection absent. | UNEXECUTED |
| **TAV-A11** | Product promotion occurs despite failed material validation. | Actual gate enforcement versus claimed gate definition. | UNEXECUTED |
| **TAV-A12** | Tests report success but cannot identify the Product/Version consumers received. | Evidence attribution and currentness for `TAV-M08`. | UNEXECUTED |

For any future competent adversarial assessment, capture independently: scenario version; Product/Version eligibility; source and test inputs; assertion and expected outcome; actual evidence (not merely hypothetical); D02 candidate result; limitations; dissent; competent human disposition; and effects on open research questions. Do not retroactively label these fixtures `PASSED` or `FAILED` from descriptive prose alone.

## 16. Source provenance, open questions and status

### Approved First-Pass source and criteria record

- **Owner authorization:** `INFOPS-0.1-IPCH-P01-D33-F01 = APPROVED_EXPERIMENTAL_E0`, F01.1–F01.16; approved the IPCH13 baseline and separate draft preparation. `INFOPS-0.1-IPCH-P01-D34-F01 = APPROVED_EXPERIMENTAL_E0` accepts this experimental guide as `DRAFT_PREPARED_ACCEPTED` only.
- **Direct sources:** `DPCH.zip/pages/DPCH-PMDD-guidance/13-DPCH13.md` (Data Product) and `AIPCH.zip/AIPCH-PMDD-guidance/14-AIPCH14.md` (AI Product).
- **Authority qualification:** external adjacent Product, semantic, policy, test, deployment and release authorities have not been independently verified by this guide.
- **Approved assessment registers:** `TAV-M01–TAV-M08` (mandatory conjunctive), `TAV-N01–TAV-N09` (negative), `TAV-ES01–TAV-ES08` (claim-specific evidence), `TAV-A01–TAV-A12` (conceptual unexecuted), and `TAV-R01–TAV-R08` (all OPEN).

### Open research register

| ID | Unresolved question | First-Pass status |
|---|---|---|
| **TAV-R01** | Which changes require a new Product Version versus semantic-definition, realization, compilation, dependency or runtime-occurrence versioning, while respecting AIPCH14's full versioned-state language? | OPEN |
| **TAV-R02** | How is DPCH13 schema-only testing `PARTIAL` reconciled with mandatory semantic consumer-contract protection, particularly when omitted semantics are material? | OPEN |
| **TAV-R03** | How is AIPCH14 unreproducible-tests `PARTIAL` reconciled with required reproducibility, and when is the deficiency foundational? | OPEN |
| **TAV-R04** | What is adequate risk- and Promise-specific test coverage for informational meaning, analytical assumptions, semantic mappings, quality, consumer contracts and applicable policy without universal test prescriptions? | OPEN |
| **TAV-R05** | How is reproducibility evidenced for time-sensitive inputs, evolving populations, nondeterministic processes or externally governed dependencies? | OPEN |
| **TAV-R06** | How are Product/Version, semantic-definition, test suite/execution, output-port contract, dependency, realization, compilation and runtime occurrence correctly linked? | OPEN |
| **TAV-R07** | What governed treatment of breaking changes, consumer migration, rollback/coexistence, exceptional promotion and communication is sufficient without prescribing one release model? | OPEN |
| **TAV-R08** | How does IPCH13 evidence interact with qualification, IPCH06/08/09/11/12 and independent governance without circular maturity conclusions? | OPEN |

**No research question has been resolved and no adversarial case executed.** Preserved parent programme safeguards include: D01–D34 approved as applicable; IPCH01–IPCH12 outstanding obligations and D05 historical order; First Pass active and Second Pass not started; original Track B B01 `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`; prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` and historical C06 `APPROVED_NOT_EFFECTIVE` with F01.6/F01.29; historical ledgers `65 / 6 / 7 / 7` and independent PC ledger unchanged; Q0–Q5 and F06/F14/F16 unresolved; 62 approved G06 E0 designs **unexecuted**, E1/E2 executions **0/0**; G06-RO01–RO12 and G03-R01–R12 **all OPEN**.

### This document's controlled status

| Activity | State |
|---|---|
| D33 criteria baseline | `APPROVED_EXPERIMENTAL_E0` |
| `IPCH13.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` — D34, not finally approved |
| D34 owner draft-acceptance disposition | `APPROVED_EXPERIMENTAL_E0` — draft acceptance only |
| IPCH13 Docusaurus overlay | `PREPARED_VERIFIED` — documentation package, not deployed |
| Repository deployment | `NOT_DEPLOYED` |
| Product-level automated tests performed by this research | `NONE` |
| Adversarial replays / empirical product scoring | `NOT_EXECUTED` |
| Second Pass / IPCH14 | `NOT_STARTED` / `NOT_INITIATED` |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |

**Final guide-status statement:** `IPCH13.md / FIRST-PASS-DRAFT-01 = DRAFT_PREPARED_ACCEPTED` under D34. This incremental documentation overlay is `PREPARED_VERIFIED`, not deployed. Neither acceptance nor packaging constitutes operational Product tests, Product maturity findings, promotion-gate execution, Second Pass, final guide approval, normative release or initiation of IPCH14.
