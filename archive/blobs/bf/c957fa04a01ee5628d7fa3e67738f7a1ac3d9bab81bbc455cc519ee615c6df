# Selected U1Y Route-C Primitive C1 Atom Emission Interface v1

## Result

```text
status = U1Y_ROUTEC_PRIMITIVE_C1_ATOM_EMISSION_INTERFACE_BUILT_VALUES_OPEN
assembly_theorem_proved = true
primitive_C1_atoms_emitted = false
missing_atom_count = 24
A_selected_computable = false
b_selected_computable = false
next_required_artifact = Selected_U1Y_RouteC_PrimitiveC1_AtomPayload_Fill_or_NoGo_v1
```

This artifact fixes the primitive C1 value interface. It proves how a
selected same-source atom payload would assemble into sector response
matrices and then into `A_selected` and `b_selected`; it does not emit
the atom values.

## Sector Order

- `u`
- `d`
- `e`
- `nuD`

## Term Order

- `theta_overlap_variation`
- `left_zero_mode_response`
- `right_zero_mode_response`
- `higgs_zero_mode_response`
- `explicit_vertex`
- `basis_connection`

## Assembly

- `C_s = sum_{term in required_terms} C_{s,term}`
- `Stack the vectorized selected sector response matrices in the fixed sector order [u,d,e,nuD], using the selected left/right zero-mode basis order.`
- `Stack the selected inhomogeneous source/constant terms emitted by the same payload. If a theorem proves the primitive C1 problem homogeneous, this row must be emitted explicitly as the zero vector by that same theorem.`

## Guardrails

- Do not fill atoms from masses, CKM/PMNS data, benchmark Yukawas, lambda12 diagnostics, or locked target columns.
- Do not call `A_selected` or `b_selected` computable until all atom matrices and the inhomogeneous row are emitted by one selected source.

## Certificate

```json
{
  "A_selected_computable": false,
  "assembly_theorem_proved": true,
  "b_selected_computable": false,
  "candidate_path": "candidate_data\\selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json",
  "certificate": "SelectedU1YRouteCPrimitiveC1AtomEmissionInterface",
  "closure_claimed": false,
  "lambda_12_computable": false,
  "missing_atom_count": 24,
  "next_required_artifact": "Selected_U1Y_RouteC_PrimitiveC1_AtomPayload_Fill_or_NoGo_v1",
  "note_path": "proof_corpus\\Selected_U1Y_RouteC_Primitive_C1_Atom_Emission_Interface_v1.md",
  "primitive_C1_atoms_emitted": false,
  "status": "U1Y_ROUTEC_PRIMITIVE_C1_ATOM_EMISSION_INTERFACE_BUILT_VALUES_OPEN",
  "target_fitting_used": false,
  "template_path": "candidate_data\\selected_u1y_routec_primitive_c1_atom_payload.template.json"
}
```
