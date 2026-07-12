---
title: "Visible Chern-Weil Formal Source"
author: "Peter Nero"
date: "May 2026"
abstract: |
  After the selected S3 class/restriction closure, the remaining visible-source
  problem asks whether the required Green-Schwarz row can come from a selected
  visible Chern-Weil source.  This note proves the weakest useful statement:
  the required row has no algebraic trace-free Chern-Weil obstruction.  A
  formal rank-two block with curvature eigenvalues (+f,-f) realizes
  Tr F_visible^2 = (8*r3^2/(r1^2*r2^2)+4*r3^2) alpha_1 and no alpha_2 or
  alpha_3 component.  Integrality, stability, HYM/Route-C selection, D_E/dotD,
  and primitive C1 contractions remain open.
---

# Purpose

The current target is the selected visible Chern-Weil/operator source.  Before
constructing a bundle or Route-C solve, we can ask a smaller question:

```text
Is the required visible Tr F^2 row algebraically realizable by a trace-free
curvature source?
```

# Required Row

The visible Green-Schwarz requirement forces:

```text
Tr F_visible^2 =
  (8*r3^2/(r1^2*r2^2) + 4*r3^2) alpha_1,
alpha_2 component = 0,
alpha_3 component = 0.
```

# Formal Rank-Two Realization

Take a formal trace-free rank-two block:

```text
F = diag(+f, -f).
```

Then:

```text
Tr F = 0,
Tr F^2 = f^2 + (-f)^2 = 2 f^2.
```

Choose:

```text
f^2 = 4*r3^2/(r1^2*r2^2) + 2*r3^2.
```

Therefore:

```text
Tr F^2 =
  2*(4*r3^2/(r1^2*r2^2) + 2*r3^2)
  = 8*r3^2/(r1^2*r2^2) + 4*r3^2.
```

This exactly matches the required alpha1 coefficient, with no alpha2 or
alpha3 support.

# What This Closes

This closes only:

```text
formal trace-free Chern-Weil row realizability,
absence of an algebraic alpha2/alpha3 obstruction,
compatibility of the selected S3 closure with a visible Chern-Weil target.
```

# What Remains

The hard source problem remains:

```text
integral quantized bundle or sheaf class,
stable visible bundle or sheaf model,
MTT selection of that source,
HYM/Strominger or Route-C residual,
source-derived Chern-Weil representative,
sector D_E/dotD/Riesz/Green data,
coherent spectral projectors,
primitive C1 contractions,
Yukawa/CKM/PMNS magnitudes.
```

In short: the row is algebraically available, but it is not yet a selected
visible SM operator source.
