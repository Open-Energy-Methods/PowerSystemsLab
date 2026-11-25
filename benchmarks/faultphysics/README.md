# FaultPhysics / RelayPhysics — qualification protocol

Status: 11 analytical unit tests and five native fault comparisons passed in CI. See [native evidence](NATIVE_EVIDENCE.md). Study cases are not the campus design. All inputs synthetic.

## Fault benchmark
20 kV, 50 Hz, source strengths 500/250 MVA, R/X=0.1, voltage factor 1.1/1.0. One 1 km series line with positive/negative Z=0.5+j1.2 ohm, zero sequence Z=1.5+j3.6 ohm, no shunt, conductor end temperature 20 C. Source X0/X1=2, R0/X0=0.2. No loads, machines or transformers. Bolted faults. Independent phase/sequence conversion and boundary-condition tests. Maximum 3ph, 2ph and 1ph, minimum 3ph and 2ph; minimum 1ph not yet qualified. Native tolerance fixed at 2% relative or 1e-6 kA absolute. Source impedance conventions from [pandapower 3.5.6](https://pandapower.readthedocs.io/en/v3.5.6/elements/ext_grid.html) and [calc_sc](https://pandapower.readthedocs.io/en/v3.5.6/shortcircuit/run.html).

Max reference currents: 5.888071062, 5.099219119, 3.821014598 kA respectively. The independent equal parallel-path example assumes identical in-phase sources with no shared impedance, and doubles 3ph current; it is NOT a permission to parallel real utilities or a campus fault calculation.

## Relay benchmark
Standard inverse equation t=TMS*0.14/(M^0.02-1) for M>1. Integrate operating progress dt/t under piecewise constant RMS current; interpolate threshold crossing within the interval. Instantaneous reset below/equal pickup is an explicit idealisation, not a claim of a vendor or standard reset implementation. Constant current, independent piecewise integration, reset, no-pickup and timestep convergence tests. IEC 60255-151 addresses time-varying current; consult authorised standard text before compliance claims. See [IEC publication](https://webstore.iec.ch/en/publication/1166).

Generic RMS envelope I(t)=1.25+3.4 exp(-t/0.04)+3.35 exp(-t/0.2) pu; synthetic initial 8 pu and final 1.25 pu, not machine-derived data, no AVR, DC offset, measurement filter or breaker delay. Pickup 2 pu, TMS 0.1. Compare an initial-current-only trip estimate to integration; examine 1 ms and 0.1 ms steps. This is an illustrative protection sensitivity experiment, not a recommendation for settings. No actual generator duty or selectivity claim.

## Run
Python 3.12, pandapower 3.5.6. From repo root:
```sh
python -m pip install -r benchmarks/m0/requirements.txt
python -m unittest discover -s benchmarks/faultphysics -v
python benchmarks/faultphysics/native.py
```
CI preserves JSON and environment. Learner gate remains open. CT158, min earth fault, transformer zero sequence, real generator decrement, far/near generator duty and manufacturer protection data remain unqualified.
