# MTT Selected U10Ubar5 1M SourcePromotion SameBranch Emission v1

Status: `MTT_SELECTED_U10UBAR5_1M_SOURCEPROMOTION_SAMEBRANCH_EMISSION_BUILT_STATIC_MATTERSLOT_READOUT_CLOSED_DYNAMIC_PAYLOAD_OPEN`.

Static matter-slot source emission is now imported:

```text
matter-slot readout static tier   : true
U10/Ubar5 source static tier      : true
1M Dirac shift static tier        : true
dynamic overlap/C1 payload closed : false
accepted internal scalar rows     : 0
```

This retires the static U10/Ubar5/1M readout blocker for the scalar-row path.
The active blocker is now dynamic: overlap kernel/C1 primitive source emission
and selected dynamic value payload rows.

Next artifact: `MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1`.
