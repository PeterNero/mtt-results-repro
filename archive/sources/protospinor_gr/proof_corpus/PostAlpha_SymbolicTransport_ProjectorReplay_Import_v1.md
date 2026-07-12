# PostAlpha SymbolicTransport ProjectorReplay Import v1

## Result

Stationary selected projector/Riesz/Green replay is now closed by exact symbolic
transport conjugation:

```text
accepted replay = exact_symbolic_transport_conjugation
accepted transport = U=exp(-u ad(T3))
selected rho_s validator-ready = true
projector/Riesz/Green replay = true
```

This does not assert that the raw finite 27-mode Fourier basis is closed under
transport. The recorded raw T1/T2 residual remains
`0.23373530261576297`.

The boundary is sharp: differentiating the transport introduces `dU/dalpha`,
so `dotD_alpha1` needs the selected transport derivative and alpha1 driver.

Status:

```text
POST_ALPHA_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN
```

Next:

```text
Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1
```
