# Selected Qa/SU3 m=1 Pic0/Source Switch Table

The ordered `L^2` gate has two remaining switches:

```text
source selection:  L3-K2 is selected by MTT as the visible ordered source
Pic0 resolution:   flat Pic0 is selected or quotiented
```

This note tests the four combinations against the strict q79 ordered-source
validator.

## Result

```text
none              -> OPEN
Pic0 only         -> OPEN, because source selection is still missing
source only       -> OPEN, because Pic0 resolution is still missing
source and Pic0   -> PASS
```

So the two switches are independent. `Pic0` is not the same gap as the lane
selector, and the lane selector does not automatically settle `Pic0`.

## Interpretation

No further arithmetic matrix is missing at this layer. The target matrix

```text
E(g1,g2)=2,  E(g3,g4)=-4,  E(g5,g6)=0
```

is already the one accepted by the ordered-source validator. The remaining
proof must justify the two source-level switches, not alter the matrix.

## Next Artifact

```text
Selected_Monad_Difference_L2_Source_and_Pic0_Quotient_v1
```

It must supply:

```text
1. source selection of the terminal monad lane L3-K2,
2. source-selected or physically justified Pic0 quotient rule,
3. binding to Appell-Humbert/Cech transitions,
4. promotion of the h1=8 Ext packet as SELECTED_DATA.
```

This still does not prove stability, HYM/Route-C, or same-source
`D_E/dotD/Riesz/Green`; those follow only after the selected source exists.
