# INFOPS — Information Product Specification

**Status: INFOPS-P01 STAGE 4 OWNER-REVIEWED CONDITIONAL RESEARCH (NON-NORMATIVE).** This is a new Docusaurus project for developing INFOPS 0.1. It is **not** a published, normative Information Product specification.

## Purpose

INFOPS will define Information Product family qualification consistent with **BPS/PIN**, **GEARM** and **GEARA**, with its own **INFOPCH** characteristics and evidence-based **Product Maturity-Driven Development (PMDD)** guidance for human and AI assessors. It will align with **HDIP/UPOS** without absorbing their distinct architectural responsibilities.

The original P01 Stage 1 baseline and review remain preserved. Stage 2 (`docs/ontology/p01-stage-02-pin-differentiation-falsification.md`) contains 36 conditional case dispositions, ten PFI thought experiments and 16 falsification tests. Stage 3 adds `docs/ontology/p01-stage-03-candidate-qualification-rules.md`, a review procedure, 20 additional boundary cases, a PFI invariance protocol and explicit owner review decisions. The original and refined KivaNura crude-oil-to-driver analogy is retained at `docs/foundations/crude-oil-to-driver-teaching-analogy.md` as **informative only**. The `research/p01-s02/` and `research/p01-s03/` files are non-normative evidence/traceability records and scripts do **not** certify any Product or PFI. **Joint sufficiency of candidate qualification conditions is unproven**; no INFOPCH maturity assessment, descriptor contract or conformance claim has been issued.

## Owner-reviewed Stage 4 overlay (19 October 2026)

**G01 (15/15), G02 (7/7) and G03 (10/10) owner-reviewed research findings have completed review.** G03-D10-F01 conditionally closes the source authority research gate; BPS/PIN, GEARM and BPS DPP normative source adoption is incomplete, and **G04 has not yet started**. Original S03 evidence and historic PROPOSED decisions remain preserved in their own sources.

S04 review pages: `docs/ontology/p01-stage-04-overview.md` (gateway), `p01-stage-04-owner-decisions.md`, `p01-stage-04-source-authorities.md`, `p01-stage-04-artifact-boundaries.md`, `p01-stage-04-release-holds.md`, and `p01-stage-04-g04-plan.md`. Research-only JSON evidence is in `research/p01-s04/`, checked by `scripts/validate-infops-p01-s04.py`.

- Owner-approved architecture direction: Information-native **INFOPROD** (semantic descriptor) and **INFOPDS** (realization/deployment contract); **BPS DPP** is cross-family and will have an Information-specific trust Profile; **HDIP HPD** remains a non-authoritative operational projection.
- All these proposed artifacts are **non-normative**. No Information Product is certified, no DPP Profile is released, and the necessary/sufficient Product-family predicate remains unproven.
- The source S03 cumulative ZIP contains **68 repository files**. The S04 overlay is relative to that baseline and contains only S04-added or S04-modified paths. It is **not** a full repository checkout and contains no `.git` data.
- The source available for packaging records G01 as **15 owner-reviewed findings**, but does not contain their verbatim individual texts. This overlay preserves the gate-level finding without inventing missing G01 descriptions.

### Applying the S04 overlay

From the **root of an INFOPS checkout that already includes P01-S03**, extract the S04 ZIP preserving relative paths. Review its changed file list before committing; retain any environment-specific `package-lock.json`, site URLs and local customization. This overlay does **not** update `.git`, remote branches, third-party repositories or machine-readable normative INFOPS schemas.

```bash
unzip -o infops-0.1-p01-s04-g01-g03-owner-reviewed-research-overlay.zip
npm run validate
npm run build
```

The `npm run validate` command runs both the preserved S01-S03 validators and the new S04 owner-review research validator. `npm run build` requires locally available Docusaurus dependencies (or a connected Netlify/CI build environment).

The initial structure deliberately resembles the AIPS Docusaurus approach: documentation, characteristics/guidance, descriptors, machine-readable `static/spec` assets, validation scripts and CI.

## Run locally

Requirements: Node.js 20+; npm; Python 3 for the scaffold validator.

```bash
npm install
npm run validate
npm start
```

