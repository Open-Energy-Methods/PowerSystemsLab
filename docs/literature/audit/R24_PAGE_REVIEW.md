# NERC (July 2025) — Characteristics and Risks of Emerging Large Loads

Source file: `89c9bfa4-e22b-4209-aac6-bda553c2ac5b.pdf` | SHA-256: `e68ac29523f2bee7078af6d69654c92af994bf45e141a4af856709c496a7be02` | 49 PDF pages.

Method: all page images rendered and scanned in sequence; selected figures, tables and numerical passages inspected using page images and extracted text. Not a verification of every cited secondary source or reproduction of every result. PDF page numbers are one-based.

| PDF page | Review finding |
|---:|---|
| 1 | Cover and July 2025 document identity. |
| 2 | Contents part 1: characterization and planning risks. |
| 3 | Contents part 2: stability, power quality, security and restoration. |
| 4 | Preface map: North American reliability regions, not European jurisdiction. |
| 5 | Executive summary: approximately 1500 MW voltage-sensitive reduction events; event references need independent review. |
| 6 | Risk category diagram: seven major categories. |
| 7 | Recommendations and high-priority risk diagram; guidance for future work, not binding universal rules. |
| 8 | Printed p.1: intended audience and working definition of large load. |
| 9 | p.2: no finalized MW threshold in this report; forecast context. |
| 10 | p.3: load categories and power-electronic demand. |
| 11 | p.4 Fig.2.1: traditional data-centre one-line; IT/cooling separation and UPS-less HPC exceptions. |
| 12 | p.5: traditional vs AI training, cooling and workload dependence; uptime number not a Tier guarantee. |
| 13 | p.6 Fig.2.2: measured 50 MW block of 200 MW facility; ramp profile example. |
| 14 | p.7 Fig.2.3: ramp detail, inference, crypto and industrial categories; not universal ramp limits. |
| 15 | p.8: industrial subclasses and hydrogen facility power-electronics mix. |
| 16 | p.9 Fig.2.4: electrolyzer one-line; not data-centre topology. |
| 17 | p.10: ERCOT, NYISO, SPP and ISO-NE examples; thresholds are local. |
| 18 | p.11: utility programs and MW/voltage threshold discussion. |
| 19 | p.12 Fig.2.5: front-of-meter vs behind-meter and hybrid supply. |
| 20 | p.13 Fig.2.6: generator online/outage, unintended grid demand transfer and observability. |
| 21 | p.14: flexible vs firm load; availability and forecasting. |
| 22 | p.15: observability, high-resolution measurements and long-term planning. |
| 23 | p.16: forecast and adequacy uncertainty, project lead times and queues. |
| 24 | p.17: transmission adequacy and system performance categories. |
| 25 | p.18: restoration planning, short-term forecast and price response. |
| 26 | p.19 Fig.3.1: large load ramp down and up; reserve requirements. |
| 27 | p.20 Fig.3.2: crypto oscillation/ramp event, coordination; do not use as AI training profile. |
| 28 | p.21: real-time coordination, outage planning and stability framing. |
| 29 | p.22 Fig.3.3: stability taxonomy and ride-through definition. |
| 30 | p.23 Fig.3.4: observed data-centre load trip; voltage-sensitive response. |
| 31 | p.24 Figs.3.5–3.6: observed ~1500 MW loss and 60.053 Hz peak; not a campus threshold. |
| 32 | p.25: overfrequency consequences and rotor-angle mechanisms. |
| 33 | p.26 Fig.3.7: simulated generator angle instability after nearby load trip; simulation not field trace. |
| 34 | p.27: small-signal issues and transient/mid-term voltage stability. |
| 35 | p.28: long-term voltage and resonance/converter-driven stability. |
| 36 | p.29: forced oscillations vs intrinsic instability and system susceptibility. |
| 37 | p.30 Fig.3.8: repetitive training load fluctuations. |
| 38 | p.31 Fig.3.9: 1 Hz forcing and 11 Hz ringdown field example; distinct frequencies. |
| 39 | p.32 Fig.3.10: turbine torsional response example, power-quality introduction. |
| 40 | p.33 Table 3.1 and Fig.3.11: EAF harmonics not data-centre spectrum; data-centre before/after mitigation example. |
| 41 | p.34 Figs.3.12–3.13: furnace current spectrum and P/Q variation; distinct load category. |
| 42 | p.35 Figs.3.14–3.15: AI node-level demand and data-centre voltage/current pulse; no universal harmonic limits. |
| 43 | p.36: sag/transient, cybersecurity and manual/UFLS obligations. |
| 44 | p.37: blackstart and segmentation of restored demand; not site switching instructions. |
| 45 | p.38: conclusions, high priority risks and conditional threshold discussion. |
| 46 | p.39: medium/low priority risks; not permission to ignore power quality. |
| 47 | p.40 Table A.1: regional construct data, thresholds and rationale; historical examples. |
| 48 | p.41 Table B.1: characteristics-to-risk matrix; useful as a study requirements checklist. |
| 49 | p.42 Appendix C: contributors; provenance. |

## Critical assessment and project implications

Printed pages are PDF page minus 7 after front matter. Fig.2.2/2.3 describes a 50 MW block with fastest observed rate 1.9 pu/s over ~250 ms; normalization belongs to that block, not our 24 MW site. Fig.3.1 reports approximately 450 to 40 MW in 36 s and subsequent near-zero plateau/recovery; Fig.3.2 reports 298 MW decrease in 25 s for crypto. These are reported examples, not generic parameters. Fig.3.6 peak is 60.053 Hz in a 60 Hz system. Fig.3.9 forcing and ringdown must not be conflated. Proposed campus experiments: parameterized load steps, ride-through/reconnection logic, PMU sampling, reserve and frequency sensitivity, and eventual torsional analysis; no import of North American binding thresholds into Europe. Report is risk characterization, not validated dynamic load model.
