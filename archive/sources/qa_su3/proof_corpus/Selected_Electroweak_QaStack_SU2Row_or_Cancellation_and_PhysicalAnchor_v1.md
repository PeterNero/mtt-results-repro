# Selected Electroweak QaStack SU2Row or Cancellation and PhysicalAnchor v1

## Result

```text
status = ELECTROWEAK_QASTACK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_ANCHOR_OPEN
same_scheme_SU2_row_or_cancellation_closed = true
lambda_12_internal_closed = true
lambda_12_internal = 2.6179362173268497
Delta_G12_internal = 0.08450302790361214
physical_K_gauge_anchor_closed = false
measured_electroweak_closure = false
next_required_artifact = Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1
```

This closes only the dimensionless internal weak-split threshold. It does
not compare to measured electroweak data.

## Same-Scheme Argument

```json
{
  "Qa_row": {
    "formula": "8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)",
    "local_determinant_interface_rule": "p_a = sum_j multiplicity_j * index_weight_j * log(lambda_j / mu^2)",
    "mu": "1",
    "role": "source-promoted internal finite positive determinant row",
    "status": "ELECTROWEAK_QASTACK_INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_SU2_PHYSICAL_OPEN",
    "value": 29.201650332199108
  },
  "Qc_SU2_rows": {
    "p_Qc": 2.442340583291322,
    "p_SU2": -1.1961941178318218,
    "source": "candidate_data\\dual_attack_local_determinant_or_omega0_source.candidate.json",
    "status": "CLOSED_FOR_WEAK_SPLIT"
  },
  "selected": true,
  "typed_hypercharge_map": {
    "status": "CLOSED_STRUCTURAL_MAP",
    "threshold_combination": "p_Y = (1/36) p_a + (1/4) p_c",
    "weak_split": "lambda_12 = p_Y - p_SU2",
    "weights": {
      "Qa_stack_weight_in_pY": "1/36",
      "Qc_circle_weight_in_pY": "1/4",
      "SU2_weight_in_lambda12": "-1"
    }
  },
  "why_this_is_not_the_forbidden_shortcut": "The rejected shortcut treated the quotient logdet directly as p_Y. This theorem instead uses the already selected Qa/Qc hypercharge map, so the quotient logdet enters only as p_a and Qc remains present."
}
```

## Selected Internal Threshold Vector

```json
{
  "Delta_G12_internal": 0.08450302790361214,
  "formulae": {
    "Delta_G12": "v1_tilde*lambda_12/(4*pi)",
    "lambda_12": "p_Y - p_SU2",
    "p_Y": "p_a/36 + p_c/4"
  },
  "lambda_12_internal": 2.6179362173268497,
  "p_SU2_weaksplit": -1.1961941178318218,
  "p_Y_internal": 1.4217420994950278,
  "p_a_internal": 29.201650332199108,
  "p_c_weaksplit": 2.442340583291322,
  "v1_tilde": 0.405623467693425
}
```

## Theorem

The selected Qa-stack finite-part theorem promotes the quotient logdet only as p_a. The selected typed hypercharge convention gives p_Y=p_a/36+p_c/4, and the Qc and SU2 rows are already selected for weak-split local-determinant accounting. Therefore the same internal scheme computes p_Y=1.4217420994950278 and lambda_12=2.6179362173268497. This closes the dimensionless internal weak-split threshold, but not physical electroweak matching, because the physical gauge/action anchor, matching scale, and RG/threshold scheme remain open.

## Physical Anchor Still Open

```json
{
  "matching_scale_and_RG_scheme_closed": false,
  "measured_electroweak_closure": false,
  "physical_K_gauge_anchor_closed": false,
  "physical_Omega0_or_alpha_action_unit_closed": false,
  "physical_gate_status": "PHYSICAL_EW_MATCHING_REDUCED_TO_OMEGA0_AND_LOCAL_DETERMINANT_OPEN",
  "reason": "lambda_12 is a dimensionless internal weak-split threshold. It does not select the physical gauge/action unit, matching scale, or RG scheme."
}
```

## Guardrails

- `p_a` is not treated as an already hypercharge-normalized `p_Y` row.
- The selected map is `p_Y=p_a/36+p_c/4`; Qc is not dropped.
- `lambda_12` is dimensionless internal threshold data, not a physical action unit.
- No observed electroweak value or target residual is used.

## Certificate

```json
{
  "Delta_G12_internal_value": 0.08450302790361214,
  "candidate_path": "candidate_data\\selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
  "certificate": "SelectedElectroweakQaStackSU2RowOrCancellationAndPhysicalAnchor",
  "closure_scope": "dimensionless_internal_weaksplit_threshold_only",
  "lambda_12_internal_closed": true,
  "lambda_12_internal_value": 2.6179362173268497,
  "measured_electroweak_closure": false,
  "next_required_artifact": "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1.md",
  "physical_K_gauge_anchor_closed": false,
  "same_scheme_SU2_row_or_cancellation_closed": true,
  "status": "ELECTROWEAK_QASTACK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_ANCHOR_OPEN",
  "target_fitting_used": false
}
```
