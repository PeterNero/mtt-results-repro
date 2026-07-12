"""Scan simple family-basis observables for right-channel label assignment."""

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


@dataclass(frozen=True)
class Row:
    name: str
    comm_u: float
    comm_d: float
    up_trace: np.ndarray
    down_trace: np.ndarray
    score: float


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


def projectors(k: np.ndarray) -> list[np.ndarray]:
    values, vectors = np.linalg.eigh(k)
    idx = np.argsort(values)
    vectors = vectors[:, idx]
    return [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]


def traces(ps: list[np.ndarray], a: np.ndarray) -> np.ndarray:
    return np.array([float(np.real_if_close(np.trace(ps[i] @ a))) for i in range(2)], dtype=float)


def comm(a: np.ndarray, k: np.ndarray) -> float:
    return float(np.linalg.norm(a @ k - k @ a))


def main() -> None:
    paper = read(ROOT / "Right_Channel_Label_Observable_Dictionary_Scan_v1.md")
    assignment = read(ROOT / "Finite_Right_Channel_Assignment_Extraction_Target_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    ku = (yu @ g_inv_sqrt).conj().T @ (yu @ g_inv_sqrt)
    kd = (yd @ g_inv_sqrt).conj().T @ (yd @ g_inv_sqrt)
    pu = projectors(ku)
    pd = projectors(kd)

    shift = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    omega = np.exp(2j * np.pi / 3)
    clock = np.diag([1.0, omega, omega * omega])
    raw_ops = {
        "I": np.eye(3),
        "Jdiag": np.diag(j_profile),
        "family_index": np.diag([0.0, 1.0, 2.0]),
        "spin_diag_-+0": np.diag([-1.0, 1.0, 0.0]),
        "spin_diag_0-+": np.diag([0.0, -1.0, 1.0]),
        "basis0": np.diag([1.0, 0.0, 0.0]),
        "basis1": np.diag([0.0, 1.0, 0.0]),
        "basis2": np.diag([0.0, 0.0, 1.0]),
        "Z3_lap": 3.0 * np.eye(3) - shift - shift.conj().T,
        "shift_cos": (shift + shift.conj().T) / 2.0,
        "shift_sin": (shift - shift.conj().T) / (2.0j),
        "clock_real": (clock + clock.conj().T) / 2.0,
        "clock_imag": (clock - clock.conj().T) / (2.0j),
    }

    rows: list[Row] = []
    target_up = np.array([-1.0, 1.0])
    target_down_dyad = np.array([1.0, 0.0])
    for name, op in raw_ops.items():
        a = np.asarray((op + op.conj().T) / 2.0, dtype=complex)
        up_t = traces(pu, a)
        down_t = traces(pd, a)
        cu = comm(a, ku)
        cd = comm(a, kd)
        score = cu + cd + min(
            float(np.linalg.norm(up_t - target_up)),
            float(np.linalg.norm(down_t - target_down_dyad)),
        )
        rows.append(Row(name, cu, cd, up_t, down_t, score))
    rows.sort(key=lambda row: row.score)

    passing = [
        row
        for row in rows
        if row.comm_u < 1e-8
        and row.comm_d < 1e-8
        and (
            np.linalg.norm(row.up_trace - target_up) < 1e-8
            or np.linalg.norm(row.down_trace - target_down_dyad) < 1e-8
        )
    ]

    gates = [
        Gate("paper saved", "PASS" if "Right-Channel Label Observable Dictionary Scan" in paper else "FAIL", "dictionary scan note present"),
        Gate("assignment target imported", "PASS" if "S_u^spin" in assignment and "S_d^dyad" in assignment else "FAIL", "assignment target imported"),
        Gate("dictionary nonempty", "PASS" if len(rows) >= 10 else "FAIL", f"{len(rows)} observables tested"),
        Gate("raw exact source", "NO-GO" if not passing else "PASS", f"exact passing raw observables={len(passing)}"),
        Gate("next route", "OPEN", "construct Schur/Riesz-projected source observable from Sigma_MTT"),
    ]

    print("Right-channel label observable dictionary scan")
    print("==============================================")
    print()
    print("Top raw observables by loose diagnostic score:")
    for row in rows[:8]:
        print(
            f"  {row.name:16s} "
            f"comm_u={row.comm_u:.3e} comm_d={row.comm_d:.3e} "
            f"up=({row.up_trace[0]:+.3f},{row.up_trace[1]:+.3f}) "
            f"down=({row.down_trace[0]:+.3f},{row.down_trace[1]:+.3f}) "
            f"score={row.score:.3e}"
        )
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
