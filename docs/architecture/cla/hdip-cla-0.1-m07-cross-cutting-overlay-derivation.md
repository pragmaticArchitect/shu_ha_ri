---
id: hdip-cla-0.1-m07-cross-cutting-overlay-derivation
title: HDIP-CLA 0.1 M07 - Cross-Cutting Overlay Derivation
sidebar_label: M07 - Cross-Cutting Overlays
---

# HDIP-CLA 0.1 M07 - Cross-Cutting Overlay Derivation

**Status:** COMPLETE

## 1. Purpose

M07 derives and freezes the canonical cross-cutting Overlay model for the **Holistic Data, Information and Intelligence Platform (HDIP)**.

M06 froze five logical responsibility Planes and one Shared Platform / Utility Foundation. M07 now answers the complementary question:

> **Which recurring obligations must remain visible across those Planes because localizing them into one Plane would weaken governance, security, evidence, quality, assurance, lifecycle, resilience or economic accountability?**

M07 is an architecture-responsibility stage. An Overlay is **not** a mandatory centralized service, platform, database, team or control function. It is an orthogonal responsibility lens that applies wherever its concern is material.

M07 evaluates the nine candidates carried forward by M06:

```text
RCF-04  Governance, Policy, Control & Compliance
RCF-05  Security, Privacy, Identity & Entitlement
RCF-19  Provenance, Evidence & Traceability
RCF-20  Observability, Telemetry & Auditability
RCF-21  Quality, Fitness & Trust Evidence
RCF-22  Evaluation & Assurance
RCF-23  Lifecycle, Version, Currentness & Change
RCF-25  Resilience, Safety, Failure & Recovery
RCF-30  Cost & Economic Accountability
```

All nine pass the M07 admission test and are frozen as independent canonical HDIP Overlays.

---

## 2. Overlay admission model

A candidate is admitted as a canonical Overlay only where all of the following are true:

1. **Cross-Plane relevance** - the responsibility materially applies across several HDIP Planes rather than having one natural exclusive Plane home.
2. **Orthogonality** - the concern constrains or qualifies Plane behavior rather than replacing the Plane's primary responsibility.
3. **Independent architectural meaning** - collapsing it into another concern would weaken a material M04/M05 distinction.
4. **Topology independence** - the responsibility remains valid whether realized centrally, federated, distributed, embedded or through several implementations.
5. **Source traceability** - the concern is supported by the M02 upstream corpus, an explicit HDIP requirement, or both.
6. **No service presumption** - the Overlay remains useful even when no standalone component with the same name exists.
7. **No authority capture** - the Overlay may coordinate, evaluate, enforce or evidence obligations without inheriting external semantic, Product, policy, Data or Decision authority.
8. **No Profile-only leakage** - a concern that is intrinsically limited to a Data-, Information- or Intelligence-specific profile is not generalized into core merely for symmetry.

An Overlay may therefore be logically mandatory while its concrete realization remains distributed.

---

## 3. Candidate disposition

| M06 candidate | M07 result | Rationale |
|---|---|---|
| **RCF-04 Governance, Policy, Control & Compliance** | **ADMIT** | Governing applicability, control, compliance, exception and accountability obligations span design, realization, runtime, consumption and evolution. |
| **RCF-05 Security, Privacy, Identity & Entitlement** | **ADMIT** | Protection and entitlement are not merely P4 access concerns; they constrain intent, discovery, runtime, provision and evidence. |
| **RCF-19 Provenance, Evidence & Traceability** | **ADMIT** | Historical reconstruction and evidence correlation span the complete architecture and must remain distinct from telemetry. |
| **RCF-20 Observability, Telemetry & Auditability** | **ADMIT** | Operational visibility spans realization, runtime, serving and evolution and supports—but does not equal—provenance or assurance. |
| **RCF-21 Quality, Fitness & Trust Evidence** | **ADMIT** | Quality and fitness evidence is required across domains, while typed metrics and contextual trust must remain distinguishable. |
| **RCF-22 Evaluation & Assurance** | **ADMIT** | Evaluation and assurance cross lifecycle phases and consume several evidence types; they cannot safely be reduced to Quality or Governance alone. |
| **RCF-23 Lifecycle, Version, Currentness & Change** | **ADMIT** | Version/currentness/change obligations apply to semantics, Products, contracts, policies, projections, runtime realizations and evidence across all Planes. |
| **RCF-25 Resilience, Safety, Failure & Recovery** | **ADMIT** | Resilience and failure-management obligations span design through evolution; safety remains typed/profile-sensitive rather than genericized. |
| **RCF-30 Cost & Economic Accountability** | **ADMIT** | Economic feasibility, resource attribution, consumer accountability and cost evidence span realization, runtime, consumption and value assessment while remaining distinct from Value. |

