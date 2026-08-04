from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    tiers = cert["claim_tiers"]
    theorem = cert["theorem"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more teleparallel bridge checks failed")
    require(
        cert["status"]
        == "CLOSURE_POTENTIAL_GR_KINETIC_NOGO_AND_TEGR_ANHOLONOMY_EINSTEIN_BRIDGE_CLOSED_COFAME_LIFT_CONSTITUTIVE_SELECTION_SCALE_LAMBDA_OPEN",
        "teleparallel bridge status changed",
    )
    require(
        theorem["part_C_quadratic_torsion_basis"]["witness_determinant"] == -4,
        "quadratic torsion basis independence was lost",
    )
    require(
        theorem["part_D_TEGR_identity"]["TEGR_coefficients"] == ["1/4", "1/2", "-1"],
        "TEGR coefficient vector changed",
    )
    require(
        theorem["part_E_exact_symbolic_execution"]["residual"] == "0",
        "symbolic teleparallel identity no longer closes",
    )
    require(
        tiers["closure_potential_alone_generates_massless_spin2_kinetic_term"]
        == "CLOSED_NO_GO",
        "algebraic closure-potential no-go was lost",
    )
    require(
        tiers["TEGR_Einstein_Hilbert_boundary_identity"] == "CLOSED_EXACT"
        and tiers["TEGR_bulk_field_equations_equal_Einstein_equations"] == "CLOSED_EXACT",
        "exact TEGR/Einstein equivalence was lost",
    )
    require(
        tiers["direct_two_derivative_action_exit"]
        == "EXACT_TELEPARALLEL_CANDIDATE_CONSTRUCTED_SELECTION_OPEN",
        "direct action exit was lost or overpromoted",
    )
    require(
        tiers["global_Lorentzian_coframe_lift_from_MTT"] == "OPEN"
        and tiers["MTT_selection_of_TEGR_constitutive_vector"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
        "coframe or constitutive selection was overpromoted",
    )
    require(
        tiers["global_Lorentzian_coframe_existence_under_declared_v4_inputs"]
        == "CLOSED_CONDITIONAL"
        and tiers["flat_metric_compatible_teleparallel_connection_existence"]
        == "CLOSED_CONSTRUCTED_FROM_GLOBAL_COFRAME"
        and tiers["same_source_Q_WW_to_global_coframe_identification"]
        == "REDUCED_TO_CAUCHY_SUPPORT_AND_OUTER_TANGENT_IDENTIFICATION_ONLY",
        "conditional global coframe/connection existence boundary changed",
    )
    require(
        tiers["local_QWW_to_ADM_coframe_map"]
        == "CLOSED_EXACT_UNDER_TYPED_BUNDLE_IDENTIFICATION"
        and tiers["ADM_metric_and_volume_from_QWW"] == "CLOSED_EXACT"
        and tiers["lapse_shift_as_fit_parameters"]
        == "CLOSED_NONE_CONSTRAINT_FIELDS",
        "explicit local QWW/ADM coframe construction changed",
    )
    require(
        tiers["QWW_transition_law_matches_spatial_tetrad_cocycle"]
        == "CLOSED_EXACT"
        and tiers["QWW_global_soldering_after_typed_identification"]
        == "CLOSED_CONDITIONAL"
        and tiers["QWW_inner_spatial_bundle_identification_after_invertibility"]
        == "CLOSED_AUTOMATIC",
        "QWW soldering/cocycle theorem changed",
    )
    require(
        tiers["local_orientation_invariance_of_G_equal_QTQ"] == "CLOSED_EXACT"
        and tiers["metric_descent_selects_TEGR_constitutive_vector"]
        == "CLOSED_UNIQUE_CONDITIONAL"
        and tiers["independent_TEGR_constitutive_parameters_after_metric_descent"]
        == "CLOSED_NONE"
        and tiers["MTT_selection_of_metric_descent_and_no_extra_frame_modes"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY"
        and tiers["frame_neutrality_principal_symbol_selects_TEGR_vector"]
        == "CLOSED_EXACT"
        and tiers["TEGR_nonlinear_frame_neutrality_sufficiency_mod_boundary"]
        == "CLOSED_EXACT"
        and tiers["MTT_identifies_teleparallel_representatives_as_neutrality_equivalent"]
        == "OPEN",
        "metric-descent TEGR selection reduction changed",
    )
    require(
        theorem["part_K_exact_frame_neutrality_selector"]["constraint_rank"] == 2
        and theorem["part_K_exact_frame_neutrality_selector"]["integer_null_ray"]
        == [1, 2, -4]
        and theorem["part_K_exact_frame_neutrality_selector"]["TEGR_symbol_residual"]
        == "0",
        "exact frame-neutrality TEGR selector changed",
    )
    require(
        theorem["part_F_selection_reduction"]["parameter_count"][
            "new_fitted_continuous_parameters"
        ]
        == 0,
        "teleparallel bridge introduced a fitted number",
    )
    require(
        guards["claims_MTT_already_selects_TEGR_coefficients"] is False
        and guards["claims_Q_WW_already_is_a_global_four_coframe"] is False
        and guards["claims_numeric_Newton_constant"] is False,
        "teleparallel claim boundary failed",
    )

    print(
        "AUDIT_PASS: closure potential kinetic no-go and exact TEGR/Einstein "
        "anholonomy bridge are closed; pure-frame neutrality selects the exact "
        "TEGR ray, while MTT support/neutrality selection, kappa_h, and Lambda "
        "remain open"
    )


if __name__ == "__main__":
    main()
