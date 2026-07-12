# Selected Electroweak U1Y Factorized ThresholdOperator SourceEmission or SU2 Cancellation v1

## Result

```text
status = ELECTROWEAK_U1Y_FACTORIZED_OPERATOR_SOURCE_OPEN_SU2_WEAKSPLIT_CLOSED
SU2_same_scheme_row_or_cancellation_closed_for_weaksplit = true
U1_factorized_threshold_operator_source_closed = false
lambda_12_closed = false
```

## What This Closes

The SU2 side is closed for scoped weak-split gauge-kinetic accounting by the
selected flat SU2 background and flat FP quotient-normalization policy. The
new quotient determinant row is also available as an algebraic conditional row:

```json
{
  "logdet": 29.201650332199108,
  "positive_spectrum": [
    {
      "base_multiplicity": 4,
      "eigenvalue": "(2*pi/3)^2",
      "quotient_multiplicity": 8,
      "rank3_multiplicity": 12
    },
    {
      "base_multiplicity": 4,
      "eigenvalue": "2*(2*pi/3)^2",
      "quotient_multiplicity": 8,
      "rank3_multiplicity": 12
    }
  ],
  "usable_for_lambda12_now": false
}
```

## What Still Blocks Closure

```json
{
  "SU2_same_scheme_weaksplit_row": {
    "reason": "Selected SU2 flatness plus flat FP quotient-normalization policy closes the leading weak-split gauge-kinetic SU2 row; this is not an absolute partition-function normalization.",
    "status": "CLOSED_SCOPED_WEAKSPLIT"
  },
  "U1_factorized_operator_source": {
    "quotient_lemma_available": true,
    "reason": "The quotient determinant lemma proves what follows if the factorized operator is selected; it does not emit the operator from source.",
    "required_formula": "A_base tensor I_3 on B_base tensor V_3",
    "status": "OPEN"
  },
  "U1_rank3_carrier": {
    "reason": "SU2 is now closed for scoped weak-split accounting, but the U1 rank-3 carrier and quotient projector still lack same-source selection.",
    "selected": false,
    "status": "SHAPE_FOUND_NOT_SELECTED"
  },
  "U1_shared_line_projector_binding": {
    "projector_found": false,
    "status": "SUPPORTED_BUT_NOT_OPERATOR_BOUND"
  },
  "hypercharge_index_Dynkin_weights": {
    "operator_packet_status": "U1_HYPERCHARGE_OPERATOR_SPECTRUM_SOURCE_PACKET_BUILT_SPECTRUM_OPEN",
    "reason": "The current operator spectrum packet builds the contract but does not select positive spectrum/index weights as U1/Y threshold data.",
    "status": "OPEN"
  }
}
```

The live blocker is now precise: emit the factorized U1/Y threshold operator
`A_base tensor I_3`, bind it to the selected shared-line quotient, and supply
the hypercharge/index/Dynkin weights in the same convention before computing
`lambda_12`.

## Forbidden Diagnostic

```json
{
  "if_quotient_logdet_were_used_as_p_U1": 30.39784445003093,
  "why_forbidden": "The quotient logdet is a finite determinant support value, while the existing p_SU2 row is in the older weak-split p-row convention. A typed convention map and hypercharge/index weights are required before any cross-convention subtraction."
}
```

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json",
  "certificate": "SelectedElectroweakU1YFactorizedOperatorOrSU2CancellationGate",
  "closed": {
    "SU2_same_scheme_row_or_cancellation_for_scoped_weaksplit": true,
    "next_source_template_written": true,
    "quotient_determinant_lemma_available": true
  },
  "closure_claimed": false,
  "next_required_artifact": "Selected_Electroweak_U1Y_FactorizedThresholdOperator_SourceEmission_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_U1Y_Factorized_ThresholdOperator_SourceEmission_or_SU2_Cancellation_v1.md",
  "open": {
    "U1_factorized_threshold_operator_source": true,
    "hypercharge_index_Dynkin_weights": true,
    "lambda_12": true,
    "physical_action_anchor": true,
    "typed_convention_map_for_lambda12": true
  },
  "status": "ELECTROWEAK_U1Y_FACTORIZED_OPERATOR_SOURCE_OPEN_SU2_WEAKSPLIT_CLOSED",
  "target_fitting_used": false,
  "template_path": "candidate_data\\selected_electroweak_u1y_factorized_threshold_operator_source.template.json"
}
```
