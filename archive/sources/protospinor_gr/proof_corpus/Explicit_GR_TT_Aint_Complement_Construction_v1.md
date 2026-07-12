# Explicit GR TT Aint Complement Construction v1

## Result

The direct GR TT complement can now be written as a formal selected-family
operator:

```text
A_GR,TT(eta_TT) = eta_TT I_2
```

on the closed TT quotient `span{TT_plus, TT_cross}`.

This follows from the already-closed quotient and transverse-plane covariance:
after gauge, trace, and longitudinal directions are removed, a parity-even
quadratic leakage/complement operator must be scalar on plus/cross.

## Three Normalizations

The construction exposes exactly where the remaining ambiguity lives.

```text
closure-metric normalized:   eta_TT = 1
action-Hessian normalized:   eta_TT = kappa_STF,int
branch-window normalized:    eta_TT = c_window kappa_STF,int
```

The first is a formal quotient normalization. The second is the response-action
normalization. The third is the possible `A_int` spectral convention, but only
if the selected projector/window derives `c_window`.

## Boundary

This does not yet close the GR TT modal gap. It closes the shape of the distinct
GR TT complement, not the selected normalization of its eigenvalue.

The next theorem is:

```text
Selected_GR_TT_Eta_Normalization_Theorem
```

It must derive `eta_TT` in the same convention as `lambda_*`.
