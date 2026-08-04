from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

TIME_BRANCH = Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json"
FUYAU_CHARGE = Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json"
FINITE_GERBE = Q79 / "certificates" / "time_oriented_fixed_gerbe_representative_certificate.json"
GS_CURVATURE = Q79 / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
LOW_ENERGY_QG = ROOT / "certificates" / "q79_interacting_low_energy_qg_eft_closure_certificate.json"
STIELTJES_NOGO = ROOT / "certificates" / "stieltjes_massless_gaussian_no_go_certificate.json"
FREE_QG = ROOT / "certificates" / "q79_free_graviton_quantization_and_uv_cutset_certificate.json"
FINITE_MODULAR = ROOT / "certificates" / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
TWISTED_ALGEBRA = ROOT / "certificates" / "q79_twisted_group_algebra_topological_character_certificate.json"
SEVEN_SEED_INDUCTION = ROOT / "certificates" / "q79_seven_seed_modular_induction_stabilizers_certificate.json"
K3_FUYAU_GLSM = (
    ROOT
    / "certificates"
    / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
)
LOCAL_TLSM_ANOMALY = (
    ROOT
    / "certificates"
    / "q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo_certificate.json"
)
SIMULTANEOUS_C2_C3 = (
    ROOT
    / "certificates"
    / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
)
HODGE_ADMISSIBILITY = (
    ROOT
    / "certificates"
    / "q79_fuyau_mixed_c2_hodge_admissibility_certificate.json"
)
PULLBACK_CHIRALITY_NOGO = (
    ROOT
    / "certificates"
    / "q79_standard_tlsm_pullback_chirality_nogo_certificate.json"
)
QG_LEDGER = TEXPAPERS / "12 Quantum Gravity" / "MTT_QUANTUM_GRAVITY_STATUS_LEDGER_2026-07-15.json"

STRING_PAPER = (
    TEXPAPERS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "_work"
    / "Modal_Triplet_Theory__From_MTT_to_String_Theory"
    / "main.tex"
)
FLUX_PAPER = (
    TEXPAPERS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "_work"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3"
    / "main.tex"
)

