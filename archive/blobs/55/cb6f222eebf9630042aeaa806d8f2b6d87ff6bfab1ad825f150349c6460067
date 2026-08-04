---
title: "Visible V_alpha Chern/Bianchi Source-Packet Candidates"
version: v1
---

# Visible `V_alpha` Chern/Bianchi Source-Packet Candidates

## Question

After the integral row and rank-two Ext gate, what is the correct next visible
source target?

## Answer

The live branch is the rank-two non-split extension:

```text
0 -> L -> V_alpha -> L^-1 -> 0,
L = (1,-2,0),
c1(L^2) = (2,-4,0),
c2(V_alpha) = +4 alpha_1,
ch2_math(V_alpha) = -4 alpha_1.
```

This is not yet a selected source.  It is the best current target because it
hits the required visible Chern class, avoids the split-line HYM no-go, and is
now tied to an executable `H^1(X,L^2)` validator.

The terminal `g3` sign/order ambiguity is now closed before this next step:
the printed Hom type is `K2-L3=(-1,2,0)`, while the physical rank-two extension
line is the dual `L=L3-K2=(1,-2,0)`, so the ordered `L^2` matrix is fixed as
`(2,-4,0)`. This does not select the source, but it removes the sign branch
from the list of open choices.

## Candidate Ledger

The audited ranking is:

```text
1. rank-two non-split extension, L=(1,-2,0)
   primary live branch; c2 arithmetic and Ext validator are in place.

2. abelian two-line flux row, (1,2,0)+(-1,-2,0)
   integral Chern/Bianchi support only.  It gives standard label 4 on alpha_1,
   but split HYM primitivity fails for the individual summands.

3. direct Route-C finite HYM/Strominger solve
   parallel fallback.  It could bypass explicit Ext data, but no selected
   residual matrices are currently present.

4. twisted S3 or gerbe source transfer
   conditional support branch.  The class/restriction machinery is useful, but
   it is not yet a visible `V_alpha` source.
```

So the abelian row is support, not the source.  Its job is to fix the integral
alpha_1 row that the genuine nonabelian source or Route-C residual must match.

## Source Packet Interface

The promotion target is:

```text
VisibleVAlphaSourcePacket.v1
```

It must include:

```text
source certificate,
selected holomorphic structure for L^2,
finite Cech or Dolbeault cochain packet,
closed non-exact Ext vector,
non-split stability certificate,
Chern/Bianchi/Freed-Witten packet for c2=4 alpha_1,
HYM/Strominger or Route-C residual certificate,
same-source D_E operator block,
same-source dotD_alpha1 response,
Riesz projector and reduced Green packet,
trace/action normalization,
SM sector projector retention.
```

The next executable target remains:

```text
certificates/visible_rank2_l2_cohomology_data.template.json
scripts/validate_visible_rank2_l2_cohomology.py
```

A real fill must validate `h1 > 0` and provide a closed non-exact extension
class.  Only then can the proof move to non-split stability and HYM/Route-C
residuals.

## What This Closes

This closes the candidate hierarchy and the exact source-packet fields needed
for promotion.  It also prevents the invalid shortcut of treating the split
abelian row as a selected HYM source.

## What Remains Open

```text
actual H^1(X,L^2),
selected nonzero Ext class,
non-split stability,
source-derived Chern-Weil representative,
HYM/Strominger or Route-C residual,
same-source D_E/dotD/Riesz/Green,
coherent spectral projectors,
primitive C1 contractions,
Yukawa and CKM magnitude closure,
full SM closure.
```
