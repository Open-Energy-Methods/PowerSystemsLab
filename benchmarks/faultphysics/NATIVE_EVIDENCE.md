# FaultPhysics / RelayPhysics native evidence

PASS: [Actions run 45723843118](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45723843118), job 139588553148, tested commit 8040f7a03664db3e454f5e41dbfdcd41afbaa14c. 11 analytical unit tests and 5 native pandapower comparisons passed. [Logged results](NATIVE_RESULTS.json) extracted from job log. CI artifact contains environment and original JSON.

| Case | Fault | Native kA | Reference kA |
|---|---|---:|---:|
| max | 3ph | 5.888071062 | 5.888071062 |
| max | 2ph | 5.099219119 | 5.099219119 |
| max | 1ph | 3.821014598 | 3.821014598 |
| min | 3ph | 4.024996673 | 4.024996673 |
| min | 2ph | 3.485749369 | 3.485749369 |

Maximum relative error 2.5480271979670465e-16; tolerance 2%. Only the simple radial case and listed modes are qualified. Ideal independent identical parallel path analytical screen 5.888071 to 11.776142 kA, not campus coupling or a switching recommendation.

Generic relay experiment: constant initial 8 pu current would predict 0.497975611 s trip at pickup 2 pu and TMS 0.1. Integrated decaying current did not trip; peak progress 0.202313424 with 0.1 ms timestep, versus 0.202312728 at 1 ms. The waveform is synthetic and the relay idealised. No settings recommendation or generator performance claim. Learner gate open.

Campus W4/W5, minimum ground fault, CT158 benchmark, near-generator duties, sequence transformer/grounding model and actual equipment selectivity still open.
