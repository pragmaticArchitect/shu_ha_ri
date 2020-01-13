---
title: P01 Stage 2 - Case Disposition Ledger
sidebar_label: P01-S02 - 36 Case Ledger
---

# INFOPS-P01-S02 - Case disposition and counterexample ledger

> **RESEARCH DRAFT / NON-NORMATIVE; all outcomes conditional.** These are **inferences from hypothetical stated subjects and assumptions**, NOT actual BPS or INFOPS Product qualification results. Stage 1's [C01-C18](./p01-stage-01-classification-cases.md) and [C19-C28](./p01-stage-01-realization-stress-tests.md) remain unchanged. C29-C36 are new falsification probes. Where a subject's actual Product Promise or BPS Productness is not given, final family membership is deliberately not decided.

## 1. How to read this ledger

- **PROVISIONAL_INFO_CANDIDATE**: facts, if proven, would justify evaluating INFOPS; never indicates qualification.
- **COMPETING_FAMILY**: stated primary VBE suggests a different family under its own governing specification.
- **PRODUCTNESS_NOT_SHOWN**: informational output or user interface is described, but an independently qualified Product subject is not evidenced.
- **BOUNDARY_UNRESOLVED**: materially different Product Promises or constitutions remain consistent with the available facts.
- **INVARIANCE_SUPPORTED**: changing representation, production or realization alone does not establish family change; says nothing about run-time conformance.
- **SEMANTIC_CHANGE**: change in governing meaning or promise must be assessed rather than treated as a technical substitution.
- **IDENTITY_OR_OCCURRENCE**: identity, semantic version, realization and output occurrence need separation.

These `researchDisposition` labels are local review vocabulary only; they are not INFOPS certification statuses and have no standing in BPS, AIPS, DPDS or DPROD.

## 2. Original classification challenge cases (C01-C18)

| Case | S02 conditional inference | Disposition | Key evidence still required |
|---|---|---|---|
| **C01** Governed Payment Lifecycle dataset | A promise of trusted state/event representation principally supports a **Data Product** investigation; timestamps/context alone do not make it Information | `COMPETING_FAMILY` | BPS Productness and actual external Data Product qualification |
| **C02** Dataset with settlement-duration and corridor measures | Derived metrics could be constituents of a Data Product, or support a different productized informational proposition | `BOUNDARY_UNRESOLVED` | Primary Product Promise, semantic intent and constituting relationship to each measure |
| **C03** One-off internal KPI dashboard | A chart can be meaningful Information without evidence that the chart/occurrence is itself a Product | `PRODUCTNESS_NOT_SHOWN` | Product identity, owner, promise, lifecycle and independent BPS Productness |
| **C04** Reusable corridor-performance subscription | Bounded settlement-performance proposition is a plausible Info VBE, if intentional Productness and governed semantics are established | `PROVISIONAL_INFO_CANDIDATE` | Promise, semantic methods, source eligibility, consumer contract, Product version |
| **C05** Versioned analytical PDF brief | Fixed delivery format and lack of a running analytical engine do not disqualify a potentially qualified informational offering | `PROVISIONAL_INFO_CANDIDATE` | Distinguish published Product edition from one-off PDF artifact; Productness/semantic governance |
| **C06** Human-curated market interpretation | Human curation can constitute meaningful Information without engine ownership | `PROVISIONAL_INFO_CANDIDATE` | Interpretive frame, method, evidence, bounded promise and Productness |
| **C07** BI tool offering arbitrary calculations | A generic calculation/visualization capability does not automatically have an informational VBE | `COMPETING_FAMILY` | Actual promise; is the subject a tool/service or a specifically constituted informational product? |
| **C08** AI Product summarizes settlement metrics | AI dependency does not classify the containing output; one-off summary need not be a Product | `BOUNDARY_UNRESOLVED` | Subject identity and whether anything new is intentionally productized |
| **C09** Governed AI inference service | If intrinsic promise is a qualified intelligence capability, AIPS is a stronger family authority | `COMPETING_FAMILY` | Independent AIPS qualification and precise Product Promise |
| **C10** Threshold-driven late-settlement alert | Information occurrence, recommendation, decision and action must be separated | `BOUNDARY_UNRESOLVED` | Owner/actor/authority, alert Productness, semantic contract and downstream authorization |
| **C11** Information offering consuming another Information Product | A distinct bounded informational promise is possible without inheriting upstream identity | `PROVISIONAL_INFO_CANDIDATE` | New Product Promise, constitution, differentiated informational value and identity |
| **C12** Metric + explanation + simulation | Could be one coherent Info proposition family, a platform/service or a real compound Product | `BOUNDARY_UNRESOLVED` | Boundedness/coherence, primary VBE, distinct component promises |
| **C13** Refreshing fraud-monitoring report with AI inputs | Neither refresh pattern nor AI dependency alone determines family; a bounded interpreted report is plausible | `PROVISIONAL_INFO_CANDIDATE` | Promise, semantic context, AIPS dependency currentness, Productness |
| **C14** Ad hoc direct analytical consumption | GEARM/GEARA allow direct consumption without Productization | `PRODUCTNESS_NOT_SHOWN` | Separate intentional qualified Product identity, if asserted |
| **C15** Same metrics/ports with different semantics | Identical payload does not establish same informational meaning or Product version | `SEMANTIC_CHANGE` | Population, period, method, relevant definition/authority versions |
| **C16** Historical report after metric change | Historical meaning belongs to the definition/occurrence-time evidence, not the newest metric definition | `IDENTITY_OR_OCCURRENCE` | Referenced historical semantic version and effective period |
| **C17** Marketplace chart with high maturity | Listing and maturity cannot create either Productness or Information family membership | `PRODUCTNESS_NOT_SHOWN` | Independent BPS Product evidence and PIN analysis; PMDD assessed later |
| **C18** Commercial bundle: feed + analysis + AI recommendations | A commercial bundle need not give each component a common intrinsic Product Family | `BOUNDARY_UNRESOLVED` | Which subject is qualified: bundle, constituent Product, or composite with a new promise? |

