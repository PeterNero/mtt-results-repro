from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "qg_actual_dg_frontier_synthesis_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    checks = cert["checks"]
    frontier = cert["frontier"]
    supersession = cert["supersession"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(checks.values()), "one or more frontier synthesis checks failed")
    require(
        cert["status"]
        == "Q79_LOW_ENERGY_QG_EFT_PARITY_CLOSED_HETEROTIC_PRIMARY_UV_ROUTE_SELECTED_FIXED_GENUS_INHERITANCE_CONDITIONAL_WORLDSHEET_AND_NONPERTURBATIVE_COMPLETION_OPEN",
        "frontier status changed",
    )
    require(
        supersession["current_evidentiary_status"] == "SUPERSEDED_AS_UNCONDITIONAL_PROOF",
        "old Boolean acceptance was not demoted",
    )
    remaining = frontier["remaining_minimal_selection_theorem"]
    require(len(remaining["must_prove"]) == 3, "remaining theorem is not sharply typed")
    require(
        remaining["clause_status"]["same_circle"]
        == "FINITE_SAME_SOURCE_MAP_CLOSED_GLOBAL_LINE_IDENTITY_NOGO_COVARIANT_BUNDLE_REPLACEMENT_CLOSED",
        "same-circle clause lost its no-go/covariant replacement",
    )
    require(
        remaining["clause_status"]["q79_odd_lift_route"]
        == "SELECTED_SIDE_STRICT_SPIN_NOGO_SPINC_REPRESENTATION_LIFT_CLOSED",
        "q79 selected-side Spin/SpinC decision was lost",
    )
    require(
        remaining["clause_status"]["primitive_physical_branch"]
        == "UNAUGMENTED_CURRENT_MTT_SELECTION_CLOSED_NOGO_BY_TWO_BRANCH_AUTOMORPHISM_ONE_DISCRETE_Q79_REALIZATION_AXIOM_SUFFICIENT",
        "primitive branch non-derivability or one-axiom completion was lost",
    )
    require(
        remaining["clause_status"]["q79_branch_HYM_globalization"]
        == "FINITE_ROOTSTACK_REYNOLDS_TT_OPERATOR_CLOSED_CONTINUUM_FM_HYM_OPTIONAL_STRONGER_ROUTE_2_OF_11_OPEN",
        "q79 spectral-symbol/HYM clause changed",
    )
    require(
        remaining["clause_status"]["UV_completion_route"]
        == "LOW_ENERGY_INTERACTING_QG_EFT_PARITY_CLOSED_Q79_HETEROTIC_PRIMARY_ROUTE_SELECTED_FIXED_GENUS_INHERITANCE_CONDITIONAL_WORLDSHEET_5_AVAILABLE_2_PARTIAL_ALL_GENUS_NONPERTURBATIVE_OPEN",
        "interacting low-energy/UV clause changed",
    )
    require(
        "target-independent physical-realization functional" in remaining["must_prove"][0]
        and "one discrete axiom A_QG" in remaining["must_prove"][0]
        and "two-branch automorphism countermodel" in remaining["must_prove"][0]
        and "h_DE=0" in remaining["must_prove"][0]
        and "h_DD=h_EE=kappa_e>0" in remaining["must_prove"][0]
        and "normalized S3 Reynolds functional" in remaining["must_prove"][0]
        and "neither the 11-row Fourier-Mukai contract nor a continuum HYM calculation blocks this tier"
        in remaining["must_prove"][0]
        and "2 of 11 rows available" in remaining["must_prove"][0],
        "finite operator exit or optional continuum boundary is no longer explicit",
    )
    require(
        "c2=9u and c3=plus-or-minus-6 are simultaneously realizable"
        in remaining["must_prove"][2]
        and "topology and the necessary Hodge-type condition are no longer blockers"
        in remaining["must_prove"][2],
        "new simultaneous clutching theorem was not carried to the UV cutset",
    )
    require(
        "necessary Hodge-type condition are no longer blockers"
        in remaining["must_prove"][2]
        and "A151 certifies 16 of 71" in remaining["must_prove"][2]
        and "L1 weight 36 of 123" in remaining["must_prove"][2]
        and "remaining 55 intervals" in remaining["must_prove"][2]
        and "closes the covariant z-chart adapter" in remaining["must_prove"][2],
        "A151 or Fu-Yau Hodge progress was not carried to the UV cutset",
    )
    require(tiers["explicit_zero_fit_metric_source_realization"] == "CLOSED", "explicit realization lost")
    require(
        tiers["same_circle_weight2_obstruction_theorem"] == "CLOSED",
        "weight-two obstruction theorem lost",
    )
    require(
        tiers["same_circle_unique_odd_root_selection"] == "OPEN",
        "odd root was overclaimed",
    )
    require(tiers["q79_w2_formula_and_branch_6H"] == "CLOSED", "q79 w2 result lost")
    require(
        tiers["trial_identity_q79_strict_Spin_decision"] == "CLOSED_NO_GO",
        "exact trial Spin decision lost",
    )
    require(
        tiers["executed_selected_side_q79_strict_Spin_decision"] == "CLOSED_NO_GO",
        "selected-side strict-Spin no-go was lost",
    )
    require(
        tiers["signed_sheet_SpinC_representation_lift"] == "CLOSED",
        "signed-sheet SpinC lift was lost",
    )
    require(
        tiers["SpinC_determinant_shared_circle_flat_bridge"] == "CLOSED_ROOT_INDEPENDENT",
        "root-independent shared determinant bridge was lost",
    )
    require(
        tiers["finite_same_source_emission_of_central_map"] == "CLOSED_UNIQUE",
        "finite same-source central map was lost",
    )
    require(
        tiers["q79_shared_circle_single_traversal_odd_sign"]
        == "CLOSED_MINUS_IDENTITY_ROOT_INDEPENDENT"
        and tiers["q79_shared_circle_double_return_odd_state"]
        == "CLOSED_IDENTITY_ROOT_INDEPENDENT"
        and tiers["q79_weight_two_metric_blindness_to_halfturn"]
        == "CLOSED_EXACT"
        and tiers["q79_same_source_finite_CLN_nil_complex"]
        == "CLOSED_EXACT_ACYCLIC_OVER_CHARACTERISTIC_NOT_TWO",
        "the double-return or finite CLN Nil theorem was lost",
    )
    require(
        tiers["double_return_alone_forces_zero_metric_strain"] == "CLOSED_NO_GO"
        and tiers["canonical_zero_defect_Minkowski_endpoint"] == "CLOSED_EXACT"
        and tiers["dynamic_selection_of_zero_defect_endpoint"] == "OPEN"
        and tiers["pregeometric_perfect_closure_to_physical_flat_vacuum_bridge"]
        == "OPEN",
        "the flat endpoint was lost or silently promoted to a selected vacuum",
    )
    require(
        tiers["exact_curved_Ricci_flat_helicity_two_wave"] == "CLOSED_CONSTRUCTED"
        and tiers["vacuum_Einstein_TEGR_equations_select_flat_endpoint"]
        == "CLOSED_NO_GO"
        and tiers["double_return_plus_Lambda_zero_select_flat_endpoint"]
        == "CLOSED_NO_GO"
        and tiers["zero_defect_state_boundary_selection_contract"]
        == "OPEN_5_ROWS_0_AVAILABLE"
        and tiers["selected_positive_defect_ground_state_functional"] == "OPEN",
        "the vacuum flatness no-go or state-selector cutset was lost",
    )
    require(
        tiers["determinant_flat_HYM_on_branch_complement"] == "CLOSED",
        "flat HYM determinant connection was lost",
    )
    require(
        tiers["resolved_rootstack_flat_HYM_carrier"] == "CLOSED",
        "resolved root-stack HYM carrier was lost",
    )
    require(
        tiers["q79_unbranched_strain_map_natural_uniqueness"] == "CLOSED_EXACT"
        and tiers["q79_coarse_finite_flat_strain_bridge_extension"]
        == "CLOSED_NO_GO_DISCRIMINANT_CUBED"
        and tiers["q79_full_S3_cusp_monodromy_orders"]
        == "CLOSED_EXACT_2_3_2_1"
        and tiers["q79_minimal_full_monodromy_rootstack"]
        == "CLOSED_UNIQUE_MINIMAL"
        and tiers["q79_rootstack_rank_six_metric_connection_bridge"]
        == "CLOSED_EXACT_FLAT_HYM"
        and tiers["q79_strict_same_source_rank_preserving_continuation"]
        == "CLOSED_UNIQUE_MINIMAL_FULL_MONODROMY_ROOTSTACK",
        "full-monodromy rank-six root-stack bridge was lost",
    )
    require(
        tiers["q79_spectral_sheet_symbol_to_rootstack_strain_carrier"]
        == "CLOSED_EXACT"
        and tiers["q79_strain_symbol_normalized_overlap_metric"]
        == "CLOSED_EXACT_IDENTITY"
        and tiers["literal_full_inverse_Fourier_Mukai_HYM_connection_identity"]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        and tiers["actual_q79_inverse_Fourier_Mukai_visible_bundle"]
        == "OPEN_GERBE_AND_LOCAL_FREENESS"
        and tiers["actual_q79_balanced_HYM_connection"] == "OPEN"
        and tiers["q79_dynamic_projected_HYM_TT_Hessian"]
        == "OPEN_ACTUAL_OPERATOR_CONDITIONAL_SCALAR_FORM_CLOSED"
        and tiers["q79_full_relative_phase_neutrality"]
        == "OPEN_EXACT_REDUCTION_GIVEN"
        and tiers["primitive_MTT_selection_of_physical_rootstack_realization"]
        == "OPEN",
        "root-stack spectral-symbol/HYM boundary was lost or overpromoted",
    )
    require(
        tiers["q79_finite_projected_rootstack_TT_Hessian"]
        == "CLOSED_EXACT_IDENTITY_SHAPE_ZERO_DIMENSIONLESS_FITS"
        and tiers["q79_finite_projected_rootstack_JDE_invariance"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and tiers["q79_finite_operator_overall_normalization"]
        == "OPEN_ONE_EFFECTIVE_SCALE"
        and tiers["rank2_HYM_row_model_equals_rank3_q79_spectral_bundle"]
        == "CLOSED_NO_GO_TYPE_MISMATCH",
        "finite Reynolds operator exit was lost or overpromoted",
    )
    require(
        tiers["q79_canonical_complement_lane_complex_structure"] == "CLOSED_EXACT"
        and tiers["q79_quarterturn_Hessian_scalarization"] == "CLOSED_EXACT"
        and tiers["q79_physical_TT_block_scalarization"]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and tiers["single_rank_one_FuYau_order4_symmetry"] == "CLOSED_NO_GO"
        and tiers["minimal_four_branch_FuYau_Chern_orbit"] == "CLOSED_EXACT"
        and tiers["shared_Z64_unique_order4_subgroup"] == "CLOSED_EXACT"
        and tiers["shared_Z64_odd_root_C4_restriction"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and tiers["active_FuYau_parent_integral_C4_action"]
        == "CLOSED_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and tiers["free_C4_orbit_covariance_scalarizes_branch_Hessian"]
        == "CLOSED_NO_GO"
        and tiers["autonomous_Lens_descent_scalarizes_Hessian"]
        == "CLOSED_EXACT_CONDITIONAL"
        and tiers["MTT_types_C4_as_Lens_redundancy"]
        == "CLOSED_NO_GO_IN_CURRENT_MARKED_SHARED_CIRCLE_SETUP_UNMARKED_REFORMULATION_OPEN"
        and tiers["marked_shared_circle_C4_autonomous_descent"]
        == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and tiers["unmarked_modular_parent_descent_contract"]
        == "OPEN_5_ROWS_0_AVAILABLE"
        and tiers["square_theta_direct_adjoint_preserves_strain"]
        == "CLOSED_NO_GO"
        and tiers["square_theta_direct_adjoint_realizes_JDE"]
        == "CLOSED_NO_GO"
        and tiers["determinant_twisted_exterior_square_edge_identification"]
        == "CLOSED_EXACT"
        and tiers["shared_root_C4_to_flat_rootstack_strain_JDE_functor"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and tiers["JDE_parallel_under_minimal_rootstack_flat_connection"]
        == "CLOSED_EXACT"
        and tiers["direct_unital_Herm3_adjoint_realizes_full_JDE"]
        == "CLOSED_NO_GO"
        and tiers["nontrivial_inverse_Fourier_Mukai_induced_JDE"]
        == "OPEN_EXTENSION_FROM_FLAT_SYMBOL_TO_ACTUAL_HYM"
        and tiers["typed_lane_quarterturn_to_FuYau_source_functor"]
        == "CLOSED_CONDITIONAL_AT_FLAT_SYMBOL_AND_FUYAU_PARENT_REPRESENTATION_TIER_ACTUAL_HYM_EXTENSION_OPEN"
        and tiers["selected_HYM_action_quarterturn_invariance"] == "OPEN",
        "quarter-turn Hessian reduction was lost or overpromoted",
    )
    require(
        tiers["MTT_selection_of_resolved_rootstack_or_equivalent"] == "OPEN",
        "resolved carrier selection was overclaimed",
    )
    require(
        tiers["selected_resolved_or_twisted_HYM_branch_extension"]
        == "STRICT_SAME_SOURCE_MINIMAL_ROOTSTACK_CLOSED_PRIMITIVE_PHYSICAL_SELECTION_OPEN",
        "branch-extension tier did not advance cleanly",
    )
    require(
        tiers["global_internal_external_line_identity"] == "CLOSED_NO_GO",
        "global internal/external line no-go was lost",
    )
    require(
        tiers["global_covariant_helicity2_DG_bundle"]
        == "CLOSED_FOR_CONSTRUCTED_REALIZATION",
        "global covariant DG bundle was lost",
    )
    require(
        tiers["selected_branch_q79_Z64_QWW_source_realization"]
        == "CLOSED_UNIQUE_UP_TO_GAUGE"
        and tiers["selected_branch_metric_source_fitted_parameters"]
        == "CLOSED_ZERO",
        "selected-branch q79/Z64/QWW factorization was lost",
    )
    require(
        tiers["global_TT_Hessian_form"]
        == "CLOSED_UNDER_STATED_STABILITY_AND_COVARIANCE_HYPOTHESES",
        "global TT Hessian form was lost",
    )
    require(
        tiers["strain_to_metric_Hessian_transport"]
        == "CLOSED_EXACT_FACTOR_ONE_QUARTER",
        "Hessian coordinate transport was lost",
    )
    require(
        tiers["Fierz_Pauli_operator_uniqueness"]
        == "CLOSED_CONDITIONAL_ON_FOUR_EXPLICIT_ACTION_HYPOTHESES",
        "Fierz-Pauli uniqueness reduction was lost",
    )
    require(
        tiers["finite_closure_Hessian_self_adjointness"]
        == "CLOSED_FROM_C3_SCALAR_FUNCTIONAL",
        "finite closure Hessian reciprocity was lost",
    )
    require(
        tiers["selected_MTT_action_hypotheses"]
        == "REDUCED_TO_LOCAL_DIFF_NATURAL_VARIATIONAL_SOURCE_AND_TWO_DERIVATIVE_IR",
        "action source reduction changed",
    )
    require(
        tiers["nonlinear_Einstein_metric_completion"]
        == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES",
        "conditional nonlinear Einstein completion was lost",
    )
    require(
        tiers["independent_stress_normalization"]
        == "CLOSED_NONE_BEYOND_KAPPA_H",
        "an independent stress knob was reintroduced",
    )
    require(
        tiers["scale_free_q79_data_fix_numeric_Newton"] == "CLOSED_NO_GO"
        and tiers["dimensionful_GR_normalization"]
        == "OPEN_ONE_EFFECTIVE_NORMALIZATION_PROVED_NECESSARY",
        "Newton-scale no-go or parameter count changed",
    )
    require(
        tiers["classical_GR_equivalence_at_declared_finite_source_IR_tier"]
        == "CLOSED_CONDITIONAL_WITH_KAPPA_AND_LAMBDA"
        and tiers["classical_GR_dimensionless_gravity_shape_parameters"]
        == "CLOSED_ZERO"
        and tiers["classical_GR_effective_law_parameter_count"] == 2
        and tiers["full_selected_classical_GR"]
        == "CLOSED_CONDITIONAL_ON_PRIMITIVE_PHYSICAL_TIER_SELECTION_AND_TWO_EFFECTIVE_VALUES"
        and tiers["full_quantum_gravity"] == "OPEN",
        "conditional two-parameter classical closure or quantum boundary changed",
    )
    require(
        tiers["free_q79_massless_graviton_quantization"]
        == "CLOSED_EXACT_TWO_HELICITIES_CONDITIONAL_CAUSAL_VACUUM"
        and tiers["free_q79_graviton_new_parameters_beyond_kappa"]
        == "CLOSED_ZERO"
        and tiers["finite_internal_trace_as_4D_UV_completion"]
        == "CLOSED_NO_GO"
        and tiers["interacting_low_energy_quantum_GR_EFT"]
        == "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER"
        and tiers["q79_quantum_GR_EFT_observable_functor"]
        == "CLOSED_AT_PARITY_STANDARD_CONDITIONAL_ON_DECLARED_WILSON_DATA_AND_STATE"
        and tiers["standard_EFT_BRST_BV_structure"]
        == "IMPORTED_STANDARD_EFT_STRUCTURE_NOT_DERIVED_FROM_MTT"
        and tiers["Einstein_graph_superficial_degree"]
        == "CLOSED_EXACT_2L_PLUS_2"
        and tiers["two_loop_Goroff_Sagnotti_divergence"]
        == "CLOSED_NONZERO_STANDARD_RESULT"
        and tiers["two_parameter_interacting_quantum_GR_at_all_scales"]
        == "CLOSED_NO_GO"
        and tiers["interacting_quantum_measure_and_constraint_closure"]
        == "OPEN_AS_PRIMITIVE_MTT_OR_NONPERTURBATIVE_DERIVATION"
        and tiers["MTT_selected_higher_derivative_Wilson_values"] == "OPEN"
        and tiers["full_interacting_quantum_gravity"]
        == "OPEN_ALL_SCALE_UV_COMPLETE_TIER",
        "free/EFT quantum closure or interacting UV boundary changed",
    )
    require(
        tiers["UV_completion_route_selection"]
        == "CLOSED_PRIMARY_Q79_HETEROTIC_STRING_INHERITANCE"
        and tiers["fixed_genus_q79_heterotic_UV_inheritance"]
        == "CLOSED_CONDITIONAL_THEOREM"
        and tiers["q79_worldsheet_contract"]
        == "OPEN_5_OF_12_AVAILABLE_2_PARTIAL"
        and tiers["q79_explicit_degree_two_K3_incidence_GLSM"]
        == "CLOSED_EXACT"
        and tiers["q79_rank_one_FuYau_divisor_source"]
        == "CLOSED_EXACT_DELTA_EQUALS_H_MINUS_L_SQUARE_MINUS4"
        and tiers["q79_reference_source_free_Bianchi"]
        == "CLOSED_EXACT_CONDITIONAL_9_PLUS_11_PLUS_4_EQUALS_24"
        and tiers["q79_full_heterotic_bundle_and_local_TLSM_anomaly"]
        == "PARTIAL_LOCAL_ANOMALY_CLOSED_PHYSICAL_NONPULLBACK_BUNDLE_OPEN"
        and tiers["q79_aggregate_local_TLSM_anomaly"]
        == "CLOSED_EXACT_A_EQUALS_2_DELTA_DELTA_T"
        and tiers["q79_active_TLSM_fiber_radius_squared"] == "CLOSED_EXACT_2"
        and tiers["q79_aggregate_rank12_Fermi_monad"]
        == "CLOSED_EXACT_C1_ZERO_C2_20_ANOMALY_EQUIVALENCE_TIER"
        and tiers["q79_separate_odd_SU3_SU9_Picard_line_monads"]
        == "CLOSED_EXACT_NOGO"
        and tiers["q79_standard_TLSM_pullback_visible_c3"]
        == "CLOSED_EXACT_ZERO_NOGO_FOR_THREE_FAMILIES"
        and tiers["q79_smooth_nonpullback_SU3_c2_9u_c3_plusminus6"]
        == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE"
        and tiers["q79_nonpullback_c2_9u_c3_plusminus6_Hodge_admissibility"]
        == "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE"
        and tiers["q79_twisted_spectral_continuous_root_tubes"]
        == "CLOSED_EXACT_90_OF_90"
        and tiers["q79_twisted_spectral_handle_and_global_surface_relation"]
        == "CLOSED_EXACT_TWO_HANDLES"
        and tiers["q79_twisted_spectral_integral_H2_presentation"]
        == "CLOSED_EXACT_92_COLUMNS"
        and tiers["q79_twisted_spectral_period_table_and_effective_quotient"]
        == "CLOSED_FLOATING_8X92_AND_EXACT_Z90_QUOTIENT"
        and tiers["q79_twisted_spectral_weighted_E32_intervals"]
        == "PARTIAL_EXACT_16_OF_71_L1_36_OF_123_Z_ADAPTER_CLOSED"
        and tiers["q79_twisted_spectral_integral_branch"]
        == "OPEN_REMAINING_55_INTERVALS_WEIGHTED_AND_FROZEN_CARRIER_DECISION"
        and tiers["q79_physical_nonpullback_SU3_SU9_worldsheet_EJ"].startswith(
            "OPEN"
        )
        and tiers["q79_finite_discrete_torsion_phase"]
        == "CLOSED_EXACT_81_OF_81"
        and tiers["q79_modular_character_seed_reduction"]
        == "CLOSED_EXACT_7_ORBITS"
        and tiers["q79_selected_finite_twisted_group_algebra"]
        == "CLOSED_EXACT_MAT3C"
        and tiers["q79_unique_finite_projective_module"]
        == "CLOSED_EXACT_DIMENSION_3"
        and tiers["q79_finite_topological_torus_index"]
        == "CLOSED_EXACT_ONE"
        and tiers["q79_seven_seed_stabilizer_induction"]
        == "CLOSED_EXACT_FINITE_LAYER"
        and tiers["q79_finite_covariance_reduction_below_seven_seeds"]
        == "CLOSED_NO_GO"
        and tiers["q79_full_heterotic_partition_function"]
        == "OPEN_SEVEN_SEED_CHARACTERS_GSO_AND_FACTORIZATION"
        and tiers["q79_all_genus_convergence"] == "OPEN"
        and tiers["q79_nonperturbative_UV_completion"] == "OPEN",
        "heterotic UV inheritance tiers changed or were overpromoted",
    )
    require(
        tiers["selected_local_diffeomorphism_natural_action_source"] == "OPEN"
        and tiers["selected_Lambda_eff"] == "OPEN",
        "selected action or cosmological term was overpromoted",
    )
    require(
        tiers["closure_potential_alone_as_GR_kinetic_source"] == "CLOSED_NO_GO"
        and tiers["coframe_torsion_as_literal_nonclosure_source"] == "CLOSED_EXACT"
        and tiers["TEGR_Einstein_Hilbert_boundary_identity"] == "CLOSED_EXACT",
        "closure-anholonomy/TEGR bridge was lost",
    )
    require(
        tiers["direct_two_derivative_action_exit"]
        == "EXACT_TELEPARALLEL_CANDIDATE_CONSTRUCTED_SELECTION_OPEN"
        and tiers["global_Lorentzian_coframe_existence_under_declared_v4_inputs"]
        == "CLOSED_CONDITIONAL"
        and tiers["flat_teleparallel_connection_existence_from_global_coframe"]
        == "CLOSED_CONSTRUCTED"
        and tiers["local_QWW_to_ADM_coframe_map"]
        == "CLOSED_EXACT_UNDER_TYPED_BUNDLE_IDENTIFICATION"
        and tiers["ADM_metric_and_volume_from_QWW"] == "CLOSED_EXACT"
        and tiers["lapse_shift_as_fit_parameters"]
        == "CLOSED_NONE_CONSTRAINT_FIELDS"
        and tiers["QWW_transition_law_matches_spatial_tetrad_cocycle"]
        == "CLOSED_EXACT"
        and tiers["QWW_global_soldering_after_typed_identification"]
        == "CLOSED_CONDITIONAL"
        and tiers["QWW_inner_spatial_bundle_identification_after_invertibility"]
        == "CLOSED_AUTOMATIC"
        and tiers["same_source_Q_WW_to_global_coframe_identification"]
        == "REDUCED_TO_CAUCHY_SUPPORT_AND_OUTER_TANGENT_IDENTIFICATION_ONLY"
        and tiers["global_Lorentzian_coframe_lift_from_MTT"] == "OPEN"
        and tiers["local_orientation_invariance_of_G_equal_QTQ"] == "CLOSED_EXACT"
        and tiers["metric_descent_selects_TEGR_constitutive_vector"]
        == "CLOSED_UNIQUE_CONDITIONAL"
        and tiers["frame_neutrality_principal_symbol_selects_TEGR_vector"]
        == "CLOSED_EXACT"
        and tiers["TEGR_nonlinear_frame_neutrality_sufficiency_mod_boundary"]
        == "CLOSED_EXACT"
        and tiers["independent_TEGR_constitutive_parameters_after_metric_descent"]
        == "CLOSED_NONE"
        and tiers["MTT_selection_of_metric_descent_and_no_extra_frame_modes"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY"
        and tiers["MTT_identifies_teleparallel_representatives_as_neutrality_equivalent"]
        == "OPEN"
        and tiers["MTT_selection_of_TEGR_constitutive_vector"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
        "teleparallel direct action exit was lost or overpromoted",
    )
    require(
        tiers["strict_same_source_candidate_orientation_fiber_neutrality"]
        == "CLOSED_CHARACTERIZATION"
        and tiers["strict_same_source_candidate_TEGR_action_form"]
        == "CLOSED_UNIQUE_AT_TWO_DERIVATIVE_IR_ORDER"
        and tiers["strict_same_source_candidate_classical_GR"]
        == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY"
        and tiers["canonical_QWW_pullback_metric"] == "CLOSED_EXACT_UNIQUE"
        and tiers["metric_observable_choice_given_QWW"]
        == "CLOSED_NO_REMAINING_CHOICE"
        and tiers["selected_branch_q79_Z64_QWW_source_realization"]
        == "CLOSED_UNIQUE_UP_TO_GAUGE"
        and tiers["primitive_MTT_selection_of_current_metric_source_realization"]
        == "CLOSED_NODERIVABILITY_FROM_CURRENT_ABSTRACT_CORPUS_ONE_DISCRETE_AXIOM_COMPLETION_AVAILABLE"
        and tiers["primitive_MTT_selection_of_canonical_Lorentzian_realization"]
        == "OPEN_INPUT_IN_CURRENT_CORPUS",
        "strict same-source candidate action closure was lost or overpromoted",
    )
    require(
        tiers["quadratic_TT_to_unique_nonlinear_action"] == "CLOSED_NO_GO",
        "quadratic-to-nonlinear action no-go was lost",
    )
    require(
        tiers["spectral_action_same_operator_SM_gravity_architecture"]
        == "CLOSED_ARCHITECTURALLY"
        and tiers["selected_product_spectral_action"] == "OPEN"
        and tiers["selected_Einstein_IR_limit_of_spectral_action"]
        == "PARTIAL_A4_RATIO_CLOSED_FULL_REMAINDER_OPEN",
        "spectral-action exit was lost or overpromoted",
    )
    require(
        tiers["active_A49_spectral_Majorana_invariants"]
        == "CLOSED_ZERO_FOR_DIRAC_ONLY_BRANCH"
        and tiers["spectral_a4_dimensionless_Einstein_Weyl_ratio"]
        == "CLOSED_CONDITIONAL_ON_A53_ONE_ATOM_TIER"
        and tiers["spectral_full_heat_kernel_remainder_bound"] == "OPEN"
        and tiers["bare_spectral_vacuum_small_or_cancelled"] == "CLOSED_NO",
        "spectral a4 IR calculation or its boundary was lost",
    )
    require(
        tiers["pure_lambda15_carrier_as_physical_massless_graviton"] == "CLOSED_NO_GO",
        "positive-gap massless-pole no-go was lost",
    )
    require(
        tiers["coherent_zero_mode_massless_TT_source"]
        == "CLOSED_GEOMETRIC_UNIT_INTERNAL_RESIDUE",
        "geometric zero-mode source row was lost",
    )
    require(
        tiers["selected_action_fusion_of_zero_and_lambda15_channels"] == "OPEN",
        "zero/gap action fusion was overpromoted",
    )
    require(
        tiers["Stieltjes_massless_permanent_Gaussian_conjunction"] == "CLOSED_NO_GO",
        "Stieltjes/massless/Gaussian no-go was lost",
    )
    require(
        tiers["all_loop_finiteness_on_positive_massless_route"] == "OPEN_NOT_PROVED",
        "all-loop finiteness was overpromoted",
    )
    require(
        tiers["ordinary_dual_and_exterior_square_preserve_HYM"]
        == "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR"
        and tiers["ordinary_dual_or_exterior_square_realizes_JDE"]
        == "CLOSED_NO_GO"
        and tiers["nonzero_c3_chiral_branch_complex_linear_self_duality"]
        == "CLOSED_NO_GO"
        and tiers["nonlocal_same_branch_Fourier_Mukai_JDE_autoequivalence"]
        == "OPEN_EXACT_11_ROW_KERNEL_EXT1_HESSIAN_CONTRACT_2_AVAILABLE",
        "ordinary HYM functor no-go or derived-kernel cutset changed",
    )
    require(
        tiers["primitive_branch_two_branch_automorphism_countermodel"]
        == "CLOSED_EXACT"
        and tiers["minimal_extra_physical_realization_data"]
        == "CLOSED_ONE_DISCRETE_AXIOM_ZERO_CONTINUOUS_KNOBS"
        and tiers["q79_geometry_operator_choice_after_A_QG"]
        == "CLOSED_UNIQUE_UP_TO_DECLARED_GAUGE"
        and tiers["augmented_MTT_low_energy_QG_law_after_A_QG"]
        == "CLOSED_CONDITIONAL_ON_KAPPA_LAMBDA_EFT_DATA_AND_STATE"
        and tiers["unique_or_forced_MTT_physical_selection"]
        == "OPEN_UNAUGMENTED_ONE_AXIOM_COMPLETION_AVAILABLE",
        "primitive branch cutset or one-axiom completion changed",
    )
    require(guards["claims_unique_MTT_selection_closed"] is False, "selection guard failed")
    require(guards["claims_full_quantum_gravity_closed"] is False, "QG overclaim")
    require(guards["claims_final_integral_branch_selected"] is False, "integral branch overclaim")
    require(guards["claims_A53_point_measure_selected"] is False, "point-measure overclaim")
    require(guards["claims_full_spectral_remainder_controlled"] is False, "spectral remainder overclaim")
    require(guards["claims_spectral_vacuum_problem_solved"] is False, "vacuum overclaim")
    require(
        guards["claims_Q_WW_already_is_global_Lorentzian_coframe"] is False
        and guards["claims_MTT_already_selects_TEGR_constitutive_vector"] is False,
        "teleparallel selection overclaim",
    )
    require(
        guards["claims_basin_local_fixed_point_uniqueness_selects_physical_geometry"]
        is False
        and guards["claims_one_axiom_completion_is_derived_from_upper_MTT_dynamics"]
        is False,
        "primitive branch-selection guardrail changed",
    )
    require(
        guards["claims_double_return_dynamically_forces_zero_metric_defect"]
        is False
        and guards["claims_flat_spacetime_has_no_time_or_space"] is False
        and guards[
            "claims_zero_defect_Minkowski_is_selected_without_Lambda_eff_zero"
        ]
        is False,
        "double-return or flat-vacuum guardrail changed",
    )
    require(
        guards["claims_vacuum_Einstein_or_TEGR_equations_select_Minkowski"]
        is False
        and guards["claims_Lambda_eff_zero_is_sufficient_for_flat_vacuum"]
        is False
        and guards["claims_double_return_excludes_Ricci_flat_gravitational_waves"]
        is False,
        "vacuum-equation selection guardrail changed",
    )
    require(
        guards["claims_abstract_quarterturn_match_is_typed_FuYau_source_functor"]
        is False
        and guards["claims_free_C4_orbit_covariance_scalarizes_one_branch"]
        is False
        and guards["claims_direct_square_theta_adjoint_realizes_JDE"] is False
        and guards[
            "claims_flat_symbol_JDE_functor_is_actual_inverse_Fourier_Mukai_HYM_functor"
        ]
        is False
        and guards["claims_direct_unital_Herm3_adjoint_can_realize_full_JDE"]
        is False
        and guards["claims_ordinary_dual_or_exterior_square_realizes_JDE"] is False
        and guards["claims_opposite_chirality_dual_branch_is_same_selected_branch"]
        is False
        and guards["claims_derived_equivalence_automatically_preserves_HYM_Hessian"]
        is False
        and guards["claims_unmarked_modular_parent_preserves_marked_shared_circle"]
        is False
        and guards["claims_shared_circle_c3_clutching_is_C4_equivariant"] is False
        and guards["claims_MTT_types_C4_as_Lens_redundancy"] is False
        and guards["claims_selected_HYM_action_quarterturn_invariance"] is False
        and guards["claims_actual_projected_HYM_operator_computed"] is False
        and guards["claims_finite_rootstack_operator_is_continuum_balanced_HYM"]
        is False
        and guards[
            "claims_conditional_classical_tier_is_primitive_unconditional_selection"
        ]
        is False
        and guards["claims_free_graviton_quantization_is_interacting_QG"] is False
        and guards["claims_finite_internal_trace_regulates_4D_loops"] is False
        and guards["claims_standard_EFT_quantization_is_derived_from_MTT"]
        is False
        and guards["claims_fixed_order_EFT_is_UV_completion"] is False
        and guards["claims_kappa_and_Lambda_are_all_interacting_quantum_parameters"]
        is False
        and guards["claims_finite_torsion_phase_is_full_heterotic_partition_function"]
        is False
        and guards["claims_unique_projective_module_is_full_closed_string_spectrum"]
        is False
        and guards["claims_finite_seed_induction_constructs_tau_dependent_characters"]
        is False
        and guards["claims_fixed_genus_string_finiteness_is_all_genus_convergence"]
        is False
        and guards["claims_first_order_FuYau_background_is_exact_worldsheet_CFT"]
        is False
        and guards["claims_exact_K3_incidence_GLSM_is_full_heterotic_TLSM"]
        is False
        and guards["claims_9_11_4_reference_Bianchi_is_local_TLSM_anomaly_matrix"]
        is False
        and guards["claims_aggregate_rank12_monad_is_physical_SU3_plus_SU9"]
        is False
        and guards["claims_local_ch2_anomaly_selects_c3_clutching"] is False
        and guards["claims_topological_c3_clutching_is_holomorphic_HYM"] is False
        and guards["claims_q79_heterotic_UV_complete_QG_closed"] is False,
        "quarter-turn source or HYM guardrail changed",
    )

    print(
        "AUDIT_PASS: global covariant DG, selected-side SpinC, finite same-source "
        "map, discriminant branch no-go, minimal full-monodromy rank-six root-stack "
        "bridge, spectral sheet-symbol bridge, nonzero-Chern full-connection "
        "no-go, root-independent C4 parent and flat-symbol JDE functor, "
        "free-orbit, direct-adjoint, and ordinary dual/exterior HYM no-gos, "
        "plus the nonlocal 11-row derived-kernel cutset, "
        "conditional Lens theorem but marked shared-circle descent no-go, Hessian/FP, exact "
        "root-independent double return, finite acyclic CLN Nil complex, exact "
        "zero-defect Minkowski endpoint, exact curved-vacuum counterexample and state cutset, "
        "the exact finite Reynolds TT operator, two-parameter conditional classical GR tier, "
        "free two-helicity q79 graviton quantization and finite-internal UV no-go, "
        "interacting low-energy QG EFT parity and its exact two-loop UV boundary, "
        "the selected q79 heterotic UV route, conditional fixed-genus inheritance, "
        "the explicit degree-two K3 incidence GLSM and rank-one Fu-Yau divisor source, "
        "and exact 81-sector to seven-seed modular reduction, "
        "the exact two-branch primitive-selection no-go and minimal one-discrete-axiom completion, "
        "TEGR candidate and nonlinear Einstein/stress reductions, "
        "propagator no-gos, and the conditional spectral a4 IR ratio are closed; "
        "the q79 zero-mode row is exact, while the full action/remainder, one Newton "
        "scale, state/boundary zero-defect selection, Lambda, selected Wilson values, "
        "primitive MTT derivation of the realization axiom and quantum measure, exact q79 "
        "worldsheet CFT, all-genus control, and nonperturbative UV completion remain"
    )


if __name__ == "__main__":
    main()
