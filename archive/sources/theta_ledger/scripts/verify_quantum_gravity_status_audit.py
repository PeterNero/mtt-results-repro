from __future__ import annotations

import json
from pathlib import Path


PROGRAM = Path(__file__).resolve().parents[1]
TEXPAPERS = PROGRAM.parent
QG = TEXPAPERS / "12 Quantum Gravity"
WORK = QG / "_work"
RESULTS = TEXPAPERS / "mtt-results-repro" / "release" / "authority"
GR_RESPONSE = TEXPAPERS / "mtt-protospinor-gr-response-proof"

AUDIT = QG / "MTT_QUANTUM_GRAVITY_RESEARCH_AND_PAPER_STATUS_AUDIT_2026-07-15.md"
LEDGER = QG / "MTT_QUANTUM_GRAVITY_STATUS_LEDGER_2026-07-15.json"


PAPERS = {
    "QG-1": "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4",
    "QG-2": "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector",
    "QG-3": "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping",
    "QG-4": "Constructive_MTT_Quantum_Gravity_III__Infrared_Limit_and_Scattering_under_SPT_Damping",
    "QG-5": "Asymptotic_Safety_as_a_Truncation_Shadow_of_a_Coherent_Sector_UV_Endpoint",
    "QG-6": "Modal_Triplet_Theory_and_Asymptotic_Safety__Asymptotic_Safety_as_the_Controlled_FRG_Shadow_of_the_Coherent_Sector_UV_Endpoint",
    "QG-7": "A_Third_Corner_Shadow_Bridge__Asymptotic_Safety__the_String_Corner__and_the_Coherent_Spine_in_Modal_Triplet_Theory",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.is_file(), f"missing file: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> None:
    audit = read(AUDIT)
    ledger = json.loads(read(LEDGER))

    require(ledger["core_paper_count"] == 7, "ledger must contain seven core papers")
    require(len(ledger["papers"]) == 7, "paper row count mismatch")
    require(
        {row["id"] for row in ledger["papers"]} == set(PAPERS),
        "paper identifiers are incomplete or duplicated",
    )

    for paper_id, directory in PAPERS.items():
        main_tex = WORK / directory / "main.tex"
        read(main_tex)
        require(paper_id in audit, f"audit is missing {paper_id}")
        require(directory in audit, f"audit is missing paper directory {directory}")

    qg_v4 = read(WORK / PAPERS["QG-1"] / "main.tex")
    require("UV-Finite, Unitary Quantum Gravity" in qg_v4, "flagship claim changed")
    require("at least one internal graviton line" in qg_v4, "all-loop claim changed")
    require("Stieltjes" in qg_v4 and "Gaussian" in qg_v4, "spectral/Gaussian claim changed")

    qg_i = read(WORK / PAPERS["QG-2"] / "main.tex")
    require(r"C\in \HS" in qg_i, "QG I covariance premise changed")
    require(r"Borel sums converge as $P\to\infty$" in qg_i, "QG I limit claim changed")

    qg_iii = read(WORK / PAPERS["QG-4"] / "main.tex")
    require(r"admits M{\o}ller operators" in qg_iii, "QG III circular premise changed")
    require(r"Hence $S=\Omega_+^\ast\Omega_-$ is unitary" in qg_iii, "QG III unitarity step changed")

    a18 = read(
        RESULTS
        / "A18"
        / "proof_corpus"
        / "MTT_Selected_QuantizationAndNonperturbativeQFT_StrictUpgradeAudit_v1.md"
    )
    require("U7 remains partial" in a18, "authoritative U7 status changed")
    require("partially closed" in a18, "authoritative U8 partial status changed")

    no_go = read(GR_RESPONSE / "proof_corpus" / "BTT_Exact_Support_Independence_NoGo_v1.md")
    require("independent of the currently sourced assumptions" in no_go, "BTT no-go changed")
    require("two-dimensional coherent internal toy support" in no_go, "BTT countermodel changed")

    canonical = json.loads(
        read(
            GR_RESPONSE
            / "candidate_data"
            / "selected_core_b0_tt_factorization_packet.canonical_fill.json"
        )
    )
    require(
        canonical["status"] == "CANONICAL_PACKET_FILLED_TESTS_PASS_SOURCE_ACCEPTANCE_OPEN",
        "canonical B0 packet no longer declares source acceptance open",
    )

    promotion = read(GR_RESPONSE / "scripts" / "compute_selected_core_b0_tt_source_theorem.py")
    require('"source_acceptance": True' in promotion, "B0 promotion mechanism changed")
    require(
        "SUPERSEDED_BY_EXPLICIT_Q79_Z64_QWW_FACTORIZATION_CLOSED_ON_SELECTED_BRANCH_CURRENT_ABSTRACT_SELECTION_NOGO_ONE_DISCRETE_A_QG_COMPLETION_AVAILABLE"
        == ledger["research_gates"]["selected_B0_TT_support_source"],
        "ledger must record the selected-branch q79/Z64/QWW factorization tier",
    )

    dg_frontier = json.loads(
        read(GR_RESPONSE / "certificates" / "qg_actual_dg_frontier_synthesis_certificate.json")
    )
    require(
        dg_frontier["status"]
        == "Q79_LOW_ENERGY_QG_EFT_PARITY_CLOSED_HETEROTIC_PRIMARY_UV_ROUTE_SELECTED_FIXED_GENUS_INHERITANCE_CONDITIONAL_WORLDSHEET_AND_NONPERTURBATIVE_COMPLETION_OPEN",
        "actual DG frontier status changed",
    )
    require(
        dg_frontier["supersession"]["current_evidentiary_status"]
        == "SUPERSEDED_AS_UNCONDITIONAL_PROOF",
        "old Boolean source theorem was not superseded",
    )
    require(
        ledger["overall_status"]
        == "LOW_ENERGY_QG_EFT_PARITY_CLOSED_Q79_HETEROTIC_PRIMARY_UV_ROUTE_SELECTED_FIXED_GENUS_INHERITANCE_CONDITIONAL_EXACT_WORLDSHEET_AND_NONPERTURBATIVE_COMPLETION_OPEN",
        "ledger headline did not advance to the selected heterotic UV route",
    )

    finite_operator = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
        )
    )
    finite_classical = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_finite_source_tegr_classical_closure_certificate.json"
        )
    )
    free_graviton = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_free_graviton_quantization_and_uv_cutset_certificate.json"
        )
    )
    low_energy_eft = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_interacting_low_energy_qg_eft_closure_certificate.json"
        )
    )
    finite_modular = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
        )
    )
    twisted_algebra = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_twisted_group_algebra_topological_character_certificate.json"
        )
    )
    seven_seed = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_seven_seed_modular_induction_stabilizers_certificate.json"
        )
    )
    k3_fuyau_glsm = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
        )
    )
    aggregate_tlsm = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo_certificate.json"
        )
    )
    simultaneous_c2_c3 = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
        )
    )
    fuyau_mixed_c2_hodge = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_fuyau_mixed_c2_hodge_admissibility_certificate.json"
        )
    )
    pullback_chirality_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_standard_tlsm_pullback_chirality_nogo_certificate.json"
        )
    )
    heterotic_uv = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_heterotic_string_uv_inheritance_cutset_certificate.json"
        )
    )
    primitive_branch = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_primitive_branch_selection_cutset_certificate.json"
        )
    )
    require(
        finite_operator["claim_tiers"]["finite_rootstack_TT_2x2_block"]
        == "CLOSED_EXACT_IDENTITY_SHAPE"
        and finite_operator["finite_data"]["TT_multiplicity_block"]
        == [["1", "0"], ["0", "1"]]
        and ledger["research_gates"]["q79_finite_projected_rootstack_tt_hessian"]
        == "CLOSED_EXACT_IDENTITY_SHAPE_ZERO_DIMENSIONLESS_FITS_ONE_SCALE",
        "finite Reynolds TT operator was lost",
    )
    require(
        finite_classical["claim_tiers"][
            "classical_GR_equivalence_at_declared_finite_source_IR_tier"
        ]
        == "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES"
        and finite_classical["parameter_ledger"][
            "continuous_effective_law_parameter_count"
        ]
        == 2
        and ledger["research_gates"]["q79_finite_source_classical_gr"]
        == "CLOSED_CONDITIONAL_TWO_PARAMETER_TIER_ZERO_DIMENSIONLESS_SHAPE_KNOBS",
        "finite-source classical GR tier was lost",
    )
    require(
        free_graviton["claim_tiers"]["free_massless_q79_graviton_carrier"]
        == "CLOSED_EXACT_TWO_HELICITIES"
        and free_graviton["claim_tiers"][
            "finite_internal_trace_changes_4D_UV_power_counting"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["free_q79_massless_graviton_quantization"]
        == "CLOSED_EXACT_TWO_HELICITIES_CONDITIONAL_CAUSAL_VACUUM",
        "free q79 graviton or finite-internal UV no-go was lost",
    )
    require(
        low_energy_eft["claim_tiers"]["interacting_low_energy_quantum_GR_EFT"]
        == "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER"
        and low_energy_eft["finite_data"]["connected_graph_superficial_degree"]
        == "2L+2"
        and low_energy_eft["claim_tiers"]["two_loop_pure_GR_divergence"]
        == "CLOSED_NONZERO_GOROFF_SAGNOTTI_STANDARD_RESULT"
        and low_energy_eft["guardrails"][
            "claims_standard_EFT_quantization_is_derived_from_MTT"
        ]
        is False
        and ledger["research_gates"]["interacting_low_energy_quantum_gr_eft"]
        == "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER"
        and ledger["research_gates"]["full_interacting_quantum_gravity"]
        == "OPEN_ALL_SCALE_UV_COMPLETE_TIER",
        "interacting low-energy QG EFT tier or UV boundary was lost",
    )
    require(
        finite_modular["finite_data"]["torus_twist_sector_count"] == 81
        and finite_modular["finite_data"]["modular_orbit_sizes"]
        == [1, 8, 8, 8, 8, 24, 24]
        and twisted_algebra["claim_tiers"]["selected_q79_twisted_group_algebra"]
        == "CLOSED_EXACT_ISOMORPHIC_TO_MAT3C"
        and twisted_algebra["finite_data"][
            "normalized_finite_topological_torus_index"
        ]
        == "1"
        and seven_seed["finite_data"]["finite_invariance_constraint_rank"]
        == 74
        and seven_seed["finite_data"]["finite_invariant_seed_dimension"] == 7,
        "q79 finite worldsheet modular/module/induction layer changed",
    )
    require(
        k3_fuyau_glsm["claim_tiers"]["explicit_degree_two_K3_smoothness"]
        == "CLOSED_EXACT"
        and k3_fuyau_glsm["incidence_GLSM"]["charge_matrix"]
        == [[1, 1, 1, 3, 0, 1, -3, -4], [0, 0, 0, 0, 1, 1, -1, -1]]
        and k3_fuyau_glsm["intersection_and_torsion_source"]["delta_square"]
        == "-4"
        and k3_fuyau_glsm["intersection_and_torsion_source"][
            "torsion_shift_charge_skeleton"
        ]["shared_circle_divisor_vector_in_H_L_basis"]
        == [0, 0]
        and k3_fuyau_glsm["q79_same_branch_arithmetic"]["reference_Bianchi"][
            "identity"
        ]
        == "9+11+4=24"
        and k3_fuyau_glsm["claim_tiers"]["exact_q79_IR_SCFT"] == "OPEN",
        "q79 degree-two K3 incidence GLSM or Fu-Yau source changed",
    )
    require(
        aggregate_tlsm["claim_tiers"]["aggregate_local_TLSM_anomaly_matrix"]
        == "CLOSED_EXACT_CONDITIONAL_ON_RANKONE_FUYAU_SOURCE"
        and aggregate_tlsm["local_TLSM_anomaly"]["quantum_anomaly_matrix"]
        == [[2, -2], [-2, 2]]
        and aggregate_tlsm["local_TLSM_anomaly"]["circle_shift_rows_M"]
        == [[1, -1], [0, 0]]
        and aggregate_tlsm["local_TLSM_anomaly"]["axial_rows_N"]
        == [[4, -4], [0, 0]]
        and aggregate_tlsm["local_TLSM_anomaly"]["active_fiber_radius_squared"]
        == 2
        and aggregate_tlsm["aggregate_rank12_bundle_monad"]["rank"] == 12
        and aggregate_tlsm["aggregate_rank12_bundle_monad"]["integral_c2"]
        == 20
        and aggregate_tlsm["claim_tiers"][
            "separate_odd_SU3_SU9_Picard_line_monads"
        ]
        == "CLOSED_EXACT_NOGO"
        and aggregate_tlsm["guardrails"][
            "claims_aggregate_monad_is_physical_V3_plus_W9"
        ]
        is False,
        "q79 exact local TLSM anomaly, aggregate monad, or odd-sector no-go changed",
    )
    require(
        pullback_chirality_nogo["schema"]
        == "MTTQ79StandardTLSMPullbackChiralityNoGo.v4"
        and pullback_chirality_nogo["claim_tiers"][
            "standard_TLSM_pullback_c3_zero"
        ]
        == "CLOSED_EXACT_NOGO"
        and pullback_chirality_nogo["standard_TLSM_pullback_theorem"][
            "pullback_c3"
        ]
        == 0
        and pullback_chirality_nogo["claim_tiers"][
            "topological_nonpullback_SU3_c3_plusminus6"
        ]
        == "CLOSED_EXACT"
        and pullback_chirality_nogo["physical_chiral_target"]["integral_c3"]
        == [6, -6]
        and pullback_chirality_nogo["physical_chiral_target"][
            "generation_index_half_c3"
        ]
        == [3, -3]
        and pullback_chirality_nogo["claim_tiers"][
            "holomorphic_nonpullback_SU3_worldsheet_bundle"
        ]
        == "OPEN",
        "q79 pullback chirality no-go or non-pullback target changed",
    )
    require(
        simultaneous_c2_c3["schema"]
        == "MTTQ79SharedCircleClutchingC2C3Independence.v1"
        and simultaneous_c2_c3["total_space_calculation"]["H4_rank"] == 21
        and simultaneous_c2_c3["total_space_calculation"]["H6_rank"] == 1
        and simultaneous_c2_c3["q79_candidate_specialization"][
            "simultaneous_reference_member"
        ]["c2"]
        == "9 u"
        and simultaneous_c2_c3["q79_candidate_specialization"][
            "simultaneous_reference_member"
        ]["c3"]
        == [6, -6]
        and simultaneous_c2_c3["claim_tiers"][
            "holomorphic_nonpullback_SU3_bundle"
        ]
        == "OPEN",
        "q79 simultaneous c2/c3 topological theorem changed or was overpromoted",
    )
    require(
        fuyau_mixed_c2_hodge["schema"]
        == "MTTQ79FuYauMixedC2HodgeAdmissibility.v1"
        and fuyau_mixed_c2_hodge["differential_representatives"]["u"][
            "bidegree"
        ]
        == [2, 2]
        and fuyau_mixed_c2_hodge["claim_tiers"][
            "mixed_c2_9u_Hodge_admissibility"
        ]
        == "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE"
        and fuyau_mixed_c2_hodge["claim_tiers"][
            "holomorphic_nonpullback_SU3_bundle"
        ]
        == "OPEN",
        "q79 Fu-Yau Hodge admissibility changed or was overpromoted",
    )
    require(
        pullback_chirality_nogo["checks"][
            "A128_all_90_continuous_root_tubes_closed"
        ]
        and pullback_chirality_nogo["checks"][
            "A129_handles_and_global_surface_relation_closed"
        ]
        and pullback_chirality_nogo["checks"][
            "A130_exact_integral_H2_basis_closed"
        ]
        and pullback_chirality_nogo["checks"][
            "A131_floating_period_table_and_A132_Z90_quotient_closed"
        ]
        and pullback_chirality_nogo["checks"][
            "A151_exact_interval_support_is_16_of_71_z_adapter_closed_branch_open"
        ],
        "q79 twisted-spectral A128-A151 frontier regressed",
    )
    require(
        heterotic_uv["claim_tiers"]["q79_heterotic_string_route_selection"]
        == "CLOSED_PRIMARY_COMPATIBLE_ROUTE"
        and heterotic_uv["claim_tiers"]["fixed_genus_heterotic_UV_inheritance"]
        == "CLOSED_CONDITIONAL_THEOREM"
        and heterotic_uv["finite_data"]["worldsheet_contract_rows_available"]
        == 5
        and heterotic_uv["finite_data"]["worldsheet_contract_rows_partial"]
        == 2
        and heterotic_uv["guardrails"]["claims_full_UV_complete_QG_closed"]
        is False,
        "q79 heterotic UV route or exact-worldsheet boundary changed",
    )
    require(
        ledger["research_gates"]["selected_qg_uv_completion_route"]
        == "CLOSED_PRIMARY_Q79_HETEROTIC_STRING_INHERITANCE"
        and ledger["research_gates"]["fixed_genus_q79_heterotic_uv_inheritance"]
        == "CLOSED_CONDITIONAL_THEOREM"
        and ledger["research_gates"]["q79_worldsheet_contract"]
        == "OPEN_5_OF_12_AVAILABLE_2_PARTIAL"
        and ledger["research_gates"]["q79_explicit_degree2_k3_incidence_glsm"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["q79_rank_one_fuyau_divisor_source"]
        == "CLOSED_EXACT_DELTA_EQUALS_H_MINUS_L_SQUARE_MINUS4"
        and ledger["research_gates"]["q79_full_heterotic_bundle_ej_and_local_tlsm_anomaly"]
        == "PARTIAL_LOCAL_TLSM_ANOMALY_CLOSED_PHYSICAL_NONPULLBACK_SU3_SU9_EJ_OPEN"
        and ledger["research_gates"]["q79_local_tlsm_anomaly_matrix"]
        == "CLOSED_EXACT_CONDITIONAL_A_EQUALS_2_DELTA_DELTA_TRANSPOSE"
        and ledger["research_gates"]["q79_integral_tlsm_torsion_charge_rows"]
        == "CLOSED_EXACT_M1_1_MINUS1_N1_4_MINUS4_K1_SQUARED_2_SECOND_CIRCLE_NEUTRAL"
        and ledger["research_gates"]["q79_aggregate_rank12_fermi_monad"]
        == "CLOSED_EXACT_ANOMALY_EQUIVALENCE_C1_ZERO_C2_20_NOT_PHYSICAL_SU3_PLUS_SU9_SPLIT"
        and ledger["research_gates"][
            "q79_separate_odd_su3_su9_picard_line_monads"
        ]
        == "CLOSED_EXACT_NOGO_BY_MOD2_PICARD_PARITY"
        and ledger["research_gates"][
            "q79_standard_tlsm_pullback_three_family_bundle"
        ]
        == "CLOSED_EXACT_NOGO_C3_ZERO"
        and ledger["research_gates"][
            "q79_shared_circle_simultaneous_c2_c3_clutching"
        ]
        == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE_C2_9U_C3_PLUSMINUS6_HOLOMORPHIC_HYM_BIANCHI_OPEN"
        and ledger["research_gates"][
            "q79_nonpullback_c2_c3_fuyau_hodge_admissibility"
        ]
        == "CLOSED_EXACT_CONDITIONAL_C2_9U_TYPE_22_C3_TYPE_33_HOLOMORPHIC_BUNDLE_OPEN"
        and ledger["research_gates"]["q79_physical_nonpullback_su3_su9_fermi_ej"]
        == "OPEN_TWISTED_SPECTRAL_OR_NONABELIAN_CURRENT_ALGEBRA_SOURCE_REQUIRED"
        and ledger["research_gates"][
            "q79_twisted_spectral_continuous_root_tubes_and_local_pl_monodromies"
        ]
        == "CLOSED_EXACT_90_OF_90"
        and ledger["research_gates"][
            "q79_twisted_spectral_handles_and_global_surface_relation"
        ]
        == "CLOSED_EXACT_TWO_HANDLES"
        and ledger["research_gates"]["q79_twisted_spectral_integral_h2_presentation"]
        == "CLOSED_EXACT_92_COLUMNS"
        and ledger["research_gates"][
            "q79_twisted_spectral_effective_integral_branch_quotient"
        ]
        == "CLOSED_EXACT_Z90"
        and ledger["research_gates"]["q79_twisted_spectral_weighted_e32_intervals"]
        == "CLOSED_EXACT_71_OF_71_L1_123_OF_123_CANONICALLY_ORIENTED_WEIGHTED_RADIUS_0P0004842494354306837"
        and ledger["research_gates"]["q79_final_integral_branch_selection"]
        == "OPEN_AFTER_A207_FROZEN_HEIGHT4_CARRIER_RIGOROUSLY_REJECTED_ALTERNATIVE_SELECTED_CARRIER_REQUIRED"
        and ledger["research_gates"]["q79_selected_finite_twisted_group_algebra"]
        == "CLOSED_EXACT_MAT3C"
        and ledger["research_gates"]["q79_seven_seed_stabilizer_induction"]
        == "CLOSED_EXACT_FINITE_LAYER"
        and ledger["research_gates"]["q79_exact_torsion_glsm_or_worldsheet_scft"]
        == "PARTIAL_EXPLICIT_K3_GLSM_LOCAL_TLSM_ANOMALY_AND_AGGREGATE_FERMI_MONAD_CLOSED_PHYSICAL_NONPULLBACK_BUNDLE_AND_IR_SCFT_OPEN"
        and ledger["research_gates"]["q79_nonperturbative_uv_completion"]
        == "OPEN",
        "QG ledger lost or overpromoted the heterotic UV route",
    )
    require(
        primitive_branch["claim_tiers"][
            "primitive_branch_selection_from_unaugmented_current_MTT"
        ]
        == "CLOSED_NO_GO_BY_EXPLICIT_TWO_BRANCH_AUTOMORPHISM_MODEL"
        and primitive_branch["claim_tiers"]["minimal_extra_branch_selection_data"]
        == "CLOSED_ONE_DISCRETE_PHYSICAL_REALIZATION_AXIOM_ZERO_CONTINUOUS_KNOBS"
        and primitive_branch["parameter_ledger"][
            "additional_discrete_physical_realization_axioms"
        ]
        == 1
        and primitive_branch["parameter_ledger"][
            "additional_continuous_parameters_from_branch_axiom"
        ]
        == 0
        and primitive_branch["countermodel"]["invariant_minimizer_set"]
        == ["R0", "R1"]
        and primitive_branch["guardrails"][
            "claims_A_QG_is_derived_rather_than_adopted"
        ]
        is False,
        "primitive branch no-go or minimal one-axiom completion was lost",
    )
    require(
        ledger["research_gates"][
            "primitive_branch_two_branch_automorphism_countermodel"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["minimal_extra_physical_realization_data"]
        == "CLOSED_ONE_DISCRETE_AXIOM_ZERO_CONTINUOUS_KNOBS"
        and ledger["research_gates"]["q79_geometry_operator_choice_after_A_QG"]
        == "CLOSED_UNIQUE_UP_TO_DECLARED_GAUGE"
        and ledger["research_gates"]["augmented_mtt_low_energy_qg_law_after_A_QG"]
        == "CLOSED_CONDITIONAL_ON_KAPPA_LAMBDA_EFT_DATA_AND_STATE",
        "ledger lost the primitive branch cutset or A_QG completion",
    )
    require(
        ledger["research_gates"]["actual_DG_metric_rows"]
        == "GLOBAL_COVARIANT_BUNDLE_CONSTRUCTION_CLOSED_GAPPED_DSTAR_COMPONENT_SELECTED_ACTION_OPEN",
        "ledger lost the actual DG computation",
    )
    require(
        ledger["research_gates"]["same_circle_physical_selection"]
        == "FINITE_SAME_SOURCE_MAP_CLOSED_GLOBAL_LINE_IDENTITY_NOGO_ASSOCIATED_BUNDLE_REPLACEMENT_CLOSED",
        "ledger lost or overclaims the same-circle Z2 reduction",
    )

    same_circle = json.loads(
        read(GR_RESPONSE / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json")
    )
    require(
        same_circle["finite_Z64_result"]["kernel"] == [0, 32]
        and same_circle["finite_Z64_result"]["square_root_character_labels"] == [1, 33],
        "same-circle finite root calculation changed",
    )
    require(
        same_circle["guardrails"]["claims_weight2_data_selects_a_unique_weight1_root"]
        is False,
        "same-circle certificate overclaims a root",
    )

    odd_lift = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "protospinor_odd_weight_lift_selector_dichotomy_certificate.json"
        )
    )
    require(
        odd_lift["status"]
        == "EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED",
        "proto-spinor/TT Z2 frontier changed",
    )
    require(
        ledger["research_gates"]["proto_spinor_gravity_Z2_interface"]
        == "W2_SPIN_NOGO_SPINC_SAME_SOURCE_FULL_MONODROMY_ROOTSTACK_AND_SPECTRAL_SHEET_SYMBOL_BRIDGES_CLOSED_PRIMITIVE_PHYSICAL_SELECTION_OPEN",
        "ledger lost the proto-spinor/TT interface theorem",
    )

    q79_w2 = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"
        )
    )
    require(
        q79_w2["universal_w2_theorem"]["result"] == "w2(E_rho_plus)=a cup a"
        and q79_w2["branch_divisor_theorem"]["branch_class"] == "[B]=6H",
        "q79 w2 or branch-divisor theorem changed",
    )

    trial_spin = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_trial_branch_irreducibility_and_spin_decision_certificate.json"
        )
    )
    require(
        trial_spin["decision"]["trial_identity_alignment"]["strict_Spin"]
        == "NO_GO"
        and trial_spin["guardrails"]["claims_selected_q79_strict_Spin_no_go"]
        is False,
        "trial/selected q79 Spin boundary changed",
    )
    require(
        ledger["research_gates"]["q79_trial_strict_spin_decision"]
        == "IDENTITY_ALIGNMENT_EXACT_NO_GO_SUPERSEDED_BY_SELECTED_SIDE_INTERVAL_TEST",
        "ledger lost the exact trial Spin decision",
    )

    selected_spinc = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_selected_side_spin_spinc_decision_certificate.json"
        )
    )
    require(
        selected_spinc["checks"]["selected_side_norm_resultant_excludes_zero"]
        is True
        and selected_spinc["decision"]["current_executed_selected_side"]["strict_Spin"]
        == "NO_GO",
        "selected-side strict-Spin decision changed",
    )
    require(
        selected_spinc["SpinC_theorem"]["generated_image_order"] == 6
        and selected_spinc["SpinC_theorem"]["determinant_character"]
        == "z^2=sign(sheet permutation)",
        "signed-sheet SpinC theorem changed",
    )
    require(
        selected_spinc["guardrails"]["claims_integral_gerbe_branch_selected"]
        is False,
        "selected-side certificate overclaims the final integral branch",
    )
    require(
        ledger["research_gates"]["q79_selected_side_strict_spin"]
        == "CLOSED_NO_GO_ON_EXECUTED_A125_A126_INTERVAL",
        "ledger lost the selected-side strict-Spin no-go",
    )
    require(
        ledger["research_gates"]["q79_signed_sheet_spinc_lift"]
        == "CLOSED_REPRESENTATION_LEVEL",
        "ledger lost or overclaims the SpinC lift",
    )
    require(
        ledger["research_gates"]["q79_final_integral_branch_selection"]
        == "OPEN_AFTER_A207_FROZEN_HEIGHT4_CARRIER_RIGOROUSLY_REJECTED_ALTERNATIVE_SELECTED_CARRIER_REQUIRED",
        "ledger overclaims the final integral branch",
    )

    shared_det_bridge = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_circle_spinc_determinant_bridge_certificate.json"
        )
    )
    require(
        shared_det_bridge["finite_data"]["hom_generator_images"] == [0, 32]
        and shared_det_bridge["checks"]["both_roots_have_identical_restriction"]
        is True,
        "root-independent shared determinant bridge changed",
    )
    require(
        shared_det_bridge["claim_tiers"]["MTT_same_source_emission_of_central_map"]
        == "OPEN",
        "shared determinant bridge overclaims same-source emission",
    )
    require(
        ledger["research_gates"]["q79_shared_circle_spinc_determinant_bridge"]
        == "CLOSED_ROOT_INDEPENDENT",
        "ledger lost the shared determinant bridge",
    )

    same_source = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_z64_same_source_monodromy_map_certificate.json"
        )
    )
    require(
        same_source["claim_tiers"]["finite_same_source_q79_to_Z64_monodromy_map"]
        == "CLOSED_UNIQUE",
        "finite same-source q79/Z64 map changed",
    )
    require(
        ledger["research_gates"]["q79_shared_z64_same_source_monodromy_map"]
        == "CLOSED_UNIQUE",
        "ledger lost the finite same-source map",
    )

    double_return = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_circle_double_return_cln_nil_flat_endpoint_certificate.json"
        )
    )
    require(
        double_return["finite_data"]["odd_root_character_sequences"]
        == {"1": [1, -1, 1], "33": [1, -1, 1]}
        and double_return["finite_data"]["metric_character_sequence"]
        == [1, 1, 1]
        and double_return["finite_data"]["folded_nil_cohomology_dimension"] == 0,
        "q79 double return or finite CLN Nil complex changed",
    )
    require(
        double_return["claim_tiers"][
            "double_return_alone_forces_zero_metric_strain"
        ]
        == "CLOSED_NO_GO"
        and double_return["claim_tiers"][
            "canonical_zero_defect_Minkowski_coframe"
        ]
        == "CLOSED_EXACT"
        and double_return["claim_tiers"][
            "double_return_dynamically_selects_zero_defect"
        ]
        == "OPEN"
        and double_return["claim_tiers"]["Lambda_eff_zero"] == "OPEN",
        "flat endpoint was lost or overpromoted",
    )
    require(
        ledger["research_gates"]["q79_shared_circle_odd_double_return"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT_PLUS_MINUS_PLUS"
        and ledger["research_gates"]["q79_same_source_finite_cln_nil_complex"]
        == "CLOSED_EXACT_ACYCLIC_OVER_CHARACTERISTIC_NOT_TWO"
        and ledger["research_gates"]["double_return_alone_forces_zero_metric_strain"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["canonical_zero_defect_minkowski_endpoint"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["dynamic_selection_of_zero_defect_endpoint"]
        == "OPEN",
        "ledger lost the double-return/flat-endpoint theorem boundary",
    )

    vacuum_selection = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_zero_defect_vacuum_selection_nogo_and_state_cutset_certificate.json"
        )
    )
    require(
        vacuum_selection["finite_data"]["Ricci_tensor"]
        == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        and vacuum_selection["finite_data"]["representative_plus_curvature"]
        == {"R_uxux": -1, "R_uyuy": 1}
        and vacuum_selection["claim_tiers"][
            "zero_stress_Lambda_zero_Einstein_equations_force_flatness"
        ]
        == "CLOSED_NO_GO",
        "vacuum flatness counterexample changed",
    )
    require(
        ledger["research_gates"]["exact_curved_ricci_flat_helicity_two_wave"]
        == "CLOSED_CONSTRUCTED"
        and ledger["research_gates"][
            "vacuum_einstein_tegr_equations_select_flat_endpoint"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "zero_defect_state_boundary_selection_contract"
        ]
        == "OPEN_5_ROWS_0_AVAILABLE",
        "ledger lost the vacuum-selection no-go or state cutset",
    )

    hym_extension = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_spinc_flat_hym_ramification_extension_certificate.json"
        )
    )
    require(
        hym_extension["claim_tiers"]["HYM_equation_on_smooth_complement"]
        == "CLOSED"
        and hym_extension["claim_tiers"]["ordinary_smooth_unramified_extension"]
        == "CLOSED_NO_GO",
        "flat-HYM/ordinary-extension dichotomy changed",
    )

    cusp_hym = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_branch_cusp_resolution_rootstack_hym_certificate.json"
        )
    )
    require(
        cusp_hym["finite_data"]["ordinary_cusp_count"] == 18
        and cusp_hym["finite_data"]["normalization_genus"] == 19
        and cusp_hym["finite_data"]["branch_arithmetic_genus"] == 37,
        "selected branch singularity inventory changed",
    )
    require(
        cusp_hym["claim_tiers"]["resolved_order_two_rootstack_flat_HYM_carrier"]
        == "CLOSED"
        and cusp_hym["claim_tiers"]["MTT_selection_of_resolved_rootstack_carrier"]
        == "OPEN",
        "resolved root-stack HYM tier changed",
    )
    require(
        ledger["research_gates"]["q79_spinc_flat_hym_on_complement"] == "CLOSED"
        and ledger["research_gates"]["q79_ordinary_smooth_ramification_extension"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["q79_selected_branch_singularity_inventory"]
        == "CLOSED_18_ORDINARY_CUSPS"
        and ledger["research_gates"]["q79_resolved_rootstack_flat_hym_carrier"]
        == "DETERMINANT_SUBSTACK_CLOSED_FULL_MONODROMY_RANK_SIX_EXTENSION_CLOSED_PRIMITIVE_PHYSICAL_SELECTION_OPEN",
        "ledger lost the HYM/ramification advance",
    )

    full_rootstack = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
        )
    )
    require(
        full_rootstack["claim_tiers"]["coarse_finite_flat_branch_extension_as_isomorphism"]
        == "CLOSED_NO_GO"
        and full_rootstack["claim_tiers"]["full_S3_cusp_monodromy"]
        == "CLOSED_EXACT_2_3_2_1"
        and full_rootstack["claim_tiers"]["minimal_full_monodromy_rootstack"]
        == "CLOSED_UNIQUE_MINIMAL"
        and full_rootstack["claim_tiers"]["rootstack_rank_six_strain_bundle_isomorphism"]
        == "CLOSED_EXACT"
        and full_rootstack["claim_tiers"]["rootstack_flat_HYM_connection_intertwining"]
        == "CLOSED_EXACT"
        and full_rootstack["claim_tiers"]["inverse_Fourier_Mukai_HYM_Hessian_intertwining"]
        == "OPEN",
        "full-monodromy q79 root-stack theorem changed",
    )
    require(
        full_rootstack["finite_data"]["minimal_root_orders"] == [2, 3, 2, 1]
        and full_rootstack["finite_data"]["simple_branch_rank"] == 3
        and full_rootstack["finite_data"]["simple_branch_smith_valuations"]
        == [0, 0, 0, 1, 1, 1],
        "q79 coarse-branch no-go or cusp monodromy data changed",
    )
    require(
        ledger["research_gates"]["q79_S3_strain_intertwiner"]
        == "CLOSED_NATURAL_UNIQUE_GLOBAL_AND_IDENTIFIED_AS_SPECTRAL_SHEET_SYMBOL_QUARTERTURN_SCALAR_FORM_CONDITIONAL_ACTUAL_HYM_OPERATOR_OPEN"
        and ledger["research_gates"]["q79_cubic_norm_coarse_branch_bridge"]
        == "CLOSED_NO_GO_DETERMINANT_EQUALS_MINUS_DISCRIMINANT_CUBED_AND_SIMPLE_BRANCH_RANK_THREE"
        and ledger["research_gates"]["q79_full_S3_cusp_monodromy_orders"]
        == "CLOSED_EXACT_2_3_2_1"
        and ledger["research_gates"]["q79_minimal_full_monodromy_rootstack"]
        == "CLOSED_UNIQUE_MINIMAL"
        and ledger["research_gates"]["q79_rootstack_rank_six_metric_connection_bridge"]
        == "CLOSED_EXACT_FLAT_HYM"
        and ledger["research_gates"]["q79_strict_same_source_rank_preserving_continuation"]
        == "CLOSED_UNIQUE_MINIMAL_FULL_MONODROMY_ROOTSTACK",
        "ledger lost the cubic-norm/full-monodromy root-stack advance",
    )

    helicity_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "global_helicity_bundle_same_circle_nogo_certificate.json"
        )
    )
    require(
        helicity_nogo["finite_data"]["external_weight_two_Chern_number"] == -4
        and helicity_nogo["claim_tiers"]["global_internal_external_line_identity"]
        == "CLOSED_NO_GO",
        "global shared/helicity line no-go changed",
    )

    global_dg = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "global_covariant_helicity2_dg_bundle_certificate.json"
        )
    )
    require(
        global_dg["claim_tiers"]["global_covariant_DG_bundle_map"]
        == "CLOSED_FOR_CONSTRUCTED_REALIZATION"
        and global_dg["claim_tiers"]["global_exact_Z64_support_identity"]
        == "CLOSED_FIBERWISE",
        "global covariant DG construction changed",
    )
    require(
        ledger["research_gates"]["global_shared_helicity_line_identity"]
        == "CLOSED_NO_GO_CHERN_0_VS_MINUS4"
        and ledger["research_gates"]["global_covariant_helicity2_DG_bundle"]
        == "CLOSED_FOR_CONSTRUCTED_REALIZATION",
        "ledger lost the global helicity correction",
    )

    q79_source_factorization = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "selected_q79_z64_qww_source_factorization_certificate.json"
        )
    )
    require(
        q79_source_factorization["claim_tiers"][
            "selected_branch_q79_Z64_QWW_source_realization"
        ]
        == "CLOSED_UNIQUE_UP_TO_GAUGE"
        and q79_source_factorization["claim_tiers"][
            "continuous_fitted_physical_parameters"
        ]
        == "CLOSED_ZERO"
        and q79_source_factorization["claim_tiers"][
            "primitive_MTT_selects_minimal_rootstack_Lorentzian_branch"
        ]
        == "OPEN"
        and q79_source_factorization["claim_tiers"][
            "inverse_Fourier_Mukai_HYM_operator_identity"
        ]
        == "OPEN",
        "selected-branch q79/Z64/QWW factorization tier changed",
    )
    require(
        q79_source_factorization["finite_data"]["source_rank"] == 2
        and q79_source_factorization["finite_data"]["q79_TT_embedding_gram"]
        == [["1", "0"], ["0", "1"]]
        and q79_source_factorization["guardrails"]["adds_fitted_numeric_parameter"]
        is False,
        "selected q79 TT source map or parameter count changed",
    )
    require(
        ledger["research_gates"]["selected_branch_q79_z64_qww_source_realization"]
        == "CLOSED_UNIQUE_UP_TO_POLARIZATION_FRAME_AND_DIFF_GAUGE"
        and ledger["research_gates"]["selected_branch_metric_source_fitted_parameters"]
        == "CLOSED_ZERO"
        and ledger["research_gates"][
            "inverse_fourier_mukai_hym_operator_identity_for_rootstack_carrier"
        ]
        == "LITERAL_FULL_CONNECTION_IDENTITY_CLOSED_NOGO_CORRECT_SHEET_SYMBOL_ROOT_INDEPENDENT_C4_PARENT_AND_FLAT_SYMBOL_JDE_FUNCTOR_CLOSED_FREE_ORBIT_DIRECT_ADJOINT_ORDINARY_DUAL_EXTERIOR_AND_MARKED_SHARED_CIRCLE_LENS_NOGOS_NONLOCAL_FM_CONTRACT_2_OF_11_CONTINUUM_ACTUAL_HYM_OPERATOR_OPEN_FINITE_REYNOLDS_OPERATOR_CLOSED",
        "ledger lost the explicit selected-branch source factorization",
    )

    spectral_hym_symbol = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
        )
    )
    require(
        spectral_hym_symbol["claim_tiers"][
            "spectral_sheet_symbol_to_q79_rootstack_strain_carrier"
        ]
        == "CLOSED_EXACT"
        and spectral_hym_symbol["claim_tiers"][
            "fiberwise_normalized_overlap_metric_on_strain_symbol"
        ]
        == "CLOSED_EXACT_IDENTITY"
        and spectral_hym_symbol["claim_tiers"][
            "literal_full_inverse_Fourier_Mukai_HYM_connection_identity"
        ]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION",
        "q79 spectral sheet-symbol bridge changed",
    )
    require(
        spectral_hym_symbol["finite_data"]["conditional_visible_c2"] == 9
        and spectral_hym_symbol["finite_data"]["conditional_underlying_real_p1"]
        == -18
        and spectral_hym_symbol["finite_data"][
            "physical_standard_isotypic_Hessian_block_shape"
        ]
        == [2, 2],
        "q79 HYM topology or projected Hessian cutset changed",
    )
    require(
        spectral_hym_symbol["claim_tiers"][
            "actual_q79_inverse_Fourier_Mukai_visible_bundle"
        ]
        == "OPEN_GERBE_AND_LOCAL_FREENESS"
        and spectral_hym_symbol["claim_tiers"]["actual_q79_balanced_HYM_connection"]
        == "OPEN"
        and spectral_hym_symbol["claim_tiers"][
            "dynamic_projected_HYM_Hessian_on_TT_standard_block"
        ]
        == "OPEN_REDUCED_TO_SYMMETRIC_2_BY_2_BLOCK",
        "future q79 spectral HYM calculation was overpromoted",
    )
    require(
        ledger["research_gates"][
            "q79_spectral_sheet_symbol_to_rootstack_strain_carrier"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["q79_strain_symbol_normalized_overlap_metric"]
        == "CLOSED_EXACT_IDENTITY_6_BY_6"
        and ledger["research_gates"][
            "q79_literal_full_hym_to_flat_rootstack_connection_identity"
        ]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        and ledger["research_gates"]["q79_actual_inverse_fourier_mukai_visible_bundle"]
        == "OPEN_GERBE_AND_LOCAL_FREENESS"
        and ledger["research_gates"]["q79_actual_balanced_hym_connection"] == "OPEN"
        and ledger["research_gates"]["q79_dynamic_projected_hym_tt_hessian"]
        == "OPEN_ACTUAL_OPERATOR_CONDITIONAL_SCALAR_FORM_CLOSED"
        and ledger["research_gates"][
            "q79_shared_central_circle_neutrality_in_spectral_endomorphisms"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "q79_full_relative_spectral_phase_neutrality"
        ]
        == "OPEN_EXACT_REDUCTION_TO_RELATIVE_PHASE_CONNECTION_GIVEN",
        "ledger lost the q79 spectral-HYM/root-stack correction",
    )

    quarterturn_hessian = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
        )
    )
    require(
        quarterturn_hessian["claim_tiers"][
            "canonical_q79_complement_lane_complex_structure"
        ]
        == "CLOSED_EXACT"
        and quarterturn_hessian["claim_tiers"][
            "self_adjoint_S3_quarterturn_Hessian_scalarization"
        ]
        == "CLOSED_EXACT"
        and quarterturn_hessian["finite_data"][
            "quarterturn_invariant_self_adjoint_commutant_dimension"
        ]
        == 2
        and quarterturn_hessian["finite_data"]["physical_TT_block"]
        == "H_std=kappa_standard*I2",
        "q79 complement-quarterturn Hessian scalarization changed",
    )
    require(
        quarterturn_hessian["claim_tiers"][
            "physical_TT_block_scalarization"
        ]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and quarterturn_hessian["claim_tiers"][
            "single_rank_one_FuYau_branch_supplies_order4_symmetry"
        ]
        == "CLOSED_NO_GO"
        and quarterturn_hessian["claim_tiers"][
            "minimal_four_branch_FuYau_Chern_orbit"
        ]
        == "CLOSED_EXACT"
        and quarterturn_hessian["claim_tiers"][
            "typed_lane_quarterturn_to_FuYau_Chern_orbit_source_functor"
        ]
        == "OPEN"
        and quarterturn_hessian["claim_tiers"][
            "selected_HYM_action_is_quarterturn_invariant"
        ]
        == "OPEN",
        "quarter-turn physical/source boundary was overpromoted",
    )
    require(
        ledger["research_gates"][
            "q79_canonical_complement_lane_complex_structure"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["q79_quarterturn_hessian_scalarization"]
        == "CLOSED_EXACT_COMMUTANT_DIMENSION_6_TO_2"
        and ledger["research_gates"]["q79_physical_tt_block_scalarization"]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and ledger["research_gates"]["single_rank_one_fuyau_order4_symmetry"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["minimal_four_branch_fuyau_chern_orbit"]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "typed_lane_quarterturn_to_fuyau_source_functor"
        ]
        == "CLOSED_CONDITIONAL_AT_FLAT_SYMBOL_AND_FUYAU_PARENT_REPRESENTATION_TIER_ACTUAL_HYM_EXTENSION_OPEN"
        and ledger["research_gates"]["selected_hym_action_quarterturn_invariance"]
        == "OPEN",
        "ledger lost the q79 quarter-turn reduction",
    )

    parent_quarterturn = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
        )
    )
    require(
        parent_quarterturn["finite_data"]["Z64_order4_subgroup"]
        == [0, 16, 32, 48]
        and parent_quarterturn["claim_tiers"][
            "odd_root_restriction_to_order4_subgroup"
        ]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and parent_quarterturn["claim_tiers"][
            "free_orbit_covariance_implies_single_branch_Hessian_invariance"
        ]
        == "CLOSED_NO_GO"
        and parent_quarterturn["claim_tiers"][
            "autonomous_Lens_quotient_descent_implies_quarterturn_invariance"
        ]
        == "CLOSED_EXACT_CONDITIONAL"
        and parent_quarterturn["claim_tiers"][
            "MTT_types_C4_as_Lens_redundancy_not_physical_superselection"
        ]
        == "OPEN",
        "shared-Z64 Fu-Yau parent/descent dichotomy changed",
    )

    square_theta_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_square_theta_quarterturn_strain_nogo_certificate.json"
        )
    )
    require(
        square_theta_nogo["finite_data"]["adjoint_J2_minus1_sector_dimension"]
        == 4
        and square_theta_nogo["finite_data"]["desired_JDE_sector_dimension"] == 6
        and square_theta_nogo["finite_data"]["strain_to_orientation_block_rank"]
        == 2
        and square_theta_nogo["claim_tiers"][
            "direct_theta_adjoint_realizes_six_dimensional_JDE"
        ]
        == "CLOSED_NO_GO"
        and square_theta_nogo["claim_tiers"][
            "nontrivial_inverse_Fourier_Mukai_induced_JDE_functor"
        ]
        == "OPEN",
        "square-theta direct-functor no-go changed",
    )

    rootplane_jde_functor = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
        )
    )
    require(
        rootplane_jde_functor["claim_tiers"][
            "determinant_twisted_exterior_square_edge_identification"
        ]
        == "CLOSED_EXACT"
        and rootplane_jde_functor["claim_tiers"][
            "shared_root_C4_realification"
        ]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and rootplane_jde_functor["claim_tiers"][
            "typed_shared_C4_to_rootstack_strain_JDE_functor"
        ]
        == "CLOSED_EXACT_ON_FLAT_SHEET_SYMBOL"
        and rootplane_jde_functor["claim_tiers"][
            "JDE_parallel_under_minimal_rootstack_flat_connection"
        ]
        == "CLOSED_EXACT"
        and rootplane_jde_functor["claim_tiers"][
            "direct_unital_Herm3_adjoint_realizes_full_JDE"
        ]
        == "CLOSED_NO_GO"
        and rootplane_jde_functor["claim_tiers"][
            "actual_inverse_Fourier_Mukai_HYM_induced_JDE"
        ]
        == "OPEN",
        "shared root-plane twisted-exterior JDE functor changed",
    )
    ordinary_hym_functor_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_certificate.json"
        )
    )
    require(
        ordinary_hym_functor_nogo["claim_tiers"][
            "ordinary_dual_and_exterior_square_preserve_HYM_equations"
        ]
        == "CLOSED_EXACT"
        and ordinary_hym_functor_nogo["claim_tiers"][
            "ordinary_dual_or_exterior_square_realizes_JDE"
        ]
        == "CLOSED_NO_GO"
        and ordinary_hym_functor_nogo["claim_tiers"][
            "nonzero_c3_branch_is_complex_linearly_self_dual"
        ]
        == "CLOSED_NO_GO"
        and ordinary_hym_functor_nogo["finite_data"][
            "derived_kernel_contract_rows_available"
        ]
        == 2
        and ordinary_hym_functor_nogo["finite_data"][
            "derived_kernel_contract_rows_required"
        ]
        == 11,
        "ordinary HYM functor no-go or derived-kernel cutset changed",
    )
    marked_c4_descent_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_marked_shared_circle_c4_descent_nogo_certificate.json"
        )
    )
    require(
        marked_c4_descent_nogo["claim_tiers"][
            "C4_preserves_the_marked_shared_circle_direction"
        ]
        == "CLOSED_NO_GO"
        and marked_c4_descent_nogo["claim_tiers"][
            "autonomous_Lens_descent_in_current_marked_shared_circle_setup"
        ]
        == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and marked_c4_descent_nogo["finite_data"][
            "quarterturn_shared_circle_image"
        ]
        == [-1, 0]
        and marked_c4_descent_nogo["finite_data"][
            "unmarked_modular_exit_contract_rows_available"
        ]
        == 0
        and marked_c4_descent_nogo["finite_data"][
            "unmarked_modular_exit_contract_rows_required"
        ]
        == 5,
        "marked shared-circle C4 descent no-go changed",
    )
    require(
        ledger["research_gates"]["shared_z64_unique_order4_subgroup"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["shared_z64_odd_root_c4_restriction"]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and ledger["research_gates"][
            "free_c4_orbit_covariance_scalarizes_branch_hessian"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["autonomous_lens_descent_scalarizes_hessian"]
        == "CLOSED_EXACT_CONDITIONAL"
        and ledger["research_gates"]["mtt_types_c4_as_lens_redundancy"]
        == "CLOSED_NO_GO_IN_CURRENT_MARKED_SHARED_CIRCLE_SETUP_UNMARKED_REFORMULATION_OPEN"
        and ledger["research_gates"][
            "marked_shared_circle_c4_autonomous_descent"
        ]
        == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and ledger["research_gates"]["unmarked_modular_parent_descent_contract"]
        == "OPEN_5_ROWS_0_AVAILABLE"
        and ledger["research_gates"]["square_theta_direct_adjoint_realizes_jde"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "determinant_twisted_exterior_square_edge_identification"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "shared_root_c4_to_flat_rootstack_strain_jde_functor"
        ]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and ledger["research_gates"][
            "jde_parallel_under_minimal_rootstack_flat_connection"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "direct_unital_herm3_adjoint_realizes_full_jde"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "ordinary_dual_and_exterior_square_preserve_hym"
        ]
        == "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR"
        and ledger["research_gates"][
            "ordinary_dual_or_exterior_square_realizes_jde"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "nonzero_c3_chiral_branch_complex_linear_self_duality"
        ]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "nonlocal_same_branch_fourier_mukai_jde_autoequivalence"
        ]
        == "OPEN_EXACT_11_ROW_KERNEL_EXT1_HESSIAN_CONTRACT_2_AVAILABLE"
        and ledger["research_gates"]["nontrivial_inverse_fourier_mukai_induced_jde"]
        == "OPEN_EXTENSION_FROM_FLAT_SYMBOL_TO_ACTUAL_HYM",
        "ledger lost the C4 parent, descent fork, or direct-theta no-go",
    )

    global_hessian = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
        )
    )
    require(
        global_hessian["claim_tiers"]["strain_to_metric_Hessian_coordinate_transport"]
        == "CLOSED_EXACT_FACTOR_ONE_QUARTER"
        and global_hessian["claim_tiers"]["Fierz_Pauli_operator_uniqueness"]
        == "CLOSED_CONDITIONAL_ON_FOUR_EXPLICIT_ACTION_HYPOTHESES",
        "global Hessian/action uniqueness reduction changed",
    )
    require(
        ledger["research_gates"]["global_TT_hessian_form"]
        == "CLOSED_UNDER_STATED_STABILITY_AND_COVARIANCE_HYPOTHESES"
        and ledger["research_gates"]["strain_to_metric_hessian_transport"]
        == "CLOSED_EXACT_KAPPA_H_EQUALS_KAPPA_E_OVER_4",
        "ledger lost the global Hessian transport",
    )

    action_reduction = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "closure_to_einstein_action_reduction_certificate.json"
        )
    )
    require(
        action_reduction["claim_tiers"]["finite_closure_Hessian_self_adjointness"]
        == "CLOSED_FROM_C3_SCALAR_FUNCTIONAL"
        and action_reduction["claim_tiers"][
            "four_dimensional_nonlinear_metric_completion"
        ]
        == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES",
        "closure reciprocity or nonlinear Einstein reduction changed",
    )
    require(
        action_reduction["claim_tiers"]["independent_stress_normalization"]
        == "CLOSED_NONE_BEYOND_KAPPA_H"
        and action_reduction["claim_tiers"][
            "scale_free_q79_data_fix_numeric_kappa_h"
        ]
        == "CLOSED_NO_GO",
        "stress normalization or Newton scale no-go changed",
    )
    require(
        action_reduction["claim_tiers"][
            "selected_MTT_local_diffeomorphism_natural_action"
        ]
        == "OPEN"
        and action_reduction["claim_tiers"]["selected_numeric_kappa_h_or_G4"]
        == "OPEN_ONE_EFFECTIVE_NORMALIZATION"
        and action_reduction["claim_tiers"]["selected_Lambda_eff"] == "OPEN",
        "selected GR data were overpromoted",
    )
    require(
        ledger["research_gates"]["finite_closure_hessian_self_adjointness"]
        == "CLOSED_FROM_C3_SCALAR_FUNCTIONAL"
        and ledger["research_gates"]["nonlinear_einstein_metric_completion"]
        == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES"
        and ledger["research_gates"]["independent_stress_normalization"]
        == "CLOSED_NONE_BEYOND_KAPPA_H"
        and ledger["research_gates"]["scale_free_q79_data_fix_numeric_newton"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["physical_newton_planck_normalization"]
        == "OPEN_ONE_EFFECTIVE_NORMALIZATION_PROVED_NECESSARY"
        and ledger["research_gates"]["selected_lambda_eff"] == "OPEN",
        "ledger lost the closure-to-Einstein advance",
    )

    teleparallel = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"
        )
    )
    require(
        teleparallel["claim_tiers"][
            "closure_potential_alone_generates_massless_spin2_kinetic_term"
        ]
        == "CLOSED_NO_GO"
        and teleparallel["claim_tiers"]["coframe_torsion_as_literal_nonclosure_tensor"]
        == "CLOSED_EXACT",
        "closure-potential no-go or coframe nonclosure theorem changed",
    )
    require(
        teleparallel["claim_tiers"]["TEGR_Einstein_Hilbert_boundary_identity"]
        == "CLOSED_EXACT"
        and teleparallel["theorem"]["part_E_exact_symbolic_execution"]["residual"]
        == "0",
        "exact TEGR/Einstein identity changed",
    )
    require(
        teleparallel["claim_tiers"]["direct_two_derivative_action_exit"]
        == "EXACT_TELEPARALLEL_CANDIDATE_CONSTRUCTED_SELECTION_OPEN"
        and teleparallel["claim_tiers"][
            "global_Lorentzian_coframe_existence_under_declared_v4_inputs"
        ]
        == "CLOSED_CONDITIONAL"
        and teleparallel["claim_tiers"][
            "flat_metric_compatible_teleparallel_connection_existence"
        ]
        == "CLOSED_CONSTRUCTED_FROM_GLOBAL_COFRAME"
        and teleparallel["claim_tiers"][
            "same_source_Q_WW_to_global_coframe_identification"
        ]
        == "REDUCED_TO_CAUCHY_SUPPORT_AND_OUTER_TANGENT_IDENTIFICATION_ONLY"
        and teleparallel["claim_tiers"][
            "QWW_transition_law_matches_spatial_tetrad_cocycle"
        ]
        == "CLOSED_EXACT"
        and teleparallel["claim_tiers"][
            "QWW_global_soldering_after_typed_identification"
        ]
        == "CLOSED_CONDITIONAL"
        and teleparallel["claim_tiers"][
            "QWW_inner_spatial_bundle_identification_after_invertibility"
        ]
        == "CLOSED_AUTOMATIC"
        and teleparallel["claim_tiers"]["global_Lorentzian_coframe_lift_from_MTT"]
        == "OPEN"
        and teleparallel["claim_tiers"]["MTT_selection_of_TEGR_constitutive_vector"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
        "teleparallel direct action exit was lost or overpromoted",
    )
    require(
        teleparallel["claim_tiers"]["local_orientation_invariance_of_G_equal_QTQ"]
        == "CLOSED_EXACT"
        and teleparallel["claim_tiers"][
            "metric_descent_selects_TEGR_constitutive_vector"
        ]
        == "CLOSED_UNIQUE_CONDITIONAL"
        and teleparallel["claim_tiers"][
            "independent_TEGR_constitutive_parameters_after_metric_descent"
        ]
        == "CLOSED_NONE"
        and teleparallel["claim_tiers"][
            "frame_neutrality_principal_symbol_selects_TEGR_vector"
        ]
        == "CLOSED_EXACT"
        and teleparallel["claim_tiers"][
            "TEGR_nonlinear_frame_neutrality_sufficiency_mod_boundary"
        ]
        == "CLOSED_EXACT"
        and teleparallel["claim_tiers"][
            "MTT_selection_of_metric_descent_and_no_extra_frame_modes"
        ]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY"
        and teleparallel["claim_tiers"][
            "MTT_identifies_teleparallel_representatives_as_neutrality_equivalent"
        ]
        == "OPEN",
        "metric-descent TEGR selection reduction changed",
    )
    require(
        teleparallel["claim_tiers"]["local_QWW_to_ADM_coframe_map"]
        == "CLOSED_EXACT_UNDER_TYPED_BUNDLE_IDENTIFICATION"
        and teleparallel["claim_tiers"]["ADM_metric_and_volume_from_QWW"]
        == "CLOSED_EXACT"
        and teleparallel["claim_tiers"]["lapse_shift_as_fit_parameters"]
        == "CLOSED_NONE_CONSTRAINT_FIELDS",
        "local QWW/ADM coframe theorem changed",
    )

    strict_source_tegr = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "strict_same_source_teleparallel_selection_certificate.json"
        )
    )
    require(
        strict_source_tegr["claim_tiers"][
            "selected_candidate_source_factors_through_G_equal_QTQ"
        ]
        == "CLOSED_EXACT"
        and strict_source_tegr["claim_tiers"]["orientation_fiber_dimension"]
        == "CLOSED_EXACT_THREE"
        and strict_source_tegr["claim_tiers"][
            "selected_candidate_orientation_source_coordinates"
        ]
        == "CLOSED_ZERO",
        "strict same-source quotient theorem changed",
    )
    require(
        strict_source_tegr["claim_tiers"][
            "strict_same_source_two_derivative_teleparallel_action"
        ]
        == "CLOSED_UNIQUE_TEGR_RAY"
        and strict_source_tegr["claim_tiers"][
            "leading_two_derivative_classical_GR_on_candidate_branch"
        ]
        == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY"
        and strict_source_tegr["claim_tiers"]["canonical_pullback_metric_given_QWW"]
        == "CLOSED_EXACT_UNIQUE"
        and strict_source_tegr["claim_tiers"]["metric_observable_choice_given_QWW"]
        == "CLOSED_NO_REMAINING_CHOICE"
        and strict_source_tegr["claim_tiers"][
            "selected_branch_q79_Z64_QWW_source_realization"
        ]
        == "CLOSED_UNIQUE_UP_TO_GAUGE"
        and strict_source_tegr["claim_tiers"][
            "selected_branch_source_realization_fitted_parameters"
        ]
        == "CLOSED_ZERO"
        and strict_source_tegr["claim_tiers"][
            "primitive_MTT_selects_candidate_metric_source_realization"
        ]
        == "REDUCED_TO_PRIMITIVE_MINIMAL_ROOTSTACK_LORENTZIAN_BRANCH_SELECTION"
        and strict_source_tegr["claim_tiers"][
            "spectral_sheet_symbol_to_rootstack_strain_carrier"
        ]
        == "CLOSED_EXACT"
        and strict_source_tegr["claim_tiers"][
            "literal_full_inverse_Fourier_Mukai_HYM_connection_identity"
        ]
        == "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION"
        and strict_source_tegr["claim_tiers"]["dynamic_projected_HYM_TT_Hessian"]
        == "OPEN_ACTUAL_OPERATOR_CONDITIONAL_SCALAR_FORM_CLOSED"
        and strict_source_tegr["claim_tiers"][
            "physical_HYM_TT_block_scalarization"
        ]
        == "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE"
        and strict_source_tegr["claim_tiers"][
            "typed_lane_quarterturn_to_FuYau_source_functor"
        ]
        == "CLOSED_CONDITIONAL_AT_FLAT_SYMBOL_AND_FUYAU_PARENT_REPRESENTATION_TIER_ACTUAL_HYM_EXTENSION_OPEN"
        and strict_source_tegr["claim_tiers"][
            "free_C4_orbit_covariance_scalarizes_branch_Hessian"
        ]
        == "CLOSED_NO_GO"
        and strict_source_tegr["claim_tiers"][
            "square_theta_direct_adjoint_realizes_JDE"
        ]
        == "CLOSED_NO_GO"
        and strict_source_tegr["claim_tiers"][
            "nontrivial_inverse_Fourier_Mukai_induced_JDE"
        ]
        == "OPEN_EXTENSION_FROM_FLAT_SYMBOL_TO_ACTUAL_HYM"
        and strict_source_tegr["claim_tiers"][
            "shared_root_C4_to_flat_rootstack_strain_JDE_functor"
        ]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and strict_source_tegr["claim_tiers"][
            "direct_unital_Herm3_adjoint_realizes_full_JDE"
        ]
        == "CLOSED_NO_GO"
        and strict_source_tegr["claim_tiers"][
            "ordinary_dual_and_exterior_square_preserve_HYM"
        ]
        == "CLOSED_EXACT_ON_TRACEFREE_SU3_SECTOR"
        and strict_source_tegr["claim_tiers"][
            "ordinary_dual_or_exterior_square_realizes_JDE"
        ]
        == "CLOSED_NO_GO"
        and strict_source_tegr["claim_tiers"][
            "nonzero_c3_chiral_branch_complex_linear_self_duality"
        ]
        == "CLOSED_NO_GO"
        and strict_source_tegr["claim_tiers"][
            "nonlocal_same_branch_Fourier_Mukai_kernel_contract"
        ]
        == "OPEN_11_ROWS_2_TOPOLOGICAL_ROWS_AVAILABLE"
        and strict_source_tegr["claim_tiers"][
            "marked_shared_circle_C4_autonomous_descent"
        ]
        == "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING"
        and strict_source_tegr["claim_tiers"][
            "unmarked_modular_parent_descent_contract"
        ]
        == "OPEN_5_ROWS_0_AVAILABLE",
        "strict same-source candidate action was lost or overpromoted",
    )
    require(
        ledger["research_gates"]["closure_potential_alone_as_gr_kinetic_source"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["coframe_torsion_as_literal_nonclosure_source"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["tegr_einstein_hilbert_boundary_identity"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["direct_two_derivative_spacetime_action_exit"]
        == "CLOSED_AT_DECLARED_FINITE_SOURCE_IR_TIER_AFTER_A_QG_PRIMITIVE_DERIVATION_AND_VALUES_OPEN",
        "ledger lost the teleparallel direct-action advance",
    )
    require(
        ledger["research_gates"][
            "global_lorentzian_coframe_existence_under_declared_v4_inputs"
        ]
        == "CLOSED_CONDITIONAL"
        and ledger["research_gates"][
            "flat_teleparallel_connection_existence_from_global_coframe"
        ]
        == "CLOSED_CONSTRUCTED"
        and ledger["research_gates"]["local_qww_to_adm_coframe_map"]
        == "CLOSED_EXACT_UNDER_TYPED_BUNDLE_IDENTIFICATION"
        and ledger["research_gates"]["adm_metric_and_volume_from_qww"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["lapse_shift_as_fit_parameters"]
        == "CLOSED_NONE_CONSTRAINT_FIELDS"
        and ledger["research_gates"][
            "qww_transition_law_matches_spatial_tetrad_cocycle"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "qww_global_soldering_after_typed_identification"
        ]
        == "CLOSED_CONDITIONAL"
        and ledger["research_gates"][
            "qww_inner_spatial_bundle_identification_after_invertibility"
        ]
        == "CLOSED_AUTOMATIC"
        and ledger["research_gates"]["same_source_qww_to_global_coframe_identification"]
        == "REDUCED_TO_CAUCHY_SUPPORT_AND_OUTER_TANGENT_IDENTIFICATION_ONLY",
        "ledger lost the conditional coframe/connection existence theorem",
    )
    require(
        ledger["research_gates"]["local_orientation_invariance_of_g_equal_qtq"]
        == "CLOSED_EXACT"
        and ledger["research_gates"]["metric_descent_selects_tegr_constitutive_vector"]
        == "CLOSED_UNIQUE_CONDITIONAL"
        and ledger["research_gates"][
            "independent_tegr_constitutive_parameters_after_metric_descent"
        ]
        == "CLOSED_NONE"
        and ledger["research_gates"][
            "frame_neutrality_principal_symbol_selects_tegr_vector"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "tegr_nonlinear_frame_neutrality_sufficiency_mod_boundary"
        ]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "mtt_selection_of_metric_descent_and_no_extra_frame_modes"
        ]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY"
        and ledger["research_gates"][
            "mtt_identifies_teleparallel_representatives_as_neutrality_equivalent"
        ]
        == "OPEN"
        and ledger["research_gates"]["mtt_selection_of_tegr_constitutive_vector"]
        == "REDUCED_TO_TELEPARALLEL_REPRESENTATIVE_NEUTRALITY",
        "ledger lost the metric-descent TEGR selection reduction",
    )
    require(
        ledger["research_gates"]["strict_same_source_candidate_source_factorization"]
        == "CLOSED_EXACT"
        and ledger["research_gates"][
            "strict_same_source_candidate_orientation_fiber_neutrality"
        ]
        == "CLOSED_CHARACTERIZATION"
        and ledger["research_gates"]["strict_same_source_candidate_tegr_action_form"]
        == "CLOSED_UNIQUE_AT_TWO_DERIVATIVE_IR_ORDER"
        and ledger["research_gates"]["strict_same_source_candidate_classical_gr"]
        == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY"
        and ledger["research_gates"]["canonical_qww_pullback_metric"]
        == "CLOSED_EXACT_UNIQUE"
        and ledger["research_gates"]["metric_observable_choice_given_qww"]
        == "CLOSED_NO_REMAINING_CHOICE"
        and ledger["research_gates"][
            "primitive_mtt_selection_of_current_metric_source_realization"
        ]
        == "CLOSED_NODERIVABILITY_FROM_CURRENT_ABSTRACT_CORPUS_ONE_DISCRETE_AXIOM_COMPLETION_AVAILABLE",
        "ledger lost strict same-source candidate closure",
    )

    nonlinear_nogo = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "quadratic_tt_nonlinear_action_nogo_certificate.json"
        )
    )
    require(
        nonlinear_nogo["claim_tiers"][
            "quadratic_TT_data_select_unique_nonlinear_action"
        ]
        == "CLOSED_NO_GO"
        and nonlinear_nogo["claim_tiers"][
            "two_derivative_IR_clause_is_logically_indispensable"
        ]
        == "CLOSED",
        "quadratic-to-nonlinear action no-go changed",
    )
    require(
        nonlinear_nogo["claim_tiers"][
            "spectral_action_as_same_operator_SM_gravity_candidate"
        ]
        == "CLOSED_ARCHITECTURALLY"
        and nonlinear_nogo["claim_tiers"]["selected_MTT_product_spectral_action"]
        == "OPEN"
        and nonlinear_nogo["claim_tiers"][
            "selected_Einstein_IR_limit_of_spectral_action"
        ]
        == "OPEN",
        "spectral-action exit changed or was overpromoted",
    )

    spectral_ir = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "spectral_action_einstein_ir_limit_certificate.json"
        )
    )
    require(
        spectral_ir["claim_tiers"]["active_A49_Majorana_invariants"]
        == "CLOSED_ZERO_FOR_DIRAC_ONLY_BRANCH"
        and spectral_ir["claim_tiers"]["dimensionless_Einstein_Weyl_ratio"]
        == "CLOSED_CONDITIONAL_ON_A53_ONE_ATOM_TIER"
        and spectral_ir["claim_tiers"]["full_spectral_heat_kernel_remainder_bound"]
        == "OPEN"
        and spectral_ir["claim_tiers"]["bare_spectral_vacuum_small_or_cancelled"]
        == "CLOSED_NO",
        "spectral Einstein/Weyl IR calculation or its boundary changed",
    )
    require(
        ledger["research_gates"]["quadratic_tt_to_unique_nonlinear_action"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"][
            "spectral_action_same_operator_sm_gravity_architecture"
        ]
        == "CLOSED_ARCHITECTURALLY"
        and ledger["research_gates"]["selected_product_spectral_action"] == "OPEN"
        and ledger["research_gates"][
            "selected_einstein_ir_limit_of_spectral_action"
        ]
        == "PARTIAL_A4_RATIO_CLOSED_FULL_REMAINDER_OPEN"
        and ledger["research_gates"]["spectral_a4_dimensionless_einstein_weyl_ratio"]
        == "CLOSED_CONDITIONAL_ON_A53_ONE_ATOM_TIER"
        and ledger["research_gates"]["spectral_full_heat_kernel_remainder_bound"]
        == "OPEN"
        and ledger["research_gates"]["bare_spectral_vacuum_small_or_cancelled"]
        == "CLOSED_NO",
        "ledger lost the two honest action exits",
    )

    massless_gap = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "massless_tt_pole_internal_gap_no_go_certificate.json"
        )
    )
    require(
        massless_gap["claim_tiers"]["pure_lambda15_carrier_as_massless_graviton"]
        == "CLOSED_NO_GO"
        and massless_gap["numerics"]["metric_zero_value_exact"] == "4/15"
        and massless_gap["numerics"]["strain_zero_value_exact"] == "1/15",
        "massless-pole/internal-gap no-go changed",
    )
    require(
        ledger["research_gates"]["z64_lambda_15_as_physical_gr_qg_gap"]
        == "CLOSED_NO_GO_AS_SOLE_MASSLESS_POLE"
        and ledger["research_gates"]["coherent_zero_mode_massless_TT_source"]
        == "CLOSED_GEOMETRIC_UNIT_INTERNAL_RESIDUE",
        "ledger lost the massless zero-mode correction",
    )

    zero_mode = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "q79_coherent_zero_mode_tt_source_certificate.json"
        )
    )
    require(
        zero_mode["claim_tiers"]["geometric_coherent_zero_mode_TT_source_row"]
        == "CLOSED"
        and zero_mode["claim_tiers"]["canonical_internal_massless_residue"]
        == "CLOSED_UNIT",
        "q79 coherent zero-mode theorem changed",
    )
    require(
        zero_mode["claim_tiers"]["physical_kappa_h_or_Newton_normalization"]
        == "OPEN"
        and ledger["research_gates"]["selected_action_zero_mode_lambda15_fusion"]
        == "OPEN",
        "zero-mode metrology/action boundary was lost",
    )

    spectral_no_go = json.loads(
        read(
            GR_RESPONSE
            / "certificates"
            / "stieltjes_massless_gaussian_no_go_certificate.json"
        )
    )
    require(
        spectral_no_go["claim_tiers"]["three_way_incompatibility"] == "CLOSED"
        and spectral_no_go["claim_tiers"][
            "all_loop_UV_finiteness_with_positive_massless_spectrum"
        ]
        == "OPEN_NOT_PROVED",
        "Stieltjes/massless/Gaussian no-go changed",
    )
    require(
        ledger["research_gates"]["stieltjes_massless_permanent_gaussian_conjunction"]
        == "CLOSED_NO_GO"
        and ledger["research_gates"]["all_loop_finiteness_on_positive_massless_route"]
        == "OPEN_NOT_PROVED",
        "ledger lost the QG propagator no-go",
    )

    required_audit_phrases = [
        "does **not** prove a UV-finite, all-scale unitary quantum theory of",
        "Finite q79 projected TT operator",
        "h_DD=h_EE>0",
        "Interacting low-energy q79 quantum gravity",
        "D=2L+2",
        "Goroff-Sagnotti",
        "compatible UV route has now been selected",
        "q79 heterotic UV inheritance",
        "Mat_3(C)",
        "rank 74 and nullity seven",
        "smooth splitting-conic degree-two K3",
        "`delta=H-L`",
        "`9+11+4=24`",
        "local torsion anomaly matrix",
        "A = [[ 2,-2],[-2, 2]] = 2 delta delta^T",
        "M1=(1,-1),  N1=(4,-4),  k1^2=2",
        "locally free rank-12 Fermi",
        "has even `c2`",
        "pulled back from K3 has `c3=0`",
        "`c2=9u,c3=+/-6`",
        "topological incompatibility as a blocker",
        "worldsheet contract remains `5/12` available plus two partial",
        "all 90 continuous root tubes",
        "92-column integral `H2` presentation",
        "`8 x 92` period",
        "A177-A206 now close",
        "all 71 selected `E32` thimble intervals",
        "radius is `0.0004842494354306837`",
        "frozen height-four carrier is rejected",
        "seven tau-dependent characters",
        "Primitive branch cutset and minimal completion",
        "two-branch automorphism countermodel",
        "single discrete axiom `A_QG`",
        "zero continuous parameters",
        "not derived from upper MTT dynamics",
        "standard BRST/BV quantization is imported, not derived from MTT",
        "standard positive spectral form conflicts with exact Gaussian decay",
        "One damped line does not control all loop directions",
        "q79 coherent scalar zero-mode TT row",
        "Correct proof ladder from here",
        "Post-audit advance: the actual `DG` construction",
        "Post-audit advance: same-circle reduced to one Z2 lift",
        "executed A125/A126 selected-side interval",
        "`h(mu)=32`",
        "eighteen ordinary cusps",
        "det(J_flat)=(-Disc)^3",
        "root orders `2,3,2,1`",
        "selected-branch q79/Z64-to-Q_WW source map is closed",
        "Herm(V)=D direct-sum S direct-sum K",
        "normalized overlap closed exact",
        "p1(V_R)=-18",
        "literal full-connection identity closed no-go for nonzero Chern data",
        "H_std=[[h_DD,h_DE],[h_DE,h_EE]]",
        "q79 complement quarter-turn and HYM scalar form",
        "J_DE(d,e)=(-e,d)",
        "`J_DE` reduces the self-adjoint commutant dimension from six",
        "C4=<16>={0,16,32,48}",
        "Free-orbit covariance is therefore not one-branch invariance",
        "direct square-theta same-carrier attempt is also closed no-go",
        "Lambda^2 E_D=sign tensor E_D",
        "global and parallel on the minimal flat root-stack symbol",
        "This cannot be reduced to direct algebra conjugation",
        "autonomous Lens descent",
        "globalizes the constructed metric derivative as",
        "Delta_metric(0)=4/15 I",
        "Fierz-Pauli/linearized-Einstein operator",
        "coherent-zero-mode TT source row",
        "unit internal residue",
        "finite six-dimensional Hessian self-adjoint",
        "four-dimensional Lovelock classification",
        "stress map has no independent gravitational normalization",
        "exact scale no-go",
        "31.8 R1^3",
        "quadratic-to-nonlinear selection no-go",
        "Weyl-cubic deformation",
        "A51-A53 product spectral",
        "two honest action exits",
        "beta^2/Lambda^2 = 20/(3 tau_int)",
        "6/tau_int = 14.7425140497997",
        "exact closure-anholonomy construction",
        "T_TEGR=(1/4)I1+(1/2)I2-I3",
        "coframe anholonomy cost",
        "no separate topological coframe-existence blocker",
        "G=Q_WW^T Q_WW` is invariant under local orientation changes",
        "local `Q_WW` coframe map is now explicit",
        "spatial tetrad/solder cocycle",
        "`lambda(1/4,1/2,-1)`",
        "A non-TEGR frame kinetic term",
        "old metric-observable-choice gate is closed",
    ]
    for phrase in required_audit_phrases:
        require(phrase.lower() in audit.lower(), f"audit guard missing: {phrase}")

    print("AUDIT_PASS: seven QG papers and current research frontier are reconciled")
    print(f"AUDIT: {AUDIT}")
    print(f"LEDGER: {LEDGER}")


if __name__ == "__main__":
    main()
