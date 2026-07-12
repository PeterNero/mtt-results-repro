---
abstract: |
  We refine the sevenfold proof target.  The corpus does not supply an explicit
  Z_7, L(7,*), or row 7w=0.  But it does supply the right kind of structure:
  Lens x Nil has two independent componentwise anomaly equations, integer
  flux labels, and discrete invariant loci.  A primitive 2x2 integer relation
  block coupling Wilson and nil/circle labels can have determinant seven even
  when no row literally contains the integer seven.  In that case Smith normal
  form gives Z_7, and elimination derives 7w=0 and 7n=0.  This is now the best
  rigorous route: derive a determinant-seven Lens-Nil compatibility block from
  the componentwise Bianchi/Wilson/projector equations.
author:
- Peter Nero
date: May 2026
title: |
  Primitive Determinant-Seven Lens-Nil Block for the MTT CP Character
---

# Purpose

The previous notes treated the sevenfold row as:

```text
7w = 0
```

or:

```text
7n = 0.
```

That is algebraically correct but too blunt.  It risks making the seven look
inserted by hand.

The better question is:

```text
Can MTT derive two small integer Lens-Nil/Wilson compatibility rows whose
primitive determinant is seven?
```

If yes, the sevenfold row appears after elimination rather than as an
assumption.

# Corpus clues

The corpus gives four relevant ingredients.

First, the proto-spinor carrier dictionary identifies:

```text
Circle carrier C: return-consistency bookkeeping,
Lens carrier L: redundancy/gauge transport,
Nil carrier N: holonomy-aware termination and discrete survivorship.
```

Second, quantization is explicitly treated as:

```text
Circle phase closure
+ Lens bundle consistency
+ Nil sector survival.
```

Third, the Lens x Nil heterotic/flux papers give an actual two-component
integer structure.  In the left-invariant sector, FCC reduces to a finite
componentwise anomaly system, and for Lens x Nil:

```text
two independent Bianchi components fix R_1/R for integer (f,h).
```

Fourth, the same papers stress that the resulting Lens x Nil loci are discrete
because of:

```text
topological constraints,
differential constraints,
coherence admissibility.
```

This is exactly the environment in which a finite character row should be
derived.

# Primitive determinant-seven mechanism

Let `w` be a Wilson/circle phase label and `n` a nil survivor or nil-lock label.
Suppose MTT derives two independent integer compatibility rows:

```text
a w + b n = 0,
c w + d n = 0.
```

The relation matrix is:

```text
M = [ a  b
      c  d ].
```

If:

```text
gcd(a,b,c,d)=1,
det(M)=ad-bc = +/-7,
```

then Smith normal form gives:

```text
coker(M) ~= Z_7.
```

The sevenfold row is then a consequence:

```text
d*(a w+b n) - b*(c w+d n) = det(M) w = 0,
-c*(a w+b n) + a*(c w+d n) = det(M) n = 0.
```

Thus:

```text
7w=0,
7n=0
```

are derived rows, not primitive assumptions.

# Minimal example

The script:

```text
primitive_determinant_seven_block_scan.py
```

finds many small primitive blocks.  One clean nonnegative example is:

```text
2w + n  = 0,
w  + 4n = 0.
```

The matrix is:

```text
[2 1
 1 4]
```

with:

```text
det = 7,
SNF = [7].
```

Elimination gives:

```text
4*(2w+n) - (w+4n) = 7w = 0,
-(2w+n) + 2*(w+4n) = 7n = 0.
```

So this block is mathematically equivalent to a sevenfold finite row, but its
input coefficients are only:

```text
1,2,4.
```

That matters.  It means the MTT proof need not find a literal seven in the
corpus.  It can find a primitive determinant-seven compatibility block.

# Coefficient fingerprint in the actual Lens x Nil corpus

The determinant-seven block is not arbitrary.  The existing Lens x Nil
coefficient appendix gives the reduced leading pattern:

```text
W_1 = 2 lambda^2 R^2,
W_3 = lambda nu R^2,
A   = 4 lambda^2 + O(lambda^2 nu^2),
B   = 4 nu^2     + O(lambda^2 nu^2).
```

The integers appearing in the visible reduced block are:

```text
2, 1, 4.
```

They form the primitive block:

```text
[2 1
 1 4],
```

whose determinant is:

```text
2*4 - 1*1 = 7.
```

This does not yet prove the sevenfold CP row, but it changes the proof target.
The task is now to derive the map from the Lens x Nil Bianchi coefficient
system to the residual Wilson/nil character relations.  If that map preserves
an exact fixed-sector integer block GL(2,Z)-equivalent to this primitive block,
the sevenfold row follows by Smith normal form.

# Combined quotient

When this block is combined with the six-stage dyadic carry:

```text
Z_64 from recursive shared-circle carry,
Z_7  from primitive Lens-Nil determinant block,
```

the script reports:

```text
torsion factors: [448]
exponent: 448
free rank: 0
```

Adding the family `Z_3` row gives:

```text
torsion factors: [1344]
exponent: 1344
free rank: 0
```

The selected CP character remains the family-trivial quotient:

```text
Z_1344 / Z_3-family ~= Z_448.
```

# Why this is better than the previous seven templates

The previous templates were:

```text
7w=0,
7n=0,
n-7c=0 plus terminal closure.
```

Those are still valid as algebraic normal forms.  But the determinant-block
route is more faithful to the actual MTT corpus because the corpus already has:

```text
two componentwise Lens x Nil equations,
integer flux data,
discrete invariant selection,
Wilson/circle phase labels,
nil survivor labels.
```

The proof target becomes:

```text
derive the two rows and compute their determinant.
```

not:

```text
find a sentence saying order seven.
```

# What must be derived next

The required theorem should have this shape.

Let:

```text
w = residual family-trivial Wilson/circle CP character,
n = holonomy-aware nil survivor label.
```

From the Lens x Nil componentwise anomaly equations, flux quantization, and
coherent-projector compatibility, derive a primitive integer block:

```text
M_LN =
[ a  b
  c  d ].
```

Then prove:

```text
gcd(a,b,c,d)=1,
abs(det M_LN)=7.
```

This immediately gives:

```text
Tor coker(M_LN) ~= Z_7.
```

# Failure modes

This candidate fails if:

```text
the two Lens x Nil rows are not independent,
the determinant is 1, 2, 3, 4, 5, 6, or a multiple incompatible with CKM,
the block is imprimitive and reduces to a smaller torsion factor,
the Wilson/nil labels do not couple to the CP overlap character,
or the resulting character is not family-trivial.
```

It also fails if the only way to obtain determinant seven is to tune flux
integers using the CKM value itself.  The block must be derived from MTT
selection/admissibility data before CKM fitting.

# Bottom line

The most promising sevenfold route is now:

```text
Do not assume 7w=0.
Derive a primitive 2x2 Lens-Nil/Wilson block with determinant seven.
```

This is a sharper and more natural proof target than the earlier pure-row
templates, and it fits the existing Lens x Nil corpus without violating the
circle/lens/nil setup.
