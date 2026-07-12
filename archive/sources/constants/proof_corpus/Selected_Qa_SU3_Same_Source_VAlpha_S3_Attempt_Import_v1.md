# Selected Qa/SU3 Same-Source VAlpha/S3 Attempt Import

## Result

The sharper q79 same-source VAlpha/S3 operator packet attempt is imported.  It
improves the previous fusion import in one important way:

```text
s3_class_restriction subvalidator: PASS
```

The packet consumes the closed S3 class/restriction data, but it is still
correctly refused because the selected VAlpha source, Pic0, same-source link,
and operator execution remain open.

## Validator Frontier

```text
schema: SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1
status: OPEN
exit_code: 2
open_item_count: 24
ordered_source: 2
s3_class_restriction: 0
visible_green_schwarz_source: 1
selected_source_promotion: 1
```

## Dependency Layers

The 24 open items split into four layers:

```text
L0 identity and selected source
  selected_by_mtt
  same_source_valpha_s3_operator
  non-fixture source certificate

L1 VAlpha ordered source
  V_alpha model selected
  L3-K2 selector closed
  nonzero Ext class selected
  non-split stability
  Pic0 selected or quotiented
  ordered-source validator passes

L2 S3/GS same-source bridge
  same-source link from V_alpha to S3 proved
  Chern-Weil row derived from same source
  visible GS source validator passes
  coherent spectral projector retention

L3 operator execution
  transition/rho_E data emitted
  HYM/Strominger or Route C residual passes
  D_E/Riesz/Green/dotD packets pass
  selected-source promotion passes
  primitive C1 or Yukawa overlap contractions
```

## First True Gate

The first true gate is:

```text
Selected_Source_Certificate_for_VAlpha_S3_DE.v1
```

It must be a non-fixture selected source certificate binding:

```text
V_alpha/L3-K2
selected S3/Green-Schwarz visible support
D_E/dotD operator data
```

Everything downstream depends on that identity.  This gate does not prove the
identity; it makes the dependency order explicit.
