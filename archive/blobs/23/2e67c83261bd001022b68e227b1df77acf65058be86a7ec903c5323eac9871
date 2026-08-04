---
title: "Visible Rank-Two L2 Ext H1 Gate"
version: v1
---

# Visible Rank-Two `L^2` Ext `H^1` Gate

## Question

Can we now compute the extension space

```text
Ext^1(L^{-1},L) = H^1(X,L^2)
```

for the visible rank-two source route

```text
0 -> L -> V_alpha -> L^{-1} -> 0?
```

## Answer

Not from the current selected data alone.  The topological calculation has
already reduced the target to four primitive line classes.  For the preferred
first branch:

```text
c1(L)   = (1,-2,0),
c1(L^2) = (2,-4,0),
c1(L^2)^2 = -16 alpha_1,
c2(V_alpha) = +4 alpha_1.
```

This is still not a holomorphic line-bundle cohomology computation.  The number
`h^1(X,L^2)` depends on the selected holomorphic representative: Cech
transition functions, an equivalent Dolbeault operator, or a resolved monad
presentation.  Chern class data and slope witnesses do not by themselves give
the Ext dimension.

## Executable Gate

The new validator:

```text
scripts/validate_visible_rank2_l2_cohomology.py
```

accepts a finite cochain packet:

```text
C0 --d0--> C1 --d1--> C2
```

for the selected holomorphic bundle `L^2`.  It computes:

```text
h1 = dim ker(d1) - rank(d0),
```

checks:

```text
d1*d0 = 0,
h1 > 0,
eta in ker(d1),
eta not in im(d0),
```

and distinguishes an algebraic fixture from selected MTT data.

The open fill slot is:

```text
certificates/visible_rank2_l2_cohomology_data.template.json
```

The template is deliberately `OPEN`; the validator returns exit code `2` for
it.  A future selected packet must fill the Cech/Dolbeault matrices and a
closed non-exact extension vector.

## What This Closes

This closes the format and acceptance test for the missing Ext computation.
The next blocker is no longer vague.  To promote the rank-two route to an
actual non-split source candidate, we need a selected line-bundle cochain
packet for `L^2` that validates with positive `h1`.

## What Remains Open

```text
actual H^1(X,L^2) value,
selected nonzero extension class,
non-split stability proof,
HYM/Strominger or Route-C residual,
same-source D_E/dotD/Riesz/Green data,
primitive C1 contractions,
full SM closure.
```
