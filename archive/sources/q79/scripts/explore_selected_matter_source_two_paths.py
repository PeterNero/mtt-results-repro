"""Explore the two honest routes to the selected matter-slot source.

The current finite theorem is conditional on selected transverse qutrit matter
slots.  This script compares the two remaining source routes:

  A. selected HYM/Strominger origin for the operator/source;
  B. selected spectral Galerkin zero-mode computation.

It deliberately records that neither route closes from the current data alone.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PATH = ROOT / "candidate_data" / "selected_matter_source_two_path_exploration.candidate.json"
CERTIFICATE_PATH = ROOT / "certificates" / "selected_matter_source_two_path_exploration_certificate.json"


def load_json(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def validator_passes(
    route_c: dict[str, Any],
    branch: str,
    mode: str,
    keys: list[str],
) -> dict[str, bool]:
    validators = (
        route_c.get("branches", {})
        .get(branch, {})
        .get("validators", {})
        .get(mode, {})
    )
    return {key: validators.get(key, {}).get("pass") is True for key in keys}


def all_values_true(values: dict[str, bool]) -> bool:
    return bool(values) and all(values.values())


def count_true(values: dict[str, bool]) -> int:
    return sum(1 for value in values.values() if value is True)


def make_exploration() -> dict[str, Any]:
    z7 = load_json("certificates/z7_fuyau_mukai_charge_sector_certificate.json")
    route_c = load_json("certificates/iwasawa_route_c_branch_smoke_attempt_certificate.json")
    galerkin_attempt = load_json("certificates/iwasawa_galerkin_zero_mode_slot_attempt_certificate.json")
    spectral_template = load_json("certificates/iwasawa_spectral_galerkin_data.template.json")
    source_attempt = load_json(
        "certificates/selected_matter_slot_transversality_source_attempt_certificate.json"
    )
    selected_gate = load_json(
        "certificates/selected_matter_slot_transversality_source_validator_certificate.json"
    )
    monad_gate = load_json("certificates/iwasawa_monad_map_data_gate_certificate.json")

    q79_honest = validator_passes(
        route_c,
        "current_q79_orientation",
        "honest_unselected",
        [
            "rhoE_mesh",
            "rhoE_metric",
            "sector_maps",
            "route_c_residual",
            "de_action",
            "riesz_gap",
            "reduced_green",
            "dotd_response",
        ],
    )
    q79_lifted = validator_passes(
        route_c,
        "current_q79_orientation",
        "lifted_selected_flags_smoke",
        [
            "rhoE_mesh",
            "rhoE_metric",
            "sector_maps",
            "route_c_residual",
            "de_action",
            "riesz_gap",
            "reduced_green",
            "dotd_response",
        ],
    )

    spectral_gates = spectral_template.get("success_gates", {})
    spectral_gate_bools = {
        key: value is True
        for key, value in spectral_gates.items()
        if isinstance(value, bool)
    }

    z7_closed = (
        z7.get("status") == "CLOSED_CHARGE_SECTOR"
        and z7.get("selection", {}).get("strominger_selection_applies") is True
        and z7.get("geometry", {}).get("green_schwarz_bianchi_identity_verified") is True
    )
    finite_if_not_blocker = (
        source_attempt.get("what_this_closes", {}).get("finite_I_F_matrices_not_the_blocker")
        is True
    )
    selected_gate_formulated = (
        selected_gate.get("status")
        == "SELECTED_MATTER_SLOT_TRANSVERSALITY_SOURCE_VALIDATOR_FORMULATED_SOURCE_OPEN"
    )
    galerkin_blocked_as_expected = (
        galerkin_attempt.get("status")
        == "IWASAWA_GALERKIN_SLOT_ATTEMPT_BLOCKED_BY_SECTOR_PROJECTION_AND_DOTD_DATA"
    )
    spectral_template_open = spectral_template.get("status") == "OPEN"
    monad_blocked = monad_gate.get("status") == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"

    path_a_gates = {
        "z7_fuyau_strominger_charge_sector_closed": z7_closed,
        "retarded_q79_branch_packet_available": bool(
            route_c.get("branches", {}).get("current_q79_orientation", {}).get("branch_packet")
        ),
        "route_c_mesh_metric_sector_honest_pass": all_values_true(
            {key: q79_honest[key] for key in ("rhoE_mesh", "rhoE_metric", "sector_maps")}
        ),
        "route_c_lifted_pipeline_algebra_passes": all_values_true(q79_lifted),
        "selected_matter_source_gate_formulated": selected_gate_formulated,
        "finite_I_F_transport_not_the_blocker": finite_if_not_blocker,
        "honest_route_c_selected_origin_passes": q79_honest.get("route_c_residual", False),
        "honest_selected_D_E_Riesz_Green_dotD_pass": all_values_true(
            {
                key: q79_honest[key]
                for key in ("de_action", "riesz_gap", "reduced_green", "dotd_response")
            }
        ),
    }
    path_b_gates = {
        "spectral_galerkin_template_exists": spectral_template_open,
        "left_invariant_rank_one_seed_attempt_completed": galerkin_blocked_as_expected,
        "typed_monad_route_checked_and_blocked": monad_blocked,
        "validator_stack_for_projector_green_dotD_exists": selected_gate_formulated,
        "selected_operator_constructed": spectral_gate_bools.get("selected_operator_constructed", False),
        "kernel_dimension_is_three": spectral_gate_bools.get("kernel_dimension_is_three", False),
        "complement_gap_positive": spectral_gate_bools.get("complement_gap_positive", False),
        "truncation_error_certified": spectral_gate_bools.get("truncation_error_certified", False),
        "sector_projection_maps_constructed": spectral_gate_bools.get(
            "sector_projection_maps_constructed", False
        ),
        "dotD_alpha1_and_Green_operator_constructed": spectral_gate_bools.get(
            "dotD_alpha1_and_Green_operator_constructed", False
        ),
    }

    path_a_closes = (
        path_a_gates["honest_route_c_selected_origin_passes"]
        and path_a_gates["honest_selected_D_E_Riesz_Green_dotD_pass"]
    )
    path_b_closes = (
        path_b_gates["selected_operator_constructed"]
        and path_b_gates["kernel_dimension_is_three"]
        and path_b_gates["complement_gap_positive"]
        and path_b_gates["truncation_error_certified"]
        and path_b_gates["sector_projection_maps_constructed"]
        and path_b_gates["dotD_alpha1_and_Green_operator_constructed"]
    )

    path_a = {
        "name": "Path A: selected HYM/Strominger source",
        "role": "justify selectedness of the operator/source and retarded branch",
        "status": "OPEN_SELECTED_STROMINGER_MATTER_SOURCE",
        "closes_selected_matter_source_now": path_a_closes,
        "gate_count": {
            "passed": count_true(path_a_gates),
            "total": len(path_a_gates),
        },
        "gates": path_a_gates,
        "current_strength": [
            "The Fu-Yau/Strominger charge sector is already closed for the q79 terminal branch.",
            "The q79/F branch-aware Route C finite files already carry mesh, metric, and sector data.",
            "The lifted selected-flag smoke packet shows the algebraic validator pipeline can pass.",
        ],
        "current_blocker": [
            "The Route C residual is smoke, not a selected HYM/Strominger solve.",
            "D_E, Riesz gap, reduced Green, and dotD fail honestly because selected source flags are absent.",
            "The closed Z7 charge sector does not by itself produce 10_M and bar5_M zero-mode bases.",
        ],
        "minimal_packet_to_close": [
            "selected background sector with Bianchi/HYM/Strominger residual certificate",
            "retarded q79/F branch attached to the same selected background",
            "selected finite D_E on Q,u,d,L,e,N,H slots",
            "selected dotD_alpha1 source on the same branch",
            "Riesz gap and reduced Green data with no lifted fixture flags",
            "projector retention from selected geometry into the qutrit family sector",
        ],
    }

    path_b = {
        "name": "Path B: spectral Galerkin zero-mode computation",
        "role": "compute the matter-slot bases, projectors, transport, and dotD response",
        "status": "OPEN_SELECTED_SPECTRAL_GALERKIN_ZERO_MODES",
        "closes_selected_matter_source_now": path_b_closes,
        "gate_count": {
            "passed": count_true(path_b_gates),
            "total": len(path_b_gates),
        },
        "gates": path_b_gates,
        "current_strength": [
            "The spectral Galerkin data template and Riesz/Green/dotD validators already exist.",
            "The left-invariant attempt proves the invariant seed is only rank one, so the need for sector-resolved/non-invariant data is explicit.",
            "This path is the most computationally concrete route to U_10, U_bar5, L2 metrics, and overlap responses.",
        ],
        "current_blocker": [
            "The selected operator D_E is not constructed.",
            "Kernel dimension, complement gap, and truncation bounds are not computed.",
            "Sector projection maps and dotD_alpha1/Green operators remain absent.",
        ],
        "minimal_packet_to_close": [
            "selected D_E imported from Path A or an equivalent selected monad/gerbe source",
            "non-invariant Galerkin basis with cutoff rule and orthonormalization",
            "low eigenpairs proving exactly three family zero modes and controlled anti-family modes",
            "Riesz projector, reduced Green operator, complement gap, and truncation error bound",
            "sector maps for 10_M, bar5_M, and Higgs slots",
            "U_10 and U_bar5 extracted in the selected L2 metrics",
        ],
    }

    candidate = {
        "calculation": "SelectedMatterSourceTwoPathExploration",
        "generated_by": "scripts/explore_selected_matter_source_two_paths.py",
        "paths": {
            "hym_strominger_source": path_a,
            "spectral_galerkin_zero_modes": path_b,
        },
        "coupling_between_paths": {
            "path_A_supplies": [
                "selected operator/source origin",
                "retarded q79/F branch on that selected source",
                "honest selected_source_verified flags for Route C validators",
            ],
            "path_B_supplies": [
                "family zero-mode basis",
                "selected L2 metrics",
                "Riesz projectors and reduced Green operator",
                "U_10/U_bar5 matter-slot transport and dotD response",
            ],
            "recommended_strategy": "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
            "why_not_either_alone": (
                "Path A currently selects a charge sector but not the matter-slot basis; "
                "Path B can compute the basis only after a selected operator/source is supplied."
            ),
        },
        "next_executable_steps": [
            "Create a selected HYM/Strominger residual packet replacing the Route C smoke residuals.",
            "Feed the resulting selected D_E into the spectral Galerkin data template.",
            "Compute eigenpairs, Riesz projector, reduced Green operator, and dotD response with certified gaps.",
            "Extract U_10/U_bar5 and rerun validate_selected_matter_slot_transversality_source.py.",
        ],
        "calculation_results": {
            "both_paths_explored": True,
            "path_A_closes_now": path_a_closes,
            "path_B_closes_now": path_b_closes,
            "neither_path_closes_alone_now": not path_a_closes and not path_b_closes,
            "hybrid_path_is_correct_next_target": True,
            "finite_I_F_transport_not_the_blocker": finite_if_not_blocker,
            "selected_matter_source_validator_ready": selected_gate_formulated,
        },
        "guardrails": {
            "claims_full_SM_closure": False,
            "claims_ordered_su5_packet_selected": False,
            "claims_selected_D_E_constructed": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "current_status": "BOTH_PATHS_OPEN_HYBRID_REQUIRED",
            "best_next_path": "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
            "reason": (
                "Use HYM/Strominger to justify selectedness, then spectral Galerkin "
                "to compute the zero-mode/matter-slot matrices."
            ),
            "remaining_first_blocker": "selected HYM/Strominger operator/source packet for D_E",
        },
    }

    return candidate


def write_outputs(candidate: dict[str, Any]) -> dict[str, Any]:
    CANDIDATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE_PATH.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    certificate = {
        "certificate": "SelectedMatterSourceTwoPathExplorationCertificate",
        "status": "SELECTED_MATTER_SOURCE_TWO_PATHS_EXPLORED_NEITHER_CLOSED",
        "analysis_script": "scripts/explore_selected_matter_source_two_paths.py",
        "candidate_data": "candidate_data/selected_matter_source_two_path_exploration.candidate.json",
        "calculation_results": candidate["calculation_results"],
        "path_status": {
            "hym_strominger_source": candidate["paths"]["hym_strominger_source"]["status"],
            "spectral_galerkin_zero_modes": candidate["paths"]["spectral_galerkin_zero_modes"]["status"],
        },
        "recommended_strategy": candidate["coupling_between_paths"]["recommended_strategy"],
        "guardrails": candidate["guardrails"],
        "verdict": candidate["verdict"],
    }
    CERTIFICATE_PATH.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return certificate


def main() -> int:
    candidate = make_exploration()
    certificate = write_outputs(candidate)
    print(
        json.dumps(
            {
                "candidate_data": str(CANDIDATE_PATH.relative_to(ROOT)).replace("\\", "/"),
                "certificate": str(CERTIFICATE_PATH.relative_to(ROOT)).replace("\\", "/"),
                "calculation_results": candidate["calculation_results"],
                "path_status": certificate["path_status"],
                "recommended_strategy": certificate["recommended_strategy"],
                "verdict": candidate["verdict"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
