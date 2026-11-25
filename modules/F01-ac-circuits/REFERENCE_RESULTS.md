# F01 — Reference results

Status: preliminary AI-assisted analytical implementation tested locally; learner gate OPEN.

For a 24 V RMS, 50 Hz ideal series RLC circuit, V is the reference phasor and positive Q denotes inductive demand. Z = R + j(2*pi*f*L - 1/(2*pi*f*C)); I = V/Z; S = V*conj(I).

| Quantity | Computed |
|---|---:|
| Z (ohm) | 10 - j22.406210658 |
| I (A) | 0.398645750 + j0.893214065 |
| P (W) | 9.567497997 |
| Q (var) | -21.437137558 |
| apparent power (VA) | 23.475261119 |

The capacitive net reactance and leading current are consistent. An eight-test combined local suite covering F01 and separate campus screening passed; the committed F01 tests reproduce its applicable checks, split into this module. No independent external solver or learner exercise has been completed. This is not physical validation.

Next: learner derives the result without reading the reference, predicts the direction of the phase change at 150 Hz, then checks a variant. Record evidence and numerical tolerances. Do not mark F01 complete solely from this solution.
