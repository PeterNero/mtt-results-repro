"""Audit the scale-lifting lemma for the selected flux/Strominger branch."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "scale_lifting_lemma_certificate.json"


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


def approx_equal(left: float, right: float, rel: float = 1e-12, abs_tol: float = 1e-12) -> bool:
    return abs(left - right) <= max(abs_tol, rel * max(abs(left), abs(right), 1e-300))


def s_star(a: float, b: float, p: float) -> float:
    return (p * a / (2.0 * b)) ** (1.0 / (p + 2.0))


def f_scale(s: float, a: float, b: float, p: float) -> float:
    return a * s ** (-p) + b * s**2


def f_second(s: float, a: float, b: float, p: float) -> float:
    return p * (p + 1.0) * a * s ** (-p - 2.0) + 2.0 * b


def main() -> None:
    cert = load_json(CERT)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    text = {key: read(path) for key, path in sources.items()}
    verdict = cert["verdict"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "CONDITIONAL_SCALE_LIFTING_LEMMA_PROVED_COEFFICIENT_EXTRACTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "proof note proves convexity",
            "PASS"
            if contains_all(
                text["proof_note"],
                ["F_scale(s) = A s^{-p} + B s^2", "strictly convex", "unique global minimizer"],
            )
            else "FAIL",
            str(sources["proof_note"]),
        ),
        Gate(
            "previous gate requested lemma",
            "PASS"
            if contains_all(
                text["minimization_functional"],
                ["Scale-Lifting Lemma", "F_scale(s) -> +infinity", "exactly one critical point"],
            )
            else "FAIL",
            str(sources["minimization_functional"]),
        ),
        Gate(
            "heterotic selection has OU source",
            "PASS"
            if contains_all(
                text["heterotic_selection"],
                ["Var}=\\delta/(2\\gamma)", "gamma=\\kappa\\lambda-L-\\Delta", "higher $\\alpha'$ corrections"],
            )
            else "FAIL",
            str(sources["heterotic_selection"]),
        ),
        Gate(
            "heterotic flux has UV control source",
            "PASS"
            if contains_all(
                text["heterotic_flux"],
                ["alpha'^2", "curvature-squared", "large volume and small flux"],
            )
            else "FAIL",
            str(sources["heterotic_flux"]),
        ),
        Gate(
            "OU floor source has variance",
            "PASS"
            if contains_all(
                text["ou_floor"],
                ["OU Dynamics", "stationary variance", "D}{\\gamma"],
            )
            else "FAIL",
            str(sources["ou_floor"]),
        ),
    ]

    for item in cert["example_normalized_cases"]:
        a = float(item["A"])
        b = float(item["B"])
        p = float(item["p"])
        star = s_star(a, b, p)
        gates.extend(
            [
                Gate(
                    f"A={a:g},B={b:g},p={p:g} s_star",
                    "PASS" if approx_equal(star, float(item["s_star"])) else "FAIL",
                    f"{star:.16g}",
                ),
                Gate(
                    f"A={a:g},B={b:g},p={p:g} F_min",
                    "PASS" if approx_equal(f_scale(star, a, b, p), float(item["F_min"])) else "FAIL",
                    f"{f_scale(star, a, b, p):.16g}",
                ),
                Gate(
                    f"A={a:g},B={b:g},p={p:g} F_second",
                    "PASS" if approx_equal(f_second(star, a, b, p), float(item["F_second_at_s_star"])) else "FAIL",
                    f"{f_second(star, a, b, p):.16g}",
                ),
                Gate(
                    f"A={a:g},B={b:g},p={p:g} positive convexity",
                    "PASS" if f_second(star, a, b, p) > 0 else "FAIL",
                    f"{f_second(star, a, b, p):.16g} > 0",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "lemma closure only",
                "PASS"
                if verdict.get("scale_lifting_lemma_proved") is True
                and verdict.get("unique_positive_minimizer_conditional_on_positive_coefficients") is True
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "coefficient extraction remains",
                "PASS"
                if verdict.get("coefficient_extraction_closed") is False
                and verdict.get("physical_absolute_normalization_closed") is False
                and verdict.get("remaining_gate_count") == 1
                else "FAIL",
                str(verdict),
            ),
        ]
    )

    print("Scale-lifting lemma audit")
    print("=========================")
    print()
    print(f"status={cert.get('status')}")
    print(f"remaining_gate={verdict.get('remaining_gate')}")
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
