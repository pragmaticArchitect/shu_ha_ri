/** INFOPS ACT1-G0-D02 approved experimental illustration; not a normative lifecycle. */
export type Path = 'consume' | 'evolve' | 'create';
export type Lane = 'creator' | 'pdep' | 'authority' | 'outcome';
export type FlowNode = {id:string; lane:Lane; title:string; note:string; detail:string};
export type FlowEdge = {id:string; from:string; to:string; label:string; paths?:Path[]};
export type Moment = {id:string; title:string; narrative:string; grouping:string; nodes:string[]; edges:string[]};
export const lanes: {id:Lane; title:string; description:string}[] = [
  {id:'creator',title:'Product Owner / Symbiant',description:'Intent, Promise, value and evolution'},
  {id:'pdep',title:'HDIP PDEP',description:'Governed discovery, validation, compilation and realization support'},
  {id:'authority',title:'Independent Authorities & Shared Services',description:'Qualification, semantics, policy, finance and assurance'},
  {id:'outcome',title:'Product Outcomes',description:'Consumption, Product exposure, evidence and evolution'}
];
export const nodes:FlowNode[] = [
  {id:'intent',lane:'creator',title:'Informational need',note:'Purpose · consumers · expected value',detail:'The creator expresses the informational need, purpose, intended consumers and anticipated value.'},
  {id:'choice',lane:'creator',title:'Choose Product path',note:'Consume · evolve · create',detail:'Discovery does not force new Product creation. The path is an exploration choice, not a qualification determination.'},
  {id:'promise',lane:'creator',title:'Informational Promise',note:'Meaning · analytics · limitations',detail:'The accountable Product Owner shapes the Product Promise, consumer context, methods, measures, assertions and interpretation.'},
  {id:'feedback',lane:'creator',title:'Review & evolve',note:'Change intent when needed',detail:'Observed effectiveness and value may trigger re-entry at the earliest materially affected responsibility.'},
  {id:'discovery',lane:'pdep',title:'Guided discovery',note:'Find existing governed Products',detail:'Search across qualified Product families and assess fit for consumption, evolution or intentional creation.'},
  {id:'design',lane:'pdep',title:'Guided design',note:'Dependencies · explanation · contracts',detail:'Assisted definition captures analytical assertions, evidence, consumption expectations and applicable dependencies.'},
  {id:'readiness',lane:'pdep',title:'Compatibility & readiness',note:'Unresolved holds made visible',detail:'Surface semantic, policy and Product qualification requirements; do not silently grant authority.'},
  {id:'compile',lane:'pdep',title:'Compile & resolve PFI',note:'Realization choices · not qualification',detail:'Prepare realization inputs and resolve feasible execution choices. Compilation cannot confer Productness or semantic authority.'},
  {id:'publish',lane:'pdep',title:'Governed publish support',note:'When applicable requirements are met',detail:'Coordinate eligible realization, registration and interface exposure; publication does not grant consumption entitlement.'},
  {id:'qualification',lane:'authority',title:'Product qualification',note:'BPS/PIN · family · Compound',detail:'Independent competent Productness, Information-family and Compound determinations, only where applicable.'},
  {id:'semantics',lane:'authority',title:'Semantic & analytical authority',note:'GEARA/GEARM · governed meanings',detail:'Authoritative semantics and analytical methods remain external to self-service automation.'},
  {id:'policy',lane:'authority',title:'Policy & assurance',note:'Legal · security · consequential decisions',detail:'Applicable privacy, policy, access and assurance decisions remain independently governed.'},
  {id:'economics',lane:'authority',title:'Economic authority boundary',note:'X9 costs visible · funding enterprise-specific',detail:'Indicative economic evidence is supplied by PDEP; investment authorization, thresholds and budgets remain enterprise-specific.'},
  {id:'sscf',lane:'outcome',title:'Existing Product → SSCF',note:'Consumption; no new Product inferred',detail:'Consume a discovered Product through generic HDIP SSCF and CEP, subject to applicable entitlements.'},
  {id:'artifacts',lane:'outcome',title:'INFOPROD ≠ INFOPDS',note:'Product meaning ≠ deployable spec',detail:'Preserve separately governed Product/Version, semantic definitions, INFOPROD, INFOPDS, compilation, PFI and runtime evidence.'},
  {id:'available',lane:'outcome',title:'Governed Product exposure',note:'Registry · marketplace · interface',detail:'An eligible new or evolved Information Product may become discoverable through governed publication. Mere interface creation is not Product qualification.'},
  {id:'signals',lane:'outcome',title:'P5 outcomes & value',note:'Usage · cost · quality · outcomes',detail:'Actual consumption, observed costs, value, interpretive quality and evidence support future evolution.'},
];
export const edges:FlowEdge[] = [
  {id:'a',from:'intent',to:'discovery',label:'discover'},
  {id:'b',from:'discovery',to:'choice',label:'options'},
  {id:'c',from:'choice',to:'sscf',label:'consume',paths:['consume']},
  {id:'d',from:'choice',to:'promise',label:'shape',paths:['evolve','create']},
  {id:'e',from:'promise',to:'design',label:'design',paths:['evolve','create']},
  {id:'f',from:'semantics',to:'readiness',label:'meaning',paths:['evolve','create']},
  {id:'g',from:'qualification',to:'readiness',label:'qualification',paths:['evolve','create']},
  {id:'h',from:'policy',to:'readiness',label:'obligations',paths:['evolve','create']},
  {id:'i',from:'design',to:'readiness',label:'validate',paths:['evolve','create']},
  {id:'j',from:'readiness',to:'compile',label:'eligible design',paths:['evolve','create']},
  {id:'k',from:'economics',to:'compile',label:'indicative economics',paths:['evolve','create']},
  {id:'l',from:'compile',to:'artifacts',label:'separate',paths:['evolve','create']},
  {id:'m',from:'compile',to:'publish',label:'support',paths:['evolve','create']},
  {id:'n',from:'publish',to:'available',label:'authorized exposure',paths:['evolve','create']},
  {id:'o',from:'sscf',to:'signals',label:'observed use',paths:['consume']},
  {id:'p',from:'available',to:'signals',label:'observed use',paths:['evolve','create']},
  {id:'q',from:'signals',to:'feedback',label:'learn'},
  {id:'r',from:'feedback',to:'discovery',label:'re-enter'}
];
const sharedStart:Moment[] = [
  {id:'P01',title:'Express informational need',grouping:'Intent & Proposition',narrative:'The Symbiant articulates an informational need, intended consumers and expected value. X9 indicative economics can begin here.',nodes:['intent','economics'],edges:['a']},
  {id:'P02',title:'Discover existing Products',grouping:'Guided Design & Definition',narrative:'Discover Product capabilities across families. An existing Product may already satisfy the need without creating anything new.',nodes:['intent','discovery','choice'],edges:['a','b']},
];
export const pathLabels:Record<Path,string> = {consume:'Consume existing',evolve:'Evolve existing',create:'Create candidate'};
export function moments(path:Path):Moment[] {
  const isConsume=path==='consume'; const isEvolve=path==='evolve';
  const qualifier=isEvolve?'An existing Product is reconsidered; identity and version changes require assessment.':'A proposed new Information Product must be independently qualified where applicable.';
  return [
    ...sharedStart,
    {id:'P03',title:'Choose Product path',grouping:'Guided Design & Definition',narrative:isConsume?'The existing Product meets the need. Handoff to SSCF/CEP; do not infer a new Product.':qualifier,nodes:isConsume?['choice','sscf']:['choice','promise','qualification'],edges:isConsume?['b','c']:['b','d']},
    {id:'P04',title:isConsume?'Interpret the existing contract':'Define informational Promise',grouping:'Guided Design & Definition',narrative:isConsume?'Review fit, meaning and consumer contract under the existing Product authority. No new Product definition is imposed.':'Define or evolve governing informational meaning, analytical measures, assumptions, limitations, consumer contract and evidence.',nodes:isConsume?['sscf','semantics']:['promise','design','semantics'],edges:isConsume?['c']:['d','e']},
    {id:'P05',title:isConsume?'Confirm governed consumption':'Resolve compatibility and governance',grouping:'Dependency / Policy Compatibility',narrative:isConsume?'SSCF handles independently governed access, policy and entitlements. Publication does not confer access.':'PDEP surfaces semantic, dependency, policy and qualification holds; authority is not granted by automation.',nodes:isConsume?['sscf','policy']:['design','readiness','qualification','semantics','policy'],edges:isConsume?['c']:['f','g','h','i']},
    {id:'P06',title:isConsume?'Handoff to generic SSCF':'Prepare governed realization',grouping:'Automated Assembly & Compilation · Governed Readiness & Decision Support',narrative:isConsume?'The creator becomes a consumer through SSCF/CEP; this is a conceptual handoff, not an integration call.':'PDEP supports compilation and PFI resolution, showing refined indicative costs; no universal investment approval gate.',nodes:isConsume?['sscf','economics']:['readiness','compile','economics','artifacts'],edges:isConsume?['c']:['j','k','l']},
    {id:'P07',title:isConsume?'Consume under applicable entitlement':'Realize and make discoverable',grouping:'Publish / Realize',narrative:isConsume?'The already governed Product is consumed via SSCF, subject to entitlements. No new registration or Product identity is implied.':'Only when applicable requirements are satisfied, support realization, registration and exposure; publication is not entitlement.',nodes:isConsume?['sscf','policy']:['compile','publish','available','artifacts'],edges:isConsume?['c']:['m','n']},
    {id:'P08',title:'Observe value and evolve',grouping:'Feedback / Evolution / Re-entry',narrative:'P5 captures usage, information quality, actual cost, outcome and value signals. The creator may re-enter at the earliest materially affected responsibility.',nodes:isConsume?['sscf','signals','feedback','discovery']:['available','signals','feedback','discovery'],edges:isConsume?['o','q','r']:['p','q','r']}
  ];
}
