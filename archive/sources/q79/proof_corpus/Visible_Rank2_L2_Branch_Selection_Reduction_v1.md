---
title: "Visible Rank-Two L2 Branch Selection Reduction"
version: v1
---

# Visible Rank-Two `L^2` Branch Selection Reduction

## Question

After finding the four integral pullback branches, can current MTT data select

```text
L=(1,-2,0),  L^2=(2,-4,0)?
```

## Short Answer

Not yet.  The current certificates reduce the problem sharply, but they do not
select the ordered base branch.

## Selector Tests

The topology gives:

```text
c2(V_alpha)=4 alpha_1,
xy=-2,
z=0.
```

So there are four branches:

```text
(-2, 1,0),
(-1, 2,0),
( 1,-2,0),
( 2,-1,0).
```

The cohomology test does not break the tie:

```text
all four branches have reduced h1(X,L^2)=8.
```

The slope test helps, but still does not select uniquely.  For a non-wall
positive slope chamber with ratio `r=p1/p2`, the negative-slope branches are:

```text
r < 1/2:       (1,-2,0), (2,-1,0),
1/2 < r < 2:  (-2,1,0), (1,-2,0),
r > 2:        (-2,1,0), (-1,2,0).
```

Thus slope sign alone always leaves two branches in a strict chamber.  The
shared/symmetric base chamber `p1=p2` would reduce the ambiguity to:

```text
(-2,1,0), (1,-2,0).
```

These are two negative-slope branches, not a unique selected line.

That is progress, but still not a unique selection.

## q79/F Orientation

The retarded branch really does select the q79/F representative at the finite
gerbe/qutrit level, and the selected S3 twisted source carries the same q79/F
orientation.

But no audited certificate currently maps:

```text
q79/F orientation -> ordered base factors -> L=(1,-2,0).
```

So q79/F is not yet a selected branch rule for the visible `L^2` line bundle.
In this certificate q79/F is real but not mapped to the base line.

## Flux Row

The old abelian row:

```text
(1,2,0)+(-1,-2,0)
```

supports the correct `alpha_1` Chern/Bianchi row, but the split-line HYM no-go
prevents using it as the actual source or as a non-split branch selector.

## Flat Character

The flat Pic0/torsion character remains open.  It is invisible to the current
`c1` and `h1` tests, so it must be selected or eliminated by source data.

## Exact Remaining Object

The next packet is:

```text
Selected_Pullback_L2_Branch_Orientation_Source.v1
```

It must supply:

```text
selected Gauduchon/Kahler chamber or slope vector,
ordered base-factor convention,
source map from q79/F, D_E/dotD, monad/Cech, or differential cohomology to L=(1,-2,0),
flat Pic0/torsion character selection or no-go,
raw transition/automorphy factors for the selected branch.
```

## Verdict

The current data do not prove the selected branch.  What is now proved is the
stronger reduction:

```text
topology + h1: four branches,
add strict slope chamber: two branches,
add symmetric shared-base chamber: the two branches (-2,1,0) and (1,-2,0),
add q79/F: still unmapped to base-line order.
```

The remaining source is genuinely orientation-carrying.  This is exactly the
piece that must exist before the `h1=8` packet can be promoted to selected
data without a hidden knob.
