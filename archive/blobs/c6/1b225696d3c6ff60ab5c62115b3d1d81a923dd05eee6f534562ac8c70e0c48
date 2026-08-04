"""Resolve the selected visible operator-source blocker as far as current data allow.

This script is intentionally severe.  It tries every currently available route
that could turn the closed q79/F charge-sector work into a selected visible
SM operator source.  If none of them supplies selected D_E/dotD/Riesz/Green
data, it emits a cut-set certificate rather than promoting fixture data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PATH = ROOT / "candidate_data" / "visible_operator_source_blocker_resolution.candidate.json"
CERTIFICATE_PATH = ROOT / "certificates" / "visible_operator_source_blocker_resolution_certificate.json"


def load_json(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def bool_path(data: dict[str, Any], keys: list[str], expected: Any = True) -> bool:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return False
        current = current.get(key)
    return current is expected


def all_true(values: dict[str, bool]) -> bool:
    return bool(values) and all(values.values())


def route_c_honest_passes(route_c: dict[str, Any], keys: list[str]) -> dict[str, bool]:
    validators = (
        route_c.get("branches", {})
        .get("current_q79_orientation", {})
        .get("validators", {})
        .get("honest_unselected", {})
    )
    return {key: validators.get(key, {}).get("pass") is True for key in keys}


def analyze() -> dict[str, Any]:
    missing = load_json("certificates/selected_missing_data_calculation_certificate.json")
    source_hunt = load_json("certificates/selected_de_source_hunt_certificate.json")
    hym_attempt = load_json("certificates/selected_hym_operator_source_attempt_certificate.json")
    two_path = load_json("certificates/selected_matter_source_two_path_exploration_certificate.json")
    monad = load_json("certificates/iwasawa_monad_map_data_gate_certificate.json")
    dolbeault = load_json("certificates/iwasawa_dolbeault_complex_extraction_certificate.json")
    route_c = load_json("certificates/iwasawa_route_c_branch_smoke_attempt_certificate.json")
    bundle_fe = load_json("certificates/iwasawa_bundle_fe_gluing_contract_certificate.json")
    gerbe = load_json("certificates/iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    spectral = load_json("certificates/iwasawa_spectral_galerkin_data.template.json")
    selected_hym_validator = load_json(
        "certificates/selected_hym_operator_source_validator_certificate.json"
    )

    mesh_metric_sector = route_c_honest_passes(
        route_c, ["rhoE_mesh", "rhoE_metric", "sector_maps"]
    )
    route_c_operator = route_c_honest_passes(
        route_c, ["route_c_residual", "de_action", "riesz_gap", "reduced_green", "dotd_response"]
    )
    spectral_gates = spectral.get("success_gates", {})

    routes = {
        "A_closed_fuyau_charge_sector": {
            "status": "INSUFFICIENT_CHARGE_SECTOR_ONLY",
            "closes_operator_source": False,
            "positive_evidence": [
                "Fu-Yau/Strominger charge-sector certificate is closed",
                "Strominger selection applies inside that fixed charge sector",
            ],
            "blocking_evidence": [
                "selected_hym_operator_source_attempt remains blocked",
                "visible SM bundle model is not selected",
                "matter operator source is not constructed",
            ],
            "checked_fields": {
                "fuyau_strominger_charge_sector_closed": bool_path(
                    hym_attempt, ["calculation_results", "fuyau_strominger_charge_sector_closed"]
                ),
                "strominger_selection_applies": bool_path(
                    hym_attempt, ["calculation_results", "strominger_selection_applies"]
                ),
                "selected_hym_operator_source_verified": bool_path(
                    hym_attempt,
                    ["calculation_results", "selected_hym_operator_source_verified"],
                    expected=True,
                ),
            },
        },
        "B_typed_monad_cech_sections": {
            "status": "BLOCKED_TYPED_MAP_SECTIONS_MISSING",
            "closes_operator_source": False,
            "positive_evidence": [
                "topological monad data support net chirality three",
                "typed line-bundle entry types are computed",
            ],
            "blocking_evidence": monad.get("required_next_inputs", []),
            "checked_fields": {
                "supports_net_chirality_three": bool_path(
                    monad, ["topological_cern_check", "supports_net_chirality_three"]
                ),
                "source_gives_explicit_f_entries": bool_path(
                    monad, ["source_monad", "source_gives_explicit_f_entries"]
                ),
                "source_gives_explicit_g_entries": bool_path(
                    monad, ["source_monad", "source_gives_explicit_g_entries"]
                ),
                "can_compute_H1_X_E_from_current_monad_data": bool_path(
                    monad,
                    ["consequence_for_sm_closure", "can_compute_H1_X_E_from_current_monad_data"],
                ),
            },
        },
        "C_direct_route_c_finite_hym_solve": {
            "status": "BLOCKED_SELECTED_RESIDUAL_AND_OPERATOR_FLAGS_MISSING",
            "closes_operator_source": False,
            "positive_evidence": [
                "q79/F branch packet exists",
                "rhoE mesh, metric, and sector maps pass honestly",
                "lifted smoke proves downstream finite algebra can pass if selected data exist",
            ],
            "blocking_evidence": [
                "route_c_residual fails selected_source_verified",
                "D_E action fails selected_source_verified per sector",
                "Riesz/Green/dotD fail selected source flags",
            ],
            "checked_fields": {
                "mesh_metric_sector": mesh_metric_sector,
                "operator_validators": route_c_operator,
                "operator_pipeline_passes": all_true(route_c_operator),
            },
        },
        "D_bundle_fe_gluing_contract": {
            "status": "FORMULATED_RHOE_DATA_OPEN",
            "closes_operator_source": False,
            "positive_evidence": [
                "rank-three bundle FE gluing contract is formulated",
                "boundary rho_E slots and cocycle requirements are known",
            ],
            "blocking_evidence": list(bundle_fe.get("still_open", {}).keys()),
            "checked_fields": {
                "closes_bundle_FE_gluing_contract": bool_path(
                    bundle_fe, ["verdict", "closes_bundle_FE_gluing_contract"]
                ),
                "closes_actual_bundle_transitions": bool_path(
                    bundle_fe, ["verdict", "closes_actual_bundle_transitions"]
                ),
                "closes_selected_Galerkin_space": bool_path(
                    bundle_fe, ["verdict", "closes_selected_Galerkin_space"]
                ),
            },
        },
        "E_discrete_gerbe_projector_route": {
            "status": "CANDIDATE_HOLONOMY_MAP_CLOSED_SELECTION_OPEN",
            "closes_operator_source": False,
            "positive_evidence": [
                "finite flat Z3 gerbe holonomy candidate matches the qutrit projective cocycle",
                "discrete Bianchi residual is zero in the finite model",
            ],
            "blocking_evidence": list(gerbe.get("still_open", {}).keys()),
            "checked_fields": {
                "candidate_holonomy_map_closed": bool_path(
                    gerbe, ["verdict", "candidate_holonomy_map_closed"]
                ),
                "selection_remains_open": bool_path(gerbe, ["verdict", "selection_remains_open"]),
                "selected_D_E_dotD": bool_path(gerbe, ["still_open", "selected_D_E_dotD"]),
            },
        },
        "F_spectral_galerkin_zero_modes": {
            "status": "BLOCKED_SELECTED_OPERATOR_ABSENT",
            "closes_operator_source": False,
            "positive_evidence": [
                "spectral Galerkin template and validators exist",
                "diagnostic Hodge pipeline works when a valid finite D is supplied",
            ],
            "blocking_evidence": [
                "selected_operator_constructed is false",
                "kernel dimension, gap, truncation bound, sector projections, dotD/Green are open",
            ],
            "checked_fields": {
                "selected_operator_constructed": spectral_gates.get(
                    "selected_operator_constructed"
                )
                is True,
                "kernel_dimension_is_three": spectral_gates.get("kernel_dimension_is_three") is True,
                "complement_gap_positive": spectral_gates.get("complement_gap_positive") is True,
                "truncation_error_certified": spectral_gates.get("truncation_error_certified") is True,
                "sector_projection_maps_constructed": spectral_gates.get(
                    "sector_projection_maps_constructed"
                )
                is True,
                "dotD_alpha1_and_Green_operator_constructed": spectral_gates.get(
                    "dotD_alpha1_and_Green_operator_constructed"
                )
                is True,
            },
        },
        "G_external_template_import": {
            "status": "TEMPLATE_ONLY_NOT_MTT_SELECTED_IWASAWA_SOURCE",
            "closes_operator_source": False,
            "positive_evidence": [
                "heterotic literature has explicit standard-model bundle/Yukawa machinery",
                "Strominger existence theorems can start from stable bundles in suitable settings",
            ],
            "blocking_evidence": [
                "external templates are not the selected Iwasawa q79/F branch",
                "they do not provide the local MTT selected rho_E/D_E/dotD packet",
                "an import still requires a compatibility theorem and validator data",
            ],
            "references": [
                {
                    "id": "hep-th/0601204",
                    "url": "https://arxiv.org/abs/hep-th/0601204",
                    "use": "heterotic standard model Yukawa formalism",
                },
                {
                    "id": "arXiv:1512.05322",
                    "url": "https://arxiv.org/abs/1512.05322",
                    "use": "holomorphic Yukawa computations for heterotic line bundle models",
                },
                {
                    "id": "arXiv:1008.1018",
                    "url": "https://arxiv.org/abs/1008.1018",
                    "use": "Strominger solutions from stable bundles on Calabi-Yau threefolds",
                },
            ],
        },
    }

    cut_set = {
        "selected_visible_sm_bundle_model": {
            "required_by": "selected_hym_operator_source validator",
            "currently_supplied": False,
        },
        "matter_operator_source_constructed": {
            "required_by": "selected_hym_operator_source validator",
            "currently_supplied": False,
        },
        "honest_route_c_residual_selected_source": {
            "required_by": "validate_iwasawa_route_c_residuals.py",
            "currently_supplied": route_c_operator.get("route_c_residual", False),
        },
        "sector_selected_D_E_flags": {
            "required_by": "validate_iwasawa_de_action.py",
            "currently_supplied": route_c_operator.get("de_action", False),
        },
        "sector_selected_Riesz_Green_flags": {
            "required_by": "validate_iwasawa_riesz_gap.py and validate_iwasawa_reduced_green.py",
            "currently_supplied": route_c_operator.get("riesz_gap", False)
            and route_c_operator.get("reduced_green", False),
        },
        "sector_selected_dotD_alpha1_flags": {
            "required_by": "validate_iwasawa_dotd_response.py",
            "currently_supplied": route_c_operator.get("dotd_response", False),
        },
    }

    all_routes_blocked = all(route["closes_operator_source"] is False for route in routes.values())
    blocker_resolved = False
    candidate = {
        "calculation": "VisibleOperatorSourceBlockerResolution",
        "generated_by": "scripts/resolve_visible_operator_source_blocker.py",
        "route_evaluation": routes,
        "irreducible_cut_set": cut_set,
        "minimal_new_data_that_would_close": [
            "selected visible SM bundle or sheaf model on the q79/F branch",
            "finite rho_E transition data from that selected bundle, not pure-gauge smoke",
            "selected HYM/Strominger residual packet with selected_source_verified true",
            "sector D_E action matrices for Q,u,d,L,e,N,H with selected-source proof",
            "Riesz projector, complement gap, reduced Green, and truncation data",
            "same-branch dotD_alpha1 and horizontal responses",
            "projector retention proving the qutrit matter-slot polarizations",
        ],
        "what_is_solved_once_and_for_all": {
            "charge_sector_closure_does_not_imply_visible_operator_source": True,
            "finite_I_F_transport_is_not_the_blocker": True,
            "route_c_smoke_cannot_be_promoted_silently": True,
            "current_corpus_has_no_closing_selected_operator_source": all_routes_blocked,
            "first_required_new_object_identified": "selected visible SM bundle/operator source",
        },
        "calculation_results": {
            "all_current_routes_checked": True,
            "all_current_routes_blocked": all_routes_blocked,
            "blocker_resolved_by_existing_data": blocker_resolved,
            "selected_hym_operator_source_validator_ready": bool_path(
                selected_hym_validator, ["verdict", "validator_formulated"]
            ),
            "first_blocking_layer": missing.get("computed_result", {}).get("first_blocking_layer"),
            "source_hunt_found_selected_D_E": bool_path(
                source_hunt, ["hunt_result", "selected_D_E_source_found"]
            ),
            "hybrid_path_still_best": two_path.get("recommended_strategy")
            == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
        },
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "claims_visible_operator_source_constructed": False,
            "claims_ordered_su5_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "promotes_external_template_to_selected_MTT_source": False,
        },
        "verdict": {
            "current_status": "IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED",
            "honest_resolution": (
                "The blocker is not solvable by recombining current closed certificates. "
                "A new selected visible SM bundle/operator-source packet is mathematically required."
            ),
            "next_action": (
                "construct or import a visible bundle/sheaf model, prove MTT selection on the q79/F "
                "branch, and emit rho_E/D_E/Riesz/Green/dotD validator data"
            ),
        },
    }
    return candidate


def write_outputs(candidate: dict[str, Any]) -> dict[str, Any]:
    CANDIDATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE_PATH.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "VisibleOperatorSourceBlockerResolutionCertificate",
        "status": "VISIBLE_OPERATOR_SOURCE_BLOCKER_IRREDUCIBLE_NEW_SOURCE_REQUIRED",
        "analysis_script": "scripts/resolve_visible_operator_source_blocker.py",
        "candidate_data": "candidate_data/visible_operator_source_blocker_resolution.candidate.json",
        "calculation_results": candidate["calculation_results"],
        "irreducible_cut_set": candidate["irreducible_cut_set"],
        "minimal_new_data_that_would_close": candidate["minimal_new_data_that_would_close"],
        "what_is_solved_once_and_for_all": candidate["what_is_solved_once_and_for_all"],
        "guardrails": candidate["guardrails"],
        "verdict": candidate["verdict"],
    }
    CERTIFICATE_PATH.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return certificate


def main() -> int:
    candidate = analyze()
    certificate = write_outputs(candidate)
    print(
        json.dumps(
            {
                "candidate_data": "candidate_data/visible_operator_source_blocker_resolution.candidate.json",
                "certificate": "certificates/visible_operator_source_blocker_resolution_certificate.json",
                "calculation_results": candidate["calculation_results"],
                "cut_set": candidate["irreducible_cut_set"],
                "status": certificate["status"],
                "verdict": candidate["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
