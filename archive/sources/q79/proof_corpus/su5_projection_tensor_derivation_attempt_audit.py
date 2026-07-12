"""Audit the SU(5) projection-tensor derivation attempt."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "derive_su5_projection_tensor_attempt.py"
CANDIDATE = REPO / "candidate_data" / "su5_projection_tensor_derivation_attempt.candidate.json"
CERT = REPO / "certificates" / "su5_projection_tensor_derivation_attempt_certificate.json"
PAPER = ROOT / "SU5_Projection_Tensor_Derivation_Attempt_v1.md"
TOL = 1e-9
SQRT3_INV = 1.0 / math.sqrt(3.0)


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


def close_vector(values: list[Any], expected: list[complex]) -> bool:
    if len(values) != len(expected):
        return False
    parsed = [to_complex(value) for value in values]
    return all(abs(value - target) < TOL for value, target in zip(parsed, expected))


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


def branch(report: dict[str, Any], name: str) -> dict[str, Any]:
    return report.get("branches", {}).get(name, {})


def validators_pass(report: dict[str, Any], name: str) -> bool:
    validators = branch(report, name).get("validators", {})
    return (
        validators.get("polarization_packet", {}).get("exit_code") == 0
        and validators.get("c1_heavy_link_delta_t", {}).get("exit_code") == 0
        and validators.get("ckm_heavy_link_gate", {}).get("exit_code") == 0
    )


def promotes_selected(report: dict[str, Any], name: str) -> bool:
    return (
        branch(report, name)
        .get("validators", {})
        .get("polarization_packet", {})
        .get("promotes_to_selected_heavy_link_input")
        is True
    )


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})

    q79_expected = [complex(SQRT3_INV, 0.0), complex(-0.5 * SQRT3_INV, -0.5)]
    q369_expected = [complex(SQRT3_INV, 0.0), complex(-0.5 * SQRT3_INV, 0.5)]
    q79 = branch(report, "current_q79_orientation")
    q369 = branch(report, "conjugate_q369_orientation")

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "SU5ProjectionTensorDerivationAttempt",
                    "T_u=I_3",
                    "T_d=F",
                    "selection_still_open",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "FINITE_PROJECTION_TENSOR_DERIVED_CONDITIONALLY_SELECTION_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "branch orientations",
            "PASS"
            if q79.get("branch_packet", {}).get("conditional_su5_transport_orientation")
            == "F"
            and q369.get("branch_packet", {}).get("conditional_su5_transport_orientation")
            == "F*"
            and q79.get("checks", {}).get("T_d_is_expected_fourier_orientation") is True
            and q369.get("checks", {}).get("T_d_is_expected_fourier_orientation") is True
            else "FAIL",
            str((q79.get("branch_packet"), q369.get("branch_packet"))),
        ),
        Gate(
            "Delta_t values",
            "PASS"
            if close_vector(q79.get("heavy_link", {}).get("Delta_t", []), q79_expected)
            and close_vector(q369.get("heavy_link", {}).get("Delta_t", []), q369_expected)
            else "FAIL",
            str((q79.get("heavy_link"), q369.get("heavy_link"))),
        ),
        Gate(
            "finite validators pass",
            "PASS"
            if validators_pass(report, "current_q79_orientation")
            and validators_pass(report, "conjugate_q369_orientation")
            and calc.get("finite_validators_pass") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "conditional not selected",
            "PASS"
            if not promotes_selected(report, "current_q79_orientation")
            and not promotes_selected(report, "conjugate_q369_orientation")
            and calc.get("selected_polarization_source_promotes") is False
            and calc.get("selection_still_open") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "CKM gate conditional pass",
            "PASS"
            if q79.get("validators", {})
            .get("ckm_heavy_link_gate", {})
            .get("report", {})
            .get("gate", {})
            .get("leading_noncommutation_pass")
            is True
            and q369.get("validators", {})
            .get("ckm_heavy_link_gate", {})
            .get("report", {})
            .get("gate", {})
            .get("leading_noncommutation_pass")
            is True
            else "FAIL",
            "conditional heavy-link gate should pass for both branches",
        ),
        Gate(
            "candidate file matches run",
            "PASS"
            if candidate.get("calculation_results") == report.get("calculation_results")
            and cert_calc == report.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "finite projection tensor: derived conditionally",
                    "selected MTT projection tensor: still open",
                    "T_u    = U_10^dagger U_10",
                    "T_d    = U_10^dagger U_bar5",
                    "promotes_to_selected_heavy_link_input = false",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) projection tensor derivation attempt audit")
    print("================================================")
    print()
    print(f"q79_Delta_t={q79.get('heavy_link', {}).get('Delta_t')}")
    print(f"q369_Delta_t={q369.get('heavy_link', {}).get('Delta_t')}")
    print(f"selection_still_open={calc.get('selection_still_open')}")
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
