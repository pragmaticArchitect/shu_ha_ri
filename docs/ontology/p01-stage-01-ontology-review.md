---
title: P01 Stage 1 - Ontology Review & Disposition
sidebar_label: P01-S01 - Ontology Review
---

# INFOPS-P01-S01 - Ontology review and proposed dispositions

> **Status: REVIEW DRAFT / NON-NORMATIVE (18 October 2026).** This is a review addendum to [the original Stage 1 baseline](./p01-stage-01-authority-and-ontology-baseline.md). It does not overwrite H01-H10, approve Information Product qualification, establish new BPS/GEARM/HDIP normative rules, award Product-family membership, or accept Stage 1 on anyone's behalf. All conclusions are proposed for review. Subsequent P01 work must test and govern them.

## 1. Review scope, input and authority

Review the ten original Stage 1 hypotheses (H01-H10), ten open questions (OQ-01-OQ-10) and eighteen cases (C01-C18) in light of the agreed reasoning about:

- Product Identity versus design/build/operational manifestations;
- Product's value-bearing essence versus its formation, execution and delivery mechanisms;
- interpretive/analytical semantics versus an analytics engine;
- PFI/golden-path implementation choices versus Product Owner-governed meaning;
- Product-family non-transitivity across Data, Information, AI, service and creative dependencies;
- multiple HDIP enterprises independently realizing an equivalent governed Product intent;
- qualification versus PMDD maturity, deployment conformance and point-of-use authorization.

Authoritative source responsibilities remain **BPS/PIN** (generic Product ontology), **GEARM** (Information, Information Proposition, Analytical Intent/Semantics/Process/Logic/Context/Output), **GEARA** (analytics architecture), **AIPS and applicable Data specifications** (adjacent Product families), and **HDIP-CLA M09/M13/M14** (realization and external boundary architecture). **INFOPS** may specialize Information Product qualification, but may not redefine these authorities. In particular, **PFI** is a Product realization responsibility/working label in the UPOS/HDIP context, not an extra frozen HDIP-CLA Plane or ABB.

Source anchors to verify at release: BPS PIN sections 2-5; GEARM M1 1.2-1.8, M2 authority, M3 3.5-3.14; GEARA 2.4 and CP1/CP2/CP3; HDIP-CLA M09 13-15; M13 BND-08/BND-09; M14 realization metamodel/PP-02 and R59; AIPS Productness/AI qualification/PMDD separation. Upstream versions and URLs remain unpinned.

## 2. Principal review finding: classification and realization are not alternative ontologies

The question **"Is the Information Product the governed Information or the engine that forms/delivers it?"** mixes the Product's intrinsic proposition with its implementation and operational manifestations.

Working distinction:

| Subject | What it is | Product-family inference |
|---|---|---|
| Information / Information Proposition (GEARM) | Meaningful content / defined informational value intended for a consumer | Does not by itself confer Productness |
| Product Definition and Product Promise (BPS/PIN) | Governed identity, intrinsic informational value, essential value capability and constraints | Candidate subject for Product and family qualification |
| Semantic constitution of proposed Information Product | Applicable Information Need, Intent, frame, context, analytical semantics and meaning-affecting formation logic, with authoritative references | Material to the meaning of the proposed Information Product; not automatically sufficient for family qualification |
| PFI realization and golden-path binding | Eligible technical form selected to implement governing requirements | Not independently a Product-family classifier |
| Executable artifact/operational behaviour | Realized code/logic, caller/adapters, runtime invocations and effects | Manifestation of a Product version, not necessarily its intrinsic identity |
| External analytics engine/API/cloud resource | Separately operated capability providing computation, hosting or data | Dependency, not automatically a constituent Product identity |
| Product output/interface/occurrence | Consumable Information and specific consumption events | Evidences value provision but does not by itself establish Productness |

This is a **lens separation**. A given Product may contain or bundle executable software; that fact does not make externally operated engines or hosting platforms intrinsic to its Product Family. Business meaning may require an analytical method; choosing the provider used to execute that method is a different decision.

### 2.1 An analytical lens is semantically necessary; a computational engine is not

The discussion uses **analytical lens** broadly to mean the governing way inputs acquire informational meaning: *intent/why, interpretive frame and purpose, context/environment, applicable semantic definitions and formation logic/how*. This should be mapped to, rather than redefined over, GEARM's existing terms (Information Need, Analytical Intent, Analytical Semantics, Analytical Context, Analytical Process/Method/Logic, Information Proposition). **"Frame" is a useful explanatory term, not yet a new canonical GEARM concept.**

GEARM explicitly allows Information formation through observation, curation, human interpretation, governed rules, Analytics, AI and synthesis. Hence INFOPS should not mistakenly require numeric calculation, executable code, a continuously operating service or a locally owned engine for every Information Product. A static research edition may carry a historically completed formation and its explanatory/provenance context.

