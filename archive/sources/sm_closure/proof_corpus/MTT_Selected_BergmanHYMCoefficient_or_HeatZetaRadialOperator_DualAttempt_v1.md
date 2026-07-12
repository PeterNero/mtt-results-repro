# MTT Selected BergmanHYMCoefficient or HeatZetaRadialOperator DualAttempt v1

## Theorem

`BergmanHYMCoefficientAndHeatZetaDualAttemptTheorem` is emitted.

## Bergman/HYM Route

The structured finite-window candidate is:

```text
k_B = (2*theta_series_cutoff + 1)/(CY_dim + End0_rank + trace_unit)
    = 25/(3+3+1)
    = 3.5714285714285716
```

It gives:

```text
tau_H(k_B) = 4.018016964859304
relative residual = 5.76200016622163e-08
```

This recovers the sharp `25/7` near-miss from a Bergman/HYM-shaped source
window. It is not promoted, because the denominator and exactness theorem are
not yet emitted.

## Heat/Zeta Route

The flat theta-window Laplace proxy gives best simple transform:

```text
4 = 4.0
tau_H = 4.018029141075982
relative residual = 2.972784320514677e-06
```

This is weaker and is not the selected H-weighted H-sector threshold operator.

## Decision

Accepted source rows: `0`.

The next best target is `MTT_Selected_BergmanHYMCoefficientSourceRule_or_ExactRadialOperator_v1`:

1. prove the Bergman/HYM denominator and exactness/error certificate, or
2. emit `tau_H`/`r_H` directly from a selected H-sector heat/zeta radial operator.