OUT_CERT = ROOT / "certificates" / "q79_heterotic_string_uv_inheritance_cutset_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Heterotic_String_UV_Inheritance_Theorem_and_Worldsheet_Cutset_v1.md"


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    time_branch = load(TIME_BRANCH)
    fuyau_charge = load(FUYAU_CHARGE)
    finite_gerbe = load(FINITE_GERBE)
    gs_curvature = load(GS_CURVATURE)
    low_energy_qg = load(LOW_ENERGY_QG)
    stieltjes_nogo = load(STIELTJES_NOGO)
    free_qg = load(FREE_QG)
    finite_modular = load(FINITE_MODULAR)
    twisted_algebra = load(TWISTED_ALGEBRA)
    seven_seed_induction = load(SEVEN_SEED_INDUCTION)
    k3_fuyau_glsm = load(K3_FUYAU_GLSM)
    local_tlsm_anomaly = load(LOCAL_TLSM_ANOMALY)
    simultaneous_c2_c3 = load(SIMULTANEOUS_C2_C3)
    hodge_admissibility = load(HODGE_ADMISSIBILITY)
    pullback_chirality_nogo = load(PULLBACK_CHIRALITY_NOGO)
    qg_ledger = load(QG_LEDGER)
    string_text = STRING_PAPER.read_text(encoding="utf-8", errors="replace")
    flux_text = FLUX_PAPER.read_text(encoding="utf-8", errors="replace")

    # Critical heterotic central-charge cancellation is an exact universal row.
    central_charge = {
        "left_moving_matter": Fraction(10) + Fraction(16),
        "left_moving_ghost": Fraction(-26),
        "right_moving_matter": Fraction(10) + Fraction(10, 2),
        "right_moving_ghost": Fraction(-15),
    }
    central_charge["left_total"] = (
        central_charge["left_moving_matter"] + central_charge["left_moving_ghost"]
    )
    central_charge["right_total"] = (
        central_charge["right_moving_matter"] + central_charge["right_moving_ghost"]
    )

    # The standard SL(2,Z) torus fundamental domain obeys |Re tau|<=1/2 and
    # |tau|>=1. Therefore Im tau>=sqrt(3)/2: the tau_2->0 field-theory UV
    # region is absent once a partition function is genuinely modular invariant.
    tau2_min = sp.sqrt(3) / 2
    tau2_min_squared = sp.simplify(tau2_min**2)

    checks = {
        "time_oriented_q79_F_branch_is_selected": time_branch["status"]
        == "TIME_ORIENTED_Q79_F_BRANCH_SELECTED_ORDERED_SU5_PACKET_OPEN",
        "q79_conjugate_partner_is_retained": time_branch["calculation_results"]
        ["q369_retained_as_global_antiunitary_conjugate"],
        "FuYau_charge_sector_GS_Bianchi_is_closed": fuyau_charge["geometry"]
        ["green_schwarz_bianchi_identity_verified"],
        "visible_curvature_level_GS_row_is_closed": gs_curvature["calculation_results"]
        ["visible_green_schwarz_curvature_verified"],
        "visible_GS_operator_source_is_honestly_open": not gs_curvature["calculation_results"]
        ["selected_visible_operator_source_verified"],
        "finite_gerbe_is_not_full_differential_cohomology": not finite_gerbe["guardrails"]
        ["claims_full_differential_cohomology_representative"],
        "critical_left_central_charge_cancels": central_charge["left_total"] == 0,
        "critical_right_central_charge_cancels": central_charge["right_total"] == 0,
        "torus_fundamental_domain_tau2_bound_is_exact": tau2_min_squared
        == sp.Rational(3, 4),
        "current_string_paper_only_proves_controlled_alpha_order": (
            "to order $\\alphap^{n}$" in string_text
            and "matches 10D supergravity+$\\alphap$ corrections" in string_text
        ),
        "current_string_modular_claim_is_only_CY_toroidal": (
            "In the CY/toroidal corner" in string_text
            and "one-loop partition function is modular-invariant" in string_text
        ),
        "flux_paper_is_first_order_alpha_prime": (
            "We work in heterotic supergravity to first order in $\\alpha'$" in flux_text
            and "Our solutions solve the Hull--Strominger system at $\\mathcal{O}(\\alpha')$"
            in flux_text
            and "At $\\mathcal{O}(\\alpha'^2)$" in flux_text
        ),
        "positive_massless_Gaussian_shortcut_is_excluded": stieltjes_nogo["claim_tiers"]
        ["three_way_incompatibility"]
        == "CLOSED",
        "finite_internal_UV_shortcut_is_excluded": free_qg["claim_tiers"]
        ["finite_internal_trace_changes_4D_UV_power_counting"]
        == "CLOSED_NO_GO",
        "two_loop_local_GR_boundary_is_closed": low_energy_qg["claim_tiers"]
        ["two_loop_pure_GR_divergence"]
        == "CLOSED_NONZERO_GOROFF_SAGNOTTI_STANDARD_RESULT",
        "q79_finite_torsion_phase_is_modular_covariant": finite_modular["claim_tiers"]
        ["finite_discrete_torsion_S_T_phase_covariance"]
        == "CLOSED_EXACT_81_OF_81",
        "q79_character_slots_reduce_to_seven_modular_orbits": finite_modular
        ["finite_data"]["modular_orbit_count"]
        == 7,
        "q79_selected_twisted_algebra_is_Mat3_with_index_one": (
            twisted_algebra["claim_tiers"]["selected_q79_twisted_group_algebra"]
            == "CLOSED_EXACT_ISOMORPHIC_TO_MAT3C"
            and twisted_algebra["finite_data"][
                "normalized_finite_topological_torus_index"
            ]
            == "1"
        ),
        "q79_seven_seed_stabilizer_induction_is_exact": (
            seven_seed_induction["claim_tiers"][
                "seven_modular_orbits_and_stabilizers"
            ]
            == "CLOSED_EXACT"
            and seven_seed_induction["finite_data"][
                "finite_invariance_constraint_rank"
            ]
            == 74
        ),
        "q79_degree_two_K3_incidence_GLSM_and_rank_one_source_are_exact": (
            k3_fuyau_glsm["claim_tiers"]["explicit_degree_two_K3_smoothness"]
            == "CLOSED_EXACT"
            and k3_fuyau_glsm["claim_tiers"]["splitting_conic_incidence_GLSM"]
            == "CLOSED_EXACT"
            and k3_fuyau_glsm["claim_tiers"][
                "rank_one_FuYau_divisor_source_delta_H_minus_L"
            ]
            == "CLOSED_EXACT"
            and k3_fuyau_glsm["claim_tiers"]["exact_q79_IR_SCFT"] == "OPEN"
        ),
        "q79_local_TLSM_anomaly_matrix_and_integral_torsion_rows_are_exact": (
            local_tlsm_anomaly["claim_tiers"][
                "aggregate_local_TLSM_anomaly_matrix"
            ]
            == "CLOSED_EXACT_CONDITIONAL_ON_RANKONE_FUYAU_SOURCE"
            and local_tlsm_anomaly["local_TLSM_anomaly"][
                "quantum_anomaly_matrix"
            ]
            == [[2, -2], [-2, 2]]
            and local_tlsm_anomaly["local_TLSM_anomaly"][
                "classical_Green_Schwarz_matrix_half_NM"
            ]
            == [[2, -2], [-2, 2]]
            and local_tlsm_anomaly["local_TLSM_anomaly"][
                "active_fiber_radius_squared"
            ]
            == 2
        ),
        "q79_aggregate_rank12_Fermi_monad_exists_but_physical_odd_split_is_open": (
            local_tlsm_anomaly["claim_tiers"][
                "aggregate_rank12_Fermi_monad_existence"
            ]
            == "CLOSED_EXACT_ANOMALY_EQUIVALENCE_TIER"
            and local_tlsm_anomaly["claim_tiers"][
                "separate_odd_SU3_SU9_Picard_line_monads"
            ]
            == "CLOSED_EXACT_NOGO"
            and local_tlsm_anomaly["claim_tiers"][
                "physical_SU3_SU9_nonAbelian_EJ_maps"
            ]
            == "OPEN"
        ),
        "standard_TLSM_pullback_c3_zero_nogo_is_exact": (
            pullback_chirality_nogo["claim_tiers"][
                "standard_TLSM_pullback_c3_zero"
            ]
            == "CLOSED_EXACT_NOGO"
            and pullback_chirality_nogo["claim_tiers"][
                "topological_nonpullback_SU3_c3_plusminus6"
            ]
            == "CLOSED_EXACT"
            and pullback_chirality_nogo["claim_tiers"][
                "holomorphic_nonpullback_SU3_worldsheet_bundle"
            ]
            == "OPEN"
            and pullback_chirality_nogo["checks"][
                "A128_all_90_continuous_root_tubes_closed"
            ]
            and pullback_chirality_nogo["checks"][
                "A130_exact_integral_H2_basis_closed"
            ]
            and pullback_chirality_nogo["checks"][
                "A151_exact_interval_support_is_16_of_71_z_adapter_closed_branch_open"
            ]
        ),
        "shared_circle_simultaneous_c2_9u_c3_plusminus6_is_topologically_exact": (
            simultaneous_c2_c3["claim_tiers"][
                "smooth_SU3_candidate_with_c2_9u_and_c3_plusminus6"
            ]
            == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE"
            and simultaneous_c2_c3["claim_tiers"][
                "holomorphic_nonpullback_SU3_bundle"
            ]
            == "OPEN"
        ),
        "mixed_c2_9u_and_c3_plusminus6_pass_selected_FuYau_Hodge_test": (
            hodge_admissibility["claim_tiers"][
                "mixed_c2_9u_Hodge_admissibility"
            ].startswith("CLOSED_EXACT")
            and hodge_admissibility["claim_tiers"][
                "holomorphic_nonpullback_SU3_bundle"
            ]
            == "OPEN"
        ),
        "asymptotic_safety_fixed_functional_is_not_available": qg_ledger["research_gates"]
        ["exact_asymptotic_safety_fixed_functional"]
        == "OPEN",
        "full_spectral_action_remainder_is_not_available": qg_ledger["research_gates"]
        ["spectral_full_heat_kernel_remainder_bound"]
        == "OPEN",
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    route_matrix = {
        "four_dimensional_local_Einstein_EFT": {
            "compatible_with_massless_positive_graviton": True,
            "all_scale_UV_completion_closed": False,
            "decisive_boundary": "nonzero two-loop Riemann-cubed counterterm",
        },
        "finite_internal_projection_as_regulator": {
            "compatible_with_low_energy_q79": True,
            "all_scale_UV_completion_closed": False,
            "decisive_boundary": "finite internal trace does not change 4D momentum power counting",
        },
        "permanent_SPT_Gaussian_physical_propagator": {
            "massless_positive_spectral_unitarity_proof_survives": False,
            "all_scale_UV_completion_closed": False,
            "decisive_boundary": "positive massless Stieltjes pole and permanent Gaussian damping are incompatible",
        },
        "asymptotic_safety": {
            "exact_selected_dimensionless_fixed_functional_available": False,
            "all_scale_UV_completion_closed": False,
            "status": "conditional external/corpus research route",
        },
        "finite_product_spectral_action": {
            "same_operator_SM_gravity_architecture": True,
            "full_remainder_and_quantum_measure_available": False,
            "all_scale_UV_completion_closed": False,
        },
        "q79_heterotic_string_inheritance": {
            "compatible_with_massless_positive_graviton": True,
            "q79_FuYau_GS_source_rows_available": True,
            "avoids_permanent_physical_Gaussian_damping": True,
            "fixed_genus_UV_finiteness_inheritance_available_if_worldsheet_contract_closes": True,
            "finite_torsion_phase_and_modular_orbit_reduction_closed": True,
            "remaining_torus_character_seed_count": 7,
            "finite_twisted_algebra": "Mat3(C)",
            "finite_topological_torus_index": 1,
            "seven_seed_stabilizer_induction_closed": True,
            "explicit_degree_two_K3_incidence_GLSM_closed": True,
            "rank_one_FuYau_torsion_divisor_source_closed": True,
            "aggregate_local_TLSM_anomaly_matrix_closed": True,
            "aggregate_rank12_Fermi_monad_exists": True,
            "physical_odd_SU3_SU9_nonAbelian_EJ_split_closed": False,
            "standard_pullback_TLSM_can_emit_three_family_c3": False,
            "smooth_nonpullback_SU3_c2_9u_c3_plusminus6_topologically_exists": True,
            "smooth_nonpullback_c2_c3_target_is_Hodge_admissible": True,
            "smooth_nonpullback_candidate_is_holomorphic_HYM": False,
            "twisted_spectral_root_tubes_closed": 90,
            "twisted_spectral_integral_H2_columns_closed": 92,
            "twisted_spectral_weighted_E32_support_closed": 16,
            "twisted_spectral_weighted_E32_support_total": 71,
            "twisted_spectral_z_chart_adapter_closed": True,
            "twisted_spectral_integral_branch_selected": False,
            "exact_q79_worldsheet_contract_closed": False,
            "all_genus_or_nonperturbative_completion_closed": False,
            "selected_as_primary_route": True,
        },
    }

    worldsheet_rows = [
        {
            "row": "W1_time_oriented_q79_target_branch",
            "status": "AVAILABLE",
            "source": str(TIME_BRANCH),
        },
        {
            "row": "W2_FuYau_Mukai_charge_and_GS_Bianchi_sector",
            "status": "AVAILABLE",
            "source": str(FUYAU_CHARGE),
        },
        {
            "row": "W3_visible_curvature_level_GS_cancellation",
            "status": "AVAILABLE_CURVATURE_TIER",
            "source": str(GS_CURVATURE),
        },
        {
            "row": "W4_critical_heterotic_central_charge",
            "status": "AVAILABLE_UNIVERSAL",
            "source": "cL=10+16-26=0; cR=10+10/2-15=0",
        },
        {
            "row": "W5_q79_low_energy_GR_and_quantum_EFT_limit",
            "status": "AVAILABLE_AT_DECLARED_PARITY_TIER",
            "source": str(LOW_ENERGY_QG),
        },
        {
            "row": "W6_global_Deligne_gerbe_and_Freed_Witten_on_full_visible_cycle_set",
            "status": "OPEN_FINITE_REPRESENTATIVE_ONLY",
            "source": str(FINITE_GERBE),
        },
        {
            "row": "W7_all_order_alpha_prime_q79_target_background",
            "status": "OPEN_CURRENT_BACKGROUND_FIRST_ORDER_ONLY",
            "source": str(FLUX_PAPER),
        },
        {
            "row": "W8_exact_q79_heterotic_0_2_SCFT_or_all_beta_functions",
            "status": "PARTIAL_EXACT_K3_GLSM_LOCAL_TLSM_ANOMALY_SMOOTH_C2_9U_C3_PLUSMINUS6_HODGE_ADMISSIBLE_CANDIDATE_90_ROOT_TUBES_92_H2_COLUMNS_Z_ADAPTER_AND_16_OF_71_E32_INTERVALS_CLOSED_HOLOMORPHIC_NONPULLBACK_BUNDLE_BRANCH_GSO_AND_IR_SCFT_OPEN",
            "source": [
                str(K3_FUYAU_GLSM),
                str(LOCAL_TLSM_ANOMALY),
                str(SIMULTANEOUS_C2_C3),
                str(HODGE_ADMISSIBILITY),
                str(PULLBACK_CHIRALITY_NOGO),
                str(STRING_PAPER),
            ],
        },
        {
            "row": "W9_q79_modular_invariant_GSO_partition_function_and_factorization",
            "status": "PARTIAL_FINITE_TORSION_PHASE_MAT3_MODULE_INDEX1_AND_7_SEED_STABILIZER_INDUCTION_CLOSED_ANALYTIC_CHARACTERS_GSO_OPEN",
            "source": [
                str(FINITE_MODULAR),
                str(TWISTED_ALGEBRA),
                str(SEVEN_SEED_INDUCTION),
            ],
        },
        {
            "row": "W10_q79_specific_string_field_vertices_and_BV_master_action",
            "status": "OPEN_STANDARD_HETEROTIC_BV_FRAMEWORK_EXTERNALLY_AVAILABLE",
            "source": "https://arxiv.org/abs/1508.05387",
        },
        {
            "row": "W11_tadpole_vacuum_shift_IR_and_soft_state_completion",
            "status": "OPEN",
            "source": "https://arxiv.org/abs/1512.00026",
        },
        {
            "row": "W12_all_genus_convergence_or_nonperturbative_definition",
            "status": "OPEN",
            "source": "not implied by fixed-genus UV finiteness",
        },
    ]
    available_rows = [
        row for row in worldsheet_rows if row["status"].startswith("AVAILABLE")
    ]
    partial_rows = [
        row for row in worldsheet_rows if row["status"].startswith("PARTIAL")
    ]

    theorem = {
        "name": "q79HeteroticStringFixedGenusUVInheritanceTheorem",
        "hypotheses": [
            "W1-W10 are supplied on one same-source q79/F heterotic worldsheet background",
            "the worldsheet theory is an exact anomaly-free modular (0,2) SCFT with a tachyon-free GSO projection",
            "BRST cohomology and string vertices obey the heterotic quantum BV master equation",
            "degeneration regions are treated by the standard factorization, tadpole-shift and infrared prescription",
        ],
        "conclusion": (
            "At every fixed genus and fixed external multiplicity, q79 heterotic amplitudes have no local ultraviolet divergences. "
            "The torus short-proper-time region is absent because the SL(2,Z) fundamental domain has Im(tau)>=sqrt(3)/2; "
            "higher-genus boundaries are degeneration/factorization regions and carry infrared rather than point-particle ultraviolet singularities."
        ),
        "does_not_conclude": [
            "convergence or Borel summability of the sum over all genera",
            "a nonperturbative definition at finite or strong string coupling",
            "absence of infrared divergences, tadpoles or vacuum shifts",
            "that the present first-order q79 Hull-Strominger packet is already an exact worldsheet CFT",
        ],
    }

    cert = {
        "certificate": "q79_heterotic_string_uv_inheritance_cutset",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": (
            "Q79_HETEROTIC_STRING_PRIMARY_UV_ROUTE_SELECTED_FIXED_GENUS_UV_INHERITANCE_THEOREM_CLOSED_CONDITIONAL_"
            "EXACT_Q79_WORLDSHEET_CFT_AND_NONPERTURBATIVE_COMPLETION_OPEN"
        ),
        "inputs": {
            "time_oriented_q79_branch": str(TIME_BRANCH),
            "FuYau_charge_sector": str(FUYAU_CHARGE),
            "finite_gerbe_representative": str(FINITE_GERBE),
            "visible_GS_curvature": str(GS_CURVATURE),
            "low_energy_q79_QG": str(LOW_ENERGY_QG),
            "positive_spectrum_Gaussian_no_go": str(STIELTJES_NOGO),
            "finite_internal_UV_no_go": str(FREE_QG),
            "q79_finite_torsion_modular_orbits": str(FINITE_MODULAR),
            "q79_twisted_group_algebra": str(TWISTED_ALGEBRA),
            "q79_seven_seed_modular_induction": str(SEVEN_SEED_INDUCTION),
            "q79_degree_two_K3_FuYau_GLSM_base": str(K3_FUYAU_GLSM),
            "q79_local_TLSM_anomaly_and_odd_bundle_no_go": str(
                LOCAL_TLSM_ANOMALY
            ),
            "q79_shared_circle_simultaneous_c2_c3": str(SIMULTANEOUS_C2_C3),
            "q79_FuYau_mixed_c2_Hodge_admissibility": str(HODGE_ADMISSIBILITY),
            "q79_standard_TLSM_pullback_chirality_no_go": str(
                PULLBACK_CHIRALITY_NOGO
            ),
            "MTT_string_paper": str(STRING_PAPER),
            "MTT_flux_paper": str(FLUX_PAPER),
        },
        "checks": checks,
        "finite_data": {
            "heterotic_central_charges": {
                key: str(value) for key, value in central_charge.items()
            },
            "torus_fundamental_domain": {
                "definition": "|Re tau|<=1/2 and |tau|>=1",
                "exact_minimum_Im_tau": "sqrt(3)/2",
                "minimum_Im_tau_squared": str(tau2_min_squared),
                "numeric_minimum_Im_tau": float(tau2_min.evalf(16)),
            },
            "q79_time_oriented_label": 79,
            "q79_conjugate_label": 369,
            "q79_plus_conjugate_mod_448": (79 + 369) % 448,
            "worldsheet_contract_rows_total": len(worldsheet_rows),
            "worldsheet_contract_rows_available": len(available_rows),
            "worldsheet_contract_rows_partial": len(partial_rows),
            "q79_torus_twist_sectors": finite_modular["finite_data"]
            ["torus_twist_sector_count"],
            "q79_modular_character_seed_orbits": finite_modular["finite_data"]
            ["modular_orbit_count"],
            "q79_twisted_projective_irrep_dimension": twisted_algebra[
                "finite_data"
            ]["unique_projective_irrep_dimension"],
            "q79_finite_topological_torus_index": twisted_algebra["finite_data"]
            ["normalized_finite_topological_torus_index"],
            "q79_seven_seed_finite_constraint_rank": seven_seed_induction[
                "finite_data"
            ]["finite_invariance_constraint_rank"],
            "q79_K3_GLSM_charge_matrix": k3_fuyau_glsm["incidence_GLSM"][
                "charge_matrix"
            ],
            "q79_rank_one_FuYau_delta_square": k3_fuyau_glsm[
                "intersection_and_torsion_source"
            ]["delta_square"],
            "q79_local_TLSM_anomaly_matrix": local_tlsm_anomaly[
                "local_TLSM_anomaly"
            ]["quantum_anomaly_matrix"],
            "q79_active_fiber_radius_squared": local_tlsm_anomaly[
                "local_TLSM_anomaly"
            ]["active_fiber_radius_squared"],
            "q79_aggregate_Fermi_bundle_c2": local_tlsm_anomaly[
                "aggregate_rank12_bundle_monad"
            ]["integral_c2"],
            "q79_topological_visible_c3_options": pullback_chirality_nogo[
                "physical_chiral_target"
            ]["integral_c3"],
            "q79_topological_visible_mixed_c2": simultaneous_c2_c3[
                "q79_candidate_specialization"
            ]["simultaneous_reference_member"]["c2"],
            "q79_visible_mixed_c2_Hodge_type": [2, 2],
            "q79_twisted_spectral_continuous_root_tubes": 90,
            "q79_twisted_spectral_integral_H2_basis_columns": 92,
            "q79_twisted_spectral_floating_period_columns": 92,
            "q79_twisted_spectral_interval_support_closed": 16,
            "q79_twisted_spectral_interval_support_total": 71,
            "q79_twisted_spectral_interval_l1_closed": 36,
            "q79_twisted_spectral_interval_l1_total": 123,
        },
        "route_matrix": route_matrix,
        "worldsheet_contract": worldsheet_rows,
        "theorem": theorem,
        "claim_tiers": {
            "old_SPT_Gaussian_route": "CLOSED_NO_GO_ON_POSITIVE_MASSLESS_SPECTRAL_BRANCH",
            "finite_internal_projection_UV_route": "CLOSED_NO_GO",
            "local_two_parameter_GR_all_scale_route": "CLOSED_NO_GO_BY_TWO_LOOP_DIVERGENCE",
            "asymptotic_safety_route": "OPEN_CONDITIONAL_EXACT_FIXED_FUNCTIONAL_ABSENT",
            "finite_spectral_action_UV_route": "OPEN_FULL_REMAINDER_MEASURE_AND_CONTINUUM_LIMIT",
            "q79_heterotic_string_route_selection": "CLOSED_PRIMARY_COMPATIBLE_ROUTE",
            "fixed_genus_heterotic_UV_inheritance": "CLOSED_CONDITIONAL_THEOREM",
            "q79_exact_worldsheet_CFT": "OPEN_5_OF_12_CONTRACT_ROWS_AVAILABLE_2_PARTIAL",
            "q79_aggregate_local_TLSM_anomaly": "CLOSED_EXACT_CONDITIONAL_ON_RANKONE_FUYAU_SOURCE",
            "q79_aggregate_rank12_Fermi_monad": "CLOSED_EXACT_ANOMALY_EQUIVALENCE_TIER",
            "q79_separate_odd_SU3_SU9_Picard_line_monads": "CLOSED_EXACT_NOGO",
            "q79_standard_TLSM_pullback_three_family_bundle": "CLOSED_EXACT_NOGO_C3_ZERO",
            "q79_smooth_nonpullback_SU3_c2_9u_c3_plusminus6": "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE",
            "q79_nonpullback_c2_9u_c3_plusminus6_Hodge_admissibility": "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE",
            "q79_twisted_spectral_topological_transport_and_integral_H2_basis": "CLOSED_EXACT_90_ROOT_TUBES_2_HANDLES_GLOBAL_RELATION_92_COLUMNS",
            "q79_twisted_spectral_period_interval_execution": "PARTIAL_EXACT_16_OF_71_SUPPORT_L1_36_OF_123_Z_ADAPTER_CLOSED",
            "q79_twisted_spectral_integral_branch": "OPEN_WEIGHTED_INTERVAL_AND_FROZEN_CARRIER_DECISION",
            "q79_physical_nonpullback_SU3_SU9_EJ_bundle": "OPEN_TWISTED_SPECTRAL_OR_NONABELIAN_CURRENT_ALGEBRA_SOURCE",
            "q79_modular_partition_function": "OPEN_ANALYTIC_SEVEN_SEEDS_GSO_FINITE_TOPOLOGICAL_MODULE_AND_INDUCTION_LAYERS_CLOSED",
            "q79_string_field_BV_realization": "OPEN_STANDARD_FRAMEWORK_AVAILABLE",
            "all_genus_convergence": "OPEN",
            "nonperturbative_UV_complete_QG": "OPEN",
        },
        "guardrails": {
            "claims_first_order_Hull_Strominger_is_exact_CFT": False,
            "claims_curvature_Bianchi_row_is_full_worldsheet_anomaly_cancellation": False,
            "claims_torus_modular_bound_proves_q79_modular_invariance": False,
            "claims_fixed_genus_finiteness_proves_genus_sum_convergence": False,
            "claims_standard_string_BV_action_is_already_instantiated_on_q79": False,
            "claims_exact_K3_base_GLSM_is_full_heterotic_TLSM": False,
            "claims_integrated_9_11_4_Bianchi_is_local_TLSM_anomaly_matrix": False,
            "claims_aggregate_rank12_monad_is_physical_V3_plus_W9": False,
            "claims_local_ch2_anomaly_determines_visible_c3": False,
            "claims_topological_c3_clutching_is_holomorphic_HYM": False,
            "claims_string_UV_finiteness_removes_IR_tadpoles_or_soft_divergences": False,
            "claims_full_UV_complete_QG_closed": False,
            "uses_observed_quantum_gravity_data": False,
            "adds_fitted_continuous_parameter": False,
        },
        "primary_sources": {
            "superstring_perturbation_supermoduli": "https://arxiv.org/abs/1209.5461",
            "superstring_UV_vs_IR": "https://arxiv.org/abs/1512.00026",
            "heterotic_quantum_BV_master_action": "https://arxiv.org/abs/1508.05387",
            "heterotic_FuYau_torsion_linear_models": "https://arxiv.org/abs/hep-th/0611084",
            "FuYau_anomaly_solutions": "https://arxiv.org/abs/hep-th/0604137",
        },
        "next_required_artifact": "q79_Exact_Heterotic_0_2_Worldsheet_CFT_Modular_BV_Packet_v1",
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Heterotic String UV Inheritance Theorem and Worldsheet Cutset v1

Date: 2026-07-16

## Result

The surviving primary MTT route to perturbative ultraviolet completion is not
permanent Gaussian damping of a four-dimensional graviton. It is inheritance
from an exact heterotic string background on the selected q79/F Fu-Yau branch.

The alternatives are now separated exactly:

- local Einstein gravity has the nonzero two-loop `Riemann^3` divergence;
- finite internal projection does not change four-dimensional loop momentum
  power counting;
- a positive massless Stieltjes propagator cannot have permanent Gaussian
  decay;
- asymptotic safety lacks an exact selected fixed functional in the corpus;
- the finite product spectral action lacks its full remainder, measure, and
  continuum theorem.

The q79 string route is compatible with every one of those boundaries and has
real same-branch support: the time-oriented `q=79/F` representative, Fu-Yau
Mukai charge sector, Green-Schwarz Bianchi data, and the curvature-level visible
Green-Schwarz row are computed.

## Exact universal checks

The critical heterotic central charges cancel:

```text
c_L = 10 + 16 - 26 = {central_charge['left_total']},
c_R = 10 + 10/2 - 15 = {central_charge['right_total']}.
```

For the standard torus modular fundamental domain,

```text
|Re tau| <= 1/2,
|tau| >= 1,
Im tau >= sqrt(3)/2 = {float(tau2_min.evalf(16)):.15f}.
```

Thus the `tau_2 -> 0` point-particle UV region is absent once the actual
partition function is modular invariant. The remaining `tau_2 -> infinity`
boundary is a degeneration/factorization or infrared region, not a local UV
counterterm region.

## Conditional inheritance theorem

Assume one same-source q79/F background supplies an exact anomaly-free modular
heterotic `(0,2)` SCFT, a tachyon-free GSO projection, factorization, and the
heterotic quantum BV master action, with tadpoles and infrared degenerations
treated by the standard vacuum-shift prescription. Then every fixed-genus,
fixed-multiplicity q79 heterotic amplitude is free of local ultraviolet
divergences.

This is the correct replacement for the invalid SPT all-loop theorem. It does
not damp the physical massless graviton propagator. Ultraviolet softness comes
from integration over worldsheet moduli modulo modular equivalence.

## Current q79 readiness: {len(available_rows)}/{len(worldsheet_rows)} available, {len(partial_rows)} partial

Available rows:

1. time-oriented q79/F target branch;
2. Fu-Yau/Mukai charge and Green-Schwarz Bianchi sector;
3. visible curvature-level Green-Schwarz cancellation;
4. universal critical heterotic central-charge cancellation;
5. q79 low-energy GR and quantum-EFT limit.

W8 is now partially constructed by an explicit smooth degree-two K3 in the
splitting-conic family. Its isomorphic `U(1)^2` incidence GLSM has exact
Calabi-Yau charge sums, paired `(2,2)` gauge-anomaly cancellation and the
`E/J` identity. Its divisor ring exposes the primitive Fu-Yau source
`delta=H-L`, with `H.delta=0` and `delta^2=-4`, while the second marked shared
circle remains untwisted. This retains the exact K3-reference allocation
`9+11+4=24`.

The local worldsheet Green-Schwarz row is now exact as well. In the `(H,L)`
basis the one-loop anomaly is

```text
A = [[ 2,-2],
     [-2, 2]] = 2 delta delta^T.
```

It is cancelled over the integers by `M1=(1,-1)`, `N1=(4,-4)` and
`k1^2=2`; the shared second circle has `M2=N2=0`. An anomaly-equivalent
rank-12 Fermi monad with `c1=0,c2=20` exists. It is not the physical
`SU(3) x SU(9)` split: the even Picard lattice proves that line-bundle
complexes cannot separately emit odd `c2=9,11`.

There is a second exact obstruction. A standard compact TLSM Fermi bundle is
pulled back from K3, so its third Chern class vanishes. It cannot realize the
already-constructed topological non-pullback visible bundle with `c3=+/-6`.
The new shared-circle clutching calculation strengthens the positive side:
`H.delta=0` supplies a primitive Gysin lift `Hhat`, and independent degree-three
and degree-five clutching channels give a smooth `SU(3)` candidate with
`c2=9(Hhat cup t)` and `c3=+/-6`. The instanton and chirality targets are
therefore simultaneously admissible topologically. The mixed class has the
closed `(2,2)` representative `(i/2) Theta wedge conjugate(Theta) wedge H`,
so the target also passes the selected Fu-Yau Hodge-type test; holomorphic
bundle existence, HYM, and
the differential total-space Bianchi equation remain open.
The remaining physical bundle must therefore come from the same-carrier
twisted spectral/Fourier-Mukai route or a genuinely non-Abelian fibered
current algebra. The first route is no longer at its old A127 cutset: all 90
continuous root tubes, both handles, the global surface relation, and the exact
92-column integral `H2` presentation are closed. The floating `8 x 92` period
table and effective `Z^90` quotient are closed, and A151 has certified 16 of 71
weighted `E32` intervals with L1 weight 36 of 123. The covariant z-chart
adapter and its first native row are closed. The remaining 55 intervals,
weighted branch decision, inverse-gerbe sheaf, holomorphic/HYM structure,
differential Bianchi representative, global GSO currents, and exact IR `(0,2)`
SCFT remain open.

The modular row W9 is also partially constructed. The selected `F_3^2` gerbe
cocycle gives an exact discrete-torsion phase on all 81 torus twist sectors,
and the modular `S,T` action reduces those sectors to seven seed character
blocks with orbit sizes `1,8,8,8,8,24,24`. Its selected twisted group algebra
is exactly `Mat_3(C)`, with one three-dimensional projective module and finite
topological torus index one. The seven seed stabilizers and modular induction
are exact; finite covariance has rank 74 and nullity seven, so it cannot reduce
the analytic seed count further. The full oscillator, gauge-current,
spin-structure, `Gamma(3)` multiplier, GSO, and factorization characters are
not yet supplied.

The decisive missing object is not another four-dimensional Hessian. It is an
exact q79 heterotic worldsheet packet containing:

1. the global Deligne gerbe and Freed-Witten restrictions on the full visible
   cycle set;
2. the physical non-pullback visible/hidden Fermi bundle beyond the now-closed
   aggregate local anomaly, followed by its differential Bianchi row and exact
   IR SCFT;
3. the seven q79 seed characters, their modular mixing/GSO completion, and
   factorization data;
4. q79-specific string-field vertices satisfying the quantum BV master equation;
5. tadpole/vacuum-shift and massless soft/IR control.

The current flux paper explicitly works only to first order in `alpha'`, and
the current string paper proves beta-function vanishing only to a controlled
order while invoking modular invariance only in the CY/toroidal corner. Those
statements cannot be promoted to an exact q79 CFT.

## Nonperturbative boundary

Fixed-genus UV finiteness does not prove convergence of the sum over genera and
does not provide a nonperturbative definition at finite string coupling. Even
after the worldsheet packet closes, all-genus summability or a genuine
nonperturbative completion remains a separate final gate.

## Primary mathematical sources

- [Superstring Perturbation Theory Revisited](https://arxiv.org/abs/1209.5461)
- [Ultraviolet and Infrared Divergences in Superstring Theory](https://arxiv.org/abs/1512.00026)
- [BV Master Action for Heterotic and Type II String Field Theories](https://arxiv.org/abs/1508.05387)
- [Linear Models for Flux Vacua](https://arxiv.org/abs/hep-th/0611084)
- [Anomaly Cancellation and Smooth Non-Kahler Solutions](https://arxiv.org/abs/hep-th/0604137)
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
