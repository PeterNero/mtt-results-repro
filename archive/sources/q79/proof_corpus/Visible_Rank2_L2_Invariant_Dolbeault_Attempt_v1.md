---
title: "Visible Rank-Two L2 Invariant Dolbeault Attempt"
version: v1
---

# Visible Rank-Two `L^2` Invariant Dolbeault Attempt

## Question

Can the missing selected packet for

```text
H^1(X,L^2),  c1(L^2)=(2,-4,0)
```

be built from the simplest global scalar invariant ansatz on Iwasawa?

## Attempt

Use the invariant anti-holomorphic basis:

```text
dbar e1 = 0,
dbar e2 = 0,
dbar e3 = e1 wedge e2.
```

Try:

```text
D_A = dbar + A wedge,
A = a1 e1 + a2 e2 + a3 e3.
```

For a scalar line operator, `A wedge A=0`, so:

```text
D_A^2=0 iff dbar A=0 iff a3=0.
```

Equivalently, D_A^2=0 iff a3=0.

The script scans all `a_i in {-1,0,1}`.

## Result

The finite result is:

```text
27 scalar invariant candidates scanned,
9 are integrable,
A=0 has h1=2,
all nonzero integrable candidates have h1=0.
```

So the only positive-`h1` invariant scalar case is the trivial complex.  It can
pass the finite cochain validator as an `UNSELECTED_FIXTURE`, but it does not
promote to selected MTT data.

## Why This Does Not Close `L^2`

The obstruction is not merely `h1`.  A global scalar invariant potential lives
on a single smooth trivialization, hence it carries:

```text
c1 = 0.
```

The target is:

```text
c1(L^2)=(2,-4,0).
```

Therefore the invariant global scalar ansatz cannot be the selected line bundle
`L^2`, even when the finite cochain algebra has positive `h1` in the trivial
case.

## What This Closes

This closes the smallest shortcut:

```text
global invariant scalar Dolbeault potential -> selected L^2 packet.
```

It fails.  The next packet must include transition or automorphy data, or an
equivalent nontrivial line-bundle Dolbeault representative carrying
`c1(L^2)=(2,-4,0)`.

## What Remains

```text
construct selected L^2 transition or automorphy data,
compute actual H^1(X,L^2) for that nontrivial line bundle,
select a closed non-exact eta,
prove non-split stability,
prove HYM/Strominger or Route-C residual,
derive same-source D_E/dotD/Riesz/Green,
full SM closure.
```
