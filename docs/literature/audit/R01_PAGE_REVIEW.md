# Thurner et al. (2018) — pandapower

Source file: `thurner2018.pdf` | SHA-256: `f19c0d2ad043af17d119f1b24ce8f24a80292952ba27d60046b406c4d706cd92` | 12 PDF pages.

Method: all page images rendered and scanned in sequence; selected figures, tables and numerical passages inspected using page images and extracted text. Not a verification of every cited secondary source or reproduction of every result. PDF page numbers are one-based.

| PDF page | Review finding |
|---:|---|
| 1 | Abstract and scope; static/quasi-static balanced studies; PYPOWER lineage. |
| 2 | Version 1.4.3 and design motivation; historical comparison, not current API specification. |
| 3 | Fig. 1: element tables and result tables; separate electrical equivalents by analysis type. |
| 4 | Table I and element models; ZIP load, PV/slack, line pi model; historical kW/kvar and sign conventions. |
| 5 | Transformer T/pi equivalents, tap and shift, three windings, ideal switches; model branches explicitly. |
| 6 | Table II and Fig. 2: fuse closed bus switches, auxiliary nodes for open terminal switches; conversion and result mapping. |
| 7 | Fig. 3: timings depend on hardware and cases; WLS, OPF and IEC 60909; not current release qualification. |
| 8 | Figs. 4–5: distribution test grid and reduced topology; graph connectivity, standard types and converters. |
| 9 | Fig. 6 and §VII: 276 possible states, 96 topology rejects, 100 fault rejects, 80 remaining, then inconsistent 88. Constraints are example-specific. |
| 10 | Figs. 7–8: voltage, loading, fault minimum, tap position, losses and topology over time; independent time steps neglect switching history. |
| 11 | Conclusions and comparisons; reported verification of equivalents is not our validation. |
| 12 | References and biographies; references not independently retrieved. |

## Critical assessment and project implications

The paper describes 1.4.3, not 3.5.6. On printed p.6518, 276−96−100=80 but §VII-C says 88. Do not resolve by guessing. Reported 9732 power flows, seven minutes on a laptop, under 15 s on 48 cores (p.6519) are historical timings. Proposed study: independent Ybus and tap/phase-shift implementation, topology filtering followed by min-fault, voltage and thermal screening, explicit switching cost and time coupling when appropriate. The paper's ±3%, 50% loading and 1.1 kA thresholds are not campus requirements.
