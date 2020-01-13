---
title: P01 Stage 3 - Candidate Information Product Qualification Rules
sidebar_label: P01-S03 - Candidate Rules
---

# INFOPS-P01-S03 - Candidate Information Product qualification rules

> **RESEARCH / OWNER-REVIEW DRAFT — NON-NORMATIVE.** These are proposed *conditional* qualification rules, not adopted requirements, a conformance schema, a classifier authorized to certify Products, or a revision of upstream semantics. S02 explicitly left joint sufficiency unproven. This page proposes a testable conjunction for P01-S04 reconciliation; it does **not** claim to have proved necessary-and-sufficient qualification.

## 1. The question and the assessed subject

**Question:** If an independently qualified BPS Product has a particular governed intent and Product Promise, what evidence would support *provisionally* classifying its intrinsic family as Information, rather than Data, AI/Intelligence, generic Service, creative content, or a Compound Product?

Before testing any criterion, specify the **exact classification subject** and its identity/version/scope. A Product, Product Version, edition, published artifact, runtime occurrence, hosted process, API provider and commercial bundle are different potential subjects. A shared execution engine may serve many distinct Products. Several enterprises may instantiate the same Product Kind without sharing one Product identity.

S01 introduced H01-H10; S02 tested 36 hypothetical cases, 16 falsification rules and ten PFI experiments. The strongest remaining challenges are C02/C21 (enriched Data versus Information) and C12/C18/C31 (multiple primary promises or compound identity). See [the S02 findings](./p01-stage-02-hypothesis-dispositions.md) and [case ledger](./p01-stage-02-case-disposition-ledger.md).

## 2. Source-of-authority boundary

| Ontological or architectural subject | Authority retained | What S03 may do |
|---|---|---|
| Generic Productness, intrinsic nature, VBE, EVC, constitution, identity, Product Promise | **BPS / PIN** | Require independent evidence and specialize carefully; do not redefine Productness |
| Information, Information Proposition, Need, Analytical Intent, Semantics, Logic, Definition/Occurrence, Context | **GEARM** | Reference and bind to governed semantic identities/definitions; do not coin competing definitions |
| Analytical responsibility and optional intentional Productization | **GEARA** | Preserve direct analytical consumption and Information Product provision as distinct |
| Data semantics and Data Product qualification | **GEDRM / GEDRA / applicable Data Product specifications** | Perform competing-family review without assuming all enriched Data are Information Products |
| AI Product qualification and intelligence capability | **AIPS / GEAIRM / GEAIRA** | Preserve AI dependency non-transitivity and independent AI Product classification |
| Production, golden paths, binding, execution and cross-boundary trace | **UPOS / PFI / HDIP-CLA** | Vary realizations without assuming a change of intrinsic kind; preserve authority and currentness |
| Information Product-family qualification | **INFOPS, after owner adoption** | Propose and falsify family-specific predicates; nothing in S03 is binding |
| Maturity and operational authorization | **Future INFOPCH/PMDD and independent governing authorities** | Keep separate from family qualification |

**Status caveat:** The BPS/PIN reference used in the research corpus is a conceptual draft. Exact versions, canonical identifiers and formally adopted cross-specification references must be pinned before a normative INFOPS release.

## 3. Proposed testable conditions

The following identifiers are **research IDs**, not normative INFOPS rules.

| ID | Proposed condition | Evidence/reasoning requested | What cannot substitute |
|---|---|---|---|
| **Q0 — Independent Productness** | The *same assessed subject* independently qualifies as a Product under BPS/PIN, with intentional constitution, identifiable Product Promise and applicable governance. | Product identity/version, Product Owner or accountable governing actor, generic Product qualification evidence and bounded Product subject. | Marketplace listing, popularity, repeated use, analytics activity, high PMDD score. |
| **Q1 — Primary informational VBE** | The subject's **primary value-bearing essence** is one governed Information Proposition, or a coherent, bounded family of such propositions, rather than a generic capability to compute, store or present arbitrary results. | Main promised consumer value; defined informational question/subject, boundaries, interpretation and purpose; comparison to competing Product-family promises. | Numeric output, a dashboard, SQL, charts, volume-weighted average price (VWAP) fields, reporting labels. |
| **Q2 — Meaning-bearing constitution** | Applicable **Information Need / intent, interpretive frame, context rules, semantic definitions and meaning-affecting formation or interpretation logic** are identified and authoritative enough to determine what the promised Information means. | Referenced semantic/method versions, population, time, scope, eligibility, assumptions, provenance and material interpretation constraints; manual or executable formation is permitted. | Mere executable code, arbitrary context words, presentation template, internal analytics engine. |
| **Q3 — Essential consumable informational capability** | The Product's essential value capability is to make the promised Information available to eligible consumers under a defined Product consumption proposition. | Consumable edition, report, subscription, interface or other qualified form; obligations governing availability, interpretation, limitations and applicable currentness. | An API existing in the environment; mandatory continuously active engine, SQL store, or particular output-port technology. |
| **Q4 — Coherent PIN and identity boundaries** | The Product Promise, EVC and constitution support meaningful Product/Version identity and explicit invariants across editions, parameters, realizations and material semantic evolution. | Product/version relationship; what may vary (runtime parameter, delivery mode, engine) and what triggers semantic/version or family re-review. | Assuming one build, repository, response, invocation or deployment equals the complete Product. |
| **Q5 — Competing-family / compound boundary resolved** | Evidence establishes why the **primary** promise of the exact subject is informational despite plausible Data, AI, Service, creative, or Compound Product interpretations; where material independently governed essences coexist, retain uncertainty pending compound analysis. | Comparable BPS/PIN assessment, applicable family requirements, subject decomposition if needed, explicit unresolved conflicts and accountable review. | Picking the most fashionable technology, family ranking, or assuming each dependency changes the host Product's kind. |

