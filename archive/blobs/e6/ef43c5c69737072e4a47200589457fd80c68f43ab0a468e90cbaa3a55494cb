---
abstract: |
  We test the first tempting finite Wilson source for the missing selected
  Iwasawa rho_E data: a constant rank-three scalar-central Weyl/clock-shift
  representation.  Writing each generator as R_i=P^a_i Q^b_i over F_3, the
  implemented Iwasawa rho_E relations become six symplectic equations.  The
  two required commuting pairs force each pair to span dimension at most one in
  F_3^2, so the cross-pairing matrix must have determinant zero.  But the
  demanded cross pairings have matrix [[s5,s6],[s6,-s5]], whose determinant is
  -(s5^2+s6^2).  Over F_3 this vanishes only for s5=s6=0.  A brute-force scan
  confirms 321 trivial-phase schema solutions and zero nontrivial scalar
  central solutions.  Thus the first constant finite-Heisenberg Wilson ansatz
  cannot supply the selected nontrivial rho_E data.  This does not obstruct
  coordinate-dependent/table-valued rho_E, typed Cech/monad transitions,
  non-scalar central 3x3 data, or a higher auxiliary carrier with a selected
  rank-three quotient.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Constant Wilson rho_E Ansatz Obstruction
---

# Purpose

Route C needs actual selected values for:

```text
rho_E,
Hermitian metric H,
A^(0,1) or D_E,
sector projectors,
dotD_alpha1.
```

The most tempting first finite `rho_E` attempt is a constant rank-three
finite-Heisenberg/Wilson carrier:

```text
R_i = P^a_i Q^b_i,       (a_i,b_i) in F_3^2,
P Q = omega Q P,
g5 = omega^s5 I,
g6 = omega^s6 I.
```

This note tests exactly that ansatz.

# Iwasawa Relation Reduction

Let:

```text
v_i = (a_i,b_i),
<v_i,v_j> = a_i b_j - b_i a_j mod 3.
```

The constant `rho_E` validator imposes:

```text
g1 g2 = g2 g1,
g3 g4 = g4 g3,
g1 g3 = g5 g3 g1,
g1 g4 = g6 g4 g1,
g2 g3 = g6 g3 g2,
g5 g2 g4 = g4 g2.
```

For the scalar-central Weyl ansatz this becomes:

```text
<v1,v2> = 0,
<v3,v4> = 0,
<v1,v3> = s5,
<v1,v4> = s6,
<v2,v3> = s6,
<v2,v4> = -s5.
```

The cross-pairing block is:

```text
[[s5,  s6],
 [s6, -s5]].
```

Its determinant is:

```text
-(s5^2+s6^2).
```

Over `F_3`, `x^2` is `0` or `1`.  Therefore the determinant is zero only when:

```text
s5 = s6 = 0.
```

The nonzero central-character cases cannot satisfy the relation pattern in
this one-clock/one-shift rank-three ansatz.

The key point is why this determinant must vanish.  In a two-dimensional
symplectic vector space, an isotropic pair spans dimension at most one.  Since
both `(v1,v2)` and `(v3,v4)` are forced to be isotropic, the cross-pairing map
between the two pairs has rank at most one.  Hence its determinant must be
zero, contradicting every nonzero `(s5,s6)` central-character row above.

# Executable Scan

The audit script runs:

```text
scripts/scan_iwasawa_constant_wilson_ansatz.py
```

It brute-forces all:

```text
(v1,v2,v3,v4) in (F_3^2)^4,
(s5,s6) in F_3^2.
```

The result is:

```text
total vector assignments = 6561,
trivial phase solution count = 321,
nontrivial scalar-central solutions = 0.
```

The full central phase counts are:

```text
(s5,s6)=(0,0): 321,
all other (s5,s6): 0.
```

# What This Closes

This closes one bad shortcut:

```text
the selected nontrivial rho_E is not obtained by a constant rank-three
scalar-central one-clock/one-shift Wilson carrier.
```

It also explains why the identity constant matrices pass only as a schema
smoke test: they live in the `s5=s6=0` row and carry no selected nontrivial
bundle/sector data.

# What Remains Open

This obstruction is deliberately narrow.  It does not rule out:

```text
coordinate-dependent or table-valued rho_E,
typed Cech/monad transition data,
non-scalar central constant 3x3 representations,
higher-dimensional Wilson carriers followed by a selected rank-three quotient,
metric-dependent HYM/Strominger finite solves.
```

# Correct Way Forward

Route C should not spend its next effort on this scalar-central constant
rank-three Wilson ansatz.

The next viable searches are:

```text
1. coordinate/table-valued rho_E on the finite Iwasawa cell,
2. typed Cech/monad transition functions recovered from explicit sections,
3. a higher auxiliary finite-Heisenberg carrier whose selected quotient is rank three,
4. a direct HYM/Strominger finite residual solve with rho_E and H varied together.
```

The best immediate continuation is the first one because the mesh validators
already exist and can reject bad corner cocycles, bad metrics, bad sector maps,
and bad `D_E` actions without using observed flavor data.
