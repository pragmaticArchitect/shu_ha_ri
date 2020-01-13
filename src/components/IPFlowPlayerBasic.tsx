import React, {useEffect, useMemo, useRef, useState} from 'react';
import {edges, lanes, nodes, moments, pathLabels, type Path} from '../data/IPG0Flow';
import './IPFlowPlayerBasic.css';

const speeds = [0.5, 1, 1.5, 2];
export default function IPFlowPlayerBasic(): React.JSX.Element {
  const [path,setPath] = useState<Path>('create');
  const [index,setIndex] = useState(0);
  const [playing,setPlaying] = useState(false);
  const [speed,setSpeed] = useState(1);
  const [expanded,setExpanded] = useState<string|null>(null);
  const steps=useMemo(()=>moments(path),[path]);
  const step=steps[index] ?? steps[0];
  const activeNodes=new Set(step.nodes);
  const activeEdges=new Set(step.edges);
  const container=useRef<HTMLDivElement|null>(null);
  const elementRefs=useRef<Record<string,HTMLButtonElement|null>>({});
  const [routes,setRoutes]=useState<Record<string,string>>({});
  const [dimensions,setDimensions]=useState({w:0,h:0});
  const changePath=(next:Path)=>{setPath(next);setIndex(0);setPlaying(false);setExpanded(null);};
  const go=(next:number)=>{setIndex(Math.max(0,Math.min(steps.length-1,next)));setPlaying(false);};
  useEffect(()=>{
    if (!playing) return;
    if (index>=steps.length-1){setPlaying(false);return;}
    const timer=window.setTimeout(()=>setIndex(i=>Math.min(i+1,steps.length-1)), Math.round(1600/speed));
    return ()=>window.clearTimeout(timer);
  },[playing,index,speed,steps.length]);
  useEffect(()=>{
    const panel=container.current;
    if(!panel)return;
    let raf=0;
    const measure=()=>{window.cancelAnimationFrame(raf);raf=window.requestAnimationFrame(()=>{
      const root=panel.getBoundingClientRect();const mapped:Record<string,string>={};
      edges.forEach(edge=>{
        if(edge.paths && !edge.paths.includes(path))return;
        const from=elementRefs.current[edge.from]?.getBoundingClientRect();
        const to=elementRefs.current[edge.to]?.getBoundingClientRect();
        if(!from||!to)return;
        const cx1=from.left+from.width/2-root.left,cy1=from.top+from.height/2-root.top;
        const cx2=to.left+to.width/2-root.left,cy2=to.top+to.height/2-root.top;
        const dx=cx2-cx1,dy=cy2-cy1;
        if(Math.abs(dx)>80){
          const sx=cx1+(dx>0?from.width/2:-from.width/2),ex=cx2+(dx>0?-to.width/2:to.width/2);
          mapped[edge.id]=`M ${sx} ${cy1} C ${sx+dx*.42} ${cy1}, ${ex-dx*.42} ${cy2}, ${ex} ${cy2}`;
        } else {
          const sy=cy1+(dy>0?from.height/2:-from.height/2),ey=cy2+(dy>0?-to.height/2:to.height/2);
          mapped[edge.id]=`M ${cx1} ${sy} C ${cx1+32} ${sy+dy*.38}, ${cx2-32} ${ey-dy*.38}, ${cx2} ${ey}`;
        }
      });
      setRoutes(mapped);setDimensions({w:root.width,h:root.height});
    });};
    measure();const observer=typeof ResizeObserver!=='undefined'?new ResizeObserver(measure):null;
    if(observer){observer.observe(panel);Object.values(elementRefs.current).forEach(el=>{if(el)observer.observe(el);});}
    window.addEventListener('resize',measure);
    return()=>{window.cancelAnimationFrame(raf);observer?.disconnect();window.removeEventListener('resize',measure);};
  },[path]);
  const visibleEdges=edges.filter(e=>(!e.paths||e.paths.includes(path)) && routes[e.id]);
  return <section className="ipg0" aria-label="HDIP Information Product self-service development G0">
    <header className="ipg0-heading"><div><p className="ipg0-overline">HDIP PDEP · Information Product SSPD · G0</p><h2>From informational intent to governed value</h2><p>Creator-led, self-service Product discovery, consumption, evolution and intentional creation.</p></div><span className="ipg0-experimental">Experimental E0 · Non-normative</span></header>
    <div className="ipg0-toolbar">
      <fieldset className="ipg0-paths"><legend>Explore Product path</legend>{(Object.keys(pathLabels) as Path[]).map(p=><label key={p} className={path===p?'selected':''}><input type="radio" name="ipg0-path" checked={path===p} onChange={()=>changePath(p)}/>{pathLabels[p]}</label>)}</fieldset>
      <div className="ipg0-controls" role="group" aria-label="Playback controls"><button onClick={()=>go(0)}>Reset</button><button onClick={()=>go(index-1)} disabled={index===0}>Previous</button><button onClick={()=>setPlaying(v=>!v)} aria-label={playing?'Pause playback':'Play playback'}>{playing?'Pause':'Play'}</button><button onClick={()=>go(index+1)} disabled={index===steps.length-1}>Next</button><label>Speed <select value={speed} onChange={e=>setSpeed(Number(e.target.value))}>{speeds.map(s=><option key={s} value={s}>{s}×</option>)}</select></label><button type="button" onClick={()=>window.print()}>Print view</button></div>
    </div>
    <div className="ipg0-narrative" aria-live="polite" aria-atomic="true"><div className="ipg0-narrative-head"><strong>{step.id} — {step.title}</strong><span>{index+1} of {steps.length}</span></div><p>{step.narrative}</p><small>HDIP M15-V03 experience: {step.grouping}. Playback moments are not lifecycle gates.</small></div>
    <div className="ipg0-progress" aria-label="Select presentation moment">{steps.map((s,i)=><button key={s.id} className={i===index?'active':''} onClick={()=>go(i)} aria-label={`${s.id}: ${s.title}`} aria-current={i===index?'step':undefined} title={s.title}>{i+1}</button>)}</div>
    <div className="ipg0-flow" ref={container}>
      <svg className="ipg0-links" width={dimensions.w} height={dimensions.h} viewBox={`0 0 ${Math.max(1,dimensions.w)} ${Math.max(1,dimensions.h)}`} aria-hidden="true"><defs><marker id="ipg0-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#7a93a8"/></marker><marker id="ipg0-arrow-active" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#0d9488"/></marker></defs>{visibleEdges.map(e=><path key={e.id} d={routes[e.id]} className={activeEdges.has(e.id)?'active':''} markerEnd={`url(#${activeEdges.has(e.id)?'ipg0-arrow-active':'ipg0-arrow'})`}/>)}</svg>
      {lanes.map(lane=><div className="ipg0-lane" key={lane.id}><div className="ipg0-lane-header"><h3>{lane.title}</h3><p>{lane.description}</p></div><div className="ipg0-lane-nodes">{nodes.filter(n=>n.lane===lane.id).map(n=><button key={n.id} ref={el=>{elementRefs.current[n.id]=el;}} type="button" className={'ipg0-node '+(activeNodes.has(n.id)?'active ':'')+(expanded===n.id?'expanded':'')} onClick={()=>setExpanded(v=>v===n.id?null:n.id)} aria-expanded={expanded===n.id} aria-label={`${n.title}: ${n.note}. Show details`}><strong>{n.title}</strong><span>{n.note}</span>{expanded===n.id&&<em>{n.detail}</em>}</button>)}</div></div>)}
    </div>
    <div className="ipg0-footnotes"><p><strong>Information Product specialization:</strong> The informational Promise, analytical semantics, assertions, provenance, explanations and consumption contracts are distinct from INFOPDS/PFI realization. INFOPROD, INFOPDS and runtime occurrences remain separate.</p><p><strong>Economic boundary:</strong> X9 supports early indicative cost/economic-impact transparency; P5 captures actual value and cost signals. Investment and funding decisions are enterprise-specific. HDIP does not prescribe a funding model, threshold, prefunding or approval gate.</p><p><strong>Authority boundary:</strong> BPS/PIN Productness, GEARA/GEARM semantics, Product-family/Compound qualification, policy and consequential decisions remain independently governed. Publication does not confer entitlement. Generic consumption is handled through SSCF/CEP.</p><p><strong>Presentation only:</strong> The seven M15-V03 groupings and eight playback moments are non-normative; branches, iteration and re-entry are allowed. No simulated action performs qualification, compilation, deployment or investment authorization.</p></div>
  </section>;
}
