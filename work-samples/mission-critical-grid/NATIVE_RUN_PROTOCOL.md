# Preliminary native load-flow gate

The shared two-bus AC and 3-phase max/min SC verification and CIGRE MV regression passed in [M0 Actions run 45721392256](https://github.com/Open-Energy-Methods/PowerSystemsLab/actions/runs/45721392256), commit 6bf8b57b490610965319888dfff5ff81c261316f. Full W0 is still OPEN (asymmetric faults, CT158, generator limitations). W1 input review is also OPEN. This is permission only to exercise the draft balanced model, not to qualify the campus design or run campus fault calculations.

Predeclare topology counts, convergence, finite voltages, total specified load and active-power balance within 1e-6 MW. Report normal split-bus state and hypothetical restored state after HV/MV B transformer removed and coupler closed. No switching transient, initial interruption, isolation logic, service continuity or full N-1 coverage is assessed. Record voltages and loading without treating assumed ratings as approved criteria. Preserve failed cases.

Run locally in Python 3.12 with pandapower 3.5.6, or see the dedicated Actions workflow. No native result is claimed until logs are available.
