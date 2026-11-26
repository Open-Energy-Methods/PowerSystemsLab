# Master Bible v0.1 — consolidation record
26 November 2026. LR0 remains open.

The companion 21-page, 6,868-word Master Bible was generated as a local downloadable PDF/Markdown package, not uploaded here. This repository record captures its scope, benchmark values, evidence boundaries and implementation priorities. The full Markdown SHA-256 is 6404a9148fe920c577c7ee23e8e92e493fd7eb633496fb76a0f48edb5933d3a7. No source PDFs, manufacturer screenshots or commercial models are redistributed.

## Chapter sequence
AC circuits and per-unit; independent AC solver; electrical equipment and conductors; symmetrical components and grounding; fault physics; converter-fed faults; overcurrent/selectivity; transformer differential and CT behaviour; machine and RMS dynamics; EMT, energisation and harmonics; integrated MissionCriticalGrid; benchmark qualification; open issues; primary source register.

17 supplied PDFs, 1381 pages, prior all-page visual screening; selected source passages reopened for this consolidation. Source IDs follow earlier LR0 and Batch II audits. Full extraction of numerical tables and standards has not been completed.

## Arithmetic results
CT158, B10 PDF pp.31–32 Fig.33–35: positive/negative sequence identical, zero sequence separate. Unit-current nodal solve at H; c=1 and 1.1 preserved. Maximum relative error against eight printed rounded impedance/current targets: 0.03816%, below proposed 1% educational tolerance. Not a current IEC 60909 compliance check.
- GH open: X1=17.252895953 ohm, X0=39.45 ohm; c=1.1 I3=1.104310774 kA, I1=0.772862749 kA; c=1 I3=1.003918885 kA, I1=0.702602499 kA.
- GH closed: X1=13.049194985 ohm, X0=27.2 ohm; c=1.1 I3=1.460056264 kA, I1=1.072409067 kA; c=1 I3=1.327323877 kA, I1=0.974917333 kA.

Eaton B05 p.55 Fig.1.4-9: scalar reduction with 1 MVA/480 V base, source branch 0.0595 pu, three 1.027 pu motor branches, outgoing cable 0.027 pu. Published rounded impedances yield 23.724123 and 15.480220 kA (published 23.720/15.480). Direct scalar reduction yields 23.728918/15.482261 kA. Full complex reconstruction and motor decay remain open.

Schneider B06 pp.270–273 G69–G72: from printed R/X subtotals, C1/C3/C7 at 400 V: 19.534969/17.741993/16.784568 kA; at 420 V: 20.511718/18.629093/17.623797 kA, latter rounds to manual 21/19/18 kA. This supports but does not prove voltage convention. 300 and 310 kW at 400 V, pf .85 give 509.426708 and 526.407598 A. Ecodial 518 A remains unresolved. Voltage drop 0.7263125%; PE adiabatic minimum 103.840856 mm². Neither full Ecodial reproduction nor actual conductor selection.

Synthetic relay P01: standard-inverse educational curve; constant 8 pu with pickup 2 pu/TMS .1 gives 0.497975611 s. Decaying waveform 1.25+3.4 exp(-t/.04)+3.35 exp(-t/.2) pu does not trip; midpoint progress 0.202312728 (1 ms), 0.202313424 (.1 ms); instantaneous reset assumed. Not an actual generator or relay setting.
F01 ideal RLC: 24 V, 50 Hz, R=10 ohm, L=.03 H, C=.0001 F; Z=10-j22.406211 ohm; P=9.567498 W, Q=-21.437138 var, I=.978136 A.
A01 campus synthetic demand 30.982268 MW and 6.423242 Mvar; unchanged design assumptions. LV 2.5 MVA/400 V transformer current 3.608439 kA and 6% stiff-source fault screen 60.140653 kA; not actual duty.

Arithmetic executed locally with Python 3.13.5/NumPy 2.3.5. No new native solver or hardware study. Assertions on CT158 eight targets, synthetic relay no-trip/time-step comparison and RLC power identity; other outputs are computed comparisons, not separate automated gates. No repository CI run claimed.

## Next implementation gates
N02 independent AC Ybus/tap/Jacobian; central differences and independent cases. E01 full cable example with separate voltage/load conventions. S01 formal native CT158 reproduction; S02 complex R/X motor case conditional on source data; S03 mixed-source B09 benchmarks. G01 transformer sequence paths, capacitance and grounding. P02 exact equipment selectivity/through-device current in every source mode. P03 differential/CT/inrush cases. D01 analytical swing; D02 Kundur appendix data and original controls/events. T01 R-L waveform; T02 native PSCAD 60 Hz reproduction before 50 Hz adaptation. A02 source-qualified campus models and explicit service transfer constraints.
Priorities: full normative text access and current edition/national adoption; preserve printed source contradictions; OEM generator/UPS/earthing/cable data and exact breaker/ATS/busway tables. W4/W5 remain open. No campus configuration or solver code changed. Do not treat contact-sheet screening as verified extraction of every cell.
