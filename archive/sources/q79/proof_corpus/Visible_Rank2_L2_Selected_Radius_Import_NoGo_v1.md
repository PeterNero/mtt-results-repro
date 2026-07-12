---
title: "Visible Rank-Two L2 Selected Radius Import No-Go"
version: v1
---

# Visible Rank-Two `L^2` Selected Radius Import No-Go

## Question

Can the selected constants radius from the no-knob constants repository supply
the missing visible `L^2` Gauduchon wall?

The needed visible wall is:

```text
p1:p2=1:2,
r1:r2=sqrt(2):1.
```

## Imported Result

The constants-side selected radius theorem closes the internal `rho_UV` branch:

```text
R_* = 4.440528182269818,
r3  = 4.440028979122532.
```

But the branch selected there is explicitly:

```text
(r1,r2,r3)=(R,R,r3(R)).
```

Thus, when imported as an Iwasawa metric for the visible slope problem:

```text
r1=r2=R_*,
p1=r2^2/r3^2,
p2=r1^2/r3^2,
p1:p2=1:1.
```

## Visible Slope Check

For `L=(x,y,z)` and

```text
J = r1^2 a + r2^2 b + r3^2 c,
```

the slope pairing is proportional to:

```text
x*r2^2*r3^2 + y*r1^2*r3^2 + z*r1^2*r2^2.
```

After positive rescaling:

```text
p1=r2^2/r3^2,
p2=r1^2/r3^2,
p3=r1^2/r2^2.
```

The target chamber is:

```text
p1:p2=1:2
negative branch: L=(1,-2,0).
```

The selected constants radius gives instead:

```text
p1:p2=1:1
negative branches: L=(-2,1,0) and L=(1,-2,0).
```

So target and swapped remain tied.

## Theorem

**Theorem.** The selected constants radius cannot be the visible `L^2`
target-wall selector when imported directly as the visible Gauduchon metric.

**Proof.** The constants branch has `r1=r2`. Therefore `p1=p2`.
At `p1=p2`, the slopes of `L=(1,-2,0)` and `L=(-2,1,0)` are both negative and
equal up to base swap. The target wall requires `p1:p2=1:2`, equivalently
`r1:r2=sqrt(2):1`. Since `1 != sqrt(2)`, the imported constants radius does
not land on the target wall. Therefore it cannot uniquely select the target
visible branch. Square.

## Interpretation

This is not a rejection of the constants result. It says the constants result
is a closed equal-horizontal internal branch, while the visible `L^2` selector
needs a source that breaks the two horizontal directions in the ratio
`sqrt(2):1`.

The constants result can still complement the program as an internal scale
source. It just cannot be used as the missing target-wall source.

## What Remains

One of the live routes must still be supplied:

```text
selected non-equal-radius source with r1:r2=sqrt(2):1,
ordered integral Cech/automorphy/D_E source,
same-source D_E/dotD/Hessian term ordering the base factors,
holonomy-sensitive source selecting or quotienting Pic0.
```

## Verdict

The selected constants radius import is now tested and ruled out for the
visible `L^2` target-wall role. The proof frontier is narrower and cleaner:
the next source must be genuinely symmetry-breaking for the visible base
ordering, or it must bypass the metric wall with an ordered integral lift.
