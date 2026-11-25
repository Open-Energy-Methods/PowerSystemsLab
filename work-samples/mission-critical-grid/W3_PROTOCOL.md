# W3 — Single-component outage screen protocol v0.1

Scope: 41 candidate single losses (2 utility sources, 2 HV/MV transformers, 2 MV bus sections, 32 MV feeders, 2 detailed LV transformers, 1 normally open coupler). No HV cable or LV breaker, UPS, standby generator, common-cause or double-fault coverage. Model has no generator; no backup credit. Initial unavailable state, isolated state, restored capacity state. Each state calculated as a balanced load flow of the reachable network; de-energised demand explicitly removed and counted. Fault-on conditions and switching timings are not simulated.

For each block, each normal path is assigned 50% IT/cooling/auxiliary demand. Restored state allocates all block demand to available paths, equal sharing where two reachable. This assumes hypothetical load transfer for all components, not measured or assured service continuity. Source outages disconnect associated HV/MV transformer before tie closure. MV bus failure keeps tie open. Non-source failures cannot trigger tie closure. The source independence assumption remains unverified.

## Predeclared checks
- Exactly 41 unique losses and 3 states each plus normal baseline.
- Source and HV transformer losses initially interrupt 12 MW IT capacity; MV section losses likewise. Feeder or detailed LV transformer loss interrupts 0.75 MW; coupler loss interrupts 0.
- No restored state may energise failed equipment, close tie for a failed MV section or retain two connected sources with a closed tie.
- Restored IT demand expected to be fully assignable for these cases by assumed transfer; if not, explicitly flag; no assertion that a physical design is resilient.
- Active and reactive power balance abs residual <= 1e-6 MW/Mvar; finite voltage on energised buses; solver convergence. Record disconnected demand independent of solver's load results.
- Assumed screening limits: 0.95–1.05 pu on energised buses; transformer and feeder utilisation <=100%. Record breaches, never force success. 90% transformer design target separately flagged. These are study thresholds, not code compliance.
- A successful run verifies workflow execution and basic invariants only. W1–W3 remain open pending engineering review, equipment validation and coverage of actual devices.
