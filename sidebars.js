/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
module.exports = {
  infopsSidebar: [
    'intro',
    {type: 'category', label: 'Specification programme', items: [
      'specification/overview','specification/status','specification/roadmap',
    ]},
    {type: 'category', label: 'Foundations & authority', items: [
      'foundations/authority-map','foundations/crude-oil-to-driver-teaching-analogy',
      'ontology/overview','ontology/qualification-boundary',
      'ontology/p01-stage-01-authority-and-ontology-baseline',
      'ontology/p01-stage-01-classification-cases',
      'ontology/p01-stage-01-ontology-review',
      'ontology/p01-stage-01-realization-stress-tests',
      'ontology/p01-stage-02-pin-differentiation-falsification',
      'ontology/p01-stage-02-case-disposition-ledger',
      'ontology/p01-stage-02-cross-enterprise-realization-tests',
      'ontology/p01-stage-02-hypothesis-dispositions',
      'ontology/p01-stage-02-owner-approved-decisions',
      'ontology/p01-stage-03-candidate-qualification-rules',
      'ontology/p01-stage-03-decision-procedure',
      'ontology/p01-stage-03-boundary-casework',
      'ontology/p01-stage-03-pfi-semantic-invariance',
      'ontology/p01-stage-03-review-decisions',
      'ontology/p01-stage-03-owner-approved-decisions',
      'ontology/p01-stage-04-overview',
      'ontology/p01-stage-04-g01-closure-basis',
      'ontology/p01-stage-04-owner-decisions',
      'ontology/p01-stage-04-source-authorities',
      'ontology/p01-stage-04-artifact-boundaries',
      'ontology/p01-stage-04-release-holds',
      'ontology/p01-stage-04-g04-plan',
      'ontology/p01-stage-04-g04-owner-approved-decisions',
      'ontology/p01-stage-04-g04-closure-record',
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
