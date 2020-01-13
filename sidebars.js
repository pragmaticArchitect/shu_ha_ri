/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
module.exports = {
  infopsSidebar: [
    'intro',
    {type: 'category', label: 'Specification programme', items: [
      'specification/overview','specification/status','specification/roadmap',
    ]},
    {type: 'category', label: 'Foundations & authority', items: [
      'foundations/authority-map','ontology/overview','ontology/qualification-boundary',
    ]},
    {type: 'category', label: 'Information Product characteristics', items: [
      'infopch/overview',
    ]},
    {type: 'category', label: 'PMDD', items: [
      'pmdd/overview','pmdd/assessment-guidance',
    ]},
    {type: 'category', label: 'Descriptors & conformance', items: [
      'descriptors/strategy','conformance/overview',
    ]},
    {type: 'category', label: 'Integration & demonstrator', items: [
      'integration/hdip-upos','reference-implementation/overview',
    ]},
    {type: 'category', label: 'Governance & reference', items: [
      'governance/change-control','governance/contributing','reference/glossary',
    ]},
  ],
};
