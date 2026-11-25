# MissionCriticalGrid — initial design basis

Status: synthetic proposal, not a solved network. First flagship application within PowerSystemsLab; not driven by a recruitment deadline.

## Candidate architecture
- 110 kV double utility connection; independence not assumed proven.
- Two 40 MVA 110/20 kV transformers; sectionalised 20 kV bus, normally open coupler.
- 16 blocks of 1.5 MW IT each (24 MW total); one detailed A/B LV block, remaining blocks with simplified dual paths and backup availability.
- Candidate 2.5 MVA 20/0.4 kV transformers per detailed A/B path; 3.125 MVA standby genset candidate per path (2.5 MW at 0.8 rated pf); both require sizing checks.
- UPS, cooling and auxiliary loads built bottom-up, with loss/recharge accounting; PUE only an energy-ratio sanity check or explicitly labelled design-point proxy.

## Studies
Design basis and SLD; load flow; switching-state contingencies; IEC 60909 max/min faults; representative breaker duty and selectivity; integrating relay and generator decrement; PSCAD energisation and RL fault waveform; generic RMS load acceptance; UPS energy and cooling continuity; reliability and design alternatives.

## Open decisions
Grid source and shared dependencies, vector groups and grounding, cable lengths and ratings, generator reactances/time constants and excitation, load makeup and motor contributions, transfer interlocks, UPS bypass and autonomy, actual equipment data and licence. Do not calculate generator-mode breaking/peak/thermal duties using unsupported solver outputs. Avoid unsupported claims of uninterrupted service, Tier compliance, real generator certification or site thermal survival.

## Acceptance
Qualified core benchmarks before campus calculations; traceable parameter register; device branch currents; manufacturer curves and selectivity limits; initial/isolation/transfer/restored states; common-mode dependencies; independent checks and explicit limitations. PowerFactory results private until licence permits publication. PSCAD model complexity subject to edition constraints.
