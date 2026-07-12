---
title: "Visible Rank-Two L2 Pullback Cech Attempt"
version: v1
---

# Visible Rank-Two `L^2` Pullback Cech Attempt

## Question

After the global scalar invariant route failed, can we build an actual finite
transition/automorphy candidate for

```text
H^1(X,L^2),  c1(L^2)=(2,-4,0)?
```

## Construction Tested

Use the standard Iwasawa deck scaffold:

```text
X = Gamma \ H_3(C),
pi(z1,z2,z3)=(z1,z2).
```

The candidate is a pullback from the holomorphic base torus:

```text
L^2 = pi^* M,
M on E1 x E2,
deg(M|E1)=2,
deg(M|E2)=-4.
```

Equivalently, the deck-level integral first-Chern cocycle has the alternating
matrix on generators `g1,...,g6`:

```text
E(g1,g2)= 2,
E(g3,g4)=-4,
E(g5,g6)= 0,
all mixed base and central terms zero.
```

This hits:

```text
c1(L^2)=(2,-4,0),
c1(L^2)^2 = -16 alpha_1,
c2(V_alpha)=+4 alpha_1
```

for the preferred rank-two extension line `L=(1,-2,0)`.

## Cohomology Calculation

For an elliptic curve line bundle of degree `d`:

```text
d>0: h0=d, h1=0,
d<0: h0=0, h1=-d.
```

Thus on the base:

```text
E1 degree  2: h0=2, h1=0,
E2 degree -4: h0=0, h1=4.
```

The Kunneth calculation gives:

```text
h0(E1 x E2,M)=0,
h1(E1 x E2,M)=2*4=8.
```

Because `H0(base,M)=0`, the vertical fiber contribution to degree one is zero
in this reduced pullback packet.  The conditional total is therefore:

```text
h1(X,pi^*M)=8.
```

## Validator Packet

The script emits:

```text
candidate_data/visible_rank2_l2_pullback_cech_attempt.cohomology.json
```

and the validator accepts it as a finite reduced cochain packet with:

```text
h1=8,
eta closed,
eta not exact.
```

Important guardrail: this packet is marked `UNSELECTED_FIXTURE`.  It is not a raw good-cover transition table and it is not yet a selected MTT source.

## What This Achieves

This is the first route that simultaneously:

```text
realizes c1(L^2)=(2,-4,0),
escapes the failed global scalar invariant ansatz,
produces positive H^1,
passes the finite Ext validator.
```

So the rank-two route is no longer blocked by lack of any plausible positive
cohomology model.

## What Remains Open

The decisive missing theorem is now:

```text
MTT selects this pullback representative, or an equivalent selected
transition/automorphy representative with the same cohomology.
```

Only after that can the same cohomology packet be promoted from
`UNSELECTED_FIXTURE` to `SELECTED_DATA`.

Then the next proof steps are:

```text
choose a nonzero Ext class from the eight-dimensional H1,
prove the extension is non-split,
prove stability in the selected chamber,
derive the HYM/Strominger or Route-C residual,
derive same-source D_E/dotD/Riesz/Green data,
compute primitive C1 contractions and flavor magnitudes.
```

## Verdict

The global scalar route is dead, but the base-pullback Cech route is alive.
It gives a concrete conditional `h1=8` Ext space for the desired topological
class.  The next target is not more cohomology arithmetic; it is the selection
source for this pullback line-bundle representative.
