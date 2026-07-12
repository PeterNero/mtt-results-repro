# Selected U1Y Route-C Primitive C1 Contractions or Lambda12 Gate v1

## Result

```text
status = U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN
alpha1_and_honest_dotD_prefix_closed = true
primitive_C1_contractions_closed = false
primitive_missing_atom_count = 24 / 24
A_selected_emitted = false
b_selected_emitted = false
lambda_12_closed = false
next_required_artifact = Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1
```

The dotD/alpha prefix is now closed, so the remaining work is cleanly
about selected primitive C1 atoms and a separate selected lambda12 spectral table.

## Primitive Atom Table

- `d`: 6 missing atoms
- `e`: 6 missing atoms
- `nuD`: 6 missing atoms
- `u`: 6 missing atoms

Required terms per sector:

- `theta_overlap_variation`
- `left_zero_mode_response`
- `right_zero_mode_response`
- `higgs_zero_mode_response`
- `explicit_vertex`
- `basis_connection`

## Lambda12 Boundary

lambda_12 remains a selected spectral/local-determinant table problem. The post-alpha C1 stack does not emit a selected U1/hypercharge determinant spectrum or a full Delta_a^sel vector.

## Theorem

After the alpha1 driver replay closes, the next obstruction is no longer dotD provenance. The selected branch has oriented functional operator emission, overlap normalization, du/dalpha1=h_ext, and honest dotD replay. What remains for flavor/SM closure is the primitive C1 atom table: for each of u,d,e,nuD, the selected source must emit theta-overlap variation, left/right/Higgs zero-mode responses, explicit vertex, and basis-connection terms. Without those 24 atoms, A_selected, b_selected, sector response matrices, Yukawa magnitudes, and lambda_12 are not computable. Separately, electroweak lambda_12 still requires a selected local determinant/spectral table, not diagnostic near-hit values.

## Guardrails

- Do not treat closed `alpha1` or dotD replay as primitive C1 closure.
- Do not derive `lambda_12` from diagnostic near-hit values.
- Do not use observed masses, CKM data, benchmark Yukawas, or locked C1 columns.

## Certificate

```json
{
  "A_selected_emitted": false,
  "alpha1_and_honest_dotD_prefix_closed": true,
  "b_selected_emitted": false,
  "candidate_path": "candidate_data\\selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json",
  "certificate": "SelectedU1YRouteCPrimitiveC1ContractionsOrLambda12Gate",
  "lambda_12_closed": false,
  "lambda_12_computable": false,
  "next_required_artifact": "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1",
  "note_path": "proof_corpus\\Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1.md",
  "observed_data_used": false,
  "primitive_C1_contractions_closed": false,
  "primitive_atom_count": 24,
  "primitive_missing_atom_count": 24,
  "status": "U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN",
  "target_fitting_used": false
}
```
