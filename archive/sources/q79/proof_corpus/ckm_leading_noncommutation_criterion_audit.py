"""Audit the leading CKM noncommutation criterion near the rank-one seed."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "ckm_leading_noncommutation_criterion_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "z64_exact_branch_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
C1_RANK_CERT = ROOT.parent / "certificates" / "c1_alpha1_rank_lift_criterion_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


Matrix = list[list[complex]]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def zero3() -> Matrix:
    return [[0j for _ in range(3)] for _ in range(3)]


def e33() -> Matrix:
    out = zero3()
    out[2][2] = 1 + 0j
    return out


def add(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] + right[i][j] for j in range(3)] for i in range(3)]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] - right[i][j] for j in range(3)] for i in range(3)]


def mul(left: Matrix, right: Matrix) -> Matrix:
    return [[sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(3)] for i in range(3)]


def comm(left: Matrix, right: Matrix) -> Matrix:
    return sub(mul(left, right), mul(right, left))


def first_variation(matrix: Matrix) -> Matrix:
    base = e33()
    return add(mul(base, adjoint(matrix)), mul(matrix, base))


def norm_sq(matrix: Matrix) -> float:
    return float(sum(abs(entry) ** 2 for row in matrix for entry in row))


def explicit_leading(delta_v1: complex, delta_v2: complex) -> Matrix:
    return [
        [0j, 0j, -delta_v1],
        [0j, 0j, -delta_v2],
        [delta_v1.conjugate(), delta_v2.conjugate(), 0j],
    ]


def main() -> None:
    cert = load_json(CERT)
    q79_cert = load_json(Q79_CERT)
    seed_cert = load_json(SEED_CERT)
    c1_rank_cert = load_json(C1_RANK_CERT)
    paper = read(ROOT / "CKM_Leading_Noncommutation_Criterion_for_Rank_One_Lift_v1.md")

    closed = cert.get("closed", {})
    open_fields = cert.get("open", {})
    expansion = cert.get("commutator_expansion", {})

    mu = [
        [1 + 0j, 2 + 0j, 3 + 1j],
        [4 + 0j, 5 + 0j, 7 - 2j],
        [8 + 0j, 9 + 0j, 11 + 0j],
    ]
    md = [
        [2 + 0j, 1 + 0j, 5 - 1j],
        [3 + 0j, 7 + 0j, 7 - 2j],
        [9 + 0j, 8 + 0j, 13 + 0j],
    ]
    delta_v = (md[0][2] - mu[0][2], md[1][2] - mu[1][2])
    leading_direct = comm(e33(), sub(first_variation(md), first_variation(mu)))
    leading_formula = explicit_leading(delta_v[0], delta_v[1])

    md_degenerate = [
        [2 + 0j, 1 + 0j, mu[0][2]],
        [3 + 0j, 7 + 0j, mu[1][2]],
        [9 + 0j, 8 + 0j, 13 + 0j],
    ]
    degenerate_delta = (md_degenerate[0][2] - mu[0][2], md_degenerate[1][2] - mu[1][2])
    degenerate_leading = comm(e33(), sub(first_variation(md_degenerate), first_variation(mu)))

    gates = [
        Gate(
            "certificate status",
            "CRITERION-CLOSED"
            if cert.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "q79 CP input",
            "CLOSED" if q79_cert.get("conclusion", {}).get("q_mod_448") == 79 else "FAIL",
            "q=79 read from exact branch certificate",
        ),
        Gate(
            "rank-one seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "Y0=E33 rank-one seed available",
        ),
        Gate(
            "C1 rank criterion input",
            "CRITERION-CLOSED"
            if c1_rank_cert.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(c1_rank_cert.get("status")),
        ),
        Gate(
            "commutator expansion",
            "PASS"
            if norm_sq(sub(leading_direct, leading_formula)) < 1e-24
            and "[E33,A_d-A_u]" in expansion.get("formula", "")
            else "FAIL",
            f"Delta_v={delta_v}",
        ),
        Gate(
            "leading noncommutation",
            "PASS"
            if norm_sq(leading_direct) > 0
            and "Delta v != (0,0)" in expansion.get("leading_noncommutation_condition", "")
            else "FAIL",
            f"leading_norm_sq={norm_sq(leading_direct):.6g}",
        ),
        Gate(
            "degenerate leading case",
            "PASS"
            if degenerate_delta == (0j, 0j)
            and norm_sq(degenerate_leading) == 0.0
            and "O(epsilon^2)" in expansion.get("fallback", "")
            else "FAIL",
            "Delta_v=0 leaves O(epsilon^2) fallback open",
        ),
        Gate(
            "rank and CKM separated",
            "PASS" if closed.get("rank_gate_separated_from_ckm_gate") is True else "FAIL",
            "C33 rank and Delta_v orientation are distinct targets",
        ),
        Gate(
            "Jarlskog not overclaimed",
            "OPEN"
            if open_fields.get("Jarlskog_invariant_from_selected_matrices") is True
            and closed.get("jarlskog_gate_not_overclaimed") is True
            else "FAIL",
            "criterion does not claim CKM angles or full CP invariant",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "Leading CKM Noncommutation Criterion" in paper else "FAIL",
            "noncommutation theorem is written",
        ),
    ]

    print("CKM leading noncommutation criterion audit")
    print("==========================================")
    print()
    print(f"Delta_v={delta_v}")
    print(f"leading_norm_sq={norm_sq(leading_direct):.12g}")
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
