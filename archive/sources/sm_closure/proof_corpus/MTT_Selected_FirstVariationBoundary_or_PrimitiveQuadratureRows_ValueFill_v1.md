# MTT Selected FirstVariationBoundary or PrimitiveQuadratureRows ValueFill v1

Status: `MTT_SELECTED_FIRSTVARIATIONBOUNDARY_OR_PRIMITIVEQUADRATUREROWS_VALUEFILL_REPLAY_ROWS_BUILT_SOURCE_PROMOTION_OPEN`.

Route A:

```text
formal Hessian/coercivity      = True
normalization compatibility    = True
physical first variation       = False
boundary cancellation          = False
```

Route B:

```text
primitive rows total           = 72
rows filled by replay          = 36
independent quadrature rows    = 0
locked target replay passes    = True
```

The row values are now explicit as replay-backed data, but not promoted as
independent quadrature and not accepted as physical `Phi_fin^C1` application.

Next artifact: `MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1`.
