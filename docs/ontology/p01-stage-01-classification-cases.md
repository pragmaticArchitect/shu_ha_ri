---
title: P01 Stage 1 - Classification Challenge Cases
sidebar_label: P01-S01 - Challenge Cases
---

# INFOPS-P01-S01 - Classification challenge inventory

> **Non-normative investigatory cases.** No case below has yet been issued an INFOPS family qualification outcome. All examples are hypothetical and must ultimately be assessed for BPS Productness independently of the apparent Data/Information/AI boundary.

## 1. Assessment discipline

For each candidate, identify (1) the *assessed subject* and Product version, if any; (2) the asserted Product Promise and VBE; (3) the Information Proposition, if material; (4) the upstream Data/Information/AI/human/semantic constituents; (5) the strongest competing Product-family explanation; (6) why the artefact or delivery modality alone is insufficient; and (7) the evidence needed to decide.

The open disposition `UNRESOLVED` means **no INFOPS rule has yet been agreed**, not that a Product is immature or has failed a quality assessment.

## 2. Stage 1 classification cases

| Case | Proposed assessed subject | Primary challenge for P01 Stage 2 |
|---|---|---|
| C01 | Versioned Payment Lifecycle dataset with timestamps and status | Structured Data and contextual meaning do not automatically establish an Information Product |
| C02 | Dataset enriched with precomputed settlement duration and corridor measures | Is adding calculations a change in family, or an enriched Data Product? |
| C03 | One-off settlement KPI displayed in an internal dashboard | Analytical Output and visualization do not automatically qualify as Products |
| C04 | Governed reusable corridor settlement performance subscription | Determine promise, Information Proposition, ownership and VBE independently of interface |
| C05 | A versioned analytical PDF brief published for clients | Can bounded static Information carry intrinsic Product identity independent of its PDF format? |
| C06 | Human-curated market interpretation with disclosed assumptions | Is machine execution necessary? The GEARM method-independent principle suggests this must be examined |
| C07 | BI tool that lets customers formulate arbitrary calculations | Is the primary value a service/tool capability or qualified Information propositions? |
| C08 | Qualified AI Product used to summarize settlement statistics | Dependency on an AI Product does not classify the resulting proposition as AI Product |
| C09 | Qualified AI inference service providing predictions and explanations | Does intrinsic value reside in an Intelligence capability or a governed Information Proposition? |
| C10 | Threshold-driven operational alert representing late-settlement indicators | Information, Recommendation, Decision and Action boundaries may be confused |
| C11 | Governed Information Product consumed by another Information Product | Dependency and constitution do not imply cloning upstream Product identity |
| C12 | Information offering combining a metric, explanation and interactive simulation | Is this one Information Product, a Service Product, several Products or a compound? |
| C13 | Periodically refreshed fraud monitoring report backed by Data and AI Products | Method, refresh frequency and upstream constituents should not predetermine family |
| C14 | Analytical Information consumed ad hoc with no declared Product Promise | GEARM/GEARA direct consumption may be correct even where no Product exists |
| C15 | Two interfaces offering identical metrics with different semantics/periods | Semantic proposition and version identity versus output/schema similarity |
| C16 | Historical report whose current metric definition has changed | Reconstruct occurrence-time semantic meaning rather than rewrite historical evidence |
| C17 | Marketplace listing of a chart with high INFOPCH-like scores | Discoverability and maturity cannot create Productness or family qualification |
| C18 | One commercial bundle of a data feed, contextual analysis and AI recommendations | Compound or contextual bundling versus intrinsic family of each qualified component |

## 3. Explicit counterexample prompts

- If C02 and C04 return identical numeric values, what distinguishes an Information Product by **intrinsic promise** rather than by SQL complexity or presentation?
- If C05 is static and human-authored, what if any essential Product capability must remain? Avoid requiring continuous calculation by assumption.
- If C07 offers no pre-defined Information Proposition, should it be classified as a Product of a different family rather than forced into INFOPS?
- If C08 uses an LLM and C06 uses an analyst, can equivalent consumer Information value be classified consistently?
- If C10 triggers a workflow action, who owns consequential decision and authorization, independently of Information provision?
- If C17 has high evidence-backed maturity, why would that not change a negative BPS/PIN or Information-family qualification result?
- If C18 contains Data, Information and AI offerings, what precisely is the **subject** classified: bundle, constituent, consumer experience or Product version?

## 4. Evidence card template (for Stage 2)

```yaml
caseId: CXX
subject: "[named candidate and version]"
assertedProductPromise: "[value promised to consumers]"
productnessEvidence: "[BPS/PIN source references, or unresolved]"
informationProposition: "[GEARM identity/version/meaning, or unresolved]"
pin:
  valueBearingEssence: "[investigated essence]"
  essentialValueCapability: "[investigated capability]"
  constitution: "[dependencies, methods and their authorities]"
  identityInvariants: "[what must remain true]"
competingExplanations: ["Data Product", "Information Product", "AI Product", "Service Product", "Compound Product", "Other"]
missingEvidence: []
status: UNRESOLVED
rationale: "This template is a research record, not an approved qualification certificate."
```

Do not attach PMDD scores, eligibility decisions or production authorization to this preliminary classification card.

## 5. Stage 2 use

Falsify hypotheses before writing normative rules. Every proposed necessary or sufficient INFOPS criterion should be challenged by at least one positive case, one counterexample and an ambiguous case. Distinguish genuine absence of Productness from unresolved family classification and insufficient evidence.
