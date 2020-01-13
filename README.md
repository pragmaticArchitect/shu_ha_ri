# INFOPS — Information Product Specification

**Status: PRE-P01 REPOSITORY SCAFFOLD.** This is a new Docusaurus project for developing INFOPS 0.1. It is **not** a published, normative Information Product specification.

## Purpose

INFOPS will define Information Product family qualification consistent with **BPS/PIN**, **GEARM** and **GEARA**, with its own **INFOPCH** characteristics and evidence-based **Product Maturity-Driven Development (PMDD)** guidance for human and AI assessors. It will align with **HDIP/UPOS** without absorbing their distinct architectural responsibilities.

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

## GitHub bootstrap

This archive contains repository-relative project files at the **ZIP root** and no `.git` directory. Extract its contents directly into the root of your empty GitHub repository checkout:

```bash
git add .
git commit -m "Initialize INFOPS Docusaurus scaffold (pre-P01)"
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
│   ├── foundations/                # Authority map
│   ├── ontology/                   # Reserved P01 subject
│   ├── infopch/                    # Reserved P02 characteristic catalogue
│   ├── pmdd/                       # Reserved P03/P04 guidance and maturity
│   ├── descriptors/                # Reserved P05 descriptor strategy
│   ├── conformance/                # Reserved P06 conformance
│   └── integration/                # UPOS and HDIP boundaries
├── src/pages/                      # Homepage and agent guidance entry
├── static/spec/infops/0.1/         # Reserved machine-readable artifact namespace
├── templates/                      # Future characteristics/qualification/agent cases
├── scripts/                        # Scaffold validation (NOT conformance)
├── .github/workflows/             # Docs build CI
├── docusaurus.config.js
└── sidebars.js
```

## Authority and release rules

The existing authority boundaries are explicitly respected: generic Productness belongs to BPS/PIN; Information/Analytics meaning to GEARM; analytical architecture to GEARA; HDIP and UPOS provide separate platform/operating concepts. Data Product DPROD/DPDS and AI Product AIPS/AIPROD/AIPDS are **referenced external/adjacent Product-family sources**, not copied into INFOPS.

The scaffold must not be treated as evidence of qualification, maturity, deployment readiness or conformance. Do not label INFOPCH characteristics or INFOPS schemas normative until those decisions have been reviewed.

## Licence

**No public licence selected yet.** Before public redistribution or contribution acceptance, the repository owner should decide and publish explicit copyright, reuse and contribution terms. This scaffold does not copy the AIPS licence or grant its permissions by implication.