### 3.1 Why nine is the minimum defensible set

Some candidates could be implemented through shared tooling, but M05 separation locks prevent semantic collapse:

```text
Provenance / Evidence        != Observability / Telemetry
Quality / Trust / Fitness    != Evaluation / Assurance
Cost                         != Usage != Outcome != Value
Identity                     != Authority != Entitlement
Policy authority             != Policy resolution != Enforcement
```

Combining those concerns into fewer Overlay identities would make the architecture less precise even if one implementation later co-realizes them.

---

# 4. Canonical HDIP Overlay catalogue

M07 freezes nine canonical HDIP-CLA 0.1 Overlays:

| ID | Canonical Overlay | Principal RCF |
|---|---|---|
| **HDIP-X1** | **Governance, Policy, Control & Compliance** | RCF-04 |
| **HDIP-X2** | **Security, Privacy, Identity & Entitlement** | RCF-05 |
| **HDIP-X3** | **Provenance, Evidence & Traceability** | RCF-19 |
| **HDIP-X4** | **Observability, Telemetry & Auditability** | RCF-20 |
| **HDIP-X5** | **Quality, Fitness & Trust Evidence** | RCF-21 |
| **HDIP-X6** | **Evaluation & Assurance** | RCF-22 |
| **HDIP-X7** | **Lifecycle, Version, Currentness & Change** | RCF-23 |
| **HDIP-X8** | **Resilience, Safety, Failure & Recovery** | RCF-25 |
| **HDIP-X9** | **Economic & Cost Accountability** | RCF-30 |

The canonical structural model is therefore:

```text
                    Orthogonal Product Lens
          BPS/PIN + Product-family specifications
  -----------------------------------------------------

 P1 Governed Intent, Definition & Authority Context
 P2 Discovery, Composition & Realization
 P3 Runtime, Formation & Execution
 P4 Provision, Consumption & Integration
 P5 Outcome, Value & Evolution

  -----------------------------------------------------
      X1 Governance, Policy, Control & Compliance
      X2 Security, Privacy, Identity & Entitlement
      X3 Provenance, Evidence & Traceability
      X4 Observability, Telemetry & Auditability
      X5 Quality, Fitness & Trust Evidence
      X6 Evaluation & Assurance
      X7 Lifecycle, Version, Currentness & Change
      X8 Resilience, Safety, Failure & Recovery
      X9 Economic & Cost Accountability
  -----------------------------------------------------
        HDIP-FND Shared Platform / Utility Foundation
```

This is a logical architecture view. It does not imply nine centralized cross-cutting platforms or one implementation component per Overlay.

---

# 5. HDIP-X1 - Governance, Policy, Control & Compliance

## 5.1 Purpose

X1 preserves the applicability, orchestration, execution context, exception handling and evidence obligations required to operate HDIP under governed policy and control without making HDIP the authority for every underlying policy.

X1 includes, where applicable:

- governing requirement and policy applicability;
- policy/reference version resolution;
- control obligation and control-point coordination;
- compliance and regulatory constraint propagation;
- exception, waiver and escalation handling;
- segregation-of-duties requirements;
- accountable approval/judgement where machine determination is insufficient;
- control execution/result evidence linkage;
- change propagation when governing obligations change.

## 5.2 Boundaries

```text
Policy authority
      !=
Policy applicability / resolution
      !=
Policy compilation
      !=
Runtime enforcement
      !=
Control Evidence
```

X1 may co-realize these responsibilities but SHALL preserve their identities and upstream authority.

---

# 6. HDIP-X2 - Security, Privacy, Identity & Entitlement

## 6.1 Purpose

X2 establishes cross-cutting responsibility for protecting participants, data, information, intelligence, interfaces and evidence while controlling who or what may act or consume for an applicable purpose.

X2 includes, where applicable:

- identity and workload/actor identity context;
- authentication;
- authorization and entitlement enforcement for access/operation;
- purpose limitation;
- privacy and confidentiality requirements;
- minimization and exposure shaping;
- secrets/key and protection requirements;
- sensitive metadata/evidence protection;
- security event and access evidence linkage.

