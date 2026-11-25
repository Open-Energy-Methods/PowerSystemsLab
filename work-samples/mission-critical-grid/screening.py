"""Analytical nameplate screen, not an AC load flow or IEC 60909 study."""
import math

def screen(it_mw=24, ratio=1.3, pf=.95, transformer_mva=40):
    if not all(math.isfinite(x) for x in (it_mw,ratio,pf,transformer_mva)) or it_mw <= 0 or ratio < 1 or not 0 < pf <= 1 or transformer_mva <= 0:
        raise ValueError('invalid screening assumptions')
    p=it_mw*ratio
    s=p/pf
    return {'facility_mw':p,'demand_mva':s,'normal_loading_pct':100*s/(2*transformer_mva),'n_minus_1_loading_pct':100*s/transformer_mva,'n_minus_1_it_limit_mw':transformer_mva*pf/ratio}

def transformer_fault_bound(mva, kv, uk_pu):
    """Ideal stiff source, nominal voltage, transformer series impedance only."""
    if not all(math.isfinite(x) and x > 0 for x in (mva,kv,uk_pu)):
        raise ValueError('invalid transformer inputs')
    return mva/(math.sqrt(3)*kv*uk_pu)

if __name__ == '__main__':
    for key,value in screen().items():
        print(f'{key}: {value:.6f}')
    print(f'LV transformer-only fault estimate: {transformer_fault_bound(2.5,.4,.06):.6f} kA')