At the same time, an ordinary Data Product can have rich business/technical semantics and transformation logic. **Having context, semantics, analysis or derived measures alone is not sufficient to qualify as an Information Product**; the Product's intrinsic promised *kind of value* must be examined.

### 2.2 Constituted information and repeatably formed information

Both are candidate realization modes of an informational promise:

- **Constituted/edition mode**: informational value is formed before a consumption occurrence (e.g. governed analytical report edition); consumers use that formed value without the Product executing a new analytics computation each time.
- **On-demand/continuously formed mode**: consumer request, time or events trigger new Information occurrences under governed interpretive/analytical rules.
- A hybrid may combine constituted outputs with dynamically generated Information.

These modes are **not new Product Families**, are not mandatory runtime stages, and must not pre-decide BPS qualification.

## 3. Hypothesis-by-hypothesis review dispositions

**Disposition:** RETAIN means compatible with current reasoning; REFINE means amend before Stage 2 testing; all remain hypotheses, not adopted INFOPS rules.

| Stage 1 | Disposition | Review finding / proposed amendment |
|---|---|---|
| **H01** | **REFINE (priority)** | Move away from the unrestricted "proposition OR capability providing propositions" dichotomy. Candidate VBE: a governed, **bounded Information Proposition or coherent proposition family**; candidate EVC: the ability to make the promised informational value available, possibly by repeatable formation. A generic engine's capability alone must not confer Information family membership. Test broad interactive Information Products fairly rather than excluding them by assumption. |
| **H02** | **REFINE** | Meaning-bearing intent/frame/context and proposition scope are material; an output format is not. But **rich semantics in a Data Product are not sufficient**. The primary Product Promise and intrinsic value, not merely context or analytical processing, must distinguish families. |
| **H03** | **REFINE (priority)** | The meaning-bearing **interpretive/analytical lens is necessary to characterize Information**, while a distinct computational transformation/execution engine is **not** universally necessary. Human/curated/static formation is legitimate; differentiate semantic logic from executable realization logic. |
| **H04** | **RETAIN / STRENGTHEN** | Explicitly adopt as a candidate **dependency/Product-family non-transitivity** test across AI-powered cars, movies, comics, songs, Data, Information and AI Products. A genuine compound/changed primary promise still warrants independent assessment. |
| **H05** | **REFINE** | Product Promise should delimit the intended informational value **and the governing analytical frame/context/logic needed for interpretation**; runtime context parameter values may vary under that governed definition. Do not require one frozen output or one unchanging static proposition. |
| **H06** | **RETAIN / CLARIFY** | Keep independent semantic/context/version currentness. Distinguish governed definition from execution occurrence and preserve historical meanings; not every parameter variation creates a new Product identity. |
| **H07** | **RETAIN / STRENGTHEN** | Cross-method independence extends to **cross-enterprise realization invariance** under eligible golden paths. A dependency on an AIPS-qualified AI Product does not itself change the containing Product's family. Semantic substitution is not allowed without authority. |
| **H08** | **RETAIN** | Distinguish Productness, Information-family qualification, PMDD maturity, realization readiness and usage/decision authorization. Mandatory obligations can block operation without magically changing intrinsic family. |
| **H09** | **RETAIN / CLARIFY** | Productization remains deliberate; implementation mechanism does not define family. Product Owner governs what is promised; PFI chooses eligible how, without acquiring semantic/Product authority. |
| **H10** | **RETAIN / STRENGTHEN** | Specify **Product identity vs definition vs implementation vs deployment vs execution/consumption occurrence**. A repo, diagram, executable, deployment and hosted service are distinct subjects/lenses; shared infrastructure does not establish Product identity. |

Proposed hypothesis review result: **4 require substantial refinement (H01, H02, H03, H05); 6 survive with narrower clarifications or strengthening (H04, H06-H10).** No new hypothesis is certified as true by this review.

## 4. Candidate cross-family propositions for falsification

These do not replace BPS/PIN; they are proposed interpretations to be reconciled with its source authority.

| Candidate | Investigative proposition | Counterexample to test |
|---|---|---|
| **XH-01: Identity / manifestation** | A Product's intrinsic identity is not identical to a repository, diagram, executable, deployment, provider resource or single output occurrence. | Embedded/self-contained Product bundles and simultaneous multiple versions. |
| **XH-02: Non-transitivity** | Product Family does not automatically propagate from producer, constituent, runtime, AI dependency or invoked service to containing Product. | Genuine multi-essence/compound Product and an intentionally changed promise. |
| **XH-03: Realization independence** | Same governed informational proposition may retain Product-family/kind classification across different eligible PFI golden paths, engines and enterprise topologies. | Semantically inequivalent algorithms, different applicable policy/jurisdiction or violated Product Promise. |
| **XH-04: Semantic constitution / execution independence** | Applicable analytical intent, interpretive frame, context and meaning-affecting logic are essential to understanding the proposed Information Product, while the engine implementing them can be an external governed capability. | Data Product with derived measures; static human-authored research; arbitrary BI engine. |
| **XH-05: Value availability / value formation** | A Product may make preconstituted value consumable or repeatedly form its promised value, without these modes determining its intrinsic Product Family. | A generic compute service with no bounded informational proposition. |

