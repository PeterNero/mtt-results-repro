# Dual Attack Local Determinant or Omega0 Source v1

## Result

Both frontier paths were attacked in parallel.

```text
lane_A_lambda12_closed = false
lane_A_reduced_to_selected_spectral_table = true
lane_B_Omega0_closed = false
lane_B_reduced_to_alpha_phys_only = true
full_physical_electroweak_closure = false
target_fitting_used = false
```

## Lane A: Local Determinant

Status:

```text
OPEN_SELECTED_GAUGE_FACTOR_SPECTRAL_TABLE_REQUIRED
```

Closed inputs:

```text
determinant_accounting_interface_closed = True
qc_circle_block_closed_for_weak_split = True
su2_flat_fp_policy_closed_for_weak_split = True
u1_shared_circle_index_closed = True
```

Strongest selected inputs:

```text
selected_p_Qc_for_weak_split = 2.442340583291322
selected_p_SU2_for_weak_split = -1.1961941178318218
selected_U1_threshold_index = 2/3
v1_tilde = 0.405623467693425
```

Diagnostics that remain non-proof:

```text
scalar_unit_lambda_12 = 3.040437642207233
gut_three_fifths_lambda_12 = 2.063501408890704
two_thirds_proxy_lambda_12 = 2.226324114443459
two_thirds_proxy_delta_g12 = 0.0718623805729687
target_witness_lambda_12 = 2.194153126940556
target_witness_delta_g12 = 0.07082394967589342
```

Blocker:

```text
selected_spectra_computed = False
final_attempt_status = FINAL_DETERMINANT_COMPUTATION_BLOCKED_BY_SPECTRAL_UNDERDETERMINATION
minimal_next_object = selected gauge-factor-resolved spectral table with U1/hypercharge, SU2, and SU3/Qa index weights
```

Decision:

```text
The lane is advanced to an exact executable determinant interface with Qc and SU2 weak-split blocks closed, but lambda_12 remains open because the selected U1/hypercharge local determinant spectrum and full index-weighted spectral table are not source-emitted.
```

## Lane B: Omega0

Status:

```text
REDUCED_TO_ALPHA_PHYS_OR_ACTION_UNIT_ONLY
```

Closed inputs:

```text
character_channel_dQ_closed = True
C_UV_internal_imported = 0.405623467693425
rho_UV_internal_closed = 0.164530397543639
s_star_closed = 1.464646774701829
C_Q_equals_1_closed = True
epsilon_equals_1_over_448_closed = True
chi_omega_equals_1_closed = True
```

Reduced formula:

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
Omega0_over_sqrt_alpha_phys = 1.5675093859261626
omega_gap_phys = Omega0 / s_star
omega_gap_phys_over_sqrt_alpha_phys = 1.0702303196927971
Lambda_gap_phys = sqrt(15) * Omega0 / s_star
Lambda_gap_phys_over_sqrt_alpha_phys = 4.144984204776443
formula_check_sqrt_15_over_log_448 = 1.5675093859261626
```

Blocker:

```text
alpha_phys_or_action_unit_selected = False
physical_Omega0_numeric_closed = False
minimal_next_object = Selected_Physical_Alpha_or_Action_Unit_Theorem_v1
```

Decision:

```text
The lane advances: Omega0 is no longer blocked by C_Q, epsilon_adm, chi_omega, C_UV, or Q_tau on the imported character-channel branch. It is reduced to the single physical action-unit primitive alpha_phys.
```

## Cross-Lane Independence

```text
can_substitute_lane_b_for_lane_a = False
reason = Omega0 fixes physical units/common normalization. It does not emit the gauge-factor-dependent determinant difference lambda_12.
can_substitute_lane_a_for_lane_b = False
reason_2 = lambda_12 fixes a dimensionless weak-split threshold. It does not select a physical inverse-length/action unit.
joint_closure_condition = Need both alpha_phys and lambda_12/Delta_a^sel, plus convention map, mu_match, and RG/threshold scheme, before measured electroweak comparison.
```

## Source Checks

```text
frontier_loaded = True
local_interface_closed = True
local_final_still_blocked = True
qc_closed = True
su2_policy_closed = True
two_thirds_near_hit_not_proof = True
character_channel_imported = True
omega0_reduced = True
sharp_semigroup_closed = True
omega_convention_closed = True
omega_factor_matches_formula = True
```

## Guardrails

- Do not promote the two-thirds proxy lambda_12 near-hit to proof.
- Do not use the diagnostic target witness lambda_12 as determinant data.
- Do not treat Omega0/alpha_phys as a substitute for gauge-factor threshold spectra.
- Do not treat lambda_12 as a physical unit or compactification action anchor.
- Do not compare to measured electroweak data until alpha_phys, lambda_12, convention map, mu_match, and RG scheme are all selected.

## Next Required Objects

- Selected_Gauge_Factor_Spectral_Table_v1
- Selected_Physical_Alpha_or_Action_Unit_Theorem_v1
- Typed_Electroweak_Convention_Map_and_RG_Scheme_v1
