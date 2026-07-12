---
title: Selected Damping Normalization Branch
author:
- Peter Nero
date: May 2026
---

# Result

The central-circle damping branch can now be finished as a reduction:

```text
selected MTT/Strominger Hessian
-> damping-selected Lambda_eff
-> central-circle R1
-> Theta IV Newton structure.
```

It is not yet a numerical closure of `G_N`.

# Branch Equations

The fixed-point damping theorem gives:

```text
tau_adm = log(C_Q/epsilon_adm)/lambda_*
Lambda_eff = sqrt(lambda_* / log(C_Q/epsilon_adm)).
```

The central-circle branch asserts:

```text
Lambda_eff^2 = lambda_S1 ~= 1/R1^2
```

up to a declared convention factor `sigma_circle`.  Thus:

```text
R1 = sigma_circle / Lambda_eff.
```

Theta IV then gives:

```text
1/G_N ~= 31.8 R1^3/G10
      ~= 31.8 sigma_circle^3/(G10 Lambda_eff^3).
```

# Naive Finite-Resolution Test

Set, only as a sanity test:

```text
C_Q = 1,
lambda_* = 1,
sigma_circle = 1,
epsilon_adm = 1/N.
```

Then:

| N | Lambda_eff | R1 |
|---|---:|---:|
| 64 | 0.4903561700249054 | 2.039333980337618 |
| 79 | 0.4783950966922162 | 2.090322427872557 |
| 448 | 0.4047291831143895 | 2.470787978037571 |

Theta I contains the admissibility bound:

```text
R1 <= 2.
```

So the naive finite-count choices are close, but do not close the branch under
the unit assumptions above.

# What This Means

We did not fail back into vagueness.  We reduced the branch to one explicit
lemma:

```text
Selected Central-Circle Damping Identification Lemma.
```

It must prove:

```text
sigma_circle * sqrt(log(C_Q/epsilon_adm)/lambda_*) <= 2
```

with equality or a selected interior value fixed from MTT data, not from target
constants.

# Why This Is The Right Remaining Lemma

If this lemma supplies `R1`, then Theta IV already supplies:

```text
Vol(X_int) ~= 31.8 R1^3,
1/G_N ~= 31.8 R1^3/G10.
```

One more independent action-normalization certificate for `G10` would then
close `G_N` without using observed `G_N`.

# Forbidden Shortcuts

The branch must reject:

```text
choosing sigma_circle to force observed G_N,
choosing epsilon_adm from M_Pl,
choosing lambda_* after comparing to H0 or rho_DE,
using observed target constants to select R1 or G10.
```
