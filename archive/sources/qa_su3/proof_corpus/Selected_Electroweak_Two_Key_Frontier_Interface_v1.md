# Selected Electroweak Two Key Frontier Interface v1

## Result

The constants/electroweak branch is reduced to two independent open keys.

```text
I_U1 = 2/3
I_SU2 = 1
I_Qa_or_SU3 = log(2008)
K_gauge_int = 1

u1y_local_determinant_key_closed = false
physical_action_anchor_key_closed = false
measured_electroweak_closure = false
```

## Key 1: U1/Y Local Determinant

```text
P_perp_quotient_index_closed = True
bad_spectrum_shortcuts_rejected = True
operator_packet_contract_built = True
strongest_live_route = projective_s3_gerbe_source_plus_selected_visible_Chern_Weil_or_U1Y_operator_row
operator_row_found = False
lambda_12_closed = False
```

This key must emit the selected U1/Y threshold operator row on `V/<s>` and its
positive spectrum or zeta/heat/torsion finite part. The `P_perp` quotient is an
index/carrier result, not a spectrum.

## Key 2: Physical Action Anchor

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
Omega0_over_sqrt_alpha_phys = 1.5675093859261626
internal_alpha_closed = True
physical_numeric_alpha_selected = False
best_structural_route = m_theory_modal_gap_planck_anchor
best_structural_route_status = structural slot identified; selected dimensionful value open
```

This key must supply a target-independent dimensional anchor. Internal
`alpha=1` is closed only as canonical internal action units, not as an SI
prediction.

## Next

```text
Selected_Electroweak_Two_Key_FillAttempt_v1
```

The next fill attempt must try both templates and report whether either key can
be promoted from current corpus data.

## Certificate

```json
{
  "alpha_template_path": "certificates\\selected_electroweak_physical_action_anchor_key.template.json",
  "candidate_path": "candidate_data\\selected_electroweak_two_key_frontier_interface.candidate.json",
  "certificate": "SelectedElectroweakTwoKeyFrontierInterface",
  "closed": {
    "forbidden_shortcuts_named": true,
    "internal_kernel_closed": true,
    "physical_action_anchor_template_built": true,
    "two_key_frontier_formalized": true,
    "u1y_key_template_built": true
  },
  "closure_claimed": false,
  "next_required_artifact": "Selected_Electroweak_Two_Key_FillAttempt_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_Two_Key_Frontier_Interface_v1.md",
  "open": {
    "measured_electroweak_closure": true,
    "physical_action_anchor_key": true,
    "typed_convention_rg_scheme": true,
    "u1y_local_determinant_key": true
  },
  "status": "ELECTROWEAK_TWO_KEY_FRONTIER_INTERFACE_BUILT_KEYS_OPEN",
  "target_fitting_used": false,
  "u1_template_path": "certificates\\selected_electroweak_u1y_local_determinant_key.template.json"
}
```
