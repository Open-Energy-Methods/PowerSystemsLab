# F01 — AC circuits and phasors

Status: PLANNED. No code or learner evidence yet.

## Objectives
Explain sinusoidal steady state, RMS vs peak, impedance, complex power and leading/lagging power factor. Solve a series RLC circuit independently before using a numerical tool.

## Exercise
Use an illustrative 24 V RMS, 50 Hz source, R=10 ohm, L=30 mH, C=100 microfarad. These are synthetic calculation values, not an approved hardware design. Calculate X_L, X_C, Z, I, P, Q and S by hand, state the reference phasor and sign convention, and check S=V I* and P=I²R. Explore limiting cases of pure resistance, inductance and capacitance, and the resonant frequency. Then implement complex arithmetic in plain Python; compare hand results with code and document numerical tolerances before running.

## Deliverables
Learner theory notes, worked derivation, Python implementation, tests covering signs and limiting cases, short explanation of reactive power and resonance. Independent variant: change frequency and predict leading/lagging before recalculation.

No physical experiment is necessary. If proposed later, follow experimental safety approval. Completion requires demonstrated learner understanding as well as checked numerical results.
