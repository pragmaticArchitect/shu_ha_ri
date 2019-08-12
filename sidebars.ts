import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  hdipSidebar: [
    'introduction',
    {
      type: 'category',
      label: 'Canonical Logical Architecture',
      items: ['architecture/hdip-cla-0.1-programme'],
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
