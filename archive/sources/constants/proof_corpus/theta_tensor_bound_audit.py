"""Audit the conditional no-knob Theta tensor bound."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "theta_tensor_bound_certificate.json"
PAPER = ROOT / "Theta_Tensor_Bound_No_Knob_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def r_bound(lambda_tev: float, m_pl_gev: float) -> float:
    lambda_gev = lambda_tev * 1_000.0
    return (lambda_gev / m_pl_gev) ** 2


def approx_equal(left: float, right: float, rel: float = 1e-12) -> bool:
    return abs(left - right) <= rel * max(abs(left), abs(right), 1e-300)


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    source_path = Path(cert["source"])
    source = read(source_path)
    selected = cert["selected_inputs"]
    computed = cert["computed_bounds"]
    verdict = cert["verdict"]
    m_pl = float(selected["reduced_planck_mass_GeV"])
    values = {
        "r_at_3_TeV": r_bound(3.0, m_pl),
        "r_at_5_TeV": r_bound(float(selected["mu_theta_TeV"]), m_pl),
        "r_at_10_TeV": r_bound(10.0, m_pl),
    }

    gates = [
        Gate(
            "certificate status",
            "PASS" if cert.get("status") == "CONDITIONAL_NO_KNOB_BOUND_CERTIFIED" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source present",
            "PASS" if source_path.exists() else "FAIL",
            str(source_path),
        ),
        Gate(
            "source carries assumptions",
            "PASS"
            if contains_all(
                source,
                [
                    "mu_\\Theta = 5~\\mathrm{TeV}",
                    "\\Lambda_\\Theta \\sim \\mu_\\Theta",
                    "H \\ll \\Lambda_\\Theta",
                    "r \\;\\lesssim\\;",
                    "2.4\\times 10^{18}",
                ],
            )
            else "FAIL",
            "Theta IV tensor-bound section",
        ),
        Gate(
            "numeric lower endpoint",
            "PASS" if approx_equal(values["r_at_3_TeV"], computed["r_at_3_TeV"]) else "FAIL",
            f"{values['r_at_3_TeV']:.16e}",
        ),
        Gate(
            "numeric central endpoint",
            "PASS" if approx_equal(values["r_at_5_TeV"], computed["r_at_5_TeV"]) else "FAIL",
            f"{values['r_at_5_TeV']:.16e}",
        ),
        Gate(
            "numeric upper endpoint",
            "PASS" if approx_equal(values["r_at_10_TeV"], computed["r_at_10_TeV"]) else "FAIL",
            f"{values['r_at_10_TeV']:.16e}",
        ),
        Gate(
            "paper states no observed-r input",
            "PASS"
            if contains_all(
                paper,
                [
                    "does not use the observed value",
                    "forbidden workflow",
                    "fitted Lambda_Theta",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
        Gate(
            "verdict discipline",
            "PASS"
            if verdict.get("is_absolute_dimensionless_bound") is True
            and verdict.get("is_unconditional_prediction") is False
            and verdict.get("is_no_knob_given_assumptions") is True
            else "FAIL",
            str(verdict),
        ),
    ]

    print("Theta tensor bound audit")
    print("========================")
    print()
    for key, value in values.items():
        print(f"{key}={value:.16e}")
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
