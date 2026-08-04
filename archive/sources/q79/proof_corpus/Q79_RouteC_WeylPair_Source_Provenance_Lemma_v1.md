# Q79 RouteC WeylPair Source Provenance Lemma v1

## Result

The requested provenance lemma is partly proved and partly reduced.  The
source-level Weyl carrier is proven: `g1 = Z`, `g2 = X`, and active shift
`(1,1)` is the selected nonzero shift.  The transfer to the C1 columns is exact
conditioned on a sector-routing rule.

The full selected provenance lemma is **not** proved yet.  The only current
route that picks `u/e <- Z` and `d/nuD <- X` is matching the locked target
columns.  That is useful as a diagnostic uniqueness result, but it cannot serve
as source selection.

## Repo Snapshot

- `q79`: `omitted-current-repo-head-for-reproducibility` dirty=`False`
- `gr`: `bb2de60 Refresh proto-spinor quantum gravity proof chain` dirty=`False`
- `sm_parity`: `a0c2bf2c Certify q79 all-76 hub and A-handle frontier` dirty=`True`

## Support Reductions

- `q79_conditional_A_solve_reduced_to_provenance`: `True`
- `sm_source_level_provenance_reduction_imported`: `True`
- `sm_conditional_transfer_map_imported`: `True`
- `sm_sector_routing_attempt_imported`: `True`
- `q79_representation_dictionary_available_but_sector_assignment_open`: `True`
- `q79_qutrit_lines_available_but_projector_retention_open`: `True`
- `q79_su5_qutrit_packet_finite_only_unselected`: `True`
- `selected_primitive_emission_search_imported_no_legal_emission`: `True`

## Source-Level Carrier

- proved: `True`
- selected by MTT at S3 level: `True`
- source-level projective class selected: `True`
- operator-level projective rhoE promoted: `False`
- g1 equals phase Z residual: `6.202651996836365e-13`
- g2 equals shift X residual: `0.0`

The q79/F,m=1 selected S3/GS gerbe source supplies the period-three projective qutrit Weyl carrier at source level: g1 is the phase generator Z, g2 is the shift generator X, and the central cocycle is selected by the S3 gerbe/Green-Schwarz data rather than by observed flavor targets.

## Conditional Transfer

- conditional exact: `True`
- phase residual: `0.0`
- shift residual: `0.0`
- selected transfer map emitted: `False`
- selected sector routing emitted: `False`
- selected normalization emitted: `False`

Formula:

- `T(Z) = sector_route(u,e; I + Z)`
- `T(X) = sector_route(d,nuD; I + X)`

## Sector Routing Search

All two-two routes:

- phase `['u', 'd']` / shift `['e', 'nuD']`: match=`False`, residuals=(`3.4641016151377544`, `3.4641016151377544`)
- phase `['u', 'e']` / shift `['d', 'nuD']`: match=`True`, residuals=(`0.0`, `0.0`)
- phase `['u', 'nuD']` / shift `['d', 'e']`: match=`False`, residuals=(`3.4641016151377544`, `3.4641016151377544`)
- phase `['d', 'e']` / shift `['u', 'nuD']`: match=`False`, residuals=(`3.4641016151377544`, `3.4641016151377544`)
- phase `['d', 'nuD']` / shift `['u', 'e']`: match=`False`, residuals=(`4.898979485566356`, `4.898979485566356`)
- phase `['e', 'nuD']` / shift `['u', 'd']`: match=`False`, residuals=(`3.4641016151377544`, `3.4641016151377544`)

Exact row relative to locked columns:

[{'is_intended_route': True, 'matches_locked_columns': True, 'phase_residual_to_locked_column': 0.0, 'phase_route': ['u', 'e'], 'shift_residual_to_locked_column': 0.0, 'shift_route': ['d', 'nuD']}]

Source data independently selects route:
`False`

Why not fully proved:

The locked columns identify the intended route uniquely relative to the target columns, but current selected source data do not contain an independent sector-charge/chirality certificate that derives the partition {u,e}|{d,nuD}. Sector projectors retain family kernels uniformly, and the SM interface classifies representations as required source data rather than already selected no-knob data.

## q79 Internal Evidence

- `e6_representation_bridge_closed`: `True`
- `e6_rank_one_seed_sector_assignment_open`: `True`
- `qutrit_clock_shift_lines_validated`: `True`
- `qutrit_complete_visible_cycle_list_open`: `True`
- `c6_orientation_reduced_not_selected`: `True`
- `su5_qutrit_finite_packet_validated`: `True`
- `su5_qutrit_selected_source_available`: `False`

## Primitive Emission Search

- `selected_primitives_found`: `False`
- `R1_promotes`: `False`
- `R4_promotes`: `False`
- `R6_ready`: `False`
- `next_required_artifact`: `MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1`

## Decision

- `full_selected_weylpair_source_provenance_proved`: `False`
- `source_level_weyl_carrier_and_active_shift_proved`: `True`
- `conditional_source_to_C1_transfer_exact`: `True`
- `locked_columns_uniquely_identify_intended_sector_route`: `True`
- `locked_columns_used_as_selector`: `False`
- `selected_sector_route_independently_proved`: `False`
- `selected_transfer_map_emitted`: `False`
- `selected_primitives_found`: `False`
- `conditional_A_promoted_to_A_selected`: `False`
- `b_selected_emitted`: `False`
- `honest_selected_deltaTheta_C1_solve_run`: `False`
- `target_fitting_used`: `False`

## Next Certificate

`SelectedWeylPairSectorChargeOrChiralityCertificate` must supply:

- a theorem-derived sector charge, chirality, or conjugation table for u,d,e,nuD
- a rule assigning the clock/phase leg Z to the u/e sector pair
- a rule assigning the shift/translation leg X to the d/nuD sector pair
- normalization compatibility with the selected dotD/Hessian/C1 response basis

## What This Closes

- `latest_repo_updates_checked`
- `source_level_weyl_carrier_provenance_closed`
- `active_shift_1_1_provenance_closed`
- `conditional_source_to_C1_transfer_exact`
- `all_two_two_sector_routes_enumerated`
- `locked_columns_identify_intended_route_uniquely`
- `current_proof_blocker_identified`
- `target_fitting_excluded`

## What Remains Open

- `selected_sector_charge_or_chirality_certificate`
- `source_derivation_of_u_e_phase_route`
- `source_derivation_of_d_nuD_shift_route`
- `selected_transfer_normalization`
- `promote_conditional_transfer_to_selected_C1_map`
- `promote_conditional_A_to_A_selected`
- `emit_theorem_derived_b_selected`
- `run_honest_selected_deltaTheta_C1_solve`
- `Phi_fin_selected_payload`
- `quotient_valid_BN_basis_certificate`
- `full_SM_or_no_knob_closure`

## Theorem

`Q79WeylPairSourceProvenanceReductionTheorem` is proved.

The q79/F,m=1 Route-C source-level Weyl carrier is proven at the S3/GS source level: g1 carries the phase/clock Z leg, g2 carries the shift/translation X leg, and active shift (1,1) is the unique nonzero active primitive shift.  The map from this carrier to the two C1 columns is exact if the sector routing u/e <- Z and d/nuD <- X is given.  However, the currently selected source data do not independently emit that sector routing or its normalization; the route is selected only by matching the already locked target columns.  Therefore the full selected Weyl-pair source-provenance lemma is not yet proved.  The next non-circular object is a selected sector-charge/chirality certificate, followed by selected Phi_fin/B_N primitive emission.

Next required artifact: `Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1`.
