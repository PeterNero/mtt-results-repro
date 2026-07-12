# Index-to-Three-Family Upgrade Gate for the Iwasawa Bundle

## Purpose

The Iwasawa flux source contains two nearby but mathematically different
claims:

```text
int_X c3(E) = 6,
```

which supports a net chirality/index count of three, and

```text
Psi_i in H^1(X,E), i=1,2,3,
```

which assumes three selected bundle-valued zero-mode representatives.

This note separates those statements.  The first is topological.  The second
requires cohomology computation.

## What the Index Gives

For an SU(3) bundle on the complex-parallelizable Iwasawa threefold, the source
uses

```text
c1(E)=0,
c2(E)=0,
int_X c3(E)=6.
```

Since the tangent bundle is holomorphically trivial in the source model, the
Todd-class correction is trivial in the invariant topological calculation.
Thus the holomorphic Euler characteristic is controlled by the third Chern
character.  Up to the orientation/convention used to identify particles versus
conjugates, this fixes a net difference:

```text
number of families - number of antifamilies = 3.
```

Equivalently, in sheaf-cohomology language, after the usual stable SU(3)
vanishing of endpoint groups, the index fixes the difference between the
middle cohomology dimensions, not each dimension separately.

## What It Does Not Give

The index alone does not prove

```text
h^1(X,E) = 3.
```

It also does not provide:

```text
orthonormal harmonic representatives Psi_1,Psi_2,Psi_3,
sector projections into Q,u,d,L,e,N,H,
L2 metrics,
projectors and Green operators,
dotD along selected C1 alpha_1,
Yukawa matrices.
```

The missing cohomology upgrade is the vanishing of the conjugate-family group.
In common heterotic notation this is the requirement that the anti-generation
cohomology vanish; by Serre duality on a trivial-canonical threefold this is
equivalent to the corresponding dual middle cohomology vanishing.

## Required Upgrade Lemma

A rigorous three-family basis needs the following finite statement:

```text
Given the selected integrable bundle E on Iwasawa,
H^0(X,E)=0,
H^3(X,E)=0,
the anti-family middle cohomology vanishes,
and the index has absolute value 3.

Therefore the family middle cohomology has dimension 3.
```

Stability can often supply the endpoint vanishings for an irreducible
slope-stable SU(3) bundle.  It does not automatically supply the middle
anti-family vanishing.  That must be computed from the selected Dolbeault or
monad complex.

## Consequence for the Current Proof

The current proof package has:

```text
topological net chirality: supported,
rank-one E6 cubic normalization: supported conditionally on Psi_i,
literal printed A^(0,1): not an integrable complex,
sparse corrected-A01 scan: no selected nearby h1=3 correction,
typed monad route: missing explicit f,g section data.
```

Therefore it is correct to say that the corpus supports a three-net-family
topological target.  It is not yet correct to say that the selected Iwasawa
bundle has produced the three family zero-mode basis needed for no-proxy SM
matrix closure.

## Forward Test

The next successful artifact should output:

```text
h^0(E), h^1(E), h^2(E), h^3(E),
h^1(E*) or the equivalent anti-family cohomology,
explicit representatives for the three selected family modes,
and the pairing/projection data needed by the zero-mode dotD interface.
```

Only after that upgrade can the `Psi_i` used in the normalized cubic be treated
as constructed rather than assumed.
