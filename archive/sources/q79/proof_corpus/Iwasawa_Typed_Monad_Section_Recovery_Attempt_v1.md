# Iwasawa Typed Monad Section Recovery Attempt

## Purpose

The previous way-forward note selected the typed monad/Cech route as the
primary path and the non-invariant spectral Galerkin route as fallback. This
note executes the first part of that decision: it asks whether the current
corpus actually contains the typed monad sections needed to run the Cech
computation.

The answer is no. The corpus contains the topological monad data and the
generic-map assertion, but not the typed section representatives, transition
data, Cech cover, or line-bundle cohomology tables needed to compute
`H^1(X,E)`.

## What Was Recovered

From the heterotic flux source we can recover:

```text
0 -> K1 -> direct_sum_i L_i -> K2 -> 0,
E = ker(g) / im(f),
```

with Chern labels:

```text
L1 = -2 a + 0 b + 1 c
L2 = -1 a + 1 b - 1 c
L3 =  1 a - 1 b + 0 c
L4 =  1 a + 0 b - 1 c
L5 =  2 a + 1 b + 1 c
K1 =  1 a + 0 b + 0 c
K2 =  0 a + 1 b + 0 c
```

These data still give the topological checks:

```text
c1(E) = 0,
c2(E) = 0,
int_X c3(E) = 6.
```

The same source also contains a normalized Iwasawa cubic:

```text
lambda_123 = 1
```

after chiral rephasing. That rank-one seed remains valid as a seed. It is not
a three-family basis.

## What Was Not Recovered

The corpus does not provide:

```text
f_i section representatives,
g_i section representatives,
transition functions for L_i,K1,K2,
Cech cover/cocycle data,
line-bundle cohomology tables,
g o f = 0 as a typed section identity,
monad exactness or controlled sheaf singularity data,
long exact sequence maps,
selected H^1(X,E) representatives,
anti-family middle-cohomology vanishing,
sector projections Q,u,d,L,e,N,H,
dotD_alpha1 and reduced Green operators.
```

This is not a cosmetic absence. These are exactly the data needed to upgrade
the net index into actual selected zero modes.

## Why The Generic-Map Phrase Does Not Close It

The source says that for generic holomorphic maps `f,g` in the monad,
parenthetically described as constant matrices in the left-invariant frame, the
bundle is indecomposable.

But the map entries have types:

```text
f_i in H^0(X, L_i tensor K1^{-1}),
g_i in H^0(X, K2 tensor L_i^{-1}).
```

For the listed line bundles, the Hom Chern labels are:

```text
f1: (-3,  0,  1)
f2: (-2,  1, -1)
f3: ( 0, -1,  0)
f4: ( 0,  0, -1)
f5: ( 1,  1,  1)

g1: ( 2,  1, -1)
g2: ( 1,  0,  1)
g3: (-1,  2,  0)
g4: (-1,  1,  1)
g5: (-2,  0, -1)
```

None is zero. Therefore a nonzero scalar constant entry is not automatically a
global typed map. It can only be accepted if the missing global section or
transition-function convention is supplied.

So the monad/Cech route remains mathematically primary, but it is data-absent
in the current corpus.

## Consequence

The fallback condition from the previous note is now triggered:

```text
typed monad/Cech route: primary but currently unfillable from corpus,
non-invariant spectral Galerkin route: next executable path.
```

The next artifact should not be another sparse invariant A01 scan. That branch
has already shown the obstruction: retaining the torsion form `e3` in the
three-entry invariant ansatz gives `h1=2`, while sparse `h1=3` candidates drop
`e3` and are not selected.

## Spectral Fallback Contract

The fallback must construct the cohomology by operator data rather than by
guessed invariant representatives. It must supply:

```text
selected operator D_E on the Iwasawa/Strominger branch,
finite basis extending beyond left-invariant forms,
matrix representation of the bundle Laplacian or Dirac/Dolbeault Laplacian,
low spectrum and Riesz projector,
kernel dimension = 3,
anti-family modes absent or controlled,
positive complement gap,
truncation-error bound,
explicit Psi_1,Psi_2,Psi_3,
L2 Gram matrix and horizontal gauge,
sector projections Q,u,d,L,e,N,H,
dotD_alpha1,
reduced Green operator,
E6 cubic or overlap tensor.
```

This feeds the existing selected cohomology-data template and then the
zero-mode/dotD interface.

## Verdict

The current corpus does not supply the typed monad maps. The correct next
move is therefore:

```text
build the Iwasawa non-invariant spectral Galerkin operator certificate.
```

This is a forward move, not a defeat. It changes the proof obligation from
"find a hidden formula in the prose" to "construct a finite, auditable spectral
operator calculation with an error certificate."
