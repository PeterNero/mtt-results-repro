---
abstract: |
  We search the Strings/Flux/M-theory corpus for a replacement source of the
  missing Z_7 factor after the original Lens-Nil appendix fails exterior
  calculus checks.  The strongest new clue is the Fu-Yau/K3 flux slice.  The
  corpus already supplies a K3 base, fixed topological data, stable holomorphic
  bundles, Li-Yau HYM existence on Gauduchon metrics, and MTT fixed-sector
  selection.  The K3 integral lattice contains a primitive rank-two sublattice
  with Gram matrix [[-2,-1],[-1,-4]], whose negative is exactly
  [[2,1],[1,4]] and has Smith normal form [7].  This gives a cleaner candidate
  source for the Z_7 CP row than the broken Lens-Nil coefficient block, but it
  still requires a bundle-realization and MTT-selection theorem.
author:
- Peter Nero
date: May 2026
title: |
  Fu-Yau/K3 Determinant-Seven Flux Candidate for the MTT CP Row
---

# Why this candidate matters

The Lens-Nil route found a determinant-seven matrix, but the source formulas
were not exterior-calculus consistent.  The Fu-Yau/K3 material in the
Strings/Flux/M-theory folder gives a better kind of source:

```text
fixed topological sector,
integral cohomology lattice,
stable holomorphic bundles,
Li-Yau HYM existence,
Strominger/Fu-Yau admissible flux slice.
```

This is exactly the environment needed for an arithmetic CP quotient.

# Corpus clues

The Strominger/Heterotic Flux paper states:

```text
Fu-Yau class = principal T^2 bundle over K3,
fixed topological data,
stable holomorphic bundle,
Li-Yau HYM connection,
MTT selection in a fixed topological sector.
```

The M-theory paper adds:

```text
topological sector fixes an integral cohomology lattice,
shifted flux quantization,
4D data determined by harmonic/integral lattice and flux class.
```

So the search target should be:

```text
an exact determinant-seven block in an integral K3/Fu-Yau flux or bundle lattice.
```

# Exact K3 lattice block

Use a copy of:

```text
U^2 subset H^2(K3,Z),
```

with basis:

```text
(e1,f1,e2,f2),
e_i . f_i = 1,
e_i^2 = f_i^2 = 0.
```

Define:

```text
v = -e1 - e2 + f2,
w =  e1 - f1 - e2 + f2.
```

In coordinates `(e1,f1,e2,f2)`:

```text
v = (-1,  0, -1, 1),
w = ( 1, -1, -1, 1).
```

Then:

```text
v^2 = -2,
w^2 = -4,
v.w = -1.
```

The Gram matrix is:

```text
G =
[-2 -1
 -1 -4].
```

Therefore:

```text
K := -G =
[2 1
 1 4].
```

Smith normal form:

```text
SNF(K) = [7].
```

So:

```text
Hom(coker K, U(1)) ~= Z_7.
```

# Why this is better than the Lens-Nil coefficient block

This first candidate lives in an actual integral cohomology lattice from the
start:

```text
H^2(K3,Z).
```

The determinant-seven matrix is not an approximate curvature coefficient and
does not depend on non-closed component forms.  It is an exact intersection
matrix.

It also aligns with HYM better.  On K3/Fu-Yau, one can aim to choose a complex
structure in which this negative definite rank-two lattice lies in the Picard
lattice and a polarization orthogonal to it.  Then the corresponding line
classes have slope zero; more generally, stable bundles with prescribed Chern
classes admit HYM connections by Li-Yau on the Gauduchon metric.

This line-bundle sentence needs a caveat.  The later gate check shows that
`v^2=-2`, so the naive polarization orthogonal to `v` sits on a K3 root wall
if `v` is effective.  Therefore the safe route is not "two immediate line
bundles."  The safe route is a stable higher-rank/Mukai-lattice realization or
a direct fixed charge-lattice interpretation.

The next correction is stronger.  Any even rank-two determinant-seven K3
`H^2` block represents norm `2` after lattice reduction, so the root-wall issue
is structural for the direct anti-self-dual curvature-pair route.  The live
replacement is now the positive Mukai charge block:

```text
H^2=2,
a=(5,H,0),
b=(7,3H,1),
Gram_Mukai(a,b)=[[2,1],[1,4]],
SNF=[7].
```

This keeps the exact `Z_7` quotient but moves it into the full algebraic Mukai
charge lattice, where standard K3 stable-sheaf theory is the correct existence
input.

# What is still open

This is not yet a finished proof.

Needed lemmas:

```text
1. Mukai realization:
   realize the positive Mukai vectors a=(5,H,0), b=(7,3H,1) in an admissible
   Fu-Yau/K3 base.

2. HYM/bundle realization:
   construct or cite stable sheaf/bundle representatives whose Mukai charge
   pairing is exactly K=[[2,1],[1,4]], and settle whether the physics requires
   locally free bundles rather than stable torsion-free sheaves.

3. Bianchi/Fu-Yau compatibility:
   show this topological data can be included in the Fu-Yau anomaly equation
   with the chosen tangent-bundle contribution and gerbe class.

4. CP character identification:
   identify the family-trivial CP labels with the unitary character group
   Hom(coker K,U(1)).

5. Selection:
   prove the MTT fixed-sector selection picks this determinant-seven block,
   rather than merely allowing it.
```

# Current status

The executable check is:

```text
fu_yau_k3_det7_candidate_check.py
```

It proves:

```text
K3 lattice contains an exact determinant-seven block,
K = [[2,1],[1,4]],
SNF(K)=[7].
```

The main open work is now bundle/Fu-Yau realization and MTT selection.

The next gate check is:

```text
K3_Picard_Realization_and_HYM_Gates_for_Det7_CP_v1.md
```

It confirms primitive lattice realization and a positive orthogonal class, but
it rejects the naive zero-slope line-bundle proof because of the K3 `(-2)` root
wall.

The corrected successor note is:

```text
Mukai_Positive_Charge_Block_for_Fu_Yau_K3_Z7_CP_v1.md
```

with check:

```text
mukai_positive_det7_charge_block_check.py
```

It records the current strongest version of the Fu-Yau/K3 `Z_7` candidate.

# Role in the full CP proof

If the Fu-Yau/K3 candidate is selected, then the odd factor becomes:

```text
Gamma_7 ~= Z_7.
```

Combined with the dyadic carry:

```text
Gamma_CP,min ~= Z_64 x Z_7 ~= Z_448.
```

The family factor remains:

```text
Gamma_amb ~= Z_64 x Z_7 x Z_3 ~= Z_1344,
Gamma_amb / Z_3-family ~= Z_448.
```

This is currently the cleanest replacement for the broken Lens-Nil `Z_7`
source.
