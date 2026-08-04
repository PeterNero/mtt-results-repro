---
abstract: |
  We isolate the most serious rigor issue in the Lens-Nil Z_7 route: the
  curvature appendix displays the determinant-seven reduced block
  [[2,1],[1,4]], but writes the curvature coefficients with
  O(lambda^2 nu^2) terms.  A finite quotient cannot be derived from approximate
  real coefficients.  The final proof must show that the exact integral
  period/differential-character relation matrix is GL(2,Z)-equivalent to
  [[2,1],[1,4]], or that the correction terms are invisible to the fixed
  arithmetic character projection.  This note gives the acceptable proof modes,
  the failure modes, and the next computation needed.
author:
- Peter Nero
date: May 2026
title: |
  Integer-Block Protection Strategy for the Lens-Nil Z_7 CP Row
---

# Problem

The Lens-Nil coefficient appendix gives the promising reduced fingerprint:

```text
W_1 = 2 lambda^2 R^2,
W_3 = lambda nu R^2,
A   = 4 lambda^2 + O(lambda^2 nu^2),
B   = 4 nu^2     + O(lambda^2 nu^2).
```

The determinant-seven block:

```text
K_0 =
[2 1
 1 4]
```

has:

```text
det(K_0)=7,
SNF(K_0)=[7].
```

But this does not prove the CP row by itself.

A finite abelian quotient is an exact arithmetic object.  It cannot be derived
from approximate real coefficients unless one proves that the approximation is
not part of the integral relation matrix.

# Failure mode

If the correction terms change the integer relation matrix, the sevenfold
factor is generally destroyed.

Examples:

```text
[3 1      det=11
 1 4]

[2 1      det=9
 1 5]

[2 2      det=4
 2 4]
```

So it is not enough to say:

```text
the corrections are small.
```

Small analytic corrections can be irrelevant to metric stability while still
fatal to exact torsion arithmetic.

# Acceptable proof modes

The final proof can protect the integer block in any one of three ways.

## Mode 1: exact period computation

Compute the exact full Chern-Weil/Bianchi period matrix on the fixed Lens-Nil
integral component basis:

```text
P_ij = integral over C_i of component_j
```

including all curvature terms.  Then prove:

```text
SNF(P)=[7],
```

or:

```text
P is GL(2,Z)-equivalent to [[2,1],[1,4]].
```

This is the strongest route.

## Mode 2: differential-cohomology protection

Prove that the `O(lambda^2 nu^2)` pieces change only the real representative
inside a fixed differential-cohomology class.  Equivalently, they are exact,
gauge, or representative-level terms that do not alter the integral character
quotient.

Then the integral matrix remains:

```text
K_LN = [[2,1],[1,4]]
```

inside the fixed sector.

## Mode 3: character-projection annihilation

Define the fixed arithmetic character projection:

```text
P_char: invariant component data -> Lambda_LN,Z.
```

Then prove:

```text
P_char(O(lambda^2 nu^2) terms) = 0
```

or that the projected exact relation matrix is GL(2,Z)-equivalent to `K_0`.

This is plausible if the correction terms belong to continuous metric/radius
matching equations rather than to the discrete flat-character quotient.

# Recommended next computation

The next technical calculation should not be another numerical phase fit.

It should be:

```text
Exact Lens-Nil period/differential-character matrix computation.
```

Concretely:

```text
1. write the full torsionful curvature R_+ in the Lens x Nil coframe;
2. compute Tr_grav R_+^2 exactly, not with O-notation;
3. pair dH, Tr F^2, and Tr R_+^2 with the integral component chains/cycles or
   differential-character test objects selected by the fixed sector;
4. reduce the resulting integer matrix by Smith normal form;
5. accept the Z_7 proof only if the protected matrix has SNF [7].
```

# Consequence for the papers

Statements should now say:

```text
The Lens-Nil appendix contains a determinant-seven reduced fingerprint.
```

They should not say:

```text
The appendix already proves an exact Z_7 relation matrix.
```

The final theorem should be conditional until the protection lemma is proved.

# Current conclusion

The correct state is:

```text
Z_7 is strongly motivated by the Lens-Nil reduced block,
formally proved if that block is protected in the fixed arithmetic sector,
but not yet unconditionally proved from the existing O-notation appendix.
```

That is a useful outcome.  It turns the remaining work into a precise
calculation rather than an open-ended search.

