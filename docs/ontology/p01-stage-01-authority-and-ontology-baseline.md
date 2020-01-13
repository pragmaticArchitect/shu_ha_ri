---
title: P01 Stage 1 - Ontology & Authority Baseline
sidebar_label: P01-S01 - Authority & Ontology
---

# INFOPS-P01-S01 - Ontology and authority baseline

> **Status: WORKING DRAFT / NON-NORMATIVE.** This is Stage 1 of INFOPS-P01. It is an evidence-based intake and analysis document, not an approved Information Product definition, family qualification rule, schema or conformance claim. Any proposed meaning below is explicitly a hypothesis until tested and governed through subsequent P01 stages.

## 1. Stage purpose

Establish an accountable ontological starting point for a future **Information Product Specification (INFOPS) 0.1** that is compatible with BPS/PIN, GEARM, GEARA and relevant Data/AI Product-family authorities. The immediate challenge is not to name an Information Product or invent a lifecycle; it is to determine **which conceptual distinctions already have an authority** and exactly **what qualification question remains for INFOPS**.

Stage 1 shall produce a source-based authority map, invariant register, competing classification hypotheses, hard counterexamples and explicit Stage 2 questions. It SHALL NOT publish normative Information Product qualification, INFOPCH characteristics, PMDD weights, descriptor contracts or a mandatory development lifecycle.

## 2. Governing source baseline and jurisdiction

| Concern | Inherited authority | Stage 1 disposition |
|---|---|---|
| Generic Product, Product Family, Product Promise, PIN, Product identity/version | **BPS/PIN** | Reference and specialize; do not redefine Productness |
| Information Need, Information, Information Proposition, Analytical Intent and analytical semantics | **GEARM** | Preserve definitions and distinction of meanings from Product qualification |
| Analytical formation, composition, direct consumption and optional Productization responsibility | **GEARA** | Preserve architecture, not confuse a GEARA Plane with a Product Family |
| Data and Data Product semantics | **GEDRM/GEDRA** and applicable **external DPROD/DPDS** | Reference qualified Data Products without cloning the external standards |
| AI Product family qualification and Intelligence semantics | **AIPS / GEAIRM / GEAIRA** | Reference AI qualifications; AI dependency alone does not determine Information Product family |
| Cross-family Productization and governed self-service | **UPOS** | Align user journeys without treating an experience as an ontology authority |
| HDIP P1-P5, X1-X9 and M14-PP-02 Information/Analytics Product Profile | **HDIP-CLA** | Map future INFOPS contracts onto frozen architecture; do not create an extra Plane |
| Information Product-family-specific qualification and family contracts | **INFOPS (planned)** | Ontological gap under examination; NO criteria frozen in Stage 1 |
| Characteristics / maturity of an already-qualified Information Product | **INFOPCH / PMDD (future)** | Explicitly separate from family qualification |

This table is a responsibility and reference map, not a declaration that all upstream source versions are legally or technically incorporated by reference. Specific upstream versions and authoritative URLs must be confirmed in the eventual publication manifest.

## 3. Inherited distinctions: no redefinition permitted

These are already supported by the upstream model and constrain our work:

1. **Product classification uses Product Intrinsic Nature (PIN).** PIN has Value-Bearing Essence (VBE), Essential Value Capability (EVC), Constitution (CON), and Identity Invariants (INV). Constituent technology, consumer context, delivery format, owner, monetization and business role do not alone establish intrinsic family.
2. **Information is not a synonym for Analytics, analytical output, Data, Product or an interface.** GEARM gives Information and Information Proposition their analytical-domain meaning.
3. **Information Proposition is not Information Product.** The former may be intentionally productized, but existence of the former does not create the latter.
4. **Analytics is not Productization.** Neither an analytical computation nor repeated consumption, persistence, publication, an API or catalog registration independently qualifies a Product.
5. **Direct consumption is valid.** GEARA supports consumption of analytical Information without requiring Product constitution.
6. **Use of AI is not inheritance of AI Product family.** Analytical logic may invoke AI Products without the containing analytical outcome automatically qualifying as an AI Product.
7. **Recommendation, Decision, Action and Outcome are not equivalent.** Information support for a Decision does not convey consequential Decision/Action authority.
8. **Method and presentation do not determine Product family.** Rules, human interpretation, statistics or AI may participate in formation; PDF, chart, API and streaming are delivery/presentation choices, not ontological proof.
9. **HDIP M14-PP-02 is a realization Profile, not an Information Product definition.** Do not import the Data PDEP Stage 0-10 lifecycle by analogy.
10. **Qualification, maturity and production/consumption authorization are different questions.** A qualified family member can have low INFOPCH maturity, and a high PMDD score cannot establish family membership.

