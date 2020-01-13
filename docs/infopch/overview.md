---
title: Information Product Characteristics (IPCH)
description: Experimental 16-characteristic catalogue for the bounded INFOPS 0.1 Analytics-contextual Information Product profile.
---

# Information Product Characteristics (IPCH)

> **Status — APPROVED EXPERIMENTAL E0 CATALOGUE; NON-NORMATIVE RESEARCH.** The accountable owner approved `INFOPS-0.1-IPCH-P01-D01-F01` (F01.1–F01.16) as the **16-characteristic catalogue**. D02–D05 subsequently established experimental assessment and guidance controls. For IPCH01, D07–D10 accepted a guidance draft, its revision and a G2 PASS / G3 PASS_WITH_QUALIFICATIONS documentary review. IPCH02 First-Pass mandatory criteria were accepted under D11 and its experimental guidance draft under D12. **Outstanding Second-Pass work remains; no individual guide is finally approved.** This page does not verify live repository adoption or authorize a normative release.

![Radial infographic depicting sixteen Information Product characteristics, from Domain-Owned through Interoperable & Composable.](/img/information-product-characteristics-ipch-0.1.png)

*Figure: Characteristics of a True Information Product — an illustrative view of the approved experimental catalogue. "True" is a visual title, **not** an independent family qualification determination, maturity award or normative certification.*

## What characteristics do — and do not — establish

**Product-family qualification and Product maturity are different questions.** The bounded INFOPS 0.1 experimental qualification convention assesses independent Product constitution (**C1**), governing Analytics contextual intent (**C2**) and governed informational meaning (**C3**), with a separate competing-family/Compound boundary procedure (**B0**) and sufficient evidence. The qualification design does **not** establish a universally necessary-and-sufficient Information Product ontology.

IPCH concerns **how maturely** an assessed Information Product fulfils and sustains its informational Promise; it does **not** confer BPS/PIN Productness, independently adjudicate family/Compound identity, or certify correctness or current eligibility. A provisional experimental profile match is not a normative family qualification and does not itself authorize operational PMDD assessment or a release.

The first fourteen characteristic names follow the shared DPCH/AIPCH foundation. The final two reuse conceptual specializations already present in AIPCH. **Inheritance means shared characteristic intent, not automatic import of Data-only or AI-only obligations.**

## Sixteen approved experimental characteristics

### IPCH01 — Domain-Owned

**[Read the experimental IPCH01 Domain-Owned PMDD guidance](./IPCH01.md)** (DRAFT-02; G2 pass / G3 qualified pass; G4–G6 not executed).

The Information Product has an identifiable accountable domain and Product authority governing its purpose, informational Promise, meaning, and evolution. Ownership concerns the **Product and its business intent**, not merely the team hosting its analytics implementation.

### IPCH02 — Deployable

**[Read the experimental IPCH02 Deployable PMDD guidance](./IPCH02.md)** (`FIRST-PASS-DRAFT-01`; accepted under D12; Second-Pass review outstanding). [Research and publication status](./ipch02-research-status.md).

The Information Product can be independently provisioned, published, managed and evolved through governed Product-oriented mechanisms. Mature deployability supports Product Owner self-service: the owner governs **what** is required, while an appropriate realization environment handles **how** it is implemented; owning a dedicated calculation engine is not a prerequisite.

### IPCH03 — Declarative

The Product's governing intent, required informational meaning, consumption expectations and constraints can be expressed explicitly, rather than being buried solely in application code or informal producer knowledge. The declaration is about governed Product intent and semantics, not a requirement for any particular configuration language.

### IPCH04 — Discoverable

Potential consumers can locate the Information Product, identify its intended informational purpose and discover how to evaluate and access it through appropriate governed discovery surfaces. Discovery should convey relevant meaning and usage limits rather than merely a name or URL.

### IPCH05 — Self-Describing

The Product makes its identity, governing Promise, semantic definitions, analytical scope, provenance, dependencies, interfaces and known usage constraints understandable without repeated producer intervention. This is primarily **Product-level intelligibility**; explanation of a particular analytical conclusion is addressed distinctly under IPCH15.

