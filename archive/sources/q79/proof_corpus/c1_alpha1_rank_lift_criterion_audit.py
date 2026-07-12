"""Audit the algebraic rank test for a single alpha_1 C1 response."""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c1_alpha1_rank_lift_criterion_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
C1_INSERTION_CERT = ROOT.parent / "certificates" / "c1_curvature_insertion_formula_certificate.json"
C1_RPLUS_CERT = ROOT.parent / "certificates" / "c1_iwasawa_rplus_support_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def det3(matrix: list[list[Fraction]]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def add3(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[left[row][col] + right[row][col] for col in range(3)] for row in range(3)]


def scale3(scalar: Fraction, matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[scalar * matrix[row][col] for col in range(3)] for row in range(3)]


def light_cofactor(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    cert = load_json(CERT)
    seed_cert = load_json(SEED_CERT)
    c1_insertion_cert = load_json(C1_INSERTION_CERT)
    c1_rplus_cert = load_json(C1_RPLUS_CERT)
    paper = read(ROOT / "C1_Alpha1_Rank_Lift_Criterion_for_Rank_One_Lift_v1.md")

    closed = cert.get("closed", {})
    open_fields = cert.get("open", {})
    det_expansion = cert.get("determinant_expansion", {})

    e33 = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    m = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(13)],
        [Fraction(17), Fraction(19), Fraction(23)],
    ]
    epsilon = Fraction(1, 97)
    direct = det3(add3(e33, scale3(epsilon, m)))
    expanded = epsilon**2 * light_cofactor(m) + epsilon**3 * det3(m)

    rank_pass_example = [
        [Fraction(1), Fraction(0), Fraction(2)],
        [Fraction(0), Fraction(1), Fraction(3)],
        [Fraction(5), Fraction(7), Fraction(11)],
    ]
    rank_pass_direct = det3(add3(e33, scale3(epsilon, rank_pass_example)))
    degenerate_example = [
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(2), Fraction(4), Fraction(1)],
        [Fraction(3), Fraction(5), Fraction(7)],
    ]

    gates = [
        Gate(
            "certificate status",
            "CRITERION-CLOSED"
            if cert.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "rank-one seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "Y0=E33 rank-one seed available",
        ),
        Gate(
            "C1 insertion input",
            "FORMULATED-OPEN"
            if c1_insertion_cert.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(c1_insertion_cert.get("status")),
        ),
        Gate(
            "C1 alpha_1 support input",
            "SUPPORT-CLOSED"
            if c1_rplus_cert.get("status") == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
            else "FAIL",
            str(c1_rplus_cert.get("status")),
        ),
        Gate(
            "determinant expansion",
            "PASS" if direct == expanded and "epsilon^2 C33" in det_expansion.get("formula", "") else "FAIL",
            f"direct={direct}, expanded={expanded}",
        ),
        Gate(
            "light-family cofactor",
            "PASS"
            if light_cofactor(m) == Fraction(1)
            and "M11*M22 - M12*M21" in det_expansion.get("light_family_cofactor", "")
            else "FAIL",
            f"C33(example)={light_cofactor(m)}",
        ),
        Gate(
            "single driver not fatal",
            "PASS"
            if light_cofactor(rank_pass_example) != 0
            and rank_pass_direct != 0
            and closed.get("single_alpha1_driver_not_algebraically_fatal") is True
            else "FAIL",
            "one alpha_1 response matrix can have nonzero light-family minor",
        ),
        Gate(
            "degenerate branch separated",
            "PASS"
            if light_cofactor(degenerate_example) == 0
            and det3(degenerate_example) != 0
            and "cubic order" in det_expansion.get("degenerate_fallback", "")
            else "FAIL",
            f"C33={light_cofactor(degenerate_example)}, detM={det3(degenerate_example)}",
        ),
        Gate(
            "values remain open",
            "OPEN"
            if open_fields.get("actual_M_C1_alpha1_entries") is True
            and open_fields.get("zero_mode_contractions_with_alpha1_driver") is True
            else "FAIL",
            "criterion only; M_C1 entries are not computed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "Alpha1 Rank-Lift Criterion" in paper else "FAIL",
            "rank-lift criterion theorem is written",
        ),
    ]

    print("C1 alpha1 rank-lift criterion audit")
    print("===================================")
    print()
    print(f"det_formula={det_expansion.get('formula')}")
    print(f"leading_condition={det_expansion.get('leading_full_rank_condition')}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
