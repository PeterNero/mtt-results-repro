---
abstract: |
  We close the algebraic rank test for the single alpha_1 C1 response row.
  The Iwasawa Rplus support theorem showed that the selected invariant C1
  curvature driver is alpha_1-only.  This does not by itself prevent full rank:
  if the induced C1 response matrix M_C1^(alpha1) has nonzero light-family
  minor M11*M22 - M12*M21, then E33 + epsilon M_C1^(alpha1) has full rank for
  sufficiently small nonzero epsilon.  Thus the next C1 computation is reduced
  to a sharp overlap determinant, while the actual entries of M_C1 remain open.
author:
- Peter Nero
date: May 2026
title: |
  C1 Alpha1 Rank-Lift Criterion for the Rank-One Yukawa Seed
---

# Purpose

The C1 Iwasawa support reduction closed:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
alpha_2 = alpha_3 = 0.
```

A single invariant curvature driver can sound too small to open two light
families.  Algebraically, that worry is not justified.  What matters is not
the number of curvature-driver rows before response; what matters is the rank
of the matrix produced after the chain:

```text
alpha_1
-> V_C1
-> Hess_Xi^{-1}
-> dotD_a
-> zero-mode contractions.
```

This note closes the exact rank test for that produced matrix.

# Setup

Use the normalized rank-one Iwasawa seed:

```text
Y0 = E33 = diag(0,0,1).
```

Let the first selected alpha_1 C1 response be:

```text
M = M_C1^(alpha1).
```

This is not a free matrix.  It is the matrix obtained by feeding the closed
alpha_1 curvature row through the selected C1 response chain.  Its entries are
still open overlap contractions.  The perturbed raw Yukawa matrix is:

```text
Y(epsilon) = E33 + epsilon M + O(epsilon^2).
```

Write:

```text
M =
[[a, b, c],
 [d, e, f],
 [g, h, i]].
```

# Determinant Expansion

A direct determinant expansion gives:

```text
det(E33 + epsilon M)
  = epsilon^2 (a e - b d)
    + epsilon^3 det(M).
```

Equivalently:

```text
det(E33 + epsilon M)
  = epsilon^2 C33(M) + epsilon^3 det(M),
```

where:

```text
C33(M) = M11*M22 - M12*M21.
```

Thus the leading full-rank test is the light-family 2x2 minor:

```text
C33(M_C1^(alpha1)) != 0.
```

# Theorem

#### Alpha1 Rank-Lift Criterion

Let:

```text
Y(epsilon) = E33 + epsilon M + O(epsilon^2)
```

with `M` the selected C1 response matrix induced by the alpha_1 curvature row.
If:

```text
M11*M22 - M12*M21 != 0,
```

then, for all sufficiently small nonzero `epsilon`, `Y(epsilon)` has rank
three.  In particular, one invariant C1 curvature driver is algebraically
enough to open two light-family eigenchannels, provided its selected response
matrix has rank two on the light-family block.

#### Proof

Expanding along the third row/column structure of `E33` gives:

```text
det(E33 + epsilon M)
  = epsilon^2 (M11*M22 - M12*M21)
    + epsilon^3 det(M).
```

If the coefficient of `epsilon^2` is nonzero, then the determinant is nonzero
for sufficiently small nonzero `epsilon`.  Therefore the perturbed matrix has
rank three.  The conclusion depends only on the induced response matrix, not
on having three independent curvature-driver components before response.

# Degenerate Case

If:

```text
C33(M) = 0
```

but:

```text
det(M) != 0,
```

then the determinant can still become nonzero at order `epsilon^3`.  This is
not the same as closing the leading two-light-eigenchannel criterion, because
the first C1 response does not have rank two on the light-family block.

If both:

```text
C33(M) = 0,
det(M) = 0,
```

then this C1 response does not pass the determinant test by itself.

# Consequence for C1

The next C1 calculation is not an unstructured 3x3 mystery.  For each sector,
the first decisive scalar is:

```text
C33_s = M_s,11 M_s,22 - M_s,12 M_s,21.
```

For quarks:

```text
C33_u != 0,
C33_d != 0
```

would close leading full rank in the up and down sectors.  CKM mixing still
requires the separate orientation/noncommutation test:

```text
[Y_u Y_u^dagger, Y_d Y_d^dagger] != 0.
```

The q79 character supplies the CP-active phase once the noncommuting closed
quark channel product is selected.

# What This Closes

```text
single alpha_1 C1 driver is not algebraically fatal,
leading rank-lift determinant is C33(M),
two-light-eigenchannel pass condition is explicit,
rank and CKM noncommutation are separated,
the next overlap calculation has a four-entry first target.
```

# What Remains Open

```text
actual M_C1^(alpha1) entries,
selected V_C1 functional,
explicit Hess_Xi blocks,
explicit dotD_a operators,
zero-mode contractions,
up/down response orientations,
canonical kinetic metrics,
RG and threshold matching.
```

# Next Calculation

Compute the four light-family contractions:

```text
M11, M12, M21, M22
```

for `M_C1^(alpha1)` in each sector.  The first decisive test is:

```text
M11*M22 - M12*M21 != 0.
```

Only after this passes should we spend serious effort on the remaining entries,
canonical normalization, and CKM angle magnitudes.

Follow-up CKM status: the leading noncommutation criterion is now closed.  For
quark response matrices:

```text
Y_u = E33 + epsilon M_u + O(epsilon^2),
Y_d = E33 + epsilon M_d + O(epsilon^2),
```

the first up/down orientation target is:

```text
Delta_v = (M_d13-M_u13, M_d23-M_u23).
```

If `Delta_v` is nonzero, then `[Y_uY_u^dagger,Y_dY_d^dagger]` is nonzero at
leading order.
