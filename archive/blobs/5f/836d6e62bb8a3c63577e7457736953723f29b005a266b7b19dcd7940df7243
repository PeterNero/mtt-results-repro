# Selected PhiFin S1 RhoE Trace Fill v1

## Result

The S1 `rho_E` trace is partially filled by importing the verified
Heisenberg/Weyl projective finite trace from the GR/protospinor repo.

Status: `SELECTED_PHIFIN_S1_RHOE_TRACE_PARTIAL_FILL_DONE_S2_OPEN`

This replaces the old identity-smoke `rho_E` shortcut for the S1 trace only.
It does not emit the full selected `Phi_fin` payload and does not set selected
source flags true.

## Imported Trace

```text
rho_E(g1) rho_E(g2) = omega^-1 rho_E(g2) rho_E(g1)
g1^3 = g2^3 = I
g3,...,g6 act trivially in the inactive kernel
```

Numeric checks:

```text
g1 unitary residual = 1.0745712787231757e-12
g2 unitary residual = 0.0
g1 order-3 residual = 1.861205938488148e-12
g2 order-3 residual = 0.0
projective commutator residual = 7.59783576575733e-13
```

## Remaining Open

- S2 selected basis/quadrature
- S2 selected `D_E`, `dotD_alpha1`, Riesz projector, reduced Green entries
- positive gap/error certificate
- honest Route-C validator replay
- `A_selected` and `b_selected`
