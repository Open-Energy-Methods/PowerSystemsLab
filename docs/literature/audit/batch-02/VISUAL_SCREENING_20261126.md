# Batch II visual screening continuation — 2026-11-26

Status: PARTIAL. All 151 pages of seven shorter documents and 27 selected pages of three long guides were rendered from the supplied PDFs and actually viewed on 24 labelled contact sheets. 178/1253 distinct pages screened; 1075 not screened. This includes earlier targeted pages, not in addition to them. Contact-sheet viewing is visual screening (figures, layout, topic coverage), not a full-resolution verification of every equation or table cell. Selected passages were reopened via text extraction to confirm detailed findings. Blank pages and front matter count as physical PDF pages. No secondary citation verification or new simulation execution. Source hashes and filenames remain in the initial audit. Images and PDFs are not redistributed.

| Source | Screened | Total | Page coverage |
|---|---:|---:|---|
| B01 | 20 | 20 | 1–20 |
| B02 | 19 | 19 | 1–19 |
| B03 | 40 | 40 | 1–40 |
| B04 | 9 | 362 | 9, 10, 11, 12, 13, 14, 15, 104, 105 |
| B05 | 9 | 152 | 1, 3, 4, 5, 6, 7, 8, 95, 96 |
| B06 | 9 | 588 | 433, 434, 439, 440, 445, 446, 447, 450, 451 |
| B07 | 19 | 19 | 1–19 |
| B08 | 11 | 11 | 1–11 |
| B09 | 6 | 6 | 1–6 |
| B10 | 36 | 36 | 1–36 |

## Source-specific findings and follow-up
### B01 Hodder et al. (2014)
PDF pp.1–2 cover/history; 3–6 transformer equivalent circuit, magnetic characteristics and inrush; 7–9 blocking/restraint and field examples; 10–12 ultrasaturation and transient flux; 13–14 transformer design and CT effects; 15–16 mitigation and tradeoffs; 17–19 dwell-time and bidirectional differential logic; 20 conclusions/references. Figs.23–26 and 29–39 motivate testing low harmonic inrush, external CT saturation, and internal faults during inrush separately. Do not copy thresholds as design settings.

### B02 Kasztenny and Samineni (2025 conference version)
PDF pp.1–6 motivation, standing differential errors, 87T/REF and enhanced architecture; 7–9 winding-specific compensation and restraint; 10–12 inrush/voltage and CT challenges; 13–15 external-fault detection and arming; 16–18 simulation examples; 19 conclusion/references. P.16 uses a 115/230 kV 150 MVA 0.15 pu wye-delta transformer, not our LV block. P.17 shows a simulated external ABG fault with CT saturation after about 1.5 cycles; a 75% restraint alone is insufficient in that example. External-fault detection secures the element before spurious differential current develops. Independent relay logic, vector compensation, CT error models and REF cases required.

### B03 Roberts et al.
PDF pp.1–7 grounding options; 8–12 directional elements; 13–19 isolated-neutral phase and sequence analysis; 20–24 compensated networks and measurement errors; 25–27 voltage and wattmetric methods; 28–33 conductance/incremental conductance and EMTP examples; 34–35 VT connections; 36–37 Tables 2–3 and conclusions; 38–40 references and biographies. Table 2 distinguishes 32I/32Q/32V (solid/low impedance), 32U (isolated neutral), combined 32W/32C (high-resistance, high-reactance and resonant grounding) as authors' recommended directional methods. Table 3 identifies sensitivity constraints due to asymmetry, CT/VT inaccuracies, unbalance and CT saturation. Cable capacitance, neutral displacement and measurement errors must be included in grounding comparison. Not generic protection approval.

### B07 Deepak et al. (2025)
PDF pp.1–6 compares EVS and complete method; 7–10 LF-SCC formulations and flow chart; 11–12 modified IEEE-39 case; 13–15 regional network comparison; 16–17 discussion/conclusion; 18–19 references. Important reproduction details p.11: line lengths reduced by factor 10 for stability; initial current from RMS at 0.1 ms after fault; replacement holds pre-fault P/Q and nominal capacity. Figure 5 reports maximum +3% deviation of LF-SCC for modified IEEE-39 cases. P.15 regional study: 1.25, 1.35, 1.45, 1.55 times RMS for 0,6,12,18 SG replacements in the studied area, not proof of a wholly converter-only regional grid. GFL current in the VDE comparison is the pre-fault magnitude, not 1.1 pu. LF-SCC reported 96–99% of RMS for final replacement scenario. This does not establish equipment-sizing limits or hardware validation. Prior chat chart label "0 SGs" was overbroad; use replacement counts. Full regional dataset availability and current solver version remain open.