## 6.2 Boundaries

```text
Identity != authority != ownership != entitlement

Authentication != Authorization

Access Authorization != consequential Decision/Action Authorization
```

HDIP-FND may provide IAM, secrets or key-management mechanisms; those mechanisms do not become the authority for the policies or mandates X2 enforces.

---

# 7. HDIP-X3 - Provenance, Evidence & Traceability

## 7.1 Purpose

X3 preserves the evidentiary chain needed to explain what definitions, versions, dependencies, policies, actors, realizations, executions, consumption events and outcomes materially participated in an HDIP occurrence.

X3 includes, where applicable:

- source and definition provenance;
- dependency and lineage evidence;
- compilation/resolution evidence;
- deployment/realization evidence;
- execution evidence;
- consumption and access evidence;
- policy/control evidence references;
- Decision/Action evidence references where applicable;
- outcome/evolution evidence correlation;
- historical reconstruction across versioned artifacts.

## 7.2 Boundaries

```text
Provenance != dependency
Provenance != operational telemetry
Evidence presence != correctness
Evidence presence != assurance
Control Evidence != generic observability signal
```

X3 is evidence architecture, not a claim that one universal evidence store or graph must exist.

---

# 8. HDIP-X4 - Observability, Telemetry & Auditability

## 8.1 Purpose

X4 provides operational visibility into HDIP realization and operation so behavior, state, performance, failure and material interactions can be detected, inspected and reconstructed at the appropriate level.

X4 includes, where applicable:

- operational metrics;
- logs and events;
- traces/correlation identifiers;
- runtime and interface health;
- latency/throughput/error/degradation signals;
- consumption/usage telemetry;
- control/quality execution telemetry;
- alerting and operational diagnostics;
- auditability support through retained and correlated operational records.

## 8.2 Boundaries

Observability may produce evidence consumed by X3, X5 and X6, but:

```text
observable != correct
observable != governed-current
observable != trusted
observable != assured
observable != valuable
```

X4 therefore remains distinct from Provenance/Evidence, Quality/Trust, Evaluation/Assurance and P5 Value.

---

# 9. HDIP-X5 - Quality, Fitness & Trust Evidence

## 9.1 Purpose

X5 provides a common architecture for expressing, evaluating and exposing quality and fitness evidence without pretending that one metric applies uniformly across Data, Information, AI, Products or consumption contexts.

X5 includes, where applicable:

- Data quality evidence;
- semantic quality evidence;
- analytical/Information quality evidence;
- AI/model/output quality evidence;
- Product/Port quality evidence;
- freshness/completeness/accuracy/uncertainty or applicable domain dimensions;
- known limitations;
- purpose-specific Fitness for Use evidence;
- trust evidence exposed to Consumers and assurance functions.

## 9.2 Boundaries

```text
Quality evidence != trust conclusion
Trust evidence   != Fitness for Use
Fitness for Use  != Assurance Finding
```

Core HDIP SHALL NOT require a universal opaque `trust score` that hides the underlying evidence, context or domain-specific measures.

---

# 10. HDIP-X6 - Evaluation & Assurance

## 10.1 Purpose

X6 provides cross-cutting architecture for testing, evaluating and forming accountable assurance conclusions about whether an HDIP use, realization, Product/capability or operational state satisfies applicable requirements.

X6 includes, where applicable:

- design-time validation/evaluation requirements;
- test, simulation and evaluation evidence;
- control-effectiveness evaluation;
- Product/capability readiness assessment;
- runtime/post-runtime evaluation where required;
- analytical and AI-specific evaluation integration;
- assurance findings and conditions;
- independent review/judgement where required;
- reassessment triggers following material change.

## 10.2 Boundaries

```text
Evaluation != Assurance
Test pass  != blanket approval
Telemetry  != Assurance Finding
Quality score != Assurance Finding
```

Evaluation may be automated where safe; accountable assurance judgement SHALL remain explicit where requirements cannot be determined mechanically.

---

# 11. HDIP-X7 - Lifecycle, Version, Currentness & Change

## 11.1 Purpose

X7 preserves explicit lifecycle and version semantics across the independent artifacts and responsibilities that HDIP composes.

X7 includes, where applicable:

