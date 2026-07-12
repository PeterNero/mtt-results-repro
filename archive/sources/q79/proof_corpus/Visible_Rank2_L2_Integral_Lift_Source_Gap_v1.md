---
title: "Visible Rank-Two L2 Integral Lift Source Gap"
version: v1
---

# Visible Rank-Two `L^2` Integral Lift Source Gap

## Purpose

The visible rank-two route has two live branch selectors:

```text
1. selected Gauduchon wall p1:p2=1:2;
2. selected integral Cech/Deligne/D_E lift to L=(1,-2,0).
```

The previous gate translated the wall route into:

```text
r1:r2 = sqrt(2):1.
```

This note tests the second route.

## Finite Quotient No-Go

The target and swapped branches are:

```text
target:  L=( 1,-2,0)
swapped: L=(-2, 1,0)
```

They have the same finite signatures:

```text
L mod 3       = (1,1,0),
L^2 mod 3     = (2,2,0),
xy            = -2,
B_1(L,L)      = 2/3,
h1 pullback   = 8,
c2 extension  = +4 alpha_1.
```

Therefore no proof that uses only the selected `F_3^2` qutrit quotient can
distinguish them.  The finite q79/F orientation is real, but it is not the
ordered integral lift.

## Existing Flat Gerbe Limit

The selected finite deck/Cech lift maps:

```text
g1 -> (1,0),
g2 -> (0,1),
g3,g4,g5,g6 -> 0.
```

It is a flat torsion gerbe period table, not an ordinary integral first-Chern
matrix.  The target ordinary `L^2` pullback line needs:

```text
E(g1,g2) =  2,
E(g3,g4) = -4,
E(g5,g6) =  0.
```

So the selected finite gerbe cannot itself be the ordinary integral lift: it
kills `g3,g4`, while the desired source needs the ordered second-base degree
`-4` there.

The shared/central circle is not being forgotten:

```text
E(g5,g6)=0
```

for the target packet, matching the current kernel/trivial central direction.
It simply does not select the sign/order between the first two base factors.

## Conditional Promotion Test

The existing pullback-Cech packet already computes:

```text
c1(L^2) = (2,-4,0),
h1(X,L^2) = 8,
nonzero Ext class available.
```

As an unselected fixture, the validator accepts the algebra but does not
promote it to selected MTT data.

The executable test then changes only the source flags to a hypothetical
selected source certificate.  With that source certificate supplied, the same
finite cohomology packet promotes through the validator.

Thus the remaining gap is not cohomology arithmetic.  It is exactly:

```text
selected ordered integral Cech/automorphy source for L^2=(2,-4,0).
```

## Sufficient Source Contract

A closing packet must supply:

```text
selected_by_mtt = true,
ordered integral c1 matrix with E(g1,g2)=2 and E(g3,g4)=-4,
source-tied base-factor order, not notation,
flat Pic0/torsion character selected or eliminated,
nonzero Ext class selected,
non-split stability,
same-source D_E/dotD/Riesz/Green.
```

## Verdict

The integral-lift route is now reduced to a source certificate:

```text
finite qutrit quotient alone: no-go for target vs swapped,
selected flat gerbe alone: not an ordinary integral c1 lift,
existing h1=8 packet: algebraically ready once selected source exists.
```

Next packet:

```text
Selected_Ordered_L2_Cech_Automorphy_Source_v1
```

or return to the wall route and prove:

```text
r1:r2 = sqrt(2):1
```

from selected source geometry.
