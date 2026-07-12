# Selected Qa/SU3 m=1 Rank-Two Ext H1 Source Data Attempt

Can the preferred rank-two route

```text
L = (1,-2,0),     L^2 = (2,-4,0)
0 -> L -> V_alpha -> L^{-1} -> 0
```

now supply the missing selected `H^1(X,L^2)` input for the visible
Chern-Weil/operator source?

## Result

The finite cohomology part is available as a conditional fixture, not yet as
selected data.

The q79 pullback-Cech/Kunneth packet has:

```text
C0 dimension = 0
C1 dimension = 8
C2 dimension = 1
d1*d0 = 0
rank d0 = 0
rank d1 = 0
h1 = 8
```

It also supplies a closed non-exact vector in `C1`, so algebraically it can
serve as a non-split Ext class.

However, the packet is explicitly marked:

```text
candidate_role = UNSELECTED_FIXTURE
source.selected_by_mtt = false
fixture_only = true
```

The validator therefore passes the finite cochain checks but refuses promotion
to selected `V_alpha` input.

## Why This Matters

This changes the shape of the blocker. Before this import, the next missing
item looked like "compute `H^1(X,L^2)`." After the import, the finite `h1`
computation is not the hard part. The hard part is the source theorem selecting
this particular ordered representative.

The current obstruction theorem says that topology, `h1`, finite qutrit data,
and the Appell-Humbert matrix do not by themselves break the target/swapped
base symmetry or select the neutral `Pic0` character.

## Best Live Handle

The strongest corpus clue is the monad line-table difference:

```text
L3 - K2 = (1,-2,0)
2(L3 - K2) = (2,-4,0)
```

This is better than a numerical fit because it is an ordered integral label
already inside the monad data. But it remains a candidate until we prove:

```text
1. L3-K2 is selected as the visible V_alpha extension source slot.
2. The monad difference binds to the Appell-Humbert/Cech transitions.
3. Pic0 is quotiented or its neutral character is selected by source data.
```

## Next Theorem

The next proof object should be:

```text
Selected_Monad_Difference_L2_Source_or_Pic0_Quotient_Theorem_v1
```

Acceptance criterion:

```text
Promote the existing h1=8 packet from UNSELECTED_FIXTURE to SELECTED_DATA
without changing the cochain matrices by hand.
```

Once this is closed, the rank-two `V_alpha` route can feed the HYM/Route-C
source, then the common `D_E/dotD/Riesz/Green` payload.
