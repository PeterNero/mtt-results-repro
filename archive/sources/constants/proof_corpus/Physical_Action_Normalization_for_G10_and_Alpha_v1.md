# Physical Action Normalization for G10 and Alpha v1

## Purpose

This gate closes the remaining action-normalization premise in the exact
central-circle damping branch by separating two statements that must not be
conflated:

1. the canonical internal action normalization of the selected MTT branch;
2. a physical SI normalization for dimensionful constants such as `G_N`.

The first is now certified. The second is not derivable from the present corpus
without an independent dimensional anchor, and treating it as a prediction would
be a target-value backsolve.

## Inputs

The exact Z64 central-circle branch gives

```text
L_64 = alpha L_tower,
K_ret,64 = S^-1,
E_Schur = 0,
lambda_* = 15 alpha.
```

The branch certificate already uses normalized tower units

```text
alpha = 1,
lambda_* = 15.
```

This closes the dimensionless damping inequality and fixes the branch-scale
Hessian block in internal units.

The 10D-to-4D GR derivation supplies the action dictionary

```text
S_grav^(4) = V_int/(16 pi Gcal) int R(g) sqrt(-g) d^4x + ...
G_eff = Gcal / V_int.
```

Theta IV supplies the structural internal-volume relation

```text
Vol(X_int) ~= 31.8 R1^3,
1/G_N ~= 31.8 R1^3 / G_10,
```

and explicitly says that the result does not compute `G_10`.

## Lemma

In the selected exact branch, the canonical internal action normalization is

```text
alpha_int = 1,
G10_int = 1.
```

This is a unit choice for the branch action functional. It is sufficient to
compute the dimensionless internal 4D gravitational coefficient

```text
G_eff,int = G10_int / Vol(X_int) = 1 / (31.8 R1^3).
```

For the finite branches tested by the damping certificate,

```text
R1(N) = sqrt(log N / 15).
```

Therefore

```text
Vol_int(N) = 31.8 (log N / 15)^(3/2),
G_eff,int(N) = 1 / Vol_int(N).
```

## Evaluated Branches

| N | R1 | Vol_int | G_eff,int |
|---:|---:|---:|---:|
| 64 | 0.5265537695468319 | 4.642536197052882 | 0.21539950526068224 |
| 79 | 0.5397189300902845 | 4.999540286439839 | 0.20001839023325438 |
| 448 | 0.6379547127299338 | 8.256513019265205 | 0.12111650495392737 |

These are internal-unit outputs of the selected exact branch, not measured SI
values.

## No-Go Clause for Physical Absolutes

No current corpus object selects a physical value of `G10`, `alpha'`, a string
length, a Planck length, or an SI conversion scale independently of the target
dimensionful observable.

Consequently the following claims remain forbidden:

```text
G_N predicted by choosing G10 from observed G_N,
M_Pl predicted by choosing the conversion scale from observed M_Pl,
absolute f_a predicted by choosing the scale from an axion benchmark,
H0 or rho_DE predicted by tuning the late-time normalization.
```

The corpus can currently claim the exact branch structure, dimensionless ratios,
dimensionless bounds, and canonical internal action coefficients. It cannot
claim absolute physical dimensionful constants until a new selected dimensional
anchor is supplied.

## Verdict

The remaining gate is closed in the only rigorous no-knob sense available:

```text
canonical internal action normalization: CLOSED
physical absolute action normalization: NO-GO WITHOUT NEW DIMENSIONAL ANCHOR
```

This strengthens the program because it prevents a hidden fit from masquerading
as a prediction.
