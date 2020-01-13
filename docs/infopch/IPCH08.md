# IPCH08 — SLA–SLO Backed & Observable: PMDD Maturity Assessment Guidance

> **INFOPS 0.1 / IPCH-P01 — EXPERIMENTAL FIRST PASS (E0)**  
> **Guide ID:** `IPCH08-PMDD-GUIDE-01`  
> **Revision:** `FIRST-PASS-DRAFT-01`  
> **Source lineage:** `DPCH08` (Data Product) / `AIPCH09` (AI Product), separately interpreted  
> **Authority:** `INFOPS-0.1-IPCH-P01-D23-F01 = APPROVED_EXPERIMENTAL_E0` (baseline and preparation authorization only)  
> **Guide status:** `EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; **owner draft acceptance:** `APPROVED_EXPERIMENTAL_E0` under `INFOPS-0.1-IPCH-P01-D24-F01` (draft acceptance only)  
> **Publication:** `NOT_DEPLOYED`; **Second Pass:** `NOT_STARTED`; **final approval:** `NOT_APPROVED`; **normative release:** `NOT_AUTHORIZED`

This sixteen-section guide is a **proposed, human- and machine-assessable experimental draft**, not evidence of executed monitoring, maturity testing, characteristic conformance or normative approval. The owner remains the accountable decision-maker within verified competence; AI assists with drafting and challenge, not independent governance authority. D23 approved the **criteria baseline**; D24 subsequently accepted this completed guide **as an experimental First-Pass draft only**, not as a final guide or normative release. The earlier dependency-informed D05 order remains historically recorded; the numerical First Pass controls drafting sequence only. All deferred Second-Pass questions and challenges remain open/unexecuted.

## 1. Characteristic identity and source lineage

| Field | First-Pass value |
|---|---|
| Characteristic | `IPCH08 — SLA–SLO Backed & Observable` |
| Assessment subject | One exact Information Product / Version, intended service and informational Promise, applicable runtime/realization context and time interval |
| Principal sources | `DPCH08 — SLA–SLO Backed & Observable` and `AIPCH09 — SLA–SLO Backed & Observable`; family-specific authority remains independent |
| Approved baseline | `INFOPS-0.1-IPCH-P01-D23-F01` F01.1–F01.16 |
| Mandatory / negative criteria | `OBS-M01–OBS-M08` conjunctive / `OBS-N01–OBS-N09` |
| Evidence | `OBS-ES01–OBS-ES08` |
| Challenges | `OBS-A01–OBS-A12 = PROPOSED_E0_UNEXECUTED` |
| Research | `OBS-R01–OBS-R08 = OPEN` |
| Assessment vocabulary | D02 `MET`, `PARTIAL`, `NOT_MET`; independent `EVIDENCE_LIMITED`; affirmative authorized `NOT_APPLICABLE`; `NOT_ASSESSABLE` when ineligible |
| Experimental scoring | D03 characteristic-level `MET=1`, `PARTIAL=0.5`, `NOT_MET=0` only |

**Upstream source distinction.** DPCH08 requires both operational SLA/SLO visibility **and automated, recurring enterprise PMDD maturity testing** (for its Data Product family, DPCH01–DPCH14). AIPCH09 requires explicit, measurable behavioural expectations and continuously measured Product-level real-world performance with actionable deviations and machine-consumable signals; its signals can feed PMDD but its canonical assertion does not independently require full enterprise PMDD characteristic-test execution. IPCH08's D23-approved experimental specialization retains **both dimensions**. It does not transfer DPCH01–14 tests directly into INFOPS or assert that all sixteen IPCH tests already exist.

**Unreconciled edge-case source rules:** DPCH08 calls “SLAs exist, no maturity monitoring” `PARTIAL` in its edge cases yet says `NOT_MET` under a stricter simplified agent rule (`OBS-R02` OPEN). AIPCH09 labels “dashboards but no SLOs” `PARTIAL` in an edge case while its simplified rule requires explicit expectations (`OBS-R03` OPEN). These tensions must not be silently resolved.

## 2. What the characteristic really asserts

> **IPCH08 — SLA–SLO Backed & Observable:** An Information Product is SLA–SLO Backed & Observable when it has explicitly governed and measurable service-level and informational-behaviour expectations, continuously emits and evaluates Product-level evidence of actual performance against those expectations, enables timely detection and action upon material deviations, and participates in automated enterprise-level PMDD monitoring that establishes and trends its continuing productization maturity.

The evidence must be attributable to the assessed Product/Version, accessible through suitable governed mechanisms, and appropriately aligned to its informational constitution and operating risk.

The claim has **two independent, non-substitutable components**: (A) operational and informational runtime observation against SLAs/SLOs, and (B) automatically recurring enterprise PMDD **productization maturity** evaluations and historical regression detection. Pipeline dashboards alone do not establish either component fully. Scheduled PMDD snapshots alone cannot replace monitoring of material runtime failures. SLO definitions alone do not prove actual monitoring. Approved experimental criteria and unexecuted designs are not evaluation results.

“Continuous” requires adequate ongoing observation and evaluation for the signal's material deviation window, **not** identical real-time sampling for every batch, report, event, analytic or recurring PMDD test. A weekly PMDD evaluation may be appropriate for maturity trends but not a substitute for an Information Product's faster operational breach detection.

## 3. Information Product specialization

Evaluate observability relative to the Product's **informational Promise** and its legitimate consumption contexts, not only hosting infrastructure. Possible relevant dimensions, subject to Product constitution and applicability, include: availability and access success; freshness, source effective time and reporting cut-off; informational completeness, consistency and reconciliation; derived-measure/analytical-output degradation; semantic-definition or dependency changes; usage/consumption failures; and applicable policy-related monitoring signals from competent sources.

For example, a consolidated-liquidity Information Product can return a successful API response while using an incomplete source population, stale reporting period or invalid aggregation. CPU health is not sufficient for its informational SLO. Conversely, a periodic Information Product may have a scheduled delivery SLO rather than a universal millisecond response target. Instrumentation should measure appropriate **end-to-end Product outcomes**.

The Information Product's actual monitored performance is distinct from the correctness of its semantic definitions (GEARM), approved analytical architecture (GEARA), independently established trust (IPCH06), compliance enforcement (IPCH09) or formal Product-family qualification (BPS/PIN). Their observations or authoritative determinations may be evidence inputs without transferring decision rights to IPCH08.

**DPP relevance:** An applicable DPP or other governed Product-bound representation may publish SLA/SLO expectations, machine-readable observability references, attributed trust signals or performance status. Its presence is **not** a new mandatory OBS criterion, proof of monitoring execution, DPP conformance or independently established service assurance. Applicable DPP authority remains separate.

## 4. Assessment subject and authority

Before attempting a maturity finding, separately establish:

1. **Product/Version:** actual assessed Information Product identifier, exact Product Version and valid D02 assessment eligibility (`EXPERIMENTAL_ELIGIBLE`, or separately authorized normative eligibility); otherwise `NOT_ASSESSABLE`.
2. **Promises and targets:** applicable service-level/informational expectations, targets, thresholds, measurement units, relevant time windows and approved authority; distinguish SLA obligations from SLO goals where applicable.
3. **Actual observation:** evidence of observed consumer-facing Product behaviours (not only component counters), monitored intervals and information-production patterns.
4. **Evaluation:** current executable evaluation/threshold-checking mechanisms, breach detection, event timestamps, ownership of response routing and actual execution history.
5. **PMDD enterprise tests:** executable, recurring maturity-test coverage; evaluation scope and characteristic/criteria versions; last assessment, trend and regression records. Do not infer executable coverage from proposed tests.
6. **Independent identities:** separately capture Product/Version, semantic-definition/version, implementation/realization revision, compilation identity, runtime occurrence, criteria/evaluation version and evidence effective/observation timestamps. Do not compress them into a single “version.”
7. **Evidence qualification:** issuer, provenance, governance authority, admissibility, target environment, missing signals, staleness, contradictions, legitimate visibility restrictions and confidence limits.

Neither observation tooling nor IPCH08 assessment authorizes service, policy, control, legal, semantic, entitlement, Product-family, DPP, realization or consequential action decisions. Governance and response arrangements derive from competent authorities. The human owner retains accountable experimental-disposition authority, without claiming verified institutional authority beyond existing holds.

## 5. Applicability and N/A rules

**Default:** IPCH08 is applicable to D02-eligible Information Products. No generic whole-characteristic `NOT_APPLICABLE` rule is established for non-real-time, internal, exploratory, restricted, niche, low-volume or infrequently produced Products. Their legitimate service and informational expectations, monitoring cadence and assurance profiles may differ; **both** mandatory observation dimensions remain relevant.

- Batch or periodic Products may measure release success, reporting-period freshness, quality against source cut-offs and timeliness; they need not imitate an always-live model endpoint.
- An E0 Product descriptor, conceptual observability blueprint or unexecuted PMDD test design is not evidence of production monitoring. If an eligible experimental Product has no operating evaluation, it cannot be presumed `MET`.
- Evidence of current operation in one realization or occurrence is not automatically transferable to all realizations or future Product Versions.
- Highly restricted data may require access-controlled observability; universally public dashboards are not mandated. Authorized governance/consumption visibility must be established under OBS-M07.
- A whole-characteristic `NOT_APPLICABLE` requires **affirmative competent D02 applicability determination**, with rationale and auditable evidence; insufficient information is `EVIDENCE_LIMITED`, not N/A.

## 6. Distinctness and non-duplication

| Neighbour | Independent maturity claim |
|---|---|
| IPCH01 — Domain-Owned | Product accountability versus actual observation and measurement of Product health. |
| IPCH03 — Declarative | Authoritative intended behaviour and Product definition versus measured actual behaviour. |
| IPCH04 — Discoverable | Discovery exposure of service status versus monitoring/evaluating that status. |
| IPCH05 — Self-Describing | Documented expectations, metadata and caveats versus execution-backed SLO evaluation. |
| IPCH06 — Trustworthy | Qualified current Product trust posture versus infrastructure producing and evaluating continuous observability signals. |
| IPCH07 — Reusable | Independent adoption versus usage telemetry as one category of observation. |
| IPCH09 — Compliant by Design | Policy/control adherence and enforcement versus observing attributed policy/control signals. |
| IPCH11 — Semantically Aligned | Semantic authority and conformance versus detection of material definition drift. |
| IPCH13 — Testable & Versioned | Testability/version-control disciplines versus executed recurring PMDD/product behaviour assessments. |
| IPCH16 — Interoperable & Composable | Actual composition and interoperability versus monitoring their performance. |

**Anti-circularity (`IPCH-NDC-01`):** A PMDD test engine's existence, scheduling or successful execution does **not** automatically prove IPCH08 `MET`. The other mandatory criteria, actual Product-level signals, governed targets, actionable deviations and history require independent proof. Reuse an evidence record across characteristics only for separately identified claims; do not copy an assessor's conclusion as another criterion's proof. A trust badge is not a monitored SLO; a compliance control description is not enforcement evidence; a declared Product SLO is not proof of runtime conformance.

## 7. Core mandatory positive criteria — `MET`

**All eight are mandatory, conjunctive and non-dilutable.** Every applicable claim must be affirmatively supported for `MET`. No numerical criterion-level weights, means, substitution by a “strong” neighbouring criterion or automatic caps are established.

| ID | Mandatory criterion | Required adherence assertion |
|---|---|---|
| **OBS-M01** | **Explicit Measurable SLA–SLO Expectations** | The Product has defined, governed and version-associated measurable expectations for its applicable operational and informational behaviour, including thresholds and meaningful evaluation windows. |
| **OBS-M02** | **Product-Level End-to-End Observability** | Monitoring reflects the actual consumer-facing Information Product experience, outcomes and informational Promise, not merely the health of infrastructure, scripts, pipelines or components. |
| **OBS-M03** | **Continuous Measurement and Evaluation** | Relevant runtime and informational signals are automatically collected and evaluated against the defined expectations at a cadence sufficient for material deviation detection given the Product's operating pattern and risk. |
| **OBS-M04** | **Information-Appropriate Behavioural Coverage** | Applicable informational quality, freshness, analytical/derivation, dependency and degradation concerns material to the Product's Promise are included in the monitored evidence, with justified applicability. |
| **OBS-M05** | **Detectable and Actionable Deviations** | Material SLA/SLO breaches, anomalies or degradation can be detected, attributed, surfaced and routed to competent investigation or remediation processes. |
| **OBS-M06** | **Automated Enterprise PMDD Maturity Observability** | Independently governed enterprise mechanisms actually execute recurring applicable PMDD characteristic evaluations, emit dated attributable maturity snapshots and preserve regression evidence, not just test designs or manual attestations. |
| **OBS-M07** | **Governed Machine-Consumable Visibility** | Product actors, authorized consumers, governance and appropriate enterprise mechanisms can inspect structured Product-linked observability outcomes and historical evidence through governed access. |
| **OBS-M08** | **Evidence Identity, Currentness and Historical Integrity** | Monitoring and PMDD evidence identifies the applicable Product/Version, effective realization/occurrence and evaluation/criteria versions, with timestamps, history, comparability and explicit limitations. |

`OBS-M06` does not mean all sixteen IPCH criteria are currently executable, adopted or normatively authoritative. **What level of automated maturity coverage suffices remains `OBS-R05 = OPEN`** and no undocumented relaxation of the approved mandatory dimension is permitted. Evaluate a live claim on the evidence actually produced, not on a research specification's ambition.

## 8. Core negative criteria — `NOT_MET`

The following are **evidence-based counter-indicators** requiring a defensible factual finding; they are not automatically applied maturity caps or an instruction to treat missing evidence as demonstrated failure.

| ID | Established negative condition |
|---|---|
| **OBS-N01** | Dashboards, logs or metrics exist but governed, measurable service/informational objectives are absent. |
| **OBS-N02** | Signals only describe infrastructure or constituent pipelines, with no defensible connection to the Product's end-to-end behaviour. |
| **OBS-N03** | Material Product runtime/informational observation is only manual or episodic and cannot detect meaningful deviations within the required window. |
| **OBS-N04** | Material freshness, informational quality, analytical degradation or dependency risks are excluded despite their essential connection to the Product Promise. |
| **OBS-N05** | Material breaches cannot be identified, attributed or routed to competent response mechanisms. |
| **OBS-N06** | Enterprise PMDD assessment is exclusively manual, optional, onboarding/audit-only or has no actual automated recurring operation. |
| **OBS-N07** | Observation outcomes are inaccessible to authorized Product actors or governance and are isolated in engineering-only tools without adequate machine-consumable exposure. |
| **OBS-N08** | Measurements or maturity evidence are stale, misattributed, wrong-version, non-comparable or represented as current despite limitations. |
| **OBS-N09** | Historical maturity trends present different Product definitions, criterion revisions or scoring versions as directly comparable without qualification. |

A verified `OBS-N06` precludes `MET` under D23; whether an otherwise mature operational-monitoring capability yields `PARTIAL` or `NOT_MET` is explicitly unresolved (`OBS-R02`). A detected `OBS-N01` similarly precludes `MET` while the edge-case severity boundary remains open (`OBS-R03`). Where absence is not demonstrated because evidence was not obtained, use `EVIDENCE_LIMITED` rather than assuming `NOT_MET`.

## 9. `PARTIAL`, `NOT_MET`, uncertainty and edge cases

| Established scenario | Candidate treatment | Guardrail |
|---|---|---|
| Eight mandatory claims fully and adequately supported | `MET` | Requires actual operational + recurring enterprise PMDD execution evidence and all other mandatory claims. |
| Product SLOs, timely automated runtime monitoring, but no operating enterprise PMDD tests | `PARTIAL` or `NOT_MET` unresolved | DPCH08 edge case suggests Partial, simplified rule Not Met; preserve `OBS-R02`. **Never MET**. |
| Dashboards and Product-linked telemetry exist, no measurable SLOs | `PARTIAL` or `NOT_MET` unresolved | AIPCH09 edge case Partial, simplified rule Not Met; preserve `OBS-R03`. **Never MET**. |
| Entire monitoring regime manual, occasional, no defensible material breach detection | `NOT_MET` if proved foundational | Mere visibility is not continuous observability. |
| Weekly PMDD maturity evaluation exists, material runtime breaches invisible | `NOT_MET` if fundamental runtime observation absent | Enterprise snapshots alone do not satisfy the characteristic. |
| Runtime evaluation active, but no permitted signal access outside engineers | `PARTIAL` or `NOT_MET` depending on actual severity | Governed consumer/governance visibility is mandatory; producer statements are insufficient. |
| Version-aligned PMDD histories unavailable in inspected materials | `EVIDENCE_LIMITED` | Do not infer historical non-existence unless proven. |
| Complete E0 design/monitoring blueprint, no execution records | Cannot claim `MET`; finding depends on operational evidence | Conceptual maturity tests are not empirical operations. |
| Product deemed ineligible under D02 | `NOT_ASSESSABLE` | Do not assign maturity score. |

`PARTIAL` requires **demonstrated genuine capability** plus an established non-foundational deficiency. `NOT_MET` requires a demonstrated foundational failure. `EVIDENCE_LIMITED` is an independent qualifier, not a fourth score. Do not turn source edge-case candidate findings into adopted global exceptions or criterion-level arithmetic. Where facts are sufficient but competing source interpretations remain unresolved, disclose the ambiguity and route it for accountable Second-Pass disposition rather than invent certainty.

## 10. Evidence signals and sufficiency

| ID | Required claim | Illustrative evidence (not prescribed implementation) |
|---|---|---|
| **OBS-ES01** | Governed objectives | Product-/Version-linked SLA/SLO contracts, indicator definitions, quality/freshness expectations, thresholds, measurement windows and approval provenance. |
| **OBS-ES02** | End-to-end Product outcome | Attributable outcome measurements, consumer-facing delivery success, informational-result timeliness/quality and the method linking telemetry to the Product Promise. |
| **OBS-ES03** | Executed continuous evaluation | Operating metric streams, sampled time series, configured evaluations, execution logs and measured detection cadence; inspect gaps. |
| **OBS-ES04** | Informational coverage | Product-relevant quality/reconciliation/freshness checks, analytical output/dependency change indicators and documented reasons for exclusions. |
| **OBS-ES05** | Actionable deviation | Breach records, alert rules, triggered events, response routing, remediation/incident traces or appropriately governed equivalent. |
| **OBS-ES06** | Automated enterprise PMDD operation | **Actual** scheduled characteristic-test execution records, timestamped maturity snapshots, historical trend/regression artefacts, characteristic/criteria versions and independent governance-source attribution. |
| **OBS-ES07** | Governed machine-consumable visibility | Structured, Product-linked observability record exposed via appropriately controlled API, registry, event stream, dashboard backing service or equivalent. |
| **OBS-ES08** | Identity, time and comparability | Exact Product/Version and effective realization/occurrence binding; semantic/criteria revision, observation and event times; evidence provenance, retention and comparability qualifications. |

**Claim-level sufficiency:** evidence establishes the specified assertion, its valid time and assessed scope; unrelated component health does not substitute. “PMDD tests are designed” is not “PMDD tests ran.” A screenshot of a dashboard without targets or history is insufficient on its own. An operator's assertion of a weekly schedule is not an executed maturity-test record. Evidence may reside in multiple governed systems; no universal platform, monitoring vendor, JSON field layout, DPP profile or fixed schedule is mandated by IPCH08.

**Evidence ledger guidance (`IPCH-ES-01`):** for each `OBS-M` record evidence URI/locator, issuer and independent authority, timestamp/effective window, Product/Version, realization/occurrence, criteria/evaluator revision, material limitation, counter-evidence, reproducibility and confidence. Protected evidence must be assessed under legitimate authorization; absence of public visibility is not failure when authorized access exists.

## 11. Agent-assisted or human assessment decision rule

1. **Resolve the assessment subject and eligibility.** Require a defensible exact Product/Version and D02 `EXPERIMENTAL_ELIGIBLE` or separately established normative eligibility. If not established, `NOT_ASSESSABLE`; stop numeric scoring.
2. **Resolve applicability and operational pattern.** State frequency of Product information production, intended users, relevant measured Promise and authorized observation scope. No generic N/A shortcut.
3. **Independently gather evidence for OBS-M01–M08.** Trace each to OBS-ES01–ES08 and source-qualified records. Include actual automated **runtime** and **PMDD** execution evidence, not just design.
4. **Check OBS-N01–N09 and contradictions.** Separate demonstrated absence/failure from inaccessible or never-examined evidence; preserve counter-evidence and time validity.
5. **Assess each mandatory claim qualitatively**, with rationale and evidence; do **not** assign point values to each criterion. Record justified coverage and any open interpretation conflicts.
6. **Apply the whole-characteristic decision:** `MET` only with all eight supported. If genuine observability exists but defects remain, analyze `PARTIAL` versus `NOT_MET` by severity; do not silently settle the `OBS-R02/R03` conflicting upstream edge cases. If evidence cannot support a defensible finding, attach independent `EVIDENCE_LIMITED` and state the bound.
7. **Apply D03 mapping only after valid characteristic finding** and D02 eligibility. Keep independent assurance, trust, compliance, semantic and critical obligations separately visible.
8. **Record human accountable disposition**, evidence provenance, assessor identity, rationale, effective time, research holds, source tensions and revisit triggers. An agent's draft output does not itself confer institutional authority.

**Anti-circularity test:** exclude any inference that an automated maturity tool has passed IPCH08 simply because it can mark itself executed. Audit a distinct source and record for actual Product-level target evaluation, telemetry, actionability, PMDD history and governance visibility.

## 12. PMDD scoring treatment

| D02 whole-characteristic result | D03 experimental characteristic score |
|---|---:|
| `MET` | `1.0` |
| `PARTIAL` | `0.5` |
| `NOT_MET` | `0.0` |
| `NOT_APPLICABLE` | Excluded from denominator only after affirmative competent applicability finding |
| `NOT_ASSESSABLE` | No characteristic score; D02 eligibility not established |
| `EVIDENCE_LIMITED` | **Independent evidence qualifier**, never assigned `0.5`, `0` or a fourth score merely because uncertainty exists |

Apply equal **characteristic-level** weights in a valid broader D03 experimental assessment, subject to existing denominator, uncertainty and applicability limitations. Do not average `OBS-M01–OBS-M08`, assign criterion weights, infer automatic caps, use labels `L0/L1/L2`, or claim normative maturity thresholds. Explicitly report the distinction between a fully evidenced whole-characteristic result and a candidate scenario left ambiguous by `OBS-R02/R03`.

A high IPCH08 score does not certify monitoring infrastructure, Product-family eligibility, other maturity characteristics, full enterprise PMDD automation or compliance. One Product's evidence does not prove platform-wide maturity test operation. Score history across different criteria/PMDD versions is not directly comparable without proper qualification.

## 13. Critical assurance and governance boundaries

- **BPS/PIN and competing Product-family/Compound authority:** independently establish Productness and family; IPCH08 observation does not award qualification.
- **GEARA and GEARM:** independently govern analytical architecture and semantic definitions; monitoring reference to a semantic Version does not confer semantic correctness.
- **INFOPROD/INFOPDS and DPP:** preserve Product definition, deployment-related specification and independently governed Digital Product Passport roles; publication of metrics in a DPP is possible evidence, not conformance authority.
- **PFI/HDIP and monitored realizations:** infrastructure, shared services, metric collection/retention, PMDD evaluation engines, source quality services, realization/compilation and runtime occurrences retain independently governed responsibilities and identities.
- **Consumer and governance visibility:** legitimate access restrictions remain; IPCH08 does not grant entitlement or assert who must operate enterprise monitoring beyond competent responsibilities.
- **Independent trust, control, legal and assurance:** observed signals may inform IPCH06, IPCH09 or separate controls but cannot supersede their binding outcomes or authorize consequential actions.
- **Anti-circularity:** do not use IPCH08's own test execution as self-justifying evidence for all OBS-M; distinguish objective execution from evidence adequacy.
- **E0 integrity:** 62 G06 E0 research designs approved but unexecuted; E1/E2 zero. No test platform, PMDD portfolio or approved criteria is treated as executed evidence. `OBS-R05` remains OPEN.

`OBS-R02`, `OBS-R03` and `OBS-R05` are explicit unresolved obligations. None is settled by this guide. A separate accountable decision would be required to change baseline criteria, install an exception or authorize Second-Pass execution.

## 14. Reassessment and evolution triggers

Reassess evidence when material changes occur, including:

- new or changed Product SLA/SLO objectives, interpretation windows, monitoring thresholds, consumer commitments or authorized risk tolerances;
- change to informational Promise, reporting grain, output semantics, material dependencies, source populations or data/analytical quality requirements;
- monitoring cadence, telemetry collector, alert routing, quality evaluation or PMDD test execution failures;
- new incidents, material breaches or evidence of informational degradation despite apparently healthy infrastructure;
- Product Version, semantic-definition Version, realization revision, compilation or runtime occurrence change affecting evidence attribution;
- changes to PMDD characteristic definitions, evaluator criteria/software or productization maturity snapshot comparability;
- loss of authorized visibility, historical observability data, timestamps, adequate evidence freshness or valid response ownership;
- research resolution or owner-amended criteria affecting `OBS-R02`, `OBS-R03` or `OBS-R05`.

Preserve immutable/historic evaluation context as justified, including old criteria Versions, observation timestamps, currentness evidence and reasons for supersession. New Version monitoring evidence does not retroactively establish observability for previous Versions. No universally mandatory calendar cadence is set.

## 15. Adversarial and boundary cases — First-Pass fixtures

**All cases are proposed research fixtures, not executed assessments, G4–G6 completion or evidence of deployed PMDD.** No result is adopted from these hypothetical cases.

| ID | Proposed challenge | Boundary to test |
|---|---|---|
| **OBS-A01** | Dashboards exist without measurable objectives | AIPCH09 source tension `OBS-R03`: visibility versus true SLO evaluation. |
| **OBS-A02** | Product runtime SLAs evaluated, but no automated PMDD test operation | DPCH08 source tension `OBS-R02`: mandatory PMDD versus `PARTIAL/NOT_MET`. |
| **OBS-A03** | Enterprise PMDD snapshots operate, but material runtime SLA breaches are invisible | Distinct non-substitutable runtime requirement. |
| **OBS-A04** | Infrastructure healthy, informational outputs materially stale | Product-level informational Promise versus component metrics. |
| **OBS-A05** | Quality monitor active but semantic-definition regression invisible | Applicable informational coverage and GEARM boundary. |
| **OBS-A06** | Weekly automated enterprise PMDD history and runtime SLO monitoring are both evidenced | Sufficiency and criteria-version-aware longitudinal interpretation. |
| **OBS-A07** | Quarterly manual maturity spreadsheet is sole PMDD evaluation | DPCH08 requirement for automated recurring monitoring. |
| **OBS-A08** | Monitoring delivered by an independently governed shared enterprise service | Implementation-neutral Product-level attribution and authority. |
| **OBS-A09** | Thresholds and telemetry exist but no actionable response routing | Detection/actionability under `OBS-M05`. |
| **OBS-A10** | Metrics reside only in engineering dashboards, unavailable to entitled Product/governance actors | Governed visibility and machine-consumption under `OBS-M07`. |
| **OBS-A11** | Maturity trend compares incompatible PMDD evaluator/characteristic versions | `OBS-M08` evidence comparability and unqualified historical claims. |
| **OBS-A12** | PMDD engine certifies IPCH08 simply because its own job executed | Anti-circularity: test execution cannot substitute for other mandatory claims. |

`OBS-A01–OBS-A12 = PROPOSED_E0_UNEXECUTED`. Future testing needs a separate authorization, complete fixture and competent evidence/decision process.

## 16. Source provenance, open questions and status

**Canonical source files examined:**

1. `DPCH.zip` → `pages/DPCH-PMDD-guidance/08-DPCH08.md`, **DPCH08 — SLA–SLO Backed & Observable**, especially its canonical Product-level operational/PMDD requirement, automated enterprise PMDD snapshots (e.g. weekly), governance visibility, manual-review failure, `PARTIAL` edge case and conflicting simplified decision rule.
2. `AIPCH.zip` → `AIPCH-PMDD-guidance/09-AIPCH09.md`, **AIPCH09 — SLA–SLO Backed & Observable**, especially explicit measurable behavioural objectives, continuous runtime evaluation, end-to-end Product-level signals, actionable deviation, machine-readable observability, dashboard-without-SLO `PARTIAL` edge case and conflicting simplified rule. AI-specific model/risk machinery is not imposed on Information Products as a universal metric checklist.
3. `INFOPS-0.1-IPCH-P01-D23-F01`, accountable owner-approved experimental First-Pass baseline, F01.1–F01.16, with D02/D03/D04/D05 method and authority boundaries unmodified.

**Open Second-Pass research:**

| ID | Exact retained research question | Status |
|---|---|---|
| **OBS-R01** | What minimum Product-level operational and informational observability dimensions apply across differing Information Product constitutions? | OPEN |
| **OBS-R02** | How does DPCH08's `PARTIAL` edge case without maturity monitoring reconcile with its stricter `NOT_MET` simplified agent rule? | **OPEN — SOURCE TENSION** |
| **OBS-R03** | How does AIPCH09's dashboard-without-SLO `PARTIAL` edge case reconcile with its mandatory measurable-objectives and simplified `NOT_MET` rule? | **OPEN — SOURCE TENSION** |
| **OBS-R04** | What cadence suffices for event-driven, batch, periodic and continuously produced Information Products? | OPEN |
| **OBS-R05** | What automated enterprise PMDD coverage suffices without presupposing all sixteen IPCH assessments are executable or normatively adopted? | **OPEN — EXECUTION-SCOPE BOUNDARY** |
| **OBS-R06** | How should Product/Version, semantic-version, realization, runtime occurrence and criteria-revision differences affect historical monitoring evidence? | OPEN |
| **OBS-R07** | How should trust, compliance, testability and observability share evidence without duplication or circularity? | OPEN |
| **OBS-R08** | What establishes actionable detection and governance visibility without prescribing monitoring vendors or response organizations? | OPEN |

**Document status:** `IPCH08-PMDD-GUIDE-01 / FIRST-PASS-DRAFT-01 = EXPERIMENTAL_DRAFT_PREPARED_ACCEPTED`; `D24_OWNER_DRAFT_ACCEPTANCE=APPROVED_EXPERIMENTAL_E0`; `PUBLICATION=NOT_DEPLOYED`; `EMPIRICAL_ASSESSMENT=NOT_EXECUTED`; `ADVERSARIAL_VALIDATION=NOT_EXECUTED`; `SECOND_PASS=NOT_STARTED`; `FINAL_GUIDE_APPROVAL=NOT_APPROVED`; `NORMATIVE_RELEASE=NOT_AUTHORIZED`.

**Existing characteristic status:** IPCH01 G4–G6 NOT_EXECUTED; IPCH02–IPCH07 outstanding reviews preserved. IPCH01–IPCH03 experimental guides confirmed deployed; IPCH04–IPCH07 overlays prepared with deployment not confirmed in the conversation. IPCH09–IPCH16 NOT_INITIATED.

**Parent INFOPS restrictions retained:** MVP-P01 D01–D08 approved; conceptual design stopped; experimental specification `DRAFT_PREPARED_NOT_VERIFIED`. Parent Track B B01 completion `NOT_ESTABLISHED`, B02–B06 `NOT_AUTHORIZED`. Effective prospective S04 `CLOSED_CONDITIONAL_RESEARCH (ONTOLOGY_AND_NORMATIVE_READINESS_UNRESOLVED)`; historical C06 `APPROVED_NOT_EFFECTIVE` with F01.6/F01.29 safeguards, original charter/audit `NOT_VERIFIED`; historical approval ledgers `65 / 6 / 7 / 7`, separate PC ledger unchanged. Q0–Q5 and F06/F14/F16 UNRESOLVED; G06's 62 E0 designs approved but UNEXECUTED; E1/E2 executions `0 / 0`; G06-RO01–RO12 and G03-R01–R12 — all 24 OPEN. No new institutional authority, repository modification, normative adoption, deployed monitoring or IPCH09 work is effected by this draft.
