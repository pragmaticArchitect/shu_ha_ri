import React, {useEffect, useMemo, useState} from 'react';
import {IPCH_GUIDANCE} from './IPChecklistData';
import './IPChecklist.css';

// Experimental worksheet, NOT a normative product-qualification or maturity engine.
type CriterionState = 'unreviewed' | 'supported' | 'partial' | 'failed';
type Assessment = 'unassessed' | 'met' | 'partial' | 'not_met';
type Eligibility = 'unknown' | 'established' | 'not_established';
type EvidenceQuality = 'unknown' | 'adequate' | 'limited';
type CriterionNote = {state: CriterionState; evidence: string};
type CharacteristicNote = {assessment: Assessment; evidenceQuality: EvidenceQuality; notes: string};
type Draft = {
  productId: string;
  productVersion: string;
  eligibility: Eligibility;
  criteria: Record<string, CriterionNote>;
  characteristics: Record<string, CharacteristicNote>;
};
const KEY = 'infops_ipch_worksheet_e0_v1';
const EMPTY: Draft = {productId:'', productVersion:'', eligibility:'unknown', criteria:{}, characteristics:{}};
const ASSESSMENTS: Array<[Assessment,string]> = [['unassessed','—'],['met','MET'],['partial','PARTIAL'],['not_met','NOT_MET']];
const STATES: Array<[CriterionState,string]> = [['unreviewed','Not reviewed'],['supported','Supported'],['partial','Partly supported'],['failed','Not supported']];

