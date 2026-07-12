---
abstract: |
  We reduce the remaining finite-label source problem to a label-selection
  problem.  In the selected B_q packet, the weighted right-channel Gram
  matrices have nondegenerate spectra.  Therefore any selected source operator
  that commutes with the right Gram matrix and assigns distinct finite labels
  to the light right channels has uniquely determined spectral projectors.
  There is no continuous freedom left in the right-channel projector placement.
  What remains is to prove that MTT assigns the labels themselves:
  retarded spinorial split in the up sector and dyadic/nil split in the down
  sector.
author:
- Peter Nero
date: June 2026
title: |
  Right-Channel Projector Selection Reduction
---

# Purpose

The finite-label source schema introduced the projectors:

```text
Xi_u,
P_dyad,
P_nil.
```

The obvious danger is that these projectors might be hidden fitting knobs.
This note proves the reduction that removes that danger:

```text
if the labels are selected and the operator commutes with K_x=Z_x^*Z_x,
then the projectors are forced by the weighted right-channel spectrum.
```

# Setup

Let:

```text
Z_x = Y_x G_A^{-1/2},
K_x = Z_x^* Z_x.
```

Assume `K_x` has simple spectrum:

```text
spec(K_x) = {k_{x,1}<k_{x,2}<k_{x,3}}.
```

Let the selected residual mass source `R_x` satisfy:

```text
[R_x,K_x]=0.
```

Then `R_x` is diagonal in the same spectral basis as `K_x`.

# Lemma: Projector Uniqueness

If `K_x` has simple spectrum, its spectral projectors:

```text
P_{x,a} = product_{b != a} (K_x-k_{x,b}I)/(k_{x,a}-k_{x,b})
```

are uniquely determined by `K_x`.

Therefore any self-adjoint operator `R_x` commuting with `K_x` has the form:

```text
R_x = r_{x,1}P_{x,1}+r_{x,2}P_{x,2}+r_{x,3}P_{x,3}.
```

The only remaining choices are the labels `r_{x,a}`.  The projectors are not
free parameters.

# Application to the Candidate

For the finite-label candidate:

```text
R_u = J(-1/2(P_{u,1}+P_{u,2}) - P_{u,1}+P_{u,2}),
R_d = (1/64)P_{d,1} + (3/2 lambda_nil)P_{d,2}.
```

The projectors are the two light spectral projectors of `K_u` and `K_d`.

Thus, once the labels are selected, the source operator is fixed.

# Remaining Label Theorems

The only unresolved source steps are now:

```text
1. Up label theorem:
   right-channel retarded spinorial source selects
   (-3/2 J,+1/2 J).

2. Down label theorem:
   dyadic survivor-width source selects 1/64 on the first light channel,
   nil half-channel source selects 3/2 lambda_nil on the second light channel.
```

# What This Closes

```text
right-channel projector freedom removed        PROVED
commuting source operator form fixed           PROVED
remaining problem reduced to finite labels     PROVED
label derivation from Sigma_MTT                OPEN
```

# Bottom Line

The mass-source problem is no longer a four-number fit.  It is now two finite
label theorems:

```text
up:   retarded spinorial split -> (-3/2 J,+1/2 J),
down: dyadic/nil split         -> (1/64,3/2 lambda_nil).
```

If those labels are derived from MTT, the projectors and the CKM-preserving
mass operator follow uniquely.

