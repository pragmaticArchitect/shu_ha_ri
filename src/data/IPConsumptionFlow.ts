// ACT2-D01/D02 approved experimental E0 design; not a normative SSCF schema.
export const sscfModel = {
  "lanes": [
    {
      "id": "consumer",
      "title": "L1 — Product Consumer (PCON)",
      "hint": "Consumption intent, evaluation, use and feedback"
    },
    {
      "id": "hdip",
      "title": "L2 — HDIP SSCF",
      "hint": "Discovery, access orchestration, CEP presentation and P5 support"
    },
    {
      "id": "authority",
      "title": "L3 — Independent Authorities & Services",
      "hint": "Competent decisions versus shared reference services"
    },
    {
      "id": "artifact",
      "title": "L4 — Governed Artifacts & Outcomes",
      "hint": "Identifiers, contracts, evidence, delivery and outcomes"
    }
  ],
  "nodes": [
    {
      "id": "intent",
      "lane": "consumer",
      "title": "Consumption intent",
      "subtitle": "Purpose, context, constraints",
      "kind": "actor",
      "description": "Consumer states intended use; does not confer qualification or permission."
    },
    {
      "id": "discover",
      "lane": "consumer",
      "title": "Explore candidate Products",
      "subtitle": "Search and matching",
      "kind": "actor",
      "description": "Consumer may discover existing governed Product offerings."
    },
    {
      "id": "evaluate",
      "lane": "consumer",
      "title": "Interpret and choose",
      "subtitle": "Meaning, Promise, trust, limitations",
      "kind": "actor",
      "description": "Selection is a contextual consumer decision, not Product qualification."
    },
    {
      "id": "request",
      "lane": "consumer",
      "title": "Request access where needed",
      "subtitle": "Applicable purpose and terms",
      "kind": "actor",
      "description": "An existing entitlement may already apply; approval is not universally mandatory."
    },
    {
      "id": "consume",
      "lane": "consumer",
      "title": "Consume existing Product",
      "subtitle": "CEP and supported Product interface",
      "kind": "actor",
      "description": "No new Product or Product Owner responsibility required."
    },
    {
      "id": "feedback",
      "lane": "consumer",
      "title": "Reflect and decide",
      "subtitle": "Value, reuse or change",
      "kind": "actor",
      "description": "May continue, stop, change consumption or propose optional PDEP referral."
    },
    {
      "id": "resolve",
      "lane": "hdip",
      "title": "Product resolution",
      "subtitle": "Catalogue and semantics",
      "kind": "capability",
      "description": "SSCF supports candidate matching; never issues independent Productness."
    },
    {
      "id": "interpret",
      "lane": "hdip",
      "title": "Contract interpretation",
      "subtitle": "Promise, meaning, method",
      "kind": "capability",
      "description": "References governed meaning and usage context."
    },
    {
      "id": "access",
      "lane": "hdip",
      "title": "Access orchestration",
      "subtitle": "Policy and entitlement interfaces",
      "kind": "capability",
      "description": "Resolves existing access or delegates determination to competent authority."
    },
    {
      "id": "cep",
      "lane": "hdip",
      "title": "CEP adaptation",
      "subtitle": "Business / Analytical / AI / System / Agentic",
      "kind": "capability",
      "description": "Consumer presentation does not change Product family or guarantee port compatibility."
    },
    {
      "id": "deliver",
      "lane": "hdip",
      "title": "Consumption support",
      "subtitle": "Binding to governed Product port",
      "kind": "capability",
      "description": "Routes permitted consumption through a supported Product interface."
    },
    {
      "id": "observe",
      "lane": "hdip",
      "title": "Observation / X9 / P5",
      "subtitle": "Usage, cost, outcome",
      "kind": "capability",
      "description": "Separates indicative consumption economics from actual observations."
    },
    {
      "id": "reentry",
      "lane": "hdip",
      "title": "Conditional re-entry",
      "subtitle": "Affected responsibilities only",
      "kind": "capability",
      "description": "Changed context can re-open affected resolution; no universal restart."
    },
    {
      "id": "pdep",
      "lane": "hdip",
      "title": "Optional PDEP referral",
      "subtitle": "Proposed Evolve / Create",
      "kind": "capability",
      "description": "Referral for unmet need does not authorize Product creation or qualify a Product."
    },
    {
      "id": "composition",
      "lane": "hdip",
      "title": "Governed composition",
      "subtitle": "Multiple existing Products",
      "kind": "capability",
      "description": "Composition is not automatic Compound Product qualification."
    },
    {
      "id": "prod-authority",
      "lane": "authority",
      "title": "BPS/PIN & family authorities",
      "subtitle": "Productness, family, Compound",
      "kind": "authority",
      "description": "Independent Product identity, version, Product-family and Compound determinations."
    },
    {
      "id": "sem-authority",
      "lane": "authority",
      "title": "GEARA/GEARM semantics",
      "subtitle": "Meaning and analytical method",
      "kind": "authority",
      "description": "Applicable semantic and analytical authority independent of SSCF."
    },
    {
      "id": "source-authority",
      "lane": "authority",
      "title": "Source & assurance authorities",
      "subtitle": "Sources, quality, confidence",
      "kind": "authority",
      "description": "Source permissions and assurance are independently competent."
    },
    {
      "id": "policy-authority",
      "lane": "authority",
      "title": "Policy authority",
      "subtitle": "Applicable rules and constraints",
      "kind": "authority",
      "description": "Policy decision does not equal access enforcement."
    },
    {
      "id": "entitlement-authority",
      "lane": "authority",
      "title": "Entitlement authority",
      "subtitle": "Consumer access decision",
      "kind": "authority",
      "description": "Access decisions attributable to independently competent authority."
    },
    {
      "id": "action-authority",
      "lane": "authority",
      "title": "Consequential action authority",
      "subtitle": "Decision / Action permission",
      "kind": "authority",
      "description": "Permission to consume is not authorization for consequential actions."
    },
    {
      "id": "investment-authority",
      "lane": "authority",
      "title": "Investment authority",
      "subtitle": "Funding and expenditure",
      "kind": "authority",
      "description": "X9/P5 visibility does not delegate financial authority."
    },
    {
      "id": "catalog",
      "lane": "authority",
      "title": "Catalogue / marketplace",
      "subtitle": "Reference and discovery service",
      "kind": "service",
      "description": "Service surfaces offers and governing references; not an intrinsic authority."
    },
    {
      "id": "evidence-service",
      "lane": "authority",
      "title": "Evidence / telemetry services",
      "subtitle": "Provenance and observations",
      "kind": "service",
      "description": "Evidence reference alone does not establish sufficiency or truth."
    },
    {
      "id": "product-id",
      "lane": "artifact",
      "title": "Product identity & Version",
      "subtitle": "Promise and Product family",
      "kind": "artifact",
      "description": "Separate Product identity/version, Promise and family qualification."
    },
    {
      "id": "semantic-id",
      "lane": "artifact",
      "title": "Semantic & method versions",
      "subtitle": "Interpretation and analytical frame",
      "kind": "artifact",
      "description": "Semantics and analytical method may have independent histories."
    },
    {
      "id": "contract-id",
      "lane": "artifact",
      "title": "Consumption Contract",
      "subtitle": "Version, purpose and limitations",
      "kind": "artifact",
      "description": "A contract is not an entitlement or consequential action permission."
    },
    {
      "id": "resolution-set",
      "lane": "artifact",
      "title": "Candidate resolution set",
      "subtitle": "Context-specific candidates",
      "kind": "artifact",
      "description": "Illustrative information, not mandated persisted artifact or certification."
    },
    {
      "id": "access-decision",
      "lane": "artifact",
      "title": "Access determination",
      "subtitle": "Policy, purpose, applicability",
      "kind": "artifact",
      "description": "Distinct accountable authorization from interface binding."
    },
    {
      "id": "interface-binding",
      "lane": "artifact",
      "title": "Product port & binding",
      "subtitle": "CEP, realization, provider versions",
      "kind": "artifact",
      "description": "Implementation details do not determine Product Family."
    },
    {
      "id": "invocation",
      "lane": "artifact",
      "title": "Invocation / execution occurrence",
      "subtitle": "Observed request and execution",
      "kind": "artifact",
      "description": "A successful invocation does not prove intended information was delivered."
    },
    {
      "id": "information-occurrence",
      "lane": "artifact",
      "title": "Delivered Information occurrence",
      "subtitle": "Information content and context",
      "kind": "artifact",
      "description": "Where applicable, distinguish delivered Information from execution occurrence."
    },
    {
      "id": "assessment",
      "lane": "artifact",
      "title": "Evidence / assessment / currentness",
      "subtitle": "Claim, provenance, sufficiency",
      "kind": "artifact",
      "description": "Independent evidence and evaluation, including historical applicability."
    },
    {
      "id": "outcome",
      "lane": "artifact",
      "title": "Usage, cost, value",
      "subtitle": "Observed P5 versus indicative X9",
      "kind": "artifact",
      "description": "Observed business value and costs require attributable evidence."
    },
    {
      "id": "handoff",
      "lane": "artifact",
      "title": "Conditional PDEP handoff",
      "subtitle": "Unmet Product need",
      "kind": "artifact",
      "description": "An intentional referral, not an approved new Product."
    },
    {
      "id": "compound",
      "lane": "artifact",
      "title": "Composition context",
      "subtitle": "Independent Compound authority",
      "kind": "artifact",
      "description": "Multi-Product use alone does not qualify a Compound Product."
    }
  ],
  "links": [
    {
      "id": "R01",
      "source": "intent",
      "target": "resolve",
      "interaction": "DECLARES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R02",
      "source": "resolve",
      "target": "catalog",
      "interaction": "RESOLVES",
      "annotation": "DERIVED_FROM"
    },
    {
      "id": "R03",
      "source": "catalog",
      "target": "resolution-set",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "DERIVED_FROM"
    },
    {
      "id": "R04",
      "source": "resolution-set",
      "target": "evaluate",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R05",
      "source": "evaluate",
      "target": "interpret",
      "interaction": "DECLARES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R06",
      "source": "interpret",
      "target": "product-id",
      "interaction": "RESOLVES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R07",
      "source": "interpret",
      "target": "semantic-id",
      "interaction": "RESOLVES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R08",
      "source": "sem-authority",
      "target": "semantic-id",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R09",
      "source": "prod-authority",
      "target": "product-id",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R10",
      "source": "interpret",
      "target": "contract-id",
      "interaction": "RESOLVES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R11",
      "source": "evaluate",
      "target": "request",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R12",
      "source": "request",
      "target": "access",
      "interaction": "DECLARES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R13",
      "source": "access",
      "target": "policy-authority",
      "interaction": "RESOLVES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R14",
      "source": "policy-authority",
      "target": "access-decision",
      "interaction": "DETERMINES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R15",
      "source": "access",
      "target": "entitlement-authority",
      "interaction": "RESOLVES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R16",
      "source": "entitlement-authority",
      "target": "access-decision",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R17",
      "source": "contract-id",
      "target": "access",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R18",
      "source": "access-decision",
      "target": "deliver",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R19",
      "source": "deliver",
      "target": "interface-binding",
      "interaction": "RESOLVES",
      "annotation": "DEPENDS_ON"
    },
    {
      "id": "R20",
      "source": "source-authority",
      "target": "interface-binding",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R21",
      "source": "interface-binding",
      "target": "cep",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "DEPENDS_ON"
    },
    {
      "id": "R22",
      "source": "cep",
      "target": "consume",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R23",
      "source": "consume",
      "target": "invocation",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "EVIDENCES"
    },
    {
      "id": "R24",
      "source": "invocation",
      "target": "information-occurrence",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "DERIVED_FROM"
    },
    {
      "id": "R25",
      "source": "information-occurrence",
      "target": "assessment",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "EVIDENCES"
    },
    {
      "id": "R26",
      "source": "evidence-service",
      "target": "assessment",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "DERIVED_FROM"
    },
    {
      "id": "R27",
      "source": "consume",
      "target": "observe",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "EVIDENCES"
    },
    {
      "id": "R28",
      "source": "observe",
      "target": "outcome",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "EVIDENCES"
    },
    {
      "id": "R29",
      "source": "outcome",
      "target": "feedback",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "DERIVED_FROM"
    },
    {
      "id": "R30",
      "source": "feedback",
      "target": "reentry",
      "interaction": "DECLARES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R31",
      "source": "reentry",
      "target": "resolve",
      "interaction": "RESOLVES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R32",
      "source": "feedback",
      "target": "pdep",
      "interaction": "OBSERVES_OR_HANDS_OFF",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R33",
      "source": "pdep",
      "target": "handoff",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R34",
      "source": "reentry",
      "target": "composition",
      "interaction": "RESOLVES",
      "annotation": "DEPENDS_ON"
    },
    {
      "id": "R35",
      "source": "composition",
      "target": "compound",
      "interaction": "PRODUCES_OR_REFERENCES",
      "annotation": "APPLIES_TO"
    },
    {
      "id": "R36",
      "source": "prod-authority",
      "target": "compound",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R37",
      "source": "investment-authority",
      "target": "outcome",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    },
    {
      "id": "R38",
      "source": "action-authority",
      "target": "consume",
      "interaction": "DETERMINES",
      "annotation": "GOVERNED_BY"
    }
  ],
  "moments": {
    "basic": [
      {
        "id": "PC-G0-P01",
        "title": "Express consumer need",
        "summary": "Purpose, intended outcome and constraints",
        "nodeIds": [
          "intent",
          "resolve"
        ]
      },
      {
        "id": "PC-G0-P02",
        "title": "Discover candidates",
        "summary": "Candidates are not certificates of Product qualification",
        "nodeIds": [
          "discover",
          "resolve",
          "catalog",
          "resolution-set"
        ]
      },
      {
        "id": "PC-G0-P03",
        "title": "Understand and select",
        "summary": "Promise, semantics, limitations and contract",
        "nodeIds": [
          "evaluate",
          "interpret",
          "product-id",
          "semantic-id",
          "contract-id"
        ]
      },
      {
        "id": "PC-G0-P04",
        "title": "Resolve governed access",
        "summary": "Existing entitlement or competent determination where required",
        "nodeIds": [
          "request",
          "access",
          "entitlement-authority",
          "access-decision"
        ]
      },
      {
        "id": "PC-G0-P05",
        "title": "Consume through CEP",
        "summary": "Use eligible Product interface; no new Product required",
        "nodeIds": [
          "cep",
          "deliver",
          "consume",
          "interface-binding"
        ]
      },
      {
        "id": "PC-G0-P06",
        "title": "Observe costs and value",
        "summary": "Distinguish indicative X9 and actual P5 evidence",
        "nodeIds": [
          "observe",
          "outcome",
          "assessment"
        ]
      },
      {
        "id": "PC-G0-P07",
        "title": "Next choice",
        "summary": "Continue, change, stop or conditionally refer need to PDEP",
        "nodeIds": [
          "feedback",
          "reentry",
          "pdep",
          "handoff"
        ]
      }
    ],
    "sa": [
      {
        "id": "PC-SA-P01",
        "title": "Consumer intent",
        "summary": "PCON declares purpose; SSCF resolves context",
        "nodeIds": [
          "intent",
          "resolve",
          "product-id"
        ]
      },
      {
        "id": "PC-SA-P02",
        "title": "Product discovery and evaluation",
        "summary": "Catalogue and governing authorities remain distinct",
        "nodeIds": [
          "catalog",
          "resolution-set",
          "evaluate",
          "interpret",
          "prod-authority",
          "sem-authority"
        ]
      },
      {
        "id": "PC-SA-P03",
        "title": "Access determination",
        "summary": "Policy, entitlement and technical enforcement are separate",
        "nodeIds": [
          "request",
          "access",
          "policy-authority",
          "entitlement-authority",
          "access-decision"
        ]
      },
      {
        "id": "PC-SA-P04",
        "title": "Governed consumption",
        "summary": "CEP adapts delivery; port compatibility must be verified",
        "nodeIds": [
          "cep",
          "deliver",
          "interface-binding",
          "consume",
          "contract-id"
        ]
      },
      {
        "id": "PC-SA-P05",
        "title": "Observation and economics",
        "summary": "Execution and delivered Information distinct; X9/P5 transparent",
        "nodeIds": [
          "invocation",
          "information-occurrence",
          "observe",
          "outcome"
        ]
      },
      {
        "id": "PC-SA-P06",
        "title": "Feedback and next decision",
        "summary": "Existing consumption or conditional PDEP handoff",
        "nodeIds": [
          "feedback",
          "reentry",
          "pdep",
          "handoff",
          "composition"
        ]
      }
    ],
    "sc": [
      {
        "id": "PC-SC-P01",
        "title": "Intent and context identity",
        "summary": "Consumer purpose, applicability and constraints",
        "nodeIds": [
          "intent",
          "resolve",
          "product-id"
        ]
      },
      {
        "id": "PC-SC-P02",
        "title": "Product resolution identity",
        "summary": "Product/Version, Promise and family determination",
        "nodeIds": [
          "resolution-set",
          "product-id",
          "prod-authority"
        ]
      },
      {
        "id": "PC-SC-P03",
        "title": "Fitness and authority",
        "summary": "Semantics, method, contract, access and assurance",
        "nodeIds": [
          "semantic-id",
          "sem-authority",
          "contract-id",
          "policy-authority",
          "source-authority"
        ]
      },
      {
        "id": "PC-SC-P04",
        "title": "Access and interface binding",
        "summary": "Decision versus enforcement, realization and CEP",
        "nodeIds": [
          "entitlement-authority",
          "access-decision",
          "interface-binding",
          "cep"
        ]
      },
      {
        "id": "PC-SC-P05",
        "title": "Consumption and execution",
        "summary": "Provider, invocation, delivered Information occurrence",
        "nodeIds": [
          "consume",
          "deliver",
          "invocation",
          "information-occurrence"
        ]
      },
      {
        "id": "PC-SC-P06",
        "title": "Evidence and assessment",
        "summary": "Exact subject, claim, provenance, sufficiency and currentness",
        "nodeIds": [
          "assessment",
          "evidence-service",
          "information-occurrence"
        ]
      },
      {
        "id": "PC-SC-P07",
        "title": "Cost, quality and value",
        "summary": "Indicative X9 vs observed P5, investment authority external",
        "nodeIds": [
          "observe",
          "outcome",
          "investment-authority"
        ]
      },
      {
        "id": "PC-SC-P08",
        "title": "Changed need / handoff",
        "summary": "Conditional re-entry, composition and PDEP without automatic Product qualification",
        "nodeIds": [
          "feedback",
          "reentry",
          "composition",
          "compound",
          "pdep",
          "handoff"
        ]
      }
    ]
  },
  "scenarios": {
    "direct": {
      "name": "Direct existing-Product consumption",
      "description": "A suitable existing governed Product can be consumed directly through supported interfaces. No compulsory PDEP or new owner role.",
      "focus": [
        "consume",
        "deliver",
        "cep",
        "interface-binding",
        "product-id"
      ]
    },
    "access": {
      "name": "Entitlement unresolved",
      "description": "A discovered Product may be promising, but policy and access authority determination must be established or remain unresolved.",
      "focus": [
        "request",
        "access",
        "policy-authority",
        "entitlement-authority",
        "access-decision"
      ]
    },
    "mismatch": {
      "name": "Unmet consumer need",
      "description": "No candidate establishes fit; explore alternatives or propose a conditional PDEP evolution/create referral.",
      "focus": [
        "resolution-set",
        "feedback",
        "pdep",
        "handoff"
      ]
    },
    "composition": {
      "name": "Governed composition",
      "description": "Multiple Products can be consumed together without automatically constituting a Compound Product.",
      "focus": [
        "composition",
        "compound",
        "prod-authority",
        "contract-id"
      ]
    },
    "change": {
      "name": "Material context change",
      "description": "New purpose, definition, Product Version or access context requires targeted re-resolution, not mandatory restart.",
      "focus": [
        "reentry",
        "resolve",
        "semantic-id",
        "contract-id",
        "access-decision"
      ]
    }
  },
  "families": [
    "Data Product",
    "Information Product",
    "AI Product",
    "Compound Product",
    "Other independently qualified family"
  ],
  "personas": [
    "Business",
    "Analytical",
    "AI",
    "System",
    "Agentic"
  ],
  "identities": [
    {
      "title": "Consumer/intent",
      "meaning": "Purpose, context, persona and relevant constraints"
    },
    {
      "title": "Product/Version",
      "meaning": "Exact Product identity, family qualification, version, Promise"
    },
    {
      "title": "Semantics/method",
      "meaning": "Semantic definition and analytical method identity/version"
    },
    {
      "title": "Contract",
      "meaning": "Consumption contract version, purpose and limitations"
    },
    {
      "title": "Entitlement",
      "meaning": "Competent access determination and technical enforcement distinct"
    },
    {
      "title": "Realization/port",
      "meaning": "Supported Product port, provider and realization versions"
    },
    {
      "title": "Execution/Information occurrence",
      "meaning": "Invocation, execution and delivered Information distinguishable"
    },
    {
      "title": "Evidence/assessment/currentness",
      "meaning": "Claim, provenance, evaluation, historical/current applicability"
    }
  ]
} as const;
export type ConsumptionView = 'basic'|'sa'|'sc';
export type ConsumptionScenario = keyof typeof sscfModel.scenarios;
