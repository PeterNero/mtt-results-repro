# MTT Selected HYM Gauge-Fixed Connection Representative or Galerkin Solve v1

## Claim

The next object is now specified as an executable solve gate.  Abstract HYM
existence is already imported, but the branch still lacks either:

1. an analytic selected gauge-fixed HYM representative `A_HYM`, or
2. a finite Newton/Galerkin coefficient vector with residual, coercivity, and
   truncation certificates.

No selected finite operator values are promoted in this artifact.

## Straight Path

The straight proof path is rank-2:

```text
selected V_alpha
+ selected equal-radius Gauduchon metric
+ gauge-fixed rank-2 HYM solve
=> selected A_HYM
=> selected rho_E / metric / D_E / Green / dotD / C1 payload
```

The gauge conditions are unitary convention, determinant normalization, and a
Coulomb slice modulo infinitesimal unitary gauge.  The residual equations are
the holomorphic-structure condition, primitive trace-free HYM equation, gauge
slice equation, metric compatibility, and Green-Schwarz/Bianchi consistency
row.

## Superset Support

The combined support path uses the Route-C/Strominger Galerkin spec, the smooth
`B_N` scaffold, and the finite `D_E` scaffold as execution infrastructure.  It
does not use those smoke/scaffold matrices as selected values.

The important type issue is now explicit: the HYM source is rank-2 `V_alpha`,
whereas the available 27-mode execution scaffold is rank-3 qutrit/family-sector
data.  A theorem-derived rank-2-to-sector transfer functor, or a proof that the
selected solve can be run directly in sector form, is required before promotion.

## First Attempt

The first solve attempt is executed at the proof-contract level and stops before
numeric values.  Existing artifacts contain no selected `A_HYM`, no selected
Newton coefficient vector, no selected residual values, and no selected
rank-2-to-sector transfer map.

## Next Artifact

`MTT_Selected_HYM_NewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1`.
