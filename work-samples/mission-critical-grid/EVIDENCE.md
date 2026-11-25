# Evidence register

| Claim | Evidence | Status |
|---|---|---|
| Preliminary nameplate arithmetic | screening.py, PRELIMINARY_SCREEN.md | local analytical checks passed; review pending |
| Network solver qualification | W0 | not started |
| Equipment selection | W1 | not qualified |
| Solved AC load flow | W2_NATIVE_EVIDENCE.md | native smoke tests passed; design review open |
| Contingencies | W3_NATIVE_EVIDENCE.md | 41 outages, 124 states passed capacity screen; no service continuity claim |
| IEC 60909 faults | shared faultphysics benchmark (PR #2) | five native synthetic benchmark comparisons passed; campus duty model blocked |
| Selectivity and protection | shared relay benchmark (PR #2) | 11 analytical unit tests passed across faults and relays; generic relay model only; campus settings unqualified |
| Resilience | W6 | not available |
| Design alternatives | W7 | not available |
| PowerFactory cross-check | W8 | not available; licence pending |
| PSCAD native studies | W9 | not available in this project |
| Dynamics and thermal continuity | W10 | not available |
| Consolidated report | W11 | not available |

This folder is the work-sample entry point, not evidence of completed studies. Release a reviewed, immutable version only when the gate requirements are met. Record commits, input hashes, solver settings, reviewer and AI assistance. Keep commercial materials private unless permitted.

Shared native evidence: [fault and relay qualification run](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45723843118). See [representative generator data](W4_GENERATOR_DATA.md) for the fixed-field limitation.
