# Selected U1Y Selected AH or Good-Cover Promotion and HYM Certificate v1

## Result

```text
rank_one_torsion_free_reflexive_hull_theorem_proved = true
conditional_AH_to_full_stability_bridge_proved = true
conditional_HYM_bridge_proved = true
selected_AH_or_goodcover_source_emitted = false
selected_Gauduchon_chamber_source_proved = false
full_stability_proved = false
full_HYM_proved = false
selected_HYM_operator_source_verified = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

This artifact closes the honest promotion bridge, not the selected source
itself. The destabilizer problem is no longer the main blocker: rank-one
torsion-free destabilizers reduce to line-bundle reflexive hulls, and the
reduced AH enumeration can promote once the selected AH/good-cover source is
emitted.

## Reflexive-Hull Reduction

Let F be a rank-one torsion-free coherent subsheaf of the rank-two holomorphic bundle V_alpha on the selected smooth complex threefold. The double dual F** is a reflexive rank-one sheaf, hence a line bundle on the smooth locus used by the AH/good-cover section algebra; the inclusion F -> V_alpha extends after saturation to an inclusion of the line-bundle reflexive hull whenever F is destabilizing. Since the quotient is torsion in codimension at least two, c1(F)=c1(F**) and F has the same selected slope as F**. Therefore it is enough to test the AH/good-cover line classes enumerated in the previous artifact.

## Selected Source Status

```text
AH_representative_constructed = true
AH_degree_product_law_verified = true
AH_reduced_boundaries_promoted_conditionally = true
AH_selected_by_mtt = false
AH_neutral_pic0_selected_by_mtt = false
AH_target_branch_selected_by_mtt = false
literal_goodcover_table_selected = false
pullback_cech_fixture_only = true
```

## HYM and Chamber Gate

```text
conditional_HYM_bridge_proved = true
full_HYM_proved = false
target_wall_equivalent_radius_ratio = r1:r2 = sqrt(2):1
target_wall_source_certified = false
integral_lift_source_certified = false
selected_Gauduchon_chamber_source_proved = false
```

## What Closes

- `rank_one_torsion_free_destabilizer_reduces_to_reflexive_line_hull` = `true`
- `reduced_AH_stability_promotes_conditionally_once_selected_source_is_supplied` = `true`
- `Li_Yau_HYM_bridge_ready_if_selected_stability_and_Gauduchon_chamber_supplied` = `true`
- `remaining_blocker_identified_as_source_selection_not_destabilizer_enumeration` = `true`

## Still Open

- `selected_AH_representative_or_literal_goodcover_Cech_source`
- `operator_layer_neutral_Pic0_selection_or_quotient`
- `selected_target_branch_L_over_swapped_branch`
- `selected_Gauduchon_chamber_source`
- `selected_HYM_connection_values`
- `selected_HYM_operator_source_values`
- `selected_RouteC_residual_values`
- `same_source_ChernWeil_GS_row`
- `same_source_D_E_Riesz_Green_dotD`
- `primitive_C1_contractions`
- `finite_part_or_spectrum`
- `lambda_12`
- `full_SM_or_no_knob_closure`

## Guardrails

- Do not treat an unselected AH representative as MTT-selected source data.
- Do not treat the pullback Cech validator fixture as a selected good-cover table.
- Do not apply HYM existence as an unconditional operator-source certificate.
- Do not compute lambda_12 until same-source U1/Y operator values and finite determinant data are emitted.
- Do not use observed electroweak data or benchmark flavor entries to choose the missing source.

## Decision

```text
strongest_result = Rank-one torsion-free destabilizers reduce to reflexive line hulls, and reduced AH stability promotes to full stability plus Li-Yau/HYM only after selected AH/good-cover and Gauduchon sources are supplied.
next_required_object = Selected_U1Y_Selected_AH_GoodCover_Source_or_RouteC_SelectedResidual_v1
alternative_next_object = Selected_U1Y_Selected_RouteC_Residual_Values_and_DEDotD_Payload_v1
```
