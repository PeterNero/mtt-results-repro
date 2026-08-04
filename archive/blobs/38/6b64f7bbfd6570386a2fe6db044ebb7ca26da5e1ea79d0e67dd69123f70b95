---
title: "Iwasawa Monad L2 Branch Orientation Candidate"
version: v1
---

# Iwasawa Monad `L^2` Branch Orientation Candidate

## Question

The current rank-two route needs a selected source for:

```text
L = (1,-2,0),
L^2 = (2,-4,0),
E(g1,g2)=2, E(g3,g4)=-4.
```

Earlier gates proved that finite `q79/F,m=1` data cannot distinguish this
branch from the swapped branch `(-2,1,0)`, and that equal-radius imports do not
select the required wall.

The new question is narrower:

```text
Does the printed Iwasawa monad line table contain an ordered integral clue for
the target branch?
```

## Computation

The monad line table records:

```text
L3 = (1,-1,0),
K2 = (0, 1,0).
```

Therefore:

```text
L3 - K2 = (1,-2,0),
2(L3 - K2) = (2,-4,0).
```

The printed typed `g3` slot is the dual line:

```text
K2 - L3 = (-1,2,0).
```

So the target branch occurs as the ordered dual of that typed monad slot.

## What This Means

This is stronger than the finite mod-3 qutrit quotient.  The finite quotient
sees both `(1,-2,0)` and `(-2,1,0)` as `(1,1)` in `F_3^2`, while the monad line
table uses ordered integral `a,b,c` labels and singles out the ordered
difference:

```text
L = L3 tensor K2^{-1}.
```

This gives a concrete candidate for the missing source packet:

```text
Selected_Monad_Difference_L2_Source.v1
```

## Guardrail

This does not yet prove that the source is selected.

The previous monad rejection remains valid for its original target: the monad
does not supply the full `L^2` Cech/Dolbeault cochain packet, explicit typed
maps, a selected nonzero Ext class, stability, or the same-source
`D_E/dotD/Riesz/Green` data.

Equivalently, this is not a selected visible V_alpha source yet.

Also, the printed monad has `c2=0`, so it cannot be silently reused as the
whole visible `c2=+4 alpha_1` source.  The role separation remains intact.  The
new point is only that the ordered line-table difference gives the right
rank-two `V_alpha` branch label.

## Validator Result

The ordered-source validator correctly refuses the monad-difference packet as
an `UNSELECTED_FIXTURE`.

It passes the arithmetic target but remains open because:

```text
source.selected_by_mtt is not true,
source status is not a selected ordered-source status,
base-factor source selection is not proved,
neutral Pic0 is not selected or quotiented.
```

## Correct Next Packet

The next proof object should be:

```text
Selected_Monad_Difference_L2_Source.v1
```

It must prove:

```text
the ordered pair (L3,K2) is selected as the visible V_alpha extension source,
the monad difference binds to the Appell-Humbert/Cech transitions for L^2,
neutral Pic0 is selected or Pic0 is quotient-irrelevant for the source,
the existing h1=8 nonzero Ext packet promotes from fixture to selected data,
the resulting non-split extension is stable/HYM or accepted by Route C,
the same selected source supplies D_E/dotD/Riesz/Green.
```

## Verdict

The corpus does contain a very sharp ordered integral lift candidate:

```text
L = L3 - K2 = (1,-2,0).
```

This is not full closure, but it is a real advance.  The remaining problem is
no longer "find any branch clue"; it is:

```text
prove that this monad-difference line is selected as the rank-two V_alpha
source and resolve Pic0.
```
