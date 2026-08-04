"""Attempt to prove selected qutrit Fourier transport from MTT geometry.

The finite algebra already proves that a clock-polarized qutrit sector and a
shift-polarized qutrit sector are related by the normalized qutrit Fourier
matrix.  This script asks the stronger selected-source question:

    Do current MTT geometry certificates select the 10_M clock sector and the
    bar5_M shift sector, so that U_10=I_3 and U_bar5=F are selected data?

The answer must come from selected geometry, not from CKM or mass data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "selected_fourier_transport_proof_attempt.candidate.json"
CERT = CERTIFICATES / "selected_fourier_transport_proof_attempt_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"_missing": True, "_path": str(path.relative_to(ROOT))}
    return json.loads(path.read_text(encoding="utf-8"))


def cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def route_result(
    name: str,
    closes: bool,
    evidence: dict[str, Any],
    blocker: str,
    closing_input: str,
) -> dict[str, Any]:
    return {
        "route": name,
        "closes_selected_fourier_transport": closes,
        "evidence": evidence,
        "blocker": None if closes else blocker,
        "closing_input": None if closes else closing_input,
    }


def analyze() -> dict[str, Any]:
    qutrit = cert("qutrit_polarization_transport_lemma_certificate.json")
    su5_packet = cert("selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json")
    su5_attempt = load_json(CERTIFICATES / "selected_su5_qutrit_polarization_data.attempt.json")
    source_attempt = cert("selected_su5_source_proof_attempt_certificate.json")
    gerbe = cert("iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    projective = cert("iwasawa_projective_twist_source_hunt_certificate.json")
    twisted = cert("iwasawa_twisted_source_packet_fill_attempt_certificate.json")
    flat_torsion = cert("iwasawa_flat_torsion_selection_gap_certificate.json")
    torsion_selector = cert("iwasawa_torsion_label_four_route_selector_certificate.json")
    orientation = cert("iwasawa_orientation_de_dotd_bridge_certificate.json")
    block_sectors = cert("iwasawa_block_factorized_sector_maps_certificate.json")
    monad = cert("iwasawa_monad_map_data_gate_certificate.json")
    typed = cert("iwasawa_typed_monad_section_recovery_certificate.json")
    galerkin = cert("iwasawa_galerkin_zero_mode_slot_attempt_certificate.json")
    selected_de = cert("iwasawa_selected_de_construction_attempt_certificate.json")
    route_c = cert("iwasawa_route_c_branch_smoke_attempt_certificate.json")
    route_b_final = cert("route_b_final_missing_object_attempt_certificate.json")

    finite_core_proved = (
        get(qutrit, "calculation_results", "finite_transport_lemma_proved") is True
        and get(qutrit, "calculation_results", "F_dagger_Z_F_equals_X") is True
        and get(qutrit, "calculation_results", "orientation_selects_F") is True
    )
    exact_object_computed = (
        get(route_b_final, "calculation_results", "Delta_t_symbolic")
        == ["1/sqrt(3)", "omega^2/sqrt(3)"]
        and get(route_b_final, "calculation_results", "route_b_packet_structurally_nonzero")
        is True
    )
    su5_fixture_valid = (
        get(su5_packet, "calculation_results", "validator_passes_finite_algebra") is True
        and get(su5_packet, "calculation_results", "validator_orientation") == "F"
    )
    su5_fixture_selected = (
        get(su5_packet, "calculation_results", "promotes_to_selected_heavy_link_input")
        is True
        and get(su5_attempt, "source", "selected_by_mtt") is True
    )

    routes = [
        route_result(
            "finite clock-shift transport",
            finite_core_proved,
            {
                "finite_transport_lemma_proved": get(
                    qutrit, "calculation_results", "finite_transport_lemma_proved"
                ),
                "F_dagger_Z_F_equals_X": get(qutrit, "calculation_results", "F_dagger_Z_F_equals_X"),
                "orientation_selects_F": get(qutrit, "calculation_results", "orientation_selects_F"),
            },
            "finite algebra would be missing",
            "prove qutrit polarization transport lemma",
        ),
        route_result(
            "strongest current SU5 polarization packet",
            su5_fixture_selected,
            {
                "validator_passes_finite_algebra": get(
                    su5_packet, "calculation_results", "validator_passes_finite_algebra"
                ),
                "candidate_role": get(su5_packet, "calculation_results", "candidate_role"),
                "source_selected_by_mtt": get(su5_attempt, "source", "selected_by_mtt"),
                "promotes_to_selected_heavy_link_input": get(
                    su5_packet, "calculation_results", "promotes_to_selected_heavy_link_input"
                ),
            },
            "packet is finite-valid but remains UNSELECTED_FIXTURE",
            "replace fixture source with selected monad/Cech, Galerkin, or gerbe/twisted-bundle source",
        ),
        route_result(
            "selected gerbe/twisted-bundle promotion",
            (
                get(gerbe, "verdict", "selection_remains_open") is False
                and get(twisted, "verdict", "promotion_packet_passes") is True
                and get(block_sectors, "calculation_results", "selected_source_ready") is True
            ),
            {
                "candidate_holonomy_map_closed": get(gerbe, "verdict", "candidate_holonomy_map_closed"),
                "gerbe_selection_remains_open": get(gerbe, "verdict", "selection_remains_open"),
                "twisted_promotion_packet_passes": get(twisted, "verdict", "promotion_packet_passes"),
                "sector_maps_selected_source_ready": get(
                    block_sectors, "calculation_results", "selected_source_ready"
                ),
                "selected_by_mtt_in_attempt_packet": get(su5_attempt, "source", "selected_by_mtt"),
            },
            "finite Z3 gerbe map is closed, but selected gerbe representative and projector retention are not supplied",
            "selected Deligne/Cech or B-field period representative with Bianchi, Freed-Witten, projector retention, D_E, and dotD",
        ),
        route_result(
            "flat torsion orientation",
            (
                get(flat_torsion, "calculation_results", "selected_torsion_label_supplied_by_current_certificates")
                is True
                and get(torsion_selector, "calculation_results", "unique_label_selected_by_any_route")
                is True
                and get(orientation, "calculation_results", "unique_branch_selected_now") is True
            ),
            {
                "current_curvature_selection_can_choose_Z3_label": get(
                    flat_torsion, "calculation_results", "current_curvature_selection_can_choose_Z3_label"
                ),
                "common_candidate_labels": get(
                    torsion_selector, "calculation_results", "common_candidate_labels"
                ),
                "unique_branch_selected_now": get(
                    orientation, "calculation_results", "unique_branch_selected_now"
                ),
                "conditional_current_orientation_label": get(
                    torsion_selector, "calculation_results", "conditional_current_orientation_label"
                ),
            },
            "current data select the nontrivial pair m in {1,2}, not a unique selected m=1/q79 representative",
            "selected differential-cohomology torsion label or antiunitary-equivalence/retarded-branch selection proof",
        ),
        route_result(
            "typed monad/Cech zero modes",
            (
                get(monad, "consequence_for_sm_closure", "can_compute_H1_X_E_from_current_monad_data")
                is True
                and get(typed, "verdict", "closes_selected_H1_E_values") is True
            ),
            {
                "can_compute_H1_X_E_from_current_monad_data": get(
                    monad, "consequence_for_sm_closure", "can_compute_H1_X_E_from_current_monad_data"
                ),
                "closes_selected_H1_E_values": get(typed, "verdict", "closes_selected_H1_E_values"),
            },
            "typed monad/Cech sections, transition data, exactness, and selected H^1 representatives remain absent",
            "complete selected typed monad/Cech package deriving U_10,U_bar5",
        ),
        route_result(
            "spectral Galerkin / selected D_E",
            (
                get(galerkin, "verdict", "filled_selected_zero_mode_dotD_interface") is True
                or get(selected_de, "verdict", "selected_D_E_constructed") is True
            ),
            {
                "filled_selected_zero_mode_dotD_interface": get(
                    galerkin, "verdict", "filled_selected_zero_mode_dotD_interface"
                ),
                "selected_D_E_constructed": get(selected_de, "verdict", "selected_D_E_constructed"),
            },
            "operator pipeline is ready, but selected D_E/source data are absent",
            "selected D_E, Riesz projectors, zero-mode bases, sector projectors, and dotD response",
        ),
        route_result(
            "Route C residual solve",
            get(route_c, "calculation_results", "selected_origin_still_missing") is False,
            {
                "lifted_selected_flags_all_validators_pass": get(
                    route_c, "calculation_results", "lifted_selected_flags_all_validators_pass"
                ),
                "selected_origin_still_missing": get(
                    route_c, "calculation_results", "selected_origin_still_missing"
                ),
            },
            "finite validator chain passes only with lifted selected flags; honest selected origin is still missing",
            "genuine finite HYM/Strominger residual solve carrying the q79/F branch packet",
        ),
    ]

    selected_routes = [
        item["route"]
        for item in routes
        if item["route"] != "finite clock-shift transport"
        and item["closes_selected_fourier_transport"]
    ]
    selected_proof_closed = bool(selected_routes)

    correct_solution = {
        "name": "Selected Gerbe-Fourier Polarization Promotion",
        "statement": (
            "A passing selected twisted-source promotion packet whose finite "
            "holonomy is the nontrivial zeta3 Heisenberg cocycle, whose "
            "projector retains the dual clock/shift sectors, and whose SU(5) "
            "slot assignment maps 10_M to clock and bar5_M to shift promotes "
            "U_10=I_3, U_bar5=F as selected MTT geometry."
        ),
        "why_this_is_the_correct_solution": [
            "finite Stone-von-Neumann/qutrit algebra already makes F unique up to conjugation",
            "SU(5) exterior-square duality is monomial and cannot supply dense F",
            "q79 fixes the current orientation only after an orientation-carrying selected source exists",
            "the remaining missing datum is therefore selected source promotion, not another numerical fit",
        ],
        "minimal_packet_fields": [
            "selected_by_mtt=true for a Deligne/Cech gerbe, B-field table, typed monad/Cech packet, or spectral Galerkin source",
            "fixed differential-cohomology torsion label m=1 for q79 or antiunitary-equivalent conjugate proof",
            "map_to_central_cocycle_verified=true for the zeta3 finite Heisenberg cocycle",
            "Green-Schwarz Bianchi and Freed-Witten checks on the selected cycles",
            "twisted_projector_retains_sector=true and coherent_spectral_projector_verified=true",
            "common family frame, selected L2 metrics, U_10, U_bar5",
            "validator result: U_10^dagger U_bar5 = F modulo rephasing/permutation",
        ],
    }

    status = (
        "SELECTED_FOURIER_TRANSPORT_PROVED"
        if selected_proof_closed
        else "SELECTED_FOURIER_TRANSPORT_PROOF_REDUCED_SOURCE_PROMOTION_OPEN"
    )

    return {
        "candidate": "SelectedFourierTransportProofAttempt",
        "status": status,
        "generated_by": "scripts/attempt_selected_fourier_transport_proof.py",
        "proof_target": {
            "claim": "MTT geometry selects U_10=I_3 and U_bar5=F for the q79 SU(5) qutrit transport packet.",
            "forbidden_sources": [
                "observed CKM data",
                "observed masses",
                "Execution II benchmark flavor entries",
                "common Fourier gauge rotation",
                "SU(3) exterior-square monomial shortcut",
            ],
        },
        "calculation_results": {
            "finite_fourier_core_proved": finite_core_proved,
            "exact_route_b_object_computed": exact_object_computed,
            "strongest_su5_fixture_finite_valid": su5_fixture_valid,
            "strongest_su5_fixture_selected": su5_fixture_selected,
            "selected_source_routes_that_close_now": selected_routes,
            "selected_fourier_transport_proved_now": selected_proof_closed,
        },
        "route_evaluation": routes,
        "correct_solution": correct_solution,
        "what_this_proves": {
            "finite_F_transport_unique_up_to_conjugation": finite_core_proved,
            "conditional_route_b_object_is_exact": exact_object_computed,
            "current_selected_geometry_does_not_yet_promote_fixture": not selected_proof_closed,
            "correct_closing_packet_identified": True,
        },
        "still_open": {
            "selected_source_promotion_for_U10_Ubar5": not selected_proof_closed,
            "selected_gerbe_or_zero_mode_origin": not selected_proof_closed,
            "selected_projector_retention": not selected_proof_closed,
            "selected_D_E_dotD_if_C1_route": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_fourier_transport_without_selected_source": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "uses_common_fourier_gauge_as_physical_mixing": False,
            "uses_exterior_square_duality_as_fourier_transport": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "requested_proof_found_in_current_corpus": selected_proof_closed,
            "honest_answer": (
                "Not yet: current data prove the finite Fourier transport and the exact conditional Route B object, but not selected source promotion."
                if not selected_proof_closed
                else "Yes: a selected source route currently promotes the Fourier transport packet."
            ),
            "next_step": (
                "Fill the correct solution packet: selected gerbe/twisted-bundle or selected zero-mode source proving 10_M clock, bar5_M shift, and U_10^dagger U_bar5=F."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "SelectedFourierTransportProofAttempt",
        "status": report["status"],
        "purpose": "Attempt to prove selected U_10=I_3, U_bar5=F Fourier transport from MTT geometry.",
        "depends_on": [
            "qutrit_polarization_transport_lemma_certificate.json",
            "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
            "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json",
            "iwasawa_twisted_source_packet_fill_attempt_certificate.json",
            "iwasawa_torsion_label_four_route_selector_certificate.json",
            "iwasawa_orientation_de_dotd_bridge_certificate.json",
            "route_b_final_missing_object_attempt_certificate.json",
        ],
        "candidate_packet": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/attempt_selected_fourier_transport_proof.py",
        "calculation_results": report["calculation_results"],
        "correct_solution": report["correct_solution"],
        "what_this_proves": report["what_this_proves"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
