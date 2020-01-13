import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  hdipSidebar: [
    'introduction',
    {
      type: 'category',
      label: 'Canonical Logical Architecture',
      items: [
        'architecture/hdip-cla-0.1-programme',
        'architecture/cla/hdip-cla-0.1-m01-charter',
        'architecture/cla/hdip-cla-0.1-m02-upstream-responsibility-intake',
        'architecture/cla/hdip-cla-0.1-m03-existing-hdip-construct-inventory',
        'architecture/cla/hdip-cla-0.1-m04-principles-design-invariants',
        'architecture/cla/hdip-cla-0.1-m05-responsibility-convergence-separation',
        'architecture/cla/hdip-cla-0.1-m06-canonical-logical-plane-derivation',
        'architecture/cla/hdip-cla-0.1-m07-cross-cutting-overlay-derivation',
        'architecture/cla/hdip-cla-0.1-m08-canonical-logical-abb-catalogue',
        'architecture/cla/hdip-cla-0.1-m09-registry-descriptor-projection-compilation-architecture',
        'architecture/cla/hdip-cla-0.1-m10-pdep-architecture',
        'architecture/cla/hdip-cla-0.1-m11-sscf-cep-architecture',
        'architecture/cla/hdip-cla-0.1-m12-canonical-inter-plane-interaction-model',
        'architecture/cla/hdip-cla-0.1-m13-external-adjacent-system-boundary-model',
        'architecture/cla/hdip-cla-0.1-m14-realization-profile-patterns',
        'architecture/cla/hdip-cla-0.1-m15-canonical-reference-views',
        {
          type: 'category',
          label: 'Canonical Architecture Visuals',
          items: [
            'architecture/cla/views/hdip-cla-0.1-m15-v01-canonical-logical-platform',
          ],
        },
        'architecture/cla/hdip-cla-0.1-m16-architecture-invariants-conformance-model',
        'architecture/cla/hdip-cla-0.1-m17-cross-artifact-reconciliation-freeze',
      ],
    },
    {
      type: 'category',
      label: 'Executable Formalization',
      items: [
        'architecture/executable/hdip-cla-0.1-executable-programme',
        'architecture/executable/hdip-cla-0.1-a1-canonical-architecture-element-registry',
        'architecture/executable/hdip-cla-0.1-a2-canonical-relationship-traceability-registry',
        'architecture/executable/hdip-cla-0.1-a3-invariant-conformance-catalogue',
        'architecture/executable/hdip-cla-0.1-a4-rdf-owl-architecture-graph',
        'architecture/executable/hdip-cla-0.1-a5-jsonld-canonical-iri',
        'architecture/executable/hdip-cla-0.1-a6-shacl-constraint-layer',
        'architecture/executable/hdip-cla-0.1-a7-structural-json-jsonld-schemas',
        'architecture/executable/hdip-cla-0.1-a8-lifecycle-contract-profile-schemas',
        'architecture/executable/hdip-cla-0.1-a9-canonical-example-corpus',
        'architecture/executable/hdip-cla-0.1-a10-positive-conformance-tests',
        'architecture/executable/hdip-cla-0.1-a11-negative-boundary-test-cases',
        'architecture/executable/hdip-cla-0.1-a12-automated-conformance-runner',
        'architecture/executable/hdip-cla-0.1-a13-cross-artifact-reconciliation',
        'architecture/executable/hdip-cla-0.1-a14-regression-suite',
        'architecture/executable/hdip-cla-0.1-a15-executable-release-closure',
      ],
    },
    {
      type: 'category',
      label: 'Foundations',
      items: ['foundations/hdip-brief'],
    },
    {
      type: 'category',
      label: 'Data Management Baseline',
      items: ['data-management/hdip-enterprise-level1-data-architecture-requirements'],
    },
    {
      type: 'category',
      label: 'Product Development',
      items: ['product-development/hdip-data-product-development-stages'],
    },
    {
      type: 'category',
      label: 'Product Consumption',
      items: ['product-consumption/hdip-product-consumption-stages'],
    },
    {
      type: 'category',
      label: 'Product Projections',
      items: ['product-projections/hdip-product-descriptor'],
    },
    {
      type: 'category',
      label: 'Synthetic Context',
      items: [
        'synthetic-context/hdip-synthetic-context',
        'synthetic-context/hdip-synctx-ontology',
        'synthetic-context/hdip-synctx-pdep-inference',
      ],
    },
  ],
};

export default sidebars;