## 3. Additional Stage 1 stress cases (C19-C28)

| Case | S02 conditional inference | Disposition | Key evidence still required |
|---|---|---|---|
| **C19** Published annual research analysis | A stable, intentionally Productized governed interpretation can be an Info candidate even after authoring machinery has gone | `PROVISIONAL_INFO_CANDIDATE` | BPS Productness; method/frame/context; versioned editorial controls |
| **C20** Generic mathematical / analytics API | Offering compute without a bounded informational promise suggests a generic capability/service, not Information merely because it returns numbers | `COMPETING_FAMILY` | Actual VBE/EVC and specified service terms |
| **C21** Data Product with VWAP and semantic metadata | Even extensive analytical calculations are not sufficient to replace a Data-representation Product Promise | `BOUNDARY_UNRESOLVED` | Governing primary promise and external Data Product requirements |
| **C22** Same Crypto Market Info intent, three enterprises | PFI engine/topology/API/AI differences alone cannot reclassify a Product; semantics/currentness must be verified separately | `INVARIANCE_SUPPORTED` | Contract-normalized semantic equivalence, identity/versions and realization evidence |
| **C23** AI-powered/AI-created Comic, Movie, Car or Rocket | Use, containment or AI-origin does not automatically change primary intrinsic VBE/EVC | `INVARIANCE_SUPPORTED` | PIN of each actual containing Product, not just AI dependency labels |
| **C24** Market information promise changes into trading intelligence | Real change of primary promised value requires requalification; cannot hide it as a new AI golden path | `SEMANTIC_CHANGE` | Versioned new promise, AIPS qualification, possible compound/Product identity decision |
| **C25** Repository, build archive and multiple deployments | Implementation representations do not automatically constitute separate Product identities or the full Product | `IDENTITY_OR_OCCURRENCE` | Logical Product identity, artifacts, builds, deployments and occurrence links |
| **C26** External mathematics API in Info Product runtime | Generated caller belongs to executable realization; external API remains separately owned; invocation remains a governed boundary | `INVARIANCE_SUPPORTED` | Blueprint Binding, API capability/contract version, semantics and trace evidence |
| **C27** Same numeric values, different populations or periods | Payload equality cannot override differences in governing informational meaning | `SEMANTIC_CHANGE` | Semantic definition identities, effective periods and population/time rules |
| **C28** Different asset/time parameters for one Product | Valid runtime parameter variation need not create a new Product version or family | `IDENTITY_OR_OCCURRENCE` | Parameter contract, allowed context range, identity invariants |

## 4. New deliberate counterexamples (C29-C36)

| Case | Explicit hypothetical premises and observation | Disposition | Falsification target |
|---|---|---|---|
| **C29** Governance-free AI-generated market narrative | A convincing narrative is produced but no Product subject, applicable information frame, source rules or logic/meaning authority is evidenced. Informational content by itself cannot certify Information Productness | `PRODUCTNESS_NOT_SHOWN` | Context alone versus Productness, H01/H03/H05 |
| **C30** Static governed information edition; engine retired | A specific versioned published market-analysis Product continues to offer its promised report after the historical authoring tools are gone | `INVARIANCE_SUPPORTED` | Refutes universal own-engine/active-execution requirement, H03/H10 |
| **C31** A subscription bundling information and autonomous trade execution | If it independently promises interpreted market information **and** governed consequential trading capability, treating it as an uncomplicated single-family Information Product is unjustified | `BOUNDARY_UNRESOLVED` | Compound/changed essential value, H01/H04/H05 |
| **C32** Same bounded analytical publication delivered by PDF or API | If the same versioned promise/meaning is preserved, replacing the interface does not change intrinsic family | `INVARIANCE_SUPPORTED` | Delivery-medium sufficiency, H02/H10 |
| **C33** AI-generated explanation supplements governed VWAP | If metric and information promise are unchanged, an independently qualified AI dependency does not automatically transform the containing Product into an AI Product | `INVARIANCE_SUPPORTED` | Non-transitivity, H04/H07 |
| **C34** PFI replaces specified VWAP with a different estimator | Even if the outputs are numerically close in one test, changing the governing analytical calculation is not proven equivalent and may breach the Product Promise | `SEMANTIC_CHANGE` | PFI semantic authority, H03/H05/H07/H09 |
| **C35** Same spec independently owned by three enterprises | Independent Product identities can implement the same semantic Product Kind and intent. Same Family/Kind is not instance identity | `IDENTITY_OR_OCCURRENCE` | Cross-enterprise identity, H06/H10 |
| **C36** A shared runtime serves ten informational Products | One execution engine and shared deployment do not collapse ten separately promised and owned informational Products into a single Product | `INVARIANCE_SUPPORTED` | Hosting/realization conflation, H09/H10 |

## 5. What S02 has *not* proven

The inventory is intentionally richer than the available independent Product evidence. It does not establish that any real product satisfies BPS Productness or all requirements of external Data Product/AIPS specifications. In particular, C02/C21 remain unresolved without primary Product Promise and family-qualification evidence; C12/C31 remain unresolved where several distinct essences are material; and the threshold for a sufficiently **bounded/coherent proposition family** remains unsettled.

The next stage must review these cases with governed input facts and adjudication criteria, not merely convert provisional outcomes to `PASSED` because they appear in this table. See the [S02 methodology](./p01-stage-02-pin-differentiation-falsification.md) and [S03 open gates](./p01-stage-02-hypothesis-dispositions.md).
