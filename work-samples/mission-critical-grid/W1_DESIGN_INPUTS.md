# W1 — Candidate campus input register v0.1

Status: draft parameterisation, NOT a frozen design basis or solved network. All new numbers are synthetic educational assumptions selected for transparent first calculations; none is a verified equipment specification. [Machine-readable register](assumptions.v0.1.json).

| Group | Provenance and interpretation |
|---|---|
| 24 MW IT; 16 x 1.5 MW | previous master plan candidate |
| 110/20/0.4 kV, 2 x 40 MVA HV/MV, 2.5 MVA LV per detailed path | previous master plan candidates |
| 3.125 MVA, 0.8 rated pf genset | previous candidate; generator not included in AC builder |
| 3000/1500 MVA utility strength; R/X 0.1 | previous synthetic grid assumptions; neither feed independence nor DSO data verified |
| 97% UPS efficiency, 0.99 input pf | new assumed operating point; replace with verified curve |
| cooling 0.34 MW at 0.90 pf; auxiliary 0.05 MW at 0.95 pf | new assumptions per block, lagging constant-PQ |
| recharge 0.10 MW at UPS input | candidate separate operating state, excluded from normal case |
| HV/MV uk 12%, vkr 0.5%; LV uk 6%, vkr 1% | assumed impedance candidates; no OEM data |
| feeder 0.5 km, R 0.2 ohm/km, X 0.1 ohm/km, 0.2 kA | illustrative assumed values, not cable sizing/ampacity verification |
| zero transformer core loss, magnetising current, phase shift, cable shunt | intentional simplification for balanced initial model; update before equipment/fault studies |
| equal split of IT, cooling and auxiliary demand | synthetic transfer assumption, not proof of actual service continuity |
| 100 MVA base, 50 Hz, 1 pu slack voltages | numerical conventions |

## Bottom-up preliminary design point
UPS input = IT / efficiency. For each load Q=P*tan(acos(pf)); add P and Q separately. Branch copper losses belong to the solved network, not to a second PUE multiplier.

| Component (full block) | MW | MVAr |
|---|---:|---:|
| UPS input including conversion loss | 1.546392 | 0.220349 |
| Cooling | 0.340000 | 0.164670 |
| Auxiliaries | 0.050000 | 0.016434 |
| Total before external distribution losses | 1.936392 | 0.401453 |
| Campus before external distribution losses | 30.982268 | 6.423242 |

Block apparent demand 1.977569 MVA; full campus 31.641096 MVA before modelled external distribution losses. With assumed 0.1 MW recharge at UPS power factor, block demand becomes 2.036392 MW and 2.078389 MVA. The 2.5 MW generator candidate has arithmetic headroom but no derating, step-load, voltage/frequency or transient qualification. The effective design-point facility/IT ratio is ~1.291 before external network losses, not annual PUE.

## Initial balanced topology
2 HV buses, 2 MV section buses, 32 MV feeder endpoints (two per block), 2 LV buses on detailed block 01 = 38 buses. Thirty-two explicit MV feeders. Four transformers total (two HV/MV, two detailed LV); the other 15 blocks use aggregated MV-equivalent loads without separate downstream transformer losses. Normal A/B split. Normally open coupler. The builder is NOT a full SLD; HV circuit impedances, detailed LV feeders, generator transfer, protective switches, neutral earthing/vector groups, shared dependencies and downstream distribution losses remain open. A/B modelling is an electrical capacity screen only.

Builder drafted, not executed: wait for W0 native solver verification. No fault results are permitted from this model until sequence/grounding and equipment parameters are qualified. The earlier 1.3 ratio screen remains a separate preliminary approximation.
