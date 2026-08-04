# Selected Heterotic BismutWeitzenbock Formula or OUWeightDerivation v1

## Result

```text
status = HETEROTIC_BISMUT_WEITZENBOCK_FORMULA_OR_OUWEIGHT_DERIVATION_BUILT_TENSOR_PAYLOAD_OPEN
formula_contract_built = true
tensor_payload_available = false
E_Qa_computed = false
OU_weights_computed = false
next_required_artifact = Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1
```

## Contract

```json
{
  "bismut_weitz_lhs": "Delta_threshold = nabla_{+,A}^* nabla_{+,A} + E_Qa",
  "known_inputs": {
    "A_r3_over_r1r2": 0.22517311887007765,
    "eight_A_squared": 0.40562346769342494,
    "metric_weighted_logdet_monotone_on_samples": true,
    "relative_one_form_weights": {
      "bar_omega_1_norm_sq": 0.05071433540836435,
      "bar_omega_2_norm_sq": 0.05071433540836435,
      "bar_omega_3_norm_sq": 0.050725739919091344
    },
    "selected_radii": {
      "r1": 4.440528182269818,
      "r2": 4.440528182269818,
      "r3": 4.440028979122532
    }
  },
  "minimal_tensor_payload": [
    "structure constants in selected orthonormal real frame",
    "J and Hermitian form omega",
    "H=d^c omega or equivalent Bismut torsion components",
    "Bismut connection coefficients Gamma^+",
    "R^+ curvature components and trace row",
    "bundle connection A and curvature F_A in selected gauge",
    "representation action on u(E)-valued one-forms",
    "inner product/trace normalization and quotient projector"
  ],
  "ou_weight_payload": [
    "selected OU mode basis indexed by (n,k)",
    "source-derived gamma_{n,k}^{-1}",
    "finite truncation/error theorem",
    "zeta or heat regularization rule"
  ],
  "selection_condition": "Since the current metric-weighted algebraic block has monotone logdet samples, any interior mu selection must come from E_Qa, source-derived OU weights, or a direct finite operator emission."
}
```

## Route Tests

```json
{
  "bismut_weitzenbock_formula_lane": {
    "E_Qa_computed": false,
    "known_geometry_enough_to_start": true,
    "missing": {
      "Bismut_connection_coefficients": null,
      "E_Qa_matrix": null,
      "Hermitian_form_omega": null,
      "R_plus_curvature_components": null,
      "ad_bundle_representation": null,
      "complex_structure_J": null,
      "connection_A_components": null,
      "curvature_F_A_components": null,
      "kernel_and_quotient_policy": null,
      "orthonormal_coframe": null,
      "structure_constants_c_ij_k": null,
      "torsion_H_or_d_c_omega_components": null,
      "trace_normalization": null
    },
    "status": "PRIMARY_TENSOR_PAYLOAD_OPEN"
  },
  "direct_finite_operator_emission_lane": {
    "required": [
      "rho_E mesh/metric",
      "D_E action",
      "Riesz/gap",
      "reduced Green",
      "finite determinant or torsion finite part"
    ],
    "status": "ACCEPTABLE_IF_EMITTED",
    "would_bypass_symbolic_E": true
  },
  "ou_weight_derivation_lane": {
    "guardrail": "arbitrary gamma_{n,k}^{-1} values are forbidden",
    "missing": {
      "OU_generator": null,
      "gamma_nk_inverse_table": null,
      "proof_weights_are_source_derived": null,
      "selected_mode_basis": null
    },
    "status": "ALTERNATIVE_OPEN",
    "weights_computed": false
  }
}
```

## Theorem

The remaining heterotic threshold source problem is now reduced to a specific tensor payload. Either compute the Bismut/Weitzenbock zero-order block E_Qa from the selected torsion, curvature, bundle connection, trace, and quotient data, or derive the OU mode weights from the same selected source. A direct finite operator emission may replace this symbolic route, but it must emit rho_E, D_E, Riesz/gap, Green, and finite-part data honestly.

## Next Template

```json
{
  "acceptance_tests": [
    "all tensors are emitted before threshold comparison",
    "E_Qa is self-adjoint in the selected inner product",
    "central/gauge zero modes match the selected quotient policy",
    "positive spectrum/heat/torsion finite part is computable",
    "no arbitrary OU weights or fitted mu are inserted"
  ],
  "bundle_tensors": {
    "ad_bundle_representation": null,
    "connection_A_components": null,
    "curvature_F_A_components": null,
    "trace_normalization": null
  },
  "geometric_tensors": {
    "Bismut_connection_coefficients": null,
    "Hermitian_form_omega": null,
    "R_plus_curvature_components": null,
    "complex_structure_J": null,
    "orthonormal_coframe": null,
    "structure_constants_c_ij_k": null,
    "torsion_H_or_d_c_omega_components": null
  },
  "operator_contract": {
    "E_Qa_matrix": null,
    "kernel_and_quotient_policy": null,
    "principal_symbol": "nabla_plus_A^* nabla_plus_A",
    "zero_order_terms": [
      "curvature action on u(E)-valued one-forms",
      "torsion contraction terms",
      "gauge-fixing curvature/torsion correction",
      "possible dilaton/Strominger lower-order correction if selected"
    ]
  },
  "ou_derivation_alternative": {
    "OU_generator": null,
    "gamma_nk_inverse_table": null,
    "proof_weights_are_source_derived": null,
    "selected_mode_basis": null
  },
  "schema": "SelectedHeteroticBismutWeitzenbockTensorPayload.v1",
  "source_identity": {
    "fixed_frame_and_gauge": null,
    "same_branch_selected_HYM_or_Strominger_source": null,
    "selected_domain": null
  },
  "status": "OPEN_TENSOR_VALUES_REQUIRED"
}
```

## Certificate

```json
{
  "E_Qa_computed": false,
  "OU_weights_computed": false,
  "candidate_path": "candidate_data\\selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation.candidate.json",
  "certificate": "SelectedHeteroticBismutWeitzenbockFormulaOrOUWeightDerivation",
  "formula_contract_built": true,
  "next_required_artifact": "Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1",
  "note_path": "proof_corpus\\Selected_Heterotic_BismutWeitzenbock_Formula_or_OUWeightDerivation_v1.md",
  "status": "HETEROTIC_BISMUT_WEITZENBOCK_FORMULA_OR_OUWEIGHT_DERIVATION_BUILT_TENSOR_PAYLOAD_OPEN",
  "target_fitting_used": false,
  "template_path": "candidate_data\\selected_heterotic_bismut_weitzenbock_tensor_payload.template.json",
  "tensor_payload_available": false
}
```
