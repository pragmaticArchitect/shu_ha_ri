---
title: P01 Stage 2 - PIN Differentiation & Falsification
sidebar_label: P01-S02 - PIN Falsification
---

# INFOPS-P01-S02 - PIN differentiation and falsification

> **Status: RESEARCH DRAFT / NON-NORMATIVE / OWNER REVIEW REQUIRED.** This document does not certify Information Product membership, revise BPS/PIN, GEARM, GEARA, AIPS, external DPROD/DPDS, or frozen HDIP-CLA, or establish a binding INFOPS Product qualification, Product type taxonomy, descriptor, maturity score, or conformance test. Stage 2 tests proposed qualifications *against* counterexamples. A successful research assertion means only that a stated inference follows from a hypothetical scenario under stated assumptions.

## 1. Purpose, inherited baseline and research subjects

Stage 1 documented H01-H10 and C01-C18; the subsequent ontology review revised the investigative hypotheses and added C19-C28. Stage 2 attempts to falsify the revised interpretation across Data, Information, AI, Service, Creative and Compound Product cases, including different PFI realizations of a common governed informational promise.

**Semantic and Product authority is not transferred to INFOPS:**

| Concern | Authority to preserve | S02 treatment |
|---|---|---|
| Generic Productness, Product identity, Product Promise, Product Family and PIN | BPS / PIN | Productness is a separate precondition; apply VBE, EVC, Constitution and Identity Invariants |
| Information, Information Proposition, Information Need, Analytical Intent, Analytical Semantics, Definition/Occurrence and Information context | GEARM | Reference meaning; distinguish semantic constitution from runtime engine |
| Analytical responsibility, direct analytical consumption and optional intentional Information Product provision | GEARA | No inference that Analytics equals Productization |
| Generic Data meaning and qualified Data Product semantics | GEDRM/GEDRA and applicable external DPROD/DPDS | Treat Data Product classification as independently governed; do not clone specifications |
| AI qualification, AI Product versions and applicable risk controls | AIPS / GEAIRM / GEAIRA | AI dependency is not Product-family inheritance; do not apply an AI qualifier to the containing Product automatically |
| Product creation/consumption and eligible implementation | UPOS / PFI, HDIP-CLA P1-P5 / X1-X9 and M09/M14 | Compilation and hosting do not establish Product Family; no new Plane, ABB, or universal golden path |
| Proposed Information Product specialization | INFOPS (not yet normative) | Derive candidate necessary conditions, then challenge each as a universal qualifier |
| Product maturity and readiness | Future INFOPCH/PMDD and separately applicable governing authorities | Explicitly excluded from family qualification decisions |

An investigated *subject* must be named before classification: a Product identity/version, report edition, one-off report occurrence, generic analytical service, generated executable, deployed instance, consumed API service, commercial bundle, or individual Product inside a bundle. Switching this subject silently invalidates a comparison.

## 2. Rules of falsification, not qualification

1. **Test a claim at its proposed logical strength.** `Necessary` means every qualifying Information Product would need it. `Sufficient` means having it would establish membership; isolated positive examples cannot prove sufficiency.
2. **Counterexamples must preserve the assessed subject.** One report occurrence is not a published Product; one executable is not the full enduring Product; one trading API is not the containing market-information Product.
3. **Use a competing-family test.** Ask whether the same evidence more strongly describes Data representation, a generic analytical tool/service, a qualified intelligence capability, creative content, or a true compound Product.
4. **Apply an engine-substitution test.** Recompute the same intended informational proposition using a different eligible golden path while preserving semantics, Product Promise and obligations. Engine substitution itself must not reclassify the Product.
5. **Apply an adverse-semantic test.** Keep the runtime architecture similar but change the agreed calculation, population, time-window interpretation, analytical assumption or information objective. Similar numbers do not establish semantic equivalence.
6. **Separate four outcomes.** (a) Productness, (b) candidate intrinsic family, (c) realization/operational conformance and authorization, and (d) INFOPCH/PMDD maturity. None can substitute for another.
7. **Distinguish hypothetical logical evaluation from real evidence.** These synthetic cases prove neither a live Product's qualification nor a deployed system's performance; empirical conformance would require Product-version evidence, accepted contract, source and semantic versions, compilation trace, execution observations and approved assessment.

Research conclusion codes used here: `COUNTEREXAMPLE_TO_RULE`, `SUPPORTED_UNDER_PREMISES`, `CONDITIONALLY_SUPPORTED`, `UNRESOLVED`, `OUTSIDE_INFOPS`. They are **not** qualification statuses.

## 3. Candidate ontology: what is being differentiated?

