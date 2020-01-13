---
title: P01 Stage 3 - Proposed Qualification Decision Procedure
sidebar_label: P01-S03 - Decision Procedure
---

# INFOPS-P01-S03 - Proposed qualification decision procedure

> **NON-NORMATIVE INVESTIGATIVE PROCEDURE.** This page specifies how to *review* candidate family claims, not how to certify an Information Product. It is not INFOPCH scoring, an AIPS qualifier or a runtime conformance test. See [the candidate rules](./p01-stage-03-candidate-qualification-rules.md).

## 1. Input dossier required for a reasoned decision

| Subject field | Minimum investigatory content | Authority / evidence boundary |
|---|---|---|
| **Subject** | Clearly scoped entity, identity, version/edition and whether this is a Product, an output occurrence, an internal tool or a commercial bundle | BPS; subject must not change during review |
| **Productness** | Evidence or explicit status of BPS Product qualification and intentional Productization | Do not infer from analytics, reuse or publishing |
| **Promise** | Product Owner's primary promised consumer value and any independent secondary/compound promises | BPS; distinguish semantic promise from delivery technology |
| **Proposition** | Governed Information Proposition or bounded coherent family, including subject, question and interpretive purpose | GEARM semantic authority; not a new INFOPS definition of Information |
| **Meaning** | Referenced Information Need/Analytical Intent, interpretive frame, context rules, metrics/methods, assumptions, formation/interpretation logic and relevant semantic versions | GEARM; manual and computational modes both possible |
| **Capability** | What eligible consumers can actually receive, and applicable interpretation/currentness/quality contract | Product Promise and exposure contract; no required API/engine |
| **Constitution** | Sources/dependencies/authority, Product identity invariants, version change rules and evidence of supplier capability bindings | BPS plus applicable family authorities; HDIP/UPOS for realization |
| **Competing claim** | Plausible Data, AI, Service, creative or compound alternative, with independent authority and unresolved evidence | Never inherit family from a dependency |

Missing data are recorded as missing data. **Lack of evidence does not demonstrate that a real subject lacks the property** unless an authoritative negative finding establishes that fact.

## 2. Proposed review protocol

```text
START: exact assessed subject/version
  |
  +-- Q0: independently BPS-qualified Product?
  |       NO / NOT SHOWN -> PRODUCTNESS_UNESTABLISHED; STOP family claim
  |       YES -> continue
  |
  +-- Q1: primary promised VBE is bounded governed Information?
  |       NO with supported different primary VBE -> COMPETING_FAMILY_PLAUSIBLE
  |       UNCLEAR -> UNRESOLVED
  |
  +-- Q2: meaning-bearing intent / frame / context / logic traceable?
  |       NO with relevant negative evidence -> CANDIDATE_CONDITION_NOT_MET
  |       UNKNOWN -> INSUFFICIENT_EVIDENCE
  |
  +-- Q3: essential capability makes promised Information consumable?
  |       NO with evidence -> CANDIDATE_CONDITION_NOT_MET
  |       UNKNOWN -> INSUFFICIENT_EVIDENCE
  |
  +-- Q4: coherent PIN / Product Version / identity invariants?
  |       NO with evidence -> CANDIDATE_CONDITION_NOT_MET
  |       UNKNOWN -> INSUFFICIENT_EVIDENCE
  |
  +-- Q5: competing-family / compound claim reconciled?
  |       NO -> CONFLICT_REVIEW
  |       YES -> PROVISIONAL_INFORMATION_MATCH
  |
  END: always non-normative; never a certificate, approval or PMDD score
```

If the question changes from the Product to one of its manifestations, **restart with a new subject**. Separately record operational and authorization findings; they do not automatically rewrite Product Family.

## 3. Permitted research dispositions

