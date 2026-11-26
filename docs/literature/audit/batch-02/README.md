# LR0 Batch II — initial targeted audit

10 PDFs, 1253 pages, all opened and text extraction attempted; four pages with no extractable text. 24 selected pages rendered and visually inspected. Other pages are indexed, not claimed visually reviewed. No full handbook audit or systematic literature review closure. Source PDFs, screenshots and full extracted text are not redistributed. AI-assisted review, maintainer review pending.

| ID | Source | PDF pages | Visually inspected pages | SHA-256 |
|---|---|---:|---|---|
| B01 | Hodder et al., Low Second-Harmonic Content (2014) | 20 | 10,15 | 355f6dad23bcd9f6334cde4f45a6911c3c5156b900608aa60bd75ce71e81c562 |
| B02 | Kasztenny and Samineni, Transformer Differential Protection Revisited (2025) | 19 | 7,17 | 4d2663139edccf64e0b589232a3bf8a2b6ec8107996f65516bcfd9a3c5358a23 |
| B03 | Roberts et al., Ground Fault Protection Methods | 40 | 4,22,36,37 | 7f133ef96713a34d10ee7c98cd4ac4df0c7784e1525c0a10d2fc34c3a1872e75 |
| B04 | Schneider Selectivity Guide (September 2026) | 362 | 9,104 | 01407b3e5fe570fdb0d09c2e67efe3154d9648c4a64088b48bb1ebaad8ca605e |
| B05 | Eaton Power Distribution Systems (2017) | 152 | 96 | 764eaf802caf45f449d0633dd35d79a0cbf7f487cd747c9af2530d4fde78ef94 |
| B06 | Schneider Electrical Installation Guide (2018) | 588 | 451 | 418db6175a792d4936dea1a505428dbef6371d8da3eb7b9e5f741cc100f95af7 |
| B07 | Deepak et al., Load-Flow-Based Initial Short Circuit (2025) | 19 | 8,10,14,15 | 500db02522cd1235ac690fa5c65fa7a50d5f5d03104380dbc7f32ba8362ae920 |
| B08 | Boutsika and Papathanassiou, DG Short Circuit (2008) | 11 | 2 | bca54a441a1457bb29ddcf6a3e56f551491f7aeb2b3bb39929f860505aa3a1e5 |
| B09 | Thurner and Braun, Vectorized Short Circuit (2018 preprint) | 6 | 3,4,5 | bab9980fb678d4b5af655e4f3cfa6007b2931a3811f3e5c217d0d40e88db07f0 |
| B10 | Schneider CT158 (2000) | 36 | 29–32 | 91adeeee24b1e266587f1eba2e3f87f9b614a39e2ab944cdf9897835e9d96b6f |

## Findings and implications (one-based PDF pages)
- B01 pp.10,15: deep core saturation can reduce second harmonic and dwell intervals, compromising fixed harmonic blocking. Cross-phase blocking and lower thresholds trade security against dependability. Test internal fault during inrush, CT effects and filter windows; no settings inferred.
- B02 pp.7,17: Table I uses winding-connection-specific differential and restraint terms; CT saturation during external faults creates spurious differential current. Enhanced methods and REF are separate functions; paper's fast operation is not universal or breaker clearing time. Independent vector compensation, CT saturation and external-fault logic benchmarks needed.
- B03 pp.4,22,36–37: grounding topology changes fault paths, voltage displacement and directional relay sensitivity. Include feeder capacitance and neutral impedance; compare resistance, isolated and resonant alternatives; do not transfer country examples or overhead-line self-extinction to cable campus. CT/VT errors and unbalance affect detection.
- B04 pp.9,104 (A-1/A-96): separate partial/full/total selectivity, cascading and tested combination limits. Table includes candidate MTZ2/3–NSX/NS devices at <=440 VAC with exact trip-unit/rating conditions. T means total up to downstream breaking capacity, not unlimited. Check overload, earth fault and all sources separately; no product selection or setting approval.
- B05 p.96 (1.7-16): machine subtransient, transient and synchronous reactance and ground-fault effects; US 2017 guide, not IEC design rules. Sections 1.4–1.7 are priority for deeper reading.
- B06 p.451 (N19): generator excitation changes sustained fault current; time grading increases thermal stress. Text from pp.439–440 and 450 also identifies battery recharge, bypass and separate source duties. Historical 2018 examples are not equipment data. Chapters B,D,E,F,G,H,M,N are priority for detailed review.
- B07 pp.8,10,14–15: proposed LF-SCC uses prefault SG internal voltage, GFL prefault current and iterative GFM current limit. Load model is constant impedance in study. Reported real-grid comparison VDE estimates about 1.25–1.55 times RMS results across investigated mixes; LF-SCC close to RMS, not physical validation. Conclusion p.17 limits method to initial currents; breaking current future work. No blanket claim IEC sizing method is wrong or UPS equivalent to generator.
- B08 p.2 (1182): near/far-generator AC decay description appears transposed relative to later equations. Historical method; do not copy error or assume three-phase fault always maximum.
- B09 pp.3–5: Eq.3 prints 0.04/K; apparent decimal error, verify normative formula and material. Eq.8 subscript differs from diagonal Zjj in subsequent matrix. Three-bus mixed-source and four-bus wind case are candidate benchmarks, not executed. Initial current only derived in paper. 
- B10 pp.29–32 (printed 27–30): voltage factor 1.0 in problem, 1.1 in solution. Independent exploratory nodal reconstruction of printed simplified sequence networks matches all eight impedance/current values within predeclared 1% tolerance; see CT158 note and script. No native solver or formal closure.

## Outstanding
Full page review for remaining 1229 pages, detailed OEM curves/footnotes and exact device ratings, current IEC texts, matching generator/UPS data, physical validation, formal review and CI. LR0 open. No campus assumptions or model code changed. PR #4 was not mergeable before this update; no merge attempted.
