"""Audit the dual Route A/Route B closure attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_dual_route_closure.py"
CANDIDATE = REPO / "candidate_data" / "dual_route_closure_attempt.candidate.json"
CERT = REPO / "certificates" / "dual_route_closure_attempt_certificate.json"
PAPER = ROOT / "Dual_Route_Closure_Attempt_v1.md"


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


def all_bool(data: dict[str, Any], expected: bool) -> bool:
    return all(value is expected for value in data.values())


def route_b_branch(report: dict[str, Any], name: str) -> dict[str, Any]:
    return (
        report.get("routes", {})
        .get("B_block_factorized_sector_resolved_C1", {})
        .get("branches", {})
        .get(name, {})
    )


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})
    route_a = report.get("routes", {}).get("A_high_scale_SU5_E6_multiplet_source", {})
    route_b = report.get("routes", {}).get("B_block_factorized_sector_resolved_C1", {})
    q79 = route_b_branch(report, "current_q79_orientation")
    q369 = route_b_branch(report, "conjugate_q369_orientation")

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "DualRouteClosureAttempt",
                    "DIFFERENCE_VARIABLES",
                    "rank_complex",
                    "A_high_scale_SU5_E6_multiplet_source",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "DUAL_ROUTE_ATTEMPT_REDUCED_ROUTE_B_TO_RANK_TWO_LINEAR_MAP_VALUES_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "Route A blocked",
            "PASS"
            if route_a.get("finite_tensor_available") is True
            and route_a.get("selected_source_closed") is False
            and route_a.get("block_packets_source_monolithic_tensor") is False
            and route_a.get("closes_now") is False
            else "FAIL",
            str(route_a),
        ),
        Gate(
            "Route B rank two",
            "PASS"
            if calc.get("route_B_sector_resolved_linear_map_rank_two") is True
            and calc.get("route_B_nonzero_delta_t_structurally_reachable") is True
            and route_b.get("selected_values_available") is False
            and route_b.get("closes_now") is False
            else "FAIL",
            str(route_b),
        ),
        Gate(
            "q79 linear map",
            "PASS"
            if q79.get("rank_over_complex") == 2
            and q79.get("nullity_over_complex") == 3
            and q79.get("same_coefficients_between_u_and_d") is True
            and q79.get("universal_equal_overlap_case_delta_t") == [0.0, 0.0]
            else "FAIL",
            str(q79),
        ),
        Gate(
            "q369 linear map",
            "PASS"
            if q369.get("rank_over_complex") == 2
            and q369.get("nullity_over_complex") == 3
            and q369.get("same_coefficients_between_u_and_d") is True
            and q369.get("universal_equal_overlap_case_delta_t") == [0.0, 0.0]
            else "FAIL",
            str(q369),
        ),
        Gate(
            "minimal variables",
            "PASS"
            if calc.get("minimal_route_B_difference_variables")
            == [
                "A_left_delta",
                "B_right_row1_delta",
                "B_right_row2_delta",
                "C_higgs_row1_delta",
                "C_higgs_row2_delta",
            ]
            else "FAIL",
            str(calc.get("minimal_route_B_difference_variables")),
        ),
        Gate(
            "candidate file matches run",
            "PASS"
            if candidate.get("calculation_results") == calc
            and cert_calc == calc
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "closed fields",
            "PASS"
            if cert.get("what_this_closes", {}).get(
                "route_B_structural_nonzero_CKM_heavy_link_possible"
            )
            is True
            and all_bool(
                {
                    key: value
                    for key, value in cert.get("what_this_closes", {}).items()
                    if key != "route_B_structural_nonzero_CKM_heavy_link_possible"
                },
                True,
            )
            else "FAIL",
            str(cert.get("what_this_closes")),
        ),
        Gate(
            "still open",
            "PASS" if all_bool(cert.get("still_open", {}), True) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "guardrails",
            "PASS" if all_bool(cert.get("guardrails", {}), False) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "Route A still has the same selected-source blocker",
                    "rank = 2",
                    "nullity = 3",
                    "five complex selected u-d overlap-difference slots",
                    "not predictions",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Dual route closure attempt audit")
    print("================================")
    print()
    print(f"route_A_closes={calc.get('route_A_high_scale_tensor_closes_now')}")
    print(f"route_B_rank_two={calc.get('route_B_sector_resolved_linear_map_rank_two')}")
    print(f"route_B_values_available={calc.get('route_B_selected_values_available')}")
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