- stable identity and version;
- lifecycle state;
- governed currentness/eligibility;
- compatibility;
- supersession and revocation;
- deprecation/retirement;
- migration and rollback;
- change-impact propagation;
- historical interpretability;
- evolution/re-entry triggers.

## 11.2 Boundaries

HDIP SHALL preserve typed lifecycle dimensions such as:

```text
semantic version
Product / Product-Version state
contract/interface version
process/logic version
realization/deployment version
policy/control version
projection/compiler version
assurance/evidence version
```

and SHALL preserve:

```text
newest/latest != governed-current != eligible for use
```

Later change must not rewrite the state that governed a historical occurrence.

---

# 12. HDIP-X8 - Resilience, Safety, Failure & Recovery

## 12.1 Purpose

X8 provides cross-cutting responsibility for designing, detecting, managing and recovering from failures or unsafe/degraded operating conditions without treating every domain's failure semantics as identical.

X8 includes, where applicable:

- resilience requirements and operating envelopes;
- dependency and failure-mode analysis;
- degraded-operation behavior;
- retry/replay/idempotency expectations where applicable;
- fallback and continuity patterns;
- failure isolation and containment;
- recovery and restoration;
- fail-safe or human intervention requirements where applicable;
- resilience/failure evidence and post-incident learning.

## 12.2 Boundaries

```text
service resilience != Data quality
service resilience != analytical validity
service resilience != AI safety
failure recovery   != historical erasure
```

AI safety, consequential-action safety and other domain-specific safety semantics remain Profile/specialization concerns even when X8 provides common resilience architecture.

---

# 13. HDIP-X9 - Economic & Cost Accountability

## 13.1 Purpose

X9 makes the economic consequences of HDIP realization and consumption visible without confusing cost with usage, outcome or intrinsic/realized value.

X9 includes, where applicable:

- design/realization cost constraints;
- cost-feasibility evidence during composition/blueprint selection;
- runtime resource-consumption economics;
- consumer/domain/product cost attribution;
- showback/chargeback support where adopted;
- heavy-consumer accountability;
- economic thresholds/budgets/guardrails;
- cost trend and anomaly evidence;
- cost evidence supplied to P5 value/evolution assessment.

## 13.2 Boundaries

```text
usage != cost
cost  != outcome
cost  != value
high cost != low value automatically
low cost  != high value automatically
```

X9 supplies economic evidence and accountability; P5 remains responsible for Outcome/Value/Evolution interpretation.

---

# 14. Cross-Plane applicability model

An Overlay is applied **where material**, not as a checkbox attached blindly to every box. The matrix below describes the expected participation pattern.

Legend:

- **P** - principal/material participation is normally expected;
- **C** - contextual participation depending on subject/risk/use;
- **—** - no generic expectation (profiles may still add one).

| Overlay | P1 | P2 | P3 | P4 | P5 |
|---|:---:|:---:|:---:|:---:|:---:|
| **X1 Governance, Policy, Control & Compliance** | P | P | P | P | P |
| **X2 Security, Privacy, Identity & Entitlement** | P | P | P | P | C |
| **X3 Provenance, Evidence & Traceability** | P | P | P | P | P |
| **X4 Observability, Telemetry & Auditability** | C | P | P | P | P |
| **X5 Quality, Fitness & Trust Evidence** | P | P | P | P | P |
| **X6 Evaluation & Assurance** | P | P | C | C | P |
| **X7 Lifecycle, Version, Currentness & Change** | P | P | P | P | P |
| **X8 Resilience, Safety, Failure & Recovery** | P | P | P | P | P |
| **X9 Economic & Cost Accountability** | C | P | P | P | P |

The matrix does not mean every implementation must instantiate nine separate mechanisms at each Plane. It states where architectural obligations must be considered and traced when applicable.

---

# 15. Concerns deliberately not admitted as additional Overlays

## 15.1 Interoperability, Contracts & Semantic Compatibility

M05 identified interoperability/contracts/semantic compatibility as strongly cross-cutting. M07 does **not** admit a tenth Overlay for it.

The concern already has two better architectural homes:

1. **P2** owns discovery/composition compatibility and validation responsibilities; and
2. **M12** will define material inter-Plane Interaction Contracts, including versioning, semantic compatibility and authority/evidence propagation obligations.

Creating an Interoperability Overlay as well would duplicate those responsibilities and weaken boundary clarity.

## 15.2 Product

Product remains an orthogonal BPS/PIN and Product-family lens across P1-P5. It is not an Overlay and not a Plane.

