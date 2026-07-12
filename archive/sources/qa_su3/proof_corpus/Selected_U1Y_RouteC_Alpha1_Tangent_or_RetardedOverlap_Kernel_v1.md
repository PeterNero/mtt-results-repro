# Selected U1Y Route-C Alpha1 Tangent or RetardedOverlap Kernel v1

## Result

```text
status = U1Y_ROUTEC_ALPHA1_TANGENT_KERNEL_REDUCED_MATTERSLOT_SOURCE_OPEN
retarded_kernel_pattern_available = true
source_level_weyl_carrier_available = true
conditional_weylpair_A_rank_solve_available = true
selected_BN_tangent_or_retarded_kernel = false
honest_dotD_replay_from_kernel = false
next_required_artifact = Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1
```

The retarded-kernel route is not empty: it has the right pattern, a
source-level Weyl carrier, and a conditional Weyl-pair rank solve. The
missing step is transfer into a selected `B_N` alpha1 tangent, and that
transfer currently factors through the same-source matter-slot/overlap
operator packet.

## Required Packet Fields

- `matter_slot_charge`: selected = `false`; required = selected charge table: 10_M -> u/e, non-10 plus 1_M -> d/nuD
- `normalization`: selected = `false`; required = selected trace/inner-product/Hessian normalization for A_selected and b_selected
- `operator_values`: selected = `false`; required = selected D_E/dotD/Riesz/Green values from the same branch
- `overlap_transfer`: selected = `false`; required = selected source-to-C1 overlap functor T_selected
- `primitive_contractions`: selected = `false`; required = selected primitive C1/Yukawa overlap contractions
- `singlet_neutrino_rule`: selected = `false`; required = selected 1_M Dirac-neutrino routing rule
- `source_identity`: selected = `false`; required = selected q79/F,m=1 visible Route-C or V_alpha/gerbe source identity

## Guardrails

- Do not promote the conditional 72x2 Weyl-pair operator to `A_selected`.
- Do not use the locked target columns as a selector.
- Do not infer selected alpha1 tangent from source-level Weyl support alone.
- Do not compare to observed flavor data in this gate.

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel.candidate.json",
  "certificate": "SelectedU1YRouteCAlpha1TangentOrRetardedOverlapKernel",
  "closure_claimed": false,
  "conditional_weylpair_A_rank_solve_available": true,
  "honest_dotD_replay_from_kernel": false,
  "next_required_artifact": "Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1",
  "note_path": "proof_corpus\\Selected_U1Y_RouteC_Alpha1_Tangent_or_RetardedOverlap_Kernel_v1.md",
  "retarded_kernel_pattern_available": true,
  "selected_BN_tangent_or_retarded_kernel": false,
  "selected_sector_charge_or_chirality": false,
  "selected_transfer_normalization": false,
  "source_level_weyl_carrier_available": true,
  "status": "U1Y_ROUTEC_ALPHA1_TANGENT_KERNEL_REDUCED_MATTERSLOT_SOURCE_OPEN",
  "target_fitting_used": false
}
```
