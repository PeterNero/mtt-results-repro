# Selected Heterotic HYM Erratum Repair Comparison Gate v1

## Result

```text
status = HETEROTIC_HYM_ERRATUM_REPAIR_COMPARISON_BUILT_SOURCE_SELECTION_OPEN
printed_block_demoted_to_diagnostic = true
repair_A_integrable = true
repair_B_integrable = true
any_repair_selected = false
next_required_artifact = Selected_Heterotic_HYM_RepairedPipeline_A_B_SourceSelection_or_Retirement_v1
```

## Comparison

```json
{
  "printed_as_source": {
    "integrable_under_standard_check": false,
    "samples": [
      {
        "det_prime": 0.00019311904907226573,
        "eigenvalues": [
          0.0,
          0.09063534779557816,
          0.25,
          0.25,
          0.3125,
          0.375,
          0.5,
          0.5625,
          1.0343646522044223
        ],
        "integrability_residual_norm_squared": 0.1875,
        "log_det_prime": -8.552203724652312,
        "mu": 0.25,
        "positive_modes": 8,
        "trace": 3.3750000000000004,
        "zero_modes": 1
      },
      {
        "det_prime": 216.0,
        "eigenvalues": [
          0.0,
          1.0,
          1.0,
          1.2679491924311228,
          2.0,
          2.0,
          3.0,
          3.0,
          4.732050807568877
        ],
        "integrability_residual_norm_squared": 3.0,
        "log_det_prime": 5.375278407684165,
        "mu": 1.0,
        "positive_modes": 8,
        "trace": 18.0,
        "zero_modes": 1
      },
      {
        "det_prime": 849346560.0,
        "eigenvalues": [
          0.0,
          4.0,
          4.0,
          8.0,
          10.143593539448982,
          20.0,
          24.0,
          36.0,
          37.856406460551014
        ],
        "integrability_residual_norm_squared": 48.0,
        "log_det_prime": 20.55997785886539,
        "mu": 4.0,
        "positive_modes": 8,
        "trace": 144.0,
        "zero_modes": 1
      }
    ],
    "source_certified": false,
    "variant": "printed_as_source"
  },
  "repair_A_diagonal_B3": {
    "integrable_under_standard_check": true,
    "samples": [
      {
        "det_prime": 0.005364418029785157,
        "eigenvalues": [
          0.0,
          0.0,
          0.3125,
          0.3125,
          0.3125,
          0.3125,
          0.75,
          0.75,
          1.0000000000000002
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": -5.227967384126285,
        "mu": 0.25,
        "positive_modes": 7,
        "trace": 3.75,
        "zero_modes": 2
      },
      {
        "det_prime": 2304.000000000001,
        "eigenvalues": [
          0.0,
          0.0,
          2.0,
          2.0,
          2.0,
          2.0,
          4.000000000000001,
          6.0,
          6.0
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": 7.742402021815782,
        "mu": 1.0,
        "positive_modes": 7,
        "trace": 24.0,
        "zero_modes": 2
      },
      {
        "det_prime": 13271040000.000002,
        "eigenvalues": [
          0.0,
          0.0,
          16.000000000000004,
          20.0,
          20.0,
          20.0,
          20.0,
          72.0,
          72.0
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": 23.308850054487856,
        "mu": 4.0,
        "positive_modes": 7,
        "trace": 240.0,
        "zero_modes": 2
      }
    ],
    "source_certified": false,
    "variant": "repair_A_diagonal_B3"
  },
  "repair_B_one_entry_B2_move": {
    "integrable_under_standard_check": true,
    "samples": [
      {
        "det_prime": 0.0034761428833007817,
        "eigenvalues": [
          0.0,
          0.0,
          0.25,
          0.25,
          0.375,
          0.5625,
          0.5625,
          0.625,
          0.7500000000000001
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": -5.661831966756147,
        "mu": 0.25,
        "positive_modes": 7,
        "trace": 3.375,
        "zero_modes": 2
      },
      {
        "det_prime": 324.00000000000006,
        "eigenvalues": [
          0.0,
          0.0,
          1.0,
          1.0,
          3.0,
          3.0,
          3.0,
          3.0000000000000004,
          4.0
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": 5.78074351579233,
        "mu": 1.0,
        "positive_modes": 7,
        "trace": 18.0,
        "zero_modes": 2
      },
      {
        "det_prime": 159252480.0,
        "eigenvalues": [
          0.0,
          0.0,
          4.0,
          4.0,
          12.0,
          24.0,
          24.0,
          36.0,
          40.0
        ],
        "integrability_residual_norm_squared": 0.0,
        "log_det_prime": 18.88600142529372,
        "mu": 4.0,
        "positive_modes": 7,
        "trace": 144.0,
        "zero_modes": 2
      }
    ],
    "source_certified": false,
    "variant": "repair_B_one_entry_B2_move"
  }
}
```

## Theorem

The printed Iwasawa HYM connection cannot be used as a final threshold proof source under the standard integrability check. Two algebraic repairs are integrable in diagnostics: Repair A replaces B3 by mu(E11-E33), and Repair B moves B2 from -E31 to -E32 while keeping B3=E12. Neither repair is source-certified. Therefore all HYM determinant/Hessian blocks computed from the printed or repaired matrices remain diagnostic until a source erratum or independent selection theorem chooses one branch and verifies the Chern-Weil, HYM, trace, quotient, and threshold data.

## Certificate

```json
{
  "any_repair_selected": false,
  "candidate_path": "candidate_data\\selected_heterotic_hym_erratum_repair_comparison_gate.candidate.json",
  "certificate": "SelectedHeteroticHYMErratumRepairComparisonGate",
  "hym_route_retired_as_final_proof_source_until_repair_selection": true,
  "next_required_artifact": "Selected_Heterotic_HYM_RepairedPipeline_A_B_SourceSelection_or_Retirement_v1",
  "note_path": "proof_corpus\\Selected_Heterotic_HYM_Erratum_Repair_Comparison_Gate_v1.md",
  "physical_electroweak_closure": false,
  "printed_block_demoted_to_diagnostic": true,
  "repair_A_integrable": true,
  "repair_B_integrable": true,
  "status": "HETEROTIC_HYM_ERRATUM_REPAIR_COMPARISON_BUILT_SOURCE_SELECTION_OPEN",
  "target_fitting_used": false
}
```
