# Selected PhiFin S2 Gap-Layer Honest Replay Lock v1

## Result

Status: `SELECTED_PHIFIN_S2_D_E_GAP_LAYER_LOCKED`

The selected `D_E` gap layer is now locked as a theorem-derived replay
contract.  The earlier combined replay failed on `D_E` only because source
flags were false; `SelectedCanonicalTraceFormulaSourceLemma` now supplies those
flags for the `D_E` layer only.

## Locked Contract

```json
{
  "D_E_honest_replay_passes_after_theorem_derived_source_flags": true,
  "D_E_source_flags_are_theorem_derived": true,
  "Riesz_Green_layer_closes": true,
  "basis_dimension": 27,
  "basis_id": "F3xF3_gerbe_twisted_fourier_N1_rank3",
  "eta_threshold": 2.1932454224643014,
  "model_gap_gamma_N": 4.386490844928603,
  "scope": "D_E gap/Riesz/Green layer only",
  "selected_eta_N": 1.0,
  "selected_gap_lower_bound": 2.386490844928603,
  "selected_green_norm_bound": 0.4190252822989217,
  "selected_trace_equality": {
    "H_sector": "canonical F3xF3 Fourier Laplacian plus rank-two projector on indices 13,14",
    "family_sectors": "canonical F3xF3 Fourier Laplacian",
    "proved": true
  },
  "zero_cluster_indices": [
    12,
    13,
    14
  ]
}
```

## Boundary

This lock does not promote `dotD_alpha1`, the alpha1 driver, `A_selected`,
`b_selected`, Yukawa data, or full SM closure.

Next required artifact:

```text
Selected_PhiFin_dotD_alpha1_C1_Response_Emission_v1
```
