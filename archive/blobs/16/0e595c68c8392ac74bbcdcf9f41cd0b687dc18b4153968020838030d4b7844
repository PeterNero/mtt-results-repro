# Selected Electroweak QaStack FinitePartPolicy and IndexScale SourceTheorem v1

## Result

```text
status = ELECTROWEAK_QASTACK_INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_SU2_PHYSICAL_OPEN
regularization_finite_part_selected_internal = true
determinant_index_weights_selected_internal = true
determinant_scale_mu_selected_internal = true
selected_p_a_internal_promoted = true
selected_p_a_internal_value = 29.201650332199108
lambda_12_closed = false
measured_electroweak_closure = false
next_required_artifact = Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1
```

This theorem closes the internal finite-part policy for the selected Qa-stack
row. It does not close the physical electroweak problem.

## Finite-Part Policy

```json
{
  "H_zero_cluster_policy": {
    "general_policy_closed": false,
    "logdet_delta_current_branch": 0.0,
    "reason": "For eta_N=1, inclusion or exclusion of the two shifted H zero-cluster modes contributes 2*log(1)=0, so the current internal p_a value is invariant under that open bookkeeping policy.",
    "selected_eta_N": 1.0,
    "selected_for_current_value": true
  },
  "kernel_policy": {
    "reason": "The shared central line is not a sector-specific threshold load and is quotiented before positive determinant evaluation.",
    "selected_for_internal_row": true,
    "source": "Selected U1 Pperp shared-line quotient policy",
    "zero_shared_line_removed_before_positive_determinant": true
  },
  "regularization": {
    "finite_positive_rule": "FINITE_POSITIVE_EIGENVALUE_ZETA_LOGDET_FOR_QUOTIENT_MODEL",
    "reason": "On the finite selected quotient table there is no infinite heat subtraction. The local determinant interface already selects the executable finite positive eigenvalue accounting once the positive spectrum, multiplicities, weights, and scale are supplied.",
    "rule": "p_a = sum_j multiplicity_j * index_weight_j * log(lambda_j / mu^2)",
    "selected_for_internal_finite_quotient_row": true
  }
}
```

## Index and Scale

```json
{
  "determinant_index_weights": {
    "policy": "unit weights on the already quotiented V/<s> positive table",
    "reason": "Pperp is applied as a domain quotient, not as an extra scalar determinant weight. After quotienting, the multiplicities 8 and 8 already contain the rank-2 retained carrier. Adding another 2/3 would double-count the shared-line quotient.",
    "selected_for_internal_row": true,
    "weights": [
      {
        "eigenvalue": "(2*pi/3)^2",
        "index_weight": 1,
        "multiplicity": 8
      },
      {
        "eigenvalue": "2*(2*pi/3)^2",
        "index_weight": 1,
        "multiplicity": 8
      }
    ]
  },
  "determinant_scale": {
    "mu": "1",
    "physical_K_gauge_closed": false,
    "reason": "The internal action-unit theorem fixes K_gauge,int=1. In the same dimensionless finite determinant units, the determinant scale is mu=1. This is not a physical electroweak gauge normalization.",
    "selected_for_internal_row": true,
    "source": "internal K_gauge action-unit anchor"
  }
}
```

## Internal p_a

```json
{
  "formula": "8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)",
  "promoted_as_internal_finite_part": true,
  "scope": "selected internal finite determinant row on V/<s>; not measured electroweak closure",
  "value": 29.201650332199108
}
```

## Theorem

For the selected q79/F,m=1 internal finite quotient row, the local determinant interface and quotient determinant lemma select the finite positive zeta/logdet accounting on V/<s>. Pperp is a domain quotient, so the retained multiplicities already include the rank-two carrier and the determinant index weights are unit weights on that quotient table. The selected internal action-unit anchor fixes mu=1 in internal determinant units. Therefore p_a^int is promoted to the quotient logdet 29.201650332199108. This does not close lambda_12 or measured electroweak matching, which still require a same-scheme SU2 row or cancellation and the physical gauge/action anchor.

## Guardrails

- `P_perp` is not counted twice as both quotient and weight.
- `mu=1` is internal determinant scale only, not physical gauge normalization.
- The eta_N=1 zero-cluster neutrality is value-level only, not a general policy theorem.
- `lambda_12` and measured electroweak closure remain open.

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
  "certificate": "SelectedElectroweakQaStackFinitePartPolicyAndIndexScale",
  "lambda_12_closed": false,
  "measured_electroweak_closure": false,
  "next_required_artifact": "Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1.md",
  "selected_p_a_internal_promoted": true,
  "selected_p_a_internal_value": 29.201650332199108,
  "status": "ELECTROWEAK_QASTACK_INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_SU2_PHYSICAL_OPEN",
  "target_fitting_used": false
}
```
