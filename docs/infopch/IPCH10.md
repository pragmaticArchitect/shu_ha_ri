# IPCH10 — Addressable: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH10-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Source lineage:** `DPCH10` (Data Product) / `AIPCH11` (AI Product), separately interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D27-F01 = APPROVED_EXPERIMENTAL_E0` (baseline and guide-preparation authorization only)  
> **Guide status:** `DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `INFOPS-0.1-IPCH-P01-D28-F01 = APPROVED_EXPERIMENTAL_E0`  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This sixteen-section guidance is an experimental **draft assessment aid**, not a declaration of Productness, Product conformance, deployed port architecture or actual consumer adoption. The owner approved the **First-Pass criteria baseline** in D27 and accepted this sixteen-section experimental draft in D28. Neither decision establishes repository deployment, empirical validation, final guide approval or normative adoption. The accountable human owner alone makes research dispositions within verified competence; the AI drafter does not assume independent institutional, semantic, policy or legal authority. The original D05 sequence remains historically preserved; this First-Pass work follows the owner-directed numerical order.

## 1. Characteristic identity and source lineage

| Field | Experimental First-Pass value |
|---|---|
| Characteristic | `IPCH10 — Addressable` |
| Guide | `IPCH10-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01` |
| Assessment subject | One independently eligible Information Product/Version and the corresponding governed informational capability, declared consumer contexts, Product output ports, contracts, applicable policy boundaries and assessment interval |
| Principal sources | `DPCH10 — Addressable` / `AIPCH11 — Addressable` |
| Owner-approved baseline | `INFOPS-0.1-IPCH-P01-D27-F01`, F01.1–F01.16 |
| Mandatory conjunctive criteria | `ADR-M01–ADR-M08` |
| Negative criteria | `ADR-N01–ADR-N09` |
| Evidence requirements | `ADR-ES01–ADR-ES08` |
| Research | `ADR-R01–ADR-R08 = OPEN` |
| Adversarial cases | `ADR-A01–ADR-A12 = PROPOSED_E0_UNEXECUTED` |
| D02 findings | `MET`, `PARTIAL`, `NOT_MET`; independent `EVIDENCE_LIMITED`; competent `NOT_APPLICABLE`; `NOT_ASSESSABLE` for ineligible subject |
| D03 characteristic scoring | `MET=1`, `PARTIAL=0.5`, `NOT_MET=0`; no criterion averaging, automatic caps or IPCH L0/L1/L2 bands |

**Directly inspected principal sources:** `DPCH.zip → pages/DPCH-PMDD-guidance/10-DPCH10.md` and `AIPCH.zip → AIPCH-PMDD-guidance/11-AIPCH11.md`. The two files anchor the characteristic derivation; their inspection is not a claim to have independently verified adjacent BPS/PIN, GEARA/GEARM, DPP, INFOPROD/INFOPDS or policy authorities.

**DPCH10 source assertion:** A Data Product is consumed through explicit, documented, governed **output ports** (e.g., APIs, SQL/query, streams or files) appropriate to different consumers. Dashboards and other visual experiences consume those ports and are **not** the Product. Its simplified failure condition is inability to consume independently of a specific UI/tool. DPCH10 explicitly labels **UI plus APIs behind it** as `Partial` (potentially transitional), **multiple clear governed ports** as `Met` and **ungoverned bypass APIs** as `Not met`. It rejects requiring all consumers to use a modality unsuited to their needs.

**AIPCH11 source assertion:** An AI Product exposes explicit, stable, governed **capability-level** ports independent of application/UI. Ports represent the qualified Product capability rather than model internals, pipelines or intermediate steps. Contract stability, policy access, monitoring, trust and reuse/composition are important source connections. Its edge cases distinguish **UI-only access** (`Not met`), **undocumented unstable API** (`Partial`) and **stable governed API** (`Met`). These are source examples, not automatic Information-family maturity determinations.

**Bounded interpretation:** IPCH10 translates those principles to an Information Product's authoritative **informational Promise**, not to raw data access or an AI model's exposed internals. It does not prescribe universal REST, SQL, event or other mandatory modality counts. The unresolved internal-API/product-port and single-port suitability questions remain open (`ADR-R01–ADR-R03`).

## 2. What the characteristic really asserts

> **IPCH10 — Addressable:** An Information Product is Addressable when its governed informational capability is independently accessible through explicit, stable, documented and policy-controlled Product-level output ports, whose contracts express the Product's informational Promise, provide consumption mechanisms appropriate to its declared consumers and remain decoupled from specific applications, experience interfaces and internal implementations.

A Product may expose several valid ports, each serving a distinct consumption pattern, without becoming several Products by virtue of interface plurality. Conversely, an attractive UI with an internal HTTP endpoint does not automatically create a Product-grade output port. Addressability is a **governed access boundary for the Product capability**. Mere technical reachability is insufficient.

Three separations are necessary:

1. **Product capability:** The independently qualified informational Promise and meaning, such as a consolidated liquidity view and its governed reporting context.
2. **Product output ports:** First-class, identifiable, stable and governed mechanisms for obtaining that capability, e.g., a semantically qualified query port, data delivery API, stream or file interface appropriate to declared use.
3. **Consumer experiences:** Dashboards, applications, notebooks, assistants or agents which consume those Product ports. They do not substitute for ports or uniquely own the Product's essential informational meaning.

A port's **contract** must disclose the relevant meaning and conditions of consumption, not merely transport-level method names. Operational evidence must correspond to the assessed Product/Version and effective port-contract version. Proper independent access is compatible with governed gateways and intermediaries if the Product's port remains a distinct authoritative boundary; the limits of that interpretation are retained in `ADR-R06`.

## 3. Information Product specialization

An Information Product might supply a time-bounded analytical report, decision-support measure, consolidated management view, narrative or other governed informational result. Its addressability should represent **that information**—the defined measures, effective intervals, coverage, semantic qualifications, relevant parameters and usage constraints—rather than demand that consumers reimplement joins, calculations or semantic interpretation from constituent Data Products. Information can be delivered by a report/file port, API, query service, subscription, event or other suitable mechanism. No particular method is a universal maturity prerequisite.

**Illustrative example (not an actual assessed Product):** a consolidated corporate liquidity Information Product promises a named liquidity position by legal entity and effective cut-off. An analyst may use a query port, an application may call a governed API, and another consumer may subscribe to events. A dashboard can use the same qualified Product capability, but cannot be the only authoritative access mechanism if independent Product addressability is claimed. The consumer should not have to obtain raw bank-account movements and reconstruct the promised consolidated measure independently.

**Port plurality versus suitability:** A single stable, governed, capability-level output port can be adequate for a genuinely narrow declared consumer population. Requiring an API plus query plus event port regardless of actual need would be an invented criterion. Conversely, a Product declared for fundamentally different consumption profiles cannot satisfy suitability solely by forcing every consumer to reverse-engineer an unsuitable interface. Preserve `ADR-R02` for the hard cases.

**Capability abstraction:** A port can expose legitimately parameterized informational results and metadata, not simply internal intermediate transformations. It can describe optional parameters and different representation formats so long as the semantic Promise and usage contract are preserved. Qualified information may include explanatory context and provenance required to consume it correctly, subject to competent semantics and Product definition authority. Do not conflate interface-form choices with independent Product-family qualification.

## 4. Assessment subject and authority

Before evaluating any ADR criterion, distinguish and record:

1. **Eligible Product/Version.** BPS/PIN generic Productness, independent Information-family qualification and D02 assessment eligibility must already have been established by competent mechanisms. An ineligible/unverified subject yields `NOT_ASSESSABLE`, not an invented maturity score.
2. **Informational Promise and semantic definition/version.** Identify the exact capability that is promised, its context, scope, effective time, permissible parameters and authoritative semantic source. IPCH10 cannot independently redefine that Promise.
3. **Product output-port identities.** List authoritative ports, identities/addresses, modalities, documented intended consumers and whether each is first-class in the Product contract.
4. **Port contract identity/version.** Record relevant requests/inputs, outputs, semantics, stability, compatibility/transition rules, entitlements and availability claims; distinguish the port contract from Product Version.
5. **Consumer contexts and experiences.** Identify declared consumer archetypes, whether any experience is mandatory, and whether consumers can obtain the qualified Product capability independently of a particular application/dashboard.
6. **Policy and access decisions.** Determine which competent policies apply to each port and where enforcement occurs; do not substitute the addressability assessment for IPCH09 legal/policy conformance.
7. **Realization and occurrence.** Identify applicable gateway, deployment, technical realization revision and observed invocation/evidence interval. Do not equate a transport endpoint or telemetry record with Product-level maturity.
8. **Evidence and decision identity.** Separate source evidence, observation, limitation, assessor interpretation, owner disposition, compilation identity and any later repository/release effect.

The assessor may identify technical indicators but cannot grant entitlement, revise enterprise semantics, declare legal compliance, authorize Product qualification or promote an experiment to normative status. All such authorities remain separately governed.

## 5. Applicability and N/A rules

**Default:** IPCH10 is applicable to every D02-eligible Information Product that claims a consumable informational capability. Human-focused, batch, periodic, highly specialized, restricted, regulated or internally consumed Products are not automatically exempt.

- A report delivered on a scheduled basis can be addressable through a governed file/object or similar qualified output port; interactive REST is not compulsory.
- An authorized access restriction is not itself a failure of addressability, provided there is a governed independent Product port and its contract/entitlement constraints are correctly represented. Do not interpret access denial as evidence that no port exists.
- A single consumer group or single modality does not automatically invalidate the characteristic. Inspect actual declared contexts and suitability, not arbitrary port count.
- A UI may be present and useful; the essential capability must not be trapped within it. An embedded UI backend is not automatically a Product port merely because network calls occur.
- A port design, API specification or catalogue entry without sufficient realization/consumption evidence cannot be treated as proven operational addressability.
- A specific modality may legitimately be inapplicable, but this is **not** whole-characteristic `NOT_APPLICABLE`.
- Whole-characteristic `NOT_APPLICABLE` requires an affirmative competent D02 determination; no generic exception is created. Ineligible Product/Version => `NOT_ASSESSABLE`.

## 6. Distinctness and non-duplication

| Neighbour / authority | Distinct IPCH10 assertion |
|---|---|
| IPCH02 — Deployable | Deploying a Product via self-service does not prove independently consumable Product output ports. |
| IPCH03 — Declarative | Describing a Product is not the same as offering stable operating output contracts. |
| IPCH04 — Discoverable | Finding a Product/port in a marketplace is not proof the capability is independently accessible. |
| IPCH05 — Self-Describing | Published information/usage description is not sufficient Product-port existence, stability or access evidence. |
| IPCH06 — Trustworthy | Trust/evidence posture is distinct from the governed consumption boundary. |
| IPCH07 — Reusable | Port availability does not establish observed adoption by multiple independent consumer contexts. |
| IPCH08 — SLA–SLO Backed & Observable | Observed service behaviour and PMDD maturity are different from the port boundary itself. |
| IPCH09 — Compliant by Design | Competent substantive policy enforcement is distinct from identifying where governed port access occurs. |
| IPCH11 — Semantically Aligned | Semantic authority determines meaning; IPCH10 verifies that port contracts faithfully express an already governed Promise. |
| IPCH13 — Testable & Versioned | Product and testing discipline differ from the specific stability/lifecycle of declared output-port contracts. |
| IPCH16 — Interoperable & Composable | Addressable Product ports do not independently prove interoperability/composition. |
| BPS/PIN and Product-family qualification | Generic Productness and Information-family classification precede IPCH10 and are not recreated by it. |
| GEARA/GEARM | Analytical/semantic authority remains independent of technical interface descriptions. |
| INFOPROD/INFOPDS and DPP | Governed Product/descriptor or evidence carriers may reference ports; their existence is not proof of actual access or conformance. |
| PFI/HDIP realization and policy/legal/assurance | Technical realization and runtime enforcement have separately competent authorities. |

Evidence may be referenced between characteristics when the *particular fact* is demonstrably common, but one characteristic's score or authority cannot be inherited wholesale. Product/Version, semantic-definition version, output-port contract version, realization revision, compilation and runtime occurrence must remain independently traceable.

## 7. Core mandatory positive criteria — `MET`

**All eight mandatory criteria must be adequately evidenced for `MET`.** They are conjunctive. No criterion-level averaging, weights, automatic caps or maturity bands are approved.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **ADR-M01** | **Explicit Product Output Port Definition** | The Information Product declares identifiable, first-class output ports through which its informational capability is consumed. |
| **ADR-M02** | **Stable Documented Consumption Contracts** | Every applicable port has a documented, governed, version-associated contract identifying access, relevant inputs/parameters, delivered outputs, semantics and usage conditions. |
| **ADR-M03** | **Capability-Level Semantic Encapsulation** | Ports expose the governed Information Product capability without obliging consumers to reconstruct it from internal Data Products, tables, processing stages or implementation details. |
| **ADR-M04** | **Experience and Application Independence** | The capability can be independently accessed without dependence on a particular dashboard, UI, embedded application or proprietary consumer experience. |
| **ADR-M05** | **Consumer-Appropriate Port Modalities** | Available ports fit the Product's declared consumer contexts, without unsuitable access patterns or bespoke per-consumer reconstruction. No universal port count is required. |
| **ADR-M06** | **Governed Policy-Enforced Port Access** | Applicable access, information-handling and usage controls are effectively enforced across relevant Product-port consumption paths. |
| **ADR-M07** | **Product and Contract Lifecycle Stability** | Port identifiers and contract evolution are governed so internal implementation changes do not cause uncontrolled breaking changes for consumers. |
| **ADR-M08** | **Product-Level Addressability Evidence Integrity** | Evidence correctly identifies the assessed Product/Version, declared ports, effective contracts, accessible mechanisms and related governance outcomes without conflating UI or internal component evidence. |

**Interpretation:** `ADR-M01` is not proven by a backend API alone; `ADR-M02` is not proven by a prose URL or screenshots alone; `ADR-M03` is not proven by a raw database endpoint; `ADR-M04` is not proven by a screen that internally invokes endpoints; `ADR-M05` is not a mechanical demand for three technical protocols; `ADR-M06` does not substitute for a competent IPCH09 policy-conformance determination; `ADR-M07` does not forbid governed breaking changes; and `ADR-M08` cannot be satisfied by irrelevant transport-level usage traffic.

**Conjunctive MET test:** Each of `ADR-M01`, `ADR-M02`, `ADR-M03`, `ADR-M04`, `ADR-M05`, `ADR-M06`, `ADR-M07` and `ADR-M08` must have relevant sufficient current evidence for the same assessed Product/Version and appropriate effective scope. Do not infer a maturity score by simply counting passing rows.

## 8. Core negative criteria — `NOT_MET`

The following are **counter-evidence conditions**. Their demonstrated presence may indicate a foundational failure or a significant deficiency; missing data alone must not be silently treated as demonstrated failure. Apply D02 evidence rules and the unresolved source edge-case boundaries.

| ID | Negative or warning condition |
|---|---|
| **ADR-N01** | Product informational capability is accessible only through one UI, dashboard or embedded application. |
| **ADR-N02** | An API/endpoint exists but is not declared, documented or supported as a first-class Product output port. |
| **ADR-N03** | Consumers must reconstruct the Information Product from underlying Data Products, raw tables, pipeline steps or implementation state. |
| **ADR-N04** | Port contracts are unstable, undocumented or subject to ungoverned breaking changes. |
| **ADR-N05** | Access depends on reverse-engineering, informal requests or ad hoc credentials instead of documented governed consumption. |
| **ADR-N06** | A materially unsuitable single modality is imposed despite established differing consumer requirements. |
| **ADR-N07** | Relevant Product-port access bypasses applicable policies, entitlements or usage controls. |
| **ADR-N08** | Essential Product capability logic is trapped inside an experience interface, defeating replacement or independent consumption. |
| **ADR-N09** | Purported addressability is evidenced only by underlying component calls, UI screenshots, catalogue labels or unattributed traffic rather than governed Product/Version ports. |

A source example can be `PARTIAL` even while a negative indicator is present—e.g., DPCH10's UI with internal APIs—where some authentic Product access capability exists but is incomplete. AIPCH11's UI-only case is `NOT_MET`. The detailed distinction is not fully settled in First Pass (`ADR-R01`, `ADR-R03`).

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Candidate finding | D02-governed interpretation |
|---|---|
| `MET` | All eight criteria adequately evidenced for the assessed Product/Version and relevant scope/interval. |
| `PARTIAL` | Genuine Product-level addressability is evidenced, with bounded **non-foundational** deficiencies such as unstable documentation, limited contract governance or an incomplete transition to first-class ports; material assessment boundaries remain explicit. |
| `NOT_MET` | A foundational requirement is demonstrably absent: UI-only access, no independent Product port, forced consumer reconstruction of the Product, or material bypass of required governed Product-port controls. |
| `EVIDENCE_LIMITED` | Evidence is incomplete, stale, disputed, contradictory or inapplicable, and a defensible substantive finding cannot be established; independent qualifier, not automatic `NOT_MET`. |
| `NOT_APPLICABLE` | Only if independent competent D02 applicability authority expressly establishes an exception; none is granted generically. |
| `NOT_ASSESSABLE` | Independent D02 Product/Version eligibility is not established. No characteristic score. |

**Source edge-case preservation:** DPCH10 calls “UI exists and APIs exist behind it” `Partial` as transitional; AIPCH11 calls “AI capability accessible only via UI” `Not met` even if internal APIs are present in application architecture. AIPCH11 regards an undocumented unstable but existing API as `Partial`, while its simplified rule stresses explicit stable governed independent ports. These examples must be presented together, not silently reconciled. The eventual classification depends on whether an independently governed capability-level port can actually be demonstrated and the materiality of deficiencies; `ADR-R01` and `ADR-R03` remain OPEN.

**Single-port nuance:** DPCH10 condemns forcing one unsuitable port on diverse consumers; this does **not** imply universal multi-port deployment. For a narrowly defined Product, one appropriate port may suffice if all eight mandatory criteria are established. When declared consumer needs demonstrably differ, suitability must be assessed, not assumed (`ADR-R02 = OPEN`).

**Policy restriction versus unavailability:** Refused access for an unauthorized actor may be correct policy enforcement, not a sign of absent addressability. However, if even authorized intended consumers cannot independently access the Product capability through any governed port, that is material counterevidence. A designed but never accessible endpoint requires evidence qualification, not a speculative operational `MET`.

## 10. Evidence signals and sufficiency

| ID | Linked criterion | Evidence claim and possible signals |
|---|---|---|
| **ADR-ES01** | ADR-M01 | Authoritative Product/Version output-port inventory, first-class port declarations, identities and owners. |
| **ADR-ES02** | ADR-M02 | Current port contracts/specifications describing input, output, meaning, versions, intended consumers and governed usage. |
| **ADR-ES03** | ADR-M03 | Product capability-to-port traceability, representative qualified results and checks that consumers do not reconstruct the Promise from internals. |
| **ADR-ES04** | ADR-M04 | Evidence of authorized independent Product consumption apart from a specific dashboard/app; replaceability or separate client invocation where applicable. |
| **ADR-ES05** | ADR-M05 | Declared consumer contexts, rationale for interface modality, evidence of fit-for-purpose use and absence of necessary bespoke reconstruction. |
| **ADR-ES06** | ADR-M06 | Applicable policy bindings, entitlement checks and actual relevant enforcement/denial outcomes at or governing the Product access boundary. |
| **ADR-ES07** | ADR-M07 | Port-contract change history, version association, compatibility/deprecation governance and relevant consumer-impact records. |
| **ADR-ES08** | ADR-M08 | Exact Product/Version/port/contract attribution, realization-effective interval and distinguishable consumption, policy and assessment evidence. |

**Evidence hierarchy:** First prefer independently authoritative Product/Version and port-contract records, applicable semantic and policy determinations, and directly relevant controlled/observed usage. Supporting telemetry, marketplace metadata, UI screenshots or design diagrams may help corroborate but do not independently prove all eight claims. The presence of an SDK, HTTP endpoint, dashboard or database connection is not automatically sufficient.

**Minimum provenance for each evidence item:** `evidence_id`, issuer/source, claim supported, Product ID/Version, port ID and effective contract version where applicable, semantic reference, technical realization context, observation/effective timestamps, collection method, assessor, evidence limitations and links to competent policy decisions when relevant. Fields are conceptual evidence categories, **not** an imposed wire schema or mandatory new DPP implementation.

**Sufficiency discipline:** A contract definition shows intended behaviour; operating evidence demonstrates applicable real accessibility; tests demonstrate particular observations; an entitlement statement does not prove every realized path is enforced. Do not import the result of IPCH09, IPCH07 or IPCH16 as proof of IPCH10. When evidence is missing, record the precise gap and `EVIDENCE_LIMITED` rather than converting uncertainty to `NOT_MET`.

## 11. Agent-assisted or human assessment decision rule

**Step 1 — establish assessment eligibility.** Resolve BPS/PIN generic Productness and independent Information Product-family qualification references as required by D02. If the Product/Version is ineligible or unestablished, record `NOT_ASSESSABLE` and stop.

**Step 2 — identify Product Promise.** Record competent Product/Version and semantic-definition references, declared consumer contexts and intended informational outcomes. Do not use an application's features to invent the Product capability.

**Step 3 — inventory purported ports.** For every asserted port, examine whether it is **first-class, declared and Product-owned/governed** or instead an internal API, intermediate query, raw table, UI control or gateway implementation detail. Preserve evidence for ambiguous classifications (`ADR-R01`).

**Step 4 — establish contracts and boundary.** Identify input/output semantics, documented effective versions, policies, stability, consumer-facing purposes and whether the Product Promise can be obtained through the port without bespoke reconstruction.

**Step 5 — test independent authorized consumption.** Seek relevant evidence that an intended authorized consumer can use the Product port independently of a particular experience interface. Do not count a backend call as sufficient solely because it is visible in browser tools; do not require real use by multiple independent contexts, as that concerns IPCH07.

**Step 6 — assess suitability, governance and evolution.** Compare the modal access with declared consumer needs; review applicable policy enforcement and contract-change governance. Do not imply a mandatory count of ports or take over IPCH09 substantive legal-policy judgments.

**Step 7 — evaluate all eight conjunctive claims.** Record `ADR-M01–M08` evidence with separate positive, negative and uncertainty assessments. Never average mandatory criteria; identify foundational versus non-foundational failures with explicit reasoning and source tensions.

**Step 8 — report only defensible result.** Produce D02 qualitative finding, separate evidence limitation, D03 characteristic-level value **only when legitimately determinate**, exact Product/Version/port/effective time, open questions and competent reviewer. Owner disposition and downstream deployment remain separate events.

**Example evaluation record (illustrative, not executed):**

```yaml
assessment_kind: EXPERIMENTAL_IPCH10_EXAMPLE
product_id: SUBJECT_TO_INDEPENDENT_QUALIFICATION
product_version: SUBJECT_TO_EVIDENCE
semantic_definition_version: NOT_ASSUMED
port_contract_versions: SUBJECT_TO_EVIDENCE
realization_revision: SUBJECT_TO_EVIDENCE
criteria: ADR-M01-ADR-M08
criteria_logic: CONJUNCTIVE_FOR_MET
negative_checks: ADR-N01-ADR-N09
evidence_items: NOT_COLLECTED
maturity_finding: NOT_ASSESSED
evidence_limitation: NOT_EVALUATED
adversarial_validation: UNEXECUTED
normative_effect: NONE
```

## 12. PMDD scoring treatment

For an independently eligible Information Product/Version with an adequately supported qualitative finding, D03 characteristic-level treatment remains:

| Maturity finding | Experimental score |
|---|---:|
| `MET` | `1` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0` |

