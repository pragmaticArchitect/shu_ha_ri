# IPCH11 — Semantically Aligned: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH11-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Source lineage:** `DPCH11` (Data Product) / `AIPCH12` (AI Product), interpreted separately  
> **Authority:** `INFOPS-0.1-IPCH-P01-D29-F01 = APPROVED_EXPERIMENTAL_E0` (criteria baseline and authorization to prepare draft only)  
> **Guide status:** `DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `INFOPS-0.1-IPCH-P01-D30-F01 = APPROVED_EXPERIMENTAL_E0`  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This sixteen-section document is **experimental assessment guidance**. It is not an authoritative enterprise ontology, a binding semantic conformity certification, a valid Information Product qualification, an executed assessment, or an approved normative standard. D29 approved the First-Pass *criteria baseline*; D30 accepted this experimental draft, not a final normative guide. Overlay preparation is separate from deployment, empirical validation, Second-Pass adversarial tests, or initiation of IPCH12. The accountable human owner remains the sole decision maker within established authority. The original D05 sequence remains historically preserved; this guide follows the owner-directed First-Pass numerical progression.

## 1. Characteristic identity and source lineage

| Field | Experimental First-Pass value |
|---|---|
| Characteristic | `IPCH11 — Semantically Aligned` |
| Guide | `IPCH11-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01` |
| Assessment subject | An independently eligible Information Product/Version and its governed informational Promise, semantic dependencies and interpretations within a defined assessment interval |
| Principal source lineage | `DPCH11 — Semantically Aligned` / `AIPCH12 — Semantically Aligned` |
| Owner-approved baseline | `INFOPS-0.1-IPCH-P01-D29-F01`, F01.1–F01.16 |
| Mandatory conjunctive criteria | `SEM-M01–SEM-M08` |
| Negative conditions | `SEM-N01–SEM-N09` |
| Evidence requirements | `SEM-ES01–SEM-ES08` |
| Second-Pass research | `SEM-R01–SEM-R08 = OPEN` |
| Adversarial cases | `SEM-A01–SEM-A12 = PROPOSED_E0_UNEXECUTED` |
| D02 assessment | `MET`, `PARTIAL`, `NOT_MET`, independent `EVIDENCE_LIMITED`, competent `NOT_APPLICABLE`, and eligibility-dependent `NOT_ASSESSABLE` |
| D03 scoring | Characteristic-level `MET=1`, `PARTIAL=0.5`, `NOT_MET=0`; no averaging of criteria, caps or IPCH L0/L1/L2 bands |

**Exact principal sources re-inspected for this draft:** `DPCH.zip → pages/DPCH-PMDD-guidance/11-DPCH11.md` and `AIPCH.zip → AIPCH-PMDD-guidance/12-AIPCH12.md` (also available as `dpch11_source.md` and `aipch12_source.md`). These are source guidance, not evidence of independently verified adjacent ontologies, registries, Product records, or competent governance decisions.

**DPCH11 — directly supported source assertions.** Shared *meaning*, not similar column names, is essential. Core concepts map to canonical enterprise/domain definitions; semantics are explicit and machine-referenceable; and combinations across Products do not require semantic guesswork, manual spreadsheets or tribal explanation. Governed, versioned evolution and clearly communicated breaking semantic changes are important. Its stated edge cases distinguish: shared vocabulary available but unused (`Not met`); partial alignment with declared local extensions (`Partial`); and full alignment **or explicit, versioned deviation** (`Met`). The last two require careful treatment rather than invented equivalence rules.

**AIPCH12 — directly supported source assertions.** Input, output and *behavioural* meaning must align explicitly with shared enterprise/domain concepts, including machine-interpretable mappings, governed evolution and consistent interpretation across consumers. Technical model outputs or schema similarity do not by themselves define business meaning. Its examples identify an ontology existing but not applied (`Not met`), consistent schema with no ontology mapping (`Partial`), mapped inputs/outputs (`Met`), and unversioned semantic change (`Not met`). The schema-only `Partial` example creates tension with the source's strong foundational alignment rule; preserve as an unresolved source distinction.

**Bounded Information Product specialization.** The derived guidance extends semantic analysis to informational measures, analytical context, assumptions, derived assertions and interpretation of outcomes. It does not import an AI Product's model dependency as an Information Product requirement. Product-family qualification and semantic authority must remain independently determined.

## 2. What the characteristic really asserts

> **IPCH11 — Semantically Aligned:** An Information Product is Semantically Aligned when the business concepts, source-context dependencies, informational measures, analytical interpretations and consumer-facing outcomes that define its informational Promise are explicitly anchored to authoritative shared enterprise or domain vocabularies and conceptual semantic definitions; those relationships, including any competent-governance-approved deviations or extensions, are machine-referenceable, governed through semantic evolution, and sufficient to support consistent interpretation and safe interoperability across independent consumers and Products.

This is the D29-approved **experimental First-Pass definition**, not a new normative vocabulary rule. Semantic alignment means *shared conceptual meaning*, not matching column labels, API schemas, standardized JSON structures or similar dashboard text. A Product whose `available_liquidity` measure has a locally defined horizon, exclusions, counterparty scope or currency convention cannot be assumed semantically equivalent to another Product with the same label. Explicit mapping must convey which concepts actually agree and which legitimately differ.

The Information Product must expose the meaning of its **informational Promise**, including material derivations and scope, rather than relying only upon upstream semantic alignment. A coherent mapping at the source Data Product level does not guarantee that a derived liquidity, utilization, risk or trend measure has a governed interpretation. Conversely, different physical encodings may faithfully represent the same meaning; equivalent labels and representations are not the definition of equivalence.

The Product Owner can be accountable for providing correct declarations and evidence but does not acquire authority to define enterprise ontology terms, approve equivalence or waive an existing semantic determination. That remains with competent GEARA/GEARM and related governance. A declaration of deviation is not automatically sufficient for `MET` (`SEM-R02`, `SEM-R04 = OPEN`).

## 3. Information Product specialization

Information Products may combine sourced facts with **interpretive context**: calculated metrics, time windows, cohort definitions, classification boundaries, normative reporting conventions, units, hypotheses and presentation logic. The assessment therefore examines semantic continuity through (a) referenced source terms, (b) governed derivation, (c) the resulting informational claim, and (d) output interpretations offered to intended consumers.

**Illustrative case — Available Liquidity (not an assessment):** Product A might calculate ledger funds after account restrictions at a cut-off, while Product B might include eligible funding facilities over the following day. They could publish an output field with the same name but carry different semantic assertions. An independent consumer must be able to distinguish them using their authoritative concept references, effective periods, calculation semantics and declared limitations. The reverse possibility also exists: query, API and file representations may legitimately expose the *same* governed meaning.

**AI source analogy without category appropriation.** AIPCH12 insists that an AI output such as a fraud score must state what it means in business terms, not merely its technical model type. For an Information Product, the analogous concern is that a reported result, indicator or analytical classification states what information it conveys and how to interpret it. This does not change the Product's family to AI or require any model dependency.

**Semantic implementation neutrality.** A competent shared vocabulary may be published through an ontology, enterprise/domain conceptual model, semantic descriptor or another governed machine-referenceable representation. RDF, OWL, SKOS, JSON-LD, a particular catalogue or reasoning engine is not a new universal condition. A Product metadata link or DPP may support evidence only where it genuinely references competent semantic definitions; a link is not proof of correct mapping, mapping execution or interoperability.

**Intentional semantic deviation.** A local extension may be valid in a domain if competent governance permits it and semantic differences are explicit, version-aware and independently interpretable. DPCH11 describes some explicit, versioned deviations as `Met`, while partial aligned local extensions may be `Partial`. D29 preserves both source statements without declaring a general exception to the eight conjunctive criteria. The exact conditions remain open.

## 4. Assessment subject and authority

Establish the following *separate* subjects before a maturity finding:

1. **Assessed Product/Version:** independent BPS/PIN generic Productness, Information-family qualification and D02 eligibility have not been established by this guide. An ineligible or unverified assessment subject is `NOT_ASSESSABLE`, not an inferred negative maturity score.
2. **Informational Promise:** authorized scope, intended consumer outcomes, material measures, interpretations, assumptions and permitted uses. Its constitutive semantics are not invented by an assessor.
3. **Authoritative semantic sources:** competent enterprise/domain vocabularies, semantic concepts, identifiers, decisions, effective definition/version, relevant extensions and approved deviations. Their authority and lifecycle must be independently verified in a real assessment.
4. **Semantic mapping records:** map source concepts, transformations, measures, outputs, meaning-bearing parameters, effective times and interpretation into the shared concepts. Mapping revision is not the same thing as a semantic-definition version.
5. **Consumption representations:** the effective output-port contract versions, interfaces and consumer-visible representations in scope; a port/version can change while Product/Version or semantics remain stable, or vice versa.
6. **Realization context:** realization revision, compilation and runtime occurrence may be evidence contexts but are not automatically the semantic authority or Product identity.
7. **Evidence and determinations:** every evidence item has provenance, supported claim, timing and limitation; an assessor's D02 finding is a determination distinct from the underlying events.

GEARA/GEARM remain the competent analytical and semantic authority. Product-family and Compound qualification, INFOPROD/INFOPDS, BPS/PIN, DPP, PFI/HDIP, policy/legal and assurance authority remain independently governed. A `MET` IPCH11 finding neither creates a Product nor redefines an enterprise term.

## 5. Applicability and N/A rules

The characteristic applies to an eligible Information Product/Version whose informational meaning is intended for independent, reliable interpretation. It is not made optional because a Product is used within one department, because consumers are familiar with its terminology, because output schemas are consistent, or because the source Data Products already refer to ontologies.

Different Information Products have different meaning-bearing constructs: a narrative report has assertions, reporting context and interpretive qualifications; a statistical measure has populations, aggregation, period and units; a periodically supplied management view has named scope, calculation semantics and reporting conventions. A particular form of metric, model or ontology software is not required merely because another Product uses it. Context-specific inapplicable **evidence examples** do not create an exemption from the characteristic.

`NOT_APPLICABLE` as a whole-characteristic outcome requires a specific competent D02 exception; none is granted by D29. `NOT_ASSESSABLE` is reserved for an assessment subject without independently established eligibility. Do not conflate ineligibility, lack of available evidence, genuine semantic failure and legitimate nonapplicability.

If evidence is incomplete, stale, conflicting or lacks semantic-version provenance, record `EVIDENCE_LIMITED` independently. A submitted mapping artifact, design, reference or glossary screenshot cannot automatically support `MET`, and absence of a particular artifact format is not itself demonstrable `NOT_MET`.

## 6. Distinctness and non-duplication

| Adjacent characteristic / authority | Distinct claim and boundary |
|---|---|
| IPCH03 — Declarative | Product intent is declared; IPCH11 assesses independently governed shared *meaning* behind that intent. |
| IPCH04 — Discoverable | Semantically finding a Product does not prove that its derived measures and assertions conform to shared meanings. |
| IPCH05 — Self-Describing | A readable description is not identical to authoritative machine-referenceable shared semantic mapping. |
| IPCH06 — Trustworthy | Trust evidence does not independently establish the correctness of semantic alignment. |
| IPCH07 — Reusable | Independent adoption and generalized design are distinct from consistent interpretation. |
| IPCH08 — SLA–SLO Backed & Observable | Monitoring semantic regression differs from establishing correct semantic meaning and evolution. |
| IPCH09 — Compliant by Design | Applying controls to classifications differs from determining competent semantic meaning for those classifications. |
| IPCH10 — Addressable | Product output ports expose information; port existence does not establish the meaning represented. |
| IPCH12 — Consumption-Driven Intent | Consumer informational purpose is distinct from concept/mapping authority and semantic interpretation. |
| IPCH13 — Testable & Versioned | Product testability/versioning differs from authoritative semantic definition and meaning evolution. |
| IPCH16 — Interoperable & Composable | Cross-Product composition may depend on alignment but cannot automatically certify each Product's semantic assertions. |
| BPS/PIN, Information-family / Compound | Product qualification is independent of this characteristic's maturity finding. |
| GEARA/GEARM | Own competent enterprise/domain semantic governance; this guide does not issue ontology/adoption/equivalence decisions. |
| INFOPROD/INFOPDS, DPP, PFI/HDIP | Records or realization mechanisms may evidence meaning; they are not automatically authority or mandatory implementations. |

Prevent circular evidence: an ontology label attached to a Product, a PMDD score, a catalogue search result or an asserted cross-product join cannot alone prove the SEM criteria. Independent semantic conformance and interpretation evidence must match the actual claim under assessment. Conversely, IPCH11 findings must not be used as a proxy for IPCH16 composability or IPCH06 trust assessments.

## 7. Core mandatory positive criteria — `MET`

The D29-approved `SEM-M01–SEM-M08` are **eight mandatory conjunctive** criteria for `MET`, to be evidenced against the exact assessed Product/Version and relevant effective interval. Their order is not a weighting scheme.

| ID | Mandatory criterion | Assessment requirement |
|---|---|---|
| **SEM-M01** | **Authoritative Shared Semantic Anchoring** | Material business and informational concepts of the Product refer to independently governed enterprise or domain semantic definitions, not local words alone. |
| **SEM-M02** | **Explicit Machine-Referenceable Semantic Bindings** | Concepts, measures and outputs have explicit structured relationships to competent authoritative meanings that machine-assisted processes can reference and examine. |
| **SEM-M03** | **Informational Promise and Analytical Meaning Alignment** | Material measures, derivations, assumptions, context and intended interpretations have governed, unambiguous meaning aligned to applicable semantic authority. |
| **SEM-M04** | **Input, Output and Consumer Interpretation Consistency** | Material source inputs, transformation outcomes, output-port representations and declared consumer meanings remain coherent or explicitly distinguished where different. |
| **SEM-M05** | **Governed Semantic Extensions and Deviations** | Semantic extensions and deviations are explicit, justified, version-linked and within competent semantic-governance decisions, rather than unilateral local redefinition. |
| **SEM-M06** | **Semantic Stability and Governed Evolution** | Changes to material meaning, source definition revisions and resulting compatibility effects are identified, version-governed and communicated to affected consumers. |
| **SEM-M07** | **Demonstrable Semantic Interoperability** | Independent consumers or Products can interpret the declared information using authoritative references without undocumented negotiation, guesswork or manual reconciliation. |
| **SEM-M08** | **Product-Level Semantic Evidence Integrity** | Evidence can be attributed to the exact Product/Version, authoritative semantic definition/version, relevant mappings and effective realization, with identified currentness and limitations. |

**Conjunctive rule:** `MET` requires adequate support for every applicable mandatory assertion. Do **not** compute an average of eight criteria, relax the meaning of `SEM-M01` for syntax-only evidence, declare all deviations permissible, or assign `MET` simply because a shared ontology is available. Where sources give transitional `PARTIAL` examples that appear to contradict foundational requirements, preserve those exact tensions under `SEM-R02–R04` for separate owner-governed Second Pass.

## 8. Core negative criteria — `NOT_MET`

These D29-approved negative conditions are counter-evidence to examine, **not** a mechanical rule treating any absence of evidence as failure.

| ID | Negative condition / red flag |
|---|---|
| **SEM-N01** | Material concepts rely on undocumented local meaning, personal knowledge or producer-only explanation. |
| **SEM-N02** | Syntactically consistent names or schemas are presented without authoritative shared semantic mappings. |
| **SEM-N03** | Matching names, identifiers or structure are treated as proof of equivalence despite materially conflicting meanings. |
| **SEM-N04** | Derived measures or analytical conclusions are defined only technically, without the meaning of the result or its important assumptions. |
| **SEM-N05** | Semantic mappings remain informal prose, slides or manual spreadsheets where structured machine-referenceable alignment is required. |
| **SEM-N06** | Product-specific semantic extensions or deviations conflict with competent shared meanings without governed justification or disposition. |
| **SEM-N07** | Material semantic changes occur without explicit version-aware evolution or consumer impact management. |
| **SEM-N08** | Consumers must manually reconcile or negotiate material meaning to interpret or combine the Product's outputs safely. |
| **SEM-N09** | Purported alignment evidence is stale, falsely mapped, associated with another Product/Version or with an unidentified semantic-definition version. |

For a real assessment, distinguish a proven negative condition from an unsupported or uninspected assertion. Structural schema consistency without ontology mapping is expressly `Partial` in an AIPCH12 edge case, yet the same source rejects structure without meaning; this tension remains unresolved (`SEM-R03`). Not all potentially negative indicators therefore imply one automatic D02 finding. Determine the nature and materiality of proven deficiencies and record their rationale.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| D02 finding / qualifier | Interpretation for experimental IPCH11 |
|---|---|
| `MET` | Adequate, current, attributable evidence supports all eight mandatory criteria, including shared authority, actual semantic mapping, interpretability and governed evolution. |
| `PARTIAL` | A genuine shared semantic alignment basis is present but proven non-foundational gaps remain, e.g., limited mapping coverage or transitional local extensions within competent governance. |
| `NOT_MET` | A foundational semantic claim is demonstrably absent: material meanings remain local/implicit, purported equivalent outputs materially disagree, a shared ontology is unused, or consumers require essential undocumented reconciliation. |
| `EVIDENCE_LIMITED` | Evidence is stale, incomplete, conflicting or insufficient to support a defensible finding; the independent qualifier is not automatic `NOT_MET`. |
| `NOT_APPLICABLE` | Only through separately verified competent D02 applicability decision; no general IPCH11 exemption is created. |
| `NOT_ASSESSABLE` | Independent Product/Version eligibility is not established; do not assign a characteristic score. |

**DPCH11 deviation versus extension (unresolved).** The source gives `Partial` to a Product where some shared meanings are aligned and others openly identified as local extensions, and `Met` to full alignment **or explicit, versioned deviation**. The approved guidance requires competent governance and semantic interoperability for `MET`; it does not silently declare all versioned deviations good enough. The original source wording and D29 constraints must coexist pending `SEM-R02` and `SEM-R04`.

**AIPCH12 schema-only case (unresolved).** The source labels consistent schemas without ontology mapping `Partial`, while defining semantic alignment as anchoring meaning in shared conceptual models and expressly describing structural schemas without mapping as negative. The guidance retains the source's `Partial` case as a challenge, not a general permission to score `PARTIAL` solely on naming consistency (`SEM-R03`).

**Additional source examples:** An enterprise ontology exists but is not applied to the Product — `Not met` in both sources. AIPCH12 regards unversioned semantic drift as `Not met`; mapping actual input/output semantics may support `Met` when the other mandatory requirements also hold. Different physical representations of one meaningful concept are not automatically competing semantic definitions.

**Conceptual candidate case:** a Product's underlying Data Products have valid mappings, but its derived risk grouping has no declared threshold interpretation. The upstream alignment does not prove `SEM-M03` or `SEM-M04`; determine actual evidence and materiality without inventing a maturity finding. None of these examples is an executed product assessment.

## 10. Evidence signals and sufficiency

| ID | Criterion | Required evidence claim and illustrative signals |
|---|---|---|
| **SEM-ES01** | SEM-M01 | Competent glossary/ontology terms, authoritative IDs, effective definitions and direct references for all material Product concepts. |
| **SEM-ES02** | SEM-M02 | Structured machine-referenceable mapping records, Product-bound semantic identifiers, verifiable mapping relations and effective revisions. |
| **SEM-ES03** | SEM-M03 | Governed definitions of derived measures, analytical assumptions, units, windows, scope, intended interpretation and their relevant authoritative concept links. |
| **SEM-ES04** | SEM-M04 | Source-to-output transformation semantic trace, output-port meanings, representation equivalence or explicit difference and consumer contract evidence. |
| **SEM-ES05** | SEM-M05 | Competently authorized semantic extensions/deviations, documented rationale, version relationships and impact determinations. |
| **SEM-ES06** | SEM-M06 | Semantic-definition/version history, mapping changes, breaking-change classification, consumer notices and compatibility evidence. |
| **SEM-ES07** | SEM-M07 | Independent consumer interpretation, interoperability checks, safe cross-Product interpretation evidence without undocumented reconciliation. |
| **SEM-ES08** | SEM-M08 | Exact Product/Version, authoritative semantics and version, mapping revision, relevant port-contract version, realization context, effective time and provenance. |

**Authority hierarchy:** authoritative meaning and approval originate in competent GEARA/GEARM or applicable delegated governance, not in an assessor's narrative. Product-bound mapping records and version histories are relevant primary evidence for their claims. Examples, design diagrams, DPP metadata, catalogue descriptions, output screenshots or consumer testimonials may corroborate but do not each prove all eight criteria. A mapping to a superseded or unverified semantic term raises a temporal authority question.

**Minimum conceptual evidence provenance:** evidence ID; source/issuer; explicit claim; assessed Product ID/Version; term or semantic-definition ID/version; mapping ID/revision; affected measure/output and port-contract versions if relevant; effective observation interval; realization and runtime context if applicable; assessment date/assessor; contradictory evidence and limitations. This is a *guidance-level evidence inventory*, not a new mandatory wire schema or DPP contract.

**Sufficiency discipline:** a proposed E0 mapping design is not a verified functioning alignment, an available ontology is not an applied mapping, and an applied mapping is not by itself proof of consistent consumer interpretation. Do not infer `NOT_MET` from incomplete source capture alone; use `EVIDENCE_LIMITED` and specify exactly what is missing. Distinguish SEM-M01–M08 factual evidence from neighboring IPCH05/06/10/16 claims and legal-policy determinations.

## 11. Agent-assisted or human assessment decision rule

**Step 1 — Product eligibility.** Establish competent BPS/PIN Productness, independent Information-family qualification, and exact Product/Version eligibility under D02. If absent, record `NOT_ASSESSABLE` rather than scoring an unqualified subject.

**Step 2 — semantic scope.** Record the Product's informational Promise, material source concepts, derivations, measures, reporting scope, semantic assertions, intended consumers and effective assessment interval. Identify which meanings are material and why.

**Step 3 — authority inspection.** Resolve authoritative enterprise/domain terms, competent ownership and effective semantic-definition versions from the actual governance source. Do not infer authority from matching names, marketplace descriptions or an unverified ontology reference.

**Step 4 — mapping and analytical interpretation.** Inspect structured mappings for sources, derived assertions and consumer outputs. Verify applicable contexts such as periods, populations, aggregations, units, thresholds and intended interpretation; distinguish actual semantic mapping from UI labels or schema names.

**Step 5 — deviation and evolution.** Inspect versioned extension/deviation decisions, competent approvals and consumer-impact governance. Preserve `SEM-R02–R04` rather than inventing a general `MET` exception.

**Step 6 — independent interpretation.** Seek relevant observed, test or governed evidence that independent consumers or other Products can interpret meanings correctly without hidden producer clarification. Do not turn this into IPCH07's reuse count or IPCH16's entire composition qualification.

**Step 7 — evaluate conjunction.** For each `SEM-M01–M08`, identify supporting evidence, relevant `SEM-N01–N09` counterevidence, provenance, currentness, and uncertainty. Do not average the mandatory criteria or use a bare shared ontology as conformance proof.

**Step 8 — record bounded D02 determination.** Apply `MET`, `PARTIAL`, `NOT_MET`, or a separate `EVIDENCE_LIMITED` qualification as actually supported. `NOT_APPLICABLE` needs competent exception; `NOT_ASSESSABLE` requires no score. Record source tensions, open R questions, relevant semantic governance authority, exact Product/Version and evidence times. Keep owner disposition and normative adoption separate.

**Example evidence register (illustrative only, no executed assessment):**

```yaml
assessment_kind: EXPERIMENTAL_IPCH11_EXAMPLE_ONLY
assessment_status: NOT_EXECUTED
product_id: REQUIRES_INDEPENDENT_QUALIFICATION
product_version: REQUIRES_EVIDENCE
informational_promise: REQUIRES_COMPETENT_DEFINITION
semantic_definition_ids_and_versions: NOT_ASSUMED
mapping_ids_and_revisions: NOT_ASSUMED
port_contract_versions: NOT_ASSUMED
realization_revision: NOT_ASSUMED
criteria: SEM-M01-SEM-M08
criteria_logic: CONJUNCTIVE_FOR_MET
counterevidence: SEM-N01-SEM-N09
evidence: NOT_COLLECTED
maturity_finding: NOT_ASSESSED
research_obligations: SEM-R01-SEM-R08_OPEN
adversarial_validation: UNEXECUTED
normative_effect: NONE
```

## 12. PMDD scoring treatment

For a D02-eligible Product/Version with an adequately supported characteristic-level maturity finding, preserve D03's experimental mapping:

| Finding | Characteristic-level score |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |

The value is assigned to the **overall characteristic finding**, not calculated by awarding one-eighth of a point per mandatory criterion, counting mapped ontology concepts, or proportionately scoring the number of outputs with mapped semantics. Conjunctive criteria remain conjunctive for `MET`. There are no newly adopted automatic caps or IPCH L0/L1/L2 bands.

`EVIDENCE_LIMITED` is a separate evidence-uncertainty qualifier, not a fourth numerical maturity score. `NOT_ASSESSABLE` reflects unestablished eligibility. A whole-characteristic `NOT_APPLICABLE` finding requires independent competent D02 authority and cannot be presumed for local Products, narrative information or otherwise non-technical consumption. Missing evidence should not automatically create a numeric zero; this remains distinct from proven foundational semantic misalignment.

**Example scoring caution:** a Product with correctly mapped source entities but unresolved derived-measure meaning cannot be scored `MET` by counting six of eight satisfactory sections. The actual characteristic finding depends on foundationality, materiality, competent semantic determinations and sufficient evidence, with unresolved borderlines retained for Second Pass. No real Product is assessed here.

## 13. Critical assurance and governance boundaries

- **Competent semantic authority:** GEARA/GEARM govern shared enterprise/domain concepts and semantic determinations. IPCH11 guidance does not authorize Product Owners or AI assessors to redefine, approve or declare equivalence for shared terms.
- **Productness and family:** BPS/PIN generic qualification, Information Product-family status, Compound Product treatment and independent Product/version authority are preconditions or neighboring determinations, not outputs of `SEM-M01–M08`.
- **Semantic artifacts:** INFOPROD/INFOPDS, semantic descriptors and DPP may record or reference authoritative meaning; no mandatory ontology technology or unapproved new DPP conformance requirement is introduced.
- **Authority integrity:** Do not conflate a Product/Version, semantic-definition/version, mapping revision, port-contract version, realization revision, compilation, runtime occurrence, evidence item and assessor determination.
- **Separate legal and policy authority:** Semantic meaning may be relevant to controls, but lawful use, restrictions, assurance and consequential decisions are governed independently; semantic maturity is not legal approval.
- **No circular qualification:** IPCH05 Self-Describing, IPCH06 Trustworthy, IPCH08 Observable, IPCH10 Addressable, IPCH13 Versioned and IPCH16 Composable cannot merely certify one another without their own independently sufficient evidence.
- **Human-led E0 governance:** The guide is AI-assisted research text. Only competent humans can approve later drafts, perform institutional authority decisions, authorize repository changes or adopt normative rules.

Potential business examples such as liquidity definitions are illustrative, not claims that any named enterprise ontology or Product already exists. All source discrepancies and interpretation limits must remain inspectable rather than being quietly normalized.

## 14. Reassessment and evolution triggers

Reassessment should be considered when a material change affects the semantic claims or their evidence, including:

1. New Product Version or changed informational Promise, measure, context, population, interpretation or derived assertion.
2. Revision, deprecation, split or replacement of an authoritative enterprise/domain concept or semantic definition.
3. New, amended or withdrawn mapping, extension, local deviation or competent semantic governance decision.
4. Changed input Data Product meanings, effective time semantics or derivation logic affecting output interpretation.
5. New output port or contract version, alternative representation or consumer group introducing material interpretation differences.
6. Realization changes capable of altering aggregation, rounding, units, time-window boundaries or semantic fidelity.
7. Observed consumer ambiguity, cross-Product mismatch, contradictory interpretation or meaningful semantic regression.
8. Evidence becoming stale, unverifiable or misattributed to the wrong Product/Version or semantic-definition version.

Reassessment does not automatically change maturity or Product qualification. It must produce a new bounded evaluation against the actual current authority and evidence. A semantic-definition change is not automatically a Product Version change; determine the applicable relationships under their own authority. Do not infer that monitoring a semantic signal (IPCH08) proves semantic conformance (IPCH11).

## 15. Adversarial and boundary cases — First-Pass fixtures

All cases below are **proposed experimental test fixtures, not executed empirical findings**. The challenge names and IDs are D29-approved; the assessment prompts are intended for later competent Second Pass.

| ID | Proposed adversarial challenge | Question for a later evidence-based replay |
|---|---|---|
| **SEM-A01** | Enterprise ontology exists but is not applied to the Product | Does source existence get incorrectly counted as applied Product mapping? |
| **SEM-A02** | Consistent field schemas and names but no shared semantic mapping | Can the AIPCH12 `Partial` example be reconciled without redefining foundational alignment? |
| **SEM-A03** | Core concepts aligned with declared but incompletely mapped local extensions | Which deficiencies are non-foundational versus potentially disqualifying? |
| **SEM-A04** | Explicit versioned deviation without competent governance approval | Is an unapproved deviation accidentally classified `MET`? |
| **SEM-A05** | Competently governed deviation with unambiguous independent interpretation | What is the legitimate path to `MET` under DPCH11's exception? |
| **SEM-A06** | Source Data Products aligned; derived informational measure ambiguous | Does the assessment independently examine the informational Promise? |
| **SEM-A07** | Different output-port representations preserve the same meaning | Can format variance be distinguished from semantic inconsistency? |
| **SEM-A08** | Identical metric name masks materially different definitions | Are name and schema similarities incorrectly treated as equivalence? |
| **SEM-A09** | Material meaning change with no version/consumer-impact governance | Does the assessor detect ungoverned drift? |
| **SEM-A10** | Valid structured mappings point to an obsolete ontology revision | Can authority and evidence currentness be correctly attributed? |
| **SEM-A11** | Independent consumers must reconcile meaning manually | Does consumer independence fail notwithstanding descriptive documentation? |
| **SEM-A12** | E0 semantic design is portrayed as executed conformance evidence | Is design/operation evidence integrity preserved? |

`SEM-A01–SEM-A12 = PROPOSED_E0_UNEXECUTED`. No simulated pass/fail conclusions are recorded as historical evidence; tests require separate authorization, materials and owner review. The original source examples remain research inputs, not automatic determinations for real Products.

## 16. Source provenance, open questions and status

### Source lineage and bounded interpretation

**Principal directly inspected files:** `DPCH.zip → pages/DPCH-PMDD-guidance/11-DPCH11.md`; `AIPCH.zip → AIPCH-PMDD-guidance/12-AIPCH12.md`. DPCH11's explicit versioned-deviation `Met` and local-extension `Partial` cases, and AIPCH12's schema-only `Partial` versus foundational ontology-alignment assertions, are intentionally preserved as source tensions. An Info-specific analytical-meaning extension is the D29-approved experimental interpretation, not a claim to have amended either source. No adjacent repository, semantic authority, policy registry or Product-specific evidence is independently verified by inspection of these source files alone.

### Second-Pass research register — all OPEN

| ID | Open research question |
|---|---|
| **SEM-R01** | What constitutes sufficient authoritative semantic anchoring for informational measures, interpretations and analytical assertions beyond aligned source entities/attributes? |
| **SEM-R02** | When may an explicit, versioned semantic deviation support `MET`, and what competent approval and interoperability evidence are needed? |
| **SEM-R03** | How should AIPCH12's schema-without-ontology `Partial` case be reconciled with its foundational shared-semantic assertion? |
| **SEM-R04** | What makes a Product-specific semantic extension legitimate without granting local actors enterprise ontology authority? |
| **SEM-R05** | How should Product/Version, semantic-definition version, mapping revision, output-port contract and realization revision be separately attributed in evidence? |
| **SEM-R06** | What evidence establishes independent interpretation and interoperability without prescribing an ontology language, registry or reasoning engine? |
| **SEM-R07** | How is material meaning preserved or qualified across derived measures, transformations, analytical assumptions and output representations? |
| **SEM-R08** | How should IPCH11 interact with IPCH05/06/08/10/13/16 without circular assessment or duplicated semantic governance? |

`SEM-R01–SEM-R08 = OPEN_SECOND_PASS`; `SEM-A01–SEM-A12 = PROPOSED_E0_UNEXECUTED`.

### Programme status and next authorization

| Programme or artifact element | Current bounded status |
|---|---|
| `INFOPS-0.1-IPCH-P01-D29-F01` | `APPROVED_EXPERIMENTAL_E0`; clauses F01.1–F01.16 approved |
| `INFOPS-0.1-IPCH-P01-D30-F01` | `APPROVED_EXPERIMENTAL_E0`; sixteen-section experimental guide accepted only |
| `IPCH11.md / FIRST-PASS-DRAFT-01` | `DRAFT_PREPARED_ACCEPTED` under D30 |
| IPCH11 First-Pass baseline | `APPROVED`; no empirical semantic assessment |
| IPCH11 overlay / Docusaurus deployment | `PREPARED_VERIFIED` / `NOT_DEPLOYED` |
| IPCH11 adversarial tests / Second Pass | `UNEXECUTED` / `NOT_STARTED` |
| IPCH11 final guidance / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| IPCH01–IPCH10 | Previous experimental baseline/draft approvals and outstanding reviews preserved |
| IPCH12–IPCH16 | `NOT_INITIATED` |
| Parent Track B B01 | Completion `NOT_ESTABLISHED`; B02–B06 `NOT_AUTHORIZED` |
| Effective prospective S04 | `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` |
| Historical C06 | `APPROVED_NOT_EFFECTIVE`; F01.6/F01.29 safeguards retained |
| Historical approval ledgers | `65 / 6 / 7 / 7`; separate PC ledger unchanged |
| Q0–Q5; F06/F14/F16 | `UNRESOLVED` |
| G06 E0 designs | 62 approved, `UNEXECUTED`; E1/E2 execution `0 / 0` |
| G06-RO01–RO12 and G03-R01–R12 | All 24 `OPEN` |
| Independent authorities | BPS/PIN, GEARA/GEARM, Product-family/Compound, INFOPROD/INFOPDS, DPP, PFI/HDIP, policy, legal, assurance and consequential actions preserved |

**Current permitted stage:** D30 owner acceptance is recorded; an incremental experimental Docusaurus overlay has been prepared and verified, but no live build or deployment is established. No semantic conformance, Second-Pass assessment, IPCH12 initiation, or normative adoption is authorized.
