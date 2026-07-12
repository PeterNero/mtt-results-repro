"""Audit the Route B final missing object calculation attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "calculate_route_b_final_missing_object.py"
CANDIDATE = REPO / "candidate_data" / "route_b_final_missing_object_attempt.candidate.json"
CERT = REPO / "certificates" / "route_b_final_missing_object_attempt_certificate.json"
PAPER = ROOT / "Route_B_Final_Missing_Object_Calculation_Attempt_v1.md"
TOL = 1e-9


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


def to_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"cannot parse complex value {value!r}")


def approx_vector(values: list[Any], expected: list[complex]) -> bool:
    parsed = [to_complex(value) for value in values]
    return len(parsed) == len(expected) and all(abs(a - b) < TOL for a, b in zip(parsed, expected))


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
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    expected = [
        1.0 / 3.0**0.5,
        complex(-1.0 / (2.0 * 3.0**0.5), -0.5),
    ]
    calc = report.get("calculation_results", {})
    exact = calc.get("final_missing_object_if_selected", {})
    packet = report.get("route_b_overlap_difference_packet", {})
    route_b_report = report.get("route_b_calculator_report", {})
    cert_calc = cert.get("calculation_results", {})

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "U_10 = I_3",
                    "U_bar5 = F",
                    "basis_connection_delta",
                    "ROUTE_B_FINAL_MISSING_OBJECT",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "ROUTE_B_FINAL_MISSING_OBJECT_CALCULATED_CONDITIONAL_SELECTION_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "unitary relative transport",
            "PASS"
            if calc.get("U10_unitary") is True
            and calc.get("Ubar5_unitary") is True
            and calc.get("relative_transport_rule") == "U_10^dagger U_bar5 = F"
            else "FAIL",
            str(calc),
        ),
        Gate(
            "Delta_t exact candidate",
            "PASS"
            if exact.get("Delta_t_symbolic") == ["1/sqrt(3)", "omega^2/sqrt(3)"]
            and approx_vector(exact.get("Delta_t_numeric", []), expected)
            else "FAIL",
            str(exact),
        ),
        Gate(
            "five overlap slots zero",
            "PASS"
            if all(value == 0.0 for value in packet.get("overlap_differences", {}).values())
            and all(value == 0.0 for value in exact.get("overlap_differences", {}).values())
            else "FAIL",
            str(packet.get("overlap_differences")),
        ),
        Gate(
            "basis connection carries object",
            "PASS"
            if approx_vector(
                packet.get("extra_delta_t_terms", {}).get("basis_connection_delta", []),
                expected,
            )
            and packet.get("extra_delta_t_terms", {}).get("theta_overlap_variation_delta")
            == [0.0, 0.0]
            and packet.get("extra_delta_t_terms", {}).get("explicit_vertex_delta")
            == [0.0, 0.0]
            else "FAIL",
            str(packet.get("extra_delta_t_terms")),
        ),
        Gate(
            "Route B calculator result",
            "PASS"
            if route_b_report.get("leading_noncommutation_structurally_nonzero") is True
            and route_b_report.get("promotes_to_selected_CKM_heavy_link_input") is False
            and approx_vector(route_b_report.get("Delta_t", []), expected)
            else "FAIL",
            str(route_b_report),
        ),
        Gate(
            "certificate records result",
            "PASS"
            if cert_calc.get("overlap_differences_all_zero") is True
            and cert_calc.get("nonzero_slot") == "basis_connection_delta"
            and cert_calc.get("route_b_packet_structurally_nonzero") is True
            and cert_calc.get("route_b_packet_promotes_to_selected_input") is False
            else "FAIL",
            str(cert_calc),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "selection remains open",
            "PASS"
            if cert.get("still_open", {}).get("selected_source_promotion") is True
            and report.get("verdict", {}).get("selected_final_object_calculated_now") is False
            else "FAIL",
            str((cert.get("still_open"), report.get("verdict"))),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "Delta_t = (1/sqrt(3), omega^2/sqrt(3))",
                    "basis_connection_delta",
                    "UNSELECTED_FIXTURE_STRONGEST_CURRENT_ROUTE",
                    "exact conditional Route B object",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Route B final missing object calculation audit")
    print("==============================================")
    print()
    print(f"Delta_t={exact.get('Delta_t_numeric')}")
    print(f"promotes_selected={route_b_report.get('promotes_to_selected_CKM_heavy_link_input')}")
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
