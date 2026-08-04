---
abstract: |
  We test whether the remaining right-channel assignment observables can be
  read directly from simple family-basis label operators already present in
  the finite B_q packet.  The answer is no.  Operators such as the anchor
  profile J, family index, Z3 clock/shift, and raw basis projectors either fail
  to commute with the weighted right-channel Gram matrices or fail the required
  trace table.  Therefore the final assignment cannot be claimed from a raw
  family-basis label.  It must come from a selected Schur/Riesz/projection
  source observable in the same right-channel basis, or from a concrete
  Sigma_MTT operator that already commutes with the right Gram matrices.
author:
- Peter Nero
date: June 2026
title: |
  Right-Channel Label Observable Dictionary Scan
---

# Purpose

The assignment target requires three source observables:

```text
S_u^spin,
S_d^dyad,
S_d^nil
```

with:

```text
[S_u^spin,K_u]=0,
[S_d^dyad,K_d]=0,
[S_d^nil,K_d]=0.
```

This scan asks whether these observables are already visible as simple
family-basis labels in the finite B_q packet.

# Dictionary Tested

The scan tests:

```text
I,
diag(J),
diag(0,1,2),
diag(-1,+1,0),
diag(0,-1,+1),
basis projectors diag(1,0,0), diag(0,1,0), diag(0,0,1),
Z3 Laplacian,
real and imaginary shift,
real and imaginary clock.
```

# Result

No raw dictionary operator passes both requirements:

```text
1. small commutator with K_x;
2. required trace table on the light projectors.
```

Examples:

```text
diag(1,0,0)
  nearly commutes better than most raw basis operators,
  but its down-sector traces are approximately (0.068,0.932),
  the opposite of the required dyadic trace (1,0).

diag(-1,+1,0)
  has spin-like values,
  but it does not commute with K_u and its up traces are about
  (0.283,-0.961), not (-1,+1).

Z3 Laplacian
  is too degenerate/symmetric and cannot provide the required split.
```

# Interpretation

This is a useful guardrail.  The remaining source observable is not a raw
family-basis label.  It must be one of:

```text
1. a Schur-Feshbach reduced label observable;
2. a Riesz-projected source observable;
3. a concrete Sigma_MTT right-channel operator already diagonal in K_x;
4. a selected commutant projection of a raw proto-spinor/nil/dyadic source.
```

Using the spectral projectors alone would reproduce the trace table, but that
would be a definition, not a source derivation.  A valid proof must show why
MTT supplies those projected observables before mass comparison.

# What This Closes

```text
raw family-basis assignment source             TESTED-NO-GO
need Schur/Riesz/projected source observable   IDENTIFIED
assignment theorem remains open                OPEN
```

# Bottom Line

The last source layer is genuinely nontrivial.  It is not hidden in a simple
raw family label.  The next viable route is to construct the selected
commutant-projected source observable:

```text
E_K(A) = sum_a P_a A P_a,
```

from a corpus-native raw observable `A`, and then prove that this Schur/Riesz
projection is the actual `Sigma_MTT` execution rule.

