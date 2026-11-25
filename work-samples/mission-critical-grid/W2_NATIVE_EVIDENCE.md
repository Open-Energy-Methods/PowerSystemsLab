# W2 — Preliminary native balanced load-flow evidence

[Actions run 45721563127](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45721563127), job 139580905391, commit 696f933180d7a0f0fe41fb7c03bdec65e888b3d4, completed successfully. pandapower 3.5.6. Input register v0.1. Reproducible JSON and environment uploaded as workflow artefacts. Model counts: 38 buses, 32 lines, 4 transformers, 32 loads, 1 coupler, 2 external grids.

| Quantity | Normal | Hypothetical restored HV transformer B outage |
|---|---:|---:|
| Load MW | 30.982268041237116 | 30.982268041237116 |
| Load Mvar | 6.423241784924212 | 6.423241784924212 |
| Source MW | 31.06281449720375 | 31.131839957355133 |
| Source Mvar | 8.01810575495372 | 9.662277411413323 |
| Loss MW | 0.08054645598050059 | 0.14957191616706023 |
| Minimum voltage pu | 0.977763883816735 | 0.9620081996875276 |
| Maximum voltage pu | 1.0 | 1.0 |
| Maximum MV feeder loading % | 14.596439533006897 | 14.83549871203845 |
| Highest in-service HV transformer loading % | 40.10120915386579 | 81.49198825289062 |

Convergence, topology, finite voltages, active power balance and specified demand assertions PASS. These are not independent cross-solver results. The restored state assumes the faulted transformer is isolated and coupler is closed. No transfer dynamics or actual availability established. W1/W2 design qualification remains open.
