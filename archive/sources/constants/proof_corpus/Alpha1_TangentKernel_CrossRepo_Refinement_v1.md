# Alpha1 Tangent Kernel Cross-Repo Refinement v1

## Result

Status: `ALPHA1_TANGENT_KERNEL_IMPORTED_ACCEPTANCE_REFINED_SELECTION_NORMALIZATION_OPEN`

The protospinor repo contains the useful finite alpha1 tangent kernel:
`h_ext`, `dotD_h=(dh) ad(T3)`, and the transported response identity
`D_sel(delta psi)+dotD_h psi=0`.

The canonical L2 dual
`N_alpha1(f)=<f,h_ext>/||h_ext||_L2^2` gives
`N_alpha1(h_ext)=1` and pins `lambda_alpha1=1` as the current unit candidate.
This is still not a selected MTT normalization functional, so the alpha1
driver is not verified.

## Imported Kernel

```json
{
  "kernel_name": "K_alpha1_tangent",
  "normalization_functional": {
    "N_alpha1_h_ext": 1.0,
    "formula": "N_alpha1(f)=<f,h_ext>/||h_ext||_L2^2",
    "h_ext_l2_squared": 0.001569278128670748,
    "lambda_alpha1_candidate": 1.0,
    "selected_now": false,
    "why_not_selected": "The canonical dual functional N(f)=<f,h_ext>/||h_ext||^2 gives N(h_ext)=1, but this is not a selected MTT normalization functional."
  },
  "operator_formula": {
    "U": "exp(-u ad(T3))",
    "dU_dalpha": "-(du/dalpha) ad(T3) U",
    "dotD_h": "dotD_h=(dh) ad(T3)",
    "identity": "D_sel(delta psi)+dotD_h psi_sel=0",
    "response": "delta psi=-(h ad(T3)) psi_sel"
  },
  "tangent": {
    "h_ext_l2": 0.03961411527057935,
    "h_ext_residual_l2": 6.751979459438445e-13,
    "role": "candidate selected alpha1 tangent h=du/dalpha1",
    "selected_now": false,
    "symbol": "h_ext",
    "zero_mean": true
  }
}
```

## Acceptance Refinement

```json
{
  "acceptance_theorem": {
    "current_evaluation": {
      "honest_dotd_validator_replay_without_lifted_flags": false,
      "normalization_functional_selected": false,
      "sector_dotd_equality_selected": false,
      "selected_value_emitted_now": false,
      "source_identity_selected": false,
      "source_strength_coordinate_selected": false,
      "tangent_equality_selected": false
    },
    "if_and_only_if_fields": [
      "source_identity.selected_emitted",
      "source_strength_coordinate.selected_emitted",
      "normalization_functional.selected_emitted",
      "tangent_equality.residual_l2 <= 1e-12",
      "sector_dotd_equality.selected_emitted",
      "honest_dotd_validator_replay_passes_without_lifted_flags"
    ],
    "meaning": "This is the exact finite criterion for when the constructed kernel becomes the selected physical alpha1 driver.",
    "name": "SelectedSameSourceAlpha1NormalizationPinDownKernel",
    "selected_value_when_passed": {
      "alpha1_driver_verified": true,
      "du_dalpha1": "h_ext",
      "h_ext_l2": 0.03961411527057935,
      "h_ext_residual_l2": 6.751979459438445e-13,
      "lambda_alpha1": 1.0,
      "selected_value_emitted": true
    }
  },
  "current_repo_improvement": {
    "source": "certificates\\routec_transport_source_promotion_repair_certificate.json",
    "stationary_source_projector_riesz_green_replay_closed": true,
    "why_this_matters": "The protospinor packet was built before the local transport repair.  Its current_evaluation is retained as provenance, but the current repo has already closed the stationary replay layer."
  },
  "stale_fields_from_protospinor_current_evaluation": {
    "honest_dotd_validator_replay_without_lifted_flags": false,
    "normalization_functional_selected": false,
    "sector_dotd_equality_selected": false,
    "selected_value_emitted_now": false,
    "source_identity_selected": false,
    "source_strength_coordinate_selected": false,
    "tangent_equality_selected": false
  },
  "still_required_now": {
    "honest_dotD_replay_without_lifted_flags": true,
    "same_source_selected_normalization_functional": true,
    "sector_dotd_equality_as_selected_theorem": true,
    "selected_C1_A_and_b": true,
    "selected_tangent_equality_h_alpha1_equals_h_ext": true,
    "source_strength_coordinate_selected_by_branch": true
  }
}
```

## Retarded Alternative Boundary

```json
{
  "classified": true,
  "kernel_pattern_available": true,
  "open_transfer_checks": {
    "honest_dotD_replay_from_kernel": false,
    "selected_BN_tangent_or_retarded_kernel": false,
    "selected_sector_charge_or_chirality": false,
    "selected_transfer_normalization": false
  },
  "schur_formula_available": true,
  "typed_sm_dotD_kernel_emitted": false,
  "unit_lag_ratio_closed": true,
  "why_not_transferable_as_proof": "The CKM retarded kernel lives on the nil-survivor dyadic label selection problem.  It supplies a pattern for a Schur-reduced retarded force, but it does not emit the q79/F,m=1 B_N-sector alpha1 tangent, projector-retention derivative, or sector dotD matrix equality."
}
```

## Frontier Update

```json
{
  "current_next": "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1",
  "old_next": "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
  "why": "The cross-repo import supplies the finite tangent kernel, unit dual candidate, and acceptance theorem.  The current transport repair already closes stationary source replay, so the next object is the selected same-source normalization packet, not another retarded-pattern analogy."
}
```
