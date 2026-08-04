# MTT SelectedSMSlotFunctor DownstreamOperatorPayloads or SMParityLedger v1

Status: `MTT_SELECTED_SMSLOTFUNCTOR_DOWNSTREAM_PAYLOAD_LEDGER_BUILT_STATIC_FIELDS_PROMOTED_DYNAMIC_C1_OPEN`.

## Result

The static SM-slot functor closure is now imported into the downstream C1
ledger.  Three old blockers are no longer generic blockers:

- `10_M -> u,e` selects the clock/phase side;
- `bar5_M -> d` plus `1_M=N^c -> nuD` selects the shift/non-10 side;
- the transported-projector trace Gram fixes the finite static transfer
  normalization.

So the Weyl-pair sector route is now source-derived at the static tier:

```text
Z / clock  -> u,e
X / shift  -> d,nuD
```

## Boundary

This still does not promote the conditional Weyl-pair operator to
`A_selected`.  The missing objects are dynamic: selected `D_E/Riesz/Green/dotD`,
the physical alpha1 driver, the selected source-to-C1 overlap tensor, primitive
C1 contractions, and `b_selected`/Hessian normalization.

Next artifact: `MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1`.
