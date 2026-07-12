# Iwasawa Galerkin Basis Skeleton

## Purpose

The non-invariant Galerkin protocol needs a finite basis `B_N`. We can already
close part of that problem:

```text
the form and rank-three fiber bookkeeping are fixed.
```

What remains open is not the tensor-product shape. It is the scalar
quotient/deck basis and the bundle transition/equivariance data.

## Closed Skeleton

Use basis elements of the form:

```text
phi_m tensor fiber_a tensor baromega_I.
```

Here:

```text
phi_m      = scalar quotient-compatible basis function,
fiber_a    = rank-three bundle fiber label, a=1,2,3,
baromega_I = anti-holomorphic form basis element.
```

The Iwasawa anti-holomorphic form counts are:

```text
degree 0: 1
degree 1: 3
degree 2: 3
degree 3: 1
```

Therefore, for scalar count `s_N`, the degreewise dimensions are:

```text
dim V_N^(0,p) = s_N * 3 * binomial(3,p).
```

The invariant sector is recovered at:

```text
s_N = 1.
```

Its dimensions are:

```text
(3, 9, 9, 3).
```

The first genuinely non-invariant extension must have:

```text
s_N >= 2.
```

For `s_N=2`, the dimensions are:

```text
(6, 18, 18, 6).
```

This is the smallest basis-size jump compatible with adding a non-invariant
scalar slot.

## Two Valid Basis Sources

There are two rigorous ways to fill the scalar part.

### Deck-Equivariant Spectral Basis

This route must supply:

```text
explicit Gamma lattice/deck generators,
scalar mode functions phi_m satisfying quotient equivariance,
derivative/action matrices for left-invariant vector fields,
bundle transition/equivariant matrices for E.
```

This is the cleanest route if the quotient harmonic analysis is available.

### Fundamental-Domain Finite Elements

This route must supply:

```text
fundamental-domain mesh or cell decomposition,
periodic/deck gluing constraints,
quadrature rule for the selected metric/volume,
bundle transition/equivariant matrices for E.
```

This route avoids needing a closed-form scalar Fourier theory on the compact
Iwasawa quotient, but it still needs the deck gluing and bundle equivariance.

## What Is Still Missing

The current corpus supplies the compact quotient and the invariant form
structure, but not:

```text
scalar basis functions phi_m,
deck or periodic constraints,
bundle transition/equivariant matrices,
metric-volume quadrature,
selected D_E action on the basis,
Gram entries,
stiffness entries.
```

Thus we have closed:

```text
form/fiber tensor bookkeeping.
```

We have not closed:

```text
actual non-invariant basis functions B_N.
```

## Guardrail

Do not use raw coordinate functions as non-invariant modes unless they satisfy
the compact quotient/deck identifications. Do not use scalar central-circle
Fourier modes as untwisted zero modes. Do not treat the invariant scalar slot
as a non-invariant basis.

## Verdict

The next concrete missing input is now narrower:

```text
deck-equivariant scalar basis
or
finite-element mesh with deck gluing,
plus bundle transition/equivariance matrices.
```

Once that scalar/bundle data is supplied, the already closed tensor skeleton
turns it into the full `B_N` basis for the selected Galerkin calculation.