### IPCH06 — Trustworthy

Confidence in the promised Information is supported by appropriate, current, inspectable evidence, including applicable informational quality, provenance, assurance and dependency states. For Information Products, **analytical-method validity** and **epistemic integrity** (including evidence-calibrated claims and uncertainty) remain explicit maturity concerns *within* Trustworthy, rather than separate top-level IPCH entries. Good metadata or operational monitoring must not conceal a materially invalid analysis.

### IPCH07 — Reusable

The Information Product can serve multiple appropriate consumers or analytical situations without bespoke producer intervention for each use. Reuse must preserve the governing semantic and usage boundaries; the ability to reuse an output does not imply that all possible downstream compositions are appropriate.

### IPCH08 — SLA–SLO Backed & Observable

The Information Product expresses appropriate consumption/service commitments and provides evidence for assessing delivery performance, availability, timeliness and relevant operational conditions. Observability supports informed consumption but is separate from proving the semantic correctness of every Information occurrence.

### IPCH09 — Compliant by Design

Applicable governance, legal, policy and access constraints are bound to the Product and enforceable through the responsible systems and contracts. Information-specific **context-safe usage** belongs here and in IPCH12; an Information Product does not thereby acquire authority over every consequential action taken by a downstream consumer.

### IPCH10 — Addressable

Consumers have identifiable, governed ways to access the Information Product through its appropriate ports, contracts or other consumption mechanisms. Addressability concerns stable contractual access, not a universal requirement for a REST API or any single technical delivery pattern.

### IPCH11 — Semantically Aligned

The Product's informational meaning and interpretation align with applicable governed domain and **GEARM** semantic references, including relevant definitions and Versions. Shared labels alone are insufficient where interpretation depends on timeframes, populations, units, assumptions or methods.

### IPCH12 — Consumption-Driven Intent

The Product's governing informational Promise and evolution are informed by declared analytical consumers, purposes and relevant decision-support contexts. The context of **appropriate and permitted use** must be understandable; incidental Analytics consumption of a Data Product does not reconstitute that source Product as an Information Product.

### IPCH13 — Testable & Versioned

The Product provides a basis for checking applicable Product, semantic and contractual expectations, and for governing their evolution across Versions. Product Version, semantic-definition Version, realization revision, execution and Information occurrences remain distinct. Tests of documented implementation behaviour must not be confused with proof that an analytical method is valid or an outcome correct.

### IPCH14 — Economically Accountable

The Product has transparent and accountable economic expectations concerning cost, sustainable operation, consumption and contribution to intended value. Economic accountability should be proportionate to the Product's context and must not presume a mandatory chargeback model or a particular funding mechanism.

### IPCH15 — Explainable & Transparent

Consumers can obtain explanations appropriate to the governing informational Promise, including relevant reasoning, method, contributing evidence, assumptions and limitations, so they can understand and **challenge specific informational outcomes**. This differs from IPCH05's Product-level self-description. Explanations are proportionate to the claim: descriptive analytics do not automatically require a causal account, model attribution or algorithmic introspection.

### IPCH16 — Interoperable & Composable

The Information Product can participate in **authorized** cross-Product arrangements while appropriately preserving semantic meaning, provenance, dependencies and applicable policy boundaries. This differs from IPCH07's individual reuse and IPCH11's semantic alignment. Maturity responsibilities must attach to the correct source Product, consuming composition or independently constituted Compound Product; an unauthorized or incorrect downstream combination is not automatically a defect in the source Product.

## Cross-family characteristic alignment

