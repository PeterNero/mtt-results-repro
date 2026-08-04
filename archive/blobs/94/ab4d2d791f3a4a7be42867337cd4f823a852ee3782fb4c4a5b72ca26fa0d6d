---
title: "Visible Split Line HYM No-Go for Positive Alpha1 Source"
author: "Peter Nero"
date: "May 2026"
abstract: |
  The integral visible source target is c1=0 and ch2=4 alpha_1.  This note
  proves that no finite split line-bundle or diagonal Cartan HYM source can
  realize the positive alpha_1 Chern-Weil row on the Iwasawa branch.  The proof
  is algebraic: individual primitivity gives S p = 0 for a positive slope
  vector p, while the target row gives a first component S11*p1 + 4*p2 > 0.
  Thus the remaining source must be genuinely nonabelian stable/sheaf data or
  an honest Route-C HYM/Strominger solve for the same class.
---

# Purpose

The previous packet closed the integral target:

```text
c1 = 0,
ch2 = 4 alpha_1,
Tr F^2 = 8*(2*pi)^2 alpha_1.
```

It also rejected the displayed two-line split candidate.  Here we prove the
general split line-bundle no-go.

# Setup

Let the split line/Cartan flux vectors be:

```text
n^(a) = (n1^(a), n2^(a), n3^(a)) in Z^3.
```

For an individual HYM line summand, primitivity requires:

```text
p dot n^(a) = 0
```

where the Iwasawa slope vector is positive:

```text
p = (r2^2/r3^2, r1^2/r3^2, r1^2/r2^2),
p_i > 0.
```

Define the second-moment matrix:

```text
S_ij = sum_a n_i^(a) n_j^(a).
```

Since every `n^(a)` is orthogonal to `p`,

```text
S p = sum_a n^(a) (n^(a) dot p) = 0.
```

# Target Row

The positive visible alpha_1 target is:

```text
S12 = 4,
S13 = 0,
S23 = 0.
```

The first component of `S p = 0` is:

```text
S11*p1 + S12*p2 + S13*p3 = 0.
```

Substituting the target row:

```text
S11*p1 + 4*p2 = 0.
```

But `S11 = sum_a (n1^(a))^2 >= 0` and `p1,p2 > 0`, hence:

```text
S11*p1 + 4*p2 > 0.
```

Contradiction.

# Conclusion

Therefore:

```text
no finite split line-bundle / diagonal Cartan HYM source
can realize the positive alpha_1 visible source row.
```

This does not obstruct a nonabelian stable bundle or sheaf.  It also does not
obstruct a direct Route-C HYM/Strominger solve.  It only removes the entire
split-line shortcut class.

# Remaining Source Target

The next source must provide:

```text
selected nonabelian stable bundle/sheaf with c1=0, ch2=4 alpha_1,
or selected Route-C residual solve for the same class,
plus same-source D_E, dotD, Riesz/Green, and projector-retention data.
```
