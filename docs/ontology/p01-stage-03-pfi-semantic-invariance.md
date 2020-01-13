---
title: P01 Stage 3 - PFI Semantic Invariance Protocol
sidebar_label: P01-S03 - PFI Invariance
---

# INFOPS-P01-S03 - PFI realization and semantic-invariance protocol

> **RESEARCH / NON-NORMATIVE.** This is a proposed falsification protocol; it does not execute a genuine HDIP PFI golden path and confers no family qualification, conformance, entitlement or publication approval. It extends [S02 cross-enterprise thought experiments](./p01-stage-02-cross-enterprise-realization-tests.md).

## 1. The governing statement

> A Product Owner governs what value a Product promises; PFI industrializes how that value can be realized through eligible golden paths. Neither the machinery chosen nor the enterprise hosting it should arbitrarily redefine the Product's intrinsic nature.

To test this, keep the **governing informational Promise and semantic obligations** fixed while changing the eligible *implementation*. This is an experiment in classification invariance, not in assuming identical instances across enterprises.

## 2. Controlled three-enterprise example

**Subject:** a hypothetical Crypto Market Price Formation Information Product Kind. The Owner specifies eligible market inputs, window meanings, calculation semantics (for example a declared VWAP method), the interpreted informational proposition, context applicability, freshness and consumer constraints. Each enterprise independently establishes its Product identity and other locally applicable governing obligations.

| Variable | Enterprise A | Enterprise B | Enterprise C |
|---|---|---|---|
| PFI golden path | Batch/stream materialization | Generated adapter + approved mathematics API | Governed analytical formation with qualified AI Product dependency |
| Value delivery | Versioned precomputed subscription | On-demand or windowed request | AI-assisted commentary accompanying governed measures |
| Runtime provider | Shared processing/storage | External math service and host runtime | Separate AI runtime plus analytical capability |
| Must preserve | Method, context, informational Promise and applicable freshness | Same as A, including provider error/precision constraints | Same as A for governed informational proposition; AI commentary must not silently alter methodology |
| Distinct accountable data | Enterprise Product identity, dependencies, contract/evidence, local controls | Same | Same, plus AIPS dependency/currentness evidence |

If the same **primary informational VBE and EVC** are preserved, these paths may realize the same intrinsic Information Product Kind. They are *not necessarily one Product instance*, and may have different maturity, assurance or authorization states.

## 3. Experimental controls

- **C1 — Exact subject:** compare a Product Kind/semantic Promise across independent Product identities, *or* multiple realizations of one Product Version; never silently switch the identity being classified.
- **C2 — Governing semantic identity:** pin metric definitions, units, calculation method, window boundaries, aggregation/weighting, eligible inputs, exclusions, population, interpretation, assumptions and applicable effective periods.
- **C3 — Product Promise:** hold intrinsic promised value fixed; preserve relevant consumer contract, including correctness/accuracy, applicability, currentness and permitted use.
- **C4 — Substitutable implementation:** vary code, data stores, analytical engine, API caller, provider, AI support and topology through independently approved PFI golden paths.
- **C5 — Evidence:** retain resolved intent, authoritative semantic references, compilation rule and golden-path versions, dependencies, provider binding, generated executable interface, runtime observations, exceptions and applicable governance approvals.
- **C6 — Independent judgments:** record Productness, intrinsic family, contract conformance, provider eligibility, decision/action authorization and PMDD separately.

HDIP-M09 provides Realization Plan, Blueprint Binding and Compilation Record concepts; HDIP-M13 preserves external runtime/provider boundaries; HDIP-M14 separates logical architecture from Realization Units and topology. The PFI does not become semantic authority by producing a working executable.

## 4. Negative controls and expected interpretations

| Control experiment | Technical variation | Meaning/conformance finding | Family inference |
|---|---|---|---|
| **P-S03-01** | Local prescribed VWAP vs mathematically equivalent external API | Candidate semantic equivalence if source, precision, method, error policy and periods satisfy terms | Family invariance may hold |
| **P-S03-02** | Same specified VWAP realized with batch/stream materialization | If freshness obligation is violated, operational nonconformance | Intrinsic family need not change |
| **P-S03-03** | Replace specified VWAP with simple moving average | Meaning changed even if sample values happen to coincide | Semantic/Product evolution review, not automatic new AI/Data kind |
| **P-S03-04** | Substitute market population/time-window boundary | Same numeric payload possible; definition no longer equivalent | Semantic-change review |
| **P-S03-05** | AI model provides commentary but governed measure remains unchanged | AI dependency included with separate authority/lineage | No automatic AI Product-family inheritance |
| **P-S03-06** | Autonomous trade execution becomes a new primary Promise | Material new intelligence/action proposition and authorization boundary | Requalify Product/compound claim |
| **P-S03-07** | Shared engine hosts ten distinct Information Products | Deployment consolidation, Product identities/contracts remain distinct | No merger of Products based on engine |
| **P-S03-08** | Three enterprises realize an equivalent Product Kind independently | Implementation and ownership differ | Same kind possible, not same Product identity |

The table expresses **expected logical findings**, not results observed from deployed systems. A future reference implementation should instantiate and measure these as executable tests, with negative cases showing precisely where equivalence or conformance fails.

## 5. Two meanings of “equivalent”

- **Semantic equivalence:** realized outputs have the governing interpretation intended by the Product Promise for equivalent eligible inputs and contexts. Numeric closeness alone is not enough.
- **Contract conformance:** the realization additionally satisfies all applicable consumer, governance, security, freshness, quality, provider, resilience and assurance obligations. Semantic equivalence does not by itself prove operational conformance.

A semantically faithful implementation failing a specified freshness requirement should not silently become a different Product Family. A different analytical meaning must not be hidden behind a successful throughput/SLA result.

## 6. Boundary record for generated API invocation

A PFI-selected golden path may generate code that invokes a mathematics API. The **generated invocation behaviour** belongs to the Product's executable realization. The **external API implementation/provider** remains a dependency with a separate identity, contract and operational boundary. The API provider, compiler, code executor, compute/memory/network resources and shared analytical engine are **not made constituents of the Product's intrinsic identity merely by invocation/hosting**.

The actual location of an embedded runtime/library inside a delivered artifact depends on the chosen Product constitution. Avoid the opposite overreach of declaring that no executable dependency can ever be packaged within any Product.

## 7. Decision rule for the experiment

```text
Implementation changed, governing meaning preserved, Product Promise preserved
    -> do not infer a new Product Family from PFI substitution.

Implementation changed, meaning-affecting rule or primary Promise changed
    -> re-open semantic / Product Version / Product-family review.

Implementation preserved meaning, but violates an operational obligation
    -> record realization/contract failure independently of intrinsic classification.

AI involved only as source, production tool or dependency
    -> no automatic transfer of AIPS AI Product identity to the containing Product.
```

Cross-reference [candidate rules](./p01-stage-03-candidate-qualification-rules.md), [casework](./p01-stage-03-boundary-casework.md) and [S03 open decisions](./p01-stage-03-review-decisions.md).
