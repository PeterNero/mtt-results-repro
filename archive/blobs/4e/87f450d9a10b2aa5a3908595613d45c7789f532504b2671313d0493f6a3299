"""Audit the two-path selected matter-source exploration."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "explore_selected_matter_source_two_paths.py"
CANDIDATE = REPO / "candidate_data" / "selected_matter_source_two_path_exploration.candidate.json"
CERTIFICATE = REPO / "certificates" / "selected_matter_source_two_path_exploration_certificate.json"
PAPER = ROOT / "Selected_Matter_Source_Two_Path_Exploration_v1.md"


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
    certificate = load_json(CERTIFICATE)

    results = candidate.get("calculation_results", {})
    guardrails = candidate.get("guardrails", {})
    verdict = candidate.get("verdict", {})
    coupling = candidate.get("coupling_between_paths", {})
    path_a = candidate.get("paths", {}).get("hym_strominger_source", {})
    path_b = candidate.get("paths", {}).get("spectral_galerkin_zero_modes", {})
    path_a_gates = path_a.get("gates", {})
    path_b_gates = path_b.get("gates", {})

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "Path A: selected HYM/Strominger source",
                    "Path B: spectral Galerkin zero-mode computation",
                    "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate written",
            "PASS"
            if candidate.get("calculation") == "SelectedMatterSourceTwoPathExploration"
            and output.get("candidate_data")
            == "candidate_data/selected_matter_source_two_path_exploration.candidate.json"
            else "FAIL",
            str(output.get("candidate_data")),
        ),
        Gate(
            "certificate status",
            "PASS"
            if certificate.get("status") == "SELECTED_MATTER_SOURCE_TWO_PATHS_EXPLORED_NEITHER_CLOSED"
            and certificate.get("recommended_strategy")
            == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES"
            else "FAIL",
            str((certificate.get("status"), certificate.get("recommended_strategy"))),
        ),
        Gate(
            "path A status",
            "PASS"
            if path_a.get("status") == "OPEN_SELECTED_STROMINGER_MATTER_SOURCE"
            and path_a.get("closes_selected_matter_source_now") is False
            and path_a_gates.get("z7_fuyau_strominger_charge_sector_closed") is True
            and path_a_gates.get("route_c_mesh_metric_sector_honest_pass") is True
            and path_a_gates.get("honest_route_c_selected_origin_passes") is False
            else "FAIL",
            str(path_a_gates),
        ),
        Gate(
            "path B status",
            "PASS"
            if path_b.get("status") == "OPEN_SELECTED_SPECTRAL_GALERKIN_ZERO_MODES"
            and path_b.get("closes_selected_matter_source_now") is False
            and path_b_gates.get("spectral_galerkin_template_exists") is True
            and path_b_gates.get("left_invariant_rank_one_seed_attempt_completed") is True
            and path_b_gates.get("selected_operator_constructed") is False
            else "FAIL",
            str(path_b_gates),
        ),
        Gate(
            "coupled strategy",
            "PASS"
            if coupling.get("recommended_strategy")
            == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES"
            and "Path A currently selects a charge sector" in coupling.get("why_not_either_alone", "")
            else "FAIL",
            str(coupling),
        ),
        Gate(
            "result guard",
            "PASS"
            if results.get("both_paths_explored") is True
            and results.get("path_A_closes_now") is False
            and results.get("path_B_closes_now") is False
            and results.get("neither_path_closes_alone_now") is True
            and results.get("hybrid_path_is_correct_next_target") is True
            else "FAIL",
            str(results),
        ),
        Gate(
            "scientific guardrails",
            "PASS"
            if guardrails.get("claims_full_SM_closure") is False
            and guardrails.get("claims_ordered_su5_packet_selected") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("uses_benchmark_flavor_entries") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("current_status") == "BOTH_PATHS_OPEN_HYBRID_REQUIRED"
            and verdict.get("best_next_path")
            == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES"
            and verdict.get("remaining_first_blocker")
            == "selected HYM/Strominger operator/source packet for D_E"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records both paths",
            "PASS"
            if contains_all(
                paper,
                [
                    "Path A: Selected HYM/Strominger Source",
                    "Path B: Spectral Galerkin Zero Modes",
                    "Neither path closes alone",
                    "selectedness first, spectral computation second",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected matter source two-path exploration audit")
    print("=================================================")
    print()
    print(f"path_A={path_a.get('status')} closes={path_a.get('closes_selected_matter_source_now')}")
    print(f"path_B={path_b.get('status')} closes={path_b.get('closes_selected_matter_source_now')}")
    print(f"strategy={coupling.get('recommended_strategy')}")
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
