---
title: "Visible Integral Chern Source Candidate and HYM Gate"
author: "Peter Nero"
date: "May 2026"
abstract: |
  The visible Chern-Weil row has now been promoted as far as current data
  honestly allow.  The Iwasawa flux corpus supplies an integral candidate:
  two integer vectors (1,2,0) and (-1,-2,0) give
  Tr F^2 = 8*(2*pi)^2 alpha_1, hence standard label 4 in
  (1/(8*pi^2)) Tr F^2 units.  This closes the integral Chern-character
  candidate, but the split abelian shortcut fails the HYM/primitivity gate:
  individual summands are not primitive for positive radii.  The next source
  must be a selected nonabelian stable bundle/sheaf or an honest Route-C solve
  with the same c1=0, ch2=4 alpha_1 class.
---

# Purpose

The previous gate separated normalization from selection.  Here we ask:

```text
Can the required alpha_1 row be represented by an integral Chern-character
candidate with an explicit trace convention?
```

The answer is yes.  But the same calculation also rejects the tempting split
abelian candidate as the final HYM source.

# Integral Candidate

The Iwasawa flux corpus gives the trace convention:

```text
F = 2*pi * sum_a T_a (n1^a a + n2^a b + n3^a c),
Tr(T_a T_b) = delta_ab,

Tr(F wedge F)
  = 2*(2*pi)^2 sum_a(
      n1^a n2^a alpha_1
    + n1^a n3^a alpha_2
    + n2^a n3^a alpha_3).
```

Take:

```text
n^(1) = (1, 2, 0),
n^(2) = (-1, -2, 0).
```

Then:

```text
sum n1*n2 = 1*2 + (-1)*(-2) = 4,
sum n1*n3 = 0,
sum n2*n3 = 0.
```

Therefore:

```text
Tr(F wedge F) = 8*(2*pi)^2 alpha_1.
```

In the common instanton normalization:

```text
(1/(8*pi^2)) Tr(F wedge F) = 4 alpha_1.
```

So the integral candidate is:

```text
c1 = 0,
ch2 row = 4 alpha_1
```

up to the selected trace/sign convention.  This is the concrete integral
target that a selected visible source must realize.

# HYM Gate

For a line-vector `n=(n1,n2,n3)`, the line HYM/primitivity condition is:

```text
n1*r2^2/r3^2 + n2*r1^2/r3^2 + n3*r1^2/r2^2 = 0.
```

For the two candidate vectors:

```text
(1,2,0):    r2^2/r3^2 + 2*r1^2/r3^2 > 0,
(-1,-2,0): -r2^2/r3^2 - 2*r1^2/r3^2 < 0.
```

Thus neither individual summand is primitive for positive radii.  They cancel
in total, but split HYM/polystability requires the individual summands or
Cartan components to satisfy the HYM condition, not merely the total first
Chern vector.

This is the important correction:

```text
the integral row exists,
the split abelian shortcut fails,
the final source must be nonabelian/stable or Route-C.
```

# What This Closes

This closes:

```text
explicit period/trace candidate for the alpha_1 row,
standard label 4 for the candidate Chern-character row,
proof that copied split abelian flux is not a selected HYM source,
the exact next source target: c1=0, ch2=4 alpha_1.
```

# What Remains

The remaining source theorem is now sharper:

```text
construct a selected nonabelian stable bundle/sheaf with c1=0 and ch2=4 alpha_1,
or solve Route C for the same class with verified HYM/Strominger residual,
then derive D_E, dotD, Riesz/Green, projector retention, and C1 contractions
from that same source.
```

This does not yet close full SM data.  It removes the integrality ambiguity and
prevents an invalid HYM shortcut.
