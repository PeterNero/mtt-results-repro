"""Diagnostic check for the quark second-order breakdown operator candidate."""

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


def second_order_cost(j_profile: np.ndarray, i: int, j: int, b: int) -> float:
    return float((j_profile[i] - j_profile[b]) ** 2 + 0.5 * (j_profile[j] - j_profile[(b + 1) % 3]) ** 2)


def y_second_order(mu: float, phase_shift: int, lambda_q: float, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            y[i, j] = weights[b] * math.exp(-lambda_q * second_order_cost(j_profile, i, j, b))
    return y


def mixing(yu: np.ndarray, yd: np.ndarray, g_inv: np.ndarray) -> np.ndarray:
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    return np.abs(uu.conj().T @ ud)


def main() -> None:
    paper = read(ROOT / "Quark_Second_Order_Breakdown_Operator_Candidate_v1.md")
    tau = cmath.exp(2j * math.pi * Q / N)
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    lambda_q = LAMBDA_LENS - 3.0 * LAMBDA_NIL
    mu_u = 8.0
    mu_d = 2.0

    yu = y_second_order(mu_u, 1, lambda_q, j_profile, tau)
    yd = y_second_order(mu_d, 2, lambda_q, j_profile, tau)
    v = mixing(yu, yd, g_inv)

    target = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )
    err = float(np.linalg.norm(v - target))
    ckm_shaped = v[0, 0] > 0.95 and v[0, 1] < 0.30 and v[0, 2] < 0.03 and v[1, 2] < 0.08
    not_exact = err > 0.005

    gates = [
        Gate("paper saved", "PASS" if "explicit B_q candidate" in paper else "FAIL", "candidate paper present"),
        Gate("q79 phase source", "PASS" if N // math.gcd(Q, N) == 448 else "FAIL", "tau order 448"),
        Gate("second-order cost", "PASS" if "b_ij+1" in paper or "b+1" in paper else "FAIL", "retarded next-role term present"),
        Gate("structural constants", "CANDIDATE", f"mu_u={mu_u:g}, mu_d={mu_d:g}, Lambda_q={lambda_q:.3f}"),
        Gate("CKM-shaped", "PASS" if ckm_shaped else "FAIL", f"|V01|={v[0,1]:.4f}, |V02|={v[0,2]:.4f}, |V12|={v[1,2]:.4f}"),
        Gate("not exact closure", "OPEN" if not_exact else "FAIL", f"CKM Frobenius residual={err:.6f}"),
        Gate("constant derivation", "OPEN", "derive mu_u, mu_d, Lambda_q from Sigma_MTT"),
    ]

    print("Quark second-order breakdown operator check")
    print("===========================================")
    print()
    print(f"J profile: {[round(float(x), 6) for x in j_profile]}")
    print(f"mu_u={mu_u:g}, mu_d={mu_d:g}, Lambda_q={lambda_q:.6f}")
    print(f"CKM residual against target: {err:.6f}")
    print("|V_candidate|:")
    for row in v:
        print("  " + " ".join(f"{x:.6f}" for x in row))
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
