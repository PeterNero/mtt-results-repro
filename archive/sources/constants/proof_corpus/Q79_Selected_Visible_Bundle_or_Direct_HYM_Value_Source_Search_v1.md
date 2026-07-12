# Q79 Selected Visible Bundle or Direct HYM Value Source Search v1

## Result

Status: `Q79_SELECTED_VISIBLE_BUNDLE_OR_DIRECT_HYM_VALUE_SOURCE_SEARCH_BUILT_PRIMARY_VALPHA_ROUTE_OPEN`

The search does not close a selected visible source, but it removes ambiguity.
The primary route is the non-split rank-two `V_alpha` extension with
`L=(1,-2,0)`.  The selected S3/Green-Schwarz support must be merged by a
same-source proof or physical quotient, and direct HYM/Route C remains the
execution engine once the source is selected.

## Search Checks

```json
{
  "S0_previous_requests_source_search": true,
  "S1_q79_visible_target_says_operator_source_first_blocker": true,
  "S2_primary_valpha_candidate_identified": true,
  "S3_abelian_shortcut_rejected": true,
  "S4_routec_preserved_as_fallback": true,
  "S5_ah_goodcover_reduced_to_single_source_class": true,
  "S6_architecture_recommends_A_plus_B_then_C": true,
  "S7_local_routec_gate_open_not_closed": true,
  "S8_operator_packet_attempt_open": true
}
```

## Search Results

```json
{
  "direct_hym_routec_fallback": {
    "id": "direct_route_c_finite_hym_strominger_solve",
    "kind": "direct_residual_solve_for_same_class",
    "open_fields": {
      "chern_bianchi_data": {
        "label": "source-derived Chern/Bianchi row",
        "requirement": "derive the alpha1 row from the same residual packet, not as a target insert",
        "status": "OPEN"
      },
      "connection_or_residual": {
        "label": "selected connection/residual",
        "requirement": "provide finite residual matrices and certified error bounds",
        "status": "OPEN"
      },
      "same_source_operator_data": {
        "label": "same-source D_E/dotD/Riesz/Green",
        "requirement": "derive the operator block after the residual source is selected",
        "status": "OPEN"
      }
    },
    "source_shape": "finite selected HYM/Strominger residual packet with c1=0,c2=+4 alpha_1",
    "why_not_primary": "It may be more general than the rank-two extension route, but currently has less finite data because no selected residual matrices are present."
  },
  "primary_route": {
    "closed_support": {
      "hits_c2_4_alpha1": true,
      "l2_h1_validator_available": true,
      "negative_slope_chamber_witness": {
        "mu_L": -1,
        "necessary_subline_slope_negative": true,
        "positive_slope_vector_p": [
          1,
          1,
          1
        ]
      },
      "split_no_go_avoided_by_non_split_route": true,
      "stable_source_sign_compatible": true,
      "terminal_g3_dual_sign_and_order_closed": true
    },
    "id": "rank2_non_split_extension_preferred_L_1_-2_0",
    "kind": "non_split_rank_two_extension",
    "open_fields": {
      "hym_or_route_c_residual": {
        "label": "HYM/Strominger or Route-C residual",
        "requirement": "construct selected connection or finite residual solve for the same bundle",
        "status": "OPEN"
      },
      "line_bundle_cochain_packet": {
        "label": "selected L^2 cochain packet",
        "requirement": "fill certificates/visible_rank2_l2_cohomology_data.template.json",
        "status": "OPEN"
      },
      "non_split_stability": {
        "label": "non-split stability",
        "requirement": "prove no positive-slope line subsheaf destabilizes the selected extension",
        "status": "OPEN"
      },
      "nonzero_ext_class": {
        "label": "nonzero Ext class",
        "requirement": "validator must prove a closed non-exact C1 vector",
        "status": "OPEN"
      },
      "same_source_operator_data": {
        "label": "same-source D_E/dotD/Riesz/Green",
        "requirement": "derive operators from this selected V_alpha inside the total visible source",
        "status": "OPEN"
      }
    },
    "source_shape": "0 -> L -> V_alpha -> L^-1 -> 0",
    "topological_target": {
      "c1_L_squared_square_alpha_coeffs": [
        -16,
        0,
        0
      ],
      "c1_L_squared_vector_abc": [
        2,
        -4,
        0
      ],
      "c1_V_alpha": [
        0,
        0,
        0
      ],
      "c2_V_alpha": [
        4,
        0,
        0
      ],
      "c3_V_alpha": 0,
      "ch2_math": [
        -4,
        0,
        0
      ],
      "l_vector_abc": [
        1,
        -2,
        0
      ]
    },
    "why_primary": "It is the smallest nonabelian route that matches the visible c2 target, does not reuse the rejected split abelian HYM shortcut, and already has an executable H^1/Ext validator."
  },
  "retired_as_final_source": {
    "id": "abelian_two_line_flux_row",
    "kind": "split_integral_line_flux_row",
    "role": "Chern_Bianchi_support_template_only",
    "why_retained": "It fixes the integral row and trace normalization to be matched by a genuine nonabelian stable source or Route-C solve."
  },
  "twisted_s3_support": {
    "id": "twisted_s3_or_gerbe_source_transfer",
    "kind": "twisted_class_source_transfer",
    "open_fields": {
      "map_to_visible_valpha": {
        "label": "twist-to-V_alpha map",
        "requirement": "prove the S3/gerbe representative selects the visible bundle or residual source",
        "status": "OPEN"
      },
      "operator_retention": {
        "label": "projector/operator retention",
        "requirement": "show D_E/dotD and sector projectors survive the twist transfer",
        "status": "OPEN"
      }
    },
    "source_shape": "use the closed S3 class/restriction infrastructure as a twist or obstruction-control layer",
    "why_not_primary": "The S3 class machinery is real support, but it is not yet a visible V_alpha source or Ext packet."
  }
}
```

## Value Fill Target

```json
{
  "direct_hym_fallback_payload": [
    "construct selected finite HYM/Strominger residual packet with c1=0,c2=+4 alpha_1",
    "derive Chern/Bianchi row from that packet",
    "run honest selected-source validators without lifted flags"
  ],
  "name": "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1",
  "primary_payload": [
    "fill selected L^2 cochain packet for L=(1,-2,0)",
    "validate h1>0 and closed non-exact Ext vector",
    "prove non-split extension and stability in selected chamber",
    "bind AH/Cech representative to the selected source class",
    "merge selected S3/Green-Schwarz support by same-source proof or physical quotient",
    "emit HYM/Route-C residual and finite D_E/Riesz/Green/dotD packets"
  ]
}
```

## Remaining Open

```json
{
  "HYM_or_RouteC_residual_certificate": true,
  "full_SM_or_no_knob_closure": true,
  "non_split_stability": true,
  "nonzero_closed_nonexact_Ext_vector": true,
  "primitive_C1_contractions": true,
  "same_source_DE_Riesz_Green_dotD": true,
  "same_source_S3_GS_binding": true,
  "selected_AH_or_Cech_source_binding": true,
  "selected_Gauduchon_or_balanced_chamber": true,
  "selected_L2_cochain_packet": true
}
```
