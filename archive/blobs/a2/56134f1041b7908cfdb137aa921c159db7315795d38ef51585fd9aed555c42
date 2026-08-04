# Terminal Section Principle from Projection Dynamics v1

## Result

Status: `TERMINAL_SECTION_PRINCIPLE_DERIVED_AT_REDUCED_FINITE_PROJECTION_LEVEL_RAW_NMTT_OPEN`

The terminal admissible-section rule is now derived at the reduced
finite projection level.  The derivation uses the same MTT execution
logic as the selected-kernel theorem: physical data factor through
coherent projection and survivor reduction, so a finite terminal lane
selects its unique admissible survivor in the sharp-survivor limit.

For q79, the finite terminal monad-difference lane has exactly one
candidate satisfying both hard filters: shared-circle neutrality and
visible Chern compatibility.  That survivor is `L3-K2`, so the
`g3 / L3-K2` source is no longer merely an added spine axiom at this
reduced level.

This still does not construct the raw upstream `N_MTT` terminal source
operator or a finite-width terminal kernel.

## Derivation Schema

```json
{
  "execution_map": "E_T = pi_terminal o pi_nil o Pi_coh",
  "name": "FiniteProjectionTerminalSectionSelectorTheorem.v1",
  "premises": [
    "Stable physical source data are post-projection observables.",
    "A finite terminal representative lane is a quotient fiber of the raw source space.",
    "Nil/survivor reduction removes representatives that violate active admissibility filters.",
    "The sharp-survivor limit selects the unique finite-cost admissible survivor when it exists.",
    "If no unique finite-cost survivor exists, no terminal selection is made."
  ],
  "proof": [
    "By post-projection observability, the physical source is constant on fibers of E_T.",
    "By quotient factorization, it is therefore a function on the finite terminal survivor set.",
    "By nil-survivor execution in the sharp limit, non-admissible representatives have infinite reduced cost.",
    "If the finite survivor set has exactly one element, that element is the selected terminal section.",
    "If the survivor set is empty or has multiple elements, this theorem refuses selection."
  ],
  "reduced_cost": "J_T(s)=0 for terminal candidates satisfying shared-circle neutrality and visible Chern/Bianchi compatibility; J_T(s)=infinity for candidates failing either hard admissibility filter. Responsibility penalties only enter if more than one candidate has finite hard-filter cost."
}
```

## q79 Reduced Projection Evaluation

```json
{
  "candidate_costs": [
    {
      "central_degree": 1,
      "hits_visible_c2": false,
      "is_central_neutral": false,
      "label": "L1-K2",
      "sharp_survivor_cost": "infinity",
      "survives_projection_filters": false,
      "value": [
        -2,
        -1,
        1
      ]
    },
    {
      "central_degree": -1,
      "hits_visible_c2": false,
      "is_central_neutral": false,
      "label": "L2-K2",
      "sharp_survivor_cost": "infinity",
      "survives_projection_filters": false,
      "value": [
        -1,
        0,
        -1
      ]
    },
    {
      "central_degree": 0,
      "hits_visible_c2": true,
      "is_central_neutral": true,
      "label": "L3-K2",
      "sharp_survivor_cost": 0.0,
      "survives_projection_filters": true,
      "value": [
        1,
        -2,
        0
      ]
    },
    {
      "central_degree": -1,
      "hits_visible_c2": false,
      "is_central_neutral": false,
      "label": "L4-K2",
      "sharp_survivor_cost": "infinity",
      "survives_projection_filters": false,
      "value": [
        1,
        -1,
        -1
      ]
    },
    {
      "central_degree": 1,
      "hits_visible_c2": false,
      "is_central_neutral": false,
      "label": "L5-K2",
      "sharp_survivor_cost": "infinity",
      "survives_projection_filters": false,
      "value": [
        2,
        0,
        1
      ]
    }
  ],
  "finite_survivors": [
    "L3-K2"
  ],
  "selected_L": [
    1,
    -2,
    0
  ],
  "selected_L2": [
    2,
    -4,
    0
  ],
  "selected_c2": [
    4,
    0,
    0
  ],
  "selected_survivor": "L3-K2"
}
```

## What Closes Now

```json
{
  "explicit_axiom_no_longer_primitive_at_reduced_terminal_level": true,
  "no_flavor_proxy_or_lifted_flag_needed_for_L3_K2": true,
  "q79_terminal_selection_derived_at_reduced_finite_survivor_level": true,
  "terminal_spine_axiom_reduced_to_projection_dynamics_schema": true
}
```

## What Remains Open

```json
{
  "Yukawa_or_full_SM_closure": true,
  "construct_raw_N_MTT_terminal_source_operator": true,
  "derive_smooth_finite_width_terminal_kernel_not_only_sharp_limit": true,
  "operator_layer_Pic0_or_flat_holonomy_rule": true,
  "primitive_C1_response_matrices": true,
  "selected_dotD_alpha1_first_variation": true,
  "selected_literal_goodcover_or_HYM_stability_payload": true
}
```

Next: `Raw_N_MTT_Terminal_Source_Operator_or_dotD_C1_Source_v1`.
