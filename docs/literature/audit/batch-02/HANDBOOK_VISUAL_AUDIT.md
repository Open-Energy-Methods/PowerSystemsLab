# Batch II handbooks — complete page-level visual screening
26 November 2026. Three original supplied PDFs reopened and SHA-256 matched to Batch II inventory. 33 labelled contact sheets (up to 36 pages each), all opened and visually screened in sequence: B05 5 sheets, B04 11 sheets, B06 17 sheets. All 1102 handbook pages screened including covers, blanks and appendices. Selected additional pages reopened at scale 1.65 (B05 p55; B04 pp223,256,299,346; B06 pp270–273). Contact sheets resolve structure and visual content, not every table entry or equation. Text extraction supports topic mapping; no claim of full-resolution review of every cell. Prior seven shorter documents: 151/151. Batch II total 1253/1253; combined with Batch I 1381/1381. All-page visual screening closed; LR0 not closed. Source PDFs and screenshots remain outside public repo.

## B05 Eaton Power Distribution Systems, August 2017 (152 pages)
| PDF pages | Subject / inspected visual evidence | Project use |
|---|---|---|
| 1–6 | Contents, design principles, objectives | Design requirements register |
| 7–28 | One-lines, standard symbols, primary/secondary arrangements, equipment drawings | Independent SLD and asset inventory |
| 29–40 | Radial, loop, selective and network arrangements | Topology and interlock comparisons |
| 41–62 | Fault-waveform relationships, breaker duty, calculation charts, worked fault examples, transformer R/X and voltage drop | FaultPhysics and equipment models |
| 63–68 | Protection curves, coordination considerations | Device-current and time-grading checks |
| 69–80 | Grounding alternatives and ground-fault diagrams | Earthing comparison, distinguish system from equipment bonding |
| 81–104 | Transformer, generator, motor and power-factor data, generator protection diagrams | Machine and equipment models |
| 105–112 | Healthcare emergency supply, transfer arrangements and load bank | Generic continuity lessons; not data-centre code |
| 113–126 | Power quality, disturbances, harmonics and UPS illustrations | Power-quality measurement and mitigation |
| 127–138 | Seismic, building and arc-related considerations | Specialist design constraints; separate scope |
| 139–152 | Standards, device designations and conductor data | Historical US reference, not applicable IEC ampacity approval |

PDF p55 (printed 1.4-15) Fig.1.4-9 checked individually. Published approximate scalar-impedance example: 500 MVA utility, 1000 kVA 480 V transformer uk 5.75%, three 250 kVA motor feeders with 1.00 pu motor impedance per branch, 0.027 pu cable per branch and faulted outgoing cable. 1 MVA base; source path 0.0595 pu, three motor paths equivalent about 0.342 pu, F1 combined 0.0507 pu, F2 0.0777 pu. Published symmetrical currents 23.720 and 15.480 kA. Conductor prose uses 0.00617 ohm whereas step 5 says 0.00619; preserve both and distinguish rounded source values. This is a shortcut magnitude combination, not complex R+jX method or IEC 60909 qualification. Compare with a full complex case only after R/X inputs are sourced. No numerical reproduction executed here.

## B04 Schneider Selectivity, Cascading and Coordination Guide, September 2026 (362 pages)
| PDF pages | Visual structure | Project use |
|---|---|---|
| 1–8 | Cover, legal notice, contents | Edition/source identity |
| 9–24 | Selectivity principles, curves, conditions and quick table access | W5 data schema and settings conditions |
| 25–109 | AC breaker selectivity matrices | Candidate upstream/downstream pairs, exact voltage and trip unit |
| 110–125 | Motor circuit breaker selectivity tables | Cooling feeders |
| 126–150 | 690 V AC tables | Other voltage variants, not 400 V default |
| 151–184 | DC selectivity examples and tables | UPS battery/DC circuits, separate DC study |
| 185–199 | Fuse selectivity curves/tables | Fuse-based protection variants |
| 200–222 | Cascading principles and tables | Conditional breaking capacity, separately from selectivity |
| 223–254 | Enhanced selectivity through cascading; tables | Qualified combinations only |
| 255–288 | Motor breaker coordination, type 1/2 tables | Starter survivability and restoration |
| 289–296 | Motor fuse coordination | Alternate motor protection |
| 297–342 | LV switches and transfer switching equipment, coordination | TSE duty, source transfer and isolation |
| 343–344 | LV transformer and capacitor protection | Inrush and capacitor bank protection |
| 345–362 | Busbar trunking coordination and back cover | Separate conductor/trunking withstand |

