"""Diagnostic for the reduced color-gap branch of the B_q operator."""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
Q = 79
N = 448
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25


@dataclass(frozen=True)
class Branch:
    label: str
    mu_u: float
    mu_d: float
    lambda_q: float
    sigma: int


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def sorted_eigh(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(h)
    idx = np.argsort(values)
    return values[idx], vectors[:, idx]


def y_second_order(branch_mu: float, phase_shift: int, lambda_q: float, sigma: int, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    weights = np.exp(-branch_mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += 0.5 * (j_profile[j] - j_profile[(b + sigma) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def branch_matrix(branch: Branch, j_profile: np.ndarray, tau: complex, g_inv: np.ndarray) -> np.ndarray:
    yu = y_second_order(branch.mu_u, 1, branch.lambda_q, branch.sigma, j_profile, tau)
    yd = y_second_order(branch.mu_d, 2, branch.lambda_q, branch.sigma, j_profile, tau)
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    return np.abs(uu.conj().T @ ud)


def is_ckm_shaped(v: np.ndarray) -> bool:
    return bool(v[0, 0] > 0.95 and 0.15 < v[0, 1] < 0.30 and v[0, 2] < 0.03 and 0.02 < v[1, 2] < 0.08)


def main() -> None:
    paper = read(ROOT / "Bq_Reduced_Color_Gap_Branch_Diagnostic_v1.md")
    source = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    tau = cmath.exp(2j * math.pi * Q / N)
    target = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )

    branches = [
        Branch("old 3nil sigma+ up-stiff", 8.0, 2.0, LAMBDA_LENS - 3.0 * LAMBDA_NIL, 1),
        Branch("reduced gap sigma+ up-stiff", 8.0, 2.0, LAMBDA_LENS - LAMBDA_NIL, 1),
        Branch("reduced gap sigma- up-stiff", 8.0, 2.0, LAMBDA_LENS - LAMBDA_NIL, -1),
        Branch("reduced gap sigma- swapped", 2.0, 8.0, LAMBDA_LENS - LAMBDA_NIL, -1),
        Branch("reduced gap sigma- symmetric", 4.0, 4.0, LAMBDA_LENS - LAMBDA_NIL, -1),
    ]

    results: list[tuple[Branch, float, np.ndarray]] = []
    for branch in branches:
        v = branch_matrix(branch, j_profile, tau, g_inv)
        results.append((branch, float(np.linalg.norm(v - target)), v))

    old_err = results[0][1]
    reduced_up_err = results[2][1]
    best_branch, best_err, best_v = min(results, key=lambda item: item[1])

    gates = [
        Gate("paper saved", "PASS" if "Reduced Color-Gap Branch" in paper else "FAIL", "branch diagnostic paper present"),
        Gate("color source linked", "PASS" if "Schur coefficient 1/2" in source or "coefficient 1/2" in source else "FAIL", "uses color-singlet B_q source"),
        Gate("old branch shaped", "PASS" if is_ckm_shaped(results[0][2]) else "FAIL", f"old residual={old_err:.6f}"),
        Gate("reduced up-stiff improves", "PASS" if reduced_up_err < old_err else "FAIL", f"{reduced_up_err:.6f} < {old_err:.6f}"),
        Gate("best sibling recorded", "DIAGNOSTIC", f"{best_branch.label}, residual={best_err:.6f}"),
        Gate("exact branch selection", "OPEN", "must derive sigma, mu_u, mu_d, Lambda_q without CKM inputs"),
    ]

    print("B_q reduced color-gap branch diagnostic")
    print("=======================================")
    print()
    for branch, err, v in results:
        print(f"{branch.label}:")
        print(f"  mu=({branch.mu_u:g},{branch.mu_d:g}), Lambda={branch.lambda_q:.6f}, sigma={branch.sigma}, residual={err:.6f}")
        print(f"  |V01|={v[0,1]:.6f}, |V02|={v[0,2]:.6f}, |V12|={v[1,2]:.6f}, shaped={is_ckm_shaped(v)}")
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

