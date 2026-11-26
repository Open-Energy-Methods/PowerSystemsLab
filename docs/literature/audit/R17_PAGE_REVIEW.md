# Cui et al. (2021) — ANDES

Source file: `13fef153-07ad-4173-b5f2-4e7934591cd6.pdf` | SHA-256: `75c865b1921f07a1f9f769c518d34f4360cf19aae688318350779feaf1fbf66a` | 12 PDF pages.

Method: all page images rendered and scanned in sequence; selected figures, tables and numerical passages inspected using page images and extracted text. Not a verification of every cited secondary source or reproduction of every result. PDF page numbers are one-based.

| PDF page | Review finding |
|---:|---|
| 1 | Abstract, DAE framework and published scope; DOI 10.1109/TPWRS.2020.3017019. |
| 2 | Fig.1: symbolic model-type code generation and numerical case-specific execution. |
| 3 | Listing 1 and Fig.2: shunt equations, sign convention and discrete limiter flags. |
| 4 | Figs.3–4, listings 2–3: services, centre of inertia and reusable transfer blocks. |
| 5 | Eqs.2–4, Table I and Fig.5: sparse Jacobians, metadata and data flow. |
| 6 | Fig.6: initialization and algebraic equation update; shared vs local variable addresses. |
| 7 | Figs.7–8 and Listing 4: sparse Jacobian construction and TGOV1 model. |
| 8 | Listing 5, Table II, Figs.9–10: power-flow timing and Kundur dynamic comparison; fixed 1/30 s trapezoid and PQ-to-Z conversion. |
| 9 | Figs.11–15: excitation, speed and voltage comparisons; modified IEEE 14 and NPCC 140; event definitions. |
| 10 | Fig.16, Table III: eigenvalues and damping comparison; Appendix Tables IV–VIII bus/line/load/generation data. |
| 11 | Appendix Tables IX–XI: GENROU, EXDC2, TGOV1 parameters; references start. |
| 12 | References and biographies; redistribution notice; no source PDF redistribution. |

## Critical assessment and project implications

Kundur case uses four GENROU machines, EXDC2 and TGOV1; opens one of the two lines 8–9 at t=2 s. IEEE 14 opens 1–2 at 1 s, reconnects after 2 s. All PQ loads become constant impedance after PF and implicit trapezoid uses 1/30 s. These are essential reproduction settings, not interchangeable with constant-power UPS dynamics. Appendix IV–XI enables a candidate reconstruction, but data transcription and current ANDES version are unqualified. Time-domain comparison is cross-code verification, not field validation. Table III damping comparison should be used with eigenvalue matching and documented units.
