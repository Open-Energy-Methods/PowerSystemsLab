"""Balanced, discrete outage capacity screen; not a switching procedure."""
import json
import math
from pathlib import Path
from collections import deque
import pandapower as pp
from campus import build, inputs, demand

def index(table, name):
    ids = table.index[table.name.eq(name)]
    if len(ids) != 1:
        raise ValueError(name)
    return ids[0]

def inventory(a):
    return ([('source',s) for s in 'AB']+
            [('hv_transformer',s) for s in 'AB']+
            [('mv_bus',s) for s in 'AB']+
            [('feeder',f'F{b:02}-{s}') for b in range(1,a['blocks']+1) for s in 'AB']+
            [('lv_transformer',s) for s in 'AB']+[('coupler','MV coupler')])

def available(n, table, name, flag=False):
    n[table].at[index(n[table],name),'in_service']=flag

def reachable(n):
    active=set(n.bus.index[n.bus.in_service])
    adj={b:set() for b in active}
    def edge(i,j):
        if i in active and j in active:
            adj[i].add(j);adj[j].add(i)
    for table,cols in [('line',('from_bus','to_bus')),('trafo',('hv_bus','lv_bus'))]:
        for row in n[table].itertuples():
            if row.in_service: edge(getattr(row,cols[0]),getattr(row,cols[1]))
    for row in n.switch.itertuples():
        if row.et!='b': raise ValueError('unsupported switch type in this model')
        if row.closed: edge(row.bus,row.element)
    sources=set(n.ext_grid.loc[n.ext_grid.in_service,'bus']) & active
    seen=set(sources);queue=deque(sources)
    while queue:
        b=queue.popleft()
        for other in adj[b]-seen:
            seen.add(other);queue.append(other)
    return seen

def case_network(a, outage=None, phase='normal'):
    n=build(a)
    coupler=index(n.switch,'MV coupler')
    if outage:
        kind,key=outage
        if kind=='source':
            bus=index(n.bus,f'HV-{key}')
            n.ext_grid.loc[n.ext_grid.bus.eq(bus),'in_service']=False
            if phase!='initial': available(n,'trafo',f'T-HV-{key}')
        elif kind=='hv_transformer': available(n,'trafo',f'T-HV-{key}')
        elif kind=='mv_bus':
            bus=index(n.bus,f'MV-{key}')
            n.bus.at[bus,'in_service']=False
            if phase!='initial':
                n.line.loc[n.line.from_bus.eq(bus)|n.line.to_bus.eq(bus),'in_service']=False
                n.trafo.loc[n.trafo.lv_bus.eq(bus)|n.trafo.hv_bus.eq(bus),'in_service']=False
        elif kind=='feeder': available(n,'line',key)
        elif kind=='lv_transformer': available(n,'trafo',f'T-B01-{key}')
        elif kind=='coupler': n.switch.at[coupler,'closed']=False
        else: raise ValueError(kind)
        if phase=='restored' and kind in ('source','hv_transformer'):
            assert not bool(n.trafo.at[index(n.trafo,f'T-HV-{key}'),'in_service'])
            n.switch.at[coupler,'closed']=True
    live=reachable(n)
    p,q=demand(a)
    fractions=[]
    for b in range(1,a['blocks']+1):
        ids=[index(n.load,f'B{b:02}-{s}-load') for s in 'AB']
        active=[i for i in ids if n.load.at[i,'bus'] in live]
        share=(1/len(active) if active else 0) if phase=='restored' else .5
        for i in ids:
            enabled=i in active
            n.load.at[i,'in_service']=enabled
            n.load.at[i,'p_mw']=p*share if enabled else 0
            n.load.at[i,'q_mvar']=q*share if enabled else 0
        fractions.append(len(active)*share)
    # Explicitly prune dead islands for numerical solve, after counting demand.
    n.bus.loc[~n.bus.index.isin(live),'in_service']=False
    for table,c1,c2 in [('line','from_bus','to_bus'),('trafo','hv_bus','lv_bus')]:
        n[table].loc[~n[table][c1].isin(live)|~n[table][c2].isin(live),'in_service']=False
    n.ext_grid.loc[~n.ext_grid.bus.isin(live),'in_service']=False
    return n,fractions,live

