/** INFOPS 0.1 ACT1-SA-D01/D02/D03 experimental E0: visualization metadata, not a normative lifecycle. */
export type SAPath = 'consume' | 'evolve' | 'create';
export type SALane = 'creator' | 'pdep' | 'authority' | 'artifact';
export type SAKind = 'actor' | 'capability' | 'authority' | 'service' | 'artifact' | 'outcome';
export type SAEdgeKind = 'declares' | 'resolves' | 'determines' | 'produces_or_references' | 'observes_or_hands_off';
export type SANode = {id:string;lane:SALane;title:string;subtitle:string;kind:SAKind;description:string;boundary?:string;paths?:SAPath[]};
export type SAEdge = {id:string;from:string;to:string;kind:SAEdgeKind;label:string;description:string;paths?:SAPath[];conditional?:boolean};
export type SAMoment = {id:string;title:string;grouping:string;narrative:string;nodeIds:string[];edgeIds:string[];reentryTo?:string};
export const saPaths:SAPath[]=['consume','evolve','create'];
export const saPathTitles:Record<SAPath,string>={consume:'Consume existing',evolve:'Evolve existing',create:'Create candidate'};
export const saLanes:{id:SALane;title:string;description:string}[]=[
 {id:'creator',title:'L1 · Product Owner / Symbiant',description:'Intent, Promise, analytical expectations and evolution'},
 {id:'pdep',title:'L2 · HDIP PDEP',description:'Shared discovery, guided definition, validation and realization support'},
 {id:'authority',title:'L3 · Independent Authorities & Shared Services',description:'Competent determinations are distinct from service lookups'},
 {id:'artifact',title:'L4 · Governed Artifacts & Outcomes',description:'Identity, contracts, evidence, realization, exposure and observation'}
];
const ec:SAPath[]=['evolve','create'];
export const saNodes:SANode[]=[
 {id:'c-need',lane:'creator',title:'Informational need',subtitle:'Purpose · consumers · value',kind:'actor',description:'Owner expresses the informational need, intended use and expected benefit.'},
 {id:'c-path',lane:'creator',title:'Product path',subtitle:'Consume · evolve · create',kind:'actor',description:'Exploration choice only; not Product qualification or entitlement.'},
 {id:'c-promise',lane:'creator',title:'Informational Promise',subtitle:'Meaning · purpose · limitations',kind:'actor',description:'Owner expresses the governing informational proposition and expected consumer interpretation.',paths:ec},
 {id:'c-meaning',lane:'creator',title:'Analytical expectations',subtitle:'Measures · method · assumptions',kind:'actor',description:'Owner declares measures, intended analytical meaning and interpretation expectations.',paths:ec},
 {id:'c-assert',lane:'creator',title:'Information assertions',subtitle:'Validity · explanation · evidence',kind:'actor',description:'Owner formulates expectations, not verified conformance.',paths:ec},
 {id:'c-use',lane:'creator',title:'Consumption expectations',subtitle:'Contract · usage limitations',kind:'actor',description:'Owner proposes intended contract obligations; entitlement is separate.'},
 {id:'c-review',lane:'creator',title:'Decide and evolve',subtitle:'Responsible owner review',kind:'actor',description:'Owner evaluates outcomes, unresolved questions and material change.',paths:ec},
 {id:'h-discover',lane:'pdep',title:'Guided Product discovery',subtitle:'Find existing capabilities',kind:'capability',description:'HDIP surfaces available Products and compatibility evidence; discovery may terminate in consumption.'},
 {id:'h-design',lane:'pdep',title:'Guided design',subtitle:'Product context and dependencies',kind:'capability',description:'HDIP helps express an Information-specific definition without assuming Productness.',paths:ec},
 {id:'h-semantic',lane:'pdep',title:'Semantic resolution',subtitle:'Lookups · references · conflicts',kind:'capability',description:'HDIP resolves semantic and analytical references; it does not approve the meanings.',paths:ec},
 {id:'h-validate',lane:'pdep',title:'Assertions and evidence',subtitle:'Candidate tests · traceability',kind:'capability',description:'Assist checks and evidence preparation; verification is not inferred.',paths:ec},
 {id:'h-policy',lane:'pdep',title:'Policy orchestration',subtitle:'Applicable controls and contracts',kind:'capability',description:'Resolve and support enforcement of policies determined by competent authorities.'},
 {id:'h-econ',lane:'pdep',title:'X9 indicative economics',subtitle:'Evolving estimates · alternatives',kind:'capability',description:'Expose indicative feasibility and costs without assuming or granting investment approval.'},
 {id:'h-compile',lane:'pdep',title:'Compilation support',subtitle:'Eligible design inputs',kind:'capability',description:'Compile or associate eligible realization inputs; does not manufacture authority or Product identity.',paths:ec},
 {id:'h-pfi',lane:'pdep',title:'PFI realization options',subtitle:'Technical binding and feasibility',kind:'capability',description:'Resolve feasible implementation options distinct from Product semantics.',paths:ec},
 {id:'h-publish',lane:'pdep',title:'Governed publication support',subtitle:'Registration · exposure',kind:'capability',description:'Coordinate authorized realization, registration and discoverability; no automatic entitlement.',paths:ec},
 {id:'h-observe',lane:'pdep',title:'P5 observation',subtitle:'Quality · actual cost · value',kind:'capability',description:'Surface observed outcomes and support evolution or renewed consumption.'},
 {id:'a-product',lane:'authority',title:'Product qualification authority',subtitle:'BPS/PIN · family · Compound',kind:'authority',description:'Competent Productness and family determinations remain independent.',boundary:'The FlowPlayer cannot qualify a Product.',paths:ec},
 {id:'a-semantic',lane:'authority',title:'Semantic and analytical authority',subtitle:'GEARA/GEARM',kind:'authority',description:'Governs applicable semantic definitions, measures and analytical methods.',boundary:'Lookup is not semantic approval.',paths:ec},
 {id:'a-policy',lane:'authority',title:'Policy and assurance authority',subtitle:'Privacy · policy · controls',kind:'authority',description:'Determines applicable policy, legal, risk and assurance requirements.',boundary:'Automation does not grant exceptions or entitlement.'},
 {id:'a-invest',lane:'authority',title:'Investment authority boundary',subtitle:'Enterprise-specific, where applicable',kind:'authority',description:'Funding and expenditure authority remains external; no universal gate or threshold.',boundary:'Cost information is not financing authorization.'},
 {id:'s-registry',lane:'authority',title:'Catalogues and registries',subtitle:'Shared evidence and discovery services',kind:'service',description:'Records and exposes references; it is not automatically the competent decision authority.'},
 {id:'r-intent',lane:'artifact',title:'Intent & Product context',subtitle:'Candidate intent record',kind:'artifact',description:'Declared need and path intent, not a Productness determination.'},
 {id:'r-product',lane:'artifact',title:'Product / Version & qualification',subtitle:'Independent identity and evidence',kind:'artifact',description:'Product identity/version and qualification evidence kept distinct from compilation.',paths:ec},
 {id:'r-semantic',lane:'artifact',title:'Semantic definition & method',subtitle:'Governed references and versions',kind:'artifact',description:'Distinct semantic-definition version and analytical-method references.',paths:ec},
 {id:'r-assert',lane:'artifact',title:'Information assertion evidence',subtitle:'Expectations ≠ passed checks',kind:'artifact',description:'Assertions, provenance, explainability and assessment evidence are separately attributable.',paths:ec},
 {id:'r-contract',lane:'artifact',title:'Consumption contract',subtitle:'Use expectations and obligations',kind:'artifact',description:'Existing or candidate contract; access entitlement is separately governed.'},
 {id:'r-infoprod',lane:'artifact',title:'INFOPROD',subtitle:'Product semantic description',kind:'artifact',description:'Governing Information Product description, distinct from deployable specification.',paths:ec},
 {id:'r-infopds',lane:'artifact',title:'INFOPDS',subtitle:'Deployable realization specification',kind:'artifact',description:'Distinct deployable specification; does not itself qualify an Information Product.',paths:ec},
 {id:'r-dpp',lane:'artifact',title:'DPP context',subtitle:'Distinct package/provenance duties',kind:'artifact',description:'Applicable BPS DPP duties remain distinct; no automatic attestation or conformance.',paths:ec},
 {id:'r-compile',lane:'artifact',title:'Compilation / PFI evidence',subtitle:'Realization and binding records',kind:'artifact',description:'Compilation and PFI records are distinct from Product and semantic-definition versions.',paths:ec},
 {id:'r-publish',lane:'artifact',title:'Published Product projection',subtitle:'Marketplace · interface',kind:'outcome',description:'Discoverability is not consumption entitlement.',paths:ec},
 {id:'r-sscf',lane:'artifact',title:'Generic SSCF / CEP',subtitle:'Consumption handoff',kind:'outcome',description:'The consumer experience is family-neutral; no new Product is required by the Consume path.'},
 {id:'r-runtime',lane:'artifact',title:'Runtime occurrence',subtitle:'Observed execution ≠ Product Version',kind:'artifact',description:'An occurrence or operational event is not an approved Product assessment.'},
 {id:'r-signals',lane:'artifact',title:'P5 outcomes and value',subtitle:'Usage · cost · quality',kind:'outcome',description:'Observed value, cost and quality feed accountable evolution and re-entry.'}
];
const makeEdge=(id:string,from:string,to:string,kind:SAEdgeKind,label:string,description:string,paths?:SAPath[],conditional=false):SAEdge=>({id,from,to,kind,label,description,paths,conditional});
export const saEdges:SAEdge[]=[
 makeEdge('e01','c-need','h-discover','declares','Need','Owner expresses an informational need.'),
 makeEdge('e02','h-discover','s-registry','resolves','Search','HDIP retrieves governed Product references.'),
 makeEdge('e03','h-discover','c-path','resolves','Options','Discovery surfaces alternatives.'),
 makeEdge('e04','c-need','r-intent','declares','Intent','Owner-declared intent record.'),
 makeEdge('e05','c-path','r-sscf','observes_or_hands_off','Consume','Existing Product leads to SSCF without new creation.',['consume']),
 makeEdge('e06','a-policy','h-policy','determines','Obligations','Applicable access and policy authority.'),
 makeEdge('e07','h-policy','r-contract','resolves','Contract','Interpret existing or proposed use obligations.'),
 makeEdge('e08','r-contract','r-sscf','observes_or_hands_off','Use','Contract context accompanies consumption.'),
 makeEdge('e09','c-promise','h-design','declares','Promise','Owner expresses informational Promise.',ec),
 makeEdge('e10','h-design','a-product','resolves','Qualification','HDIP presents Product context for independent determination.',ec,true),
 makeEdge('e11','a-product','r-product','determines','Identity','Competent qualification evidence and Product identity.',ec,true),
 makeEdge('e12','c-meaning','h-semantic','declares','Meaning','Owner supplies proposed definitions and analytic assumptions.',ec),
 makeEdge('e13','h-semantic','a-semantic','resolves','Reference','Resolve governing semantic and method references.',ec),
 makeEdge('e14','a-semantic','r-semantic','determines','Governed meaning','Competent semantic/analytical determination.',ec,true),
 makeEdge('e15','h-design','r-infoprod','produces_or_references','Product description','Associate separately governed Product semantics.',ec),
 makeEdge('e16','c-assert','h-validate','declares','Assertions','Owner declares validity/evidence expectations.',ec),
 makeEdge('e17','h-validate','r-assert','produces_or_references','Evidence','Prepare candidate checks and evidence links, not passed assessment.',ec),
 makeEdge('e18','c-use','h-policy','declares','Intended use','Owner specifies consumption expectations.'),
 makeEdge('e19','a-policy','r-contract','determines','Policy','Independent obligations shape contract.',undefined,true),
 makeEdge('e20','h-econ','a-invest','resolves','X9 support','Economics may inform enterprise-specific finance decisions.',undefined,true),
 makeEdge('e21','h-design','h-econ','resolves','Feasibility','Progressively refine indicative economic evidence.',ec),
 makeEdge('e22','h-design','h-compile','resolves','Eligible inputs','Conditional realization preparation only.',ec,true),
 makeEdge('e23','h-compile','r-infopds','produces_or_references','Deployable spec','Associate INFOPDS realization specifications.',ec),
 makeEdge('e24','h-compile','r-compile','produces_or_references','Compilation','Separate compilation and realization evidence.',ec),
 makeEdge('e25','h-compile','h-pfi','resolves','PFI options','Resolve implementation binding candidates.',ec),
 makeEdge('e26','h-pfi','r-compile','produces_or_references','Binding','PFI realization evidence is separately tracked.',ec),
 makeEdge('e27','r-infoprod','r-dpp','produces_or_references','Packaging context','Applicable DPP responsibilities without automatic conformance.',ec,true),
 makeEdge('e28','h-publish','r-publish','produces_or_references','Exposure','Coordinate authorized publication, where eligible.',ec,true),
 makeEdge('e29','r-publish','r-sscf','observes_or_hands_off','Discover','Published Product may be discovered via SSCF.',ec),
 makeEdge('e30','r-sscf','r-runtime','observes_or_hands_off','Use','Conceptual runtime occurrence evidence; not an execution call.'),
 makeEdge('e31','r-runtime','h-observe','observes_or_hands_off','Signals','Observed operations inform P5.'),
 makeEdge('e32','h-observe','r-signals','produces_or_references','Value','Observed cost, quality, usage and value.'),
 makeEdge('e33','r-signals','c-review','observes_or_hands_off','Evolution','Owner receives evidence for evolution.',ec),
 makeEdge('e34','r-signals','h-discover','observes_or_hands_off','Re-entry','Revisit the earliest materially affected responsibility.'),
 makeEdge('e35','h-design','r-semantic','produces_or_references','References','Link authoritative semantic definition versions.',ec),
 makeEdge('e36','r-contract','r-infoprod','produces_or_references','Contract link','Preserve applicable consumption-contract link.',ec),
];
const mm=(id:string,title:string,grouping:string,narrative:string,nodeIds:string[],edgeIds:string[],reentryTo?:string):SAMoment=>({id,title,grouping,narrative,nodeIds,edgeIds,reentryTo});
const start=(path:SAPath):SAMoment[]=>[
 mm('SA-P01','Explore informational need','Intent & Proposition','The creator expresses consumer need and intended outcome; HDIP explores available capabilities and X9 can inform early feasibility.',['c-need','h-discover','r-intent','h-econ'],['e01','e04']),
 mm('SA-P02','Resolve Product path','Guided Design & Definition',path==='consume'?'Existing governed Product fits the need. The creator explores contract and SSCF consumption without new Product creation.':path==='evolve'?'An existing Product is selected for change; Product/Version and qualification implications remain independently assessed.':'Intentional new Product candidacy is explored; family and Productness remain independently determined.',['h-discover','s-registry','c-path',...(path==='consume'?['r-sscf']:['a-product','r-product'])],['e02','e03',...(path==='consume'?['e05']:['e10','e11'])])
];
export function saMoments(path:SAPath):SAMoment[] {
 const consume=path==='consume'; const evolve=path==='evolve';
 return [
 ...start(path),
 mm('SA-P03',consume?'Interpret existing Product Promise':'Shape informational Promise','Guided Design & Definition',consume?'Inspect existing Product semantics and contract; no new informational Promise or Product identity is manufactured.':evolve?'Owner revises an existing informational Promise, with material changes subject to identity/version reassessment.':'Owner declares a candidate informational Promise, including consumer purpose and limitations.',consume?['r-contract','h-discover','r-sscf']:['c-promise','h-design','r-infoprod','a-product'],consume?['e08']:['e09','e15']),
 mm('SA-P04',consume?'Review governed meaning':'Ground semantics and analytical meaning','Guided Design & Definition',consume?'Interpret existing authoritative definitions and analytical limitations; do not invent new semantic approvals.':'Resolve authoritative semantic and analytical definitions, including method and definition-version distinctions.',consume?['r-contract','s-registry','r-sscf']:['c-meaning','h-semantic','a-semantic','r-semantic'],consume?['e08']:['e12','e13','e14','e35']),
 mm('SA-P05',consume?'Assess existing evidence':'Establish assertions and evidence expectations','Dependency / Policy Compatibility',consume?'Examine existing Product fit and relevant evidence. New Information Product tests are not required by the Consume visualization.':'Owner declares information assertions; HDIP prepares checks, provenance and explainability evidence without claiming tests have passed.',consume?['r-contract','s-registry']:['c-assert','h-validate','r-assert','a-semantic'],consume?['e07']:['e16','e17']),
 mm('SA-P06',consume?'Resolve use and entitlement context':'Resolve policy and consumption contracts','Dependency / Policy Compatibility',consume?'Existing contracts, independently governed entitlements and policy apply before SSCF consumption.':'Declared usage expectations are evaluated against applicable independent policy and consumption-contract authority.',consume?['c-use','h-policy','a-policy','r-contract','r-sscf']:['c-use','h-policy','a-policy','r-contract','r-infoprod'],consume?['e18','e06','e07','e08']:['e18','e06','e19','e07','e36']),
 mm('SA-P07','Evaluate feasibility and indicative economics','Governed Readiness & Decision Support',consume?'Reuse and consumption have economic implications. X9 remains informative; investment approval remains enterprise-specific.':'PDEP provides indicative cost/feasibility and alternatives; optional enterprise investment determinations remain external.',consume?['h-econ','a-invest','r-sscf']:['h-design','h-econ','a-invest','r-product'],consume?['e20']:['e21','e20']),
 mm('SA-P08',consume?'No new Product compilation':'Compile and resolve realization','Automated Assembly & Compilation',consume?'Handoff to generic SSCF: no new INFOPROD, INFOPDS, compilation or Product deployment implied.':evolve?'Only materially impacted eligible realization is reconsidered; Product identity, semantic version and deployment remain distinct.':'Eligible design inputs may be compiled and associated with separate INFOPROD, INFOPDS, DPP and PFI records; compilation cannot qualify a Product.',consume?['r-sscf','r-contract']:['h-compile','h-pfi','r-infoprod','r-infopds','r-dpp','r-compile'],consume?['e08']:['e22','e23','e24','e25','e26','e27']),
 mm('SA-P09',consume?'Handoff to generic SSCF':'Coordinate governed publication','Publish / Realize',consume?'Consume the existing governed Product via SSCF/CEP, subject to applicable rights; nothing is published by this path.':'HDIP may coordinate authorized publication, Product registry projection and interface exposure; publication does not grant entitlement.',consume?['r-contract','r-sscf','a-policy']:['h-publish','r-publish','r-sscf','a-policy'],consume?['e08']:['e28','e29']),
 mm('SA-P10','Observe outcomes and evolve','Feedback / Evolution / Re-entry','P5 exposes observed cost, quality, consumption and value. Re-entry may revisit discovery or any materially affected prior responsibility; it is not a mandatory restart.',consume?['r-sscf','r-runtime','h-observe','r-signals','h-discover']:['r-runtime','h-observe','r-signals','c-review','h-discover'],consume?['e30','e31','e32','e34']:['e30','e31','e32','e33','e34'],'SA-P02')
 ];
}
export function visibleSANodes(path:SAPath){return saNodes.filter(n=>!n.paths||n.paths.includes(path));}
export function visibleSAEdges(path:SAPath){const ids=new Set(visibleSANodes(path).map(n=>n.id));return saEdges.filter(e=>(!e.paths||e.paths.includes(path))&&ids.has(e.from)&&ids.has(e.to));}
