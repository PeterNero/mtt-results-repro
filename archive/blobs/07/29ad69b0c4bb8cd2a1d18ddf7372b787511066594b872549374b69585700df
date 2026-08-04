"""Audit the selected central-circle damping identification lemma."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"
PAPER = ROOT / "Selected_Central_Circle_Damping_Identification_Lemma_v1.md"


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


def r1(lambda_star: float, c_q: float, epsilon: float, sigma: float) -> float:
    return sigma * math.sqrt(math.log(c_q / epsilon) / lambda_star)


def required_alpha(c_q: float, epsilon: float, sigma: float) -> float:
    return sigma * sigma * math.log(c_q / epsilon) / 60.0


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    source_text = {key: read(path) for key, path in sources.items()}
    verdict = cert["verdict"]
    cases = cert["tested_cases"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "CONDITIONALLY_CLOSED_BY_Z64_NORMALIZED_TOWER_IDENTIFICATION"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "selected branch has target lemma",
            "PASS"
            if contains_all(source_text["selected_branch"], ["sigma_circle", "sqrt(log(C_Q/epsilon_adm)/lambda_*)", "R1 <= 2"])
            else "FAIL",
            str(sources["selected_branch"]),
        ),
        Gate(
            "Z64 source has normalized tower input",
            "PASS"
            if contains_all(
                source_text["z64_operator"],
                ["lambda_* = 15 alpha", "lambda_next = 24 alpha", "9 alpha", "alpha=1"],
            )
            else "FAIL",
            str(sources["z64_operator"]),
        ),
        Gate(
            "Theta I supplies R1 bound",
            "PASS"
            if contains_all(source_text["theta_i"], ["R_1\\le 2", "lambda_{\\Sigma_1}", "1}{R_1^2"])
            else "FAIL",
            str(sources["theta_i"]),
        ),
        Gate(
            "damping source supplies formula",
            "PASS"
            if contains_all(source_text["fixed_point_damping"], ["tau_{\\rm adm}", "lambda_\\ast", "C_Q", "varepsilon_{\\rm adm}"])
            else "FAIL",
            str(sources["fixed_point_damping"]),
        ),
    ]

    for item in cases:
        n = int(item["N"])
        epsilon = float(item["epsilon_adm"])
        c_q = float(item["C_Q"])
        sigma = float(item["sigma_circle"])
        naive = r1(float(item["lambda_star_naive"]), c_q, epsilon, sigma)
        normalized = r1(float(item["lambda_star_z64_normalized"]), c_q, epsilon, sigma)
        alpha_min = required_alpha(c_q, epsilon, sigma)
        gates.extend(
            [
                Gate(
                    f"N={n} naive R1 reproduces old failure",
                    "PASS" if approx_equal(naive, float(item["R1_naive"])) and naive > 2.0 else "FAIL",
                    f"{naive:.16g}",
                ),
                Gate(
                    f"N={n} Z64-normalized R1",
                    "PASS" if approx_equal(normalized, float(item["R1_z64_normalized"])) else "FAIL",
                    f"{normalized:.16g}",
                ),
                Gate(
                    f"N={n} Z64 branch closes R1<=2",
                    "PASS" if normalized <= 2.0 and item["closes_R1_le_2"] is True else "FAIL",
                    f"{normalized:.16g} <= 2",
                ),
                Gate(
                    f"N={n} alpha threshold",
                    "PASS" if approx_equal(alpha_min, float(item["required_alpha_min"])) and alpha_min < 1.0 else "FAIL",
                    f"{alpha_min:.16g}",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "conditional closure only",
                "PASS"
                if verdict.get("lemma_closed_under_z64_tower_identification") is True
                and verdict.get("numeric_absolute_normalization_closed") is False
                and verdict.get("remaining_premise_count") == 2
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "paper records remaining premises",
                "PASS"
                if contains_all(
                    paper,
                    [
                        "not yet an unconditional prediction",
                        "prove the damping Hessian block is the Z64 central-circle tower block",
                        "physical action-normalization certificate for G10 and alpha",
                    ],
                )
                else "FAIL",
                str(PAPER),
            ),
        ]
    )

    print("Selected central-circle damping identification lemma audit")
    print("=========================================================")
    print()
    print(f"tested_cases={len(cases)}")
    print(f"remaining_premise_count={verdict.get('remaining_premise_count')}")
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
