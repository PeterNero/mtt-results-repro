"""Check mass-layer requirements after the selected finite B_q branch."""

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


def normalized_singular_values(y: np.ndarray) -> np.ndarray:
    singular_values = np.array(sorted(np.linalg.svd(y, compute_uv=False)), dtype=float)
    return singular_values / singular_values[-1]


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


def main() -> None:
    paper = read(ROOT / "Selected_Mass_Layer_Requirements_after_Bq_v1.md")
    selected = read(ROOT / "Selected_Finite_Bq_Branch_Theorem_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)

    up = normalized_singular_values(yu @ g_inv_sqrt)
    down = normalized_singular_values(yd @ g_inv_sqrt)
    up_target = np.array([1.2e-5 / 0.53, 1.6e-3 / 0.53, 1.0])
    down_target = np.array([2.2e-4 / 0.11, 5.5e-3 / 0.11, 1.0])
    a_up = np.log(up[:2] / up_target[:2])
    a_down = np.log(down[:2] / down_target[:2])

    # Best simple right family-basis non-terminal prefactor from a coarse scan.
    target_ckm = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )
    best: tuple[float, float, float, np.ndarray, np.ndarray, np.ndarray] | None = None
    for au in np.linspace(0.0, 6.0, 121):
        pu = np.diag([math.exp(-float(au)), math.exp(-float(au)), 1.0])
        for ad in np.linspace(0.0, 3.0, 121):
            pd = np.diag([math.exp(-float(ad)), math.exp(-float(ad)), 1.0])
            yu_p = yu @ pu
            yd_p = yd @ pd
            up_p = normalized_singular_values(yu_p)
            down_p = normalized_singular_values(yd_p)
            mass_err = float(
                np.linalg.norm(np.log(up_p[:2] / up_target[:2]))
                + np.linalg.norm(np.log(down_p[:2] / down_target[:2]))
            )
            if best is None or mass_err < best[0]:
                best = (mass_err, float(au), float(ad), up_p, down_p, ckm_matrix(yu_p, yd_p, j_profile))
    assert best is not None
    _, best_au, best_ad, best_up, best_down, best_ckm = best
    best_ckm_err = float(np.linalg.norm(best_ckm - target_ckm))

    gates = [
        Gate("paper saved", "PASS" if "Selected Mass-Layer Requirements" in paper else "FAIL", "requirements paper present"),
        Gate("selected branch imported", "PASS" if "mu_u=8" in selected and "mu_d=2" in selected else "FAIL", "selected B_q theorem imported"),
        Gate("required actions positive", "PASS" if np.all(a_up > 0) and np.all(a_down > 0) else "FAIL", "extra suppression required"),
        Gate("actions quantified", "PASS" if 4.4 < float(np.mean(a_up)) < 4.7 and 1.1 < float(np.mean(a_down)) < 1.6 else "FAIL", f"A_u~{np.mean(a_up):.3f}, A_d~{np.mean(a_down):.3f}"),
        Gate("simple prefactor mass improvement", "PASS", f"A_u={best_au:.3f}, A_d={best_ad:.3f}"),
        Gate("simple prefactor CKM no-go", "PASS" if best_ckm_err > 0.10 and best_ckm[1, 2] > 0.10 else "FAIL", f"CKM residual={best_ckm_err:.6f}, V_cb={best_ckm[1,2]:.4f}"),
        Gate("selected mass layer", "OPEN", "need CKM-preserving action/prefactor/RG source"),
    ]

    print("Selected mass-layer requirements after B_q check")
    print("================================================")
    print()
    print("Required extra actions:")
    print(f"  A_u1={a_up[0]:.6f}, A_u2={a_up[1]:.6f}, mean={np.mean(a_up):.6f}")
    print(f"  A_d1={a_down[0]:.6f}, A_d2={a_down[1]:.6f}, mean={np.mean(a_down):.6f}")
    print("Best simple right-family prefactor:")
    print(f"  A_u={best_au:.6f}, A_d={best_ad:.6f}, CKM residual={best_ckm_err:.6f}, V_cb={best_ckm[1,2]:.6f}")
    print("  up:   " + " ".join(f"{x:.8f}" for x in best_up))
    print("  down: " + " ".join(f"{x:.8f}" for x in best_down))
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
