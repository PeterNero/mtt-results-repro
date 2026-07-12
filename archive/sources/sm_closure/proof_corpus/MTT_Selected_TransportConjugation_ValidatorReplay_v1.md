# MTT Selected Transport-Conjugation Validator Replay v1

Status: `MTT_SELECTED_TRANSPORT_CONJUGATION_VALIDATOR_REPLAY_CLOSED_DOTD_OPEN`.

## Result

The finite validator is extended by an exact symbolic transport rule:

```text
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
Q_s^sel = U Q_s^model U^-1
U = exp(-u ad(T3))
```

This closes the selected projector/Riesz/Green/source replay without requiring
the raw 27-mode `B_N` Fourier truncation to be closed under multiplication by
`exp(+-u ad(T3))`.  The raw replay residual remains diagnostic only:

```text
direct truncated residual = 0.23373530261576297
gauge-frame residual      = 8.863447760090952e-16
```

The accepted replay is symbolic and exact: it conjugates already-validated
model-active finite identities through the selected unitary transport.

## What This Closes

- symbolic transport-conjugation validator extension,
- finite selected projector/Riesz/Green replay in the transported frame,
- selected source verification for the stationary zero-mode/projector packet,
- validator-ready `rho_s` sector packet.

## Boundary

This does not close `dotD_alpha1`.  Differentiating the transported packet
introduces the extra transport-derivative term

```text
d/dalpha (U rho U^-1)
```

so the next artifact must supply `dU/dalpha` and the selected alpha1 driver
from the same branch.

No measured constants, benchmark targets, or lifted selected flags are used.

Next artifact: `MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1`.
