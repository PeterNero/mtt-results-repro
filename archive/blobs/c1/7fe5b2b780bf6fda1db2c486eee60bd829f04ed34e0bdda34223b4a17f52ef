---
title: Selected Central-Circle Damping Identification Lemma
author:
- Peter Nero
date: May 2026
---

# Result

The remaining central-circle damping lemma closes under one precise
identification premise:

```text
the damping Hessian on the selected central-circle branch is the normalized
Z64 central-circle tower block.
```

This is a real advance, but not yet an unconditional prediction of `G_N`.

# Lemma

The branch needed:

```text
sigma_circle * sqrt(log(C_Q/epsilon_adm)/lambda_*) <= 2.
```

Equivalently:

```text
lambda_* >= sigma_circle^2 log(C_Q/epsilon_adm)/4.
```

Theta I supplies the geometric admissibility bound:

```text
R1 <= 2.
```

# Corpus Input

The Z64 operator-identification paper gives, on the exact-order-64
central-circle tower sector:

```text
L_fl,MTT | H_64 = alpha L_tower + E,
lambda_* = 15 alpha,
lambda_next = 24 alpha,
Delta = 9 alpha.
```

It also states:

```text
In normalized tower units one sets alpha=1.
```

Thus the selected normalized tower value is:

```text
lambda_* = 15.
```

# Executable Test

With `C_Q=1`, `sigma_circle=1`, and `epsilon_adm=1/N`:

| N | R1 with lambda*=1 | R1 with lambda*=15 | required alpha |
|---|---:|---:|---:|
| 64 | 2.039333980337618 | 0.5265537695468319 | 0.06931471805599453 |
| 79 | 2.090322427872557 | 0.5397189300902845 | 0.07282413087445036 |
| 448 | 2.470787978037571 | 0.6379547127299338 | 0.10174655387358307 |

So the old `lambda_*=1` sanity branch failed mildly, while the normalized
Z64 tower branch closes the `R1 <= 2` inequality with room to spare.

# What Is Closed

The damping lemma is no longer the hard obstruction.  If the selected damping
Hessian is the Z64 central-circle tower Hessian in normalized tower units, then:

```text
R1 = sqrt(log(N)/15) <= 2
```

for the tested finite branches `N=64`, `N=79`, and `N=448`.

# What Remains

Two things still cannot be skipped:

```text
1. prove the damping Hessian block is the Z64 central-circle tower block;
2. supply the physical action-normalization certificate for G10 and alpha.
```

After those two gates, Theta IV can use:

```text
1/G_N ~= 31.8 R1^3/G10.
```

# Forbidden Shortcuts

This result must not be turned into a numerical constant by:

```text
choosing alpha from observed G_N,
choosing sigma_circle from M_Pl,
choosing epsilon_adm after comparing to H0 or rho_DE,
using R1 as a physical prediction before the Hessian-identification premise.
```
