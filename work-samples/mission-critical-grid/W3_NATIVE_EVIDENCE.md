# W3 — Native outage capacity screen

PASS of predeclared numerical capacity-screen criteria, NOT design qualification or physical resilience. [Actions run 45723538152](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45723538152), job 139587535987, tested commit e6d765c107d68221bdcd25bf98966c5c624ac310. 41 distinct outages, 124/124 converged states, 0/41 restored states with flags. Full state JSON and dependency records were uploaded in CI. The [restored rows](W3_RESTORED_RESULTS.json) are reproduced from actual job logs.

| Failure category | Cases | Initial unavailable IT MW per case | Worst restored V pu | Max restored transformer % | Max feeder % |
|---|---:|---:|---:|---:|---:|
| Utility | 2 | 12 | 0.962008 | 81.491988 | 14.835499 |
| HV transformer | 2 | 12 | 0.962008 | 81.491988 | 14.835499 |
| MV section | 2 | 12 | 0.951531 | 83.132072 | 29.997702 |
| Feeder | 32 | 0.75 | 0.966531 | 81.841930 | 29.532163 |
| LV transformer | 2 | 0.75 | 0.966531 | 81.841930 | 29.532163 |
| Normally open coupler | 1 | 0 | 0.977764 | 40.450840 | 14.596440 |

All restored states allocate 24 MW IT under assumed transferable demand. Worst MV section outage loss 167.027 kW. Minimum voltage just 0.001531 pu above assumed 0.95 pu screen; sensitivity to impedance, load, taps and utility voltage is necessary. Initial state is not fault-on; no time-to-restore or service continuity inferred. Model lacks UPS, standby generation, detailed breaker, LV and HV line outages and shared dependencies. Do not infer Tier compliance or full N-1 certification.

W4/W5 remain open. Shared [FaultPhysics and RelayPhysics development PR](https://github.com/Open-Energy-Methods/PowerSystemsLab/pull/2) establishes synthetic sequence and variable-current verification cases. Before campus fault-duty studies, resolve equipment parameters, grounding and transformer zero sequence, source cases, conductor temperature, motor/converter contribution and generator data; distinguish initial, making, breaking and thermal duties.