## 15.3 Registry

Registry is a logical cross-Plane infrastructure responsibility deferred to M09. Registry participation is not itself a governance or lifecycle Overlay.

## 15.4 Utility/Foundation

Compute, storage, network, runtime hosting, messaging, IAM mechanisms, telemetry transport and similar mechanisms remain **HDIP-FND**, not an Overlay.

## 15.5 Outcome / Value

Outcome, realized usefulness and value interpretation remain the primary responsibility of **HDIP-P5**. X9 supplies cost evidence; X4 supplies telemetry; X5/X6 supply quality/assurance evidence. Those do not replace P5.

## 15.6 Consequential Decision / Action / Human Oversight

These remain Intelligence/regulated-use specializations around the P4 integration boundary and applicable Profiles. They are not generalized into a universal HDIP Overlay.

---

# 16. Relationship to existing HDIP constructs

### 16.1 Historical Governance Plane

The historical Governance Plane is now replaced architecturally by several explicit cross-cutting responsibilities, principally X1, X2, X3, X5, X6 and X7. A future diagram may visually group them, but no single `Governance Plane` owns every concern.

### 16.2 COVP

M07 completes the COVP decomposition begun in M05/M06:

```text
Observability     -> HDIP-X4
Cost              -> HDIP-X9
Value / Outcome   -> HDIP-P5
```

A consumer experience may present these together, but the architecture no longer treats `COVP` as one canonical responsibility type.

### 16.3 PDEP

PDEP traverses P1-P5 and applies relevant X1-X9 obligations at each lifecycle stage. The Overlay model does not create extra PDEP stages; it qualifies how existing lifecycle responsibilities are governed, evidenced, secured, evaluated, versioned, made resilient and economically accountable.

### 16.4 SSCF and CEP

SSCF/CEP consumption experiences primarily traverse P2/P4/P5 but remain subject to applicable X1-X9 responsibilities, especially entitlement, evidence, trust/fitness, lifecycle/currentness and economic accountability.

---

# 17. Source architecture traceability

M07 is not a copy of any source Overlay/Fabric model. It composes evidence from all three reference architectures.

## 17.1 GEDRA

GEDRA's Cross-Cutting Governance & Control responsibility supplies strong evidence for policy/control, privacy/security, quality, evidence, lifecycle and exception handling. GEDRA's Value/Observability/Feedback and Technology/Utility responsibilities additionally support X4, X8 and X9. M07 decomposes these concerns more finely because HDIP spans Data, Information and Intelligence and because M05 separation locks require explicit non-collapse.

## 17.2 GEARA

GEARA's five Fabrics map as follows:

| GEARA Fabric | HDIP treatment |
|---|---|
| Governance / Policy / Assurance | **X1 + X6** |
| Security / Privacy / Entitlement | **X2** |
| Provenance / Evidence / Observability | **X3 + X4** |
| Quality / Trust | **X5** |
| Lifecycle / Version / Change | **X7** |

GEARA Foundation/resilience and outcome/value/economic responsibilities also contribute to X8/X9 where applicable.

## 17.3 GEAIRA

GEAIRA's eight Overlays map many-to-many:

| GEAIRA Overlay | HDIP treatment |
|---|---|
| X1 Security, Privacy & Trust Boundaries | **HDIP-X2 + HDIP-X5**, with safety aspects in X8 where applicable |
| X2 Identity, Authority & Policy Enforcement | **HDIP-X1 + HDIP-X2**, while authority identity remains typed |
| X3 Evidence, Provenance & Traceability | **HDIP-X3** |
| X4 Observability, Telemetry & Auditability | **HDIP-X4** |
| X5 Resilience, Safety & Failure Management | **HDIP-X8** |
| X6 Lifecycle, Version, Currentness & Change | **HDIP-X7** |
| X7 Interoperability, Contracts & Semantic Compatibility | **P2 + M12 Interaction Contracts**, not an HDIP Overlay |
| X8 Governance, Human Accountability & Compliance | **HDIP-X1 + HDIP-X6** where assurance/accountable assessment applies |

X9 Economic & Cost Accountability is an HDIP-specific cross-cutting concern justified by M05 RCF-30, GEDRA value/FinOps evidence and HDIP's explicit heavy-consumer/economic-accountability model; it is not inherited from a same-named generic source Overlay.

---

# 18. Overlay anti-patterns

