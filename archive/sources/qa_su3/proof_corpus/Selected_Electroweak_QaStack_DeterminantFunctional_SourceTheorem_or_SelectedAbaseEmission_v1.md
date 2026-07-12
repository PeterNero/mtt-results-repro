# Selected Electroweak QaStack DeterminantFunctional SourceTheorem or SelectedAbaseEmission v1

## Result

```text
status = ELECTROWEAK_QASTACK_DETERMINANTFUNCTIONAL_OR_SELECTED_ABASE_EMISSION_GATE_BUILT_VALUES_OPEN
route_a_selected_abase_emission_closed = false
route_b_direct_bn_functional_closed = false
minimal_selected_finite_part_payload_written = true
conditional_quotient_logdet_carried = 29.201650332199108
selected_p_a_promoted = false
lambda_12_closed = false
next_required_artifact = Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1
```

Both legal closure routes are now explicit. Route A promotes the constructed
`A_base tensor I_3` row only if it is emitted by the selected source. Route B
bypasses `A_base` by emitting the determinant finite part directly on selected
`B_N` over `V/<s>`. Route B is ranked as the better next attack.

## Route A

```json
{
  "already_available": {
    "Pperp_quotient_functor_closed_for_tensor_identity": true,
    "matrix_constructed": true,
    "quotient_logdet": 29.201650332199108,
    "quotient_matrix_constructed": true,
    "same_source_as_27mode_DE_gap_layer": true,
    "same_source_as_Pperp_trace_policy": true
  },
  "blocker": "The exact matrix is constructed and quotient algebra is closed, but the same branch has not emitted it as selected source data.",
  "missing_selected_fields": {
    "Qa_stack_weights_and_scale_policy_closed": false,
    "factorized_matrix_emitted_by_prior_source": false,
    "hypercharge_index_Dynkin_weights_closed": false,
    "selected_source_emission_closed": false,
    "typed_convention_map_closed": false
  },
  "name": "selected_A_base_tensor_I3_emission",
  "purpose": "Promote the constructed tensor-identity row as the selected electroweak Qa-stack threshold operator.",
  "route_closed_now": false
}
```

## Route B

```json
{
  "already_available": {
    "Pperp_domain_policy_closed": true,
    "conditional_Pperp_weighted_logdet": 29.201650332199108,
    "determinant_template_schema": "SelectedElectroweakU1YDeterminantFunctionalSourceTheorem.v1",
    "positive_model_complement_spectrum_available": true,
    "selected_27mode_DE_gap_trace_equality": true
  },
  "blocker": "The selected B_N gap layer and conditional spectrum exist, but no same-source theorem defines the determinant finite part on V/<s>.",
  "missing_selected_fields": {
    "H_zero_cluster_policy": null,
    "determinant_functional_source_theorem_found": false,
    "hypercharge_index_Dynkin_weights": null,
    "kernel_policy": null,
    "regularization_finite_part": null,
    "same_scheme_SU2_row_or_cancellation": null,
    "sector_restriction_to_V_mod_s": null
  },
  "name": "direct_selected_determinant_functional_on_BN",
  "purpose": "Avoid proving A_base identity by emitting the finite-part determinant functional directly on selected B_N.",
  "route_closed_now": false
}
```

## Minimal Next Payload

```json
{
  "forbidden": [
    "observed lambda_12 or sin^2(theta_W)",
    "gap lower bound as determinant spectrum",
    "P_perp identity spectrum",
    "Qa/SU3 log(2008) injection",
    "unit convention or physical anchor data",
    "promote constructed A_base matrix without source emission",
    "promote Pperp trace index as determinant finite part",
    "compute lambda_12 before same-scheme SU2 row or cancellation"
  ],
  "must_emit": {
    "domain_and_operator": {
      "H_zero_cluster_policy": null,
      "kernel_policy": null,
      "operator_choice": "A_base_tensor_I3_emission_or_direct_BN_finite_part",
      "positive_eigenvalue_table_on_V_mod_s": null,
      "sector_restriction_to_V_mod_s": null,
      "selected_B_N_basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3"
    },
    "electroweak_completion_only_after_payload": {
      "lambda12_formula": null,
      "same_scheme_SU2_row_or_cancellation": null
    },
    "finite_part": {
      "determinant_scale": null,
      "index_weights": null,
      "p_a_value": null,
      "regularization": null
    },
    "source_identity": {
      "no_observed_or_benchmark_inputs": null,
      "same_branch_q79_F_m1": null,
      "selected_by_mtt": null,
      "source_certificate": null
    }
  },
  "schema": "SelectedElectroweakQaStackMinimalSelectedFinitePartPayload.v1"
}
```

## Theorem

Given the closed selected 27-mode D_E gap layer, Pperp domain policy, and tensor-identity quotient lemma, electroweak Qa-stack p_a can be promoted only by one of two selected same-source theorems: either the source emits the exact A_base tensor I_3 threshold row, or it emits a direct finite zeta/heat/torsion determinant functional on the selected B_N quotient domain V/<s>. The current source emits neither theorem, so the conditional logdet remains support only.

## Guardrails

- The conditional quotient logdet is not promoted.
- The constructed `A_base` matrix is not promoted as selected.
- `P_perp` remains a domain/trace policy, not a finite-part theorem.
- `p_a`, `lambda_12`, and measured electroweak closure remain open.

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json",
  "certificate": "SelectedElectroweakQaStackDeterminantFunctionalOrSelectedAbaseEmission",
  "conditional_quotient_logdet_carried": 29.201650332199108,
  "lambda_12_closed": false,
  "minimal_selected_finite_part_payload_written": true,
  "next_required_artifact": "Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_QaStack_DeterminantFunctional_SourceTheorem_or_SelectedAbaseEmission_v1.md",
  "route_a_selected_abase_emission_closed": false,
  "route_b_direct_bn_functional_closed": false,
  "selected_p_a_promoted": false,
  "status": "ELECTROWEAK_QASTACK_DETERMINANTFUNCTIONAL_OR_SELECTED_ABASE_EMISSION_GATE_BUILT_VALUES_OPEN",
  "target_fitting_used": false
}
```
