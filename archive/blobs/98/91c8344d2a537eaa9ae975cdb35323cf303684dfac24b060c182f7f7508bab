"""Audit the selected Fourier transport proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_selected_fourier_transport_proof.py"
CANDIDATE = REPO / "candidate_data" / "selected_fourier_transport_proof_attempt.candidate.json"
CERT = REPO / "certificates" / "selected_fourier_transport_proof_attempt_certificate.json"
PAPER = ROOT / "Selected_Fourier_Transport_Proof_Attempt_v1.md"


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


def route(report: dict[str, Any], name: str) -> dict[str, Any]:
    for item in report.get("route_evaluation", []):
        if item.get("route") == name:
            return item
    return {}


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    solution = report.get("correct_solution", {})

    routes_to_check = [
        "strongest current SU5 polarization packet",
        "selected gerbe/twisted-bundle promotion",
        "flat torsion orientation",
        "typed monad/Cech zero modes",
        "spectral Galerkin / selected D_E",
        "Route C residual solve",
    ]

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "Selected Gerbe-Fourier Polarization Promotion",
                    "selected_by_mtt=true",
                    "UNSELECTED_FIXTURE",
                    "Route C residual solve",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "SELECTED_FOURIER_TRANSPORT_PROOF_REDUCED_SOURCE_PROMOTION_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "finite core proved",
            "PASS"
            if calc.get("finite_fourier_core_proved") is True
            and calc.get("exact_route_b_object_computed") is True
            and calc.get("strongest_su5_fixture_finite_valid") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "not selected now",
            "PASS"
            if calc.get("strongest_su5_fixture_selected") is False
            and calc.get("selected_fourier_transport_proved_now") is False
            and calc.get("selected_source_routes_that_close_now") == []
            else "FAIL",
            str(calc),
        ),
        Gate(
            "source routes blocked",
            "PASS"
            if all(
                route(report, name).get("closes_selected_fourier_transport") is False
                for name in routes_to_check
            )
            else "FAIL",
            str({name: route(report, name).get("closes_selected_fourier_transport") for name in routes_to_check}),
        ),
        Gate(
            "correct solution identified",
            "PASS"
            if solution.get("name") == "Selected Gerbe-Fourier Polarization Promotion"
            and contains_all(
                " ".join(solution.get("minimal_packet_fields", [])),
                [
                    "selected_by_mtt=true",
                    "fixed differential-cohomology torsion label",
                    "twisted_projector_retains_sector=true",
                    "U_10^dagger U_bar5 = F",
                ],
            )
            else "FAIL",
            str(solution),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "open fields",
            "PASS"
            if cert.get("still_open", {}).get("selected_source_promotion_for_U10_Ubar5") is True
            and cert.get("still_open", {}).get("selected_projector_retention") is True
            and cert.get("still_open", {}).get("full_SM_closure") is True
            else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "paper records verdict",
            "PASS"
            if contains_all(
                paper,
                [
                    "finite Fourier transport: proved",
                    "selected Fourier transport from MTT geometry: not yet proved",
                    "Selected Gerbe-Fourier Polarization Promotion",
                    "UNSELECTED_FIXTURE",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected Fourier transport proof attempt audit")
    print("==============================================")
    print()
    print(f"finite_core={calc.get('finite_fourier_core_proved')}")
    print(f"selected_now={calc.get('selected_fourier_transport_proved_now')}")
    print(f"solution={solution.get('name')}")
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
