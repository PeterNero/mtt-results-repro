---
title: "Visible Rank-Two L2 Appell-Humbert Automorphy Source Attempt"
version: v1
---

# Visible Rank-Two `L^2` Appell-Humbert Automorphy Source Attempt

## Purpose

The previous packet reduced the integral-lift branch to a selected source
certificate for the ordered ordinary Chern matrix:

```text
E(g1,g2)= 2,
E(g3,g4)=-4,
E(g5,g6)= 0.
```

This note tests whether the missing object is still the existence of an
automorphy representative, or the MTT selection of that representative.

## Construction

On the standard Gaussian base torus:

```text
E1 x E2 = C/(Z+iZ) x C/(Z+iZ)
```

take degree vector:

```text
(d1,d2,d3)=(2,-4,0).
```

For a deck element:

```text
gamma=(m1,n1,m2,n2,m3,n3),
```

the normalized Appell-Humbert/theta multiplier is:

```text
a(gamma,z)
 = prod_{j=1}^2 exp(-pi*i*d_j*n_j^2*i - 2*pi*i*d_j*n_j*z_j).
```

The central/shared-circle pair has degree zero and therefore contributes no
ordinary line-bundle Chern class.

## Checks

The script checks:

```text
cocycle law holds modulo 2*pi*i*Z,
c1 matrix is the ordered target matrix,
E(g1,g2)= 2,
E(g3,g4)=-4,
E(g5,g6)= 0,
mixed base terms vanish,
central/shared-circle terms vanish.
```

Because all pairings are even, the trivial semicharacter is mathematically
consistent.  This gives a neutral Pic0 representative, but it does not prove
that MTT selects the neutral Pic0 representative.

## What This Closes

The selected-source problem is sharper now:

```text
explicit non-flat automorphy representative exists,
ordinary integral c1 matrix is realized,
finite torsion gerbe is not being reused as ordinary c1,
shared circle is retained with zero degree,
trivial semicharacter is allowed for this even matrix.
```

So the remaining gap is not an automorphy-existence gap.

## What Remains Open

The open selection theorem is:

```text
MTT selects Gamma0 or an equivalent lattice,
MTT selects L=(1,-2,0) over the swapped branch,
MTT selects or eliminates flat Pic0 twists,
the same selected source is the visible V_alpha branch,
the selected source supplies the Ext class, stability, D_E, dotD, Riesz, and Green data.
```

## Verdict

The ordered `L^2` source now has a concrete Appell-Humbert representative.  It
does not yet have an MTT selection proof.  The next proof attempt should derive
branch/neutral-Pic0 selection from the MTT Hessian, Gauduchon wall, or the
same-source Strominger/HYM functional, then promote the existing `h1=8` packet
without changing its cohomology by hand.