The leading family hypothesis is that the **primary Value-Bearing Essence (VBE)** of an Information Product is a governed, bounded **Information Proposition**, or a coherent bounded family of such propositions. The **Essential Value Capability (EVC)** is to make that promised informational value consumable through an eligible Product interface, whether it is already constituted, formed upon request, periodically regenerated, interactively refined within its contract, or realized through several modes.

A **meaning-bearing semantic constitution** is relevant: governing Information Need/Analytical Intent, interpretive frame (what question, why, perspective/analytical assumptions), context rules (subject, population, environment, time and applicability), semantic definitions and meaning-affecting formation/interpretation logic. Semantic definition is not equivalent to compiled executable logic. A governing context *rule* is not equivalent to a particular runtime context *value*.

**Key qualification:** a Data Product may also contain calculations, semantic annotations, contextual definitions and derived measures. A genuine Information Product distinction cannot rest on the mere presence of those ingredients. Nor is the production or analytical execution engine a required intrinsic component. GEARM itself distinguishes `Information Proposition != Information Product`; BPS Productness and intentional Product constitution remain independent gates.

### 3.1 Candidate necessary conditions to test, not accepted requirements

| ID | Candidate condition | Counterexample / challenge | S02 disposition |
|---|---|---|---|
| **N01** | Generic BPS Productness of the exact assessed subject must be independently established | A one-off dashboard chart or a generated report occurrence can carry meaningful Information but lack evidence of Productness (C03/C14/C17) | `SUPPORTED_UNDER_PREMISES` as inherited authority; not newly invented by INFOPS |
| **N02** | The primary VBE is informational value expressible through a bounded Information Proposition or coherent family | A BI engine can produce arbitrary information yet principally promise general-purpose analytical tooling (C07/C20); broad interactive informational offerings (C12/C31) challenge over-restrictive bounds | `CONDITIONALLY_SUPPORTED`; what counts as coherent/bounded remains open |
| **N03** | Applicable intent, frame, context rules and meaning-affecting semantic logic make the promised informational proposition interpretable | Static human-curated research need not contain executable analytics code (C05/C06/C19/C30); Data Product may have equally rich semantics (C02/C21) | `SUPPORTED_UNDER_PREMISES` for semantic meaning, **not sufficient** for Information family membership |
| **N04** | EVC is governed availability of the intended informational proposition(s) to eligible consumers | A Product can supply a fixed, versioned edition; it need not continually regenerate (C05/C30). An arbitrary computation API may offer availability without a bounded informational promise (C20) | `CONDITIONALLY_SUPPORTED`; availability does not imply a universal runtime/port form |
| **N05** | Product Promise and identity invariants distinguish the informational offering from specific outputs/occurrences and from dependencies | Two enterprises may share Product Kind and semantics but have different owners and identities (C22/C35); changed framing/version can alter the promise (C15/C16/C27) | `SUPPORTED_UNDER_PREMISES`, inherited PIN semantics; family-specific invariant set still open |
| **N06** | Family classification follows the primary intrinsic value rather than the production method, model, engine, delivery medium or hosting environment | AI-powered movies, Data Products with VWAP, and precomputed/API/AI-assisted market information (C21-C26/C32) | `SUPPORTED_UNDER_PREMISES`, with explicit compound/changed-promise exception review |

No row above is a completed **necessary-and-sufficient** theorem. N02 and N04 remain especially vulnerable to borderline informational platforms, editorial catalogues and packaged compound services. They cannot be made normative solely because these examples are intuitively compelling.

## 4. Shortcut criteria conclusively rejected as universal tests

| Tempting rule | Why it fails | Demonstrative counterexamples |
|---|---|---|
| `contains an analytics engine -> Information Product` | A generic tool computes, but its VBE may be analytical tooling, not a governed informational proposition | C07, C20 |
| `must contain its own analytics engine` | A qualified candidate may distribute a fixed analytical publication or bind to a shared engine | C05, C19, C26, C30 |
| `contains AI -> AI Product` | Constituent/producer family is not inherited; AIPS qualification must test the Product itself | C08, C13, C23, C33 |
| `has metrics / calculated fields -> Information Product` | A qualified Data Product may expose derived measures while promising governed Data representation | C02, C21 |
| `is a dashboard, API, PDF, chart or subscription -> Information Product` | Format and delivery mechanism do not establish VBE, Productness or intentional Productization | C03, C05, C17, C32 |
| `same numerical payload -> same informational meaning` | Different populations, period boundaries, weights, source eligibility or methods can change meaning | C15, C27, C34 |
| `approved golden path -> semantically equivalent realization` | A golden path controls eligible realization, not the authority to redefine a governed metric | C22, C24, C34 |
| `is published, reused, registered or highly mature -> qualified` | Distribution, repeated use, listing and PMDD are not family-qualification evidence | C03, C14, C17 |
| `same intent across enterprises -> same Product instance` | Same Product Kind/promise may be implemented by distinct governed Product identities | C22, C35 |
| `runtime access failure -> different Product Family` | Operational conformance and intrinsic classification are independent questions | C22-F3 |

