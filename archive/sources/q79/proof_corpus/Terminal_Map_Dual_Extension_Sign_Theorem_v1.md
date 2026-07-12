# Terminal Map Dual Extension Sign Theorem

## Question

The terminal-lane filter gives `L3-K2=(1,-2,0)`, while the monad map table
prints the corresponding terminal `g3` Hom type as `K2-L3=(-1,2,0)`.

Is this a sign error, a second branch, or the expected duality between the map
entry and the rank-two visible extension line?

## Result

It is the expected duality.

The printed `g3` map entry has type

```text
K2-L3 = (-1,2,0).
```

The visible rank-two extension route uses the convention

```text
0 -> L -> V_alpha -> L^{-1} -> 0.
```

Therefore the physical L is the dual of the printed g3 terminal map type:

```text
L=L3-K2=(1,-2,0).
L^2=(2,-4,0).
```

This is exactly the line used by the rank-two extension, pullback Cech, and
Appell-Humbert packets. In the ordered deck basis `g1,...,g6`, the matrix is

```text
[ 0  2  0  0  0  0]
[-2  0  0  0  0  0]
[ 0  0  0 -4  0  0]
[ 0  0  4  0  0  0]
[ 0  0  0  0  0  0]
[ 0  0  0  0  0  0]
```

So the sign and base-order convention is no longer a free choice once the
terminal `g3` route is selected. The visible extension line is `L3-K2`, and the
printed terminal map entry is its dual Hom type.

## Theorem

Conditional on selecting the terminal `g3` source, the visible rank-two
extension source is forced to use

```text
L=(1,-2,0), L^2=(2,-4,0).
```

The ordered Appell-Humbert/Cech matrix already constructed in the repository is
the correct matrix for that convention.

## What This Closes

- The terminal `g3` dual sign convention.
- The ambiguity between printed Hom type `K2-L3` and physical extension line
  `L3-K2`.
- The ordered `L^2=(2,-4,0)` matrix binding, conditional on the terminal `g3`
  route.

## Guardrail

This does not prove that MTT selects g3.

The remaining packet is now:

```text
Selected_Terminal_Map_Source_Principle.v1
```

It must prove that MTT selects the terminal `g3` source and supplies selected
typed transition/automorphy data or same-source operator data. Only then can
the existing `h1=8` pullback packet be promoted from `UNSELECTED_FIXTURE` to
`SELECTED_DATA`.
