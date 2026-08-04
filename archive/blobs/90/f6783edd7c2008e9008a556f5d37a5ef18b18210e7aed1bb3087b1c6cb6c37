---
abstract: |
  We extend the finite quotient replacement test from cyclic groups to finite
  abelian product quotients, as naturally produced by Smith normal form.  The
  key result is that a literal cyclic Z_448 is not necessary: the product
  quotient Z_64 x Z_7 supports a diagonal character with the same CKM
  phase-branch accuracy and exact leptonic -pi/2 as the Z_448 benchmark.
  However, not every factorization of 448 works.  Product quotients such as
  Z_4 x Z_112, Z_8 x Z_56, Z_16 x Z_28, and Z_2 x Z_224 collapse to the same
  coarse phase accuracy as Z_112/Z_224 in the simple diagonal-character test.
  Therefore the structural target is sharpened: MTT need not derive literal
  Z_448, but it must derive a quotient whose character spectrum contains a
  diagonal cyclic subsystem of effective order 448, preferably with coprime
  factors 64 and 7 or an equivalent character embedding.
author:
- Peter Nero
date: May 2026
title: |
  Product Quotient Character Criteria for MTT Flavor CP
---

# Purpose

The recursive quotient program computes the finite flavor character group by
Smith normal form:

```text
Gamma_fl ~= Z_{d1} x ... x Z_{dr} x Z^s.
```

The finite CP characters live in the torsion part.  Therefore the quotient
selected by MTT need not be cyclic.  A product quotient may still contain a
diagonal character subsystem with the same effective order as `Z_448`.

# Product character diagnostic

For a product quotient

```text
G = Z_{d1} x ... x Z_{dr},
```

use a diagonal character phase

```text
delta(k_1,...,k_r)
 =
2 pi sum_i k_i/d_i
mod 2 pi.
```

This is the first diagnostic.  A later detailed MTT model may restrict which
diagonal characters are selected by overlap channels.

# Script

The diagnostic script is:

```text
finite_abelian_quotient_character_search.py
```

It searches character tuples for:

- CKM phase-branch closeness to `delta_q = 1.107978573420`;
- CKM Jarlskog error;
- leptonic phase closeness to `-pi/2`.

# Main result

The product presentation

```text
Z_64 x Z_7
```

matches the `Z_448` benchmark under a diagonal character:

```text
G = Z_64 x Z_7
CKM weights = (57, 2)
delta_q = 1.107972409079
phase error = 6.164e-06
J error = 8.920e-11
lepton weights = (48, 0)
delta_l = -pi/2 exactly
```

This is the same phase quality as the cyclic `Z_448` benchmark.  Since `64`
and `7` are coprime, the finite abelian group `Z_64 x Z_7` is abstractly
isomorphic to `Z_448`.  The difference is source-theoretic, not
group-theoretic: MTT might derive separate dyadic and sevenfold rows whose
Smith normal form combines into a single `Z_448` invariant factor.

# Why this matters

This weakens the target theorem in a good way.

The old source target was:

```text
derive Z_448.
```

The better source target is:

```text
derive a finite quotient whose character spectrum contains
an effective order-448 diagonal subsystem.
```

This matters because recursive topology, flux quantization, and orbifold data
may naturally produce separate rows for coprime factors.  Smith normal form then
combines those rows into the invariant cyclic factor.

# Not every factorization works

The script also checks several factorizations of `448`.  In the simple
diagonal-character diagnostic:

```text
Z_4 x Z_112   phase error = 1.402e-02
Z_8 x Z_56    phase error = 1.402e-02
Z_16 x Z_28   phase error = 1.402e-02
Z_32 x Z_14   phase error = 1.402e-02
Z_2 x Z_224   phase error = 1.402e-02
```

These are much worse than `Z_448` or `Z_64 x Z_7` on the CKM phase branch.

The reason is structural: to get a true order-448 phase resolution, the relevant
components must combine with least common multiple `448` in the selected
character.  The coprime split

```text
448 = 64 * 7
```

is the cleanest source presentation, and Smith normal form identifies it with a
cyclic `Z_448` invariant factor.

# Interpretation for recursive MTT

The quotient-search target should now be:

1. compute `A_rec` from shared-circle, lens, nil, flux, Wilson-line, orbifold,
   pairwise-bundle, and projector rows;
2. compute `Tor coker A_rec`;
3. check whether `Tor coker A_rec` contains:
   - a cyclic `Z_448`, or
   - a product subsystem such as `Z_64 x Z_7`, or
   - another diagonal character subsystem with comparable phase accuracy;
4. only then attach the character data to overlap kernels.

# Possible structural origins

The product criterion suggests new places to look:

- a `Z_64` factor from recursive shared-circle closure, repeated covering, or
  projector periodicity;
- a `Z_7` factor from flux/orbifold/discrete gauge data;
- a diagonal compatibility condition coupling the two factors in the pairwise
  line-bundle phase sum.

This is more plausible than demanding that a single terminal manifold factor
produce `Z_448`.

# Majorana sector

The Majorana admissibility condition remains separate.  For a finite abelian
group `G`, a neutral character `x in G` is Majorana self-admissible only if

```text
2x = 0.
```

For `Z_64 x Z_7`, the two-torsion subgroup is generated by the element

```text
(32, 0).
```

Thus the CP diagonal character and the Majorana neutral character must still be
distinguished.

# Bottom line

The finite CP target is now more flexible and more rigorous:

```text
Do not force literal Z_448.
Derive Tor coker A_rec.
Accept any derived quotient whose selected character spectrum
contains the required effective order-448 phase resolution.
```

`Z_64 x Z_7` is now a first-class replacement target.
