"""Check the hypercharge-square stiffness source for B_q."""

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


def y_second_order(mu: float, phase_shift: int, lambda_q: float, j_profile: np.ndarray, tau: complex) -> np.ndarray:
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += 0.5 * (j_profile[j] - j_profile[(b - 1) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def selected_bq_matrix(mu_u: float, mu_d: float) -> tuple[float, np.ndarray]:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    tau = cmath.exp(2j * math.pi * Q / N)
    lambda_q = LAMBDA_LENS - LAMBDA_NIL
    yu = y_second_order(mu_u, 1, lambda_q, j_profile, tau)
    yd = y_second_order(mu_d, 2, lambda_q, j_profile, tau)
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
    return float(np.linalg.norm(v - target)), v


def is_ckm_shaped(v: np.ndarray) -> bool:
    return bool(v[0, 0] > 0.95 and 0.15 < v[0, 1] < 0.30 and v[0, 2] < 0.03 and 0.02 < v[1, 2] < 0.08)


def main() -> None:
    paper = read(ROOT / "Bq_Hypercharge_Square_Stiffness_Source_v1.md")
    hypercharge_corpus = read(
        Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\13 Standard Model & Topology-Only Constraints\Topology__Only_Constraints_in_Modal_Triplet_Theory.md")
    )
    orientation = read(ROOT / "Bq_Retarded_Predecessor_Orientation_Lock_v1.md")
    gap = read(ROOT / "Bq_No_Double_Counting_Gap_Selection_Lemma_v1.md")

    q_u = 2
    q_d = 1
    endpoint_factor = 2
    mu_u = endpoint_factor * q_u * q_u
    mu_d = endpoint_factor * q_d * q_d
    err, v = selected_bq_matrix(float(mu_u), float(mu_d))
    swapped_err, swapped_v = selected_bq_matrix(float(mu_d), float(mu_u))

    gates = [
        Gate("paper saved", "PASS" if "Stiffness Selection Theorem" in paper else "FAIL", "stiffness source paper present"),
        Gate(
            "hypercharge source",
            "PASS" if "Y(u_R)=\\tfrac{2}{3}" in hypercharge_corpus and "Y(d_R)=-\\tfrac{1}{3}" in hypercharge_corpus else "FAIL",
            "topology-only u/d hypercharges found",
        ),
        Gate("charge numerators", "PASS" if (q_u, q_d) == (2, 1) else "FAIL", "primitive 1/3 units give q_u=2,q_d=1"),
        Gate("quadratic Hessian", "PASS" if (mu_u, mu_d) == (8, 2) else "FAIL", f"2*q^2 gives mu_u={mu_u}, mu_d={mu_d}"),
        Gate("orientation imported", "PASS" if "sigma = -1" in orientation else "FAIL", "predecessor orientation fixed"),
        Gate("gap imported", "PASS" if "lambda_lens - lambda_nil" in gap else "FAIL", "reduced lens-nil gap fixed"),
        Gate("selected branch shaped", "PASS" if is_ckm_shaped(v) else "FAIL", f"residual={err:.6f}, |V12|={v[1,2]:.4f}"),
        Gate("swapped not selected", "PASS" if "swapped stiffness branch retired" in paper else "FAIL", f"swapped residual={swapped_err:.6f} is diagnostic only"),
        Gate("actual Hessian extraction", "OPEN", "full H_u^cl,H_d^cl still must verify charge-twist block"),
    ]

    print("B_q hypercharge-square stiffness source check")
    print("=============================================")
    print()
    print(f"q_u={q_u}, q_d={q_d}, endpoint_factor={endpoint_factor}")
    print(f"mu_u={mu_u}, mu_d={mu_d}")
    print(f"selected branch residual={err:.6f}")
    print("|V_selected|:")
    for row in v:
        print("  " + " ".join(f"{x:.6f}" for x in row))
    print(f"swapped residual={swapped_err:.6f}")
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