**Q0 is an inherited *generic Productness precondition*. Q1–Q4 are candidate intrinsic family differentiators. Q5 is an adjudication and evidence gate, not a magical new property of Information.** This separation prevents the procedural fact that a reviewer has resolved a dispute from being mistaken for an ontological property of the Product.

### 3.1 What does “bounded, coherent proposition family” mean?

A proposal is provisionally coherent when the family shares a **governing informational objective**, controlled subject/scope and interpretable semantic contract, and when supported parameterization or evolution remains within that agreed meaning. It does **not** require enumeration of every future question, output value or supported parameter.

A generic analytical toolbox supporting arbitrary unrelated questions is not made an Information Product solely because it can generate information. An interactive subscription providing a governed set of settlement-health interpretations might nonetheless qualify even when output instances and parameters change. **The coherence boundary is a hypothesis to test, not a numeric threshold or a predetermined UI limit.**

### 3.2 Two senses of “logic”

- **Meaning-affecting logic** includes an approved metric definition, interpretive rule, analytical assumption, qualifying methodology or justified human/editorial method. It belongs to the semantic constitution of the promised Information, whether expressed by reference or directly.
- **Executable realization logic** includes generated adapters, compiler output, provider calls, orchestration and optimizations. It may be inside the realized executable, but its compiler, enterprise analytical engine, provider and compute/memory/network backbones need not be constituents of the Product itself.

PFI may select approved golden paths for realization; it may **not silently change** governed meaning (for example, replacing agreed VWAP with a different estimator), authorize decisions/actions, or confer Product-family identity. Refer to [S03 PFI invariance protocol](./p01-stage-03-pfi-semantic-invariance.md).

## 4. Candidate conjunction — **joint sufficiency unproven**

A proposed **semantic** family predicate for an exact subject/version `s` is:

```text
S03_CANDIDATE_INFORMATION_FAMILY(s)
    := BPS_PRODUCT(s)               # Q0; must be assessed by BPS authority
       AND INFORMATION_PRIMARY_VBE(s) # Q1
       AND GOVERNED_MEANING(s)        # Q2
       AND INFORMATION_EVC(s)         # Q3
       AND COHERENT_PIN_IDENTITY(s)   # Q4

Research adjudication additionally requires:
    - Q5 competing-family and compound review
    - adequate evidence, governing versions and applicable authority
    - no unresolved contradiction on the assessed subject
```

This is an **investigative classifier**. The conjunction is proposed as a *candidate necessary-and-sufficient target* **only if later adopted and shown to survive falsification**. As of S03, neither universality of each condition nor joint sufficiency has been demonstrated, and Q5 explicitly admits unresolved cases. A `PROVISIONAL_INFORMATION_MATCH` is an inference under assumptions, **not an approved family qualification**.

## 5. What S03 explicitly rejects as family qualifiers

- Technology/provenance proxies: AI-created, AI-powered, cloud/on-prem, SQL, Python, model presence, API provider, processor type, engine ownership, transport, deployment topology or compiler.
- Data-shape proxies: precomputed KPI, semantic metadata, structured result, rich description, VWAP numerical values, dashboard, PDF or subscription label.
- Administrative proxies: cataloguing, repeated reuse, publication, high maturity/INFOPCH, passing runtime tests, platform deployment or affordability.
- Pipeline proxies: requiring a sequential raw Data → curated Data → Information → Knowledge → Intelligence path; requiring the Product to own a continuously running analytics engine.
- Authority proxies: allowing PFI/golden paths to invent Product meaning, or allowing AI inference usage to reclassify its containing Product automatically.

## 6. Four independent decisions

1. **BPS Productness** — Is the stated subject a Product at all?
2. **INFOPS family qualification candidate** — Is its primary intrinsic Product promise informational?
3. **Realization / operational conformance and authorization** — Does a given Product Version/implementation fulfil its applicable obligations, including provider controls and semantic equivalence?
4. **INFOPCH/PMDD maturity** — How mature is an already-qualified Product under an applicable, independently authorized assessment framework?

Evidence of (3) or (4) cannot establish (1) or (2). A failed freshness SLA may signal nonconformance without changing intrinsic family. A different mathematical formula may signal a material semantic change requiring Product review.

## 7. Exit conditions before qualification can become normative

S03 does **not** meet these gates merely by being published:

- Adopted/pinned BPS/PIN and GEARM authority versions, explicit mappings and applicable independent Data/AI specifications.
- Reviewed real Product subjects and governed Promises; independently verified Productness.
- Defensible distinction for enriched Data Products (C02/C21), multi-primary/compound offerings (C12/C18/C31), interactive general-purpose analytical services (C07/C20), and knowledge/creative publication boundaries.
- Counterexamples challenging both necessity *and* sufficiency; independent review of near misses and false positives/negatives.
- Approved semantic equivalence tests for PFI realizations and traceable negative tests for semantic drift.
- Owner decisions and publication authority, subsequent executable qualification/evidence model (not an invented P03 maturity score).

Continue with the [S03 decision procedure](./p01-stage-03-decision-procedure.md), [boundary casework](./p01-stage-03-boundary-casework.md), [owner review register](./p01-stage-03-review-decisions.md), and the [informative KivaNura teaching analogy](../foundations/crude-oil-to-driver-teaching-analogy.md).
