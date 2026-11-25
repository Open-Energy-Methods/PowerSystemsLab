# Benchmark registry

Candidate benchmarks, not executed results. Obtain original source/version, redistribution permission, input hash and expected quantities before qualification.

| ID | Case | Objective | Evidence target |
|---|---|---|---|
| B01 | analytical RLC and three-phase | phasors and power | independent closed form |
| B02 | two-bus network | load flow and short circuit | separate hand calculation |
| B03 | IEEE/WSCC 9 bus | AC network | independent solver/published outputs |
| B04 | IEEE 14 bus | voltage and PV limits | independent solver |
| B05 | CIGRE MV | distribution and contingencies | source data and independent re-entry |
| B06 | CIGRE LV | unbalanced distribution | phase-resolved data and solver |
| B07 | Schneider CT158 | fault current | published worked case, method alignment |
| B08 | IEEE 30 bus | OPF | objective/constraints with same settings |
| B09 | New England 39 bus | dynamics | separate dynamic dataset and reference |
| B10 | IEEE 118 bus | larger network | independent solver and contingency |
| B11 | IEEE RTS | reliability | qualified reliability dataset |
| B12 | single-machine benchmark | rotor response | analytical limiting case |
| B13 | PSCAD RL circuit | fault offset | analytical time-domain solution |
| B14 | PSCAD energisation example | saturation/inrush | reference reproduction |
| B15 | IEEE First Benchmark Model | SSR | qualified original dynamic model and provenance |
| B16 | synthetic campus | integrated engineering | traceable inputs and cross-tool checks |

Packaged networks run with their native tool are regression checks, not automatically independent verification. Static datasets do not supply missing dynamic/reliability parameters. Keep tool-specific modifications explicit. CIGRE documents and third-party data may restrict redistribution.