**Important nuance:** "Same intent" alone does not prove identical Product instances, compatible versions, operational conformance, or legal/governance equivalence. Product and family qualification must be evaluated for each actual bounded subject and version. A golden path cannot convert semantic non-equivalence into semantic equivalence merely by being approved.

## 5. Provisional family-differentiation test — not a qualifier yet

For candidate S, request evidence in this order:

1. **Subject/lens**: What exactly is being classified (governed Product identity/version, static edition, running service, API dependency, report occurrence, marketed bundle)?
2. **BPS Productness**: Is S a Product independently of whether it contains analytical content or has a marketplace entry? Unresolved Productness stops family certification.
3. **PIN**: What is S's VBE, EVC, Constitution and Identity Invariants? Which aspects are value semantics versus realization artifacts?
4. **GEARM grounding**: Identify the Information Proposition (or coherent bounded proposition family) and controlling Information Need, Intent, semantic definitions, contextual frame, formation logic and authoritative versions; account for preconstituted value where relevant.
5. **Strongest competing family**: Why is the primary value not mainly governed Data representation, generic analytics tooling, an independently qualifying AI intelligence capability, a generic service or a compound offering?
6. **Realization-neutral check**: Would eligible substitution of engines, API providers, compilation paths, location or precomputation change the promised **meaning**? If not, those facts alone must not change family classification.
7. **Disposition and uncertainty**: Record `CANDIDATE`, `COMPETING_FAMILY`, `PRODUCTNESS_UNRESOLVED`, `EVIDENCE_GAP` or `UNRESOLVED`, with rationale. **Do not issue an Information Product qualification certificate** in S01.
8. **Separate subsequent checks**: PMDD maturity, per-realization deployment/currentness, quality/fitness, access and downstream consequential Decision/Action authority.

This investigative sequence is **not** a complete sufficient/necessary condition set; P01-S02/S03 will derive and falsify those conditions.

## 6. Original open questions: reviewed priority

| Original question | Proposed review disposition |
|---|---|
| **OQ-01** Data versus Information | **Top priority**: enriched/precomputed/semantically rich Data Product versus bounded Information Proposition promise. |
| **OQ-02** Proposition versus producing capability | **Reframe**: VBE versus EVC and realization; fixed/bounded proposition families versus general-purpose analytics capability. |
| **OQ-03** Productization boundary | **Top priority**: BPS Productness independently of GEARM Information formation and optional Productization. |
| **OQ-04** Multiple propositions | **Keep open**: coherent bounded families, collections, compound Product and evolving service. |
| **OQ-05** Information and AI | **Keep open**: non-transitivity versus changed intrinsic intelligence promise/compound cases. |
| **OQ-06** Version/occurrence | **Strengthen**: definition/currentness, historical semantic meaning, runtime parameters and compiled bindings. |
| **OQ-07** Qualification versus maturity evidence | **Keep separate**: neither PMDD score nor build/runtime success confers family qualification. |
| **OQ-08** Contextual classifications | **Keep open**: actor role and commercial packaging versus intrinsic Product family. |
| **OQ-09** HDIP mapping | **Keep informative**: map to existing P2/P3/P4 and M14-PP-02; never create extra frozen Plane. |
| **OQ-10** Source manifest | **Still open**: exact applicable versions and URLs must be pinned before normative release. |

## 7. Gate for P01-S02

We should not issue draft normative qualification rules until the [realization and boundary stress tests](./p01-stage-01-realization-stress-tests.md) have been reviewed. S02 should specifically attempt to falsify H01-v2, H02-v2, H03-v2 and H05-v2, reconcile them to H04/H06-H10, and identify actual necessary/sufficient conditions. Keep INFOPCH and PMDD out of family qualification.

### Proposed review decisions (not pre-approved)

- **RD-01:** Accept identity/manifestation separation as an investigatory cross-family constraint.
- **RD-02:** Accept analytical/interpretive *semantic constitution* as relevant to Information-family classification; do not make engine ownership a qualification requirement.
- **RD-03:** Accept PFI realization independence subject to governing semantic/contractual equivalence; no universal golden path.
- **RD-04:** Accept Product-family non-transitivity, with compound/changed-promise exception tests.
- **RD-05:** Preserve explicit uncertainty about necessary/sufficient Information Product criteria pending S02 evidence.

**Review result:** READY FOR OWNER REVIEW; **NOT accepted, not normative, not frozen**.
