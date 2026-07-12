# Selected Rho-UV Response-Ratio Computation Attempt v1

## Purpose

This note attempts to compute the remaining superset ratio

```text
rho_UV = C_UV^2 / delta
```

from selected response data. It records the strongest calculation the present
corpus supports and identifies the exact missing numeric input.

## Closed Source Data

The selected Iwasawa curvature source is closed:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
alpha_2 component = 0,
alpha_3 component = 0.
```

Thus the selected UV response row has support only on the `alpha_1` direction.
In the invariant `(2,2)` basis

```text
(alpha_1, alpha_2, alpha_3),
```

the source-certified row is

```text
U_raw = (v1_tilde, 0, 0).
```

For the symmetric Iwasawa slice `r1=r2=R`, this becomes

```text
v1_tilde = 8 r3^2/R^4.
```

The heterotic anomaly solution gives

```text
r3^2 = 8(2pi)^2 / (16/alpha' + 8/R^4).
```

In internal `alpha'=1` units,

```text
r3^2 = 8(2pi)^2 / (16 + 8/R^4),
v1_tilde(R) = 64(2pi)^2 / (16 R^4 + 8).
```

This is a genuine source-certified computation.

## Norm Formula

Let `G_alpha` be the selected inner-product Gram matrix on the invariant
`(2,2)` response rows. Then

```text
||U_raw||^2 = U_raw^T G_alpha U_raw
            = G_11 v1_tilde^2.
```

If the invariant basis is orthonormalized before taking the response norm, then

```text
G_11 = 1,
||U_raw||^2 = v1_tilde^2.
```

But the current corpus does not state that this orthonormalization is the
selected response-row inner product for `rho_UV`. Therefore `G_11` must be
kept explicit unless a future certificate fixes it.

## Disturbance Row

The OU source gives

```text
Var(a) = delta/(2 gamma).
```

The white-noise paper proves that `delta` is the integrated covariance of a
finite-memory disturbance in the white-noise limit. It does not compute the
selected finite-memory covariance row from the Z64/Strominger carrier.

Let the selected disturbance covariance row be `D_raw`, evaluated in the same
response inner product. Then the desired ratio is

```text
rho_UV = ||U_raw||^2 / ||D_raw||^2.
```

With the closed UV row this becomes

```text
rho_UV = G_11 v1_tilde^2 / ||D_raw||^2.
```

On the symmetric Iwasawa slice in internal `alpha'=1` units,

```text
rho_UV(R) =
  G_11 [64(2pi)^2 / (16 R^4 + 8)]^2 / ||D_raw||^2.
```

If, and only if, a future certificate selects both:

```text
G_11 = 1,
||D_raw||^2 = 1,
```

then

```text
rho_UV(R) = [64(2pi)^2 / (16 R^4 + 8)]^2.
```

This is a demonstration specialization, not a current no-knob prediction.

## Evaluated Demonstration Values

Under the non-certified demonstration specialization `G_11=1` and
`||D_raw||^2=1`:

| R | r3 | v1_tilde | rho_UV | s_* |
|---:|---:|---:|---:|---:|
| 1 | 3.627598728468436 | 105.275780278286 | 11082.9899132021 | 9.34260594395577 |
| 2 | 4.375048680836414 | 9.57052547984423 | 91.5949579603476 | 4.20084963151094 |
| 5 | 4.441106850564644 | 0.252459904744092 | 0.0637360035033962 | 1.25051626958438 |

These numbers are useful diagnostics only. They are not physical predictions
because `G_11` and `||D_raw||^2` are not source-certified.

## Why The Numeric Closure Still Fails

The current corpus does not supply:

```text
1. the selected response-row inner product G_alpha;
2. the selected finite-memory disturbance covariance row D_raw;
3. a fluctuation-dissipation theorem tying D_raw to the same Hessian/retarded
   kernel normalization used for the UV row.
```

The C1 response extraction attempt confirms the same obstruction: the alpha_1
curvature driver row is closed, but selected primitive contractions and operator
responses remain absent.

## Verdict

The requested computation closes to the following source-certified formula:

```text
rho_UV =
  G_11 [64(2pi)^2 / (16 R^4 + 8)]^2 / ||D_raw||^2
```

on the symmetric Iwasawa branch in internal `alpha'=1` units.

It does not close to a unique number from the present corpus.

The next strictly necessary data are:

```text
G_11,
||D_raw||^2,
or a theorem forcing G_11/||D_raw||^2.
```

Any numeric value for `rho_UV` before those are supplied would be an additional
normalization assumption.
