---
title: Exploratory Absolute Normalization Solution
author:
- Peter Nero
date: May 2026
---

# Result

The strongest current route to absolute normalization is not direct flux
minimization alone.  The viable solution schema is:

```text
selected flux/topology sector
-> Strominger/MTT fixed point and Hessian
-> damping-selected coherence scale
-> physical normalization branch.
```

This is a solution schema, not yet a numerical closure.

# Stage 1: Select the Sector

The Strominger/heterotic corpus supplies an MTT selection functional `Xi`.
In a fixed topological sector, it gives existence of minimizers and, near a
solution satisfying the stated hypotheses, a unique local minimizer.  The MTT
fixed point equals this minimizer.

This is exactly the right source of selected operator data:

```text
A = selected Hessian / linearized damping generator,
P = coherent projector,
Q = I - P.
```

# Stage 2: Select the Damping Scale

The fixed-point damping theorem gives:

```text
tau_adm = lambda_*^{-1} log(C_Q / epsilon_adm).
```

Here:

```text
lambda_* = incoherent-sector spectral gap,
C_Q      = semigroup constant,
epsilon  = admissible incoherent leakage tolerance.
```

The corresponding effective scale is:

```text
Lambda_eff = tau_adm^{-1/2}
           = sqrt(lambda_* / log(C_Q / epsilon_adm)).
```

This is the key move.  The scale is selected by fixed-point damping data rather
than by fitting a target constant.

# Stage 3: Turn the Scale into an Absolute Normalization

One branch must then be proved:

```text
Lambda_eff = alpha_prime^{-1/2}
```

or:

```text
Lambda_eff^2 = lambda_S1 ~= 1/R1^2
```

or:

```text
Lambda_eff fixes G10 through the selected 10D action normalization.
```

The central-circle branch is the best first branch because the Theta corpus
already uses:

```text
lambda_S1 ~ 1/R1^2
```

and Theta IV writes Newton structure in terms of:

```text
1/G_N ~= 31.8 R1^3/G10.
```

# Exploratory Numeric Model

For a dimensionless sanity check only, set:

```text
lambda_* = 1,
C_Q = 1,
epsilon_adm = 1/N.
```

Then:

| N | tau_adm | Lambda_eff |
|---|---:|---:|
| 64 | 4.1588830833596715 | 0.4903561700249054 |
| 79 | 4.3694478524670215 | 0.4783950966922162 |
| 448 | 6.104793232414985 | 0.4047291831143895 |

These are not physical predictions.  They show that once the finite-sector
tolerance and Hessian gap are selected, the scale is no longer free.

# What This Solves

This gives a non-backsolved path:

```text
selected Hessian data
selected damping tolerance
selected physical branch
-> absolute normalization.
```

# What Remains

To close the branch, we must supply:

```text
lambda_* from the selected MTT/Strominger Hessian,
C_Q from the incoherent semigroup estimate,
epsilon_adm from finite-sector resolution or basin separation,
one proved physical identification of Lambda_eff.
```

# Forbidden Shortcuts

The construction must reject:

```text
epsilon chosen to match G_N,
lambda_* chosen to match M_Pl,
branch chosen after checking H0 or rho_DE,
observed target constants used as minimization data.
```
