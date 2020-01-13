---
title: P01 Stage 2 - Cross-Enterprise PFI Experiments
sidebar_label: P01-S02 - PFI Experiments
---

# INFOPS-P01-S02 - Cross-enterprise realization and semantic-equivalence experiments

> **NON-NORMATIVE research protocol, not a completed benchmark.** No live HDIP deployments, actual PFI golden paths or runtime results were examined. Every numeric example is synthetic and exists to test the logical strength of Product-classification claims, not to certify a Product or a platform.

## 1. Subject and baseline intent

A candidate **Crypto Market Information Product** promises governed *market price-formation information* for selected crypto assets, exchanges and time windows. For the primary metric, assume its governing semantic definition explicitly requires **Volume-Weighted Average Price (VWAP)** from eligible executions within the specified event-time window, using a fixed currency and specified missing-data/source-quality treatment. The offering includes interpretive frame, market/source context rules, declared metric and precision requirements, applicable freshness constraints, eligible consumer interface and independent BPS Product qualification **as a test assumption only**.

We are testing **same intrinsic family/kind despite eligible realization differences**, NOT assuming the three enterprises share one governed Product instance, product owner, version, entitlements or regulatory posture.

### Controlled semantic inputs

```text
metric: VWAP
formula: sum(execution_price * executed_quantity) / sum(executed_quantity)
source eligibility: approved exchange execution events only
population: selected asset and included exchanges
window: [start_event_time, end_event_time) in UTC
meaning: trade-weighted executed price over the governed window
currency: a declared common denomination
undefined/zero-volume: explicitly governed error/empty outcome
```

**Two synthetic trades:** price 100, quantity 1; price 120, quantity 3. Correct governed VWAP = `(100*1 + 120*3)/(1+3) = 115`. An unweighted arithmetic mean = 110. The two methods may coincide in some inputs yet still differ in meaning. Thus numeric coincidence is not proof of semantic equivalence.

## 2. Enterprise implementations

| Layer | Enterprise A: materialized | Enterprise B: external math API | Enterprise C: optional AI explanation |
|---|---|---|---|
| Governing semantic promise | Same *hypothetical* VWAP informational proposition | Same *hypothetical* VWAP informational proposition | Same VWAP proposition; an AI Product may supply optional explanatory text only |
| PFI path | Generate batch/stream SQL plus materialization and serving | Generate runtime orchestration, API caller and capability binding | Generate governed analytical step plus AI Product invocation for supplementary explanation |
| Product realization | Compiled/declared query, scheduler, serving adapter | Request preparation, API adapter, typed dependency/error handling and serving adapter | Qualified metric calculation, AI-bound explanation step, evidence and serving adapters |
| External runtime/provider | Data processing engine, hosting, exchange feeds | Math API provider, hosting, exchange feeds | Separately governed AI Product runtime/provider, hosting, exchange feeds |
| Provider inside Product identity? | No by mere use | No; generated caller is realized behaviour, provider remains external | No; AIPS-qualified AI dependency does not change containing VBE merely by use |
| Same Product instance? | Not assumed | Not assumed | Not assumed |
| Evidence to collect | SQL version, source events, event-time rules, materialization/currentness | Method/schema/precision contract, provider identity/version, invocation, failures | AIPS qualification/currentness, AI contract, defined limits of explanatory text, source/version trace |

Same declared intent **plus eligible golden paths** does not prove compliance. Each enterprise must demonstrate the applicable Product Promise and semantics under its own obligations. It is acceptable for A, B and C to use different implementation details and still occupy the same Product Family/Kind, if independently qualified; it is also possible for one to fail operational contract without becoming a different Family.

## 3. Controlled experiments and expected reasoning

