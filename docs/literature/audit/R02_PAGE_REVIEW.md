# Zimmerman et al. (2011) — MATPOWER

Source file: `zimmerman2011.pdf` | SHA-256: `2538b852baa3ad899cb6b5a0141fa810fe6414a1885b561c9bac53365f76b87a` | 8 PDF pages.

Method: all page images rendered and scanned in sequence; selected figures, tables and numerical passages inspected using page images and extracted text. Not a verification of every cited secondary source or reproduction of every result. PDF page numbers are one-based.

| PDF page | Review finding |
|---:|---|
| 1 | Scope and toolbox architecture; AC/DC PF and OPF, not dynamics. |
| 2 | Fig. 1 and eqs.1–7: pi branch, complex tap at from end; per-unit and sign conventions. |
| 3 | Eqs.8–29: sparse admittance assembly, AC power balance, DC approximations and phase shifts. |
| 4 | Eqs.30–36: slack/PV/PQ, Newton and alternatives, Q-limit outer loop; power flow does not enforce all OPF limits. |
| 5 | PTDF/LODF with slack distribution; AC and DC OPF formulations and branch limits. |
| 6 | Extended objective/constraints, piecewise-linear cost, dispatchable loads, capability and angle constraints. |
| 7 | Table I: OPF case dimensions and binding constraints; algorithms and historical experiment setup. |
| 8 | Table II: run times and conclusion; not present-day runtime predictions; references/biographies. |

## Critical assessment and project implications

MATPOWER v4 paper: DC approximation neglects branch resistance/charging, assumes near-unit voltage and small angle differences (p.14). Cannot validate reactive demand or voltage margin using DC flow. Branch tap orientation, line charging, bus shunts, generator Q limits and base alignment are required in AC comparisons. PTDF/LODF screening is not a substitute for island-aware AC restoration. Use independent code and documented comparison case to reduce common ancestry risk.
