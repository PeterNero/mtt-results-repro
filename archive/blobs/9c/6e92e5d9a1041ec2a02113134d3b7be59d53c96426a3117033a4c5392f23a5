---
title: Damping Hessian Z64 Block Identification
author:
- Peter Nero
date: May 2026
---

# Result

The previous premise:

```text
the damping Hessian block is the Z64 central-circle tower block
```

is now certified for the selected exact central-circle branch.

This does not derive the exact branch from the full mixed MTT Hessian.  It says
that once the exact central-circle branch is the branch under study, the
Hessian block and retarded kernel are already explicit in the Z64 corpus.

# Exact Branch Data

The Z64 exact central-circle certificate supplies:

```text
K_64 = C[coker A_64] ~= C[Z_64],
S e_j = e_{j+1 mod 64},
K_ret,64 = S^-1 = S^63,
L_64 = alpha L_tower,
alpha > 0.
```

In normalized certificate units:

```text
alpha = 1.
```

The tower operator is:

```text
L_tower |d> = C(d)|d>,
C(d)=sum_i(d_i^2-1).
```

The selected tower is:

```text
d_*=(2,2,2,2,2),
C(d_*)=15.
```

The next cost is:

```text
24.
```

So:

```text
lambda_* = 15 alpha,
Delta = 9 alpha.
```

# Schur Leakage

In the exact coherent block:

```text
P_CP,64 <= Pi_coh,
[L,Pi_coh]=0.
```

Therefore:

```text
P_fl L Q = 0,
Q L P_fl = 0,
C_fl = 0,
E_Schur = 0.
```

This means there is no residual Schur correction to the exact Z64 damping block.

# Damping Consequence

The selected normalized damping value is:

```text
lambda_* = 15.
```

Thus:

```text
R1 = sqrt(log(C_Q/epsilon_adm)/15)
```

for `sigma_circle=1` in normalized exact-branch units.

With `C_Q=1` and `epsilon_adm=1/N`:

| N | R1 |
|---|---:|
| 64 | 0.5265537695468319 |
| 79 | 0.5397189300902845 |
| 448 | 0.6379547127299338 |

All close the Theta I bound:

```text
R1 <= 2.
```

# What This Closes

```text
exact-branch Hessian block       CLOSED
exact-branch retarded kernel     CLOSED
Schur correction in exact branch CLOSED
central-circle damping bound     CLOSED in normalized exact-branch units
```

# What Remains

Only the physical normalization gate remains for non-SM absolute constants:

```text
physical action-normalization certificate for G10 and alpha.
```

The stronger robustness project remains open:

```text
derive the exact central-circle branch from the full unprojected mixed MTT
Hessian without selecting the exact branch first.
```

That is useful, but it is not the same as the exact-branch proof spine.

# Forbidden Shortcut

Do not choose `alpha`, `G10`, or a unit conversion from observed `G_N`, `M_Pl`,
`H0`, `rho_DE`, or absolute axion scales.
