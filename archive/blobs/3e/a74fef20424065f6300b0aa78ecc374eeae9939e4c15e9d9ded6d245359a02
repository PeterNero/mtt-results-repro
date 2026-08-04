from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "strict_same_source_teleparallel_selection_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    theorem = cert["theorem"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more strict same-source checks failed")
    require(
        cert["status"]
        == "STRICT_SAME_SOURCE_CANONICAL_PHYSICAL_BRANCH_SELECTS_TEGR_IR_ACTION_EXACT_PRIMITIVE_REALIZATION_KAPPA_LAMBDA_UV_OPEN",
        "strict same-source status changed",
    )
    require(
        theorem["part_A_exact_metric_quotient"]["jacobian_rank"] == 6
        and theorem["part_A_exact_metric_quotient"]["kernel_dimension"] == 3,
        "metric quotient rank/nullity changed",
    )
    require(
        theorem["part_B_selected_candidate_source_support"]["orientation_source_coordinates"]
        == 0,
        "an orientation source coordinate was inserted",
    )
    require(
        theorem["part_D_exact_TEGR_selection"]["constraint_rank"] == 2
        and theorem["part_D_exact_TEGR_selection"]["unique_ray"]
        == "(c1,c2,c3)=lambda(1/4,1/2,-1)",
        "TEGR selection ray changed",
    )
    require(
        tiers["strict_same_source_requires_orientation_fiber_neutrality"]
        == "CLOSED_CHARACTERIZATION"
        and tiers["strict_same_source_two_derivative_teleparallel_action"]
        == "CLOSED_UNIQUE_TEGR_RAY"
        and tiers["strict_same_source_nonlinear_metric_descent"]
        == "CLOSED_EXACT_MOD_BOUNDARY",
        "strict same-source action closure changed",
    )
    require(
        tiers["canonical_pullback_metric_given_QWW"] == "CLOSED_EXACT_UNIQUE"
        and tiers["metric_observable_choice_given_QWW"]
        == "CLOSED_NO_REMAINING_CHOICE"
        and theorem["part_G_canonical_pullback_metric_selection"]["parameter_count"]
        == 0,
        "canonical QWW pullback metric selection changed",
    )
    require(
        tiers["cauchy_support_typing_without_extra_source_map"]
        == "CLOSED_CONDITIONAL_ON_CANONICAL_PHYSICAL_REALIZATION"
        and tiers["inner_spatial_bundle_typing"]
        == "CLOSED_AUTOMATIC_FROM_INVERTIBLE_QWW",
        "support or inner-bundle typing changed",
    )
    require(
        tiers["selected_branch_q79_Z64_QWW_source_realization"]
        == "CLOSED_UNIQUE_UP_TO_GAUGE"
        and tiers["selected_branch_source_realization_fitted_parameters"]
        == "CLOSED_ZERO"
        and tiers["primitive_MTT_selects_candidate_metric_source_realization"]
        == "REDUCED_TO_PRIMITIVE_MINIMAL_ROOTSTACK_LORENTZIAN_BRANCH_SELECTION"
        and tiers["spectral_sheet_symbol_to_rootstack_strain_carrier"]
        == "CLOSED_EXACT"
        and tiers["literal_full_inverse_Fourier_Mukai_HYM_connection_identity"]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        and tiers["actual_q79_inverse_Fourier_Mukai_visible_bundle"]
        == "OPEN_GERBE_AND_LOCAL_FREENESS"
        and tiers["dynamic_projected_HYM_TT_Hessian"]
        == "OPEN_ACTUAL_OPERATOR_CONDITIONAL_SCALAR_FORM_CLOSED"
        and tiers["primitive_MTT_selects_canonical_Lorentzian_realization"]
        == "OPEN_INPUT_IN_CURRENT_CORPUS",
        "primitive selection was overpromoted",
    )
    require(
        tiers["canonical_complement_lane_complex_structure"] == "CLOSED_EXACT"
        and tiers["quarterturn_Hessian_scalarization"] == "CLOSED_EXACT"
        and tiers["physical_HYM_TT_block_scalarization"]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and tiers["shared_Z64_unique_order4_subgroup"] == "CLOSED_EXACT"
        and tiers["shared_Z64_odd_root_C4_restriction"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
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
        and tiers["selected_HYM_action_quarterturn_invariance"] == "OPEN"
        and theorem["part_I_conditional_HYM_Hessian_scalarization"][
            "physical_block"
        ]
        == "H_std=kappa_standard*I2",
        "conditional quarter-turn HYM scalarization changed",
    )
    require(
        tiers["ordinary_dual_and_exterior_square_preserve_HYM"]
        == "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR"
        and tiers["ordinary_dual_or_exterior_square_realizes_JDE"]
        == "CLOSED_NO_GO"
        and tiers["nonzero_c3_chiral_branch_complex_linear_self_duality"]
        == "CLOSED_NO_GO"
        and tiers["nonlocal_same_branch_Fourier_Mukai_kernel_contract"]
        == "OPEN_11_ROWS_2_TOPOLOGICAL_ROWS_AVAILABLE",
        "ordinary HYM functor no-go or nonlocal kernel cutset changed",
    )
    require(
        guards["claims_primitive_MTT_uniquely_selects_current_metric_source"] is False
        and guards["claims_primitive_MTT_derives_Y4_without_physical_realization_input"]
        is False
        and guards["claims_numeric_Newton_constant"] is False
        and guards[
            "claims_full_nonzero_Chern_HYM_connection_equals_flat_rootstack_connection"
        ]
        is False
        and guards["claims_dynamic_projected_HYM_Hessian_computed"] is False,
        "strict same-source guardrail failed",
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
        and guards["claims_selected_HYM_action_quarterturn_invariance"] is False,
        "quarter-turn source or invariance was overpromoted",
    )

    print(
        "AUDIT_PASS: strict same-source factorization removes unsourced frame "
        "modes, closes the q79/Z64-to-QWW map on the selected root-stack TT branch, "
        "and selects the exact TEGR ray; the spectral sheet-symbol bridge and literal "
        "full-connection no-go, root-independent C4 parent and flat-symbol JDE "
        "functor, free-orbit/direct-adjoint no-gos, and conditional scalar form are "
        "closed; marked shared-circle Lens descent is a no-go, while primitive branch selection, nonlocal HYM extension or the actual operator, "
        "kappa_h, Lambda, and UV completion remain"
    )


if __name__ == "__main__":
    main()
