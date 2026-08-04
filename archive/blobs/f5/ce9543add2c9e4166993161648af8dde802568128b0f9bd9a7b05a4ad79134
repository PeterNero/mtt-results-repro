from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_heterotic_string_uv_inheritance_cutset_certificate.json"
NOTE = ROOT / "proof_corpus" / "q79_Heterotic_String_UV_Inheritance_Theorem_and_Worldsheet_Cutset_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = cert["claim_tiers"]
    data = cert["finite_data"]
    guards = cert["guardrails"]
    routes = cert["route_matrix"]

    require(all(cert["checks"].values()), "one or more UV route checks failed")
    require(
        cert["status"]
        == "Q79_HETEROTIC_STRING_PRIMARY_UV_ROUTE_SELECTED_FIXED_GENUS_UV_INHERITANCE_THEOREM_CLOSED_CONDITIONAL_EXACT_Q79_WORLDSHEET_CFT_AND_NONPERTURBATIVE_COMPLETION_OPEN",
        "UV inheritance status changed",
    )
    require(
        data["heterotic_central_charges"]["left_total"] == "0"
        and data["heterotic_central_charges"]["right_total"] == "0",
        "critical heterotic central charge changed",
    )
    require(
        data["torus_fundamental_domain"]["exact_minimum_Im_tau"] == "sqrt(3)/2"
        and data["torus_fundamental_domain"]["minimum_Im_tau_squared"] == "3/4",
        "torus modular fundamental-domain bound changed",
    )
    require(
        data["worldsheet_contract_rows_total"] == 12
        and data["worldsheet_contract_rows_available"] == 5
        and data["worldsheet_contract_rows_partial"] == 2
        and data["q79_torus_twist_sectors"] == 81
        and data["q79_modular_character_seed_orbits"] == 7
        and data["q79_twisted_projective_irrep_dimension"] == 3
        and data["q79_finite_topological_torus_index"] == "1"
        and data["q79_seven_seed_finite_constraint_rank"] == 74,
        "q79 worldsheet readiness count changed",
    )
    require(
        data["q79_local_TLSM_anomaly_matrix"] == [[2, -2], [-2, 2]]
        and data["q79_active_fiber_radius_squared"] == 2
        and data["q79_aggregate_Fermi_bundle_c2"] == 20
        and data["q79_topological_visible_c3_options"] == [6, -6]
        and data["q79_topological_visible_mixed_c2"] == "9 u"
        and data["q79_visible_mixed_c2_Hodge_type"] == [2, 2]
        and data["q79_twisted_spectral_continuous_root_tubes"] == 90
        and data["q79_twisted_spectral_integral_H2_basis_columns"] == 92
        and data["q79_twisted_spectral_floating_period_columns"] == 92
        and data["q79_twisted_spectral_interval_support_closed"] == 16
        and data["q79_twisted_spectral_interval_support_total"] == 71
        and data["q79_twisted_spectral_interval_l1_closed"] == 36
        and data["q79_twisted_spectral_interval_l1_total"] == 123,
        "q79 local TLSM anomaly or chiral target changed",
    )
    require(
        data["q79_K3_GLSM_charge_matrix"]
        == [[1, 1, 1, 3, 0, 1, -3, -4], [0, 0, 0, 0, 1, 1, -1, -1]]
        and data["q79_rank_one_FuYau_delta_square"] == "-4",
        "q79 K3 GLSM or rank-one Fu-Yau source changed",
    )
    require(
        routes["q79_heterotic_string_inheritance"]["selected_as_primary_route"]
        is True
        and routes["q79_heterotic_string_inheritance"][
            "smooth_nonpullback_SU3_c2_9u_c3_plusminus6_topologically_exists"
        ]
        is True
        and routes["q79_heterotic_string_inheritance"][
            "smooth_nonpullback_c2_c3_target_is_Hodge_admissible"
        ]
        is True
        and routes["q79_heterotic_string_inheritance"][
            "twisted_spectral_z_chart_adapter_closed"
        ]
        is True
        and routes["q79_heterotic_string_inheritance"][
            "smooth_nonpullback_candidate_is_holomorphic_HYM"
        ]
        is False
        and routes["q79_heterotic_string_inheritance"][
            "exact_q79_worldsheet_contract_closed"
        ]
        is False,
        "heterotic route selection or worldsheet boundary changed",
    )
    require(
        tiers["fixed_genus_heterotic_UV_inheritance"]
        == "CLOSED_CONDITIONAL_THEOREM"
        and tiers["q79_exact_worldsheet_CFT"]
        == "OPEN_5_OF_12_CONTRACT_ROWS_AVAILABLE_2_PARTIAL"
        and tiers["q79_aggregate_local_TLSM_anomaly"]
        == "CLOSED_EXACT_CONDITIONAL_ON_RANKONE_FUYAU_SOURCE"
        and tiers["q79_separate_odd_SU3_SU9_Picard_line_monads"]
        == "CLOSED_EXACT_NOGO"
        and tiers["q79_standard_TLSM_pullback_three_family_bundle"]
        == "CLOSED_EXACT_NOGO_C3_ZERO"
        and tiers["q79_smooth_nonpullback_SU3_c2_9u_c3_plusminus6"]
        == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE"
        and tiers["q79_nonpullback_c2_9u_c3_plusminus6_Hodge_admissibility"]
        == "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE"
        and tiers[
            "q79_twisted_spectral_topological_transport_and_integral_H2_basis"
        ]
        == "CLOSED_EXACT_90_ROOT_TUBES_2_HANDLES_GLOBAL_RELATION_92_COLUMNS"
        and tiers["q79_twisted_spectral_period_interval_execution"]
        == "PARTIAL_EXACT_16_OF_71_SUPPORT_L1_36_OF_123_Z_ADAPTER_CLOSED"
        and tiers["q79_twisted_spectral_integral_branch"]
        == "OPEN_WEIGHTED_INTERVAL_AND_FROZEN_CARRIER_DECISION"
        and tiers["q79_physical_nonpullback_SU3_SU9_EJ_bundle"].startswith("OPEN")
        and tiers["q79_modular_partition_function"]
        == "OPEN_ANALYTIC_SEVEN_SEEDS_GSO_FINITE_TOPOLOGICAL_MODULE_AND_INDUCTION_LAYERS_CLOSED"
        and tiers["all_genus_convergence"] == "OPEN"
        and tiers["nonperturbative_UV_complete_QG"] == "OPEN",
        "perturbative and nonperturbative tiers were conflated",
    )
    require(
        tiers["old_SPT_Gaussian_route"]
        == "CLOSED_NO_GO_ON_POSITIVE_MASSLESS_SPECTRAL_BRANCH"
        and tiers["finite_internal_projection_UV_route"] == "CLOSED_NO_GO"
        and tiers["local_two_parameter_GR_all_scale_route"]
        == "CLOSED_NO_GO_BY_TWO_LOOP_DIVERGENCE",
        "retired UV shortcuts were reopened",
    )
    require(
        guards["claims_first_order_Hull_Strominger_is_exact_CFT"] is False
        and guards["claims_fixed_genus_finiteness_proves_genus_sum_convergence"]
        is False
        and guards["claims_full_UV_complete_QG_closed"] is False,
        "UV inheritance theorem was overpromoted",
    )
    for phrase in [
        "q79 Heterotic String UV Inheritance Theorem",
        "c_L = 10 + 16 - 26 = 0",
        "Im tau >= sqrt(3)/2",
        "fixed-genus,",
        "Current q79 readiness: 5/12",
        "seven seed character",
        "1,8,8,8,8,24,24",
        "Mat_3(C)",
        "topological torus index one",
        "rank 74 and nullity seven",
        "U(1)^2` incidence GLSM",
        "delta=H-L",
        "9+11+4=24",
        "local anomaly",
        "A = [[ 2,-2]",
        "k1^2=2",
        "rank-12 Fermi monad",
        "odd `c2=9,11`",
        "third Chern class vanishes",
        "`c3=+/-6`",
        "`c2=9(Hhat cup t)`",
        "closed `(2,2)` representative",
        "all 90",
        "92-column integral `H2`",
        "16 of 71",
        "L1 weight 36 of 123",
        "covariant z-chart",
        "exact q79 heterotic worldsheet packet",
        "Fixed-genus UV finiteness does not prove convergence",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: q79 heterotic string inheritance is the primary compatible "
        "UV route; fixed-genus finiteness is a closed conditional theorem, while "
        "the exact 5/12 plus two-partial worldsheet contract and nonperturbative completion remain open"
    )


if __name__ == "__main__":
    main()
