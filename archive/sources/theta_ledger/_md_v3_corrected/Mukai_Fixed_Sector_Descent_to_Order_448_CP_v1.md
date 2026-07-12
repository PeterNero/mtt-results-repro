---
abstract: |
  We update the order-448 CP descent after replacing the broken Lens-Nil
  determinant-seven source by the positive Mukai charge block.  The finite
  arithmetic is unchanged: the Mukai block has Smith normal form [7], the
  recursive shared-circle carry contributes [64], and the selected product has
  Smith normal form [448].  With the family Z3 kept as an orthogonal ambient
  factor, the ambient block has order 1344 and the family quotient leaves the
  selected order-448 CP character.  What remains open is no longer the finite
  abelian arithmetic, but the geometric selection theorem: stable
  sheaf/bundle realization, Fu-Yau anomaly compatibility, global topological
  sector selection, and derivation of the Z64 dyadic carry from the recursive
  shared circle.  The CP-character identification and fixed-sector MTT
  selection reduction are now closed once the Mukai sector is supplied.
author:
- Peter Nero
date: May 2026
title: |
  Mukai Fixed-Sector Descent to the Order-448 CP Character
---

# Purpose

This note carries the new Mukai `Z_7` block forward into the full order-448
program.

The previous arithmetic checks used the same matrix:

```text
K = [[2,1],
     [1,4]],
SNF(K)=[7].
```

But the label "Lens-Nil" is no longer the live geometric source.  The current
source is:

```text
K_Mukai = Gram_Mukai((5,H,0),(7,3H,1)).
```

So the selected CP arithmetic should now be read as:

```text
Z_64 from recursive shared-circle dyadic carry,
Z_7 from the positive Mukai charge block,
Z_3 as the family factor kept orthogonal to chi_CP.
```

# Mukai odd factor

From:

```text
Mukai_Positive_Charge_Block_for_Fu_Yau_K3_Z7_CP_v1.md
```

we have:

```text
H^2=2,
a=(5,H,0),
b=(7,3H,1),
Gram_Mukai(a,b)=
[[2,1],
 [1,4]].
```

Therefore:

```text
coker(K_Mukai) ~= Z_7,
Hom(coker K_Mukai,U(1)) ~= Z_7.
```

# Dyadic factor

The dyadic block is still the six-stage carry candidate:

```text
SNF(carry_6)=[64].
```

This remains an open geometric derivation gate, but the finite arithmetic is
clear.

# Selected quotient

Because:

```text
gcd(64,7)=1,
```

the selected product is cyclic:

```text
Z_64 x Z_7 ~= Z_448.
```

The block diagonal matrix:

```text
carry_6 + K_Mukai
```

has:

```text
SNF=[448].
```

# Ambient quotient

Keep the family factor as a separate `Z_3`:

```text
Gamma_amb ~= Z_64 x Z_7 x Z_3.
```

Since:

```text
gcd(64,7,3)=1,
```

the ambient block has:

```text
SNF=[1344].
```

The CKM CP label used in the arithmetic ledger is:

```text
237 mod 1344.
```

Its order is:

```text
1344 / gcd(237,1344) = 448.
```

The family kernel is:

```text
{0,448,896}.
```

So the selected CP character is the order-448 quotient of the ambient
order-1344 character.

# Current theorem skeleton

The proof should now be stated as:

```text
Assume:
1. the recursive shared-circle gate gives the dyadic carry block [64];
2. a Bianchi-compatible Fu-Yau/K3 topological sector supplies the positive
   Mukai charge block K_Mukai as an integral charge-lattice quotient;
3. fixed-sector MTT selection carries that supplied quotient to the selected
   Strominger fixed point;
4. the CP labels are Hom(coker K_Mukai,U(1)) on the odd sector;
5. the family Z3 is orthogonal to chi_CP.

Then:
Gamma_CP,min ~= Z_448,
Gamma_amb ~= Z_1344,
Gamma_amb / Z_3-family ~= Z_448.
```

# Remaining gates

```text
stable sheaf realization              closed for individual Mukai vectors
CP character identification           closed once A_P is supplied
MTT fixed-sector selection            closed once sector contains A_P
Fu-Yau anomaly/topological completion open
global topological-sector choice      open
recursive shared-circle Z64 derivation open
```

One caveat is now essential.  The Mukai block is currently a charge-lattice
block, not a two-summand HYM bundle construction.  The explicit generators
`(5,H,0)` and `(7,3H,1)` have different slopes, and a same-slope
Picard-rank-one determinant-seven Mukai Gram block is obstructed.  Therefore
the selected quotient theorem should use the charge-lattice/differential-
character interpretation unless a new stable bundle construction is supplied.

# Executable check

The check:

```text
mukai_fixed_sector_descent_check.py
```

reports:

```text
Mukai positive charge block K_Mukai       SNF [7]
six-stage dyadic carry                    SNF [64]
selected CP quotient block                SNF [448]
ambient block with family Z3              SNF [1344]
CKM CP label 237 mod 1344                 order 448
```

# Bottom line

The finite quotient arithmetic survives the Fu-Yau correction:

```text
Lens-Nil source failed;
negative K3 H^2 source is root-obstructed;
positive Mukai charge source carries the Z_7 factor forward.
```

So the next real proof work is geometric selection, not arithmetic search.
