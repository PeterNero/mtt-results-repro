"""Attempt to prove the selected SU(5) qutrit source lemma.

The finite tensor step is already closed conditionally:

    selected clock/shift polarizations => T_u = I, T_d = F or F*

This script attacks the remaining proof obligation: can the current corpus
legally promote the conditional U_10/U_bar5 data to selected MTT data?  It
checks every currently available source route and writes a certificate with the
exact blocker if no route supplies a selected geometric source.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "selected_su5_source_proof_attempt.candidate.json"
CERT = CERTIFICATES / "selected_su5_source_proof_attempt_certificate.json"


def load_json(name: str) -> dict[str, Any]:
    path = CERTIFICATES / name
    if not path.exists():
        return {"_missing": True, "_path": str(path.relative_to(ROOT))}
    return json.loads(path.read_text(encoding="utf-8"))


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def route(
    *,
    name: str,
    status: str,
    closes: bool,
    evidence: list[str],
    blocker: str,
    next_input: str,
) -> dict[str, Any]:
    return {
        "route": name,
        "status": status,
        "closes_selected_source": closes,
        "evidence": evidence,
        "blocker": None if closes else blocker,
        "next_input": None if closes else next_input,
    }


def build_report() -> dict[str, Any]:
    projection = load_json("su5_projection_tensor_derivation_attempt_certificate.json")
    packet = load_json("selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json")
    monad_gate = load_json("iwasawa_monad_map_data_gate_certificate.json")
    typed_monad = load_json("iwasawa_typed_monad_section_recovery_certificate.json")
    galerkin = load_json("iwasawa_galerkin_zero_mode_slot_attempt_certificate.json")
    selected_de = load_json("iwasawa_selected_de_construction_attempt_certificate.json")
    route_c = load_json("iwasawa_route_c_branch_smoke_attempt_certificate.json")
    route_c_c1 = load_json("iwasawa_route_c_smoke_c1_dependency_certificate.json")
    gerbe = load_json("iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    flat_torsion = load_json("iwasawa_flat_torsion_selection_gap_certificate.json")
    torsion_selector = load_json("iwasawa_torsion_label_four_route_selector_certificate.json")
    orientation = load_json("iwasawa_orientation_de_dotd_bridge_certificate.json")
    block_twist = load_json("iwasawa_block_factorized_twisted_packet_candidate_certificate.json")
    block_sectors = load_json("iwasawa_block_factorized_sector_maps_certificate.json")
    missing = load_json("selected_missing_data_calculation_certificate.json")

    conditional_tensor_closed = (
        get(projection, "calculation_results", "finite_projection_tensor_derived") is True
        and get(projection, "calculation_results", "finite_validators_pass") is True
        and get(projection, "calculation_results", "both_conjugate_branches_derived") is True
    )
    selected_tensor_promoted = (
        get(projection, "calculation_results", "selected_polarization_source_promotes") is True
    )
    packet_selected = get(packet, "verdict", "selected_packet_constructed") is True

    routes = [
        route(
            name="conditional finite tensor",
            status=get(projection, "status", default="MISSING"),
            closes=selected_tensor_promoted,
            evidence=[
                "finite_projection_tensor_derived="
                + str(get(projection, "calculation_results", "finite_projection_tensor_derived")),
                "finite_validators_pass="
                + str(get(projection, "calculation_results", "finite_validators_pass")),
                "selected_polarization_source_promotes="
                + str(get(projection, "calculation_results", "selected_polarization_source_promotes")),
            ],
            blocker="finite tensor is derived only conditionally; source.selected_by_mtt remains false",
            next_input="selected U_10 and U_bar5 source data",
        ),
        route(
            name="selected SU5 packet fill",
            status=get(packet, "status", default="MISSING"),
            closes=packet_selected,
            evidence=[
                "validator_passes_finite_algebra="
                + str(get(packet, "calculation_results", "validator_passes_finite_algebra")),
                "candidate_role=" + str(get(packet, "calculation_results", "candidate_role")),
                "promotes_to_selected_heavy_link_input="
                + str(get(packet, "calculation_results", "promotes_to_selected_heavy_link_input")),
            ],
            blocker="strongest packet is an unselected fixture, not selected MTT data",
            next_input="selected gerbe/twisted-bundle source promotion or selected zero-mode packet",
        ),
        route(
            name="typed monad/Cech zero modes",
            status=get(typed_monad, "status", default="MISSING"),
            closes=(
                get(monad_gate, "consequence_for_sm_closure", "can_compute_H1_X_E_from_current_monad_data")
                is True
                and get(typed_monad, "verdict", "closes_selected_H1_E_values") is True
            ),
            evidence=[
                "can_compute_H1_X_E_from_current_monad_data="
                + str(
                    get(
                        monad_gate,
                        "consequence_for_sm_closure",
                        "can_compute_H1_X_E_from_current_monad_data",
                    )
                ),
                "closes_selected_H1_E_values="
                + str(get(typed_monad, "verdict", "closes_selected_H1_E_values")),
                "explicit_f_i_section_representatives_missing="
                + str(get(typed_monad, "not_recovered_from_corpus", "explicit_f_i_section_representatives")),
                "explicit_g_i_section_representatives_missing="
                + str(get(typed_monad, "not_recovered_from_corpus", "explicit_g_i_section_representatives")),
            ],
            blocker="typed f_i,g_i sections, transition/Cech maps, exactness, and H^1(X,E) representatives are absent",
            next_input="complete typed monad/Cech package with selected H^1(X,E), sector projections, metrics, Green data, and dotD",
        ),
        route(
            name="left-invariant Galerkin slot fill",
            status=get(galerkin, "status", default="MISSING"),
            closes=get(galerkin, "verdict", "filled_selected_zero_mode_dotD_interface") is True,
            evidence=[
                "filled_selected_zero_mode_dotD_interface="
                + str(get(galerkin, "verdict", "filled_selected_zero_mode_dotD_interface")),
                "computed_c1_primitive_contractions="
                + str(get(galerkin, "verdict", "computed_c1_primitive_contractions")),
            ],
            blocker="closed invariant data reproduce only the rank-one E33 seed and no sector U_10/U_bar5 split",
            next_input="sector projection maps, slot D_E/dotD operators, projectors, Green operators, and Higgs representative",
        ),
        route(
            name="selected D_E construction",
            status=get(selected_de, "status", default="MISSING"),
            closes=get(selected_de, "verdict", "selected_D_E_constructed") is True,
            evidence=[
                "selected_D_E_constructed="
                + str(get(selected_de, "verdict", "selected_D_E_constructed")),
                "diagnostic_pipeline_ready="
                + str(get(selected_de, "verdict", "diagnostic_pipeline_ready")),
                "first_blocking_layer="
                + str(get(missing, "computed_result", "first_blocking_layer")),
            ],
            blocker="the selected operator source is absent; the Hodge/Galerkin machinery is ready but unfed",
            next_input="one concrete selected D_E source: corrected non-invariant A^(0,1), typed monad/Cech data, or direct HYM/Strominger solve",
        ),
        route(
            name="Route C branch-aware finite solve",
            status=get(route_c, "status", default="MISSING"),
            closes=get(route_c, "calculation_results", "selected_origin_still_missing") is False,
            evidence=[
                "lifted_selected_flags_all_validators_pass="
                + str(get(route_c, "calculation_results", "lifted_selected_flags_all_validators_pass")),
                "selected_origin_still_missing="
                + str(get(route_c, "calculation_results", "selected_origin_still_missing")),
                "route_c_smoke_dotD_alone_closes_ckm_heavy_link="
                + str(get(route_c_c1, "calculation_results", "route_c_smoke_dotD_alone_closes_ckm_heavy_link")),
            ],
            blocker="small-N algebra passes only after artificial selected flags are lifted; honest packets fail selected-origin gates",
            next_input="genuine finite HYM/Strominger residual solve carrying the q79/F or q369/F* branch packet",
        ),
        route(
            name="projective gerbe/twisted bundle",
            status=get(gerbe, "status", default="MISSING"),
            closes=(
                get(gerbe, "verdict", "selection_remains_open") is False
                and get(block_twist, "calculation_results", "selected_source_promotion_ready") is True
                and get(block_sectors, "calculation_results", "selected_source_ready") is True
            ),
            evidence=[
                "candidate_holonomy_map_closed="
                + str(get(gerbe, "verdict", "candidate_holonomy_map_closed")),
                "selection_remains_open=" + str(get(gerbe, "verdict", "selection_remains_open")),
                "selected_source_promotion_ready="
                + str(get(block_twist, "calculation_results", "selected_source_promotion_ready")),
                "selected_source_ready="
                + str(get(block_sectors, "calculation_results", "selected_source_ready")),
            ],
            blocker="finite Z3 holonomy and block architecture are valid, but the selected gerbe representative and projector retention are not supplied",
            next_input="selected Deligne/Cech or B-field period representative with Bianchi, Freed-Witten, projector retention, D_E, and dotD",
        ),
        route(
            name="flat torsion and orientation selector",
            status=get(orientation, "status", default="MISSING"),
            closes=(
                get(flat_torsion, "calculation_results", "selected_torsion_label_supplied_by_current_certificates")
                is True
                and get(torsion_selector, "calculation_results", "unique_label_selected_by_any_route") is True
                and get(orientation, "calculation_results", "unique_branch_selected_now") is True
            ),
            evidence=[
                "current_curvature_selection_can_choose_Z3_label="
                + str(get(flat_torsion, "calculation_results", "current_curvature_selection_can_choose_Z3_label")),
                "common_candidate_labels="
                + str(get(torsion_selector, "calculation_results", "common_candidate_labels")),
                "unique_branch_selected_now="
                + str(get(orientation, "calculation_results", "unique_branch_selected_now")),
            ],
            blocker="all routes reduce to the nontrivial conjugate pair m in {1,2}; no selected orientation-carrying D_E/dotD package chooses q79 versus q369",
            next_input="fixed differential-cohomology torsion label or antiunitary-equivalence/retarded-branch selection proof",
        ),
    ]

    closed_routes = [item["route"] for item in routes if item["closes_selected_source"]]
    blocked_routes = [item["route"] for item in routes if not item["closes_selected_source"]]
    all_routes_blocked = len(closed_routes) == 0 and len(blocked_routes) == len(routes)

    return {
        "candidate": "SelectedSU5SourceProofAttempt",
        "status": (
            "SELECTED_SU5_SOURCE_PROOF_CLOSED"
            if not all_routes_blocked
            else "SELECTED_SU5_SOURCE_PROOF_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE"
        ),
        "generated_by": "scripts/attempt_selected_su5_source_proof.py",
        "proof_target": {
            "lemma": "MTT selects 10_M in clock polarization and bar5_M in shift polarization, giving selected U_10=I and U_bar5=F/F*.",
            "needed_for": [
                "promotion of the conditional SU(5) projection tensor",
                "selected C1 basis_connection heavy-link entry",
                "no-proxy CKM leading noncommutation branch",
            ],
        },
        "route_evaluation": routes,
        "calculation_results": {
            "conditional_projection_tensor_closed": conditional_tensor_closed,
            "conditional_q79_Td_equals_F": get(
                projection, "calculation_results", "q79_branch_Td_equals_F"
            )
            is True,
            "conditional_q369_Td_equals_F_conjugate": get(
                projection, "calculation_results", "q369_branch_Td_equals_F_conjugate"
            )
            is True,
            "selected_projection_tensor_promoted": selected_tensor_promoted,
            "selected_packet_constructed": packet_selected,
            "selected_D_E_constructed": get(selected_de, "verdict", "selected_D_E_constructed")
            is True,
            "typed_monad_route_closes": routes[2]["closes_selected_source"],
            "galerkin_route_closes": routes[3]["closes_selected_source"],
            "route_c_selected_origin_closes": routes[5]["closes_selected_source"],
            "gerbe_twisted_route_closes": routes[6]["closes_selected_source"],
            "flat_torsion_orientation_closes": routes[7]["closes_selected_source"],
            "closed_source_routes": closed_routes,
            "blocked_source_routes": blocked_routes,
            "all_current_source_routes_blocked": all_routes_blocked,
            "remaining_proof_closed_now": not all_routes_blocked,
        },
        "what_this_closes": {
            "finite_tensor_not_the_blocker": conditional_tensor_closed,
            "current_corpus_source_routes_exhausted_for_this_lemma": all_routes_blocked,
            "exact_remaining_source_obligation_identified": all_routes_blocked,
            "no_proxy_guardrails_preserved": True,
        },
        "still_open": {
            "selected_U10_Ubar5_source": all_routes_blocked,
            "selected_orientation_carrying_D_E_dotD": all_routes_blocked,
            "selected_gerbe_period_or_torsion_label": all_routes_blocked,
            "selected_C1_primitive_contractions": all_routes_blocked,
            "full_SM_closure": all_routes_blocked,
        },
        "minimal_closing_packet": {
            "one_of": [
                "typed monad/Cech data deriving selected U_10,U_bar5 from H^1(X,E)",
                "non-invariant spectral Galerkin packet with selected D_E, Riesz projectors, sector bases, and dotD",
                "selected gerbe/twisted-bundle packet proving projector retention and the qutrit sector polarization",
                "Route C residual solution whose selected_source flags are justified and whose branch packet selects q79/F or q369/F*",
            ],
            "must_include": [
                "selected source certificate, not a fixture flag",
                "common family frame and L2 metrics",
                "U_10 and U_bar5 unitary in those metrics",
                "10_M clock polarization and bar5_M shift polarization",
                "orientation F for q79 or F* for the conjugate branch",
                "no observed masses, CKM angles, or benchmark flavor entries as inputs",
            ],
        },
        "guardrails": {
            "claims_selected_U10_Ubar5": not all_routes_blocked,
            "claims_selected_D_E_constructed": False,
            "claims_selected_gerbe_representative": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "attempted_to_close_remaining_proof": True,
            "remaining_proof_closed": not all_routes_blocked,
            "mathematical_result": (
                "The conditional finite tensor is proved, but the current corpus does not prove the selected source lemma."
                if all_routes_blocked
                else "At least one current source route closes the selected source lemma."
            ),
            "first_missing_object": "selected orientation-carrying operator/source package deriving U_10 and U_bar5",
            "recommended_next_step": "Construct the minimal closing packet above, preferably through Route C or typed monad/Cech data, then rerun this proof attempt.",
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "SelectedSU5SourceProofAttemptCertificate",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "proof_target": report["proof_target"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "minimal_closing_packet": report["minimal_closing_packet"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write candidate and certificate")
    args = parser.parse_args()
    report = build_report()
    if args.write:
        write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
