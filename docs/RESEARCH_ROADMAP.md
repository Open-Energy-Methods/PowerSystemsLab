# Competence-based roadmap

No dates. Status of every module: planned until evidence is recorded.

| Module | Prerequisites | Deliverable and gate |
|---|---|---|
| F01 AC circuits | basic algebra | RLC phasors; hand vs complex Python |
| F02 three-phase power | F01 | balanced Y/delta, power and sign checks |
| F03 per-unit | F02 | multi-voltage transformer base invariance |
| F04 numerical methods | F01 | residual/Jacobian and convergence study |
| N01 Y-bus | F03 | hand-built three-bus admittance matrix |
| N02 AC load flow | N01,F04 | independent Newton-Raphson and hand two-bus check |
| N03 standard networks | N02 | IEEE 9/14 and CIGRE MV cases; external reference or independent solve |
| N04 network design | N03 | equipment sizing and campus SLD |
| N05 contingencies | N04 | initial/isolation/transfer/restoration states |
| E01 equipment models | F03 | transformer and cable impedance, ratings |
| E02 machines | E01 | synchronous and induction machine equations |
| S01 sequence networks | F02,E01 | balanced and unbalanced fault checks |
| S02 IEC 60909 | S01,N02 | max/min fault comparison; duty limits |
| P01 relay curves | S02 | analytical time-current checks |
| P02 variable current | P01,E02 | integrating relay with pickup/reset and timestep convergence |
| P03 coordination | P02 | branch currents, manufacturer curves and selectivity limitations |
| P04 advanced protection | P03 | differential/distance/directional examples |
| D01 swing equation | E02,N02 | energy/frequency response and equilibrium check |
| D02 governors/AVR | D01 | generic parameter sensitivity, not vendor certification |
| D03 multi-machine | D02 | dynamic benchmark with documented model data |
| T01 RL fault waveform | S01 | PSCAD and analytical DC offset/peak comparison |
| T02 transformer inrush | T01,E01 | closing angle, residual flux, saturation and timestep checks |
| T03 generator decrement | T01,E02 | machine transient vs simplified envelope |
| T04 switching/insulation | T02 | reduced switching case and limits |
| C01 converters | F01 | rectifier/inverter and energy conservation |
| C02 harmonics | C01,N02 | spectrum and source impedance sensitivity |
| C03 converter control | C01,D01 | stability and current-limiting study |
| C04 HVDC/FACTS | C03 | reduced link/compensation benchmark |
| G01 distribution | N03,S01 | unbalanced feeder comparison |
| G02 grid integration | D03,C03 | renewable and storage connection study |
| G03 grid rules | G02 | requirements traceability, no compliance claim |
| O01 OPF | N02,F04 | objective and constraint residual checks |
| O02 dispatch/SCOPF | O01,N05 | contingency feasibility and sensitivities |
| O03 state estimation | N02,F04 | residual, observability and bad-data tests |
| R01 resilience | N05,P03 | SPOF, common-mode and restoration audit |
| R02 probabilistic reliability | R01 | synthetic failure rates, uncertainty and sensitivity |
| R03 thermal continuity | R01,E01 | thermal and UPS energy balance, no real hall survival claim |
| I01 digital systems | O03,P03 | offline signal and message semantics |
| H01 electrothermal | E01 | cable/transformer thermal model and convergence |
| H02 experimental methods | F01 | safety approval, calibration and uncertainty |
| A01 campus capstone | N05,S02,P03,R01 | independently reviewed educational study |
| A02 advanced applications | relevant branches | application-specific gates |

Order is flexible wherever dependencies allow. Commercial tools are optional until legitimate access is confirmed. Reserve time-limited evaluation licences for prepared cases.