## 4. Core ontological inquiry

For a proposed subject S, investigate at least five distinct identities without equating them:

- **Semantic subject**: the Information Need, Information Proposition and governing semantic definitions (GEARM).
- **Product subject**: any product-qualified offering and its BPS/PIN version, promise and ownership.
- **Intrinsic value**: the essence and essential value capability which consumers engage, distinguished from upstream ingredients and means of delivery.
- **Constitution**: dependencies and formation relationships (e.g. Data, human reasoning, analytical definitions, AI capabilities, interfaces), distinguished from family membership.
- **Occurrence and context**: the time, consumer purpose, analytical execution, result and experience, distinguished from the enduring Product/definition.

A candidate Information Product must eventually be tested against **generic BPS Product qualification first** and **Information Product family specialization second**. A third, downstream step may assess INFOPCH/PMDD maturity, but must not alter the first two answers.

## 5. Working hypotheses for Stage 2 - NOT adopted rules

| ID | Investigative hypothesis | What could falsify or refine it? |
|---|---|---|
| H01 | An Information Product's VBE principally resides in a governed **Information Proposition** or in a capability that provides such propositions. | Durable Information offerings that have value not reducible to a discrete proposition; Info Products built from a catalogue or evolving interactive analytical environment. |
| H02 | An interpretable, meaning-bearing proposition is material to family membership; a delivery medium is not. | A Product supplying governed analytical information without a single stable proposition; ambiguous Product/service boundary. |
| H03 | Analytics may form Information but a distinct computational transformation need not be universal. | Curated human-authored interpretations, published static analyses and interactive analytical experiences. |
| H04 | The presence of Data, Information or AI Product dependencies does not by itself determine intrinsic Product family. | Compound or tightly coupled offerings that genuinely combine several independent value-bearing essences. |
| H05 | A Product Promise must make the Information value intelligible to a consumer and identify its intended semantic context. | General-purpose analytical capability without a bounded promise; consumer-specific interactive composition. |
| H06 | Meaning and context may be version-bound independently of runtime output, data schema or interface version. | A change in analytical definition with apparently identical numerical results; personalizations under one promise. |
| H07 | Human, symbolic, statistical and AI methods may contribute to the same Information Product without automatic family reclassification. | Output whose essential value is an independently qualified Intelligence capability rather than Information. |
| H08 | Qualifying an Information Product does not require high PMDD maturity, universal historical replay, full provenance completeness or a universal quality score. | Mandatory obligations required by existing BPS, governance or applicable Product-family source that are preconditions instead of maturity features. |
| H09 | Productization is intentional and governed but does not prescribe one universal role, method, lifecycle or technology. | A case in which contextual business ownership, physical packaging or distribution seems to define the entire intrinsic Product. |
| H10 | One deployed artifact may serve several semantic and Product contexts; the classification subject must be explicit. | Genuine multi-family or compound Product claims requiring a more precise constituent-family ontology. |

Each hypothesis shall be tested against positive cases, negative cases and counterexamples in [the Stage 1 case inventory](./p01-stage-01-classification-cases.md). Hypotheses are prompts for examination, not executable acceptance tests.

## 6. Candidate reasoning procedure (not a qualification algorithm)

