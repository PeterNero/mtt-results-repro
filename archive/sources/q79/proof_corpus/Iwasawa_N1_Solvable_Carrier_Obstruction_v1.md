---
abstract: |
  We lift the N=1 prime-field phase coboundary obstruction to finite solvable
  matrix carriers.  Since the N=1 source-level phase cohomology vanishes for
  F2, F3, F5, and F7, any non-coboundary flat table in a finite solvable carrier
  whose abelian composition primes lie in this set would descend at some
  derived quotient to a forbidden non-coboundary prime-order phase table.
  Therefore the usual small solvable matrix carriers, including S3 permutation
  matrices, dihedral carriers, A4/S4 rotation carriers, quaternion/nilpotent
  carriers, and finite Heisenberg phase carriers over the certified primes,
  cannot close rhoE-source promotion at N=1.  Perfect or non-solvable carriers,
  larger meshes, and selected D_E-response promotion remain open.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa N=1 Solvable Carrier Obstruction
---

# Purpose

After the phase coboundary obstruction, the obvious next attempt is:

```text
try genuinely matrix-valued finite carriers.
```

The first matrix carriers one naturally reaches for are usually solvable:

```text
S3 permutation matrices,
dihedral groups,
quaternion or nilpotent groups,
finite Heisenberg groups,
A4 and S4 rotation representations.
```

This note proves that this whole family is still blocked at `N=1`, at the
`rhoE_source` promotion level, whenever the relevant abelian composition primes
are among:

```text
2, 3, 5, 7.
```

# Input

The prior executable obstruction proves:

```text
H^1_source(N=1; F_p) = 0
```

for:

```text
p = 2, 3, 5, 7.
```

In the finite-table language, every flat prime-field phase table is a
source-key-compatible coboundary.

# Derived-Series Lift

Let `G` be a finite solvable carrier group.  If a `G`-valued source-level flat
table is non-coboundary, descend through the derived series:

```text
G >= [G,G] >= [[G,G],[G,G]] >= ...
```

At the first nontrivial abelian derived quotient, the table gives a nontrivial
abelian obstruction.  A finite nontrivial abelian group has a cyclic
prime-order quotient:

```text
C_p.
```

Thus a non-coboundary finite solvable carrier table would produce a
non-coboundary `F_p` phase table for some composition prime `p`.

But for the certified primes:

```text
p in {2,3,5,7},
```

the phase obstruction says no such source-level class exists.

# Covered Examples

The executable audit covers these representative matrix-carrier families:

```text
cyclic phase carriers,
dihedral D4/D5/D7 carriers,
quaternion Q8,
finite Heisenberg p-groups for p=2,3,5,7,
S3 permutation matrices,
A4 tetrahedral rotation representation,
S4 octahedral rotation representation,
GL(2,F3)-type solvable binary carrier.
```

All are blocked as `N=1` source-level `rho_E` closure routes by the same
derived-series argument.

# What This Closes

This closes the next tempting false route:

```text
small finite solvable nonabelian matrix carriers at N=1.
```

In particular, replacing scalar/diagonal phases by `S3` permutation matrices
does not evade the source-level obstruction.

# What Remains Open

This is not a general nonabelian no-go theorem.

It does not rule out:

```text
perfect or non-solvable finite carriers, such as A5 or PSL(2,7),
larger mesh N > 1 searches,
typed Cech/monad transition data,
finite HYM/Strominger selected D_E response,
de_response promotion with nonzero dotD source and horizontal response.
```

# Correct Next Move

The source-level search has now narrowed again.

The next finite carrier search should target:

```text
perfect/non-solvable carriers,
```

or we should pivot from source-level `rho_E` promotion to:

```text
selected D_E/dotD response promotion.
```

That is the live route toward primitive C1 contractions and eventually the
actual no-proxy Yukawa matrices.
