"""Native comparison for a synthetic radial network, no campus fault duties."""
import json
import math
from pathlib import Path
import pandapower as pp
from pandapower.shortcircuit import calc_sc
from faults import reference,parallel_paths
from relay import time_constant,decay_case

def main():
    n=pp.create_empty_network(sn_mva=100,f_hz=50)
    a=pp.create_bus(n,vn_kv=20)
    b=pp.create_bus(n,vn_kv=20)
    pp.create_ext_grid(n,a,s_sc_max_mva=500,s_sc_min_mva=250,rx_max=.1,rx_min=.1,r0x0_max=.2,x0x_max=2,r0x0_min=.2,x0x_min=2)
    pp.create_line_from_parameters(n,a,b,length_km=1,r_ohm_per_km=.5,x_ohm_per_km=1.2,c_nf_per_km=0,max_i_ka=1,r0_ohm_per_km=1.5,x0_ohm_per_km=3.6,c0_nf_per_km=0,endtemp_degree=20)
    cases=[]
    for case,c,sk,types in [('max',1.1,500,('3ph','2ph','1ph')),('min',1.0,250,('3ph','2ph'))]:
        ref=reference(c,sk)
        for fault in types:
            calc_sc(n,bus=b,case=case,fault=fault,ip=False,ith=False,use_pre_fault_voltage=False)
            actual=float(n.res_bus_sc.at[b,'ikss_ka'])
            expected=ref[fault]
            cases.append({'case':case,'fault':fault,'native_ka':actual,'reference_ka':expected,'relative_error':abs(actual-expected)/expected,'pass':math.isclose(actual,expected,rel_tol=.02,abs_tol=1e-6)})
    data={'classification':'synthetic benchmark, not campus equipment duty','fault_cases':cases,'ideal_parallel_source_screen':parallel_paths(),'relay':{'constant_initial_8pu_s':time_constant(8,2,.1),'decay_dt_1ms':decay_case(dt=.001),'decay_dt_0.1ms':decay_case()}}
    s=json.dumps(data,indent=2,allow_nan=False)
    print(s);Path('faultphysics-results.json').write_text(s+'\n')
    if not all(x['pass'] for x in cases): raise AssertionError('native fault mismatch; preserve evidence')
if __name__=='__main__': main()
