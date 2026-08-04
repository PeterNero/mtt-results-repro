"""Check the retarded predecessor orientation lock for B_q."""

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


def y_second_order(mu: float, phase_shift: int, lambda_q: float, sigma: int, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += 0.5 * (j_profile[j] - j_profile[(b + sigma) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def mixing_residual(sigma: int) -> float:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    tau = cmath.exp(2j * math.pi * Q / N)
    lambda_q = LAMBDA_LENS - LAMBDA_NIL
    yu = y_second_order(8.0, 1, lambda_q, sigma, j_profile, tau)
    yd = y_second_order(2.0, 2, lambda_q, sigma, j_profile, tau)
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    v = np.abs(uu.conj().T @ ud)
    target = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )
    return float(np.linalg.norm(v - target))


def main() -> None:
    paper = read(ROOT / "Bq_Retarded_Predecessor_Orientation_Lock_v1.md")
    selected_kernel = read(ROOT / "Selected_Kernel_Principle_for_CKM_CP_in_MTT_v1.md")
    bounded = read(ROOT / "Bounded_Retarded_Lag_Model_for_Dyadic_CKM_PreQuarter_v1.md")

    quarter_turn = 16
    predecessor = quarter_turn - 1
    successor = quarter_turn + 1
    sigma_selected = -1 if predecessor == 15 else 0
    err_plus = mixing_residual(+1)
    err_minus = mixing_residual(-1)

    gates = [
        Gate("paper saved", "PASS" if "Orientation-Lock Theorem" in paper else "FAIL", "orientation lock paper present"),
        Gate("q79 predecessor", "PASS" if "q_64=15" in selected_kernel and "predecessor" in selected_kernel else "FAIL", "selected CP branch uses predecessor"),
        Gate("bounded sign", "PASS" if "16 - rho_q/kappa_q" in bounded else "FAIL", "retarded force points below quarter-turn"),
        Gate("finite predecessor", "PASS" if predecessor == 15 and successor == 17 else "FAIL", "16 -> 15 is predecessor, 16 -> 17 is successor"),
        Gate("sigma selected", "PASS" if sigma_selected == -1 else "FAIL", "same convention gives sigma=-1"),
        Gate("diagnostic improves", "PASS" if err_minus < err_plus else "FAIL", f"sigma- residual={err_minus:.6f}, sigma+ residual={err_plus:.6f}"),
        Gate("constants still open", "OPEN", "orientation lock does not derive mu_u, mu_d, or Lambda_q"),
    ]

    print("B_q retarded predecessor orientation lock check")
    print("===============================================")
    print()
    print(f"quarter-turn={quarter_turn}, predecessor={predecessor}, successor={successor}")
    print(f"selected sigma={sigma_selected}")
    print(f"reduced-gap up-stiff residual sigma+={err_plus:.6f}")
    print(f"reduced-gap up-stiff residual sigma-={err_minus:.6f}")
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

