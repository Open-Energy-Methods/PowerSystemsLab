"""Draft balanced utility-fed campus model. Native execution and verification pending."""
import json
import math
from pathlib import Path

def inputs():
    return json.loads(Path(__file__).with_name('assumptions.v0.1.json').read_text())

def demand(a):
    parts=[(a['it_mw_per_block']/a['ups_efficiency'],a['ups_pf']),
           (a['cooling_mw_per_block'],a['cooling_pf']),
           (a['aux_mw_per_block'],a['aux_pf'])]
    return sum(p for p,pf in parts),sum(p*math.tan(math.acos(pf)) for p,pf in parts)

def build(a=None):
    import pandapower as pp
    a=inputs() if a is None else a
    g=a['grid']
    n=pp.create_empty_network(sn_mva=a['base_mva'],f_hz=a['frequency_hz'])
    mv={}
    for side in ('A','B'):
        hv=pp.create_bus(n,vn_kv=g['kv'],name=f'HV-{side}')
        mv[side]=pp.create_bus(n,vn_kv=a['hv_transformer']['lv_kv'],name=f'MV-{side}')
        pp.create_ext_grid(n,hv,vm_pu=g['vm_pu'],s_sc_max_mva=g['sc_max_mva'],s_sc_min_mva=g['sc_min_mva'],rx_max=g['rx'],rx_min=g['rx'])
        t=a['hv_transformer']
        pp.create_transformer_from_parameters(n,hv,mv[side],sn_mva=t['mva'],vn_hv_kv=t['hv_kv'],vn_lv_kv=t['lv_kv'],vk_percent=t['vk_percent'],vkr_percent=t['vkr_percent'],pfe_kw=t['pfe_kw'],i0_percent=t['i0_percent'],shift_degree=t['shift_degree'],name=f'T-HV-{side}')
    pp.create_switch(n,mv['A'],mv['B'],et='b',closed=False,name='MV coupler')
    p,q=demand(a)
    for block in range(1,a['blocks']+1):
        for side in ('A','B'):
            end=pp.create_bus(n,vn_kv=a['hv_transformer']['lv_kv'],name=f'B{block:02}-{side}-MV')
            pp.create_line_from_parameters(n,mv[side],end,**a['mv_feeder'],name=f'F{block:02}-{side}')
            load_bus=end
            if block==1:
                t=a['lv_transformer']
                load_bus=pp.create_bus(n,vn_kv=t['lv_kv'],name=f'B01-{side}-LV')
                pp.create_transformer_from_parameters(n,end,load_bus,sn_mva=t['mva'],vn_hv_kv=t['hv_kv'],vn_lv_kv=t['lv_kv'],vk_percent=t['vk_percent'],vkr_percent=t['vkr_percent'],pfe_kw=t['pfe_kw'],i0_percent=t['i0_percent'],shift_degree=t['shift_degree'],name=f'T-B01-{side}')
            pp.create_load(n,load_bus,p_mw=p/2,q_mvar=q/2,name=f'B{block:02}-{side}-load')
    return n

# Intentionally no automatic solver run. W0 must be passed and inputs reviewed first.
if __name__=='__main__':
    a=inputs(); p,q=demand(a)
    print(f'Analytical block demand: {p:.9f} MW, {q:.9f} Mvar')
    print('Native model not executed. See W1_DESIGN_INPUTS.md.')
