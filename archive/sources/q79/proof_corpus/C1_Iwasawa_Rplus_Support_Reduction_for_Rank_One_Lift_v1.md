---
abstract: |
  We close the invariant Iwasawa R_+ support row feeding the C1 curvature
  insertion.  In the selected left-invariant Iwasawa branch, the torsional
  gravitational curvature satisfies Tr_grav R_+^2 = v1_tilde alpha_1 with
  v1_tilde = 8 r3^2/(r1^2 r2^2), and has no alpha_2 or alpha_3 component.
  Thus the invariant C1 curvature driver is a single alpha_1 row, not three
  independent curvature knobs.  This reduces the C1 linear-response input but
  does not yet evaluate Yukawa weights, since the map through V_C1, Hess_Xi,
  dotD_a, and zero-mode contractions remains open.
author:
- Peter Nero
date: May 2026
title: |
  C1 Iwasawa Rplus Support Reduction for Rank-One Lift
---

# Purpose

The C1 insertion formula says that the next numerical task is:

```text
V_C1 -> Hess_Xi^{-1} -> dotD_a -> zero-mode overlap.
```

Before evaluating that chain, we can close one piece of input data already
present in the corpus:

```text
the invariant Iwasawa support of Tr_grav R_+^2.
```

# Selected Branch

The branch is the left-invariant Iwasawa `SU(3)` structure used for the
rank-one tree seed.  The flux source states that, in this ansatz, the metric,
torsion, Bismut curvature, and gauge fields are all left-invariant.  Therefore
the Bianchi identity is complete inside the invariant `(2,2)` subspace:

```text
span{alpha_1, alpha_2, alpha_3}.
```

The same source identifies the left-invariant truncation with the coherent
spectral projection used in MTT.  Thus this is not an arbitrary finite
truncation; it is the coherent sector for the explicit Iwasawa calculation.

# Rplus Support

The source computes:

```text
Tr_grav R_+^2 = v1_tilde(r1,r2,r3) alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2).
```

There are no components along:

```text
alpha_2,
alpha_3.
```

For the equal-radius specialization `r1 = r2 = R`:

```text
v1_tilde = 8 r3^2/R^4.
```

The Bianchi component equation gives:

```text
r3^2 = 8(2*pi)^2 / (16/alpha_prime + 8/R^4).
```

# Bianchi Support

The same Iwasawa block gives:

```text
dH = -4 r3^2 alpha_1,
u1 = 8(2*pi)^2,
u2 = u3 = 0.
```

Thus:

```text
u2 = v2 = 0,
u3 = v3 = 0,
u1 - v1 = (16/alpha_prime) r3^2.
```

So the invariant curvature/Bianchi driver is aligned with the same `alpha_1`
row.

# Consequence for C1

This rules out a tempting but invalid maneuver:

```text
C1 cannot be treated as three independent invariant curvature coefficients.
```

In the selected invariant Iwasawa branch, the raw curvature driver is:

```text
alpha_1 only.
```

This is good news for rigor and bad news for casual freedom.  It makes C1 more
predictive, but it also means C1 by itself may be rank-limited unless the
alpha_1 row produces enough nontrivial zero-mode contractions through
`dotD_a` and the projector response.

# Theorem

#### Iwasawa Rplus Support Theorem

On the selected left-invariant Iwasawa branch, the C1 torsional curvature
input inherited from `Tr_grav R_+^2` has invariant support only on `alpha_1`,
with coefficient:

```text
v1_tilde = 8 r3^2/(r1^2 r2^2).
```

Consequently the invariant C1 curvature driver is a single row before applying
the selected `V_C1`, Hessian inverse, Dirac/operator variations, and zero-mode
overlap contractions.

#### Proof

The flux compactification source explicitly states that the Iwasawa metric,
torsion, Bismut curvature, and gauge fields are left-invariant, so the
componentwise Bianchi analysis is complete in the invariant `(2,2)` basis
`alpha_1, alpha_2, alpha_3`.

In the Rplus appendix, the source computes the torsional spin curvature:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
```

with no alpha_2 or alpha_3 component.  The main Iwasawa anomaly calculation
then uses exactly this support statement to set `v2 = v3 = 0` and solve the
Bianchi equations with only the alpha_1 component active.

The MTT appendix identifies the invariant truncation with the coherent
spectral projection, so the support statement applies to the selected
coherent Iwasawa calculation.  Therefore the C1 curvature input is alpha_1-only
inside this branch.  The Yukawa consequence still requires the later
linear-response evaluation, so no C1 Yukawa number follows here.

# What This Closes

```text
Iwasawa R_+ invariant support,
alpha_1-only curvature row,
explicit v1_tilde coefficient,
Iwasawa Bianchi component support,
coherent projection context,
one-row nature of the invariant C1 curvature driver.
```

# What Remains Open

```text
selected V_C1 functional,
map from alpha_1 row to deltaTheta_C1,
Hess_Xi blocks,
dotD_a operators,
zero-mode contractions,
C1 A_gamma values,
C1 S_gamma values,
rank-lift nonzero test.
```

# Next Calculation

The next C1 calculation is now narrower:

```text
feed alpha_1 into V_C1,
solve Hess_Xi deltaTheta_C1 = -Pi_coh grad V_C1,
compute dotD_a(deltaTheta_C1),
contract with the selected zero modes.
```

Only that can decide whether C1 supplies one or two nonzero light-family
eigenchannels.

Follow-up status: the alpha1 rank-lift criterion is now closed.  If
`M_C1^(alpha1)` is the response matrix obtained from this single curvature
row, then:

```text
det(E33 + epsilon M_C1)
  = epsilon^2 (M11*M22 - M12*M21)
    + epsilon^3 det(M_C1).
```

So the first decisive C1 overlap calculation is the light-family minor
`M11*M22 - M12*M21`.
