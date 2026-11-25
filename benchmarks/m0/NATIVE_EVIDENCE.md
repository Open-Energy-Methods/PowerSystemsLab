# Native qualification evidence — initial AC and 3ph solver gates PASS

[GitHub Actions run 45721392256](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45721392256), tested commit 6bf8b57b490610965319888dfff5ff81c261316f; job qualify (139580324724) completed successfully. Result JSON and pip-freeze were uploaded by the workflow. Python 3.12.16, pandapower 3.5.6, NumPy 2.4.6, SciPy 1.18.1, pandas 2.3.3, networkx 3.7. Full environment available in workflow artifact, not yet a lockfile.

| Quantity | Native | Reference |
|---|---:|---:|
| receiving voltage pu | 0.9950630645714083 | 0.9950630645714081 |
| receiving angle deg | -0.28790145400331785 | -0.2879014540033181 |
| source MW | 2.005857695355906 | 2.005857695355921 |
| source Mvar | 0.8140584688542063 | 0.8140584688542095 |
| line loss MW | 0.005857695355914627 | 0.005857695355914783 |
| line loss Mvar | 0.014058468854195372 | 0.01405846885419548 |
| max 3ph Ikss kA | 5.888071061601967 | 5.888071061601967 |
| min 3ph Ikss kA | 4.0249966728095785 | 4.0249966728095785 |

All comparisons passed predeclared tolerances.

CIGRE MV no-DER regression: 15 buses, 15 lines, 2 transformers, 18 loads, 8 switches, 1 grid. Source 45.045731794076985 MW, demand 44.742149999999995 MW, losses 0.30358179407688524 MW; minimum 0.9229797752679476 pu at bus 11, maximum 1.03 pu. Counts, convergence, finite voltages, and active power balance PASS. Native regression, not independent CIGRE verification.

M0/W0 remains partial: asymmetric fault/sequence tests, CT158, generator-mode limitations, independent CIGRE cross-check, transitive lock, commercial tools and learner evidence remain open. Balanced campus load-flow smoke testing may proceed; no qualified campus fault or equipment-duty claims.