M07 rejects the following architecture anti-patterns:

1. **Overlay-as-platform** - requiring one centralized service per Overlay.
2. **Overlay checkbox architecture** - attaching X1-X9 labels without explicit obligations, evidence or interactions.
3. **Governance dumping ground** - moving security, evidence, quality, assurance, lifecycle or cost into X1 merely because they are governed.
4. **Telemetry equals evidence** - treating logs/metrics as sufficient provenance, Control Evidence or assurance.
5. **Quality equals assurance** - treating quality thresholds or scores as blanket approval/assurance.
6. **Trust-score collapse** - replacing contextual evidence and Fitness for Use with one opaque score.
7. **IAM equals authority** - treating identity infrastructure or entitlement configuration as Product/Data/policy/Decision authority.
8. **Latest equals current** - assuming the newest version is automatically governed-current and eligible.
9. **Cost equals value** - treating lower cost as higher value or high usage as successful outcome.
10. **Resilience-only-infrastructure** - treating failure/recovery as solely an HDIP-FND concern and ignoring Plane-level behavior.
11. **Duplicate Overlay per Plane** - cloning one Overlay into five independent semantic definitions.
12. **Overlay owns semantics** - allowing an Overlay to redefine GEDRM/GEARM/GEAIRM/BPS/Product-family meanings.

---

# 19. Canonical M07 architecture rules

**HDIP-CLA-M07-R01 - Nine-Overlay freeze.** HDIP-CLA 0.1 SHALL use exactly nine canonical cross-cutting Overlays, HDIP-X1 through HDIP-X9, as defined by M07 unless changed through governed versioning.

**HDIP-CLA-M07-R02 - Overlay logicality.** A canonical Overlay SHALL represent an orthogonal architecture responsibility and SHALL NOT imply a mandatory physical platform, service, database, team or organizational function.

**HDIP-CLA-M07-R03 - Overlay orthogonality.** An Overlay SHALL qualify or constrain applicable Plane responsibilities without replacing the Plane's primary architectural purpose.

**HDIP-CLA-M07-R04 - Shared realization allowed.** One implementation MAY realize responsibilities from multiple Overlays and Planes where identity, authority and evidence distinctions remain explicit.

**HDIP-CLA-M07-R05 - Contextual applicability.** Overlay applicability SHALL be determined by the material responsibilities and risk/context of the subject; an Overlay SHALL NOT be applied or declared not applicable merely for diagram symmetry.

**HDIP-CLA-M07-R06 - Overlay traceability.** Material Overlay obligations SHALL retain traceability to relevant source responsibilities, policy/contract requirements, architecture interactions and evidence where applicable.

**HDIP-CLA-M07-R07 - Primary responsibility preservation.** Cross-cutting treatment SHALL NOT relocate a Plane's primary responsibility into an Overlay merely because the responsibility is governed, secured, observed or evaluated.

**HDIP-CLA-M07-R08 - Foundation distinction.** HDIP-FND mechanisms MAY realize Overlay capabilities but Foundation participation SHALL NOT establish Overlay authority, semantic meaning, trust or assurance.

**HDIP-CLA-M07-R09 - Product-lens distinction.** Product qualification and Product-family semantics SHALL remain orthogonal to X1-X9 and SHALL NOT be inferred from successful Overlay processing.

**HDIP-CLA-M07-R10 - No Overlay checkbox.** Conformance SHALL NOT be claimed by naming X1-X9 alone; applicable obligations, boundaries and evidence SHALL be demonstrable.

**HDIP-CLA-M07-R11 - X1 authority preservation.** X1 SHALL coordinate governing obligations without assuming ownership of externally authoritative policy, legal, regulatory or domain rules merely because HDIP resolves or enforces them.

**HDIP-CLA-M07-R12 - X1 policy-stage distinction.** Policy authority, applicability resolution, compilation/binding and runtime enforcement SHALL remain distinguishable.

**HDIP-CLA-M07-R13 - X1 Control Evidence distinction.** Control Evidence SHALL remain distinguishable from policy declaration, control definition, control execution and generic telemetry.

**HDIP-CLA-M07-R14 - X1 judgement honesty.** Material approval, risk acceptance, exception or assurance decisions requiring accountable judgement SHALL NOT be represented as machine-proven solely because executable rules or telemetry exist.

**HDIP-CLA-M07-R15 - X2 identity non-authority.** Identity, authentication and credential possession SHALL NOT by themselves establish Product ownership, Data authority, policy authority or Decision authority.

