---
title: "Visible Rank-Two L2 Source Ambiguity Classification"
version: v1
---

# Visible Rank-Two `L^2` Source Ambiguity Classification

## Question

Can the topological rank-two target by itself select the pullback line

```text
L=(1,-2,0),  L^2=(2,-4,0)?
```

## Short Answer

No.  The `c2=4 alpha_1` target narrows the problem sharply, but it does not
select a unique source.

For a rank-two extension

```text
0 -> L -> V_alpha -> L^{-1} -> 0
```

with `c1(L)=(x,y,z)`, the visible target gives:

```text
c2(V_alpha)=-c1(L)^2=(4,0,0).
```

Equivalently:

```text
xy=-2,
xz=0,
yz=0.
```

Since `xy=-2`, both `x` and `y` are nonzero, so `z=0` is forced.  The line is
therefore a base-pullback class, but there are four integral branches:

```text
L=(-2, 1,0),  L^2=(-4, 2,0),
L=(-1, 2,0),  L^2=(-2, 4,0),
L=( 1,-2,0),  L^2=( 2,-4,0),
L=( 2,-1,0),  L^2=( 4,-2,0).
```

The intended branch `L=(1,-2,0)` is one of them, not the unique one.

## Cohomology Check

For each of the four branches, the reduced base-pullback Kunneth calculation
gives:

```text
h1(X,L^2)=8.
```

So the `h1=8` result is robust, but it is not a branch selector.  Neither
`c2` nor the cohomology dimension tells us which of the four branches MTT
selects.

## Flat-Character Issue

Even after a branch is chosen, a base flat character remains invisible to the
current `c1/h1` tests.  On elliptic factors with nonzero degree, twisting by a
`Pic0` character preserves the degree and the Hodge dimensions:

```text
degree d>0: h0=d, h1=0,
degree d<0: h0=0, h1=-d.
```

Thus flat-character data is not something we may silently set to zero.  If the
source allows such characters, the selected-source certificate must either fix
one or prove that the MTT branch rule eliminates them.

## What This Proves

This closes an important negative theorem:

```text
c2=4 alpha_1 plus h1=8 does not prove selected L=(1,-2,0).
```

Promoting the current pullback packet to `SELECTED_DATA` without branch and
flat-character evidence would introduce a hidden knob.

## Exact Remaining Source Requirement

The selected-source certificate must now supply:

```text
the branch-orientation rule selecting L=(1,-2,0),
the rule selecting or eliminating flat Pic0 characters,
the rule excluding central or torsion twists if they are available,
raw transition/automorphy factors for the selected representative,
the link to the same visible V_alpha branch.
```

## Verdict

The proof has advanced, but not by overclaiming.  We now know exactly why the
source certificate is necessary: topology forces the right base plane and the
right `c2`, while branch orientation and flat/torsion character data remain
genuine selected-source information.
