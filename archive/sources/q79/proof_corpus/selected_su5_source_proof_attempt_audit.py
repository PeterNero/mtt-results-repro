"""Audit the selected SU(5) source proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_selected_su5_source_proof.py"
CANDIDATE = REPO / "candidate_data" / "selected_su5_source_proof_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_su5_source_proof_attempt_certificate.json"
PAPER = ROOT / "Selected_SU5_Source_Proof_Attempt_v1.md"


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


def route_by_name(report: dict[str, Any], name: str) -> dict[str, Any]:
    for item in report.get("route_evaluation", []):
        if item.get("route") == name:
            return item
    return {}


def all_guardrails_false(data: dict[str, Any]) -> bool:
    return all(value is False for value in data.get("guardrails", {}).values())


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})
    routes = report.get("route_evaluation", [])

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "SelectedSU5SourceProofAttempt",
                    "selected_D_E_constructed",
                    "all_current_source_routes_blocked",
                    "minimal_closing_packet",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "SELECTED_SU5_SOURCE_PROOF_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "finite tensor closed",
            "PASS"
            if calc.get("conditional_projection_tensor_closed") is True
            and calc.get("conditional_q79_Td_equals_F") is True
            and calc.get("conditional_q369_Td_equals_F_conjugate") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "selection not promoted",
            "PASS"
            if calc.get("selected_projection_tensor_promoted") is False
            and calc.get("selected_packet_constructed") is False
            and calc.get("remaining_proof_closed_now") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "routes all blocked",
            "PASS"
            if len(routes) == 8
            and calc.get("all_current_source_routes_blocked") is True
            and calc.get("closed_source_routes") == []
            and len(calc.get("blocked_source_routes", [])) == 8
            and all(item.get("closes_selected_source") is False for item in routes)
            else "FAIL",
            str(calc.get("blocked_source_routes")),
        ),
        Gate(
            "monad route blocked correctly",
            "PASS"
            if route_by_name(report, "typed monad/Cech zero modes").get("closes_selected_source")
            is False
            and "typed f_i,g_i" in route_by_name(report, "typed monad/Cech zero modes").get(
                "blocker", ""
            )
            else "FAIL",
            str(route_by_name(report, "typed monad/Cech zero modes")),
        ),
        Gate(
            "Route C source gate blocked",
            "PASS"
            if route_by_name(report, "Route C branch-aware finite solve").get(
                "closes_selected_source"
            )
            is False
            and "artificial selected flags" in route_by_name(
                report, "Route C branch-aware finite solve"
            ).get("blocker", "")
            else "FAIL",
            str(route_by_name(report, "Route C branch-aware finite solve")),
        ),
        Gate(
            "gerbe route source gate blocked",
            "PASS"
            if route_by_name(report, "projective gerbe/twisted bundle").get(
                "closes_selected_source"
            )
            is False
            and "selected gerbe representative" in route_by_name(
                report, "projective gerbe/twisted bundle"
            ).get("blocker", "")
            else "FAIL",
            str(route_by_name(report, "projective gerbe/twisted bundle")),
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
            "still open fields",
            "PASS" if all(value is True for value in cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "guardrails",
            "PASS" if all_guardrails_false(cert) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "paper records proof attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "conditional finite tensor: closed",
                    "selected source promotion: not closed",
                    "all_current_source_routes_blocked = true",
                    "selected orientation-carrying operator/source packet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected SU(5) source proof attempt audit")
    print("==========================================")
    print()
    print(f"conditional_projection_tensor_closed={calc.get('conditional_projection_tensor_closed')}")
    print(f"all_current_source_routes_blocked={calc.get('all_current_source_routes_blocked')}")
    print(f"remaining_proof_closed_now={calc.get('remaining_proof_closed_now')}")
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
