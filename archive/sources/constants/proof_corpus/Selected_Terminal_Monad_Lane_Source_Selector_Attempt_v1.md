# Selected Terminal Monad Lane Source Selector Attempt v1

## Result

The local `Pic0` obstruction is no longer part of the ordered Chern-Weil/H1
gate.  After quotienting `Pic0` locally, the remaining source-layer theorem is
exact:

```text
Base_Order_Breaking_Terminal_Lane_Source_v1
```

It must supply a source that selects terminal monad differences `L_i-K2` as the
visible ordered `L` lane and orders the two base factors.

## What Is Forced If The Lane Is Selected

The existing terminal-lane arithmetic still forces:

```text
L3-K2 = (1,-2,0)
2(L3-K2) = (2,-4,0)
K2-L3 = (-1,2,0)
```

The dual `K2-L3` matches the printed `g3` type, so the line is the same up to
duality.

## Validator Check

With `Pic0` quotiented but without the source selector, the strict ordered
source validator remains open:

```text
source.selected_by_mtt is not true
base factor order is not selected
standard/equivalent lattice is not selected
```

With the exact missing terminal source axiom switched on, the same packet
passes the strict ordered-source validator.

## Route Audit

Current closed invariants cannot derive the selector.  The base-swap
obstruction still applies: topology, `h1`, finite qutrit data, and the
Appell-Humbert curvature matrix do not choose the ordered target over the
swapped/dual orbit.

The remaining honest source routes are:

```text
1. selected wall/base-order source,
2. same-source D_E/dotD/Riesz/Green response,
3. typed transition or rhoE data binding the terminal lane to the operator packet.
```

## What Closed

```text
local Pic0 blocker for ordered CW/H1 gate: closed
terminal-lane conditional uniqueness: imported closed
L3-K2 forced if terminal lane selected: closed
h1=8 nonzero Ext fixture ready after source selection: closed conditionally
strict validator pass if exact selector is supplied: yes
```

## What Remains

```text
derived terminal monad lane selector: open
base-order breaking source: open
typed transition/rhoE data: open
same-source D_E/dotD/Riesz/Green: open
non-split stability/HYM: open
global holonomy-sensitive Pic0: open
full SM closure: open
```
