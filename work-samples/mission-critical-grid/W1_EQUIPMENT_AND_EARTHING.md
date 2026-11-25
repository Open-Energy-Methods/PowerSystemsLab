# W1 — Equipment, grounding and switching design decisions

Status: preliminary engineering choices, not approved specifications. The balanced v0.1 model remains unchanged; vector groups, sequence parameters, fault-duty and ground-fault calculations are NOT enabled by this note.

## Candidate arrangements
- HV/MV: consider YNd11 with HV neutral connected according to utility requirements, and MV delta with a separately designed zigzag grounding transformer and neutral resistor per section. The actual utility neutral practice, earth-fault current target, grounding transformer ratings, zero-sequence impedance and thermal duty are open. A delta alone does not provide an MV neutral; do not silently assume a grounded source. Compare alternative YNyn arrangements with appropriate tertiary and earthing analysis.
- MV/LV: candidate Dyn11 with TN-S LV distribution, distinct neutral and PE downstream of the defined neutral-earth connection. Generator neutral arrangement and transfer-pole policy require detailed design; do not infer a safe neutral bonding scheme from the balanced model.
- Both parallel-capable transformer paths require compatible voltage ratio, impedance, vector group and phase sequence. Current study only allows the coupler to close with one incomer isolated, not paralleling utilities.
- Source circuit impedances, transformer load/no-load losses, thermal ratings, cable installation conditions, voltage-drop, cable fault withstand and switchgear Icu/Ics/Icw/Icm remain unqualified. The existing 200 A feeder rating is a placeholder, not a cable selection.
- At 20 kV, 40 MVA nameplate corresponds to 1154.7 A; at 400 V, 2.5 MVA corresponds to 3608.4 A. Nominal currents are not protective-device settings.

## Manufacturer evidence leads
- Schneider Electric [Selectivity, Cascading and Coordination Guide 2026, LVPED318033EN](https://www.se.com/us/en/download/document/LVPED318033EN/): covers MasterPacT MTZ ACB and ComPacT NSX MCCB families. Exact voltage, device, trip unit, curve, tolerance and tested combination must be identified before a selectivity claim.
- Schneider Electric [MasterPacT MTZ2/3 user guide](https://productinfo.se.com/masterpactmtz2-3userguide/doca0101-mtz2-3-user-guide/English/BM_MasterPact%20MTZ2_3_b5effd44_T001601218.xml/%24/TPC_Range_b5effd44_T001601604): candidate frame family only; no equipment selected.
- STAMFORD [S7L1D-J4 winding 312 technical sheet ESA062L874 rev E](https://www.stamford-avk.com/sites/stamfordavk/files/ESA062L874_S7L1D-J4-E-W312.pdf): public reference for a 2500 kVA, 400 V, 50 Hz alternator; this is NOT the 3125 kVA candidate and not a complete engine-generator rating. Extract and verify reactances/time constants and rating bases in the later generator qualification step; do not transplant parameters silently.
- STAMFORD [technical downloads](https://www.stamford-avk.com/downloads): source for identifying a matching alternator.
- UPS: exact model and efficiency curve, recharge limits, bypass topology and current limitation remain open.

These are source leads, not a completed procurement or standards compliance check. Review exact technical documents before extracting parameter values; do not redistribute vendor PDFs without permission.

## Permitted discrete switching rules
1. Normal MV coupler open. Treat all load components as equal A/B split and theoretically transferable, a deliberately optimistic capacity screen; cooling and auxiliary transfer hardware not represented.
2. Source loss: identify dead section; isolate the associated transformer before closing the coupler. Transformer loss: remove failed transformer before closing coupler. Never parallel two live utility paths.
3. MV section loss: isolate section and incident branches; coupler remains open. Transfer affected loads to surviving block path under the optimistic transfer assumption.
4. Block feeder or detailed LV transformer loss: isolate failed path, transfer its half demand to remaining path. No automatic generator credit.
5. Coupler unavailable: leave open; normal supply unaffected. This says nothing about its ability to close during a second failure.
6. Initial state represents unavailable asset, not fault-on transient; isolation and restored states are discrete steady-state abstractions, not operational procedures. No voltage/frequency transfer transients, UPS hold-up, breaker interlocks or service continuity certification.

Remaining W1 gates: real equipment data, vector group/earthing implementation with independently checked sequence network, cable engineering, detailed SLD, UPS/generator/interlock models.
