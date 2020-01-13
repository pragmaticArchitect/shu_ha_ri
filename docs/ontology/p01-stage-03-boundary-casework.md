---
title: P01 Stage 3 - Qualification Boundary Casework
sidebar_label: P01-S03 - Boundary Cases
---

# INFOPS-P01-S03 - Candidate qualification boundary casework

> **HYPOTHETICAL / RESEARCH-ONLY / NON-NORMATIVE.** No row below is an actual Product qualification, negative certificate or permission to operate. Cases S03-T01–T20 apply the [proposed Q0–Q5 decision model](./p01-stage-03-candidate-qualification-rules.md) to constructed scenarios; C01–C36 in the original [S02 ledger](./p01-stage-02-case-disposition-ledger.md) remain unchanged. Case identifiers here are not INFOPCH characteristics or conformance test IDs.

## 1. Data–Information and analytical-service boundaries

| Case | Defined subject and governing Promise | Conditional S03 inference | Research disposition / missing proof |
|---|---|---|---|
| **S03-T01** | A genuine Data Product promises governed historical exchange-trade representations; a VWAP field is included as derived data | VWAP alone does not make Information the primary VBE; inspect Data Product family authority | `COMPETING_FAMILY_PLAUSIBLE`; confirm actual Promise and external Data-spec applicability (S02 C02/C21) |
| **S03-T02** | A separately qualified Product promises governed *interpretation of crypto price formation*, including eligible population, VWAP method, context, assumptions and intended consumer assessment; numerical payload identical to T01 | Conditions Q1–Q4 appear supportable if BPS Productness and family boundaries are demonstrated | `PROVISIONAL_INFORMATION_MATCH`, **not qualified** (S02 C04/C15/C27) |
| **S03-T03** | A Product exposes the same VWAP values and is called both “Data Product” and “Information Product”; the primary Promise is missing | Neither terminology nor same-value test decides primary intrinsic VBE | `INSUFFICIENT_EVIDENCE` (S02 C02/C21) |
| **S03-T04** | An API Product promises arbitrary mathematical calculations without a governed informational objective | Primary VBE is general computational/analytical capability, not a bounded informational proposition by definition | `COMPETING_FAMILY_PLAUSIBLE`; verify owner Promise (S02 C07/C20) |
| **S03-T05** | A versioned annual research report intentionally productized, with evidence, editorial interpretation, context and consumer Promise; authoring engine retired | Static, human-authored Product may qualify; owning a live engine is not Q1–Q4 | `PROVISIONAL_INFORMATION_MATCH` if generic Productness and informational VBE established (S02 C05/C19/C30) |
| **S03-T06** | One-off analyst report produced in a meeting without independent Productness | Useful Information is not enough to establish a Product subject | `PRODUCTNESS_UNESTABLISHED` (S02 C03/C14) |
| **S03-T07** | Reusable but unconstrained BI explorer bundled with arbitrary templates; no bounded Information Promise | Produces Information but may primarily promise general analytics tooling | `CONFLICT_REVIEW` if Product offers independent, bounded subscriptions; otherwise competing Service/tooling family (S02 C12/C20) |
| **S03-T08** | Live settlement-health subscription publishes governed measures and interpretation, with bounded allowed interactive drill-down | Variable outputs and parameters do not defeat bounded/coherent proposition family if its semantics are controlled | `PROVISIONAL_INFORMATION_MATCH` if Q0–Q5 evidenced (S02 C04/C12/C28) |

## 2. AI, compound and downstream-action boundaries

| Case | Defined subject and governing Promise | Conditional S03 inference | Research disposition / missing proof |
|---|---|---|---|
| **S03-T09** | AI Product principally promises fraud inference/prediction as an intelligence capability | AIPS and BPS determine its family; outputs containing Information do not automatically make the Product an Info Product | `COMPETING_FAMILY_PLAUSIBLE` (S02 C09) |
| **S03-T10** | Governed Information subscription invokes an independently qualified AI Product for explanatory text without changing metric/interpretation rules | AI is a dependency; informational VBE may persist | `REALIZATION_INVARIANCE_CONDITIONAL`, contingent on meaning and Promise preservation (S02 C08/C13/C33) |
| **S03-T11** | “Crypto market insight and auto-trader” promises both Information and autonomous trade execution under potentially different authorities | Material dual Promise and consequential-action rights cannot be hidden under INFOPS | `CONFLICT_REVIEW`, review compound/independent Products and authorization (S02 C18/C31) |
| **S03-T12** | Alert output says “Late settlement likely”; downstream workflow may initiate an action | Information/recommendation/output and authorized Decision/Action must be separately scoped | `CONFLICT_REVIEW` until Product subject, permissions and promise clarified (S02 C10) |
| **S03-T13** | A Movie, Comic, Car or Rocket is produced or operated with AI capabilities but principally promises audiovisual, narrative, mobility or aerospace value | AI use/provenance does not inherit AI Product Family | `COMPETING_FAMILY_PLAUSIBLE` for Info/AI; PIN of actual host Product required (S02 C23) |

