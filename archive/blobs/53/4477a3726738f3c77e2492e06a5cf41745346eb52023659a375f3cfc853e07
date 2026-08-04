# Selected Qa/SU3 Visible L2 Orientation Source Attempt v1

## Result

The visible rank-two source is now reduced to a machine-checkable ordered
source packet.

The desired ordered branch is:

```text
L=(1,-2,0),  L^2=(2,-4,0)
E(g1,g2)=+2,  E(g3,g4)=-4,  E(g5,g6)=0
```

The current Appell-Humbert representative has the right matrix, but it is still
only a fixture.  The orientation source is not closed.

## What Closed

The following shortcuts are now explicitly ruled out as final selectors:

```text
finite qutrit orientation selects integer branch: no
equal-radius constants import selects target wall: no
current Appell-Humbert attempt is selected: no
```

The target wall is identified:

```text
p1:p2 = 1:2
r1:r2 = sqrt(2):1
```

This wall would select `L=(1,-2,0)` as the unique negative branch, but current
source certificates do not select that wall.

## Validator State

The ordered-source validator is available and refuses the current packet with
exit code `2`, meaning open/incomplete rather than false mathematics.

Open items:

```text
packet is marked fixture_only
source.selected_by_mtt is not true
source status is not a selected ordered-source status
selection evidence missing: standard_lattice_or_equivalent_selected
selection evidence missing: base_factor_order_selected
selection evidence missing: base_swap_broken_by_source
Pic0 resolution rule missing
Pic0 character not selected or quotiented
```

Accepted final statuses are:

```text
VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED
VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED
```

## Next Object

The next concrete object is:

```text
visible_rank2_l2_ordered_source.selected.json
```

It must prove, from source data rather than notation:

```text
standard lattice or equivalent selected,
ordered base factors selected,
base-swap degeneracy broken by source,
the selector is not only finite mod 3 qutrit data,
the selector is not equal-radius import,
Pic0 is selected or quotiented,
raw transition or automorphy data match the target ordered matrix.
```

Only after that packet validates should the H1=8 Ext packet be rerun as
`SELECTED_DATA`.

## Gate Verdict

```text
visible L2 orientation source closed: no
orientation gap machine-checkable: yes
remaining gate is ordered selected-source packet: yes
target fitting used: no
```