1. **Identify the assessed subject**: Product version, asset, service, analytical output, report occurrence or capability; don't silently switch subject mid-test.
2. **Identify governing authorities and versions**: BPS/PIN, GEARM, applicable Data/AI family specifications, domain semantic ownership and any upstream contracts.
3. **Evaluate generic Productness via BPS**: if not established, return `PRODUCTNESS_UNRESOLVED` or `NOT_QUALIFIED`, not a guessed family membership.
4. **Describe the proposition and PIN dimensions**: VBE, EVC, CON and INV; explicitly distinguish value from ingredients.
5. **Explore competing families**: Data, Information, Intelligence/AI, Service, Compound, other, plus `UNRESOLVED`; test boundary counterexamples.
6. **Record assessment rationale and missing evidence**. Stage 1 cannot issue an INFOPS Information Product qualification certificate.
7. **Keep PMDD and production authorization separate** from the classification outcome.

The eventual normative family test must be developed in P01 Stage 2 or later and only then encoded into machine-readable requirements.

## 7. Open ontology questions (priority order)

| ID | Open decision | Evidence needed |
|---|---|---|
| OQ-01 | What is the necessary and sufficient differentiator of Information Product from qualified Data Product? | Contrast qualified output propositions sharing the same payload and interfaces |
| OQ-02 | Is the VBE the Information Proposition, a governed ability to provide propositions, or either under bounded conditions? | Static report, recurring subscription, self-service analytical service |
| OQ-03 | What makes an Information Proposition qualified for Product specialization without equating `Information` and `Product`? | BPS PIN/Product Promise application to examples |
| OQ-04 | Can several analytical propositions constitute one Product without violating identity and promise? | Report collections, interactive comparison, evolving metric services |
| OQ-05 | When does Information packaged together with qualified AI/Intelligence become compound or stay Information? | AI-assisted narratives versus inference-service offerings |
| OQ-06 | Are Information-specific type/occurrence and semantic versioning sufficient, or are further family-specific identity invariants required? | Definition vs observation vs report occurrence cases |
| OQ-07 | What constitutes mandatory family qualification evidence versus optional/graded maturity evidence? | BPS constraints and the future INFOPCH inventory |
| OQ-08 | Can a Product have several context-specific classifications without intrinsic identity being contradicted? | Direct analytical consumption, derived Products and multi-family cases |
| OQ-09 | What are the non-normative HDIP implications of an INFOPS-qualified Product? | P3-ABB-02, P4 Product Ports, PDEP and M14-PP-02 mappings |
| OQ-10 | Which source versions/authority URLs will be pinned for INFOPS 0.1? | Approved release baselines for BPS/PIN, GEARM/GEARA, external Data and AI specifications |

## 8. Source traceability (to be pinned)

- **BPS Product Ontology / PIN**: Sections 2-4 (intrinsic nature, VBE, EVC, constitution and identity invariants).
- **GEARM 0.1**: M1 Sections 1.2-1.8 and M2 semantic authority matrix / source-jurisdiction distinctions.
- **GEARA 0.1**: Section 2.4 Product Boundary and adjacent Data/AI/Decision boundaries.
- **HDIP-CLA 0.1 M14**: PP-02 Information / Analytics Product Profile and separation from Data PDEP.
- **AIPS PMDD ontology realignment**: Productness, family qualification, maturity and independent governance separation.

Do not treat this list as a resolved normative version manifest. Each source version and publication URL requires an explicit Stage 2 or release decision.

## 9. Completion criteria and hand-off

Stage 1 is review-ready when: all cited source responsibilities are mapped; inherited constraints are distinguishable from hypotheses; at least twelve boundary cases have been captured; unresolved ontology questions are documented; INFOPCH/PMDD and descriptor rules remain unfrozen; and the Docusaurus site contains no misleading claim of published qualification or conformance.

**Next proposed stage: INFOPS-P01-S02 - PIN Differentiation & Falsification Tests.** Investigate OQ-01 through OQ-06 and assign justified case dispositions. No Stage 2 result is presupposed here.
