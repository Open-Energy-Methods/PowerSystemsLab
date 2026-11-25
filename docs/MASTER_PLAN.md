# PowerSystemsLab — programme charter v0.1

Status: proposed foundation; no implementation qualified. Supersedes job-specific scheduling, not technical evidence. The programme draws on earlier MissionCriticalGrid planning (v0.1–v0.3 reviewed; later revisions described in discussion, not independently retrieved in full).

## Mission
Develop transferable power-system engineering competence from first principles through industrial tools, numerical verification and safe physical experiments. No deadline or job application governs scope. Choose subsequent modules by prerequisite and interest, with all technical branches retained as long-term objectives.

## Laboratories
| ID | Discipline | Scope |
|---|---|---|
| PSL-00 | Foundations | AC circuits, phasors, three-phase power, per-unit, numerical methods |
| PSL-01 | Computational power systems | Y-bus, AC/DC load flow, NR, voltage control, OPF |
| PSL-02 | Equipment | Transformers, cables, switchgear, CT/VT, synchronous and induction machines |
| PSL-03 | Fault analysis | Sequence networks, IEC 60909, fault duty and grounding |
| PSL-04 | Protection | Overcurrent, differential, distance, directional, relay integration, selectivity |
| PSL-05 | Dynamics | RMS stability, excitation, governor, motor and inverter dynamics |
| PSL-06 | EMT | PSCAD, switching, saturation, fault waveforms, insulation coordination |
| PSL-07 | Power electronics | Rectifiers, inverter control, harmonics, UPS, HVDC and FACTS |
| PSL-08 | Grid integration | Renewables, distribution, transmission, reactive power, grid codes |
| PSL-09 | Operations | OPF/SCOPF, dispatch, state estimation, time-series operation |
| PSL-10 | Reliability | N-1/N-2, common mode, probabilistic adequacy, restoration |
| PSL-11 | Digital systems | IEC 61850, SCADA, PMU, CIM, offline digital twins |
| PSL-12 | Electrothermal | Thermal rating, losses, ageing and coupled electrical/thermal models |
| PSL-13 | Physical experiments | Isolated ELV circuits, machines, conversion, signal-level protection |
| PSL-14 | Applications | Integrated case studies and consultancy-style reports |

## Architecture
Use common, versioned parameter records (SI units, bases, sign conventions, sources and licence status), solver-specific adapters, and independent test cases. Do not promise automatic cross-tool interoperability. Keep solver code separate from benchmark inputs and outputs. Commercial models are private by default until permissions are clear.

## Programme outputs
Theory notes, derivations, worked problems, benchmark datasets or permitted retrieval scripts, tests, numerical studies, reports, uncertainty analysis and learner evidence. Maintain a claim ledger and limitations with each study. No artificial release dates; promote modules only after documented gates.

## Application portfolio
MissionCriticalGrid first; future candidates: TurbineGrid (thermal plant and generator), IndustrialGrid, RenewableGrid, HVDC Link, StorageGrid, MicroGrid, NordicGrid. These are placeholders for future studies, not completed projects. Reuse earlier portfolio work only with source, licence and independent reproduction checks.

## Governance
Use branches and reviewable PRs; protect existing work; record assumptions and changes before inspecting results; preserve failed benchmarks and explain deviations. Use AI as tutor, reviewer and coding aid with attribution; learner must independently demonstrate skill. Establish code/data licence policy before public code reuse. See verification and safety protocols.
