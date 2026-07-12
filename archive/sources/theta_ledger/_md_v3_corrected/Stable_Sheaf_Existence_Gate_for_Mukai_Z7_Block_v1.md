---
abstract: |
  We close the stable-object existence gate for the positive Mukai Z_7 block.
  On a Picard-rank-one K3 surface with H^2=2, the Mukai vectors
  a=(5,H,0) and b=(7,3H,1) are primitive, have positive rank, and have
  Mukai squares 2 and 4.  Standard K3 stable-sheaf theory implies that, for a
  v-general polarization, the moduli spaces of stable sheaves with these
  primitive Mukai vectors are nonempty irreducible holomorphic symplectic
  manifolds of dimensions 4 and 6.  Thus the selected determinant-seven Mukai
  block is not merely formal lattice arithmetic: its two charge vectors are
  individually realized by stable K3 sheaf sectors.  This does not yet prove a
  single common-slope HYM polystable bundle, Fu-Yau anomaly compatibility, or
  MTT selection of the block; those remain separate gates.
author:
- Peter Nero
date: May 2026
title: |
  Stable-Sheaf Existence Gate for the Mukai Z7 Block
---

# Purpose

The positive Mukai block:

```text
a = (5,H,0),
b = (7,3H,1),
H^2=2
```

gave:

```text
K_Mukai =
[[2,1],
 [1,4]],
det K_Mukai = 7,
SNF(K_Mukai)=[7].
```

The remaining question at this layer was whether `a` and `b` are only formal
Mukai lattice vectors or can be realized by stable K3 sheaf sectors.

# Mukai Data

Use the K3 Mukai pairing:

```text
<(r,c,s),(r',c',s')> = c.c' - r s' - r' s.
```

For:

```text
a=(5,H,0),
b=(7,3H,1),
H^2=2,
```

we get:

```text
<a,a>=2,
<a,b>=1,
<b,b>=4.
```

Both vectors are primitive:

```text
gcd(5,1,0)=1,
gcd(7,3,1)=1.
```

Both have positive rank:

```text
r(a)=5,
r(b)=7.
```

Their expected stable-sheaf moduli dimensions are:

```text
dim M_H(a) = <a,a> + 2 = 4,
dim M_H(b) = <b,b> + 2 = 6.
```

# Stable-Sheaf Existence Theorem

Standard K3 stable-sheaf theory says that for a primitive Mukai vector `v` on
a projective K3 surface and a `v`-general polarization, the stable-sheaf moduli
space is a nonempty irreducible holomorphic symplectic manifold when the Mukai
square is in the allowed range.  This is the theorem package used by Mukai,
O'Grady, Huybrechts, and Yoshioka.

Reference anchors:

```text
Kota Yoshioka, Irreducibility of moduli spaces of vector bundles on K3
surfaces, arXiv:math/9907001.

Justin Sawon, Moduli spaces of sheaves on K3 surfaces, arXiv:1603.00785.
```

The two selected vectors satisfy the hypotheses:

```text
a primitive, a^2=2;
b primitive, b^2=4.
```

Therefore stable sheaf sectors with Mukai vectors `a` and `b` exist for a
generic compatible polarization.

# Theorem: Stable-Object Gate Closed

For the Picard-rank-one K3 sector with `H^2=2`, the Mukai vectors:

```text
a=(5,H,0),
b=(7,3H,1)
```

are individually realized by stable K3 sheaves in the standard K3
stable-sheaf moduli theory.

Consequently, the determinant-seven Mukai block is not just a formal lattice
block.  It is a stable-object charge block.

# What This Does Not Prove

This does not undo the earlier same-slope obstruction.  The slopes are:

```text
mu_H(a)=2/5,
mu_H(b)=6/7.
```

So `a` and `b` are not two same-slope summands of one polystable HYM bundle.

The remaining gates are:

```text
1. locally-free/HYM interpretation if the physical construction requires
   honest vector bundles rather than stable torsion-free sheaves;

2. Fu-Yau/Strominger anomaly compatibility for the chosen charge sector;

3. MTT selection of this determinant-seven Mukai block;

4. identification of family-trivial CP labels with Hom(coker K_Mukai,U(1)).
```

# Gate Status

```text
Mukai arithmetic SNF [7]                         PROVED
a,b primitive positive Mukai vectors             PROVED
stable K3 sheaf sectors for a,b                  PROVED
single common-slope HYM polystable bundle        OBSTRUCTED
locally-free/HYM physical interpretation         OPEN
Fu-Yau anomaly compatibility                     OPEN
MTT selection of this Z_7 block                  OPEN
CP character-identification                      OPEN
```

# Bottom Line

The `Z_7` side advances one step:

```text
formal Mukai lattice block -> stable K3 sheaf charge block.
```

The remaining `Z_7` work is no longer stable-object existence.  It is
Fu-Yau compatibility, physical interpretation, and MTT selection.
