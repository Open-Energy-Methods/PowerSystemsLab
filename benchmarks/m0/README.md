# M0/W0 — Analytical references and native solver qualification

Status: analytical reference calculations and three local unit tests passed in Python 3.13.5. Native pandapower execution pending: package installer returned no available distribution in the assistant runtime, despite version 3.5.6 being listed on PyPI. CI recipe is provided; actual workflow status is separate.

## Two-bus case
20 kV, 50 Hz, balanced constant-PQ load 2 MW + j0.8 Mvar; 1 km line R=0.5 ohm, X=1.2 ohm, no shunt. Load flow slack 1 pu and 0 degrees; source impedance applies only to fault analysis. For three-phase faults use source strength 500/250 MVA (max/min), R/X=0.1, c=1.1/1.0, line temperature 20 C, zero fault impedance and no pre-fault-voltage method.

With receiving squared voltage w, solve w²+[2(RP+XQ)-Vs²]w+|Z|²(P²+Q²)=0; select the high-voltage solution. Fault impedance is Zline + Zsource, |Zsource|=c V²/Sk, and I=c V/(sqrt(3)|Ztotal|).

| Reference | Value |
|---|---:|
| Receiving voltage | 0.995063064571 pu |
| Receiving angle | -0.287901454 degrees |
| Source P | 2.005857695 MW |
| Source Q | 0.814058469 Mvar |
| Line active loss | 0.005857695 MW |
| Initial symmetrical max fault | 5.888071062 kA |
| Initial symmetrical min fault | 4.024996673 kA |

Predeclared gates: absolute 1e-6 in each displayed load-flow unit; SC 2% relative or 1e-6 kA absolute. CIGRE MV no-DER native case: documented counts, convergence, finite bus voltages and active-power balance within 1e-6 MW. This is regression/smoke checking, not independent CIGRE validation.

## Reproduce
From root, use a Python 3.12 virtual environment:
```sh
python -m pip install -r benchmarks/m0/requirements.txt
python -m unittest discover -s benchmarks/m0 -v
python benchmarks/m0/qualify.py
```
Record pip freeze and JSON results. Only the top-level library version is pinned; lock transitive dependencies after a successful run.

Sources: [PyPI release](https://pypi.org/project/pandapower/3.5.6/), [source impedance method](https://pandapower.readthedocs.io/en/v3.5.6/shortcircuit/voltage_source.html), [CIGRE networks](https://pandapower.readthedocs.io/en/v3.5.6/networks/cigre.html). No standard full-text certification claim. Remaining W0 gates: CT158, supported asymmetric fault tests, generator restrictions, independent CIGRE comparison later. No campus study is qualified by these references alone.
