# Preliminary analytical screening

All inputs are synthetic candidates from the design basis and earlier study plan. No external equipment ratings have been validated.

| Input | Value | Meaning |
|---|---:|---|
| IT demand | 24 MW | 16 x 1.5 MW |
| Facility/IT design-point power ratio | 1.30 | temporary aggregate proxy, not measured annual PUE |
| Power factor | 0.95 | assumed aggregate magnitude |
| HV/MV transformers | 2 x 40 MVA | candidate nameplates |
| Detailed LV transformer | 2.5 MVA, 0.4 kV, uk=6% | candidate impedance |

## Computed results
| Quantity | Value |
|---|---:|
| Estimated facility active demand | 31.200 MW |
| Apparent demand | 32.842 MVA |
| Equal-sharing normal transformer loading | 41.053% per transformer |
| Single-transformer restored-state loading | 82.105% |
| IT capacity at 100% single-transformer nameplate | 29.231 MW |
| LV transformer-only nominal symmetrical current | 60.141 kA |

Equations: P=IT*ratio; S=P/pf; utilisation=S/S_available; transformer-only I=S_r/(sqrt(3)*U_r*uk). The fault number is a stiff-source nominal-voltage illustration, NOT a maximum IEC 60909 duty or a bound on total fault current with other contributions. No source/cable impedance, voltage or correction factors, motor or generator contributions are included. Do not select breakers based on it.

The N-1 result assumes successful switching, sufficient downstream capacity, equal normal sharing and no extra losses beyond the proxy. It establishes only aggregate arithmetic headroom, not voltage, fault duty, redundancy or actual restored load. Bottom-up demand accounting replaces the proxy at W1; no additional loss may be counted twice.

The assistant executed these equations locally using CPython 3.13.5; capacity, fault and invalid-input checks passed within a combined eight-test suite. The committed test file contains the applicable screening checks. No network solver or commercial software was used. AI-assisted implementation; no claim of learner competence or independent external verification.
