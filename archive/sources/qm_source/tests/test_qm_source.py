from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mtt_qm_source.build import (
    apparatus_frame_normalization,
    basin_born_reduction,
    canonical_pq_hazard_rigidity,
    canonical_damping_pointer_dilation,
    canonical_q79_hessian_recorder_source,
    canonical_q79_minimal_recorder_action,
    canonical_cauchy_quantum_model,
    canonical_q79_fock_output_measure,
    canonical_pq_penrose_semigroup_bridge,
    canonical_pq_instrument_nonuniqueness,
    cauchy_slice_quantum_kinematics,
    one_anchor_physical_clock_lift,
    penrose_profile_dependence_nogo,
    anchor_free_penrose_profile_factor,
    capture_descent_reduction,
    effect_frame_reduction,
    finite_kinematics,
    fixed_point_clock_nogo,
    framed_q79_free_dirac_car_net,
    interaction_channel_extraction,
    one_axiom_born_completion,
    preparation_selection_nogo,
    preparation_moment_reduction,
    q79_cauchy_normal_euclidean_metric_rigidity,
    q79_boundaryless_bv_bfv_gluing_phase_reduction,
    q79_bulk_to_boundary_dirac_family_source_cutset,
    q79_cofinal_free_bv_cutoff_and_interacting_counterterm_cutset,
    q79_euclidean_reflection_free_physical_os_el_cutset,
    q79_firstorder_costello_bv_graphwise_counterterm,
    q79_auxiliary_spectral_fixed_coupling_eg_first_tangent_bridge,
    q79_fixed_coupling_regulated_cstar_promotion_criterion,
    q79_gaugefixed_laplace_and_interior_heat_kernel,
    q79_heat_kernel_counterterm_seed_and_qme_induction_cutset,
    q79_lorentzian_spectral_sp_qme_cauchy_bridge,
    q79_continuum_sm_classical_bv_composition,
    q79_covariant_projective_module_hym_symbol_naturality_cutset,
    q79_explicit_cech_projector_connection_compiler_cutset,
    q79_intrinsic_spectral_strain_quotient_shorted_hessian_cutset,
    q79_physical_family_source_dependency_analytic_completion_cutset,
    q79_temporal_companion_free_shell_independence,
    q79_orbitwise_finite_spectral_chiral_measure_cutset,
    q79_uniform_gauss_ghostzero_brst_ward_defect_reduction,
    q79_sm_based_gauge_frame_regulator_orbit,
    q79_sm_boundary_crossing_line_reduction,
    q79_sm_determinant_phase_torsor_quotient,
    q79_sm_diffeomorphism_transported_regulator_orbit,
    q79_sm_equicausal_formal_state_transport,
    q79_sm_free_physical_cstar_reference_and_nonpromotion,
    q79_sm_finite_shell_bv_pushforward_regulator_comparison,
    q79_sm_gauge_compatible_finite_bv_regulator_criterion,
    q79_sm_gaugefixed_hyperbolic_bv_equicausal,
    q79_sm_local_auxiliary_elliptic_bv_regulator,
    q79_sm_local_formal_physical_state,
    q79_sm_local_formal_state_space_gluing,
    q79_sm_renormalized_timeordering_local_qme,
    quadratic_hazard_capture,
    selected_context_source_functor,
    shared_circle_marked_poisson_actualization,
    source_freshness,
)