def solve_state(a,outage=None,phase='normal'):
    n,frac,live=case_network(a,outage,phase)
    p,q=demand(a); total=sum(frac)
    unserved=a['blocks']-total
    result={'phase':phase,'coupler_closed':bool(n.switch.closed.iloc[0]),'energised_buses':len(live),
            'served_it_mw':a['it_mw_per_block']*total,'unserved_it_mw':a['it_mw_per_block']*unserved,
            'unserved_cooling_mw':a['cooling_mw_per_block']*unserved,
            'unserved_facility_mw':p*unserved,'blocks_full':sum(x==1 for x in frac)}
    if not live:
        return dict(result,converged=False,flags=['no energised buses'])
    try:
        pp.runpp(n,algorithm='nr',calculate_voltage_angles=True,numba=False,tolerance_mva=1e-8)
    except pp.LoadflowNotConverged:
        return dict(result,converged=False,flags=['load flow failed'])
    assert n.converged
    pl=float(n.res_load.p_mw.sum());ql=float(n.res_load.q_mvar.sum())
    ps=float(n.res_ext_grid.p_mw.sum());qs=float(n.res_ext_grid.q_mvar.sum())
    lp=float(n.res_line.pl_mw.sum()+n.res_trafo.pl_mw.sum())
    lq=float(n.res_line.ql_mvar.sum()+n.res_trafo.ql_mvar.sum())
    assert abs(pl-p*total)<1e-6 and abs(ql-q*total)<1e-6
    assert abs(ps-pl-lp)<1e-6 and abs(qs-ql-lq)<1e-6
    volt=n.res_bus.loc[list(live),'vm_pu']
    assert all(math.isfinite(v) for v in volt)
    t=n.res_trafo.loc[n.trafo.in_service,'loading_percent']
    l=n.res_line.loc[n.line.in_service,'loading_percent']
    assert all(math.isfinite(v) for v in t) and all(math.isfinite(v) for v in l)
    vmin=float(volt.min());vmax=float(volt.max())
    mt=float(t.max()) if len(t) else 0.;ml=float(l.max()) if len(l) else 0.
    flags=[]
    if vmin<.95 or vmax>1.05: flags.append('voltage outside assumed range')
    if mt>100: flags.append('transformer above assumed rating')
    if ml>100: flags.append('feeder above assumed rating')
    if mt>90: flags.append('transformer above 90% design target')
    if unserved>1e-9: flags.append('unserved load')
    return dict(result,converged=True,source_mw=ps,source_mvar=qs,loss_mw=lp,min_vm_pu=vmin,max_vm_pu=vmax,max_trafo_pct=mt,max_line_pct=ml,flags=flags)

def main():
    a=inputs()
    cases=inventory(a)
    assert len(cases)==len(set(cases))==41
    baseline=solve_state(a)
    results=[]
    for kind,key in cases:
        states=[solve_state(a,(kind,key),phase) for phase in ('initial','isolated','restored')]
        expected=12 if kind in ('source','hv_transformer','mv_bus') else 0 if kind=='coupler' else .75
        assert math.isclose(states[0]['unserved_it_mw'],expected,abs_tol=1e-9)
        assert states[0]['coupler_closed']==states[1]['coupler_closed']==False
        assert states[2]['coupler_closed']==(kind in ('source','hv_transformer'))
        assert math.isclose(states[2]['unserved_it_mw'],0,abs_tol=1e-9)
        results.append({'kind':kind,'asset':key,'states':states})
    summary={'cases':len(results),'states':3*len(results)+1,
             'converged':sum(s['converged'] for r in results for s in r['states'])+baseline['converged'],
             'restored_with_flags':sum(bool(r['states'][2]['flags']) for r in results)}
    data={'classification':'synthetic balanced capacity screen; no service continuity claim','summary':summary,'baseline':baseline,'cases':results}
    Path('contingency-results.json').write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    print(json.dumps(summary,indent=2))
    for r in results:
        s=r['states'][2]
        print(json.dumps({'kind':r['kind'],'asset':r['asset'],'initial_unserved_it_mw':r['states'][0]['unserved_it_mw'],'restored':s},allow_nan=False))
    if summary['converged']!=summary['states']: raise RuntimeError('one or more load flows failed')

if __name__=='__main__': main()
