---
title: "Visible Rank-Two Extension Route for V_alpha"
author: "Peter Nero"
date: "May 2026"
abstract: |
  We reduce the minimal nonabelian source factor V_alpha to an explicit
  rank-two extension target.  For a non-split extension
  0 -> L -> V_alpha -> L^{-1} -> 0 with l=c1(L)=x a + y b + z c, one has
  c1(V_alpha)=0, c3(V_alpha)=0, and c2(V_alpha)=-l^2.  In the Iwasawa alpha
  basis l^2=2(xy alpha_1+xz alpha_2+yz alpha_3), so c2=+4 alpha_1 requires
  xy=-2 and xz=yz=0.  This gives four primitive line classes.  Each admits a
  positive slope chamber where the visible subline L has negative slope, a
  necessary condition for stability.  The route is therefore arithmetically
  viable, but still open at the decisive level: one must supply a nonzero
  extension class in H^1(X,L^2), prove the extension non-split and stable, and
  derive the same-source HYM/Strominger and D_E/dotD data.
---

# Purpose

The additive route identified the missing source factor:

```text
V_alpha:
  c1 = 0,
  c2 = +4 alpha_1,
  c3 = 0.
```

The smallest classical nonabelian source shape is a rank-two extension:

```text
0 -> L -> V_alpha -> L^{-1} -> 0.
```

This note tests whether that route is arithmetically compatible with the
required visible Chern class.

# Chern-Class Formula

Let:

```text
l = c1(L) = x a + y b + z c.
```

In the Iwasawa alpha basis:

```text
l^2 = 2(xy alpha_1 + xz alpha_2 + yz alpha_3).
```

For the rank-two extension:

```text
c1(V_alpha) = 0,
c2(V_alpha) = -l^2,
c3(V_alpha) = 0.
```

Thus the target:

```text
c2(V_alpha) = +4 alpha_1
```

requires:

```text
xy = -2,
xz = 0,
yz = 0.
```

Therefore `z=0` and the primitive solutions are:

```text
l = ( 1,-2,0),
l = (-1, 2,0),
l = ( 2,-1,0),
l = (-2, 1,0).
```

# Necessary Slope Chamber

For stability of an extension with subline `L`, the displayed subline must at
least have negative slope:

```text
mu(L) = p dot l < 0,
p=(p1,p2,p3), p_i>0.
```

Each candidate has a positive witness:

```text
( 1,-2,0): p=(1,1,1),   mu=-1,
(-1, 2,0): p=(3,1,1),   mu=-1,
( 2,-1,0): p=(1,3,1),   mu=-1,
(-2, 1,0): p=(1,3,1),   mu=-1.
```

So the rank-two extension route is not killed by the elementary slope
necessary condition.

# Why This Does Not Violate The Split-Line No-Go

The split-line no-go forbids a finite split line-bundle or diagonal Cartan HYM
source for the positive visible row.

The present route is different:

```text
V_alpha must be non-split.
```

The line `L` is used to build the holomorphic extension.  The HYM source is the
nonabelian extension `V_alpha`, not the direct sum `L plus L^{-1}`.  The split
limit remains forbidden.

# What This Closes

This closes:

```text
minimal rank-two extension Chern arithmetic,
finite primitive line-class candidates,
negative-slope chamber witnesses,
exact next missing Ext/stability data.
```

# What Remains

The route still needs:

```text
H^1(X,L^2) nonzero, or equivalent Cech/monad extension data,
chosen nonzero extension class,
proof the extension is non-split,
proof no other positive-slope line subsheaf destabilizes V_alpha,
selected Gauduchon/Kahler chamber,
source-derived Chern-Weil representative,
HYM/Strominger residual or Li-Yau/HYM existence certificate,
E8 commutant / SM-sector protection or recomputation,
same-total-source D_E, dotD, Riesz/Green, and projectors.
```

# Next Executable Step

Pick one of the four line classes, preferably the chamber-compatible minimal
choice:

```text
l = (1,-2,0).
```

Then compute:

```text
Ext^1(L^{-1},L) = H^1(X,L^2).
```

If that group has a selected nonzero class and the extension is stable, the
minimal nonabelian `V_alpha` source becomes a real candidate.  If it vanishes,
this rank-two extension route is obstructed and we move to a higher-rank or
Route-C source.
