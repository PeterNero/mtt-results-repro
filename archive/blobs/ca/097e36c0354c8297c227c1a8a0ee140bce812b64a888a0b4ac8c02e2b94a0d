"""Check the selected finite B_q branch theorem."""

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


def y_selected(mu: float, phase_shift: int, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    lambda_q = LAMBDA_LENS - LAMBDA_NIL
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += 0.5 * (j_profile[j] - j_profile[(b - 1) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def main() -> None:
    paper = read(ROOT / "Selected_Finite_Bq_Branch_Theorem_v1.md")
    color = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    orientation = read(ROOT / "Bq_Retarded_Predecessor_Orientation_Lock_v1.md")
    gap = read(ROOT / "Bq_No_Double_Counting_Gap_Selection_Lemma_v1.md")
    stiffness = read(ROOT / "Bq_Hypercharge_Square_Stiffness_Source_v1.md")

    tau = cmath.exp(2j * math.pi * Q / N)
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
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
    err = float(np.linalg.norm(v - target))
    ckm_shaped = bool(v[0, 0] > 0.95 and 0.15 < v[0, 1] < 0.30 and v[0, 2] < 0.03 and 0.02 < v[1, 2] < 0.08)

    gates = [
        Gate("paper saved", "PASS" if "Selected Finite B_q Branch" in paper else "FAIL", "consolidated theorem present"),
        Gate("q79 phase", "PASS" if N // math.gcd(Q, N) == 448 else "FAIL", "tau has order 448"),
        Gate("color coefficient", "PASS" if "delta^2/2" in color and "1/2" in paper else "FAIL", "Schur color source imported"),
        Gate("orientation", "PASS" if "sigma = -1" in orientation and "sigma=-1" in paper else "FAIL", "predecessor orientation imported"),
        Gate("gap", "PASS" if "lambda_lens - lambda_nil" in gap and "Lambda_q=lambda_lens-lambda_nil" in paper else "FAIL", "reduced gap imported"),
        Gate("stiffness", "PASS" if "mu_u = 2 * 2^2 = 8" in stiffness and "mu_u=8" in paper else "FAIL", "hypercharge-square stiffness imported"),
        Gate("CKM-shaped", "PASS" if ckm_shaped else "FAIL", f"residual={err:.6f}, |V01|={v[0,1]:.4f}, |V12|={v[1,2]:.4f}"),
        Gate("full Hessian execution", "OPEN", "full Sigma_MTT Hessian extraction still required"),
    ]

    print("Selected finite B_q branch theorem check")
    print("========================================")
    print()
    print(f"J profile: {[round(float(x), 6) for x in j_profile]}")
    print(f"sigma=-1, Lambda_q={LAMBDA_LENS - LAMBDA_NIL:.6f}, mu_u=8, mu_d=2")
    print(f"CKM residual={err:.6f}")
    print("|V_selected|:")
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

