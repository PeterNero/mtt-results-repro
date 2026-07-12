---
title: "Selected Pullback L2 Branch Orientation Source Gate"
version: v1
---

# Selected Pullback `L^2` Branch Orientation Source Gate

## Purpose

The previous reduction showed:

```text
c2 + h1                         -> four branches,
strict slope chamber             -> two branches,
symmetric shared-base chamber     -> (-2,1,0) and (1,-2,0),
q79/F finite orientation          -> real, but not mapped to base order.
```

This note checks whether the already selected finite `q79/F,m=1` qutrit
orientation can break the remaining swapped-base ambiguity.

## Finite Qutrit Check

The selected deck/Cech lift uses:

```text
pi(g1)=(1,0),
pi(g2)=(0,1),
B_1((a,b),(c,d)) = -c*b/3 mod Z.
```

For the target and swapped branches:

```text
target:  L=( 1,-2,0),
swapped: L=(-2, 1,0).
```

Both have:

```text
active F_3^2 image = (1,1),
B_1(L,L) = 2/3,
xy = -2.
```

So the finite qutrit orientation cannot distinguish these two branches.  It
orients the active clock-shift pair, but it does not supply the integral lift:

```text
(1,1) in F_3^2  ->  (1,-2,0) rather than (-2,1,0).
```

## Chamber Gate

The slope test gives a sharper route.  With slope vector `p=(p1,p2,1)`:

```text
p1:p2 = 1:2  -> only (1,-2,0) has negative slope,
p1:p2 = 2:1  -> only (-2,1,0) has negative slope.
```

Thus the minimal chamber selector for the target branch is:

```text
selected Gauduchon wall/chamber p1:p2 = 1:2.
```

But the current selected curvature sources only supply equal-radius or
symmetric data.  Those support the shared-base chamber, not the `1:2` wall.
Therefore the wall is a live route, not a closed theorem.

## Correct Way Forward

The next packet must provide one of:

```text
1. source-certified p1:p2 = 1:2 Gauduchon wall/chamber;
2. integral Cech/Deligne/automorphy lift selecting (1,-2,0) from the finite
   (1,1) qutrit class;
3. D_E/dotD/Riesz/Green source whose ordered base response forces the same
   branch.
```

It must also select or eliminate the flat `Pic0`/torsion character, because
`c1` and `h1` do not see that datum.

## What This Closes

```text
finite qutrit orientation cannot select between (1,-2,0) and (-2,1,0),
equal-radius/symmetric chamber is not enough,
p1:p2 = 1:2 is the first explicit chamber selector for the target branch,
the orientation source must be stronger than the F_3 quotient.
```

## What Remains Open

```text
selected p1:p2 = 1:2 chamber source,
integral lift from finite qutrit class to integer branch,
raw transitions or automorphy factors for L=(1,-2,0),
flat Pic0/torsion character selection,
non-split extension stability,
same-source D_E/dotD/Riesz/Green,
full SM closure.
```

## Verdict

The selected `q79/F,m=1` finite orientation is necessary but not sufficient.
The branch is now reduced to a very concrete missing source:

```text
Selected_Pullback_L2_Branch_Orientation_Source.v1
```

Its cleanest target is either a source-certified `p1:p2 = 1:2` Gauduchon
wall/chamber or an integral lift of the finite `(1,1)` qutrit class to
`L=(1,-2,0)`.
