"""Check Schur/Riesz commutant projection for right-channel labels."""

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
    _values, vectors = np.linalg.eigh(k)
    idx = np.argsort(_values)
    vectors = vectors[:, idx]
    return [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]


def expectation(projectors: list[np.ndarray], a: np.ndarray) -> np.ndarray:
    return sum((p @ a @ p for p in projectors), np.zeros_like(a, dtype=complex))


def traces(projectors: list[np.ndarray], a: np.ndarray) -> np.ndarray:
    return np.array([float(np.real_if_close(np.trace(p @ a))) for p in projectors], dtype=float)


def main() -> None:
    paper = read(ROOT / "Schur_Riesz_Commutant_Projection_for_Right_Channel_Labels_v1.md")
    scan = read(ROOT / "Right_Channel_Label_Observable_Dictionary_Scan_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    ku = (yu @ g_inv_sqrt).conj().T @ (yu @ g_inv_sqrt)
    projectors = spectral_projectors(ku)
    raw = np.diag([-1.0, 1.0, 0.0]).astype(complex)
    raw = (raw + raw.conj().T) / 2.0
    projected = expectation(projectors, raw)

    raw_comm = float(np.linalg.norm(raw @ ku - ku @ raw))
    projected_comm = float(np.linalg.norm(projected @ ku - ku @ projected))
    herm_error = float(np.linalg.norm(projected - projected.conj().T))
    trace_error = float(np.linalg.norm(traces(projectors, raw) - traces(projectors, projected)))

    gates = [
        Gate("paper saved", "PASS" if "Schur-Riesz Commutant Projection" in paper else "FAIL", "projection theorem present"),
        Gate("scan imported", "PASS" if "raw family-basis assignment source" in scan else "FAIL", "raw scan imported"),
        Gate("raw noncommutes", "PASS" if raw_comm > 1e-3 else "FAIL", f"raw commutator={raw_comm:.3e}"),
        Gate("projected commutes", "PASS" if projected_comm < 1e-10 else "FAIL", f"projected commutator={projected_comm:.3e}"),
        Gate("projected Hermitian", "PASS" if herm_error < 1e-12 else "FAIL", f"Hermitian error={herm_error:.3e}"),
        Gate("trace preserved", "PASS" if trace_error < 1e-12 else "FAIL", f"trace error={trace_error:.3e}"),
        Gate("raw label source", "OPEN", "find corpus-native raw labels with required trace table"),
    ]

    print("Schur/Riesz commutant projection right-label check")
    print("==================================================")
    print()
    print(f"raw commutator:       {raw_comm:.12e}")
    print(f"projected commutator: {projected_comm:.12e}")
    print(f"Hermitian error:      {herm_error:.12e}")
    print(f"trace preservation:   {trace_error:.12e}")
    print("raw traces:           " + " ".join(f"{x:+.6f}" for x in traces(projectors, raw)))
    print("projected traces:     " + " ".join(f"{x:+.6f}" for x in traces(projectors, projected)))
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