`EVIDENCE_LIMITED` remains independent evidence metadata/qualification rather than a fourth score; `NOT_APPLICABLE` requires competent determination; `NOT_ASSESSABLE` cannot be scored as an eligible Product. The existing experimental equal-characteristic-weight rule is preserved; no criterion weighting, arithmetic combination of `ADR-M01–M08`, automatic cap or IPCH L0/L1/L2 bands is introduced.

**Conjunctivity versus partial maturity:** All eight claims must be sufficiently evidenced for `MET`. This does not automatically define the exact `PARTIAL`/`NOT_MET` outcome every time one mandatory criterion fails. A demonstrated foundational absence is different from a real but limited first-class port with documented non-foundational deficiencies. The unresolved source transition scenarios must be escalated for Second-Pass replay rather than resolved by a newly invented numeric threshold.

**No empirical scoring has occurred:** The guide describes how an authorized assessor may reason. It does not score a real Product, conduct external interface tests, publish a maturity evaluation, or execute a monitoring or governance service.

## 13. Critical assurance and governance boundaries

1. **Productness and family authority are independent.** A technically accessible endpoint cannot itself qualify an Information Product. Preserve BPS/PIN and independently competent Product-family and Compound governance.
2. **Semantics remain independently governed.** An output-port contract referencing liquidity, risk, coverage, reconciliation or other informational meaning does not establish that the semantics are correct. Preserve GEARA/GEARM and Product-definition authority.
3. **DPP is not compulsory.** A DPP may be an applicable governed evidence carrier, but its presence is not a new mandatory IPCH10 implementation/conformance requirement. A listed output port must still be supported by its contract and relevant evidence.
4. **Policy enforcement remains competent.** `ADR-M06` evaluates whether port access is actually governed; it does not decide legal applicability, grant entitlements, waive restrictions or replace IPCH09. A transport security control alone is not proof that all applicable information-usage obligations are satisfied.
5. **Experience independence is not UI prohibition.** A replaceable dashboard may be an entirely legitimate consumer of ports. Its existence is not adverse; sole dependency on it for the Product capability is adverse.
6. **Output-port identity is not runtime occurrence.** Port specification, actual deployment, service instance, gateway route, access event, realization revision and Product Version are distinct. Never collapse them into one 'API' identity.
7. **Reuse and composability remain separate.** One stable API can demonstrate potential addressability, not independent observed multiple-context reuse or cross-Product interoperability.
8. **Owner-led experimental authority remains bounded.** D27 approves criteria and preparation, not final guide adoption. The AI drafts/challenges and maintains traceability but cannot authorize publication, normative conformance or institutional governance changes.

