# PSCAD example archive — static inspection
Source remanentflux-1.zip; SHA-256 446ad2a2db5e105ce45f5a3b72ae45e2a26c7684a637e866f8b22dd4b3baa818. Read ZIP entries in memory and parsed XML, no execution.
| Entry | Size bytes | XML version |
|---|---:|---|
| MasterCase.pscx | 71005 | 4.6.2 |
| RemanentFluxExample.pswx | 2229 | 4.6.2 |
| SlaveCase.pscx | 86744 | 4.6.3 |
Workspace Set1 references both projects, one task each. No output files or waveforms included.
## Saved parameters vs PDF
| Parameter | Archive value | Interpretation |
|---|---|---|
| Source and transformer frequency | 60 Hz | Original example is NOT 50 Hz |
| Slave duration | 0.7 s | About 0.183–0.2 s after stated closing range |
| Slave time_step / sample_step | 10 / 500 | PSCAD microsecond conventions; confirm native UI |
| Master duration / timestep | 0.0005 s / 500 | Parameter driver, not electrical waveform |
| Transformer | 10 MVA, 66/0.64/0.64 kV | Three windings, not campus transformers |
| Xl12, Xl13, Xl23 | .095308709, .095308709, .008 pu | Pairwise leakage inputs |
| CuL12, CuL13, CuL23 | .00575, .00575, .00001 pu | Saved winding loss inputs |
| NLL | .00084 pu | Saved no-load loss input |
| Tdc, Xair, Im1, Xknee | .69 s, .275 pu, 1%, 1.25 pu | Match Fig.6 |
| RFlux1–3 | start 0, inc .1, end .5, N=10 each | Arithmetic grid has six points; verify active mode and actual values |
| ClosingTime | start .5, inc .002, end .517, N=10 | Endpoint not on step grid; verify mode and actual values |
| Seed | automatic setting in screenshot, stored 23309 | Do not assume deterministic schedule |
| Slave Mruns | 10 | Not proof of actual number of executed cases |
## Qualification proposal
First open a private copy in installed PSCAD, record edition/version/compiler and any conversion notices, inspect actual run mode and exported parameter schedule, run one base case if permitted. If multi-case support is unavailable, construct single-case manual sweep without bypassing licence limits. Record measured phase current and flux, peak, sampling and timestep. Compare 10/5/2.5 us integration and refine sample interval to avoid underestimating peak. The reported .69 s decay input exceeds post-closure simulation duration; extend horizon for decay analysis. At 60 Hz, 2 ms = 43.2 electrical degrees; at 50 Hz = 36 degrees. Original source at 60 Hz must be preserved for reproduction before a new 50 Hz case. Obtain magnetic data and confirm physical residual-flux combinations; do not use independent arbitrary core flux values as actual measured remanence. The PDF has no quantitative output target; native reproduction plus separate analytical RL/flux checks are needed. No commercial execution or licence qualification claimed. No vendor files or screenshots committed.
