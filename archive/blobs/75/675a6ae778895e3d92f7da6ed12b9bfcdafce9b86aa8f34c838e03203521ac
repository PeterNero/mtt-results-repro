# Selected U1 Threshold Carrier Projector or SU2 Operator Spectrum v1

## Result

The `2/3` source theorem survives the stricter promotion audit, but it is not
yet promoted.  The current corpus contains the right carrier shape, not the
selected threshold operator packet.

```text
rank_three_carrier_shape_found = true
source_selected_u1_carrier_found = false
quotient_projector_P_perp_found = false
su2_unit_index_or_spectrum_found = true
promoted_to_selected_threshold_index = false
measured_electroweak_closure = false
```

## Rank-Quotient Replay

```text
raw_rank_from_candidate_carrier = 3
raw_projector_trace = 3
central_shared_directions_removed_if_projector_is_supplied = 1
would_give_U1_weight = 2/3
matches_source_theorem_weight = true
```

This is useful: the known factorized Iwasawa carrier has exactly the shape
needed for the source theorem.  It still cannot be used as selected proof data
because its own packet marks `selected_by_mtt=false`.

## U1 Promotion Tests

- `rank_three_projective_carrier_shape`: shape=true, promotable=false
  Reason: The sibling packet has the correct rank-3 projective carrier shape, but selected_by_mtt is false and selected gerbe source is not verified.
- `sector_projector_shape`: shape=true, promotable=false
  Reason: The available sector projector is identity on the family block; it does not supply the quotient projector P_perp that removes the shared central mode.
- `same_source_operator_fusion`: shape=true, promotable=false
  Reason: Ordered-source validation now passes, but the packet is fixture_only, selected_by_mtt is false, and same_source_for_ordered_L_pic0_GS_and_DE is false.

## SU2 Promotion Tests

- `flat_background_universal_fp_branch`: CONDITIONAL_CLOSURE_BRANCH, promotable=true
  Reason: The later selected flat FP quotient-normalization policy closes the field-independent flat ghost term for weak-split gauge-kinetic accounting.
- `selected_su2_threshold_background_flatness`: SU2_THRESHOLD_BACKGROUND_FLATNESS_CLOSED_FP_POLICY_OPEN, promotable=true
  Reason: Theta II/III select the flat/trivial SU2 leading threshold background and eliminate the need for a non-flat FP spectrum at this order.
- `selected_flat_fp_quotient_policy`: FLAT_FP_QUOTIENT_NORMALIZATION_POLICY_CLOSED_FOR_WEAK_SPLIT, promotable=true
  Reason: The FP determinant is the quotient projection Jacobian.  If it is field-independent along physical directions, it is representative-measure normalization rather than an interacting threshold term.
- `curved_nonabelian_fp_operator`: OPEN_SELECTED_SPECTRUM_REQUIRED, promotable=true
  Reason: The curved branch no longer blocks the leading weak-split gate because selected flatness makes a non-flat FP spectrum unnecessary in this scoped accounting.

## Source-Theorem Hypotheses After This Gate

- `H1_three_direction_u1_threshold_carrier`: SHAPE_FOUND_NOT_SELECTED
- `H2_exactly_one_shared_central_universal_mode`: SUPPORTED_BUT_NOT_OPERATOR_BOUND
- `H3_physical_quotient_removes_shared_mode`: PROJECTOR_MISSING
- `H4_SU2_unit_index_or_selected_spectrum`: CLOSED_FOR_WEAK_SPLIT_BY_FLATNESS_AND_FP_QUOTIENT_POLICY
- `H5_no_target_selection`: CLOSED

## Minimal Packet That Would Close This Gate

U1:

- selected_by_mtt true for the rank-3 U1 threshold carrier
- same-source identification of the shared central-circle basis vector
- explicit quotient projector P_perp with trace 2 on the selected carrier
- operator/determinant statement that the U1 threshold trace uses P_perp

SU2:

- closed for weak-split accounting by selected SU2 flatness and flat FP quotient-normalization policy

Scheme:

- same normalization scheme as Qa/SU3 log(2008)
- no lambda_12 or measured electroweak data as selection input

## Guardrails

- A rank-3 candidate carrier is not a selected U1 threshold carrier.
- The identity family projector is not the shared-circle quotient projector P_perp.
- The SU2 closure is scoped to weak-split gauge-kinetic threshold accounting and must not be reused for vacuum energy or absolute partition-function normalization.
- This gate may be used as a no-go certificate for the current U1 source record, not as electroweak closure.

## Next Required Object

```text
Same_Source_Selected_U1_Carrier_Projector_Theorem_v1
```