function encodeCSV(cell: unknown) { return '"'+String(cell??'').replace(/"/g,'""')+'"'; }
function download(filename: string, content: string, mime: string) {
  const blob = new Blob([content],{type:mime});
  const url=URL.createObjectURL(blob);
  const link=document.createElement('a'); link.href=url; link.download=filename; link.click();
  window.setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function safeDraft(raw: string): Draft {
  try {
    const parsed=JSON.parse(raw);
    if (!parsed || typeof parsed!=='object') return EMPTY;
    const eligibility: Eligibility = ['unknown','established','not_established'].includes(parsed.eligibility)?parsed.eligibility:'unknown';
    return {productId:String(parsed.productId??''), productVersion:String(parsed.productVersion??''),
      eligibility, criteria:(parsed.criteria && typeof parsed.criteria==='object')?parsed.criteria:{},
      characteristics:(parsed.characteristics && typeof parsed.characteristics==='object')?parsed.characteristics:{}};
  } catch {return EMPTY;}
}

export default function IPChecklist() {
  const [draft,setDraft]=useState<Draft>(EMPTY);
  const [loaded,setLoaded]=useState(false);
  const [openCode,setOpenCode]=useState<string>('IPCH01');
  useEffect(()=>{try {const raw=localStorage.getItem(KEY); if(raw)setDraft(safeDraft(raw));}catch{} setLoaded(true);},[]);
  useEffect(()=>{if(!loaded)return;try{localStorage.setItem(KEY,JSON.stringify(draft));}catch{}},[draft,loaded]);
  const setCriterion=(id:string,change:Partial<CriterionNote>)=>setDraft(p=>({...p,criteria:{...p.criteria,[id]:{state:p.criteria[id]?.state??'unreviewed', evidence:p.criteria[id]?.evidence??'',...change}}}));
  const setCharacteristic=(id:string,change:Partial<CharacteristicNote>)=>setDraft(p=>({...p,characteristics:{...p.characteristics,[id]:{assessment:p.characteristics[id]?.assessment??'unassessed',evidenceQuality:p.characteristics[id]?.evidenceQuality??'unknown',notes:p.characteristics[id]?.notes??'',...change}}}));
  const summary=useMemo(()=>IPCH_GUIDANCE.map(g=>{
    const statuses=g.criteria.map(c=>draft.criteria[c.id]?.state??'unreviewed');
    const allSupported=statuses.every(st=>st==='supported');
    const assessed=draft.characteristics[g.code]?.assessment??'unassessed';
    const evidenceQuality=draft.characteristics[g.code]?.evidenceQuality??'unknown';
    const eligible=draft.eligibility==='established'&&Boolean(draft.productId.trim())&&Boolean(draft.productVersion.trim());
    // Do not infer PARTIAL/NOT_MET from atomics: D02 requires a reasoned judgment.
    const eligibleMet=eligible&&allSupported&&evidenceQuality==='adequate';
    const effective: Assessment = assessed==='met'&&!eligibleMet?'unassessed':assessed;
    return {code:g.code,raw:assessed,effective,metBlocked:assessed==='met'&&!eligibleMet,
      metCandidate:eligibleMet, completed:statuses.filter(x=>x!=='unreviewed').length, total:statuses.length};
  }),[draft]);
  const counts=useMemo(()=>({met:summary.filter(x=>x.effective==='met').length, partial:summary.filter(x=>x.effective==='partial').length,
    notMet:summary.filter(x=>x.effective==='not_met').length, pending:summary.filter(x=>x.effective==='unassessed').length}),[summary]);
  const exportPayload=()=>({kind:'INFOPS-IPCH-EXPERIMENTAL-WORKSHEET',schemaVersion:1,subject:{productId:draft.productId,productVersion:draft.productVersion,
    eligibility:draft.eligibility},assessmentMethod:'D02/D03; characteristic-level MET=1 PARTIAL=0.5 NOT_MET=0; no aggregate score, no L0/L1/L2 bands',
    generatedAt:new Date().toISOString(),nonNormative:true,ownerDecision:'D40 accepted guidance; D41 qualified inventory; D42 deferred',
    summary:counts,characteristics:IPCH_GUIDANCE.map((g,i)=>({...g,record:draft.characteristics[g.code]??null,
      effectiveWorksheetFinding:summary[i].effective,metBlocked:summary[i].metBlocked,
      criteria:g.criteria.map(c=>({...c,record:draft.criteria[c.id]??null}))}))});
  const exportCSV=()=>{
    const out=[['Product ID','Product Version','Eligibility','IPCH','Characteristic','Criterion ID','Mandatory criterion','Criterion status','Criterion evidence','Proposed finding','Effective worksheet finding','Evidence quality','Characteristic notes'].map(encodeCSV).join(',')];
    IPCH_GUIDANCE.forEach((g,i)=>g.criteria.forEach(c=>{const r=draft.criteria[c.id];const ch=draft.characteristics[g.code];out.push([
      draft.productId,draft.productVersion,draft.eligibility,g.code,g.name,c.id,c.label,r?.state??'unreviewed',r?.evidence??'',
      ch?.assessment??'unassessed',summary[i].effective,ch?.evidenceQuality??'unknown',ch?.notes??''
    ].map(encodeCSV).join(','));}));
    download('infops_ipch_experimental_worksheet.csv',out.join('\r\n'),'text/csv;charset=utf-8');
  };
  const reset=()=>{if(!window.confirm('Clear this browser’s INFOPS IPCH checklist answers?'))return;setDraft({...EMPTY});};
  return <section className="ipc-root">
    <div className="ipc-top"><div><h1>📊 Information Product Maturity Checklist</h1>
      <p>INFOPS 0.1 · IPCH01–IPCH16 · <strong>Experimental, non-normative worksheet</strong></p></div>
      <div className="ipc-actions"><button type="button" className="button button--primary" onClick={()=>download('infops_ipch_experimental_worksheet.json',JSON.stringify(exportPayload(),null,2),'application/json')}>Export JSON</button>
        <button type="button" className="button button--secondary" onClick={exportCSV}>Export CSV</button>
        <button type="button" className="button button--danger button--outline" onClick={reset}>Reset</button></div></div>
    <p className="ipc-alert"><strong>Assessment boundary:</strong> This worksheet does not establish Information Product qualification, independent semantic authority, operational conformance, or release certification. D02 Product/Version eligibility and competent evidence review apply. Each IPCH is assessed conjunctively; there are <strong>no characteristic weights, aggregate maturity percentages, or L0/L1/L2 thresholds</strong>. Local entries are not verified evidence.</p>
    <div className="ipc-subject">
      <label>Product identity <input value={draft.productId} onChange={e=>setDraft(p=>({...p,productId:e.target.value}))} placeholder="Exact Product ID"/></label>
      <label>Product version <input value={draft.productVersion} onChange={e=>setDraft(p=>({...p,productVersion:e.target.value}))} placeholder="Exact Product Version"/></label>
      <label>Independent Product/Version eligibility <select value={draft.eligibility} onChange={e=>setDraft(p=>({...p,eligibility:e.target.value as Eligibility}))}>
          <option value="unknown">Not established / unknown</option><option value="established">Established by competent authority (self-reported)</option>
          <option value="not_established">Not established</option>
        </select></label>
    </div>
    {draft.eligibility!=='established'&&<p className="ipc-warning">D02 eligibility has not been established. Characteristic entries remain working notes and must not be interpreted as actual maturity findings; the Product is <strong>NOT_ASSESSABLE</strong> for this worksheet.</p>}
    <div className="ipc-counts" aria-label="Worksheet tally — not a maturity score">
      <span><strong>{counts.met}</strong> candidate MET</span><span><strong>{counts.partial}</strong> noted PARTIAL</span>
      <span><strong>{counts.notMet}</strong> noted NOT_MET</span><span><strong>{counts.pending}</strong> unassessed / gated</span>
    </div>
    <div className="ipc-scroll"><table className="table ipc-table"><thead><tr>
      <th>#</th><th>IPCH</th><th>Characteristic</th><th>Assessment checklist</th><th>Supported only when…</th><th>Finding</th><th>Evidence (URL or notes)</th><th>Evidence quality</th></tr></thead>
      <tbody>{IPCH_GUIDANCE.map((g,i)=>{
        const ch=draft.characteristics[g.code];const sm=summary[i];
        return <React.Fragment key={g.code}><tr className="ipc-mainrow"><td>{i+1}</td><td><code>{g.code}</code></td>
          <td><strong>{g.name}</strong><a className="ipc-guide" href={g.guide}>Guidance ↗</a></td>
          <td><button type="button" className="ipc-expand" aria-expanded={openCode===g.code} onClick={()=>setOpenCode(openCode===g.code?'':g.code)}>
            {openCode===g.code?'▾':'▸'} {g.criteria.length} mandatory criteria ({sm.completed} reviewed)</button></td>
          <td className="ipc-condition">All {g.criteria.length} mandatory criteria supported for candidate MET; independent evidence, eligibility and applicable boundary checks required.</td>
          <td><fieldset className="ipc-radios"><legend className="sr-only">Proposed status {g.code}</legend>
            {ASSESSMENTS.map(([val,label])=><label key={val}><input type="radio" name={`assess-${g.code}`} value={val}
              checked={(ch?.assessment??'unassessed')===val} onChange={()=>setCharacteristic(g.code,{assessment:val})}/>{label}</label>)}
            </fieldset>{sm.metBlocked&&<small className="ipc-blocked">MET gated: complete criteria, evidence and Product identity</small>}
            {sm.effective==='met'&&<small className="ipc-candidate">Candidate only — not certified</small>}</td>
          <td><textarea rows={2} aria-label={`Notes for ${g.code}`} placeholder="Claim evidence; caveats" value={ch?.notes??''} onChange={e=>setCharacteristic(g.code,{notes:e.target.value})}/></td>
          <td><select aria-label={`Evidence quality ${g.code}`} value={ch?.evidenceQuality??'unknown'} onChange={e=>setCharacteristic(g.code,{evidenceQuality:e.target.value as EvidenceQuality})}>
            <option value="unknown">Not reviewed</option><option value="adequate">Adequate (self-reported)</option><option value="limited">EVIDENCE_LIMITED</option></select></td></tr>
          {openCode===g.code&&<tr><td colSpan={8}><div className="ipc-criteria">
            <p><strong>{g.code} mandatory evidence checklist.</strong> Criterion entries support a reasoned characteristic-level finding; they are not separately weighted or averaged. A criterion marked “Not supported” does not mechanically assign PARTIAL or NOT_MET.</p>
            {g.criteria.map(c=>{const r=draft.criteria[c.id];return <div className="ipc-criterion" key={c.id}>
              <div><strong>{c.id}: {c.label}</strong><p>{c.required}</p></div>
              <select aria-label={`Evidence support for ${c.id}`} value={r?.state??'unreviewed'} onChange={e=>setCriterion(c.id,{state:e.target.value as CriterionState})}>
                {STATES.map(([v,l])=><option key={v} value={v}>{l}</option>)}</select>
              <input aria-label={`Evidence reference for ${c.id}`} placeholder="Evidence URL, ID or limitation" value={r?.evidence??''} onChange={e=>setCriterion(c.id,{evidence:e.target.value})}/></div>})}
          </div></td></tr>}</React.Fragment>;
      })}</tbody></table></div>
    <details className="ipc-details"><summary>Assessment guidance and safeguards</summary>
      <p><strong>MET (1.0)</strong> requires all applicable mandatory claims and adequate evidence; a self-reported MET is gated above until all criterion entries are supported and exact eligible Product/Version and adequate evidence are specified. <strong>PARTIAL (0.5)</strong> and <strong>NOT_MET (0.0)</strong> require a reasoned substantive assessment; they are not automatically inferred from criterion counts.</p>
      <p><strong>EVIDENCE_LIMITED</strong> is independent of the score. <strong>NOT_ASSESSABLE</strong> applies where competent eligibility is not established. There is no blanket <strong>NOT_APPLICABLE</strong>. Conditional branches, such as IOC-M07, require an applicability judgment within the mandatory criterion.</p>
      <p>Evidence, ownership, semantically authoritative definitions, Product-family qualification and policy/assurance remain independent. IPCH01 has a DRAFT-02 qualified history; later guides are accepted experimental drafts. D41 is reconciled with qualifications; D42 verification was deferred to the 1.0 backlog. No live validation or normative release is implied.</p>
    </details>
    <details className="ipc-details"><summary>Suggested follow-up work (unassessed or weak evidence)</summary><ul>
      {IPCH_GUIDANCE.filter((g,i)=>summary[i].effective!=='met').map(g=><li key={g.code}><strong>{g.code} — {g.name}:</strong> review mandatory criteria and Product/Version evidence against the <a href={g.guide}>accepted experimental guidance</a>; preserve open research qualifications.</li>)}
    </ul></details>
    <p className="ipc-foot">Data is stored only in this browser’s localStorage. Exported files contain any Product IDs and evidence notes you entered; handle them under your organization’s information-handling rules.</p>
  </section>;
}