## 3. KivaNura analogy, Product identity and PFI boundaries

| Case | Defined subject and governing Promise | Conditional S03 inference | Research disposition / missing proof |
|---|---|---|---|
| **S03-T14** | Vehicle-telemetry Product promises governed sensor/event representations | Contextual sensor metadata or diagnostic labels alone do not establish informational VBE | `COMPETING_FAMILY_PLAUSIBLE`, independently assess actual Data Promise and family rules (S02 C02) |
| **S03-T15** | Engine-health Product promises governed *interpretation* of sensor temperature against vehicle-specific limits, loads and context | Interpretive semantic constitution and informational Promise distinguish it from raw telemetry | `PROVISIONAL_INFORMATION_MATCH` only with independent Productness and Q0–Q5 evidence (S02 C06/C27) |
| **S03-T16** | Technical service manual or knowledge reference sold as a stand-alone Product | It contains Information/Knowledge; however its primary VBE might be authored technical reference content, a Service, or another kind | `CONFLICT_REVIEW` until BPS/PIN and applicable creative/reference-family boundaries analyzed (S02 C05/C12) |
| **S03-T17** | Crypto Information Product Kind is realized in three enterprises by precomputation, a math API and AI-assisted formation with identical governed Promise | No PFI mechanism alone should alter Product Kind; each enterprise has its own identity and controls | `REALIZATION_INVARIANCE_CONDITIONAL`; require semantic and contract equivalence (S02 C22/C26/C35) |
| **S03-T18** | PFI swaps agreed VWAP for another estimator or changes the market population | Material semantics changed even if outputs look plausible | `SEMANTIC_CHANGE_REVIEW`; no silent certification under same Promise (S02 C24/C27/C34) |
| **S03-T19** | One Product accepts different valid asset/time-window parameters | Parameter occurrence changes need not create a Product Version or family | `REALIZATION_INVARIANCE_CONDITIONAL` within permitted context rules (S02 C28) |
| **S03-T20** | A shared analytical engine serves ten differently owned Info Product candidates | Shared runtime neither merges Product identities nor proves they are qualified Information Products | `REALIZATION_INVARIANCE_CONDITIONAL` for identity independence only (S02 C25/C36) |

## 4. Findings that may be provisionally preserved

1. **Informational semantics are not a payload type.** Same fields can appear under different intrinsic Product Promises; Data/Information remains unresolved until the actual promise and independent authorities are examined.
2. **Information formation need not be computational or self-hosted.** Contextually interpreted, editorially governed static Information can be a valid candidate, subject to BPS Productness.
3. **AI participation is non-transitive.** Being generated by, containing, or invoking an AI Product does not automatically make a host Product an AI Product.
4. **An API/engine is not a family qualifier.** The external engine is not automatically part of Product intrinsic identity; generated invocation behaviour may be part of a specific executable realization.
5. **Knowledge and Intelligence are not forced successor stages.** The KivaNura analogy is informative and must not create a mandatory pipeline or decide Product kind.
6. **Compound claims need real subject decomposition.** The correct subject may be a bundle, one constituent Product, or an independently qualified compound; do not resolve by arbitrary “dominant technology”.

## 5. Falsification gaps and required real-world evidence

- **Possible false positives:** an enriched Data Product marketed as “insight”; generic BI with themed dashboards; an AI inference Product wrapped as an informational subscription; a knowledge manual assumed to be an Information Product.
- **Possible false negatives:** editorially constituted research Product with no executable logic; interactive bounded Information Proposition; dynamic Information Product dependent on externally operated engines.
- **Unknowns:** what proves a coherent proposition family in a complex product, how to adjudicate truly independent multi-primary promises, and how much semantic metadata a Data Product can include without changing its primary VBE.

A real qualification record must pin subject identity, owner/governing Product Promise, semantic authority/effective versions, independent Productness result, family alternatives and applicable lifecycle context. The [S03 decision procedure](./p01-stage-03-decision-procedure.md) can structure review, but is not itself an approved assessment or conformance procedure.
