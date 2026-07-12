# Selected Gauge-Factor Zeta Finite-Part Candidate v1

## Purpose

The spectral-table candidate produces cutoff determinant sums.  Those sums are
not determinant finite parts until a regularization prescription is supplied.

This note implements the first explicit regularization candidate:

```text
scripts/estimate_selected_zeta_finite_part.py
```

It fits the cutoff determinant sequence to a heat-kernel-style asymptotic
basis and reports the constant term.

## Subtraction Basis

The diagnostic subtraction basis is:

```text
K^2 log K,
K^2,
K log K,
K,
log K,
constant.
```

The constant term is interpreted as the finite-part candidate.

## Status

This is not yet a final zeta determinant theorem.  It depends on:

```text
1. the scalar proxy operator profile;
2. the Nil p != 0 lower-proxy spectrum;
3. unit diagnostic weights;
4. a fitted asymptotic basis rather than an analytic heat-kernel proof.
```

## What It Achieves

The pipeline now contains every computational stage:

```text
selected scaffold
-> generated gauge-factor spectral table
-> cutoff determinant responses
-> finite-part estimator
-> electroweak C1 response interface.
```

The remaining upgrade is mathematical, not structural:

```text
Exact_Selected_Gauge_Threshold_Operator_and_Zeta_Determinant_v1.
```

That artifact must replace the proxy spectra and fitted subtraction basis by
the exact selected threshold operator, exact spectrum or heat coefficients, and
topology-certified weights.