## 14. Reassessment and evolution triggers

Reassess relevant IPCH10 evidence after material changes to:

- the Product/Version, informational Promise, semantic-definition/version or intended consumer contexts;
- the declared output-port inventory, addressing scheme, input/output schema or effective contract version;
- an API gateway, query service, event stream, file delivery or other realization path where independently accessible consumption or contract stability might change;
- application/UI design where essential Product logic migrates into—or out of—the experience layer;
- applicable policy, entitlement, classification or consumption purpose and its actual enforcement path;
- consumer suitability, such as a newly declared machine consumer that cannot reasonably use the existing modality;
- deprecation, backward incompatibility, protocol migration or introduction of a new port;
- evidence currentness, Product-to-port attribution, usage observations or contradictions between specification and effective consumption.

A change **trigger** is not an automatic regression judgment. A new port does not automatically improve maturity; a single-port design does not automatically lower it; and a port change may be governed and fully compatible. Record the affected Product/Version, effective contract identity, observation period, relevant evidence and competent interpretation. Unverified changes should be marked with the correct evidence limitation.

## 15. Adversarial and boundary cases — First-Pass fixtures

All twelve cases are **proposed research fixtures only**; no replay, Product assessment, runtime invocation, conformance testing or empirical finding has taken place.

| ID | Challenge | What must be discriminated / research link |
|---|---|---|
| **ADR-A01** | Dashboard is the sole access mechanism | UI-only application boundary versus first-class Product port; likely foundational failure if proven (`ADR-R03`). |
| **ADR-A02** | Dashboard has internal undocumented APIs | Whether backend endpoints are independently supported Product ports and whether source `PARTIAL` can apply (`ADR-R01`, `ADR-R03`). |
| **ADR-A03** | Product exposes a documented independent API | Real capability-level semantics, governance and stability versus mere endpoint existence. |
| **ADR-A04** | Product has several governed ports suited to different consumers | Contract coherence and suitable plurality without automatically proving reuse or composability. |
| **ADR-A05** | Product has one port that adequately serves declared contexts | Avoid invented universal multimodal requirement (`ADR-R02`). |
| **ADR-A06** | Product has one port unsuitable for materially different declared needs | Distinguish legitimate specialization from forced one-size-fits-all design (`ADR-R02`). |
| **ADR-A07** | Consumers query an underlying Data Product and reconstruct information | Underlying component reachability is not Information Product addressability (`ADR-R04`, `ADR-R08`). |
| **ADR-A08** | Product API exposes intermediate processing or model internals | Capability-level encapsulation versus implementation exposure (`ADR-R04`). |
| **ADR-A09** | Port definitions exist while access bypasses applicable policies | Addressability boundary and separate IPCH09 enforcement evidence (`ADR-R07`). |
| **ADR-A10** | UI is replaceable because it consumes first-class Product ports | Independent Product port vs legitimate optional experience (`ADR-R01`, `ADR-R06`). |
| **ADR-A11** | Internal realization changes break port contracts without governance | Effective contract stability and identity/version lineage (`ADR-R05`). |
| **ADR-A12** | Marketplace advertises Product port that cannot be independently verified/accessed | Discovery versus effective Product addressability and evidence integrity (`ADR-R08`). |