**HDIP-CLA-M07-R16 - X2 entitlement scope.** Access/operation entitlement SHALL be scoped to applicable actor/workload, resource, purpose, context and lifecycle/currentness constraints where required.

**HDIP-CLA-M07-R17 - X2 cross-Plane protection.** Security and privacy obligations SHALL NOT be localized solely to P4 access; they may apply from P1 intent through P5 evidence/evolution.

**HDIP-CLA-M07-R18 - X2 IAM mechanism non-authority.** Identity/IAM/secrets mechanisms supplied by HDIP-FND SHALL implement protection responsibilities without becoming the semantic or governance authority for the entitlements/policies they enforce.

**HDIP-CLA-M07-R19 - X3 provenance distinction.** Provenance, dependency, lineage, derivation, composition and operational telemetry SHALL remain distinguishable relationships/evidence types.

**HDIP-CLA-M07-R20 - X3 evidence typing.** Material evidence SHALL retain sufficient identity, type, source, version/currentness and correlation context to support governed interpretation.

**HDIP-CLA-M07-R21 - X3 historical preservation.** Later supersession, reevaluation, revocation or new evidence SHALL NOT rewrite the evidence/version context that governed an earlier material occurrence.

**HDIP-CLA-M07-R22 - X3 evidence non-assurance.** Evidence availability or provenance completeness SHALL NOT by itself prove correctness, authorization, Fitness for Use, control effectiveness or assurance.

**HDIP-CLA-M07-R23 - X4 observability non-assurance.** Operational observability SHALL NOT by itself establish quality, trust, correctness, authorization, value or assurance.

**HDIP-CLA-M07-R24 - X4 telemetry distinction.** Metrics, logs, traces and events MAY contribute to evidence but SHALL NOT be treated automatically as semantic provenance, lineage or Control Evidence.

**HDIP-CLA-M07-R25 - X4 auditability.** Where auditability is required, HDIP SHALL retain sufficient correlation and historical operational records to reconstruct material behavior without requiring one universal log store.

**HDIP-CLA-M07-R26 - X4 topology independence.** Observability responsibilities SHALL remain valid across centralized, federated, distributed, embedded and provider realizations and SHALL NOT mandate one observability stack.

**HDIP-CLA-M07-R27 - X5 quality/trust/fitness distinction.** Quality evidence, trust evidence, trust conclusion and Fitness for Use SHALL remain distinguishable.

**HDIP-CLA-M07-R28 - X5 no universal trust score.** Core HDIP SHALL NOT require one opaque score as sufficient representation of Data, Information, AI, Product or contextual trust/fitness.

**HDIP-CLA-M07-R29 - X5 typed quality.** Shared quality infrastructure SHALL preserve domain- and artifact-specific dimensions, definitions, thresholds and authority.

**HDIP-CLA-M07-R30 - X5 contextual fitness.** Fitness for Use SHALL be evaluated relative to an intended purpose/context and SHALL NOT be inferred from generic quality metrics alone.

**HDIP-CLA-M07-R31 - X6 Evaluation/Assurance distinction.** Evaluation result, test result, quality measure and Assurance Finding SHALL remain distinguishable.

**HDIP-CLA-M07-R32 - X6 assurance authority.** The system/tool that executes an evaluation SHALL NOT automatically become the accountable assurance authority for the conclusion derived from that evaluation.

**HDIP-CLA-M07-R33 - X6 automation honesty.** Automation MAY support or determine assurance only where the applicable requirement is safely machine-evaluable; judgement-dependent assurance SHALL retain accountable assessment.

**HDIP-CLA-M07-R34 - X6 evaluation traceability.** Material Evaluation/Assurance findings SHALL retain traceability to the evaluated subject/version, criteria, evidence and applicable authority/context.

**HDIP-CLA-M07-R35 - X7 latest/current distinction.** The newest or latest artifact/version SHALL NOT automatically be treated as governed-current, eligible or authorized for use.

**HDIP-CLA-M07-R36 - X7 typed lifecycle semantics.** Semantic, Product, contract, process/logic, realization, deployment, policy/control, evidence and assurance lifecycle/version states SHALL remain distinguishable where applicable.

**HDIP-CLA-M07-R37 - X7 historical meaning.** Supersession, rollback, retirement or later change SHALL NOT rewrite which versions and constraints governed a historical occurrence.

