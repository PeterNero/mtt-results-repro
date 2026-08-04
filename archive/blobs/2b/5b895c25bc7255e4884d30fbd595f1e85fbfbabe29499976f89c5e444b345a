"""Audit the exploratory absolute-normalization solution schema."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "exploratory_absolute_normalization_solution_certificate.json"
PAPER = ROOT / "Exploratory_Absolute_Normalization_Solution_v1.md"


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


def tau_adm(lambda_star: float, c_q: float, epsilon: float) -> float:
    return math.log(c_q / epsilon) / lambda_star


def lambda_eff(lambda_star: float, c_q: float, epsilon: float) -> float:
    return math.sqrt(lambda_star / math.log(c_q / epsilon))


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    sources = {key: Path(value) for key, value in cert.get("source_paths", {}).items()}
    source_text = {key: read(path) for key, path in sources.items()}
    model = cert["exploratory_numeric_model"]
    assumptions = model["assumptions"]
    verdict = cert["verdict"]

    lambda_star = float(assumptions["lambda_star_unit"])
    c_q = float(assumptions["C_Q"])
    rows = model["computed"]

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "EXPLORATORY_SOLUTION_SCHEMA_CERTIFIED_NOT_NUMERIC_CLOSURE"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source paths present",
            "PASS" if all(path.exists() for path in sources.values()) else "FAIL",
            str([str(path) for path in sources.values() if not path.exists()]),
        ),
        Gate(
            "damping source has formula",
            "PASS"
            if contains_all(
                source_text["fixed_point_damping"],
                [
                    "tau_{\\rm adm}",
                    "lambda_\\ast",
                    "log\\frac{C_Q}{\\varepsilon",
                    "Lambda_{\\rm eff}",
                ],
            )
            else "FAIL",
            str(sources["fixed_point_damping"]),
        ),
        Gate(
            "Strominger source has unique minimizer",
            "PASS"
            if contains_all(
                source_text["strominger_selection"],
                ["unique local minimizer", "positive hessian", "fixed point", "minimizer"],
            )
            else "FAIL",
            str(sources["strominger_selection"]),
        ),
        Gate(
            "flux source has scale/locus equations",
            "PASS"
            if contains_all(
                source_text["heterotic_flux"],
                ["u_1-v_1", "r_3^2", "fixing the *ratio* $R_1/R", "selection potential"],
            )
            else "FAIL",
            str(sources["heterotic_flux"]),
        ),
        Gate(
            "Theta source has central-circle branch data",
            "PASS"
            if contains_all(
                source_text["theta_iv"],
                ["R_1^3", "G_{10}", "31.8", "coherence scale"],
            )
            else "FAIL",
            str(sources["theta_iv"]),
        ),
    ]

    for row in rows:
        n = int(row["N"])
        epsilon = 1.0 / n
        gates.extend(
            [
                Gate(
                    f"N={n} epsilon",
                    "PASS" if approx_equal(epsilon, float(row["epsilon"])) else "FAIL",
                    f"{epsilon:.16g}",
                ),
                Gate(
                    f"N={n} tau",
                    "PASS"
                    if approx_equal(tau_adm(lambda_star, c_q, epsilon), float(row["tau_adm"]))
                    else "FAIL",
                    f"{tau_adm(lambda_star, c_q, epsilon):.16g}",
                ),
                Gate(
                    f"N={n} Lambda_eff",
                    "PASS"
                    if approx_equal(lambda_eff(lambda_star, c_q, epsilon), float(row["Lambda_eff_in_sqrt_lambda_units"]))
                    else "FAIL",
                    f"{lambda_eff(lambda_star, c_q, epsilon):.16g}",
                ),
            ]
        )

    gates.extend(
        [
            Gate(
                "branches not overclaimed",
                "PASS"
                if all(item.get("status") == "BRANCH_ASSUMPTION_NEEDS_SOURCE" for item in cert.get("candidate_identifications", []))
                else "FAIL",
                str(cert.get("candidate_identifications", [])),
            ),
            Gate(
                "forbidden shortcuts listed",
                "PASS"
                if contains_all(
                    " ".join(cert.get("forbidden_shortcuts", [])),
                    ["match G_N", "match M_Pl", "observed target constants"],
                )
                else "FAIL",
                str(cert.get("forbidden_shortcuts", [])),
            ),
            Gate(
                "paper states non-closure",
                "PASS"
                if contains_all(
                    paper,
                    [
                        "solution schema, not yet a numerical closure",
                        "These are not physical predictions",
                        "epsilon chosen to match G_N",
                    ],
                )
                else "FAIL",
                str(PAPER),
            ),
            Gate(
                "verdict",
                "PASS"
                if verdict.get("solution_schema_found") is True
                and verdict.get("numeric_absolute_normalization_closed") is False
                and verdict.get("best_branch_to_try_first") == "central_circle_branch"
                else "FAIL",
                str(verdict),
            ),
        ]
    )

    print("Exploratory absolute normalization solution audit")
    print("================================================")
    print()
    print(f"rows={len(rows)}")
    print(f"best_branch={verdict.get('best_branch_to_try_first')}")
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
