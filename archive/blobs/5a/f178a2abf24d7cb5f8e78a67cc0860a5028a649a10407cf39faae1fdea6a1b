# Selected Electroweak U1Y HyperchargeWeights TypedConvention Gate v1

## Result

```text
status = ELECTROWEAK_U1Y_TYPED_HYPERCHARGE_MAP_CLOSED_STACK_DETERMINANT_SOURCE_OPEN
typed_hypercharge_convention_map_closed = true
hypercharge_index_weights_closed_structurally = true
Qa_stack_p_a_source_closed = false
lambda_12_closed = false
```

## Typed Map

```json
{
  "Delta_G_12": "Delta_G_12 = v1_tilde*lambda_12/(4*pi)",
  "hypercharge_embedding": "Y = (1/6) Q_a - (1/2) Q_c",
  "selected_structurally": true,
  "selected_weights": {
    "Qa_stack_weight_in_pY": "1/36",
    "Qc_circle_weight_in_pY": "1/4",
    "SU2_weight_in_lambda12": "-1"
  },
  "threshold_combination": "p_Y = (1/36) p_a + (1/4) p_c",
  "weak_split": "lambda_12 = p_Y - p_SU2"
}
```

## Route Tests

```json
{
  "Qa_stack_interpretation_of_quotient_operator": {
    "accepted": false,
    "conditional_Delta_G_12": 0.08450302790361214,
    "conditional_lambda_12": 2.6179362173268497,
    "conditional_p_Y": 1.4217420994950278,
    "conditional_p_a": 29.201650332199108,
    "reason": "This is the legal convention if the constructed factorized quotient operator is source-emitted as the Qa stack determinant. That source-emission/provenance remains open.",
    "status": "CONDITIONAL_NOT_PROMOTED"
  },
  "Qc_and_SU2_rows": {
    "accepted": true,
    "p_Qc": 2.442340583291322,
    "p_SU2": -1.1961941178318218,
    "reason": "Qc circle and SU2 flat FP quotient rows are selected for weak-split threshold accounting.",
    "status": "CLOSED_FOR_WEAK_SPLIT"
  },
  "direct_U1Y_row_shortcut": {
    "accepted": false,
    "diagnostic_lambda_if_used": 30.39784445003093,
    "reason": "The constructed quotient logdet is not source-typed as an already hypercharge-normalized p_Y row. Treating it as p_Y would bypass the selected Qa/Qc hypercharge map.",
    "status": "REJECTED_UNTYPED_DIRECT_ROW"
  },
  "typed_hypercharge_stack_map": {
    "accepted": true,
    "reason": "The selected hypercharge interface emits Y=(1/6)Qa-(1/2)Qc and p_Y=p_a/36+p_c/4 before electroweak comparison.",
    "status": "CLOSED_STRUCTURAL_MAP"
  }
}
```

The direct-row shortcut is rejected. The legal path is now precise: promote the
constructed quotient determinant as the selected `p_a` stack determinant, or
emit a distinct source-typed hypercharge-normalized `p_Y` row.

## Remaining Blockers

```json
[
  "selected source must emit the constructed quotient operator as the Qa stack determinant p_a, or emit a separately typed hypercharge-normalized p_Y row",
  "selected source emission of the exact A_base tensor I_3 matrix is still open",
  "regularization/scale statement must identify the quotient logdet convention with the p-row convention",
  "physical action anchor and RG/matching scale remain separate two-key requirements for measured electroweak closure"
]
```

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
  "certificate": "SelectedElectroweakU1YHyperchargeWeightsTypedConventionGate",
  "closed": {
    "Qc_row_for_weaksplit": true,
    "SU2_row_for_weaksplit": true,
    "hypercharge_index_weights_structural": true,
    "typed_hypercharge_convention_map": true
  },
  "closure_claimed": false,
  "conditional_lambda12_if_quotient_is_p_a": 2.6179362173268497,
  "next_required_artifact": "Selected_Electroweak_QaStack_Determinant_SourceEmission_or_U1YRowPromotion_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_U1Y_HyperchargeWeights_TypedConvention_Gate_v1.md",
  "open": {
    "Qa_stack_p_a_source_emission": true,
    "direct_hypercharge_normalized_pY_source_emission": true,
    "lambda_12": true,
    "physical_action_anchor": true,
    "regularization_scale_p_row_identification": true
  },
  "status": "ELECTROWEAK_U1Y_TYPED_HYPERCHARGE_MAP_CLOSED_STACK_DETERMINANT_SOURCE_OPEN",
  "target_fitting_used": false
}
```