These fixtures do not pre-authorize authoritative decisions or change D02/D03 rules. Their precise expected findings, contrary evidence and replay outcomes require independently authorized Second-Pass work.

## 16. Source provenance, open questions and status

### Source lineage and bounded interpretation

- **DPCH10**, directly inspected: explicit Product-owned output ports, documentation/versioning/governance, fit to consumption needs, independent access from replaceable UI experiences, and the transitional UI-plus-internal-API `Partial` case. It treats bypassing governance as `Not met`.
- **AIPCH11**, directly inspected: stable capability-representing output ports, explicit documented input/output contracts, independence from applications/UI, policy control and stable multi-consumer interfaces. Its UI-only `Not met`, undocumented/unstable API `Partial` and governed stable port `Met` cases are retained without asserting universal Information-family results.
- **INFOPS D27 owner approval:** the Information Product-specialized criteria and register IDs in this document are approved experimental baseline assertions. They do not amend DPCH10/AIPCH11 or automatically authorize Product qualification, implementation or normative release.
- **No evidence of source-wide verification:** adjacent INFOPS, BPS/PIN, GEARA/GEARM, DPP, policy, legal, Product-family and realization sources have not all been independently verified by this IPCH10 authoring activity.

### Second-Pass research register — all OPEN

| ID | Research question | Status |
|---|---|---|
| **ADR-R01** | How precisely can an independently governed Product output port be distinguished from an internal application API or component interface? | OPEN |
| **ADR-R02** | When does a single port genuinely satisfy declared consumer needs, and when is that modality materially unsuitable? | OPEN |
| **ADR-R03** | How does DPCH10's transitional UI-plus-API `PARTIAL` example differ from foundational UI-only `NOT_MET` conditions? | OPEN |
| **ADR-R04** | What evidence demonstrates capability-level semantic abstraction without exposing implementation internals or requiring consumer reconstruction? | OPEN |
| **ADR-R05** | How are Product/Version, semantic-definition version, port-contract version, realization revision and observed occurrence correctly attributed? | OPEN |
| **ADR-R06** | How does independent Product consumption work through enterprise gateways, catalogues, agents and other shared intermediaries? | OPEN |
| **ADR-R07** | What demonstrates policy-enforced port access without usurping IPCH09 or competent substantive policy authority? | OPEN |
| **ADR-R08** | What constitutes genuine Product-level addressability evidence instead of a catalogue entry, UI screenshot, technical traffic or underlying Data Product access? | OPEN |

