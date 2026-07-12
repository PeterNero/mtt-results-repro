# MTT Selected CKMAngleLaw FromSelectedHeavyLinkValues or FlavorObservableReplay v1

Status: `MTT_SELECTED_CKMANGLELAW_FROM_SELECTEDHEAVYLINKS_CHAIN_TIED_ANGLEMAP_OPEN`.

## Result

`SelectedCKMSourceChainIntegrationAfterHeavyLinkSelectionTheorem` is proved.

The CKM source-input chain is now tied together:

```text
flavor policy bridge
  -> q79 CKM phase contact
  -> heavy-link eight-slot contract
  -> selected sector transport B_10=I_3, B_bar5=F
  -> selected Delta_v = (1/sqrt(3), omega^2/sqrt(3))
```

The old heavy-link-values-open flag is superseded.  The selected heavy-link
entry count is now `8/8`, and the selected branch has nonzero leading
noncommutation readiness.

## Selected Delta Signature

```text
Delta_v = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i)
||Delta_v|| = sqrt(2/3)
```

## Guarded CKM Postcheck

Using only measured CKM angles as a downstream postcheck, not as selectors:

```text
delta_q79 = 63.482142857143 deg
phase residual = 2.213743629349 deg
Jarlskog relative residual = 0.018190645457
```

## Boundary

This does not yet derive CKM angle magnitudes.  Since Jarlskog needs
`s12*s23*s13*c12*c23*c13^2*sin(delta)`, the q79 phase contact alone cannot
source-derive Jarlskog until the angle prefactor is also source-derived.

The remaining non-looping target is a source-owned functional

```text
A_CKM : (Delta_v, selected flavor operator rows) -> (s12, s23, s13)
```

Next artifact: `MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1`.
