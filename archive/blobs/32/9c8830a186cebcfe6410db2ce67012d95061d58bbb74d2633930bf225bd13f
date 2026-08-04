"""Audit the selected damping normalization branch."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_damping_normalization_branch_certificate.json"
PAPER = ROOT / "Selected_Damping_Normalization_Branch_v1.md"


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


def lambda_eff(lambda_star: float, c_q: float, epsilon: float) -> float:
    return math.sqrt(lambda_star / math.log(c_q / epsilon))


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    source_text = {key: read(path) for key, path in sources.items()}
    verdict = cert["verdict"]
    examples = cert["exploratory_finite_resolution_examples"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "CENTRAL_CIRCLE_BRANCH_REDUCED_TO_SINGLE_OPEN_LEMMA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "sources present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "damping source has scale formula",
            "PASS"
            if contains_all(
                source_text["fixed_point_damping"],
                ["tau_{\\rm adm}", "lambda_\\ast", "Lambda_{\\rm eff}", "not freely adjustable"],
            )
            else "FAIL",
            str(sources["fixed_point_damping"]),
        ),
        Gate(
            "strominger source has Hessian/minimizer",
            "PASS"
            if contains_all(
                source_text["strominger_selection"],
                ["Positive Hessian", "unique local minimizer", "spectral gap", "fixed point"],
            )
            else "FAIL",
            str(sources["strominger_selection"]),
        ),
        Gate(
            "theta I has central-circle bound",
            "PASS"
            if contains_all(source_text["theta_i"], ["R_1\\le 2", "lambda_{\\Sigma_1}", "R_1^2"])
            else "FAIL",
            str(sources["theta_i"]),
        ),
        Gate(
            "theta IV has Newton structure",
            "PASS"
            if contains_all(source_text["theta_iv"], ["31.8", "R_1^3", "G_{10}", "does not attempt to compute"])
            else "FAIL",
            str(sources["theta_iv"]),
        ),
        Gate(
            "Z64 source has central-circle Hessian clues",
            "PASS"
            if contains_all(source_text["z64_operator"], ["shared central circle", "lambda_* = 15 alpha", "spectral gap equals 9"])
            else "FAIL",
            str(sources["z64_operator"]),
        ),
    ]

    for item in examples:
        n = int(item["N"])
        epsilon = float(item["epsilon_adm"])
        c_q = float(item["C_Q"])
        lambda_star = float(item["lambda_star"])
        eff = lambda_eff(lambda_star, c_q, epsilon)
        r1 = 1.0 / eff
        gates.extend(
            [
                Gate(
                    f"N={n} Lambda_eff",
                    "PASS" if approx_equal(eff, float(item["Lambda_eff"])) else "FAIL",
                    f"{eff:.16g}",
                ),
                Gate(
                    f"N={n} R1",
                    "PASS" if approx_equal(r1, float(item["R1_if_sigma_one"])) else "FAIL",
                    f"{r1:.16g}",
                ),
                Gate(
                    f"N={n} naive R1 bound status",
                    "PASS" if r1 > 2.0 else "FAIL",
                    "naive branch remains above R1<=2; not closed",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "single lemma recorded",
                "PASS"
                if cert.get("single_open_lemma", {}).get("name") == "Selected Central-Circle Damping Identification Lemma"
                and "sigma_circle" in cert.get("single_open_lemma", {}).get("statement", "")
                else "FAIL",
                str(cert.get("single_open_lemma", {})),
            ),
            Gate(
                "no numeric overclaim",
                "PASS"
                if verdict.get("branch_finished_as_reduction") is True
                and verdict.get("numeric_absolute_normalization_closed") is False
                and verdict.get("remaining_lemma_count") == 1
                else "FAIL",
                str(verdict),
            ),
            Gate(
                "paper states reduction",
                "PASS"
                if contains_all(
                    paper,
                    [
                        "can now be finished as a reduction",
                        "naive finite-count choices are close",
                        "do not close the branch",
                        "Selected Central-Circle Damping Identification Lemma",
                    ],
                )
                else "FAIL",
                str(PAPER),
            ),
        ]
    )

    print("Selected damping normalization branch audit")
    print("===========================================")
    print()
    print(f"examples={len(examples)}")
    print(f"remaining_lemma_count={verdict.get('remaining_lemma_count')}")
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
