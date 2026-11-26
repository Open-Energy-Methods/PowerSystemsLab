# PSCAD (2018) — remanent flux technical example

Source file: `remanent_flux_transformer.pdf` | SHA-256: `be43c7d0d9d4a2e47f9fcab4e2d0a648673bb7fc878f35b48ba8f2e95e203e78` | 5 PDF pages.

Method: all page images rendered and scanned in sequence; selected figures, tables and numerical passages inspected using page images and extracted text. Not a verification of every cited secondary source or reproduction of every result. PDF page numbers are one-based.

| PDF page | Review finding |
|---:|---|
| 1 | Figs.1–2: 10 MVA 66/0.64/0.64 kV three-winding transformer, essentially unloaded secondaries via 1 Gohm; Master/Slave set. |
| 2 | Figs.3–5: four real sweep variables, three residual fluxes and closing time; screenshots show 10 runs per variable alongside range/increment. |
| 3 | Fig.6: saturation on winding #1, basic hysteresis, knee 1.25 pu, air core 0.275 pu, magnetizing current 1%, decay .69 s; cross-case signals. |
| 4 | Figs.7–9: XGE error and output-file location; no numerical waveform or peak reference. |
| 5 | Figs.10–11: local process execution workaround in Professional 4.6.1 screenshot; not proof of Free Edition support. |

## Critical assessment and project implications

See archive audit for 60 Hz and saved timestep. Treat as procedural reproduction, not numerical validation. Closing-time grid is inconsistent with both inclusive endpoint and 10 equally spaced points; residual flux grid also does not imply ten distinct levels. Do not infer exact schedule or Cartesian run count from configuration alone. Capture actual run log. A 50 Hz adaptation is a separate model. No results supplied.
