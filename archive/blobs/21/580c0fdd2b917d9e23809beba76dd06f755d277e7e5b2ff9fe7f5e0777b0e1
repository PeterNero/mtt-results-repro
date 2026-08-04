"""Audit the Execution I threshold-profile structural claim."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "execution_i_threshold_profile_certificate.json"
PAPER = ROOT / "Execution_I_Threshold_Profile_Structural_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def vector_add(left: list[float], right: list[float]) -> list[float]:
    return [a + b for a, b in zip(left, right)]


def scalar_mul(scalar: float, vector: list[float]) -> list[float]:
    return [scalar * value for value in vector]


def norm(vector: list[float]) -> float:
    return math.sqrt(sum(value * value for value in vector))


def approx_equal(left: float, right: float, rel: float = 1e-12, abs_tol: float = 1e-12) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def vector_approx_equal(left: list[float], right: list[float]) -> bool:
    return len(left) == len(right) and all(approx_equal(a, b) for a, b in zip(left, right))


def main() -> None:
    cert = load_json(CERT)
    source_path = Path(cert["source"])
    source = read(source_path)
    paper = read(PAPER)
    selected = cert["selected_inputs"]
    computed = cert["computed_checks"]
    verdict = cert["verdict"]

    chi_1 = [float(value) for value in selected["exceptional_basis"]["chi_1"]]
    chi_2 = [float(value) for value in selected["exceptional_basis"]["chi_2"]]
    c_1 = float(selected["exceptional_coefficients"]["c_1"])
    c_2 = float(selected["exceptional_coefficients"]["c_2"])
    exceptional = vector_add(scalar_mul(c_1, chi_1), scalar_mul(c_2, chi_2))
    bulk = [float(value) for value in selected["bulk_vector_reported"]]
    exceptional_norm = norm(exceptional)
    bulk_norm = norm(bulk)
    ratio = exceptional_norm / bulk_norm

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "THRESHOLD_PROFILE_STRUCTURAL_CONSISTENCY_CERTIFIED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source present",
            "PASS" if source_path.exists() else "FAIL",
            str(source_path),
        ),
        Gate(
            "source has threshold ansatz",
            "PASS"
            if contains_all(
                source,
                [
                    "\\Delta\\vec{\\alpha}",
                    "\\delta = -25.2",
                    "\\log \\tau_1",
                    "\\Delta_a^{\\mathrm{exc}}",
                    "c_1 = 0.31",
                    "c_2 = -0.27",
                ],
            )
            else "FAIL",
            "Execution I threshold sections",
        ),
        Gate(
            "exceptional vector",
            "PASS"
            if vector_approx_equal(exceptional, computed["exceptional_vector_from_basis"])
            else "FAIL",
            str(exceptional),
        ),
        Gate(
            "exceptional sum zero",
            "PASS" if approx_equal(sum(exceptional), computed["sum_exceptional_vector"]) else "FAIL",
            f"{sum(exceptional):.16g}",
        ),
        Gate(
            "exceptional norm",
            "PASS" if approx_equal(exceptional_norm, computed["exceptional_norm"]) else "FAIL",
            f"{exceptional_norm:.16g}",
        ),
        Gate(
            "bulk norm",
            "PASS" if approx_equal(bulk_norm, computed["bulk_norm_reported"]) else "FAIL",
            f"{bulk_norm:.16g}",
        ),
        Gate(
            "few-percent ratio",
            "PASS" if approx_equal(ratio, computed["norm_ratio"]) and ratio < 0.03 else "FAIL",
            f"{ratio:.16g}",
        ),
        Gate(
            "no prediction overclaim",
            "PASS"
            if verdict.get("structural_consistency_certified") is True
            and verdict.get("new_no_knob_prediction_certified") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records coefficient caveat",
            "PASS"
            if contains_all(
                paper,
                [
                    "not certified as a new no-knob prediction",
                    "solving for exact matching",
                    "consistency coefficients",
                    "without fitting the target threshold profile",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Execution I threshold profile audit")
    print("===================================")
    print()
    print(f"exceptional_vector={exceptional}")
    print(f"exceptional_norm={exceptional_norm:.16g}")
    print(f"bulk_norm={bulk_norm:.16g}")
    print(f"norm_ratio={ratio:.16g}")
    print()

    width = max(len(gate.label) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
