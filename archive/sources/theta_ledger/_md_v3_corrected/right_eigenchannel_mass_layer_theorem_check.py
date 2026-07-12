"""Check the right-eigenchannel mass-layer theorem target."""

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


def sorted_eigh(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(h)
    idx = np.argsort(values)
    return values[idx], vectors[:, idx]


def ckm_matrix(yu: np.ndarray, yd: np.ndarray, j_profile: np.ndarray) -> np.ndarray:
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    return np.abs(uu.conj().T @ ud)


def right_eigenchannel_adjust(y: np.ndarray, target_ratios: np.ndarray, g_inv_sqrt: np.ndarray, g_sqrt: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    z = y @ g_inv_sqrt
    u, singular_values, vh = np.linalg.svd(z, full_matrices=True)
    # np.linalg.svd sorts descending.  Target ratios are ascending normalized.
    target_desc = np.array([1.0, target_ratios[1], target_ratios[0]], dtype=float)
    current_desc = singular_values / singular_values[0]
    factors = target_desc / current_desc
    adjusted_z = u @ np.diag(singular_values * factors) @ vh
    adjusted = adjusted_z @ g_sqrt
    actions = -np.log(factors)
    # Return actions in ascending light, middle, heavy order.
    return adjusted, np.array([actions[2], actions[1], actions[0]], dtype=float)


def normalized_singular_values(y: np.ndarray) -> np.ndarray:
    s = np.array(sorted(np.linalg.svd(y, compute_uv=False)), dtype=float)
    return s / s[-1]


def main() -> None:
    paper = read(ROOT / "Right_Eigenchannel_Mass_Layer_Theorem_Target_v1.md")
    req = read(ROOT / "Selected_Mass_Layer_Requirements_after_Bq_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    g_sqrt = np.diag(np.exp(1.0 * j_profile))
    target_u = np.array([1.2e-5 / 0.53, 1.6e-3 / 0.53, 1.0])
    target_d = np.array([2.2e-4 / 0.11, 5.5e-3 / 0.11, 1.0])

    ckm_before = ckm_matrix(yu, yd, j_profile)
    yu_adj, au = right_eigenchannel_adjust(yu, target_u, g_inv_sqrt, g_sqrt)
    yd_adj, ad = right_eigenchannel_adjust(yd, target_d, g_inv_sqrt, g_sqrt)
    ckm_after = ckm_matrix(yu_adj, yd_adj, j_profile)
    up_after = normalized_singular_values(yu_adj @ g_inv_sqrt)
    down_after = normalized_singular_values(yd_adj @ g_inv_sqrt)

    ckm_delta = float(np.linalg.norm(ckm_after - ckm_before))
    mass_err = float(np.linalg.norm(np.log(up_after / target_u)) + np.linalg.norm(np.log(down_after / target_d)))

    gates = [
        Gate("paper saved", "PASS" if "Right-Eigenchannel Mass-Layer" in paper else "FAIL", "right-eigenchannel theorem present"),
        Gate("requirements imported", "PASS" if "A_u ~= 4.55" in req else "FAIL", "mass requirements imported"),
        Gate("CKM preserved", "PASS" if ckm_delta < 1e-10 else "FAIL", f"||Delta CKM||={ckm_delta:.3e}"),
        Gate("mass ratios matched", "PASS" if mass_err < 1e-10 else "FAIL", f"log mass error={mass_err:.3e}"),
        Gate("actions positive", "PASS" if np.all(au[:2] > 0) and np.all(ad[:2] > 0) else "FAIL", f"A_u={au}, A_d={ad}"),
        Gate("geometric source", "OPEN", "derive right-eigenchannel actions from Sigma_MTT"),
    ]

    print("Right-eigenchannel mass-layer theorem check")
    print("===========================================")
    print()
    print(f"CKM delta after right-eigenchannel action: {ckm_delta:.12e}")
    print(f"log mass-ratio error: {mass_err:.12e}")
    print("actions:")
    print("  A_u: " + " ".join(f"{x:.6f}" for x in au))
    print("  A_d: " + " ".join(f"{x:.6f}" for x in ad))
    print("adjusted normalized singular values:")
    print("  up:   " + " ".join(f"{x:.8f}" for x in up_after))
    print("  down: " + " ".join(f"{x:.8f}" for x in down_after))
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
