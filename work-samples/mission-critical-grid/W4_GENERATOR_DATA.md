# W4/W5 — Representative generator data and model-form limitation

Source: STAMFORD S7L1D-J4, winding 312, document ESA062L874 rev E, 01 April 2024, [manufacturer PDF](https://www.stamford-avk.com/sites/stamfordavk/files/ESA062L874_S7L1D-J4-E-W312.pdf), printed pp. 2, 3 and 6, visually checked. Representative 400 V / 50 Hz alternator, 2500 kVA Class H reactance base. Not the campus 3125 kVA generator and not a selected engine-generator set.

| Parameter | Value | Page |
|---|---:|---:|
| Saturated Xd (pu) | 2.36 | 2 |
| Saturated X'd (pu) | 0.16 | 2 |
| Saturated X''d (pu) | 0.12 | 2 |
| Saturated X2 (pu) | 0.15 | 2 |
| Saturated X0 (pu) | 0.03 | 2 |
| T'd (s) | 0.164 | 3 |
| T''d (s) | 0.008 | 3 |
| Ta (s) | 0.037 | 3 |
| Separately excited 50 Hz sustained three-phase current (A) | 11142 | 6 |

Fixed-field, no-load, resistance-neglected terminal bolted-fault approximation:
Ipu(t)=1/Xd+(1/X'd-1/Xd)exp(-t/T'd)+(1/X''d-1/X'd)exp(-t/T''d).
This is an illustrative model-form comparison, not a vendor performance prediction. Base current 3608.439 A. Approximate initial RMS symmetrical current 30.070 kA. Fixed-field asymptote 1.529 kA; published separately excited sustained current 11.142 kA. Do not equate them. The manufacturer's 50 Hz curve exhibits current recovery as the excitation system responds, and its pre-minimum 400 V correction is 1.05 relative to the plotted base. The sustained number does not take that correction. No curve was digitised or fitted.

The difference is a model-form limitation, not a failed calibration of the datasheet. Use the manufacturer curve/qualified excitation model for sensitivity in a selected genset; distinguish initial symmetrical, peak, breaking and thermal duties. Need a 400 V 50 Hz machine matching the final generator rating, engine ratings and AVR response. A 3125 kVA entry at 60 Hz or different voltage is not equivalent. No actual campus generator duty or settings claim.

Python arithmetic was independently executed in the assistant runtime; no native generator simulation or vendor validation.
