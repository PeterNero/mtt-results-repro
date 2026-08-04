# Exact Circle/Sphere Zeta Pieces v1

## Purpose

This note upgrades the determinant program from fitted cutoff diagnostics to
exact zeta formulas wherever the current selected scaffold gives an exact
scalar-proxy spectrum.

The closed pieces are:

```text
U1  -> circle scalar Laplacian,
SU2 -> effective round S2/lens scalar Laplacian.
```

The `SU3` Nil determinant remains open.

## U1 Circle

For the circle sector:

```text
lambda_n = n^2/R1^2,
m_n = 2,
n >= 1.
```

The spectral zeta function is:

```text
zeta_U1(s) = 2 R1^(2s) zeta_R(2s).
```

Therefore:

```text
p_U1 = -zeta_U1'(0) = 2 log(2 pi R1).
```

## SU2 Effective Sphere

For the effective round sphere/lens sector:

```text
lambda_l = l(l+1)/A,
m_l = 2l+1,
A = (f2 R_lens)^2 = 0.280 R1.
```

Let:

```text
S(s) = sum_{l>=1} (2l+1) [l(l+1)]^(-s).
```

Then:

```text
S(0) = -2/3,
-S'(0) = -4 zeta_R'(-1).
```

Scaling by `A` gives:

```text
p_SU2 = -4 zeta_R'(-1) + (2/3) log(A).
```

Using:

```text
zeta_R'(-1) = 1/12 - log(A_Glaisher).
```

this is fully computable without target data.

## Selected q79 Values

For the selected q79 scaffold:

```text
R1 = 0.5397189300902845,
A = 0.280 R1.
```

The calculator:

```text
scripts/compute_exact_circle_sphere_zeta.py
```

reports:

```text
p_U1,
p_SU2,
p_U1 - p_SU2.
```

## Verdict

This closes the analytic scalar-proxy determinant for `U1` and `SU2`.

It does not close full electroweak C1 because the remaining determinant must be
computed for:

```text
SU3 Nil / selected gauge-threshold operator / topology-certified weights.
```

The next required artifact is:

```text
Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1.
```