class QmSourceTestCase(unittest.TestCase):
    def test_sources_are_hash_pinned_and_current(self) -> None:
        certificate = source_freshness()
        self.assertTrue(certificate["all_current"])
        self.assertEqual(len(certificate["sources"]), 42)
        self.assertEqual(
            {row["role"] for row in certificate["sources"]},
            {
                "theorem_authority",
                "selected_branch_authority",
                "executable_authority",
                "conditional_support",
                "diagnostic_only",
            },
        )

    def test_finite_kinematics_is_exact_but_not_physical_completion(self) -> None:
        certificate = finite_kinematics()
        self.assertTrue(certificate["all_exact_checks_pass"])
        self.assertEqual(certificate["carrier"]["fiberwise_complex_dimension"], 6)
        self.assertEqual(certificate["blocker_readiness"]["B.QM.02_physical_time_and_energy"], "open")
        self.assertEqual(certificate["complex_structures"]["intertwiner_between_carriers"], "OPEN_NOT_ASSUMED")

    def test_cauchy_hilbert_functor_is_exact_but_physical_dynamics_stays_open(self) -> None:
        certificate = cauchy_slice_quantum_kinematics()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["status"],
            "SELECTED_CAUCHY_FINITE_SYMBOL_HILBERT_FUNCTOR_CLOSED_EXACT_PHYSICAL_PROPAGATOR_AND_LAB_COMPARISON_OPEN",
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.02_gauge_comparison_functor"],
            "closed_exact_zero_error",
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.02_selected_inter_slice_propagator"],
            "open",
        )
        self.assertEqual(
            certificate["exact_witness"]["global_projector_ranks"],
            [6, 12],
        )
        self.assertEqual(
            certificate["exact_witness"]["dynamics_counterexample_ranks"],
            [8, 10],
        )
        self.assertFalse(
            certificate["type_guards"]["imports_A52_profile_product_triple"]
        )

    def test_canonical_binary_operational_model_completes_declared_qm02_exit(self) -> None:
        certificate = canonical_cauchy_quantum_model()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["blocker_assessment"]["B.QM.02_exit_certificate"],
            "complete_at_canonical_q79_binary_one_anchor_finite_symbol_tier",
        )
        self.assertEqual(
            certificate["exact_checkpoint"][
                "basis_preparation_effect_probabilities"
            ],
            ["1/448", "149/448", "149/224"],
        )
        self.assertEqual(
            certificate["exact_checkpoint"]["eventual_record_probabilities"],
            ["1/3", "2/3"],
        )
        self.assertEqual(
            certificate["exact_checkpoint"]["informative_noise_multiplicity"],
            2,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "strict_unaugmented_upper_MTT_selection_of_clock_anchor"
            ],
            "open",
        )
        self.assertIn(
            "not identified",
            certificate["free_graviton_fock_type_guard"]["nonidentification"],
        )

    def test_fock_output_measure_closes_canonical_second_moment_descent(self) -> None:
        certificate = canonical_q79_fock_output_measure()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["B_QM_01_assessment"]["exit_certificate"],
            "complete_at_canonical_q79_binary_one_anchor_operational_output_measure_tier",
        )
        self.assertEqual(
            certificate["B_QM_01_assessment"][
                "canonical_binary_SecondMomentCaptureDescent"
            ],
            "closed_exact",
        )
        self.assertEqual(
            certificate["exact_checkpoint"]["q79_ready_p_q_probabilities"],
            ["1/448", "149/448", "149/224"],
        )
        self.assertEqual(
            certificate["exact_checkpoint"]["equal_density_selected_p_weights"],
            ["1/2", "1/2"],
        )
        self.assertEqual(
            certificate["exact_checkpoint"]["unequal_fourth_moment_p_weights"],
            ["1/2", "1/4"],
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_structural_stochastic_primitives_for_output_measure"
            ],
            0,
        )
        self.assertEqual(
            certificate["B_QM_01_assessment"][
                "objective_single_history_actualization"
            ],
            "open",
        )

    def test_framed_q79_free_dirac_net_closes_declared_qft_tier(self) -> None:
        certificate = framed_q79_free_dirac_car_net()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["B_QFT_01_assessment"]["exit_certificate"],
            (
                "complete_at_selected_q79_framed_free_massless_dirac_"
                "even_observable_net_tier"
            ),
        )
        self.assertEqual(
            certificate["exact_witness"]["q79_projector_ranks_on_dirac_carrier"],
            [8, 16],
        )
        self.assertEqual(
            certificate["exact_witness"]["chirality_projector_ranks"],
            [2, 2],
        )
        self.assertEqual(
            certificate["parameter_ledger"]["new_continuous_parameters"],
            0,
        )
        self.assertEqual(
            certificate["B_QFT_01_assessment"]["full_interacting_or_SM_QFT"],
            "open",
        )
        self.assertIn(
            "not selected",
            certificate["state_space"]["preferred_state"],
        )

    def test_q79_continuum_sm_classical_bv_composition_advances_qft02(self) -> None:
        certificate = q79_continuum_sm_classical_bv_composition()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["carrier_ledger"][
                "three_family_left_Weyl_internal_dimension"
            ],
            48,
        )
        self.assertEqual(
            certificate["carrier_ledger"][
                "continuum_left_Weyl_component_dimension"
            ],
            96,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_typed_continuum_SM_carrier"
            ],
            "closed_exact",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_classical_BRST_and_BV_CME"
            ],
            "closed_exact_on_the_composed_continuum_field_stack",
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.QFT.02_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_continuous_parameters_from_composition"
            ],
            0,
        )
        self.assertIn(
            "not the 48-state",
            certificate["relation_to_q79_free_carrier"]["not_identified"],
        )

    def test_q79_sm_gauge_fixed_hyperbolic_equicausal_tier(self) -> None:
        certificate = q79_sm_gaugefixed_hyperbolic_bv_equicausal()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_witness"]["A57_beta_vector"],
            ["41/10", "-19/6", "-7"],
        )
        self.assertEqual(
            certificate["exact_witness"]["s_h_plus_h_s"],
            [["1", "0"], ["0", "1"]],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_gauge_fixed_hyperbolic_free_BV_complex"
            ],
            "closed_on_declared_onshell_background_chart",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_equicausal_Peierls_star_and_time_slice_algebra"
            ],
            "closed_on_declared_background_chart",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_unrestricted_microcausal_closure"
            ],
            "superseded_false_in_general_by_primary_counterexample",
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.QFT.02_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )
        self.assertIn(
            "not a positive physical",
            certificate["equicausal_algebra"]["positivity_boundary"],
        )

    def test_q79_sm_renormalized_timeordering_and_local_qme_tier(
        self,
    ) -> None:
        certificate = q79_sm_renormalized_timeordering_local_qme()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["local_QME_anomaly"]["class_vector"],
            [0, 0, 0, 0, 0],
        )
        self.assertEqual(
            certificate["global_anomaly_boundary"][
                "SU2_doublets_total"
            ],
            12,
        )
        self.assertEqual(
            certificate["global_anomaly_boundary"]["Witten_parity"],
            0,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_interacting_time_ordered_products"
            ],
            (
                "closed_as_formal_Epstein_Glaser_products_on_declared_"
                "charts"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_all_orders_perturbative_QME_scheme"
            ],
            (
                "closed_by_exact_one_loop_zero_plus_Adler_Bardeen_"
                "and_renormalized_BV_theorems"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_global_spin_gauge_anomaly_obstruction"
            ],
            "closed_zero_for_the_faithful_Z6_group",
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.QFT.02_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_local_formal_physical_state_tier(self) -> None:
        certificate = q79_sm_local_formal_physical_state()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_free_quartet"][
                "ghost_zero_closed_Gram"
            ],
            [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "0"]],
        )
        self.assertEqual(
            certificate["exact_free_quartet"][
                "physical_cohomology_Gram"
            ],
            [["1", "0"], ["0", "1"]],
        )
        self.assertEqual(
            certificate["free_field_extension"][
                "physical_gauge_polarizations_per_spatial_eigenmode"
            ],
            24,
        )
        self.assertEqual(
            certificate["free_field_extension"][
                "Weyl_complex_field_components"
            ],
            96,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_positive_physical_interacting_state"
            ],
            (
                "closed_as_local_formal_existence_on_bounded_H1_zero_"
                "q79_charts"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.QFT.02_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )
        self.assertIn(
            "not uniquely selected",
            certificate["formal_physical_representation"][
                "nonuniqueness"
            ],
        )

    def test_q79_sm_local_formal_state_space_gluing_tier(self) -> None:
        certificate = q79_sm_local_formal_state_space_gluing()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_local_formal_state_space_functor"
            ],
            "closed_exact_on_q79Chart_0",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_common_parent_finite_compatible_family"
            ],
            "closed_exact",
        )
        self.assertEqual(
            certificate["common_parent_compatible_family"][
                "exact_witness"
            ]["B_via_AB"],
            [["1/2", "0"], ["0", "1/2"]],
        )
        self.assertEqual(
            certificate["common_parent_compatible_family"][
                "exact_witness"
            ]["B_via_AB"],
            certificate["common_parent_compatible_family"][
                "exact_witness"
            ]["B_via_BC"],
        )
        self.assertEqual(
            certificate["arbitrary_gluing_no_go"][
                "Bell_XX_expectation"
            ],
            "1",
        )
        self.assertEqual(
            certificate["arbitrary_gluing_no_go"][
                "forced_product_XX_expectation"
            ],
            "0",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_arbitrary_overlap_state_sheaf_gluing"
            ],
            "impossible_in_general_by_exact_Bell_monogamy_witness",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_single_global_interacting_q79_state"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_equicausal_formal_state_transport_tier(self) -> None:
        certificate = q79_sm_equicausal_formal_state_transport()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_Hadamard_seed_witness"]["beta_first"],
            [
                ["1", "0", "2/7", "0", "12/49"],
                ["0", "1", "0", "6/7", "0"],
                ["0", "0", "1", "0", "12/7"],
                ["0", "0", "0", "1", "0"],
                ["0", "0", "0", "0", "1"],
            ],
        )
        self.assertEqual(
            certificate["exact_state_transport_witness"][
                "transported_density"
            ],
            [["34/75", "4/25"], ["4/25", "41/75"]],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_formal_physical_state_cone_transport"
            ],
            "closed_up_to_specified_formal_star_isomorphism",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_literal_interacting_local_quasi_equivalence"
            ],
            (
                "not_yet_well_typed_without_fixed_coupling_Cstar_"
                "von_Neumann_completion"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.QFT.02_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_free_physical_cstar_and_nonpromotion_tier(
        self,
    ) -> None:
        certificate = (
            q79_sm_free_physical_cstar_reference_and_nonpromotion()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_finite_Cstar_witness"][
                "tensor_basis_rank"
            ],
            64,
        )
        self.assertEqual(
            certificate["exact_finite_Cstar_witness"][
                "product_density"
            ],
            [
                ["3/10", "0", "0", "0", "0", "0", "0", "0"],
                ["0", "1/10", "0", "0", "0", "0", "0", "0"],
                ["0", "0", "1/5", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "1/15", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "3/20", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "1/20", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "1/10", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "1/30"],
            ],
        )
        self.assertEqual(
            certificate["fixed_coupling_nonpromotion_theorem"][
                "Hamiltonian_families"
            ]["lambda_one_probe_derivation_reference"],
            [["0", "-1"], ["0", "0"]],
        )
        self.assertEqual(
            certificate["fixed_coupling_nonpromotion_theorem"][
                "Hamiltonian_families"
            ]["lambda_one_probe_derivation_flat"],
            [["0", "-1/2"], ["0", "0"]],
        )
        self.assertEqual(
            certificate["fixed_coupling_nonpromotion_theorem"][
                "derivative_polynomials_0_through_12"
            ][1],
            [{"degree": 3, "coefficient": "1"}],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_free_physical_Cstar_reference_net"
            ],
            "closed_exact_at_lambda_zero",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_formal_to_fixed_nonzero_coupling_promotion"
            ],
            (
                "nonunique_without_extra_nonperturbative_selection_by_"
                "exact_flat_ambiguity"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_interacting_fixed_coupling_Cstar_net"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_hodge_spectral_regulator_criterion_and_type_nogo(
        self,
    ) -> None:
        certificate = (
            q79_sm_gauge_compatible_finite_bv_regulator_criterion()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_nested_spectral_family_witness"][
                "cutoff_ranks"
            ],
            {"0": 2, "1": 4, "4": 6, "9": 8},
        )
        self.assertEqual(
            certificate["exact_q79_quartet_hodge_witness"][
                "Hodge_laplacian"
            ],
            [
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0"],
                ["0", "0", "1", "0", "0", "0"],
                ["0", "0", "0", "1", "0", "0"],
                ["0", "0", "0", "0", "1", "0"],
                ["0", "0", "0", "0", "0", "1"],
            ],
        )
        self.assertEqual(
            certificate["internal_projector_nonpromotion_theorem"][
                "accepted_complete_physical_regulator_sources"
            ],
            [],
        )
        self.assertEqual(
            certificate["finite_Wilsonian_pushforward_witness"][
                "effective_Hessian"
            ],
            [["5/2", "1/2"], ["1/2", "7/6"]],
        )
        self.assertEqual(
            certificate["finite_Wilsonian_pushforward_witness"][
                "determinants"
            ],
            {
                "det_full": "16",
                "det_high": "6",
                "det_effective": "8/3",
            },
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_selected_external_BV_Laplacian_and_domain"
            ],
            "open_single_operator_domain_package",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_local_auxiliary_elliptic_bv_regulator_exists(
        self,
    ) -> None:
        certificate = q79_sm_local_auxiliary_elliptic_bv_regulator()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_principal_symbol_witness"]["covectors"][
                -1
            ]["covector"],
            [1, 2, 3, 4],
        )
        self.assertEqual(
            certificate["exact_principal_symbol_witness"]["covectors"][
                -1
            ]["norm_squared"],
            "30",
        )
        self.assertTrue(
            certificate["principal_symbol_checks"][
                "direct_sum_full_linear_BV_principal_complex_is_elliptic"
            ]
        )
        self.assertEqual(
            certificate["regulator_capability"][
                "accepted_local_auxiliary_operator_sources"
            ],
            ["q79_local_auxiliary_elliptic_BV_package"],
        )
        self.assertEqual(
            certificate["regulator_capability"][
                "accepted_complete_physical_regulator_sources"
            ],
            [],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_selected_external_BV_Laplacian_and_domain"
            ],
            "open_or_replaceable_by_regulator_choice_independence",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_finite_shell_bv_pushforward_and_comparison(
        self,
    ) -> None:
        certificate = (
            q79_sm_finite_shell_bv_pushforward_regulator_comparison()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_contractible_shell_witness"][
                "restricted_quadratic_determinant"
            ],
            "-36",
        )
        self.assertEqual(
            certificate["crossing_cutset"]["spectral_flow"],
            1,
        )
        self.assertEqual(
            certificate["crossing_cutset"][
                "APS_negative_projector_ranks"
            ],
            {"s=-1": 2, "s=0": 1, "s=1": 1},
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_UV_Hodge_Lagrangian_cycle"
            ],
            (
                "closed_for_every_positive_finite_BV_Hodge_"
                "compatible_shell"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_actual_q79_regulator_choice_independence"
            ],
            "open_five_component_obstruction_vector",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_based_gauge_frame_regulator_orbit(
        self,
    ) -> None:
        certificate = q79_sm_based_gauge_frame_regulator_orbit()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["boundary_result"]["APS_spectral_flow"],
            0,
        )
        self.assertEqual(
            certificate["boundary_result"]["BV_BFV_boundary_flux"],
            "0",
        )
        self.assertEqual(
            certificate["exact_boundary_interior_witness"][
                "shell_determinant"
            ],
            "4",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_actual_q79_regulator_path"
            ],
            (
                "closed_on_connected_boundary_identity_gauge_"
                "frame_orbit"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_regulator_choice_independence"
            ],
            "closed_on_presentation_orbit_open_on_quotient_moduli",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_sm_diffeomorphism_transported_regulator_orbit(
        self,
    ) -> None:
        certificate = (
            q79_sm_diffeomorphism_transported_regulator_orbit()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["boundary_result"][
                "transported_region_relative_APS_spectral_flow"
            ],
            0,
        )
        self.assertEqual(
            certificate["boundary_result"][
                "transported_region_relative_BV_BFV_flux"
            ],
            "0",
        )
        self.assertEqual(
            certificate["exact_transported_boundary_witness"][
                "shell_determinant"
            ],
            "4",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_transported_region_isotopy"
            ],
            (
                "closed_when_all_geometric_and_boundary_data_are_"
                "pushforwards"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_region_shape_or_embedding_choice"
            ],
            (
                "closed_mod_ambient_isotopic_pushforward_open_"
                "beyond_it"
            ),
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_cauchy_normal_euclidean_metric_rigidity(
        self,
    ) -> None:
        certificate = q79_cauchy_normal_euclidean_metric_rigidity()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_rational_witness"][
                "initial_scalar_principal_symbol"
            ],
            "1",
        )
        self.assertEqual(
            certificate["exact_rational_witness"][
                "boosted_scalar_principal_symbol"
            ],
            "41/9",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_auxiliary_positive_metric_formula"
            ],
            "closed_unique_given_future_unit_Cauchy_normal",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_full_local_Lorentz_boost_regulator_neutrality"
            ],
            "excluded_by_exact_scalar_symbol_counterexample",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_positive_metric_and_normal_choice_count"
            ],
            "reduced_from_two_named_rows_to_one_source_object",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_temporal_companion_free_shell_independence(
        self,
    ) -> None:
        certificate = (
            q79_temporal_companion_free_shell_independence()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_rational_normal_path"]["parameters"],
            ["0", "1/4", "1/2"],
        )
        self.assertEqual(
            certificate["positive_cutoff_crossing_theorem"][
                "projector_ranks"
            ],
            {"before": 6, "after": 2},
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_Cauchy_normal_Euclideanization_source"
            ],
            (
                "closed_as_auxiliary_quotient_for_normalized_free_"
                "finite_shell_observables"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_absolute_unnormalized_determinant_line"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_common_determinant_phase_is_a_normalized_torsor(
        self,
    ) -> None:
        certificate = q79_sm_determinant_phase_torsor_quotient()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_common_phase_witness"][
                "normalized_observable"
            ],
            {"real": "17/25", "imaginary": "-31/25"},
        )
        self.assertEqual(
            certificate["relative_phase_cutset"][
                "same_phase_sector_intensity"
            ],
            "4",
        )
        self.assertEqual(
            certificate["relative_phase_cutset"][
                "relative_i_sector_intensity"
            ],
            "2",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_absolute_common_determinant_phase"
            ],
            "excluded_as_unidentifiable_U1_convention_torsor",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_relative_phase_between_disconnected_sectors"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_APS_crossing_reduces_to_one_unselected_line(
        self,
    ) -> None:
        certificate = q79_sm_boundary_crossing_line_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_APS_crossing"]["negative_ranks"],
            {"minus": 2, "zero": 1, "plus": 1},
        )
        self.assertEqual(
            certificate["exact_APS_crossing"]["spectral_flow"],
            1,
        )
        self.assertEqual(
            certificate["shared_line_parity_shadow"][
                "crossing_value"
            ],
            {
                "spectral_flow": 1,
                "Z64_image": 32,
                "shared_sign_holonomy": "-1",
            },
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_source_free_crossing_phase_selection"
            ],
            "excluded_by_U1_stabilizer_nogo",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_flavor_holonomy_as_analytic_phase_source"
            ],
            "excluded_by_determinant_object_type_mismatch",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_full_relative_Dai_Freed_phase"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_boundary_source_is_typed_and_not_promoted(
        self,
    ) -> None:
        certificate = q79_bulk_to_boundary_dirac_family_source_cutset()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["continuum_circle_family"]["crossing"],
            {
                "a": "1",
                "mode": -1,
                "kernel": "span_C(exp(-i theta))",
                "crossing_form": "1",
                "spectral_flow": 1,
            },
        )
        self.assertEqual(
            certificate["continuum_circle_family"]["counterfamily"][
                "spectral_flow"
            ],
            0,
        )
        self.assertEqual(
            certificate["continuum_to_finite_Galerkin_homotopy"][
                "finite_endpoint"
            ],
            "H_1(t)=diag(-2,t,3)",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_bulk_to_boundary_Dirac_BFV_functor"
            ],
            "closed_conditional_exact_after_boundary_source_package",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_bulk_only_boundary_family_selection"
            ],
            "excluded_by_same_basepoint_sf_zero_vs_one_counterfamily",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_selected_physical_noncollar_boundary_family"
            ],
            "open_reduced_to_typed_boundary_source_package",
        )
        self.assertFalse(
            certificate["physical_source_contract"][
                "physical_crossing_kernel_line"
            ]["accepted"]
        )
        self.assertTrue(
            certificate["guardrails"]["shared_circle_is_not_physical_time"]
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_auxiliary_boundary_phase_cancels_without_a_physical_selector(
        self,
    ) -> None:
        certificate = q79_boundaryless_bv_bfv_gluing_phase_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_selected_physical_noncollar_boundary_family"
            ],
            "retired_as_false_exit_on_current_boundaryless_QFT_domain",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_auxiliary_boundary_phase_after_gluing"
            ],
            "closed_formal_exact_as_dual_line_cancellation",
        )
        for row in certificate["BV_BFV_gluing"][
            "finite_phase_witness"
        ].values():
            self.assertEqual(row["glued_real"], 1)
            self.assertEqual(row["glued_imaginary"], 0)
        self.assertEqual(
            certificate["parameter_ledger"][
                "retired_false_physical_source_rows"
            ],
            3,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_uniform_interacting_cutoff_removal"
            ],
            "open",
        )

    def test_free_cofinal_cutoff_closes_but_local_counterterms_remain(
        self,
    ) -> None:
        certificate = (
            q79_cofinal_free_bv_cutoff_and_interacting_counterterm_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_cofinal_free_BV_spectral_cutoff_family"
            ],
            "closed_on_each_admissible_compact_auxiliary_chart",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_raw_interacting_cutoff_removal"
            ],
            "excluded_without_local_counterterms",
        )
        rows = certificate["interacting_local_divergence_witness"]["rows"]
        self.assertEqual(rows[0]["local_diagonal_trace"], "1")
        self.assertEqual(rows[-1]["local_diagonal_trace"], "36")
        self.assertEqual(
            len(
                certificate[
                    "interacting_counterterm_comparison_contract"
                ]
            ),
            6,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_formal_EG_interacting_continuum_scheme"
            ],
            "remains_closed_not_reopened",
        )

    def test_heat_kernel_counterterm_seed_reduces_bridge_to_three_jobs(
        self,
    ) -> None:
        certificate = (
            q79_heat_kernel_counterterm_seed_and_qme_induction_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_exact_smooth_heat_regulator_seed"
            ],
            "closed_exact",
        )
        self.assertEqual(
            certificate["exact_dyadic_heat_kernel_seed"]["identities"][
                "Hodge_homotopy"
            ],
            "Q P_1^3+P_1^3 Q=H_1-H_3",
        )
        rows = certificate["exact_quadratic_local_counterterm_seed"][
            "rows"
        ]
        self.assertEqual(
            rows[-1]["divergent_quadratic_coefficient_D_N"],
            "36",
        )
        self.assertEqual(
            rows[-1]["Z_N_coefficients_in_1_g_hbar_g2_basis"],
            ["0", "1", "-36"],
        )
        self.assertEqual(
            set(certificate["independent_q79_work_packages"]),
            {"HK", "CT", "GLUE", "DERIVED"},
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_spectral_cutoff_to_EG_counterterm_bridge"
            ],
            "open_three_independent_q79_work_packages_HK_CT_GLUE",
        )

    def test_gaugefixed_laplace_operator_closes_local_HK(self) -> None:
        certificate = q79_gaugefixed_laplace_and_interior_heat_kernel()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["naive_adjoint_Hodge_no_go"][
                "base_transverse_value"
            ],
            "1",
        )
        self.assertEqual(
            certificate["naive_adjoint_Hodge_no_go"][
                "doubled_covector_transverse_value"
            ],
            "16",
        )
        self.assertTrue(
            certificate["principal_symbol_checks"][
                "every_gauge_detour_commutator_is_scalar_Laplace_type"
            ]
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_HK_selected_mixed_BV_heat_kernel_hypotheses"
            ],
            (
                "closed_on_declared_boundaryless_compact_support_"
                "auxiliary_Euclidean_regulator_tier"
            ),
        )
        self.assertEqual(
            {
                row["independent_work_package"]
                for row in certificate[
                    "bridge_reclassification"
                ].values()
                if row["independent_work_package"] is not None
            },
            {"CT", "EL"},
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_spectral_or_heat_to_EG_counterterm_bridge"
            ],
            "open_two_independent_work_packages_CT_and_EL",
        )

    def test_firstorder_costello_BV_closes_formal_CT(self) -> None:
        certificate = q79_firstorder_costello_bv_graphwise_counterterm()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["firstorder_gauge_BV_complex"][
                "fiber_dimensions_per_generator"
            ],
            [1, 7, 7, 1],
        )
        self.assertTrue(
            all(
                row["differential_ranks"] == [1, 6, 1]
                for row in certificate["firstorder_gauge_BV_complex"][
                    "principal_symbol_rows"
                ]
            )
        )
        self.assertTrue(
            all(
                all(row["checks"].values())
                for row in certificate["firstorder_gauge_BV_complex"][
                    "principal_symbol_rows"
                ]
            )
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_CT_graphwise_local_counterterms"
            ],
            "closed_at_every_finite_perturbative_bidegree",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_CT_QME_BRST_primitives"
            ],
            (
                "closed_by_zero_local_anomaly_class_and_all_orders_"
                "compatible_scheme"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_spectral_or_heat_to_EG_counterterm_bridge"
            ],
            "open_one_independent_work_package_EL",
        )
        self.assertEqual(
            {
                row["independent_work_package"]
                for row in certificate[
                    "bridge_reclassification"
                ].values()
                if row["independent_work_package"] is not None
            },
            {"EL"},
        )

    def test_q79_reflection_closes_free_physical_OS_and_sharpens_EL(
        self,
    ) -> None:
        certificate = (
            q79_euclidean_reflection_free_physical_os_el_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["pointwise_temporal_reflection"][
                "adapted_reflection"
            ],
            [
                ["-1", "0", "0", "0"],
                ["0", "1", "0", "0"],
                ["0", "0", "1", "0"],
                ["0", "0", "0", "1"],
            ],
        )
        self.assertEqual(
            len(certificate["global_reflection_contract"]["rows"]),
            8,
        )
        self.assertEqual(
            certificate["global_reflection_contract"][
                "accepted_selected_rows"
            ],
            0,
        )
        witness = certificate["free_physical_OS_theorem"][
            "exact_finite_witness"
        ]
        self.assertEqual(witness["rank"], 2)
        self.assertTrue(
            all(
                Fraction(value) >= 0
                for value in witness["principal_minors"]
            )
        )
        self.assertEqual(
            Fraction(witness["probe_OS_norm"]),
            Fraction(1273, 16384),
        )
        self.assertEqual(
            certificate["smooth_global_promotion_obstruction"][
                "metric_at_positive_sample"
            ][1][1],
            "5/4",
        )
        self.assertEqual(
            certificate["smooth_global_promotion_obstruction"][
                "theta_pullback_metric_at_positive_sample"
            ][1][1],
            "3/4",
        )
        self.assertEqual(
            len(certificate["analytic_Calderon_route"]["rows"]),
            6,
        )
        self.assertEqual(
            certificate["interacting_formal_OS_no_go"][
                "fixed_lambda_one_values"
            ],
            ["1", "-1/2"],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_EL_free_physical_OS_on_reflection_contract"
            ],
            "closed_exact_conditionally_at_finite_positive_shell",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_EL_overall"
            ],
            "open_sharpened",
        )

    def test_q79_direct_Lorentzian_regulator_closes_formal_EL_exit(
        self,
    ) -> None:
        certificate = (
            q79_lorentzian_spectral_sp_qme_cauchy_bridge()
        )
        self.assertTrue(certificate["all_checks_pass"])
        witness = certificate["exact_finite_Cauchy_witness"]
        self.assertEqual(
            witness["spectrum"],
            ["0", "0", "1", "1", "4", "4"],
        )
        self.assertEqual(
            witness["regulator_spectrum"],
            ["1", "1", "2", "2", "5", "5"],
        )
        self.assertEqual(
            witness["dyadic_heat_step_one"],
            [
                ["1/2", "0", "0", "0", "0", "0"],
                ["0", "1/2", "0", "0", "0", "0"],
                ["0", "0", "1/4", "0", "0", "0"],
                ["0", "0", "0", "1/4", "0", "0"],
                ["0", "0", "0", "0", "1/32", "0"],
                ["0", "0", "0", "0", "0", "1/32"],
            ],
        )
        self.assertEqual(
            len(certificate["direct_six_row_bridge"]),
            6,
        )
        self.assertTrue(
            all(
                row["accepted"]
                for row in certificate[
                    "direct_six_row_bridge"
                ].values()
            )
        )
        self.assertEqual(
            certificate["exact_QME_restoration_witness"][
                "restored_breaking"
            ],
            ["0", "0", "0", "0", "0", "0"],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_spectral_cutoff_to_EG_counterterm_bridge"
            ],
            "closed_six_of_six_at_local_formal_direct_Lorentzian_tier",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_EL_renormalized_equicausal_Cauchy_transport"
            ],
            "closed_at_formal_physical_H0_on_declared_q79_charts",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_fixed_coupling_regulated_Cstar_landing_and_promotion_cut(
        self,
    ) -> None:
        certificate = (
            q79_fixed_coupling_regulated_cstar_promotion_criterion()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "regulated_fixed_coupling"
            ],
            "5/5",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "0/9",
        )
        self.assertEqual(
            certificate["acceptance_counts"]["Borel_promotion"],
            "1/6",
        )
        witness = certificate[
            "exact_finite_compact_gauge_witness"
        ]
        self.assertEqual(witness["fixed_algebra_dimension"], 8)
        self.assertEqual(witness["witness_fixed_coupling"], "1/3")
        self.assertEqual(
            witness["Gauss_projector"],
            [
                ["1", "0", "0", "0"],
                ["0", "1", "0", "0"],
                ["0", "0", "0", "0"],
                ["0", "0", "0", "0"],
            ],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_fixed_nonzero_coupling_finite_regulator_Cstar"
            ],
            "closed_for_auxiliary_finite_regulators",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_fixed_nonzero_coupling_continuum_Cstar"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_auxiliary_spectral_fixed_coupling_EG_first_tangent(
        self,
    ) -> None:
        certificate = (
            q79_auxiliary_spectral_fixed_coupling_eg_first_tangent_bridge()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "regulated_fixed_coupling"
            ],
            "5/5",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "1/9",
        )
        self.assertEqual(
            certificate["acceptance_counts"]["Borel_promotion"],
            "1/6",
        )
        self.assertTrue(
            certificate["continuum_promotion_rows"][
                "formal_EG_tangent_identification"
            ]["accepted"]
        )
        self.assertFalse(
            certificate["continuum_promotion_rows"][
                "geometry_selected_q79_external_regulator_family"
            ]["accepted"]
        )
        witness = certificate["exact_finite_tangent_witness"]
        self.assertEqual(
            witness["observable_and_retarded_tangent"]["imaginary"],
            [
                ["0", "-1", "0", "0"],
                ["1", "0", "0", "0"],
                ["0", "0", "0", "0"],
                ["0", "0", "0", "0"],
            ],
        )
        self.assertEqual(
            certificate["SP_composite_probe_qualification"][
                "untransported_probe_mixed_tangent"
            ],
            "2",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_formal_EG_first_tangent_identification"
            ],
            (
                "closed_for_common_source_relative_S_and_cocycle_"
                "generator_on_the_auxiliary_gauge_covariant_spectral_"
                "family_at_formal_coefficientwise_tier_with_SP_"
                "transported_observables"
            ),
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_uniform_Gauss_ghostzero_BRST_Ward_reduction(
        self,
    ) -> None:
        certificate = (
            q79_uniform_gauss_ghostzero_brst_ward_defect_reduction()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "1/9",
        )
        self.assertFalse(
            certificate["continuum_promotion_rows"][
                "vanishing_Gauss_BRST_Ward_defect"
            ]["accepted"]
        )
        self.assertEqual(
            certificate["continuum_promotion_rows"][
                "vanishing_Gauss_BRST_Ward_defect"
            ]["reduced_to"],
            "full_nonabelian_chiral_measure_at_fixed_cutoff",
        )
        dependency_graph = certificate[
            "continuum_exit_dependency_graph"
        ]
        self.assertEqual(
            dependency_graph["independent_open_count"],
            7,
        )
        self.assertEqual(
            dependency_graph["dependent_open_rows"],
            ["vanishing_Gauss_BRST_Ward_defect"],
        )
        witness = certificate["exact_finite_witness"]
        self.assertEqual(witness["fixed_algebra_dimension"], 8)
        self.assertEqual(
            witness["exact_zero_defect_sequence"],
            ["0"] * 8,
        )
        self.assertNotEqual(
            witness["off_sector_BRST_defect"],
            [["0"] * 8 for _ in range(8)],
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_uniform_compact_gauge_norm_defect"
            ],
            (
                "closed_exact_zero_at_every_admitted_finite_regulator_"
                "and_in_every_Cstar_reduced_product"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_full_quantum_Ward_defect"
            ],
            (
                "open_dependency_reduced_to_full_nonabelian_chiral_"
                "measure_and_determinant_Jacobian"
            ),
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_orbitwise_finite_spectral_chiral_measure_cutset(
        self,
    ) -> None:
        certificate = (
            q79_orbitwise_finite_spectral_chiral_measure_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "orbitwise_finite_spectral_measure"
            ],
            "7/7",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "full_domain_measure_extension"
            ],
            "0/4",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "1/9",
        )
        self.assertFalse(
            certificate["continuum_promotion_rows"][
                "full_nonabelian_chiral_measure_at_fixed_cutoff"
            ]["accepted"]
        )
        self.assertFalse(
            certificate["continuum_promotion_rows"][
                "vanishing_Gauss_BRST_Ward_defect"
            ]["accepted"]
        )
        witness = certificate["exact_finite_witness"]
        self.assertEqual(
            set(witness["gauge_word_determinants"].values()),
            {"1"},
        )
        self.assertEqual(
            witness["Jacobian_defect_sequence"],
            ["0"] * 8,
        )
        self.assertEqual(
            witness["transported_top_wedge_Gram_determinant"],
            "1",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_orbitwise_finite_spectral_chiral_measure"
            ],
            (
                "closed_nonperturbatively_on_each_connected_gapped_"
                "anomaly_free_certified_presentation_component"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_full_nonabelian_chiral_measure"
            ],
            (
                "open_reduced_to_full_domain_locality_quotient_moduli_"
                "crossing_strata_and_disconnected_sector_gluing"
            ),
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_physical_family_source_dependency_and_completion(
        self,
    ) -> None:
        certificate = (
            q79_physical_family_source_dependency_analytic_completion_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "conditional_analytic_completion"
            ],
            "8/8",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "actual_physical_source_payload"
            ],
            "0/3",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "full_domain_measure_extension"
            ],
            "0/4",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "1/9",
        )
        selected_family = certificate[
            "full_domain_extension_rows"
        ][
            "selected_physical_chiral_projector_and_Hessian_family"
        ]
        self.assertFalse(selected_family["accepted"])
        self.assertEqual(
            selected_family["reduced_to"],
            ["B.HS.01", "B.GEO.01", "B.ACTION.01"],
        )
        nonpromotion = certificate[
            "exact_finite_nonpromotion_witness"
        ]
        self.assertEqual(nonpromotion["projector_rank"], 4)
        self.assertEqual(
            nonpromotion["projected_zero"],
            nonpromotion["projected_hidden"],
        )
        self.assertNotEqual(
            nonpromotion["Dirac_zero"],
            nonpromotion["Dirac_hidden"],
        )
        self.assertNotEqual(
            nonpromotion["Hessian_zero"],
            nonpromotion["Hessian_hidden"],
        )
        kato = certificate["exact_Kato_family_witness"]
        self.assertEqual(
            kato["Kato_generator_at_zero"],
            kato["Kato_velocity"],
        )
        self.assertEqual(kato["spectral_gap"], "3")
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.QFT.02_finite_source_to_smooth_family_selection"
            ],
            "excluded_by_exact_finite_projection_noninjectivity",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_covariant_projective_module_HYM_symbol_naturality(
        self,
    ) -> None:
        certificate = (
            q79_covariant_projective_module_hym_symbol_naturality_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "universal_projective_naturality"
            ],
            "10/10",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "physical_q79_same_source_instantiation"
            ],
            "0/3",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "full_domain_measure_extension"
            ],
            "0/4",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "continuum_reduced_product"
            ],
            "1/9",
        )
        bott = certificate["exact_nonzero_Chern_HYM_witness"]
        self.assertEqual(bott["first_Chern_number"], "1")
        self.assertEqual(
            bott["Chern_density"],
            (
                "Tr(p[partial_u p,partial_v p])="
                "2i/(1+u^2+v^2)^2"
            ),
        )
        lanes = certificate["external_lane_factor_theorem"]
        self.assertEqual(lanes["relative_lane_ranks"], [1, 2, 3])
        feshbach = certificate[
            "finite_compression_and_Feshbach_theorem"
        ]
        self.assertEqual(
            feshbach["coupled_residual_squared"],
            "1/4",
        )
        self.assertEqual(
            feshbach["self_energy_at_zero"],
            [["1/12", "0"], ["0", "0"]],
        )
        self.assertEqual(
            feshbach["Feshbach_operator_at_zero"],
            [["11/12", "0"], ["0", "2"]],
        )
        self.assertEqual(
            certificate["blocker_assessment"]["B.GEO.01_overall"],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_explicit_Cech_projector_connection_compiler(
        self,
    ) -> None:
        certificate = (
            q79_explicit_cech_projector_connection_compiler_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "explicit_Cech_connection_compiler"
            ],
            "12/12",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "physical_q79_same_source_instantiation"
            ],
            "0/3",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "independent_post_endpoint_symbol_selectors"
            ],
            0,
        )
        witness = certificate[
            "exact_shared_circle_witness"
        ]
        self.assertEqual(
            witness["winding_Grassmann_connection_terms"],
            [[[{
                "exponent": 0,
                "real": "0",
                "imag": "16/25",
            }]]],
        )
        self.assertEqual(
            witness["winding_connection_difference_terms"],
            [[[{
                "exponent": 0,
                "real": "0",
                "imag": "-23/75",
            }]]],
        )
        cutoff = certificate[
            "presentation_independence_and_cutoff_witness"
        ]["cutoff_leakage"]
        self.assertEqual(
            cutoff["1"]["leaked_norm_squared"],
            "16/25",
        )
        self.assertEqual(
            cutoff["1"]["retained_norm_squared"],
            "9/25",
        )
        hidden = certificate[
            "twisted_hidden_adjoint_compiler"
        ]
        self.assertEqual(
            hidden[
                "fundamental_products_with_nonzero_central_phase"
            ],
            36,
        )
        self.assertEqual(
            hidden["adjoint_composition_rows_checked"],
            729,
        )
        self.assertEqual(
            hidden["adjoint_composition_failures"],
            [],
        )
        self.assertEqual(
            certificate["rank_102_coupled_complex_compiler"][
                "total_rank_complex"
            ],
            102,
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.GEO.01_overall"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_q79_intrinsic_spectral_strain_quotient_and_shorted_Hessian(
        self,
    ) -> None:
        certificate = (
            q79_intrinsic_spectral_strain_quotient_shorted_hessian_cutset()
        )
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["acceptance_counts"][
                "intrinsic_spectral_strain_quotient"
            ],
            "14/14",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "physical_q79_same_source_instantiation"
            ],
            "0/3",
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "remaining_independent_dimensionless_TT_equalities_after_symmetry_lift"
            ],
            0,
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "physical_TT_shape_equalities_conditionally_forced"
            ],
            2,
        )
        self.assertFalse(
            certificate["acceptance_counts"][
                "physical_TT_shape_unconditionally_accepted"
            ]
        )
        self.assertEqual(
            certificate["acceptance_counts"][
                "remaining_structural_same_source_S3xC4_symmetry_lifts"
            ],
            1,
        )
        invariant_ring = certificate[
            "relative_phase_invariant_ring"
        ]
        self.assertEqual(
            invariant_ring["generic_real_dimension"],
            7,
        )
        self.assertEqual(
            invariant_ring["sample"]["triangle"],
            {"real": "-13", "imag": "9"},
        )
        self.assertEqual(
            invariant_ring["sample"]["relation_value"],
            "250",
        )
        linear_no_go = certificate[
            "linear_rank_six_subspace_no_go"
        ]
        self.assertEqual(
            linear_no_go["full_root_plane_character"],
            [6, 0, 0],
        )
        self.assertEqual(
            linear_no_go["selected_two_permutation_character"],
            [6, 2, 0],
        )
        self.assertIn(
            "must be nonlinear",
            linear_no_go["conclusion"],
        )
        comparison = certificate[
            "TT_Reynolds_comparison"
        ]
        self.assertFalse(
            comparison[
                "anisotropic_counterwitness"
            ]["one_scale_repairs"]
        )
        self.assertEqual(
            comparison["isotropic_witness"]["kappa_fin"],
            "1/2",
        )
        symmetry = certificate[
            "S3xC4_shorted_symmetry_inheritance"
        ]
        self.assertEqual(
            symmetry["TT_commutant_dimension"],
            1,
        )
        self.assertEqual(
            symmetry[
                "independent_dimensionless_TT_equalities_after_lift"
            ],
            0,
        )
        self.assertFalse(
            symmetry["exact_nonphysical_witness"][
                "physical_q79_endpoint"
            ]
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.GEO.01_direct_linear_Wfin_subspace_route"
            ],
            "excluded_by_relative_phase_and_S3_character_no_go",
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.GEO.01_TT_shape_equalities"
            ],
            (
                "conditional_implication_closed_exact_physical_"
                "instantiation_open_on_one_same_source_S3xC4_"
                "symmetry_lift"
            ),
        )
        self.assertEqual(
            certificate["blocker_assessment"][
                "B.GEO.01_overall"
            ],
            "open",
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_physical_continuous_parameters"
            ],
            0,
        )

    def test_born_result_is_a_reduction_not_a_source_claim(self) -> None:
        certificate = basin_born_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["blocker_readiness"]["B.QM.01_preparation_measure"], "open")
        self.assertIn("context-dependent basin events", certificate["event_level_no_go"]["allowed_structure"])
        self.assertEqual(certificate["rational_example"]["fourier_basis_probabilities"], ["1/6"] * 6)
        self.assertEqual(certificate["legacy_pure_state_claim_counterexample"]["encoded_ray_probability"], "7/12")
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_preparation_to_density_identification"],
            "open",
        )

    def test_generated_certificates_are_valid_json(self) -> None:
        certificate_dir = ROOT / "certificates"
        if not certificate_dir.is_dir():
            self.skipTest("run scripts/verify.py first")
        for path in certificate_dir.glob("*.json"):
            self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)

    def test_finite_geometry_does_not_select_one_preparation(self) -> None:
        certificate = preparation_selection_nogo()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["commutants"]["S3_complex_dimension"], 8)
        self.assertEqual(certificate["commutants"]["S3_JDE_and_normalized_hessian_complex_dimension"], 4)
        self.assertIn("state_data", certificate["interpretation"])

    def test_effect_reduction_is_conditional_and_includes_nonprojective_povm(self) -> None:
        certificate = effect_frame_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["rational_povm_example"]["trace_weights"],
            ["11/24", "7/24", "1/4"],
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_selected_physical_effect_map"],
            "open",
        )

    def test_preparation_moment_functor_reduces_consistency_gates(self) -> None:
        certificate = preparation_moment_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_nonuniqueness_witness"]["plus_effect_probability"],
            "1/2",
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_probability_noncontextuality"],
            "automatic_after_same_effect_factorization",
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_physical_capture_calibration"],
            "open",
        )

    def test_bare_geometry_capture_descent_is_the_remaining_single_gate(self) -> None:
        certificate = capture_descent_reduction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["exact_countermodel"]["A_weights"], ["1/2", "1/2"])
        self.assertEqual(certificate["exact_countermodel"]["B_weights"], ["1/4", "3/4"])
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_second_moment_capture_descent"],
            "open_single_gate",
        )

    def test_generic_quadratic_hazard_exit_remains_unsourced(self) -> None:
        certificate = quadratic_hazard_capture()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_example"]["first_capture_probabilities"],
            ["7/12", "5/12"],
        )
        self.assertEqual(
            certificate["blocker_readiness"]["B.QM.01_selected_clock_source"],
            "open",
        )

    def test_one_axiom_completion_is_minimal_candidate_not_adopted(self) -> None:
        certificate = one_axiom_born_completion()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["adoption_state"], "candidate_only")
        self.assertEqual(certificate["parameter_ledger"]["new_structural_axioms"], 1)
        self.assertEqual(certificate["parameter_ledger"]["new_continuous_parameters"], 0)
        self.assertEqual(certificate["parameter_ledger"]["observed_probabilities_used"], 0)

    def test_q79_selects_one_binary_quadratic_response_context(self) -> None:
        certificate = canonical_pq_hazard_rigidity()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["q79_selected_context"]["exact_rates"], ["1/3", "2/3"])
        self.assertIn("clock", certificate["boundary"]["open"])

    def test_free_fixed_point_damping_is_not_the_capture_clock(self) -> None:
        certificate = fixed_point_clock_nogo()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(certificate["semigroup"]["asymptotic_loss"], "2/3")
        self.assertIn("not", certificate["no_go"]["conclusion"])

    def test_raw_apparatus_channels_normalize_without_a_knob(self) -> None:
        certificate = apparatus_frame_normalization()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_nonprojective_example"]["probabilities"],
            ["5/6", "1/6"],
        )
        self.assertIn("derive R_C,a", certificate["source_boundary"]["open"])

    def test_interaction_derivative_emits_raw_pointer_channels(self) -> None:
        certificate = interaction_channel_extraction()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["exact_example"]["frame_gram"],
            [["2", "0"], ["0", "1"]],
        )
        self.assertIn("does not yet emit", certificate["corpus_audit"]["verdict"])

    def test_selected_damping_has_an_exact_pointer_isometry(self) -> None:
        certificate = canonical_damping_pointer_dilation()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["reduced_dynamics"]["exact_sample_coherence_factor"],
            "3/5",
        )
        self.assertEqual(
            certificate["pointer_isometry"]["asymptotic_effects"],
            ["P_Haar", "Q"],
        )
        self.assertIn(
            "selection of one realized pointer outcome",
            certificate["interpretation_boundary"]["open"],
        )

    def test_q79_dephasing_is_the_binary_penrose_semigroup_conditionally(self) -> None:
        certificate = canonical_pq_penrose_semigroup_bridge()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["rigidity"]["conclusion"],
            "a(t)=exp(-gamma t) for one gamma>=0",
        )
        self.assertEqual(
            certificate["parameter_ledger"]["unsourced_positive_rate_scales"],
            1,
        )
        self.assertIn(
            "compatible",
            certificate["clock_reconciliation"]["verdict"],
        )

    def test_same_q79_channel_has_inequivalent_exact_instruments(self) -> None:
        certificate = canonical_pq_instrument_nonuniqueness()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["pointer_instrument"]["example_probabilities"],
            ["241/625", "384/625"],
        )
        self.assertEqual(
            certificate["random_unitary_instrument"]["example_probabilities"],
            ["16/25", "9/25"],
        )
        self.assertIn("do not determine", certificate["no_go"]["result"])

    def test_one_anchor_clock_lift_fixes_rate_coefficient_without_second_scale(self) -> None:
        certificate = one_anchor_physical_clock_lift()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["derived_rate"]["energy_anchor"],
            "gamma=lambda_phys/E0=log(448)E0",
        )
        self.assertEqual(
            certificate["parameter_ledger"]["additional_clock_scale_parameters"],
            0,
        )
        self.assertIn("open", certificate["penrose_target"]["status"])

    def test_penrose_rate_must_be_context_dependent_over_physical_profiles(self) -> None:
        certificate = penrose_profile_dependence_nogo()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertIn("cannot be a universal", certificate["no_go"]["conclusion"])
        self.assertEqual(certificate["contextual_repair"]["context_rate"], "gamma_C=r_C gamma0=E_C^(G,ell)/hbar")
        self.assertIn("not a fitted", certificate["source_contract"]["not_a_new_universal_parameter"])

    def test_penrose_profile_factor_is_independent_of_absolute_anchor(self) -> None:
        certificate = anchor_free_penrose_profile_factor()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["rate_ratio"]["profile_factor"],
            "r_C=gamma_C/gamma0=g0 J_C/(2 log(448))",
        )
        self.assertEqual(certificate["rate_ratio"]["anchor_status"], "E0 and hbar cancel exactly")

    def test_five_context_outputs_descend_from_one_selected_action_package(self) -> None:
        certificate = selected_context_source_functor()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["status"],
            "SAME_SOURCE_FIVE_OUTPUT_FUNCTOR_EXACT_SELECTED_ACTION_PAYLOAD_OPEN",
        )
        self.assertEqual(
            certificate["exact_finite_witness"]["context_involution"],
            [["1", "0"], ["0", "-1"]],
        )
        self.assertEqual(certificate["exact_finite_witness"]["ell_hat"], "1/2")
        self.assertEqual(
            certificate["exact_finite_witness"]["J_C_over_4pi"],
            "13/25",
        )
        self.assertEqual(
            certificate["exact_finite_witness"]["instrument_probabilities"],
            ["1/3", "2/3"],
        )
        self.assertEqual(
            certificate["parameter_ledger"]["new_universal_continuous_parameters"],
            0,
        )
        self.assertIn(
            "cannot be relabelled",
            certificate["current_mtt_frontier"]["type_guard"],
        )

    def test_q79_minimal_recorder_action_emits_informative_capture_clocks(self) -> None:
        certificate = canonical_q79_minimal_recorder_action()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["status"],
            "Q79_MINIMAL_RECORDER_ACTION_GAUGE_CLASS_EXACT_ADOPTION_AND_RATE_SOURCE_OPEN",
        )
        self.assertEqual(
            certificate["two_state_defect_recorder"]["exact_checkpoint"][
                "kraus_operators"
            ],
            ["P+(7/25)Q", "(24/25)Q"],
        )
        self.assertIn(
            "dimension at least three",
            certificate["three_state_capture_recorder"]["minimality"],
        )
        self.assertEqual(
            certificate["exact_witness"]["three_step_attenuation"],
            "4096/15625",
        )
        self.assertEqual(
            certificate["exact_witness"][
                "eventual_record_probabilities_if_trace_rule_is_available"
            ],
            ["1/3", "2/3"],
        )
        self.assertEqual(
            certificate["parameter_ledger"]["new_universal_dimensionless_parameters"],
            0,
        )
        self.assertEqual(
            certificate["selection_principle"]["adoption_state"],
            "candidate_structural_principle_not_yet_selected_by_upper_MTT",
        )

    def test_q79_hessian_sources_the_defect_meter_but_not_its_context(self) -> None:
        certificate = canonical_q79_hessian_recorder_source()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["status"],
            "Q79_HESSIAN_RESIDUAL_AND_SPECTRAL_RECORDER_SOURCE_EXACT_CONTEXT_AND_ACTUALIZATION_OPEN",
        )
        self.assertEqual(
            certificate["finite_action_source"]["gram_identity"],
            "D_fin^* D_fin=Q=I-P_Haar",
        )
        self.assertEqual(
            certificate["exact_witness"][
                "unequal_rate_hazards_on_kernel_and_support"
            ],
            ["1", "2"],
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_universal_structural_axioms_for_canonical_context"
            ],
            0,
        )
        self.assertIn(
            "cannot decide",
            certificate["nonselection_no_go"]["conclusion"],
        )

    def test_marked_poisson_primitive_actualizes_quadratic_hazards(self) -> None:
        certificate = shared_circle_marked_poisson_actualization()
        self.assertTrue(certificate["all_checks_pass"])
        self.assertEqual(
            certificate["status"],
            "SHARED_CIRCLE_MARKED_POISSON_ACTUALIZATION_EXACT_ONE_PRIMITIVE_NOT_SELECTED",
        )
        self.assertEqual(
            certificate["exact_witness"]["first_capture_probabilities"],
            ["1/6", "1/3", "1/2"],
        )
        self.assertEqual(
            certificate["exact_witness"]["record_masses_by_that_time"],
            ["1/8", "1/4", "3/8"],
        )
        self.assertEqual(
            certificate["exact_witness"]["q79_gamma_15_cause_rates"],
            ["5", "10"],
        )
        self.assertEqual(
            certificate["parameter_ledger"][
                "new_structural_stochastic_primitives_if_adopted"
            ],
            1,
        )
        self.assertIn(
            "not a zero-primitive",
            certificate["comparison_with_A_Born"]["logical_status"],
        )


if __name__ == "__main__":
    unittest.main()
