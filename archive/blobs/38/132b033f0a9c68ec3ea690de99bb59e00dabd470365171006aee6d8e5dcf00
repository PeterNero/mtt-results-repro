"""Scan scalar quark stiffness in the anchored bridge seed.

This is a diagnostic no-go, not a fit.  CKM values are used only after the
structural family is defined, to test whether the two-scale stiffness family
can be CKM-like.
"""

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


def bridge_matrix(weights: np.ndarray) -> np.ndarray:
    return np.array([[weights[(-(i + j)) % 3] for j in range(3)] for i in range(3)], dtype=complex)


def sorted_eigh(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(h)
    idx = np.argsort(values)
    return values[idx], vectors[:, idx]


def mixing(mu_u: float, mu_d: float, j_profile: np.ndarray, g_inv: np.ndarray, tau: complex) -> np.ndarray:
    cu = np.exp(-mu_u * j_profile) * np.array([tau**b for b in range(3)], dtype=complex)
    cd = np.exp(-mu_d * j_profile) * np.array([tau ** (2 * b) for b in range(3)], dtype=complex)
    yu = bridge_matrix(cu)
    yd = bridge_matrix(cd)
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    return np.abs(uu.conj().T @ ud)


def main() -> None:
    paper = read(ROOT / "Scalar_Quark_Stiffness_Diagnostic_NoGo_v1.md")
    tau = cmath.exp(2j * math.pi * Q / N)
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    target = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )

    best = (float("inf"), None, None, None)
    for mu_u in np.linspace(0.1, 12.0, 120):
        for mu_d in np.linspace(0.1, 12.0, 120):
            mat = mixing(float(mu_u), float(mu_d), j_profile, g_inv, tau)
            err = float(np.linalg.norm(mat - target))
            if err < best[0]:
                best = (err, float(mu_u), float(mu_d), mat)

    err, mu_u, mu_d, mat = best
    ckm_like = mat[0, 0] > 0.9 and mat[0, 1] < 0.35 and mat[0, 2] < 0.05 and mat[1, 2] < 0.08
    still_large = mat[0, 1] > 0.45 or mat[1, 2] > 0.3

    gates = [
        Gate("paper saved", "PASS" if "Scalar Quark-Stiffness Diagnostic No-Go" in paper else "FAIL", "diagnostic paper present"),
        Gate("q79 phase source", "PASS" if N // math.gcd(Q, N) == 448 else "FAIL", "tau has exact order 448"),
        Gate("scan completed", "PASS", f"best mu_u={mu_u:.3f}, mu_d={mu_d:.3f}, error={err:.3f}"),
        Gate("not CKM-like", "PASS" if not ckm_like else "FAIL", "two-scale family should not pass CKM accidentally"),
        Gate("still large mixing", "PASS" if still_large else "FAIL", f"|V01|={mat[0,1]:.3f}, |V12|={mat[1,2]:.3f}"),
        Gate("structured source needed", "OPEN", "derive localization/channel geometry beyond scalar stiffness"),
    ]

    print("Scalar quark-stiffness diagnostic scan")
    print("======================================")
    print()
    print(f"best mu_u={mu_u:.6f}, mu_d={mu_d:.6f}, error={err:.6f}")
    print("best |V|:")
    for row in mat:
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
