# MTT Selected RouteBSelectedBasisIndependenceFill or RowSourceGap v1

Status: `MTT_SELECTED_ROUTEB_SELECTEDBASISINDEPENDENCEFILL_BUILT_ROW_SOURCE_GAP_OPEN`

This step fills the Route B selected-basis independence clause.

The selected stationary projectors and ordered bases are imported from the
finite projector source-promotion chain: model-active B_N values are not copied;
they are promoted only after symbolic transport conjugation
`P_s^sel = U P_s^model U^-1`.

The strict validator still rejects the packet on one remaining Route B field:
`source_independent_of_residual_projector_replay`. The row values, finite trace
quadrature, and selected basis are ready, but we still need the theorem that the
dynamic 110-row C1 packet is evaluated from that selected basis rather than
inherited from residual-projector replay.

Next artifact: `MTT_Selected_RouteBRowSourceIndependenceProof_or_RouteAPhysicalSourceFill_v1`.
