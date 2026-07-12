# MTT Selected Step40 dotDTransportAlpha1Import or PrimitiveC1Frontier v1

Status: `MTT_SELECTED_STEP40_DOTD_TRANSPORT_ALPHA1_IMPORTED_PRIMITIVE_C1_FRONTIER_OPEN`.

Step40 reconciles two already-proved pieces:

- local transport derivative:
  `dU/dalpha = -(du/dalpha) ad(T3) U`
- same-branch alpha1 import:
  `du/dalpha1 = h_ext`, `selected_dotD_source_verified = true`,
  `alpha1_driver_verified = true`

This retires `dotD_alpha1` as an active blocker for the transported packet.

Still open:

- primitive C1 contractions from the transported zero modes, Green response,
  and `dotD`
- full-sector C1 value emission or a theorem that primitive C1 is not needed
- `A_selected`, `b_selected`
- internal `R_theta` scalar rows and true no-knob SM equivalence

Next artifact: `MTT_Selected_PrimitiveC1Contractions_or_FullSectorC1ValueEmission_v1`.
