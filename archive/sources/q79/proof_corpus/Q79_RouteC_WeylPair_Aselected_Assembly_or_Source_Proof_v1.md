# Q79 RouteC WeylPair Aselected Assembly or Source Proof v1

## Result

The Weyl-pair assembly layer is closed conditionally.  If the selected source
emits the phase and shift Weyl-pair columns, the conditional operator has shape
`[72, 2]`, rank `2`, and solves the locked
DeltaTheta_C1 equation with residual `7.691850745534255e-16`.

This is not yet `A_selected`.  The operator is explicitly marked
`is_A_selected = False` because the same-branch source
provenance lemma is still open.

## Repo Snapshot

- `q79`: `omitted-current-repo-head-for-reproducibility` dirty=`False`
- `gr`: `1dc67ca Reanchor long PhiFin source cutsets` dirty=`False`
- `sm_parity`: `34810e5 Refresh verification report after kernel rows` dirty=`False`

## Support Reductions

- `q79_primitive_counterexample_and_weyl_gate_closed_source_open`: `True`
- `previous_weyl_pair_algebraic_gate_built`: `True`
- `gr_weyl_pair_source_gate_built_source_open`: `True`
- `gr_conditional_A_solve_built_source_open`: `True`
- `sm_conditional_A_solve_built_source_open`: `True`
- `target_fitting_excluded`: `True`

## Conditional Operator

- name: `A_weylpair_conditional`
- columns: `['phase_packet', 'shift_packet']`
- shape: `[72, 2]`
- is A_selected: `False`
- why not selected: The columns solve the locked algebraic equation, but current artifacts do not yet prove same-branch selected source emission of the Weyl-pair packet.

## Locked Solve

- rank: `2`
- condition number: `1.0000000000000002`
- consistent: `True`
- deltaTheta_conditional: `[1.0, 1.0000000000000002]`
- residual norm: `7.691850745534255e-16`
- relative residual: `1.5700924586837752e-16`
- exact to tolerance: `True`

## Decision

- `conditional_A_weylpair_assembled`: `True`
- `conditional_deltaTheta_solve_exact`: `True`
- `algebraic_rank_obstruction_absent_for_weylpair_packet`: `True`
- `conditional_A_promoted_to_A_selected`: `False`
- `selected_source_provenance_proved`: `False`
- `A_selected_emitted`: `False`
- `b_selected_emitted`: `False`
- `honest_selected_deltaTheta_C1_solve_run`: `False`
- `full_SM_or_no_knob_closure`: `False`
- `target_fitting_used`: `False`

## Provenance Reduction

`SelectedWeylPairSourceProvenanceLemma` is the next lemma.

The selected q79/F,m=1 S3/Green-Schwarz Route-C source emits the two conditional Weyl-pair columns used here as theorem-derived selected source data: the phase-like I+Z basis-holonomy packet and the shift-like I+X active-vertex packet, in the same B_N/projector/dotD/zero-mode basis.

Must prove:

- phase column is selected source emission, not diagnostic target choice
- shift column is selected active (1,1) vertex emission, not fitted response
- both columns share the selected Route-C basis and normalization
- source coefficients are fixed internally before downstream flavor checks

## What This Closes

- `latest_repo_updates_checked`
- `previous_primitive_counterexample_and_weyl_gate_imported`
- `conditional_A_weylpair_assembled`
- `conditional_deltaTheta_solve_exact`
- `algebraic_rank_obstruction_absent_for_weylpair_packet`
- `remaining_gap_reduced_to_source_provenance`
- `next_target_advanced_to_source_provenance_lemma`
- `target_fitting_excluded`

## What Remains Open

- `prove_selected_weylpair_source_provenance`
- `promote_conditional_A_to_A_selected`
- `emit_theorem_derived_b_selected`
- `run_honest_selected_deltaTheta_C1_solve`
- `selected_PhiFin_alpha1_payload_values`
- `full_SM_or_no_knob_closure`

## Theorem

`Q79ConditionalWeylPairDeltaThetaSolveTheorem` is proved.

Conditioned on same-branch selected source emission of the two enriched Weyl-pair columns, the q79/F,m=1 Route-C 72x2 conditional operator has rank 2 and solves the locked DeltaTheta_C1 splitter equation with deltaTheta=(1,1) up to roundoff.  Thus the Weyl-pair assembly layer has no remaining algebraic rank or consistency obstruction.  This does not promote the conditional operator to A_selected, does not emit b_selected, and does not run an honest selected DeltaTheta solve; the remaining proof is exactly the selected Weyl-pair source provenance lemma.

Next required artifact: `Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1`.
