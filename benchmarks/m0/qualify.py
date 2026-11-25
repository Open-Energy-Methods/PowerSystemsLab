"""Native solver qualification; no claim until successful execution."""
import json
import math
import platform
import importlib.metadata
from pathlib import Path
import pandapower as pp
from pandapower.shortcircuit import calc_sc
from pandapower.networks import create_cigre_network_mv
from reference import load_flow, fault

def check(actual, expected, atol, rtol=0):
    if not math.isfinite(actual) or not math.isclose(actual,expected,abs_tol=atol,rel_tol=rtol):
        raise AssertionError(f'{actual=} {expected=} {atol=} {rtol=}')

def two_bus():
    net=pp.create_empty_network(sn_mva=100, f_hz=50)
    a=pp.create_bus(net,vn_kv=20,name='Source')
    b=pp.create_bus(net,vn_kv=20,name='Receiving')
    pp.create_ext_grid(net,a,vm_pu=1,va_degree=0,s_sc_max_mva=500,s_sc_min_mva=250,rx_max=.1,rx_min=.1)
    pp.create_line_from_parameters(net,a,b,length_km=1,r_ohm_per_km=.5,x_ohm_per_km=1.2,c_nf_per_km=0,max_i_ka=1,endtemp_degree=20)
    pp.create_load(net,b,p_mw=2,q_mvar=.8)
    pp.runpp(net,algorithm='nr',calculate_voltage_angles=True,numba=False,tolerance_mva=1e-9)
    assert net.converged
    actual=dict(vm_pu=float(net.res_bus.at[b,'vm_pu']),va_degree=float(net.res_bus.at[b,'va_degree']),p_source_mw=float(net.res_ext_grid.p_mw.sum()),q_source_mvar=float(net.res_ext_grid.q_mvar.sum()),p_loss_mw=float(net.res_line.pl_mw.sum()),q_loss_mvar=float(net.res_line.ql_mvar.sum()))
    expected=load_flow()
    for k,v in actual.items():
        check(v,expected[k],1e-6)
    sc={}
    for case,c,sk in [('max',1.1,500),('min',1.0,250)]:
        calc_sc(net,bus=b,fault='3ph',case=case,ip=False,ith=False,branch_results=False,use_pre_fault_voltage=False)
        v=float(net.res_bus_sc.at[b,'ikss_ka'])
        check(v,fault(c,sk),1e-6,0.02)
        sc[case]={'ikss_ka':v,'reference_ka':fault(c,sk)}
    return {'load_flow':actual,'reference':expected,'short_circuit':sc}

def cigre():
    net=create_cigre_network_mv(with_der=False)
    counts={k:len(net[k]) for k in ('bus','line','trafo','load','switch','ext_grid')}
    assert counts==dict(bus=15,line=15,trafo=2,load=18,switch=8,ext_grid=1),counts
    pp.runpp(net,algorithm='nr',calculate_voltage_angles=True,numba=False,tolerance_mva=1e-8)
    assert net.converged and net.res_bus.vm_pu.notna().all()
    source=float(net.res_ext_grid.p_mw.sum())
    load=float(net.res_load.p_mw.sum())
    losses=float(net.res_line.pl_mw.sum()+net.res_trafo.pl_mw.sum())
    check(source-load-losses,0,1e-6)
    return {'classification':'native regression, not independent verification','counts':counts,'p_source_mw':source,'p_load_mw':load,'p_loss_mw':losses,'min_vm_pu':float(net.res_bus.vm_pu.min()),'max_vm_pu':float(net.res_bus.vm_pu.max()),'buses':[{'bus':int(i),'vm_pu':float(row.vm_pu),'va_degree':float(row.va_degree)} for i,row in net.res_bus.iterrows()]}

def main():
    version=importlib.metadata.version('pandapower')
    assert version=='3.5.6',version
    report={'python':platform.python_version(),'pandapower':version,'dependencies':{k:importlib.metadata.version(k) for k in ('numpy','scipy','pandas','networkx')},'two_bus':two_bus(),'cigre_mv':cigre()}
    text=json.dumps(report,indent=2,allow_nan=False)
    print(text)
    Path('qualification-results.json').write_text(text+'\n',encoding='utf-8')

if __name__=='__main__': main()
