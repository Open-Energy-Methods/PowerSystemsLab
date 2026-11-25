# LR0 — Decisions and closure gates

Initial synthesis completed; LR0 not fully closed. Proposed engineering decisions require review before simulation change. Priority P0 blocks relevant W4/W5 claims, P1 blocks a mature capacity/resilience study, P2 blocks later specialised claims. No change to existing simulation assumptions or results in this PR.

| ID | Priority | Evidence | Decision / required work | Closure evidence |
|---|---|---|---|---|
| D01 | P0 | R05–R07 | Distinguish 2026 standard from pinned 2016 implementation | authorized edition comparison and national adoption; method matrix |
| D02 | P0 | R08 | CT158 reproduction under both voltage-factor conventions | independent sequence network reconstruction and predeclared tolerance |
| D03 | P0 | R08,R15 | transformer vector groups and grounding/zero-sequence model | sourced sequence impedances, neutral return path, independently checked cases |
| D04 | P0 | R07,R08 | max/min source configurations, temperature, device currents, peak/thermal/breaking scope | qualified benchmark per current type, unsupported-mode flags |
| D05 | P0 | R09–R11 | representative equipment TCC and tested selectivity | exact device, voltage, settings, manufacturer tables/limits, documented grading |
| D06 | P0 | R12 | revise alternator reference to rev F while preserving rev E history; no 3.125 MVA inference | exact candidate rating/data, excitation response and branch current waveform |
| D07 | P0 | R09,R12 | distinguish generic relay integration from actual settings | reset/filter/tolerance and breaker time qualification; matched waveform test |
| D08 | P1 | R13,R14,R15 | replace illustrative cable and transformer ratings | equipment data, thermal conditions, impedance/loss/ampacity/withstand checks |
| D09 | P1 | R20–R23 | explicit component P/Q, UPS and cooling/transfer dependencies | bottom-up sourced inputs, all-block downstream losses, operating mode register |
| D10 | P1 | R20,R21,R23 | qualify narrow voltage margin and restoration assumptions | sensitivity to taps, impedance, load and utility voltage; unserved component accounting |
| D11 | P2 | R16,R17 | dynamic case and model parameters | benchmark equilibrium, time-domain results, independent comparison |
| D12 | P2 | R18,R19 | reduced EMT experiments | native case reproduction and time-step/analytical check |
| D13 | P2 | R20,R24,R25 | grid-facing dynamic demand model | published/measured behaviour and jurisdiction-specific connection rules |
| D14 | P2 | R02,R26 | OPF, DER and QSTS benchmarking | qualified data and independent objective/constraint checks |
| D15 | P2 | R04,R01,R02 | independent CIGRE reproduction | lawful original data, independently constructed model, discrepancies documented |
| D16 | P2 | R21,R23 | thermal and UPS resilience | component energy and thermal data, uncertainty, service-continuity limits |

## Next action order
1. Review and merge this literature PR without claiming complete review. Acquire authorized IEC edition access and retrieve CT158 source and exact OEM tables. Preserve source edition and access limits.
2. Complete independent CT158 sequence case and missing min earth-fault benchmark; these can be educational without pretending 2026 conformance.
3. Resolve transformer/earthing and source/temperature data; run only scoped synthetic utility-fed fault screening after approval.
4. Select representative breakers and relay data, qualify through-device current and coordination. Keep generator-mode settings open until matching alternator/excitation data.
5. Expand literature by technical discipline as described in protocol; add full-text peer-reviewed sources, evidence extraction and contradiction log before each later module. No fixed deadline.

Review status: AI-assisted targeted research. All assumptions/changes above are proposals unless explicitly sourced. Maintainer should review and independently explain results. No engineering or legal certification.