### Programme status and next authorization

| Item | Preserved status |
|---|---|
| `D01–D28` | `APPROVED_EXPERIMENTAL_E0` |
| IPCH10 guide | `DRAFT_PREPARED_ACCEPTED`; owner D28 disposition `APPROVE` |
| Guide template | D04 sixteen-section structure preserved |
| D05 original characteristic order | Historically preserved; First-Pass numerical progression owner-directed |
| `ADR-M01–ADR-M08` | Approved First-Pass **mandatory conjunctive** criteria |
| `ADR-N01–ADR-N09` / `ADR-ES01–ADR-ES08` | Approved First-Pass negative and evidence registers |
| `ADR-A01–ADR-A12` | `PROPOSED_E0_UNEXECUTED` |
| `ADR-R01–ADR-R08` | ALL `OPEN` |
| IPCH01–IPCH09 | Earlier approved guidance and all outstanding review obligations preserved; IPCH01–IPCH03 experimental deployment confirmed, IPCH04–IPCH09 overlays prepared with deployment confirmation outstanding |
| IPCH11–IPCH16 | `NOT_INITIATED` |
| IPCH10 overlay / deployment | `OVERLAY_PREPARED_VERIFIED` / `NOT_DEPLOYED` |
| Second Pass / empirical assessment | `NOT_STARTED` / `NOT_EXECUTED` |
| Final guide approval / normative release | `NOT_APPROVED` / `NOT_AUTHORIZED` |
| Parent Track B B01 completion | `NOT_ESTABLISHED` |
| Parent B02–B06 | `NOT_AUTHORIZED` |
| Effective prospective S04 | `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)` |
| Historical C06 | `APPROVED_NOT_EFFECTIVE`; safeguards F01.6/F01.29 preserved |
| Historical approval ledgers | `65 / 6 / 7 / 7`; separate PC ledger unchanged |
| Q0–Q5; F06/F14/F16 | UNRESOLVED |
| G06 E0 designs | 62 approved and UNEXECUTED |
| E1/E2 execution | `0 / 0` |
| G06-RO01–RO12 and G03-R01–R12 | All 24 OPEN |

**Owner decision recorded:** `INFOPS-0.1-IPCH-P01-D28-F01 = APPROVED_EXPERIMENTAL_E0`; guide `DRAFT_PREPARED_ACCEPTED`. This incremental Docusaurus overlay is prepared for operator review only, not deployed. No IPCH11 authoring, Second-Pass execution, live repository changes, final guide approval or normative INFOPS release is authorized here.