Selected enlarged pages:
- PDF 223 / A-215: NSX250H TM250D upstream + NSX100F TM25D downstream example. Ordinary total selectivity up to downstream breaking rating 36 kA; enhanced breaking capacity and enhanced selectivity both 70 kA for stated combination. Two different values in a cascading table cell denote separate selectivity and breaking limits. Not general permission to use 70 kA for other breakers.
- PDF 256 / B-2: Type 1 coordination can allow starter/contact damage with safety conditions; Type 2 expects continued operability subject to permitted minor contact welding and separation. Distinct from upstream/downstream selectivity. Cooling restart and maintenance should distinguish these conditions.
- PDF 299 / C-3: switch-disconnector utilisation categories AC-21/22/23, frequent vs nonfrequent duty, conditional short-circuit ratings and short-time withstand. A switch-disconnector is not a general fault-interrupting breaker. Do not infer transfer switch suitability from continuous current alone.
- PDF 346 / E-2: example two 630 kVA 400 V uk 4% transformers; prospective fault 44 kA at main and 33 kA downstream. Source specifies NSX630N (50 kA breaking capacity) / KSA630 protection level 50 kA; NSX160F (36 kA breaking capacity) / KSA160 protection level 35 kA. Breaker capacity and protected trunking level separate quantities. Educational source example, not a chosen campus pair. No bulk table transcription; no claim of every cell verified.

## B06 Schneider Electrical Installation Guide 2018 (588 pages)
| PDF pages | Chapter | Project use |
|---|---|---|
| 1–8 | Front matter | Edition and scope |
| 9–32 | A general design | Load demand, simultaneity and design methodology |
| 33–76 | B MV utility connection | Substations, equipment, protection and interlocks |
| 77–94 | C LV utility connection | Supply arrangements; local constraints |
| 95–128 | D architecture selection | Architecture assessment, backup and maintainability |
| 129–170 | E LV distribution | TT/TN/IT, bonding, busways, environment |
| 171–226 | F shock/fire protection | Loop impedance, RCD, disconnection and fire safety |
| 227–274 | G conductor sizing | Installation method, derating, voltage drop, short circuit and PE/neutral |
| 275–308 | H switchgear | Breaking/making/withstand, selectivity and maintenance |
| 309–346 | J overvoltage protection | Lightning and coordinated SPD protection |
| 347–378 | K energy efficiency | Energy measurement and efficiency opportunities |
| 379–408 | L PF correction | Reactive compensation, location, capacitor resonance |
| 409–432 | M harmonics | THD, spectra, resonance, neutral heating, mitigation |
| 433–497 | N particular sources and loads | Generator, UPS, bypass, transformer and motor protection |
| 498–530 | P photovoltaics | DC/AC architecture and monitoring, future study |
| 531–546 | Q special locations | Reference only; not industrial campus scope |
| 547–574 | R EMC | Earthing mesh, routing, shielding, coupling |
| 575–588 | S measurement and end matter | Meter accuracy and operating uncertainty |

### New worked benchmark: G69–G72, PDF 270–273 (enlarged individually)
630 kVA 20/0.4 kV transformer, 4% impedance, 7100 W load loss (G70); 250/500 MVA MV source in one-line; 250 kVA standby generator on separate LV section; TN-S main and downstream IT isolation transformer. Follow utility path C1/C3/C7.
| Quantity | Ecodial Fig.G70 p271 | Simplified Figs.G71–G72 pp272–273 |
|---|---:|---:|
| C1 load current A | 909 | 909 |
| C3 load current A | 518 | 526 |
| C7 load current A | 238 | 238 |
| C1 3ph kA | 21.5 | 21 |
| C3 3ph kA | 21.5 | 19 |
| C7 3ph kA | 18 | 18 |
| C7 cumulative voltage drop % | .714 | .73 |
C1 2x240 mm², C3 2x120, C7 1x95 Cu phase conductors in source example. G69 lists L7 140 kW and L8 160 kW; G46 describes C3 load as 310 kW at pf .85. Do not assume the reason for differences (software load/voltage conventions, approximations or publication discrepancy). Arithmetic check 310 kW/(sqrt(3)*400*.85)=526.4076 A. G47 PE example: 21 kA, .5 s, k=143 yields 103.8409 mm² (printed 104); source notes lower-impedance fault-protection check also needed, so this thermal minimum is not final selection. No model reproduction; establish benchmark input convention and independently recompute later. Historical standards references not current normative proof.

### Further research implications
Chapter M p421 diagrams distinguish source L and shunt C resonance; p425 addresses neutral current from triplen harmonics. Approximate relation IN≈3 I3 assumes balanced conditions and dominant third harmonic; later model should allow other triplen and load unbalance. Do not presume modern UPS output/input harmonics equal server harmonics. Chapter N p491 distinguishes motor coordination categories; chapter S pp582–583 distinguishes intrinsic accuracy from operating uncertainty. These pages viewed on contact sheets and supporting text read; not individually enlarged in this continuation. Earlier p450 UPS strongest/weakest source example and p451 excitation limitation remain applicable. All equipment and model inputs still require verification.

## Gate disposition
Visual coverage complete at contact-sheet level. Full numerical-cell review, detailed equation and standards extraction, independent benchmark reproduction (including G69 and Eaton), current IEC text access, exact generator/UPS equipment, breaker/ATS/busway data and actual protection qualification remain open. No simulations or campus design changes. Source screenshots not redistributed. Proposed new tasks (not yet implemented): cable/PE benchmark, motor coordination, switch/TSE duty, busway protection, harmonics/neutral loading and metering uncertainty. Literature PR remains unmerged and reported not mergeable before update.
