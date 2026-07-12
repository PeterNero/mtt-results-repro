---
abstract: |
  We identify a concrete sevenfold fingerprint inside the existing Lens x Nil
  corpus.  The heterotic Lens x Nil coefficient appendix gives
  W_1=2 lambda^2 R^2, W_3=lambda nu R^2, and leading torsional spin-curvature
  coefficients A=4 lambda^2+O(lambda^2 nu^2), B=4 nu^2+O(lambda^2 nu^2).
  The reduced integer fingerprint [[2,1],[1,4]] has determinant seven and
  Smith normal form Z_7.  This does not yet prove the CP row, because one must
  still derive the map from componentwise Bianchi coefficients to Wilson/nil
  character relations and prove that the higher-order curvature terms do not
  change the fixed-sector integer block.  But it is the first MTT-native
  fingerprint explaining where the missing seven could come from without
  inserting 7 by hand.
author:
- Peter Nero
date: May 2026
title: |
  Lens-Nil Coefficient Fingerprint for the Sevenfold CP Row
---

# Purpose

The previous note found that a primitive two-row block:

```text
[2 1
 1 4]
```

has:

```text
det = 7,
SNF = [7].
```

This note checks whether the actual MTT Lens x Nil corpus contains the same
integer fingerprint.

# Lens x Nil coefficient facts

In the heterotic Lens x Nil construction, the internal space is:

```text
X_6 = L(3,1) x (Gamma \ Nil_3).
```

With:

```text
d eta_i    = lambda epsilon_ijk eta_j wedge eta_k,
d sigma_6  = nu sigma_4 wedge sigma_5,
```

the coefficient appendix gives:

```text
dH = W_1 beta_1 + W_3 beta_3,
W_1 = 2 lambda^2 R^2,
W_3 = lambda nu R^2.
```

For torsional spin curvature:

```text
Tr_grav R_+^2 = A beta_1 + B beta_3,
A = 4 lambda^2 + O(lambda^2 nu^2),
B = 4 nu^2 + O(lambda^2 nu^2).
```

Thus the reduced leading coefficient pattern is:

```text
2, 1, 4.
```

# Determinant-seven block

The natural primitive symmetric block built from these coefficients is:

```text
K_LN =
[2 1
 1 4].
```

Its determinant is:

```text
2*4 - 1*1 = 7.
```

Smith normal form gives:

```text
Tor coker(K_LN) ~= Z_7.
```

Equivalently, if the componentwise Lens x Nil equations descend to character
relations:

```text
2w + n  = 0,
w  + 4n = 0,
```

then elimination gives:

```text
7w = 0,
7n = 0.
```

# Reproducible check

The executable check is:

```text
lens_nil_seven_fingerprint_check.py
```

It reports:

```text
primitive coefficient block
  matrix: [[2, 1], [1, 4]]
  determinant: 7
  torsion factors: [7]
  exponent: 7
  free rank: 0
```

Combining this block with the six-stage dyadic carry gives:

```text
torsion factors: [448]
exponent: 448
free rank: 0
```

Adding family `Z_3` gives:

```text
torsion factors: [1344]
exponent: 1344
free rank: 0
```

# Why this matters

This is materially stronger than the previous situation.

Previously, the sevenfold row was an algebraic target:

```text
derive Z_7 somehow.
```

Now the determinant-seven integer fingerprint is present in the MTT
Lens x Nil construction already used for theta closure:

```text
W_1 coefficient: 2,
mixed W_3 coefficient: 1,
leading R_+ coefficient: 4.
```

The seven therefore need not come from:

```text
an L(7,*) lens space,
a seven-dimensional carrier,
a literal order-seven Wilson line stated in the corpus,
or phenomenological CKM fitting.
```

It can come from:

```text
determinant of the primitive Lens-Nil coefficient block.
```

The caveat is essential: the appendix writes `A` and `B` with
`O(lambda^2 nu^2)` corrections.  A final proof must show that these corrections
either vanish in the fixed arithmetic character projection, are absorbed into
continuous metric/radius equations, or leave an exact GL(2,Z)-equivalent
integer relation block.

# What is not yet proved

The fingerprint is not yet a theorem.

The missing map is:

```text
componentwise Bianchi/flux coefficients
        ->
integer relations on residual Wilson/nil CP character labels.
```

We must show that the same primitive block governing:

```text
beta_1, beta_3 component closure
```

also governs the finite residual phase labels:

```text
w, n.
```

Until that map is derived, the result is a strong structural clue, not a final
proof.

# Correct proof target

The next theorem should state something like:

```text
Under the coherent projector, the family-trivial residual CP phase labels
(w,n) inherit the primitive Lens-Nil component matrix
K_LN = [[2,1],[1,4]]
from the invariant Bianchi system.
```

Then:

```text
SNF(K_LN) = [7],
```

so:

```text
Gamma_7 ~= Z_7.
```

Combining with the dyadic carry:

```text
Z_64 x Z_7 ~= Z_448.
```

and adding the family row:

```text
Z_64 x Z_7 x Z_3 ~= Z_1344,
```

with selected CP quotient:

```text
Z_1344 / Z_3-family ~= Z_448.
```

# Bottom line

This is the best concrete sevenfold lead so far:

```text
the missing seven appears as det [[2,1],[1,4]]
inside the actual Lens x Nil coefficient system.
```

The remaining task is not to search the corpus for `Z_7`.  It is to prove that
the Lens x Nil coefficient block descends to the residual Wilson/nil CP
character relation block.
