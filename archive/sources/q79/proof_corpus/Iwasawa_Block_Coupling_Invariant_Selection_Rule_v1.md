---
abstract: |
  We compute the finite qutrit invariant-pairing rule required by the
  block-factorized Iwasawa twist packet.  With the Higgs kept as a trivial
  rank-one line, an SM Yukawa pair is invariant only when the two matter
  projective orientations are conjugate, with twist exponents summing to zero
  modulo three.  The same-twist assignment for all family sectors is therefore
  blocked for ordinary SM Higgs couplings, while conjugate left/right
  assignments pass the finite invariant-count test.  This formulates the
  coupling rule but does not select the orientation assignment or compute
  Yukawa magnitudes.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Block Coupling Invariant Selection Rule
---

# Setup

Let `V_s` be a qutrit projective block with twist orientation `s in Z/3`.
The diagonal finite generators on `V_s tensor V_t` are:

```text
X_pair = X tensor X,
Z_pair = Z^s tensor Z^t.
```

For a trivial Higgs line, an SM Yukawa operator reduces at this finite level to
a matter-pair invariant:

```text
Q u H, Q d H, L e H, L N H
```

with `H` contributing no qutrit phase.

# Pair Invariant Count

The fixed dimensions are:

```text
0+0 -> 3
0+1 -> 0
0+2 -> 0
1+0 -> 0
1+1 -> 0
1+2 -> 1
2+0 -> 0
2+1 -> 1
2+2 -> 0
```

Thus the nontrivial allowed matter-pair orientations are exactly:

```text
1+2, 2+1.
```

Equivalently, the trivial-Higgs finite rule is:

```text
s_left + s_right = 0 mod 3.
```

# SM Consequence

The same-twist assignment

```text
Q,u,d,L,e,N all have orientation 1
```

gives zero fixed dimension for all four ordinary SM Yukawa pairs.

The conjugate-right assignment

```text
Q,L have orientation 1,
u,d,e,N have orientation 2
```

gives fixed dimension one for:

```text
Q u, Q d, L e, L N.
```

The conjugate-left assignment with orientations reversed also passes.

# E6 Cubic Comparison

For a three-factor cubic, the same nonzero orientation can be invariant:

```text
1+1+1 = 0 mod 3,
fixed_dimension = 3.
```

This explains why a high-scale three-family or E6-like cubic can coexist with a
different low-energy SM Higgs-pairing rule.  Once the Higgs is projected to a
separate trivial line, ordinary SM Yukawa pairs need conjugate matter
orientations.

# Status

This closes a finite coupling rule, not a selected coefficient theorem.
Still open:

```text
MTT-selected sector orientation assignment,
selected D_E and dotD on oriented factorized blocks,
primitive C1 contractions,
Yukawa magnitudes and kinetic/RG matching.
```
