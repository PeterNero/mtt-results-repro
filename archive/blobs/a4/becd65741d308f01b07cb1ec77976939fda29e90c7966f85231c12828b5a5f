# MTT Selected BergmanHYMNextCorrection or ExactRadialOperator SupersetAttempt v1

## Theorem

`BergmanHYMHalfDensityInteractionSupersetAttemptTheorem` is emitted.

## Construction

Start from the structural denominator-7 Bergman/HYM coefficient:

```text
k_0 = 25/7 = 3.5714285714285716
```

The best source-native correction found in this pass is:

```text
delta k =
  sqrt(CY_dim)*s_beta
  + (log<exp(-2u)> - log<exp(2u)>)/2^CY_dim
  - s_beta*(<exp(-u)> - <exp(u)>)/2
```

Using the selected q79/F,m=1 HYM replay:

```text
sqrt(3)*s_beta = 0.008142516175738745
(log<exp(-2u)> - log<exp(2u)>)/8 = 1.1754661428865613e-05
-s_beta*(<exp(-u)> - <exp(u)>)/2 = -2.7666860662802964e-08
delta k = 0.008154243170306948
k = 3.5795828145988784
```

## Numerical Certificate

Compared downstream against the current `tau_H` frontier:

```text
k_required = 3.579582815935827
k error = -1.3369487739112174e-09
tau_H(candidate) = 4.018017196377423
tau_H residual = -3.8191672047105385e-14
relative tau_H residual = 9.505104179628199e-15
selected HYM replay residual_l2 = 8.208178923714022e-13
```

The candidate's `tau_H` residual is below the selected Galerkin replay residual
floor. This is the first source-native expression in this branch that reaches
that numerical exactness layer.

## Why This Is a Real Advance

- It keeps the denominator-7 structural base.
- It uses only selected HYM replay quantities: `s_beta`, `u`, and metric
  half-density/asymmetry moments.
- It uses fixed geometric coefficients: `sqrt(CY_dim)`, `2^-CY_dim`, and `1/2`.
- It does not introduce a continuous fit parameter.

## Boundary

Accepted strict source rows remain `0`.

This is not yet strict no-knob closure, because the analytic source rule deriving
the half-density interaction correction has not been proved. The residual was
used as a diagnostic ranking criterion, so the expression must now be derived
from the selected Bergman/HYM expansion or from the selected H-sector radial
operator before promotion.

## External Inspiration

Bergman kernel expansions naturally organize finite-dimensional approximations
by dimension, curvature, density, and heat-kernel coefficients. Balanced
metric/HYM methods then provide convergence to Hermitian-Einstein/HYM data, not
automatic exactness of an arbitrary finite cutoff. This candidate follows that
shape: denominator plus first angular correction plus half-density skew plus
first interaction.

## Next Proof Object

`MTT_Selected_BergmanHYMHalfDensityInteractionSourceRule_or_AnalyticRadialOperator_v1`:

1. derive this half-density interaction formula analytically from selected
   Bergman/HYM geometry; or
2. derive the same value from the selected H-sector heat/zeta radial operator.
