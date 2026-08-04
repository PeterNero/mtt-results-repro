# MTT Selected Phi_fin Payload or B_N Basis Emission

Status: `MTT_SELECTED_PHIFIN_OR_BN_EMISSION_CONTRACTS_LOCKED_VALUES_OPEN`.

This locks down the remaining parts at field level.

## Contracts

- selected Phi_fin payload: `candidate_data/selected_phifin_payload_or_bn_basis_emission/selected_phifin_payload.emission_contract.json`
- selected B_N basis: `candidate_data/selected_phifin_payload_or_bn_basis_emission/selected_bn_basis.emission_contract.json`

## Remaining Parts

- `R1_selected_source_certificate`: must identify the selected q79/F,m=1 Strominger/HYM minimizer and justify all selected-source flags
- `R2_selected_rhoE_metric_connection`: must emit rho_E, Hermitian metric, connection A*, and sector projectors
- `R3_selected_operator_spectral_data`: must emit D_E, Riesz projectors, gaps, reduced Green operators, and dotD_alpha1
- `R4_selected_basis_data`: must emit quotient/deck-valid B_N, quadrature, Gram/stiffness matrices, and eigenpairs
- `R5_selected_C1_response`: must emit finite Hessian source, horizontal responses, and primitive C1 contractions
- `R6_replay_without_lifted_flags`: must rerun validators on honest manifest and promotion gate without formal-lift flags

## Dependency Order

1. `R1_selected_source_certificate`
2. `R2_selected_rhoE_metric_connection`
3. `R4_selected_basis_data`
4. `R3_selected_operator_spectral_data`
5. `R5_selected_C1_response`
6. `R6_replay_without_lifted_flags`

## Result

The contracts are written and the honest replay target is locked.  No selected
values are emitted yet.  The next step must fill either the selected `Phi_fin`
payload or the selected quotient/deck-valid `B_N` basis, then replay the
Route-C manifest without lifted flags.

Next artifact: `MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1`.
