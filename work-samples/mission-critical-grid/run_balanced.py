"""Preliminary balanced load-flow smoke test; not a qualified design."""
import json
import math
from pathlib import Path
import importlib.metadata
import pandapower as pp
from campus import build, inputs, demand

def run_case(restored=False):
    a=inputs()
    n=build(a)
    counts={k:len(n[k]) for k in ('bus','line','trafo','load','switch','ext_grid')}
    assert counts==dict(bus=38,line=32,trafo=4,load=32,switch=1,ext_grid=2),counts
    if restored:
        n.trafo.loc[n.trafo.name.eq('T-HV-B'),'in_service']=False
        n.switch.loc[n.switch.name.eq('MV coupler'),'closed']=True
    pp.runpp(n,algorithm='nr',calculate_voltage_angles=True,numba=False,tolerance_mva=1e-8)
    assert n.converged and n.res_bus.vm_pu.notna().all()
    p,q=demand(a)
    p_load=float(n.res_load.p_mw.sum())
    q_load=float(n.res_load.q_mvar.sum())
    assert math.isclose(p_load,p*a['blocks'],abs_tol=1e-6)
    assert math.isclose(q_load,q*a['blocks'],abs_tol=1e-6)
    p_supply=float(n.res_ext_grid.p_mw.sum())
    losses=float(n.res_line.pl_mw.sum()+n.res_trafo.pl_mw.sum())
    assert abs(p_supply-p_load-losses)<1e-6
    return {'state':'hypothetical restored state after T-HV-B unavailable and MV coupler closed' if restored else 'normal split bus','counts':counts,'p_load_mw':p_load,'q_load_mvar':q_load,'p_supply_mw':p_supply,'q_supply_mvar':float(n.res_ext_grid.q_mvar.sum()),'loss_mw':losses,'min_vm_pu':float(n.res_bus.vm_pu.min()),'max_vm_pu':float(n.res_bus.vm_pu.max()),'max_feeder_loading_pct':float(n.res_line.loading_percent.max()),'transformers':[{'name':str(n.trafo.at[i,'name']),'loading_pct':float(row.loading_percent)} for i,row in n.res_trafo.iterrows() if bool(n.trafo.at[i,'in_service'])]}

def main():
    assert importlib.metadata.version('pandapower')=='3.5.6'
    data={'classification':'preliminary synthetic balanced AC load flow only','pandapower':'3.5.6','cases':[run_case(),run_case(True)]}
    s=json.dumps(data,indent=2,allow_nan=False)
    print(s)
    Path('campus-preliminary-results.json').write_text(s+'\n')

if __name__=='__main__': main()
