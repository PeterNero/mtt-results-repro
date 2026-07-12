---
title: "VAlpha/S3 Two-Block Source-Selector Reduction"
version: v1
---

# Result

The two-block finite shape is now tied to the integral `V_alpha` route.

The ordered integral Appell-Humbert model for:

```text
L^2 = (2,-4,0)
```

reduces mod `3` to exactly the same rank-four form constructed by the
two-block `S3` finite lift.

# What This Proves

The current selected `S3` deck quotient supplies only one active F3^2 block.
Equivalently, the current selected S3 deck quotient supplies only one active F3^2 block:

```text
g1 -> (1,0)
g2 -> (0,1)
g3 -> (0,0)
g4 -> (0,0)
g5 -> (0,0)
g6 -> (0,0)
```

So the current selected `S3` quotient cannot itself supply the second active
block.  This agrees with the rank obstruction.

The ordered integral model supplies the finite shadow that we need:

```text
E(g1,g2) =  2
E(g3,g4) = -4
E(g5,g6) =  0
```

Modulo `3`, its active `(g1,g2,g3,g4)` block is:

```text
[[0,2,0,0],
 [1,0,0,0],
 [0,0,0,2],
 [0,0,1,0]]
```

which is exactly the two-block finite lift.

# Remaining Selector

The missing object is no longer:

```text
finite compatibility,
ordinary Appell-Humbert existence,
or h1/cohomology arithmetic.
```

Those are closed conditionally or constructively.  The remaining object is a
selected symmetry-breaking source:

```text
selected ordered integral source,
or selected r1:r2=sqrt(2):1 Gauduchon wall,
or same-source D_E/dotD/Hessian data ordering the base factors,
plus Pic0 selection or quotienting.
```

# Guardrail

This does not prove the ordered integral source is selected by MTT.  It proves
that any successful source theorem must supply the second active block through
an ordered integral/geometric source or an equivalent physical quotient, not
through the currently selected single `S3` active quotient alone.
