# MTT Selected Nonlinear HYM Correction Coefficient Solve v1

## Result

The first trace-free HYM correction source is now computed from the unit Ext row:

```text
rho = |eta_00^unit|^2
mean(rho) = 0.9999999999999997
f = rho - 1
```

The zero-mean Coulomb scalar equation

```text
Delta phi = f,    mean(phi)=0
```

is solved by periodic FFT/Galerkin inversion on a `24^4` grid. The residual is:

```text
||Delta phi - f||_L2 = 5.588e-16
```

The first trace-free End0 correction is:

```text
S_1 = phi * T3
```

up to the global sign convention of the HYM linearization.

## What This Closes

This closes the first selected trace-free density correction and identifies the
`T3` diagonal End0 direction forced by the off-diagonal unit Ext row.

## Guardrail

This is not yet the full nonlinear HYM connection. The full theorem still needs
the `exp(S)` Newton replay with quadratic curvature terms, a coercive Jacobian
bound, a truncation certificate, and validator-ready finite operator payloads.

## Next Artifact

`MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1`.
