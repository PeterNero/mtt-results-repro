"""Audit the visible operator-source blocker resolution."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "resolve_visible_operator_source_blocker.py"
CANDIDATE = REPO / "candidate_data" / "visible_operator_source_blocker_resolution.candidate.json"
CERT = REPO / "certificates" / "visible_operator_source_blocker_resolution_certificate.json"
PAPER = ROOT / "Visible_Operator_Source_Blocker_Resolution_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_script() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    output = run_script()
    script_text = read(SCRIPT)
    paper = read(PAPER)
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)

    routes = candidate.get("route_evaluation", {})
    results = candidate.get("calculation_results", {})
    cut_set = candidate.get("irreducible_cut_set", {})
    solved = candidate.get("what_is_solved_once_and_for_all", {})
    guardrails = candidate.get("guardrails", {})
    verdict = candidate.get("verdict", {})

    required_routes = {
        "A_closed_fuyau_charge_sector",
        "B_typed_monad_cech_sections",
        "C_direct_route_c_finite_hym_solve",
        "D_bundle_fe_gluing_contract",
        "E_discrete_gerbe_projector_route",
        "F_spectral_galerkin_zero_modes",
        "G_external_template_import",
    }
    required_cut = {
        "selected_visible_sm_bundle_model",
        "matter_operator_source_constructed",
        "honest_route_c_residual_selected_source",
        "sector_selected_D_E_flags",
        "sector_selected_Riesz_Green_flags",
        "sector_selected_dotD_alpha1_flags",
    }

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "VisibleOperatorSourceBlockerResolution",
                    "IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED",
                    "A_closed_fuyau_charge_sector",
                    "G_external_template_import",
                    "minimal_new_data_that_would_close",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate written",
            "PASS"
            if candidate.get("calculation") == "VisibleOperatorSourceBlockerResolution"
            and output.get("candidate_data")
            == "candidate_data/visible_operator_source_blocker_resolution.candidate.json"
            else "FAIL",
            str(output.get("candidate_data")),
        ),
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "VISIBLE_OPERATOR_SOURCE_BLOCKER_IRREDUCIBLE_NEW_SOURCE_REQUIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "all routes checked",
            "PASS"
            if required_routes.issubset(routes)
            and all(routes[name].get("closes_operator_source") is False for name in required_routes)
            else "FAIL",
            str(routes.keys()),
        ),
        Gate(
            "charge route blocked",
            "PASS"
            if routes.get("A_closed_fuyau_charge_sector", {}).get("status")
            == "INSUFFICIENT_CHARGE_SECTOR_ONLY"
            and routes.get("A_closed_fuyau_charge_sector", {})
            .get("checked_fields", {})
            .get("fuyau_strominger_charge_sector_closed")
            is True
            and routes.get("A_closed_fuyau_charge_sector", {})
            .get("checked_fields", {})
            .get("selected_hym_operator_source_verified")
            is False
            else "FAIL",
            str(routes.get("A_closed_fuyau_charge_sector", {})),
        ),
        Gate(
            "monad route blocked",
            "PASS"
            if routes.get("B_typed_monad_cech_sections", {}).get("status")
            == "BLOCKED_TYPED_MAP_SECTIONS_MISSING"
            and routes.get("B_typed_monad_cech_sections", {})
            .get("checked_fields", {})
            .get("supports_net_chirality_three")
            is True
            and routes.get("B_typed_monad_cech_sections", {})
            .get("checked_fields", {})
            .get("can_compute_H1_X_E_from_current_monad_data")
            is False
            else "FAIL",
            str(routes.get("B_typed_monad_cech_sections", {})),
        ),
        Gate(
            "route c blocked",
            "PASS"
            if routes.get("C_direct_route_c_finite_hym_solve", {}).get("status")
            == "BLOCKED_SELECTED_RESIDUAL_AND_OPERATOR_FLAGS_MISSING"
            and routes.get("C_direct_route_c_finite_hym_solve", {})
            .get("checked_fields", {})
            .get("operator_pipeline_passes")
            is False
            else "FAIL",
            str(routes.get("C_direct_route_c_finite_hym_solve", {})),
        ),
        Gate(
            "gerbe and spectral blocked",
            "PASS"
            if routes.get("E_discrete_gerbe_projector_route", {}).get("status")
            == "CANDIDATE_HOLONOMY_MAP_CLOSED_SELECTION_OPEN"
            and routes.get("F_spectral_galerkin_zero_modes", {}).get("status")
            == "BLOCKED_SELECTED_OPERATOR_ABSENT"
            else "FAIL",
            str(
                (
                    routes.get("E_discrete_gerbe_projector_route", {}).get("status"),
                    routes.get("F_spectral_galerkin_zero_modes", {}).get("status"),
                )
            ),
        ),
        Gate(
            "external templates guarded",
            "PASS"
            if routes.get("G_external_template_import", {}).get("status")
            == "TEMPLATE_ONLY_NOT_MTT_SELECTED_IWASAWA_SOURCE"
            and len(routes.get("G_external_template_import", {}).get("references", [])) == 3
            else "FAIL",
            str(routes.get("G_external_template_import", {})),
        ),
        Gate(
            "cut set complete",
            "PASS"
            if required_cut.issubset(cut_set)
            and all(
                cut_set[name].get("currently_supplied") is False
                for name in required_cut
            )
            else "FAIL",
            str(cut_set),
        ),
        Gate(
            "calculation result",
            "PASS"
            if results.get("all_current_routes_checked") is True
            and results.get("all_current_routes_blocked") is True
            and results.get("blocker_resolved_by_existing_data") is False
            and results.get("first_blocking_layer") == "selected_operator_source"
            else "FAIL",
            str(results),
        ),
        Gate(
            "solved ambiguity",
            "PASS"
            if solved.get("charge_sector_closure_does_not_imply_visible_operator_source") is True
            and solved.get("route_c_smoke_cannot_be_promoted_silently") is True
            and solved.get("current_corpus_has_no_closing_selected_operator_source") is True
            and solved.get("first_required_new_object_identified")
            == "selected visible SM bundle/operator source"
            else "FAIL",
            str(solved),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("current_status")
            == "IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED"
            and "not solvable by recombining current closed certificates"
            in verdict.get("honest_resolution", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records resolution",
            "PASS"
            if contains_all(
                paper,
                [
                    "No, not from the current data",
                    "Irreducible Cut Set",
                    "charge-sector closure does not imply visible operator-source closure",
                    "IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible operator-source blocker resolution audit")
    print("================================================")
    print()
    print(f"routes_checked={len(routes)}")
    print(f"all_routes_blocked={results.get('all_current_routes_blocked')}")
    print(f"status={cert.get('status')}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
