"""Audit the finite qutrit polarization transport lemma."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "qutrit_polarization_transport_lemma_certificate.json"
PAPER = ROOT / "Qutrit_Polarization_Transport_Lemma_v1.md"
SCRIPT = REPO / "scripts" / "prove_qutrit_polarization_transport_lemma.py"
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
    return all(abs(value - target) < TOL for value, target in zip(parsed, expected))


def run_analysis() -> dict[str, Any]:
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
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    analysis = run_analysis()

    heisenberg = analysis.get("finite_heisenberg_checks", {})
    intertwiners = analysis.get("fourier_intertwiner_checks", {})
    classification = analysis.get("dephased_hadamard_classification", {})
    theorem = analysis.get("sector_transport_theorem", {})
    heavy = analysis.get("heavy_link_consequence_if_selected", {})
    proved = analysis.get("what_this_proves", {})
    still_open = analysis.get("still_open", {})
    guardrails = analysis.get("guardrails", {})
    verdict = analysis.get("verdict", {})
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    cert_open = cert.get("still_open", {})
    cert_guardrails = cert.get("guardrails", {})
    cert_verdict = cert.get("verdict", {})

    expected = [
        1.0 / 3.0**0.5,
        complex(-1.0 / (2.0 * 3.0**0.5), -0.5),
    ]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "QUTRIT_POLARIZATION_TRANSPORT_LEMMA_PROVED_SELECTOR_HYPOTHESIS_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["F_dagger_Z_F_equals_X", "dephased_hadamard_roots"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "finite Heisenberg checks",
            "PASS" if all(value is True for value in heisenberg.values()) else "FAIL",
            str(heisenberg),
        ),
        Gate(
            "Fourier intertwiners",
            "PASS" if all(value is True for value in intertwiners.values()) else "FAIL",
            str(intertwiners),
        ),
        Gate(
            "Hadamard uniqueness",
            "PASS"
            if classification.get("solutions_count") == 2
            and classification.get("fourier_table_present") is True
            and classification.get("conjugate_fourier_table_present") is True
            and classification.get("orientation_selects_F_not_Fstar") is True
            else "FAIL",
            str(classification),
        ),
        Gate(
            "sector theorem",
            "PASS"
            if theorem.get("B_10") == "I_3 after dephasing/family-order convention"
            and theorem.get("B_bar5") == "F after the positive first-row/first-column convention"
            and theorem.get("finite_algebraic_transport_proved") is True
            else "FAIL",
            str(theorem),
        ),
        Gate(
            "heavy-link consequence",
            "PASS"
            if approx_vector(heavy.get("Delta_t_numeric", []), expected)
            and heavy.get("leading_heavy_link_nonzero") is True
            else "FAIL",
            str(heavy),
        ),
        Gate(
            "analysis proved fields",
            "PASS" if all(value is True for value in proved.values()) else "FAIL",
            str(proved),
        ),
        Gate(
            "analysis still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "analysis guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "analysis verdict",
            "PASS"
            if verdict.get("finite_transport_lemma_proved") is True
            and verdict.get("sector_transport_selection_reduced_to_polarization_selection") is True
            and verdict.get("selector_hypothesis_remains_external_to_this_finite_proof") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("finite_heisenberg_relation_ZX_equals_omega_XZ") is True
            and calc.get("F_dagger_Z_F_equals_X") is True
            and calc.get("F_dagger_X_F_equals_Z_inverse") is True
            and calc.get("dephased_hadamard_root3_solutions") == 2
            and calc.get("solutions_are_F_and_F_conjugate") is True
            and calc.get("finite_transport_lemma_proved") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "certificate still open",
            "PASS" if all(value is True for value in cert_open.values()) else "FAIL",
            str(cert_open),
        ),
        Gate(
            "certificate guardrails",
            "PASS" if all(value is False for value in cert_guardrails.values()) else "FAIL",
            str(cert_guardrails),
        ),
        Gate(
            "certificate verdict",
            "PASS"
            if cert_verdict.get("finite_transport_lemma_proved") is True
            and cert_verdict.get("full_sector_transport_selection_proved") is False
            else "FAIL",
            str(cert_verdict),
        ),
        Gate(
            "paper records proof",
            "PASS"
            if contains_all(
                paper,
                [
                    "F^dagger Z F = X",
                    "F^dagger X F = Z^-1",
                    "F,",
                    "F^*",
                    "Polarization Selection Lemma",
                    "This does not by itself prove",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Qutrit polarization transport lemma audit")
    print("=========================================")
    print()
    print(f"Delta_t_if_selected={heavy.get('Delta_t_numeric')}")
    print(f"hadamard_solutions={classification.get('solution_exponent_tables')}")
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
