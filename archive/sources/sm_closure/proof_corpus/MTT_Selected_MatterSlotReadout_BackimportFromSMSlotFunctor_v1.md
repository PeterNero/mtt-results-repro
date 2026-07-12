# MTT Selected MatterSlotReadout Backimport From SMSlotFunctor v1

Status: `MTT_SELECTED_MATTERSLOT_READOUT_BACKIMPORT_BUILT_STATIC_READOUT_CLOSED_DYNAMIC_OPEN`.

The older matter-slot readout search proved an important no-go: stationary
`rho_s` invariants alone cannot distinguish `10_M`, `bar5_M`, and `1_M`.
That no-go still stands.

What changed is that later SM-slot functor work supplied the missing source
labels.  All six static source arrows are now emitted, so the matter-slot
readout is closed at the static source tier:

- `10_M -> u,e` with `U_10=I_3`
- `bar5_M -> d` with `U_bar5=F`
- `1_M=N^c -> nuD`
- phase/shift partition `u,e | d,nuD`
- transported-projector trace/transfer normalization

This is not a dynamic operator/C1 closure.  Dynamic `D_E/Riesz/Green/dotD`,
primitive C1 contractions, `A_selected`, `b_selected`, physical flavor
constants, true SM equivalence, and no-knob closure remain open.

Next artifact: `MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1`.
