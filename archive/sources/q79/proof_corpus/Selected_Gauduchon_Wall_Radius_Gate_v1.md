---
title: "Selected Gauduchon Wall Radius Gate"
version: v1
---

# Selected Gauduchon Wall Radius Gate

## Purpose

The previous gate identified the first chamber selector for the target visible
branch:

```text
L=(1,-2,0),
p1:p2 = 1:2.
```

This note translates that abstract slope wall into Iwasawa metric data.

## Slope From the Iwasawa Metric

On the invariant Iwasawa branch:

```text
J = r1^2 a + r2^2 b + r3^2 c,
l = x a + y b + z c.
```

Because `a^2=b^2=c^2=0`, the Gauduchon slope pairing is proportional to:

```text
int_X l wedge J^2
  = 2*(x*r2^2*r3^2 + y*r1^2*r3^2 + z*r1^2*r2^2).
```

Equivalently, up to a positive common factor, the slope vector is:

```text
p = (r2^2/r3^2, r1^2/r3^2, r1^2/r2^2).
```

So:

```text
p1:p2 = r2^2:r1^2.
```

## Target Wall

The target wall:

```text
p1:p2 = 1:2
```

is therefore:

```text
r2^2:r1^2 = 1:2,
r1:r2 = sqrt(2):1.
```

At this wall the slope signs are:

```text
negative: (1,-2,0),
zero:     (-2,1,0), (2,-1,0),
positive: (-1,2,0).
```

Thus the wall would select the target branch as the unique negative-slope
candidate, provided the source also proves that the zero-slope alternatives do
not destabilize or replace the selected source.

The conjugate wall:

```text
p1:p2 = 2:1
```

would instead select:

```text
(-2,1,0).
```

## Current Corpus Status

The current selected Iwasawa curvature packets use the equal-radius
specialization:

```text
r1 = r2 = R.
```

That gives:

```text
p1:p2 = 1:1,
negative branches = (-2,1,0), (1,-2,0).
```

So equal radius is not enough.

The flux corpus also says that, at first order in the invariant Iwasawa
truncation, the radii and bundle moduli enter continuously and a shape modulus
remains.  The selected Iwasawa calculation fixes `r3` after the equal-radius
specialization; it does not currently derive:

```text
r1:r2 = sqrt(2):1.
```

## Rejected Shortcut

A split line-bundle or diagonal Cartan HYM primitivity condition can diagnose
walls, but the split-line HYM no-go already rules that route out as a visible
source for the positive `alpha_1` row.  It cannot be reused as a hidden branch
selector.

## Live Routes

Two honest routes remain:

```text
1. construct a genuinely nonabelian stable/sheaf or Route-C source selecting
   r1:r2 = sqrt(2):1;
2. bypass the wall by constructing an integral Cech/Deligne/D_E lift of the
   finite qutrit class to L=(1,-2,0).
```

Both routes must still handle the flat `Pic0`/torsion character.

## Verdict

The Gauduchon wall problem is now a radius-ratio source problem:

```text
selected target wall = selected r1:r2 = sqrt(2):1.
```

Current packets do not prove that.  The next packet is:

```text
Selected_Iwasawa_Gauduchon_Wall_or_Integral_Lift.v1
```

It must either derive the target radius ratio from selected source geometry or
construct the integral lift selecting `L=(1,-2,0)`.

Open items:

```text
selected r1:r2 = sqrt(2):1 source,
integral Cech/D_E lift,
flat Pic0/torsion character,
non-split extension stability,
same-source D_E/dotD/Riesz/Green,
full SM closure.
```