These are falsifications of **proposed universal proxy rules**, not certifications of any named hypothetical case.

## 5. Cross-family stress: Data, Information, AI, Service and Compound

### 5.1 Data Product versus Information Product is a promise/PIN boundary

Suppose the same signed output contains timestamps, prices and a calculated volume-weighted average price (VWAP). A Data Product might primarily promise a governed representation of market observations, including derived attributes, defined measures and accurate source semantics. An Information Product candidate might principally promise an **assessment of price formation**, with governed interpretation, frame, intended comparison, population, period, assumptions and fitness for that informational question.

**Identical output is possible**. The classification cannot rely on payload shape, the existence of SQL or the presence of analytical descriptions. It requires separately evidenced primary VBE/EVC, Promise and identity invariants, followed by comparison to the applicable external Data Product qualification authority. If an offering materially promises both independently, assess **Compound** or constituent Products instead of declaring a universal family-precedence rule. When evidence is insufficient, record `UNRESOLVED`.

### 5.2 Information Product versus generic analytical service

An enterprise BI engine or arbitrary analytics API may provide a powerful capability to form Information without promising a bounded information proposition. Its primary intrinsic offering may be a tool or Service Product. A configured risk-monitoring service providing a governed and coherent set of risk explanations *might* instead qualify as Information, depending on Productness, promise, boundedness and constitution. This is a boundary for later owner decisions, not a ban on interactive products.

### 5.3 Information Product versus AI Product

An Information Product may invoke a separately qualified AIPS AI Product. The containing Product does not thereby inherit AI family. If the primary proposition changes from governed interpreted market information to a qualified intelligence capability, independent AIPS qualification and possibly a new Product identity / compound offering require assessment. A predictive number itself does not automatically prove AI Product status.

### 5.4 Creative and other Products

Comics, Movies, Songs, Cars and Rockets may be AI-created or AI-powered without turning into AI Products. Product-family classification is non-transitive through dependencies and production methods. AI Products can nonetheless be genuine independently qualifying constituents. Cross-family PIN concepts are not redefined by INFOPS.

## 6. Analytical constitution is not an engine inventory

Interpretive meaning requires applicable **frame, purpose, context rules and governing logic**. The formation logic may be represented declaratively, through explanatory method descriptions, analysis instructions or other governed semantic definitions. A fixed publication may already embody the results. Runtime may bind third-party APIs or shared analytic engines using PFI-approved golden paths.

A **generated API caller/adapter** may be part of the Product's executable realization; the externally operated API implementation is a separately governed dependency. Its invocation and provider-boundary evidence remain visible in the runtime account. The source code compiler, data processing platform, CPU, memory and network do not acquire Product identity merely because they enabled production or execution.

**Exception:** A self-contained Product may package an embedded execution component as a constituent; packaging alone still does not establish its Product Family. The Product Promise, PIN and applicable constitution decide.

## 7. Formal falsification experiments and supporting material

- [Case dispositions C01-C36](./p01-stage-02-case-disposition-ledger.md) state conditional inferences, strongest competitors and missing evidence.
- [Cross-enterprise PFI controlled experiments](./p01-stage-02-cross-enterprise-realization-tests.md) specify semantic equality, non-equivalence and execution-obligation fault injections.
- [Hypothesis disposition / S03 gates](./p01-stage-02-hypothesis-dispositions.md) identifies what Stage 2 eliminated and what Stage 3 must still establish.
- `research/p01-s02/cases.json`, `hypothesis-tests.json` and `research-decisions.json` are machine-readable **research ledgers**, not public specification schemas.

The repository checker verifies case/test inventory and decision traceability only. Passing it does not demonstrate semantic correctness, Product qualification or implementation conformance.

## 8. Stage 2 conclusion (proposed, awaiting owner review)

The `contains engine` versus `is Information` dichotomy is rejected. The leading approach is a **Product-qualified, governed informational value proposition** with an essential ability to supply that value and a **meaning-bearing semantic constitution**, realized by substitutable eligible mechanisms. No pure *necessary and sufficient* Info-versus-Data test is yet established for materially dual-promise offerings, and no standalone INFOPS qualification decision or conformance certificate is issued by S02.