| IPCH | Characteristic | Data Product counterpart | AI Product counterpart |
| --- | --- | --- | --- |
| IPCH01 | Domain-Owned | DPCH01 | AIPCH01 |
| IPCH02 | Deployable | DPCH02 | AIPCH02 |
| IPCH03 | Declarative | DPCH03 | AIPCH03 (Declarative Specification) |
| IPCH04 | Discoverable | DPCH04 | AIPCH05 |
| IPCH05 | Self-Describing | DPCH05 | AIPCH06 |
| IPCH06 | Trustworthy | DPCH06 | AIPCH07 |
| IPCH07 | Reusable | DPCH07 | AIPCH08 |
| IPCH08 | SLA–SLO Backed & Observable | DPCH08 | AIPCH09 |
| IPCH09 | Compliant by Design | DPCH09 | AIPCH10 |
| IPCH10 | Addressable | DPCH10 | AIPCH11 |
| IPCH11 | Semantically Aligned | DPCH11 | AIPCH12 |
| IPCH12 | Consumption-Driven Intent | DPCH12 | AIPCH13 |
| IPCH13 | Testable & Versioned | DPCH13 | AIPCH14 |
| IPCH14 | Economically Accountable | DPCH14 | AIPCH15 |
| IPCH15 | Explainable & Transparent | Additional specialization | AIPCH16 |
| IPCH16 | Interoperable & Composable | Additional specialization | AIPCH20 |

*Alignment indicates shared intent or a candidate specialization, not identical family-specific evaluation obligations. Numbering is IPCH-local; AIPCH includes an additional declarative intelligence characteristic at AIPCH04.*

## Deliberately retained non-duplication boundaries

- **Analytical validity:** explicit Information-specific concern within **IPCH06 Trustworthy**, supported by **IPCH13 Testable & Versioned**; not an additional top-level characteristic.
- **Epistemic integrity and uncertainty calibration:** explicit concern within **IPCH06 Trustworthy**, with relevant communication/explanation evidence under **IPCH15**; not an additional top-level characteristic.
- **Context-safe and policy-bound use:** covered within **IPCH09 Compliant by Design** and **IPCH12 Consumption-Driven Intent**, preserving downstream consequential-action authority.
- **Explainability versus self-description:** IPCH15 concerns explanations of outcomes; IPCH05 concerns understandable Product constitution and description.
- **Composability versus reuse/alignment:** IPCH16 concerns cross-Product constraints and responsibility; IPCH07 concerns independent reuse and IPCH11 concerns semantic alignment.

## Status and next boundary

**Approved at conversation level:** D01–D10 of `INFOPS-0.1-IPCH-P01`. The sixteen-characteristic catalogue and experimental D02 assessment architecture, D03 scoring mapping, D04 guidance template and D05 authoring sequence are approved as bounded E0 research, **not normative requirements**.

**IPCH01:** The [Domain-Owned guide](./IPCH01.md) is `DRAFT-02 / EXPERIMENTAL_DRAFT_PREPARED`. D10 records **G2 PASS** and **G3 PASS_WITH_QUALIFICATIONS**, with DR-01–DR-08 verified **at documentary level only**. DO-01–DO-15 and G4-C01/C02 are unexecuted; R01–R04 remain open. G4–G6 have not been executed; G5 final individual-guide approval is **NOT_APPROVED**. The other fifteen characteristic guides are **NOT_INITIATED**.

**Scoring limitation:** D03 provides a provisional characteristic-level MET=1, PARTIAL=0.5, NOT_MET=0 mapping with equal weights and affirmative N/A handling, but no IPCH L0/L1/L2 maturity bands, criterion weighting, automatic caps or actual Product assessment are established. Evidence-limited uncertainty is not a maturity state.

**Parent research remains restricted:** The MVP-P01 conceptual design stopped after D08; parent Track B B01 completion is NOT_ESTABLISHED; prospective S04 is CLOSED_CONDITIONAL_RESEARCH with ontology/normative readiness unresolved. Q0–Q5, F06/F14/F16 and all 24 G03/G06 obligations remain unresolved/open; 62 G06 E0 designs remain unexecuted and E1/E2 executions remain zero. Source-documentary audit limitations and independent BPS/PIN, GEARA, GEARM, family/Compound, legal/policy and assurance authorities are not modified. **No Product has been qualified or maturity-assessed by publishing this overlay.**

*Repository naming note:* The existing path `infopch` is retained for compatibility; the owner-approved experimental characteristic identifiers are **IPCH01–IPCH16**. Historical repository artifacts and authorities are not renamed.
