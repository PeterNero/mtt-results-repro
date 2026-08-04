# Selected Electroweak U1Y LocalDeterminant From 27Mode DE GapLayer v1

## Result

```text
status = ELECTROWEAK_U1Y_LOCALDETERMINANT_FROM_27MODE_DE_GAPLAYER_ATTEMPTED_FUNCTIONAL_MAP_OPEN
conditional_27mode_spectrum_written = true
selected_U1Y_determinant_functional_closed = false
lambda_12_closed = false
measured_electroweak_closure = false
```

## What We Tried Before

Yes: earlier gates tried nearby routes. They closed the 27-mode `D_E`
gap/Riesz/Green layer, tested scalar proxy spectra, and ran diagnostic
`lambda_12` scans. They did not select the determinant functional mapping the
27-mode `D_E` packet to the U1/Y finite part on `V/<s>`.

## Conditional Spectrum

```json
{
  "F3xF3_frequency_spectrum": [
    {
      "eigenvalue": "0",
      "multiplicity": 1
    },
    {
      "eigenvalue": "(2*pi/3)^2",
      "multiplicity": 4
    },
    {
      "eigenvalue": "2*(2*pi/3)^2",
      "multiplicity": 4
    }
  ],
  "H_sector_zero_cluster_shift_candidate": {
    "include_in_determinant_policy_selected": false,
    "reason": "The trace-equals-27mode theorem identifies the H-sector zero-cluster rank-two shift, but the electroweak U1/Y determinant functional has not selected whether this H-sector shift enters the U1/Y threshold finite part.",
    "selected_eta_N": 1.0,
    "shifted_zero_modes": 2,
    "unshifted_zero_modes": 1
  },
  "base_laplacian_unit": "(2*pi/3)^2",
  "base_laplacian_unit_numeric": 4.386490844928604,
  "basis_dimension": 27,
  "basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3",
  "conditional_logdet_if_H_eta1_zero_shift_included": {
    "formula": "positive_complement_logdet + 2*log(1)",
    "numeric": 43.80247549829866
  },
  "conditional_zeta_logdet_positive_complement": {
    "formula": "12*log((2*pi/3)^2) + 12*log(2*(2*pi/3)^2)",
    "numeric": 43.80247549829866
  },
  "rank3_model_kernel_multiplicity": 3,
  "rank3_model_positive_complement": [
    {
      "eigenvalue": "(2*pi/3)^2",
      "multiplicity": 12
    },
    {
      "eigenvalue": "2*(2*pi/3)^2",
      "multiplicity": 12
    }
  ],
  "schema": "Conditional27ModeDEFiniteSpectrumAttempt.v1"
}
```

## Determinant Map Tests

```json
{
  "include_H_zero_cluster_shift": {
    "conditional_logdet_if_eta1_included": 43.80247549829866,
    "reason": "The H-sector rank-two zero-cluster shift is source-identified, but the U1/Y determinant finite-part policy has not selected inclusion, exclusion, or cancellation.",
    "status": "POLICY_OPEN"
  },
  "use_27mode_gap_bound_as_logdet": {
    "reason": "selected_gap_lower_bound is a Riesz/gap stability bound, not an eigenvalue list or zeta finite part.",
    "status": "REJECTED_BOUND_NOT_SPECTRUM",
    "value_tested": 2.386490844928603
  },
  "use_Pperp_trace_index_as_weighted_spectrum": {
    "reason": "P_perp closes the quotient trace index 2/3 only; it cannot supply positive eigenvalues or a zeta/heat/torsion finite part.",
    "status": "REJECTED_PROJECTOR_NOT_SPECTRUM"
  },
  "use_rank3_model_complement_spectrum_as_U1Y": {
    "conditional_logdet": 43.80247549829866,
    "reason": "The rank-3 F3xF3 complement spectrum is emitted by the D_E gap-layer theorem, but no source selects it as the U1/Y local determinant on V/<s> with hypercharge/index weights.",
    "status": "CONDITIONAL_SUPPORT_NOT_SELECTED_U1Y_FUNCTIONAL"
  }
}
```

## Required Functional

```json
{
  "must_not_use": [
    "observed lambda_12 or sin^2(theta_W)",
    "gap lower bound as determinant spectrum",
    "P_perp identity spectrum",
    "Qa/SU3 log(2008) injection",
    "unit convention or physical anchor data"
  ],
  "must_select": [
    "sector restriction from the 27-mode B_N/End0 packet to U1/Y on V/<s>",
    "kernel and H-sector zero-cluster inclusion/exclusion policy",
    "hypercharge/index/Dynkin weights before electroweak comparison",
    "same-scheme SU2 determinant row or exact cancellation theorem",
    "regularization convention for finite zeta/heat/torsion part",
    "lambda_12 formula using only selected rows"
  ],
  "schema": "SelectedElectroweakU1YDeterminantFunctionalRequired.v1"
}
```

## Next

```text
Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1
```

The new missing object is not another 27-mode `D_E` proof. It is the selected
U1/Y determinant functional: the source theorem that says which weighted,
kernel-quotiented, regularized part of the 27-mode packet is the U1/Y local
threshold row, and how the same scheme handles SU2 or cancels it.

## Certificate

```json
{
  "candidate_path": "candidate_data\\selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
  "certificate": "SelectedElectroweakU1YLocalDeterminantFrom27ModeDEGapLayer",
  "closed": {
    "Pperp_rejected_as_spectrum": true,
    "conditional_27mode_model_spectrum": true,
    "gap_bound_rejected_as_logdet": true,
    "required_U1Y_determinant_functional_isolated": true
  },
  "closure_claimed": false,
  "conditional_logdet_positive_complement": 43.80247549829866,
  "next_required_artifact": "Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1",
  "note_path": "proof_corpus\\Selected_Electroweak_U1Y_LocalDeterminant_From_27Mode_DE_GapLayer_v1.md",
  "open": {
    "lambda_12": true,
    "same_scheme_SU2_determinant_or_cancellation": true,
    "selected_U1Y_determinant_functional": true,
    "selected_finite_part": true,
    "selected_positive_U1Y_eigenvalues": true
  },
  "spectrum_attempt_path": "candidate_data\\selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
  "status": "ELECTROWEAK_U1Y_LOCALDETERMINANT_FROM_27MODE_DE_GAPLAYER_ATTEMPTED_FUNCTIONAL_MAP_OPEN",
  "target_fitting_used": false
}
```