| Experiment | Intervention | Expected reasoned disposition | Identity / family consequence |
|---|---|---|---|
| **PFI-F1** | A/B/C calculate governed VWAP under equivalent semantic contracts using different runtime engines | `SUPPORTED_UNDER_PREMISES`: family invariance is compatible with three implementations; real equivalence still needs evidence | Different implementations do not *alone* create a different Product Family |
| **PFI-F2** | B's golden path silently replaces VWAP with simple arithmetic mean | `COUNTEREXAMPLE_TO_RULE`: an approved path is insufficient evidence of preserved semantics | Recompilation or contract breach; material semantic Product change may require version/identity reassessment |
| **PFI-F3** | A publishes every 300 seconds but Product Promise requires  < = 1 second freshness | `CONDITIONALLY_SUPPORTED`: operational nonconformance; does not automatically change intrinsic family | Contract/currentness failure, not automatic reclassification |
| **PFI-F4** | A and B both output 100 on data where all prices happen to be 100, but A calculates VWAP and B simple mean | `COUNTEREXAMPLE_TO_RULE`: a matching example cannot prove method semantics | Need semantic-spec comparison and differentiated input tests |
| **PFI-F5** | C's AI output shifts from ancillary explanation to autonomous trading strategies and consequential execution | `SEMANTIC_CHANGE`: changed value proposition and authority, not merely a PFI substitution | Re-evaluate actual Product subject, AIPS qualification and compound/decision boundaries |
| **PFI-F6** | B switches to another eligible math provider while keeping calculation and obligations equivalent | `SUPPORTED_UNDER_PREMISES`: provider identity changes, not intrinsically the Product Family | New Blueprint Binding/Compilation Record and dependency/version evidence; no automatic new Product Family |
| **PFI-F7** | Three enterprises separately own Products implementing the same semantic Product Kind | `IDENTITY_OR_OCCURRENCE`: family/type equivalence does not imply instance identity | Preserve separate Product, Product Owner, jurisdiction and version identifiers |
| **PFI-F8** | Generated API caller remains in B's executable, external API becomes unreachable | `CONDITIONALLY_SUPPORTED`: Product runtime behaviour/dependency is observable, provider implementation remains externally governed | Degradation/failure obligations apply; no automatic provider ownership or family transfer |
| **PFI-F9** | A materializes version 1 metric; current metric definition changes to version 2 and old outputs are queried | `IDENTITY_OR_OCCURRENCE`: reconstruct semantics from the applicable historical version, not latest lookup | Preserve Product/semantic version and historical meaning |
| **PFI-F10** | C generates a plausible but unsupported causal explanation despite correct VWAP | `CONDITIONALLY_SUPPORTED`: keeping the metric correct does not assure the full informational explanation | Fitness/trust/semantic obligations may fail; AI dependency does not settle family identity |

PFI-F1/F6 are **conditional demonstrations of logical invariance**. They are not empirical proofs that every implementation is eligible. F2/F4/F5 are decisive counterexamples to stronger, unsafe claims of golden-path authority, payload equivalence and family inheritance.

## 4. Definition, realization and execution evidence separation

**Semantic Definition Graph (GEARM):** Information Need, analytical intent, proposition identity/version, frame, subject/population/time context, governing VWAP logic, Product Promise and relevant authorities.

**PFI / HDIP-P2 realization evidence:** resolved inputs and Registry versions, Realization Plan, selected eligible Blueprint Binding, compiler/rule-set version and Compilation Record. PFI does not acquire Product-semantic or policy authority. M09 Realization Plan is not executable code by definition.

**Executable Product realization:** implementation of governed metric/formation logic, generated API callers/adapters, response validation, version/error handling and consumer-facing Product logic. Generated runtime invocation belongs to realization behaviour without being presupposed as a Product Owner's explicitly authored intent.

**External dependency and infrastructure:** hosted compute/storage/network, Math API implementation, AI runtime and source-feed provider are independently governed capabilities. They may be embedded or bundled if explicitly constituted, but mere hosting, execution or invocation is not identity transfer. M13 Runtime/Infrastructure and Product/Capability Provider boundary responsibilities remain applicable.

**Execution Evidence Graph (GEARM):** actual input event/semantic versions, method/compiled artifact/binding versions, provider response and failure evidence, time, output occurrences and consumer/decision-use references. Historical outputs must not be silently reinterpreted against newest semantics.

## 5. Property-based / metamorphic probes for a future HDIP-RI

These are planned **runtime tests** to execute against the later Reference Implementation, not tests executed during INFOPS-P01-S02:

- Preserve declared VWAP under equivalent implementations across unequal trade weights; assert for the synthetic example that the result is 115 and not 110.
- If every eligible execution quantity is multiplied by a common positive constant, VWAP should remain the same (holding all other governing rules constant).
- Changing eligible source population, event-time window boundary or price-denomination rules must be treated as semantic inputs, not unnoticed compiler defaults.
- Both the compiled implementation and runtime output must identify or permit reconstruction of the correct effective semantic-definition version.
- If a provider returns insufficient precision, silently interpolates missing events or alters currency, detect the deviation rather than declare semantic equivalence from plausible numeric values.
- If AI explanations are optional, check their governing relation to the original metric and their unsupported-claim/uncertainty handling independently of the metric computation.
- Demonstrate separate failure classification: (`INTRINSIC_FAMILY_UNCHANGED`, `PRODUCT_CONTRACT_NOT_MET`, `EXTERNAL_DEPENDENCY_FAILED`, `SEMANTIC_EQUIVALENCE_NOT_ESTABLISHED`). These are **research labels**, not HDIP/INFOPS normative status codes.
- Verify that an otherwise equivalent external provider change produces correct new bindings/evidence without automatically issuing a new Product-family classification.

## 6. Conclusion / open limits

Different enterprises can choose different PFI golden paths for the same governing intent **without requiring a new Product Family**. This is compatible with frozen HDIP M09/M13/M14. But a shared label or intent string does not establish Product-instance identity, contract satisfaction, semantic equivalence, trust or applicable policy compliance. Genuine semantic change and genuine compound/Product change remain subject to independent authority.

Cross-check [the S02 falsification method](./p01-stage-02-pin-differentiation-falsification.md), [36-case ledger](./p01-stage-02-case-disposition-ledger.md) and [S03 review gates](./p01-stage-02-hypothesis-dispositions.md).
