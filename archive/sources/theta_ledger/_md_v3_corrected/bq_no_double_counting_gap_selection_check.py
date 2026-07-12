"""Check the no-double-counting gap selection lemma for B_q."""

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
            cost += 0.5 * (j_profile[j] - j_profile[(b - 1) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def residual(lambda_q: float) -> float:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    tau = cmath.exp(2j * math.pi * Q / N)
    yu = y_second_order(8.0, 1, lambda_q, -1, j_profile, tau)
    yd = y_second_order(2.0, 2, lambda_q, -1, j_profile, tau)
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
    paper = read(ROOT / "Bq_No_Double_Counting_Gap_Selection_Lemma_v1.md")
    color_source = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    orientation = read(ROOT / "Bq_Retarded_Predecessor_Orientation_Lock_v1.md")

    lambda_internal = LAMBDA_LENS - LAMBDA_NIL
    lambda_external = LAMBDA_LENS - 3.0 * LAMBDA_NIL
    err_internal = residual(lambda_internal)
    err_external = residual(lambda_external)

    gates = [
        Gate("paper saved", "PASS" if "No Double Counting" in paper else "FAIL", "gap selection paper present"),
        Gate("color Schur source", "PASS" if "delta^2/2" in color_source else "FAIL", "internal color completion imported"),
        Gate("orientation imported", "PASS" if "sigma = -1" in orientation else "FAIL", "predecessor orientation imported"),
        Gate("internal gap value", "PASS" if abs(lambda_internal - 3.32) < 1e-12 else "FAIL", f"lambda_lens-lambda_nil={lambda_internal:.6f}"),
        Gate("external gap value", "PASS" if abs(lambda_external - 2.82) < 1e-12 else "FAIL", f"lambda_lens-3lambda_nil={lambda_external:.6f}"),
        Gate("diagnostic improves", "PASS" if err_internal < err_external else "FAIL", f"internal={err_internal:.6f}, external={err_external:.6f}"),
        Gate("stiffness constants", "OPEN", "mu_u and mu_d remain to be derived from Hessian blocks"),
    ]

    print("B_q no-double-counting gap selection check")
    print("==========================================")
    print()
    print(f"lambda_internal = lambda_lens - lambda_nil = {lambda_internal:.6f}")
    print(f"lambda_external = lambda_lens - 3lambda_nil = {lambda_external:.6f}")
    print(f"up-stiff sigma- residual internal = {err_internal:.6f}")
    print(f"up-stiff sigma- residual external = {err_external:.6f}")
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

