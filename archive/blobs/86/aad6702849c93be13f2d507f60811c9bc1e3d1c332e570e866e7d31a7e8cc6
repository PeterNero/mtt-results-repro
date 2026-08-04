# MTT Selected FiniteCutoffExactnessRoutes or ProjectedSourcePrinciple v1

## Theorem

`FiniteCutoffExactnessRouteClassificationTheorem` is emitted.

## Result

Automatic finite-cutoff exactness is possible, but not by ordinary continuum
magic.

The current HYM replay uses nonlinear terms such as `exp(u)` and `exp(-2u)`.
Those are not proved continuum-bandlimited. Therefore ordinary Fourier/trapezoid
quadrature exactness does not make the continuum calculation exact at finite
cutoff.

The viable route is:

```text
FiniteProjectedHYMSourcePrinciple
```

For the selected q79/F,m=1 H-sector branch, MTT must select the finite projected
algebra `A_N` itself as the source object:

```text
a star_N b := P_N(a b)
exp_N(u) := P_N(exp(u)) or the equivalent finite algebra exponential
Tr_N := normalized finite trace
Delta_N, Green_N := finite projected operators
```

Then the cutoff computation is exact because it is an identity inside the
selected finite source algebra, not an approximation to an unprojected continuum
geometry.

## Current Classification

```text
mesh = 24
theta_series_cutoff = 12
grid points = 331776
half-density tau_H residual = -3.8191672047105385e-14
selected HYM replay residual floor = 8.208178923714022e-13
```

The half-density candidate already sits below the selected replay floor. To make
that automatic exactness, the remaining proof must show that the finite projected
algebra is selected by MTT and that the half-density interaction formula is a
source identity in that algebra.

## Routes

- Continuum trigonometric exactness: blocked unless all integrands are proved
  bandlimited or replaced by projected finite operations.
- Gaussian/quadrature exactness: not the current periodic/Fourier setup.
- Homogeneous/fuzzy Bergman exactness: blocked by nonconstant `u` unless we
  replace the replay with a selected homogeneous finite matrix geometry.
- Localization/residue exactness: possible but no fixed-point formula is emitted.
- Finite projected source exactness: selected as the best route.

## Next Proof Object

`MTT_Selected_FiniteProjectedHYMSourcePrinciple_or_BandlimitExactnessProof_v1` must either prove the finite projected HYM source principle or prove a
true bandlimit/homogeneous/localization exactness theorem for the same H scalar.
