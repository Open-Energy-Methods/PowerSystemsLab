# Verification and validation protocol

## Gate sequence
1. State question, scope, model equations and assumptions.
2. Register sources, units, bases, uncertainty and rights.
3. Predeclare expected outputs, tolerances (absolute and relative), solver settings and pass/fail rules.
4. Check analytical limiting cases, signs, conservation, units and numerical convergence.
5. Run independent reference implementation or published benchmark where available.
6. Report raw and derived results, mismatches, negative findings, limitations and reproducibility instructions.
7. Learner solves a variant and explains the result without generated notes.

## Evidence categories
- Unit test: implementation property.
- Regression: comparison with earlier outputs or native package case.
- Numerical verification: analytical or independent numerical reference with aligned inputs.
- Physical validation: comparison to measurements with uncertainty; not implied by cross-tool agreement.
- Educational engineering screening: not compliance or approval.

Record commit, environment, input hashes, solver settings, commands, timestamp, output paths, reviewer and discrepancy disposition. Independent checks may not use the same computational implementation. Avoid tolerance changes after seeing results; document any revised protocol and rerun.

Candidate load-flow comparison tolerances: voltage 0.005 pu and branch power 1% plus predeclared absolute near-zero tolerance. Candidate initial fault current tolerance 2% for matched models. These are study proposals, not standards requirements. Check reference uncertainty and tighten/justify for each case. Distinguish different current definitions and model options; do not force a match.

For variable-current inverse-time relay, integrate 1/T(I) above pickup with explicit reset and measurement conventions; compare against constant-current formula and independent piecewise integration. Test timestep sensitivity, pickup crossings and failure-to-trip cases. Manufacturer selectivity tables needed where energy selectivity matters.

## Publication gate
No unqualified results or implied physical validation. No restricted commercial artefacts, licence keys, proprietary standards text or employer data. No use in real installations without appropriately authorised engineering review.
