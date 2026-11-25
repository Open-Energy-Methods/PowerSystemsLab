# M0 — Environment qualification

Status: PARTIAL. The assistant executed reference calculations locally using CPython 3.13.5. NumPy, SciPy and pytest were import-discoverable, not version-qualified. pandapower was not installed. No PowerFactory, PSCAD, CIGRE, IEC 60909 solver or CI run has been qualified in this environment.

## Reproduce the standard-library exercise
From the repository root:
```sh
python modules/F01-ac-circuits/f01.py
python -m unittest discover -s modules/F01-ac-circuits -v
```
The reference implementation is AI-assisted. Local tests are numerical evidence, not learner assessment. The learner should solve independently before inspecting the reference.

## Remaining M0 gates
- Select a supported Python and pinned pandapower version; record installation and dependency versions.
- Verify native load flow, an analytical two-bus short circuit and a CIGRE MV regression case.
- Record options, tolerances and generator-mode restrictions before applying the solver.
- Reproduce the existing PSCAD native case on the user's licensed installation; record version and node limits.
- Establish legitimate PowerFactory access and publication permissions before evaluation.
- Select repository licensing before third-party reuse.

No commercial software is required for F01. Do not represent this preliminary environment audit as full qualification.