**HDIP-CLA-M07-R38 - X7 governed change propagation.** Material change SHALL trigger applicable compatibility, impact, reassessment, migration, re-binding or lifecycle actions rather than silent downstream adoption.

**HDIP-CLA-M07-R39 - X8 resilience/safety distinction.** Service resilience, Data availability/quality, analytical validity and AI/consequential-action safety SHALL remain distinguishable even when common recovery mechanisms are used.

**HDIP-CLA-M07-R40 - X8 failure/recovery evidence.** Material failure, degraded operation, fallback and recovery SHALL produce/retain applicable evidence sufficient for operational and governance reconstruction.

**HDIP-CLA-M07-R41 - X8 safety specialization.** Domain-specific safety requirements SHALL remain Profile/specialization concerns and SHALL NOT be generalized into one universal HDIP safety semantic model.

**HDIP-CLA-M07-R42 - X8 not Foundation-only.** Resilience SHALL NOT be treated solely as an infrastructure responsibility; applicable Plane behavior, contracts, state and recovery semantics SHALL also be explicit.

**HDIP-CLA-M07-R43 - X9 cost/value separation.** Cost, usage, outcome and value SHALL remain distinct even where the same telemetry contributes evidence to several assessments.

**HDIP-CLA-M07-R44 - X9 economic attribution.** Where economic accountability is required, cost attribution SHALL identify the relevant resource/consumer/Product/capability/context sufficiently to support governed interpretation.

**HDIP-CLA-M07-R45 - X9 heavy-consumer accountability.** HDIP MAY implement showback, chargeback, quotas, budgets or heavy-consumer controls where appropriate, but those mechanisms SHALL remain governed policies rather than intrinsic Product semantics.

**HDIP-CLA-M07-R46 - X9 economic evidence non-value.** Economic evidence SHALL inform P5 Outcome/Value/Evolution assessment but SHALL NOT by itself prove value or determine Product qualification.

**HDIP-CLA-M07-R47 - Interoperability non-Overlay.** Interoperability, Contract and semantic-compatibility concerns SHALL be represented through P2 responsibilities and M12 Interaction Contracts rather than a duplicate tenth HDIP Overlay.

**HDIP-CLA-M07-R48 - No ABB implication.** Admission of X1-X9 SHALL NOT imply one canonical ABB or service per Overlay; M08 SHALL independently apply responsibility-based ABB admission criteria.

---

# 20. What M07 deliberately does not decide

M07 does not freeze:

- canonical ABB identities or ABB count (M08);
- physical governance/security/evidence/observability/quality/assurance/lifecycle/resilience/cost services;
- registry deployment/consolidation (M09);
- HPD/descriptor/projection physical storage or graph topology (M09);
- PDEP family-specific lifecycle details beyond accepted boundaries (M10);
- SSCF/CEP implementation topology (M11);
- canonical inter-Plane Interaction Contracts or protocol schemas (M12);
- adjacent external-system boundaries (M13);
- deployment/realization patterns (M14);
- canonical reference views (M15);
- final conformance modes, machine-checkability or evidence sufficiency rules (M16).

---

# 21. M07 completion state

**HDIP-CLA M07 - COMPLETE.**

M07 establishes:

- **9 canonical Cross-Cutting Overlays**;
- explicit admission of all nine M06 Overlay candidates;
- explicit separation of Provenance/Evidence from Observability/Telemetry;
- explicit separation of Quality/Fitness/Trust Evidence from Evaluation/Assurance;
- explicit Economic & Cost Accountability independent from P5 Value;
- an applicability model across P1-P5;
- explicit non-admission of Interoperability/Contracts/Semantic Compatibility as a tenth Overlay;
- explicit treatment of Product as an orthogonal lens, Registry as M09 architecture and Utility as HDIP-FND rather than Overlays;
- a many-to-many source mapping to GEDRA, GEARA and GEAIRA cross-cutting structures;
- **12 Overlay anti-patterns**;
- **48 normative M07 rules**;
- **0 canonical ABBs** introduced by M07.

### Next stage

> **M08 - Canonical Logical ABB Catalogue**

M08 will apply the responsibility-based ABB admission discipline to the five canonical Planes, nine canonical Overlays and Shared Platform / Utility Foundation, admitting only cohesive, independently useful logical building blocks rather than promoting every responsibility, service label or Overlay into a component.
