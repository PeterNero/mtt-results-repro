"""Check the finite-label right-channel mass operator candidate."""

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


def normalized_singular_values(z: np.ndarray) -> np.ndarray:
    s = np.array(sorted(np.linalg.svd(z, compute_uv=False)), dtype=float)
    return s / s[-1]


def right_action_adjust(y: np.ndarray, actions_light: np.ndarray, g_inv_sqrt: np.ndarray, g_sqrt: np.ndarray) -> np.ndarray:
    z = y @ g_inv_sqrt
    u, singular_values, vh = np.linalg.svd(z, full_matrices=True)
    # np.linalg.svd orders heavy, middle, light.  Actions are light, middle, heavy.
    actions_desc = np.array([actions_light[2], actions_light[1], actions_light[0]], dtype=float)
    adjusted_z = u @ np.diag(singular_values * np.exp(-actions_desc)) @ vh
    return adjusted_z @ g_sqrt


def main() -> None:
    paper = read(ROOT / "Finite_Label_Right_Channel_Mass_Operator_Candidate_v1.md")
    battery = read(ROOT / "Mass_Action_Source_Theory_Battery_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    g_sqrt = np.diag(np.exp(1.0 * j_profile))

    target_u = np.array([1.2e-5 / 0.53, 1.6e-3 / 0.53, 1.0])
    target_d = np.array([2.2e-4 / 0.11, 5.5e-3 / 0.11, 1.0])
    required_u = np.array([4.48005803, 4.61589902, 0.0], dtype=float)
    required_d = np.array([1.15867841, 1.52651629, 0.0], dtype=float)

    j = LAMBDA_NIL / LAMBDA_LENS
    candidate_u = np.array([4.0 * math.log(math.pi) - 1.5 * j, 4.0 * math.log(math.pi) + 0.5 * j, 0.0])
    candidate_d = np.array([math.log(math.pi) + 1.0 / 64.0, math.log(math.pi) + 1.5 * LAMBDA_NIL, 0.0])

    ckm_before = ckm_matrix(yu, yd, j_profile)
    yu_cand = right_action_adjust(yu, candidate_u, g_inv_sqrt, g_sqrt)
    yd_cand = right_action_adjust(yd, candidate_d, g_inv_sqrt, g_sqrt)
    ckm_after = ckm_matrix(yu_cand, yd_cand, j_profile)
    up_after = normalized_singular_values(yu_cand @ g_inv_sqrt)
    down_after = normalized_singular_values(yd_cand @ g_inv_sqrt)

    ckm_delta = float(np.linalg.norm(ckm_after - ckm_before))
    action_error = float(np.linalg.norm(candidate_u - required_u) + np.linalg.norm(candidate_d - required_d))
    mass_log_error = float(np.linalg.norm(np.log(up_after / target_u)) + np.linalg.norm(np.log(down_after / target_d)))

    gates = [
        Gate("paper saved", "PASS" if "Finite-Label Right-Channel" in paper else "FAIL", "candidate paper present"),
        Gate("battery imported", "PASS" if "finite right-channel operator route selected" in battery else "FAIL", "battery fingerprint imported"),
        Gate("CKM preserved", "PASS" if ckm_delta < 1e-10 else "FAIL", f"||Delta CKM||={ckm_delta:.3e}"),
        Gate("action error small", "PASS" if action_error < 0.02 else "FAIL", f"||Delta A|| sum={action_error:.6f}"),
        Gate("mass ratios near target", "PASS" if mass_log_error < 0.02 else "FAIL", f"log mass error={mass_log_error:.6f}"),
        Gate("operator source", "OPEN", "derive finite labels from Sigma_MTT"),
    ]

    print("Finite-label right-channel mass operator candidate check")
    print("=======================================================")
    print()
    print("candidate actions:")
    print("  A_u: " + " ".join(f"{x:.6f}" for x in candidate_u))
    print("  A_d: " + " ".join(f"{x:.6f}" for x in candidate_d))
    print("required actions:")
    print("  A_u: " + " ".join(f"{x:.6f}" for x in required_u))
    print("  A_d: " + " ".join(f"{x:.6f}" for x in required_d))
    print(f"action error sum: {action_error:.12e}")
    print(f"CKM delta:        {ckm_delta:.12e}")
    print(f"mass log error:   {mass_log_error:.12e}")
    print("candidate normalized singular values:")
    print("  up:   " + " ".join(f"{x:.8f}" for x in up_after))
    print("  down: " + " ".join(f"{x:.8f}" for x in down_after))
    print("target normalized singular values:")
    print("  up:   " + " ".join(f"{x:.8f}" for x in target_u))
    print("  down: " + " ".join(f"{x:.8f}" for x in target_d))
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
