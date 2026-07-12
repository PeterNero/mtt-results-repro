# MTT CONST EW 02 Weak Mixing B37 RA2 Boundary or RB4 Independent Source v1

Status: `MTT_CONST_EW_02_B37_RA2_BOUNDARY_OR_RB4_INDEPENDENT_SOURCE_BUILT`

Label: `CONST-EW-02 / WEAK-MIXING / B37-RA2-BOUNDARY-OR-RB4-INDEPENDENT-SOURCE`

## Result

```text
RA-2 formal C1 defect functional source          True
RA-2 finite trace algebraic boundary cancellation True
RA-2 physical boundary/source promotion          False
RB-4 strict independent payload schema imported  True
RB-4 independent values/source ids filled        False
```

## Superset Use

This is a combined superset step constrained to one locked C1 target. Route A
uses the variational/finite-trace encoding; Route B uses the independent
quadrature/source-payload encoding. They are not free knobs: both must emit
source-owned objects before promotion.

## Next

`CONST-EW-02 / WEAK-MIXING / B38-ACTION-IDENTITY-OR-RB4-PAYLOAD-FILL`
