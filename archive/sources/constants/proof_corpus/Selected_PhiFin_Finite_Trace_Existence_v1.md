# Selected PhiFin Finite Trace Existence v1

## Result

The abstract S1-S2 finite-trace lemma is proved, but finite values are still
open.

Status: `SELECTED_PHIFIN_FINITE_TRACE_EXISTENCE_PROVED_VALUES_OPEN`

## Theorem

`SelectedPhiFinFiniteTraceExistenceLemma`

Given the S0 selected smooth source and a declared finite Route-C Galerkin/Cech basis, the Phi_fin finite trace is mathematically defined: it has a selected connection/rho_E trace, finite D_E and dotD matrices, and Riesz/Green operators whenever the selected gap certificate is positive. This proves existence and functoriality of S1-S2, but not the emitted numeric/symbolic entries.

Proved: `True`

## Prerequisites

- `S0_selected_source_closed`: PASS
- `branch_fixed`: PASS
- `not_fixture_or_lifted`: PASS
- `target_fitting_excluded`: PASS

## Proof

### connection_trace

A selected smooth HYM/Strominger source determines a connection A_E and Hermitian metric h_E on the selected bundle/sheaf/gerbe module. On a finite good cover, parallel transport and transition restriction define rho_E or an equivalent connection trace.

### galerkin_projection

For any declared finite Route-C basis B_N in the selected Hilbert space, the orthogonal projection P_N gives finite matrices P_N D_E P_N and P_N dotD_alpha1 P_N. These matrices are selected because A_E and the basis are selected inputs, not fitted target data.

### riesz_green

If the zero-mode cluster is separated by a positive selected gap gamma_N, the Riesz projector is the contour integral of the finite resolvent and the reduced Green operator is the inverse on the projected complement.

### error_gap_control

If the basis residual epsilon_N is bounded and epsilon_N is smaller than the selected gap margin, standard Galerkin perturbation gives stable projectors and controlled reduced Green error.

## Emission Boundary

The theorem proves that the objects exist as selected finite traces.  The repo
still must emit:

- `selected_connection_or_rhoE_entries`
- `basis_BN_or_Cech_basis_entries`
- `D_E_matrix_entries`
- `dotD_alpha1_matrix_entries`
- `Riesz_contour_or_projector_entries`
- `reduced_Green_entries`
- `gap_gamma_N_and_residual_epsilon_N`

## Next Artifact

`Selected_PhiFin_S1S2_Value_Emission_v1`

This is the object that must compute or symbolically emit the entries before the
Route-C validators may honestly pass.
