# Raw N_MTT Terminal Source Operator v1

## Result

Status: `RAW_NMTT_TERMINAL_SOURCE_OPERATOR_CONSTRUCTED_FINITE_MODEL_SMOOTH_RAW_OPEN`

A finite raw terminal `N_MTT` source operator is now constructed on
the q79 terminal monad-difference lane.  The operator is the
nonnegative closure-strain multiplication operator whose eigenvalue
is the squared norm of the candidate's shared-circle and visible
Chern violation vector.

Its unique zero mode is `L3-K2`, and the finite-width heat kernel
`exp(-beta N_MTT_terminal_q79)` converges to the `L3-K2` survivor
projector as `beta -> infinity`.

This is a finite terminal-table operator.  It does not construct the
smooth continuum `N_MTT` operator on the full raw configuration space.

## Operator Definition

```json
{
  "basis": [
    "L1-K2",
    "L2-K2",
    "L3-K2",
    "L4-K2",
    "L5-K2"
  ],
  "domain": "R^5 with basis terminal monad differences L_i-K2",
  "eigenvalues": [
    85.0,
    21.0,
    0.0,
    13.0,
    33.0
  ],
  "formula": "N e_i = ||(central_i, c2_i-target_c2)||^2 e_i",
  "kernel_basis": [
    "L3-K2"
  ],
  "matrix": [
    [
      85.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    [
      0.0,
      21.0,
      0.0,
      0.0,
      0.0
    ],
    [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    [
      0.0,
      0.0,
      0.0,
      13.0,
      0.0
    ],
    [
      0.0,
      0.0,
      0.0,
      0.0,
      33.0
    ]
  ],
  "name": "N_MTT_terminal_q79",
  "spectral_gap": 13.0,
  "target_c2": [
    4,
    0,
    0
  ],
  "violation_components": [
    "central/shared-circle degree",
    "c2_alpha1_minus_target",
    "c2_alpha2_minus_target",
    "c2_alpha3_minus_target"
  ]
}
```

## Raw Candidate Vectors

```json
[
  {
    "basis_label": "L1-K2",
    "c2_extension_alpha_coeffs": [
      -4,
      4,
      2
    ],
    "central_degree": 1,
    "closure_cost_eigenvalue": 85.0,
    "survives_kernel": false,
    "target_c2": [
      4,
      0,
      0
    ],
    "value": [
      -2,
      -1,
      1
    ],
    "violation_vector": [
      1,
      -8,
      4,
      2
    ]
  },
  {
    "basis_label": "L2-K2",
    "c2_extension_alpha_coeffs": [
      0,
      -2,
      0
    ],
    "central_degree": -1,
    "closure_cost_eigenvalue": 21.0,
    "survives_kernel": false,
    "target_c2": [
      4,
      0,
      0
    ],
    "value": [
      -1,
      0,
      -1
    ],
    "violation_vector": [
      -1,
      -4,
      -2,
      0
    ]
  },
  {
    "basis_label": "L3-K2",
    "c2_extension_alpha_coeffs": [
      4,
      0,
      0
    ],
    "central_degree": 0,
    "closure_cost_eigenvalue": 0.0,
    "survives_kernel": true,
    "target_c2": [
      4,
      0,
      0
    ],
    "value": [
      1,
      -2,
      0
    ],
    "violation_vector": [
      0,
      0,
      0,
      0
    ]
  },
  {
    "basis_label": "L4-K2",
    "c2_extension_alpha_coeffs": [
      2,
      2,
      -2
    ],
    "central_degree": -1,
    "closure_cost_eigenvalue": 13.0,
    "survives_kernel": false,
    "target_c2": [
      4,
      0,
      0
    ],
    "value": [
      1,
      -1,
      -1
    ],
    "violation_vector": [
      -1,
      -2,
      2,
      -2
    ]
  },
  {
    "basis_label": "L5-K2",
    "c2_extension_alpha_coeffs": [
      0,
      -4,
      0
    ],
    "central_degree": 1,
    "closure_cost_eigenvalue": 33.0,
    "survives_kernel": false,
    "target_c2": [
      4,
      0,
      0
    ],
    "value": [
      2,
      0,
      1
    ],
    "violation_vector": [
      1,
      -4,
      -4,
      0
    ]
  }
]
```

## Finite-Width Terminal Kernel

```json
{
  "beta_values": [
    1.0,
    4.0,
    16.0
  ],
  "closed_scope": "finite terminal table only",
  "kernel": "K_beta = exp(-beta N_MTT_terminal_q79)",
  "projection_error_bounds": {
    "1.0": 2.2603294069810542e-06,
    "16.0": 4.642455656042647e-91,
    "4.0": 2.6102790696677047e-23
  },
  "projector_error_bound": "||K_beta - P_L3-K2|| on the normalized complement is <= exp(-beta * spectral_gap)",
  "weights_by_beta": {
    "1.0": {
      "normalized": [
        1.2160965495519145e-37,
        7.582543283116799e-10,
        0.9999977389174447,
        2.2603242961896628e-06,
        4.658875610977208e-15
      ],
      "selected_weight": 0.9999977389174447,
      "unnormalized": [
        1.2160992992528256e-37,
        7.582560427911907e-10,
        1.0,
        2.2603294069810542e-06,
        4.658886145103398e-15
      ]
    },
    "16.0": {
      "normalized": [
        0.0,
        1.1941367950549688e-146,
        1.0,
        4.642455656042647e-91,
        4.926217186867559e-230
      ],
      "selected_weight": 1.0,
      "unnormalized": [
        0.0,
        1.1941367950549688e-146,
        1.0,
        4.642455656042647e-91,
        4.926217186867559e-230
      ]
    },
    "4.0": {
      "normalized": [
        2.1871378321977182e-148,
        3.3057006267607343e-37,
        1.0,
        2.6102790696677047e-23,
        4.7111658015535965e-58
      ],
      "selected_weight": 1.0,
      "unnormalized": [
        2.1871378321977182e-148,
        3.3057006267607343e-37,
        1.0,
        2.6102790696677047e-23,
        4.7111658015535965e-58
      ]
    }
  }
}
```

## What Closes Now

```json
{
  "finite_raw_terminal_N_MTT_operator_constructed": true,
  "finite_width_terminal_heat_kernel_constructed_on_terminal_table": true,
  "positive_spectral_gap_to_nonselected_terminal_candidates": true,
  "sharp_survivor_projection_recovered_as_beta_to_infinity": true,
  "unique_zero_mode_selects_L3_K2": true
}
```

## What Remains Open

```json
{
  "Yukawa_or_full_SM_closure": true,
  "derive_terminal_violation_weights_from_full_closure_Hessian": true,
  "operator_layer_Pic0_or_flat_holonomy_rule": true,
  "primitive_C1_response_matrices": true,
  "selected_dotD_alpha1_first_variation": true,
  "selected_literal_goodcover_or_HYM_stability_payload": true,
  "smooth_continuum_raw_N_MTT_operator": true
}
```

Next: `Selected_Qa_SU3_M1_CW_dotD_alpha1_and_C1_Primitive_Source_v1`.
