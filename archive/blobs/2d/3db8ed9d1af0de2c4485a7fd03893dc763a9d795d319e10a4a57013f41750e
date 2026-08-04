"""Check the finite right-channel assignment extraction target."""

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


def spectral_projectors(k: np.ndarray) -> list[np.ndarray]:
    values, vectors = np.linalg.eigh(k)
    idx = np.argsort(values)
    vectors = vectors[:, idx]
    return [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]


def tr(p: np.ndarray, s: np.ndarray) -> float:
    return float(np.real_if_close(np.trace(p @ s)))


def comm(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a @ b - b @ a))


def main() -> None:
    paper = read(ROOT / "Finite_Right_Channel_Assignment_Extraction_Target_v1.md")
    up_label = read(ROOT / "Up_Retarded_Spinorial_Right_Channel_Label_Theorem_v1.md")
    down_label = read(ROOT / "Down_Dyadic_Nil_Right_Channel_Label_Theorem_v1.md")
    projector_reduction = read(ROOT / "Right_Channel_Projector_Selection_Reduction_v1.md")

    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    ku = (yu @ g_inv_sqrt).conj().T @ (yu @ g_inv_sqrt)
    kd = (yd @ g_inv_sqrt).conj().T @ (yd @ g_inv_sqrt)
    pu = spectral_projectors(ku)
    pd = spectral_projectors(kd)

    # These are formal target observables.  The open step is to compute them
    # from Sigma_MTT rather than define them from the projectors.
    s_u_spin_target = -pu[0] + pu[1]
    s_d_dyad_target = pd[0]
    s_d_nil_target = pd[1]

    up_trace = np.array([tr(pu[0], s_u_spin_target), tr(pu[1], s_u_spin_target)])
    down_trace = np.array(
        [
            [tr(pd[0], s_d_dyad_target), tr(pd[1], s_d_dyad_target)],
            [tr(pd[0], s_d_nil_target), tr(pd[1], s_d_nil_target)],
        ]
    )
    up_expected = np.array([-1.0, 1.0])
    down_expected = np.array([[1.0, 0.0], [0.0, 1.0]])
    trace_error = float(np.linalg.norm(up_trace - up_expected) + np.linalg.norm(down_trace - down_expected))
    comm_error = comm(s_u_spin_target, ku) + comm(s_d_dyad_target, kd) + comm(s_d_nil_target, kd)

    j = LAMBDA_NIL / LAMBDA_LENS
    up_labels = j * (-0.5 + up_trace)
    down_labels = np.array([down_trace[0, 0] / 64.0, 1.5 * LAMBDA_NIL * down_trace[1, 1]])

    gates = [
        Gate("paper saved", "PASS" if "Finite Right-Channel Assignment Extraction Target" in paper else "FAIL", "assignment target present"),
        Gate("up theorem imported", "PASS" if "spec_light(R_u)" in up_label else "FAIL", "up finite label theorem imported"),
        Gate("down theorem imported", "PASS" if "spec_light(R_d)" in down_label else "FAIL", "down finite label theorem imported"),
        Gate("projector uniqueness imported", "PASS" if "projectors are not" in projector_reduction else "FAIL", "projector reduction imported"),
        Gate("trace table target", "PASS" if trace_error < 1e-12 else "FAIL", f"trace error={trace_error:.3e}"),
        Gate("target observables commute", "PASS" if comm_error < 1e-10 else "FAIL", f"commutator sum={comm_error:.3e}"),
        Gate("label reconstruction", "PASS" if abs(up_labels[0] + 1.5 * j) < 1e-12 and abs(down_labels[0] - 1.0 / 64.0) < 1e-12 else "FAIL", "labels reconstruct from traces"),
        Gate("Sigma_MTT extraction", "OPEN", "compute these observables from actual selected source map"),
    ]

    print("Finite right-channel assignment extraction target check")
    print("=======================================================")
    print()
    print("target trace table:")
    print(f"  up spin:       {up_trace[0]:+.6f} {up_trace[1]:+.6f}")
    print(f"  down dyad row: {down_trace[0,0]:+.6f} {down_trace[0,1]:+.6f}")
    print(f"  down nil row:  {down_trace[1,0]:+.6f} {down_trace[1,1]:+.6f}")
    print("reconstructed residual labels:")
    print("  up:   " + " ".join(f"{x:+.12f}" for x in up_labels))
    print("  down: " + " ".join(f"{x:+.12f}" for x in down_labels))
    print(f"trace error:      {trace_error:.12e}")
    print(f"commutator error: {comm_error:.12e}")
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