### B08 Boutsika and Papathanassiou (2008)
PDF pp.1–4 historic IEC framework, current definitions and correction factors; 5–6 DG types; 7–9 case network and detailed calculation tables, transformer tap influence; 10–11 fault reduction options and conclusion. P.2 apparent transposition of near/far generator decay wording persists. Tables 1–2 and Figure 5 provide a later independent tap/fault benchmark. Do not apply historical converter assumptions as current standards.

### B09 Thurner and Braun (2018)
PDF pp.1–2 scope and model representation; 3 element equivalents and voltage factors; 4 vectorized voltage/current-source methods; 5 three-bus numerical example and wind park validation; 6 radial MV case and conclusion. P.3 Eq.3 prints 0.04/K; CT158 printed p.25 uses 0.004/K for its stated materials (historical confirmation, not current normative review). Eq.8 impedance index conflicts with following diagonal expression. P.5 three-bus published total 145.254,4.052,4.641 kA; Fig.5 four-bus with/without wind parks and 3.903 kA at bus 2 with wind parks. No new reproduction. P.6 case illustrates dependency on radial source distance and DG.

### B10 Schneider CT158
PDF pp.1–5 front matter/lexicon; 6–13 fault duty, waveform components and assumptions; 14–20 impedance method, equipment impedances, voltage referral; 21–24 first industrial network example (Fig.21 and Fig.22); 25–28 sequence components and current definitions; 29–32 second example and equivalent circuits; 33–36 conclusion/bibliography/blank/back page. Existing simplified sequence reconstruction remains exploratory, c=1 vs c=1.1 discrepancy retained. Add a distinct LV impedance-method benchmark using first example and verify units/rounding before use; no new run.

### B04 Schneider Selectivity (2026) — targeted only
PDF 9–15 (A-1 through A-7),104–105 (A-96/A-97). Current/time/energy/logic and cascading distinctions; p.15 table assumptions include maximum long-time setting and upstream short-time pickup 10 Ir, with stated alternatives and ratios. Pp.104–105 table legends define T up to downstream breaking capacity. Footnotes explicitly require separate earth-fault check for upstream MicroLogic 6/7; some combinations have Ir upstream >1.3 Ir downstream. Candidate comparison must capture exact voltage, capacity class, trip unit, pickup, delay, instantaneous mode, overload/earth leakage requirements, table cell and footnotes. No specific combination approved; no table wholesale reproduced.

### B05 Eaton (2017) — targeted only
PDF 1,3–8,95–96: scope/contents, objectives, single-line design process and generator fundamentals, hybrid high resistance grounding diagram and short-circuit behaviour. Use as industrial design workflow and candidate grounding comparison; US-oriented requirements and historical edition cannot be applied as EU normative rules. Full guide not reviewed.

### B06 Schneider Electrical Installation Guide (2018) — targeted only
PDF 433–434,439–440,445–447,450–451. Fig.N8 separates utility, generator, rectifier and bypass supplies. Fig.N10 staged rectifier restart example; no universal ramp. UPS modes and battery selection pp.445–447. Fig.N25 p.450 explicitly distinguishes breaking duty for strongest supply and trip dependability on weakest, bypass/static-switch limits and load energization. P.451 shows excitation-dependent sustained currents and time-grading thermal tradeoff. Do not copy illustrative 2018 overload/current/delay factors as modern OEM settings. Add four separately documented supply states: utility via inverter, utility bypass, generator-fed rectifier/bypass and battery/inverter-only; verify actual device topology and permissible combinations.

## Decision
Continue long handbook review by chapter and full-resolution extraction of relevant table cells. 1075 pages remain unviewed (B04 353, B05 143, B06 579). LR0 remains OPEN; full standards, equipment data, independent benchmark reproduction, and maintainer review remain open. No commercial or campus simulations changed. Do not represent contact-sheet coverage as verification of all numerical claims.