Open the local URL displayed by Docusaurus (normally http://localhost:3000).

For a production build:

```bash
npm run build
npm run serve
```

`npm install` produces a `package-lock.json` file. **Commit that lockfile** to the GitHub repository after the first successful install; CI automatically switches to `npm ci` when present. Dependency installation requires network access to npm unless dependencies are already cached.

## GitHub / stage overlays

For an **existing INFOPS repository already deployed on Netlify**, apply the **P01-S04 owner-reviewed research overlay ZIP** on top of the exact uploaded `INFOPS.zip` checkout rather than replacing the checkout. Its repository-relative paths contain only files added or modified since the S03 cumulative research baseline; retain your own `package-lock.json`, repository-specific configuration and independent files. Run `npm run validate` and `npm run build`, review and commit the changes.

The full updated repository ZIP retains your original top-level `shu_ha_ri/` folder; the smaller overlay is rooted at the repo root. See `INFOPS-P01-S04-MERGE-NOTES.md` for the actual baseline-specific deployment instructions. After validating your local checkout:

```bash
git add .
git commit -m "Record INFOPS P01 S04 owner-reviewed G01-G03 research"
git push -u origin HEAD
```

If you have not yet cloned/connected the remote, first clone the empty repository from its real URL and copy the contents into it. There is no assumed repository URL in this scaffold.

## Deployment settings

`docusaurus.config.js` uses `https://example.org` and `/` as safe *placeholders*, not deployment commitments. Before publishing, configure:

- `SITE_URL` to the actual website origin (for example `https://docs.example.org`);
- `BASE_URL` to `/` for a site root, or `/<repository-name>/` for project-style GitHub Pages;
- `organizationName` / `projectName` to the actual account and repository name;
- publisher-approved copyright and licensing conditions.

For example:

```bash
SITE_URL=https://docs.example.org BASE_URL=/ npm run build
```

## Layout

```text
├── docs/                           # Proposed specification and PMDD docs
│   ├── specification/              # Status, programme, roadmap
│   ├── foundations/                # Authority map and informative oil/driver analogy
│   ├── ontology/                   # Reserved P01 subject
│   ├── infopch/                    # Reserved P02 characteristic catalogue
│   ├── pmdd/                       # Reserved P03/P04 guidance and maturity
│   ├── descriptors/                # Reserved P05 descriptor strategy
│   ├── conformance/                # Reserved P06 conformance
│   └── integration/                # UPOS and HDIP boundaries
├── src/pages/                      # Homepage and agent guidance entry
├── static/spec/infops/0.1/         # Reserved machine-readable artifact namespace
├── templates/                      # Future characteristics/qualification/agent cases
├── research/p01-s02/                # Preserved S02 falsification research ledgers
├── research/p01-s03/                # S03 candidate rules, cases, analogy and decision ledger
├── research/p01-s04/                # S04 conditional owner-review and adoption-hold ledgers
├── scripts/                        # Scaffold/research validation (NOT conformance)
├── .github/workflows/             # Docs build CI when configured in your checkout
├── docusaurus.config.js
└── sidebars.js
```

## Authority and release rules

The existing authority boundaries are explicitly respected: generic Productness belongs to BPS/PIN; Information/Analytics meaning to GEARM; analytical architecture to GEARA; HDIP and UPOS provide separate platform/operating concepts. Data Product DPROD/DPDS and AI Product AIPS/AIPROD/AIPDS are **referenced external/adjacent Product-family sources**, not copied into INFOPS.

The Stage 2 and Stage 3 research ledgers are **not semantic conformance engines** and does not establish any live Product qualification. The scaffold must not be treated as evidence of qualification, maturity, deployment readiness or conformance. Do not label INFOPCH characteristics or INFOPS schemas normative until those decisions have been reviewed.

## Licence

**Uploaded repository licensing note:** The attached `INFOPS.zip` includes a `LICENSE` file containing GNU General Public License Version 3 text. The S04 integration preserves that file unchanged. The repository owner should confirm whether this is the intended licence and ensure applicable notices and redistribution conditions are met. No further licence is granted or modified by this research overlay.
