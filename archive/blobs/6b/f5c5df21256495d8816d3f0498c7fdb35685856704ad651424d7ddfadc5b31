# Selected Heterotic Ctau PositiveFinitePart or SmoothDiracConvention SourceTheorem v1

## Result

```text
status = HETEROTIC_CTAU_DIRAC_CONVENTION_POSITIVE_FINITEPART_CLOSED_TRIVIAL_MAGNITUDE_OPEN
ctau_positive_finitepart_convention_closed = true
ctau_logdet_value_full_BN = 0.0
ctau_supplies_orientation = true
ctau_supplies_nonzero_threshold_magnitude = false
oriented_phifin_product_operator_closed = false
next_required_artifact = Selected_Heterotic_OrientedPhiFin_ProductOperator_or_SmoothEQa_MagnitudeSource_v1
```

## Theorem

For the selected signed central-rank operator C_tau, the canonical finite chiral doubling D_C=[[0,C_tau],[C_tau,0]] supplies a no-knob positive operator D_C^*D_C=C_tau^2 on the nonzero complement while retaining orientation through sign(C_tau). The selected finite positive determinant policy therefore applies to this convention and gives logdet 0 on both the full B_N and embedded 11-label carriers, with eta 0 from symmetric plus/minus counts. Hence C_tau is a selected orientation operator, not a nonzero threshold-magnitude source. The next closure object must bind C_tau orientation to the selected Phi_fin positive gap layer or emit an equivalent smooth E_Qa magnitude operator from the same source.

## Dirac Packet

```json
{
  "construction": {
    "chiral_space": "H_plus direct_sum H_minus, each copy equal to the selected B_N carrier",
    "dirac_operator": "D_C = [[0, C_tau], [C_tau, 0]]",
    "kernel_policy": "remove ker(C_tau) before finite positive determinant, exactly as the finite determinant policy removes zero modes/shared kernel before logdet",
    "new_continuous_parameter": null,
    "orientation_operator": "sign(C_tau) on the nonzero C_tau complement, with kernel projected out",
    "positive_operator": "D_C^* D_C = diag(C_tau^2, C_tau^2)"
  },
  "finiteparts": {
    "embedded_11_logdet_Dirac_square_positive_complement": 0.0,
    "eta_embedded_11_from_symmetric_plus_minus_counts": 0,
    "eta_full_BN_from_symmetric_plus_minus_counts": 0,
    "full_BN_logdet_Dirac_square_positive_complement": 0.0
  },
  "schema": "SelectedHeteroticCtau.FiniteChiralDiracConvention.v1",
  "selection_status": {
    "finite_chiral_doubling_selected_by_signed_selfadjoint_operator": true,
    "nonzero_threshold_magnitude_supplied": false,
    "orientation_retained": true,
    "positive_finitepart_policy_applies": true
  },
  "source_operator": "C_tau",
  "spectra": {
    "embedded_11": {
      "C_tau": {
        "-1": 4,
        "0": 3,
        "1": 4
      },
      "C_tau_square_positive_complement": {
        "1": 8
      },
      "Dirac_square_positive_complement": {
        "1": 16
      },
      "kernel_dimension_C_tau": 3,
      "kernel_dimension_Dirac_square": 6
    },
    "full_BN": {
      "C_tau": {
        "-1": 9,
        "0": 9,
        "1": 9
      },
      "C_tau_square_positive_complement": {
        "1": 18
      },
      "Dirac_square_positive_complement": {
        "1": 36
      },
      "kernel_dimension_C_tau": 9,
      "kernel_dimension_Dirac_square": 18
    }
  }
}
```

## Next Request

```json
{
  "closure_claimed": false,
  "forbidden_shortcuts": [
    "use C_tau Dirac logdet 0 as the heterotic threshold magnitude",
    "multiply Phi_fin by C_tau without a same-domain commutation/source theorem",
    "insert a positive shift such as 2I+C_tau as a determinant operator",
    "choose orientation weights from observed electroweak data"
  ],
  "purpose": "Use C_tau only as selected sign/orientation and the already selected Phi_fin gap layer as the positive magnitude carrier, if a same-source product operator or smooth E_Qa theorem emits their compatibility.",
  "required_to_close_next": {
    "candidate_operator": "D_oriented^2 = PhiFin_positive_gap on nonzero magnitude complement, orientation/sign = C_tau",
    "commutation_or_simultaneous_functional_calculus": null,
    "prove_kernel_policy_compatible": null,
    "recompute_finitepart_with_Ctau_sector_or_orientation_weights": null,
    "same_BN_domain_for_Ctau_and_PhiFin_positive_gap": true,
    "show_no_double_counting_of_shared_circle": null,
    "source_emits_oriented_operator": null
  },
  "schema": "SelectedHeterotic.OrientedPhiFinProductOperatorRequest.v1",
  "target_fitting_used": false
}
```
