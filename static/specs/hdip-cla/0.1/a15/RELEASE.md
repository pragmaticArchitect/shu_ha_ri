# HDIP-CLA 0.1 — A15 bounded executable formalization release

The archive is an integrity-verifiable machine-readable representation of the frozen M17 human-readable baseline. It is NOT an external-authority endorsement, independent SHACL/OWL certificate, implementation M16 conformance claim or production approval.

## Verify the extracted complete package

From the repository root:

```bash
python static/specs/hdip-cla/0.1/a15/run_release_verification.py --root . --output static/specs/hdip-cla/0.1/a15/a15-verification-report.json
python static/specs/hdip-cla/0.1/a15/test_release_verification.py
```

The verifier checks the complete tracked payload inventory, SHA-256 and file sizes, frozen M17 and 250 immutable A14 predecessor file hashes, A1–A3 counts, hashed stored A14 regression evidence, release scope/claims and the explicit five open verification dependencies. It intentionally excludes the self-referential release manifest and the two regenerated A15 reports from its hashed payload, but verifies that these three paths are the only exclusions. External ZIP checksums are published as a sidecar. No third-party signature is claimed.

For full runtime regression (additional dependencies: `jsonschema`, `rdflib`):

```bash
python static/specs/hdip-cla/0.1/a14/run_regression.py --output /tmp/hdip-cla-a14-fresh.json
```

The fresh result must show `PASS_BOUNDED_REGRESSION`; a stored report alone does not prove runtime tests have been executed in a new environment.

## Disposition and unresolved evidence

- A15 status: `FORMALIZATION_PACKAGE_CLOSED_BOUNDED`.
- A15 static verifier: `PASS_BOUNDED_RELEASE_INTEGRITY` only if all checks pass.
- M16 implementation conformance: `NOT_ESTABLISHED`.
- Publication/external governance approval: `NOT_ASSERTED`.
- Independent SHACL, full OWL reasoning and Docusaurus production build: `NOT_RUN`.
- Accountable architecture assessment: `NOT_ESTABLISHED`.
- External semantic/Product/policy/Decision attestation: `NOT_PERFORMED`.

A mismatch is a formalization/package defect to be reviewed against frozen M17; do not silently redefine authority, rebaseline hashes or discard historical assessments.