| Outcome | Interpretation |
|---|---|
| `PRODUCTNESS_UNESTABLISHED` | The subject's generic BPS qualification has not been established; no Information-family decision is justified. |
| `PROVISIONAL_INFORMATION_MATCH` | Under the explicit hypothetical/admitted evidence, all candidate semantic conditions appear satisfied and a competing claim has been addressed; **not certified**. |
| `COMPETING_FAMILY_PLAUSIBLE` | Primary VBE appears more consistent with another family; independent qualified family authority still governs its classification. |
| `CONFLICT_REVIEW` | Several materially different primary value propositions, boundary scopes or possible compound identities remain plausible. |
| `CANDIDATE_CONDITION_NOT_MET` | Facts contradict at least one candidate intrinsic condition for this stated subject. |
| `INSUFFICIENT_EVIDENCE` | Available facts cannot resolve some candidate conditions; never automatically reject a real Product. |
| `REALIZATION_INVARIANCE_CONDITIONAL` | Different eligible implementations appear able to preserve one candidate Product Kind; **not** a Productness or maturity status. |
| `SEMANTIC_CHANGE_REVIEW` | Meaning-affecting drift or changed primary promise requires renewed Product/semantic analysis. |

These codes are **not** official INFOPS, BPS, AIPS, DPROD, INFOPCH or PMDD results. They should not be used to label real Products in a registry without separately governed adoption.

## 4. Identical-payload example: two VWAP Products

**Hypothetical D:** The primary Promise is governed historical trade representation with declared fields, and a VWAP field is included for convenience. The buyer may perform their own interpretation. Information appears in the payload, but Data representation may remain the primary Product essence; `COMPETING_FAMILY_PLAUSIBLE` or `CONFLICT_REVIEW` is appropriate pending external Data Product authority and exact Promise.

**Hypothetical I:** The primary Promise is a governed interpretation of crypto price formation by defined market windows, eligible sources, VWAP methodology, assumptions, contextual baseline and consumer interpretation obligations. The same numerical VWAP field can be included; if all other candidate conditions and Productness are evidenced, `PROVISIONAL_INFORMATION_MATCH` is plausible.

**Result:** same value, field format, API and even upstream processing do **not** entail the same intrinsic Product kind. Conversely, the mere declaration “Information Product” does not prove Hypothetical I qualifies.

## 5. Information versus intelligence versus authority to act

An AI Product may supply interpretation, explanation or inference to the Information Product. That is a dependency relationship, not a family-identity inheritance. Where the subject principally promises a qualified intelligence capability itself, independently apply AIPS and the subject's BPS/PIN; do not assert an INFOPS decision first.

Information that recommends an action is not automatically a Product authorized to make or execute that decision. Keep Recommendation, Decision, Action and Outcome separate as GEARM requires. Do not make automatic-trading authority part of an informational proposition by semantic sleight of hand.

## 6. PFI and evidence independence

A PFI compilation trace can support an implementation claim (which blueprint, compiler/rule version, contracts, external provider and semantic references were bound). It cannot itself prove that the Product was a Product, that its informational VBE is primary or that an AI capability made it an AI Product.

For same-promise cross-enterprise claims, compare governed semantic definitions, source eligibility, context applicability, Product Promise and consumer contract *before* comparing execution engines. See [the PFI protocol](./p01-stage-03-pfi-semantic-invariance.md).

## 7. Review decision record (template)

```text
subject: <Product or other explicit subject; version / scope>
productnessAuthority: BPS / PIN (adopted ref and result or NOT_ESTABLISHED)
productPromise: <source/version/claim>
informationProposition: <GEARM concept source/version/contract>
semanticConstitution: <frame, context, meaning-affecting logic, refs>
valueBearingEssence: <primary promise plus competing interpretation>
essentialValueCapability: <consumer proposition + interface/edition>
identityInvariants: <what preserves or changes family and Product identity>
competingFamilyReview: <Data / AI / Service / creative / compound>
result: <one research disposition above>
uncertaintyAndMissingEvidence: <explicit, no inference from absence>
reviewerAndDecisionDate: <record if performed; blank for examples>
normative: false
certificationIssued: false
```

The [casework](./p01-stage-03-boundary-casework.md) deliberately contains missing evidence and hard conflicts to test the method rather than producing an artificial 100% qualification success rate.
