# CT158 exploratory sequence-network reconstruction

From B10 Figures 33–35, all reactances in ohm referred to 30 kV, resistance neglected, positive=negative sequence. Nodes E,F,G,H. Positive: E to reference 5.8 and 99 in parallel; F,G to reference 288 each; EF 5.25, EG 14, FH 7, GH 10.5 when closed. Zero: E to reference 2.7; EF 15.75, EG 42, FH 21, GH 31.5 when closed. No H shunt in simplified published diagrams. No arbitrary tuning. Inject unit current at H, solve nodal equations, take imaginary driving-point impedance. This reconstructs simplified diagrams, not entire original nameplate model.

| Topology | X1 | X0 | 3ph at c=1.1 kA | 1ph at c=1.1 kA | 3ph at c=1 kA | 1ph at c=1 kA |
|---|---:|---:|---:|---:|---:|---:|
| GH open | 17.252895953 | 39.45 | 1.104310774 | .772862749 | 1.003918885 | .702602499 |
| GH closed | 13.049194985 | 27.2 | 1.460056264 | 1.072409067 | 1.327323877 | .974917333 |

Published rounded values: open 17.25,39.45,1.104,.773; closed 13.05,27.2,1.460,1.072. Eight relative errors <1%. NumPy arithmetic executed locally. Reproducible script provided, CI not run; formal independent review still required. Historical 2000 benchmark, not modern IEC compliance. 
