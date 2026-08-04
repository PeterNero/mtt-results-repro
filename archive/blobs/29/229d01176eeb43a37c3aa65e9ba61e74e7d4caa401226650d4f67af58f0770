"""Check the right-channel projector selection reduction."""

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


def spectral_projectors(k: np.ndarray) -> tuple[np.ndarray, list[np.ndarray]]:
    values, vectors = np.linalg.eigh(k)
    idx = np.argsort(values)
    values = values[idx]
    vectors = vectors[:, idx]
    projectors = [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]
    return values, projectors


def projector_errors(projectors: list[np.ndarray]) -> tuple[float, float]:
    idem = sum(float(np.linalg.norm(p @ p - p)) for p in projectors)
    orth = 0.0
    for i, p in enumerate(projectors):
        for j, q in enumerate(projectors):
            if i != j:
                orth += float(np.linalg.norm(p @ q))
    return idem, orth


def lagrange_projector(k: np.ndarray, values: np.ndarray, a: int) -> np.ndarray:
    eye = np.eye(k.shape[0], dtype=complex)
    out = eye.copy()
    for b, kb in enumerate(values):
        if b == a:
            continue
        out = out @ ((k - kb * eye) / (values[a] - kb))
    return out


def main() -> None:
    paper = read(ROOT / "Right_Channel_Projector_Selection_Reduction_v1.md")
    source_schema = read(ROOT / "Finite_Label_Right_Channel_Source_Operator_Schema_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    ku = (yu @ g_inv_sqrt).conj().T @ (yu @ g_inv_sqrt)
    kd = (yd @ g_inv_sqrt).conj().T @ (yd @ g_inv_sqrt)

    evals_u, projs_u = spectral_projectors(ku)
    evals_d, projs_d = spectral_projectors(kd)
    min_gap_u = float(np.min(np.diff(evals_u)))
    min_gap_d = float(np.min(np.diff(evals_d)))
    idem_u, orth_u = projector_errors(projs_u)
    idem_d, orth_d = projector_errors(projs_d)

    lagrange_err = 0.0
    for a in range(3):
        lagrange_err += float(np.linalg.norm(lagrange_projector(ku, evals_u, a) - projs_u[a]))
        lagrange_err += float(np.linalg.norm(lagrange_projector(kd, evals_d, a) - projs_d[a]))

    j = LAMBDA_NIL / LAMBDA_LENS
    ru = j * (-1.5 * projs_u[0] + 0.5 * projs_u[1])
    rd = (1.0 / 64.0) * projs_d[0] + (1.5 * LAMBDA_NIL) * projs_d[1]
    comm_err = float(np.linalg.norm(ru @ ku - ku @ ru) + np.linalg.norm(rd @ kd - kd @ rd))

    gates = [
        Gate("paper saved", "PASS" if "Right-Channel Projector Selection Reduction" in paper else "FAIL", "projector reduction paper present"),
        Gate("source schema imported", "PASS" if "Xi_u" in source_schema and "P_dyad" in source_schema else "FAIL", "finite-label source schema imported"),
        Gate("up spectrum simple", "PASS" if min_gap_u > 1e-10 else "FAIL", f"min gap={min_gap_u:.3e}"),
        Gate("down spectrum simple", "PASS" if min_gap_d > 1e-10 else "FAIL", f"min gap={min_gap_d:.3e}"),
        Gate("projectors valid", "PASS" if idem_u + orth_u + idem_d + orth_d < 1e-12 else "FAIL", f"idempotent+orth error={idem_u+orth_u+idem_d+orth_d:.3e}"),
        Gate("Lagrange uniqueness", "PASS" if lagrange_err < 1e-10 else "FAIL", f"Lagrange projector error={lagrange_err:.3e}"),
        Gate("commuting source", "PASS" if comm_err < 1e-10 else "FAIL", f"commutator sum={comm_err:.3e}"),
        Gate("finite labels", "OPEN", "derive label assignment from Sigma_MTT"),
    ]

    print("Right-channel projector selection reduction check")
    print("=================================================")
    print()
    print("K_u eigenvalues: " + " ".join(f"{x:.12e}" for x in evals_u))
    print("K_d eigenvalues: " + " ".join(f"{x:.12e}" for x in evals_d))
    print(f"min gaps: up={min_gap_u:.12e}, down={min_gap_d:.12e}")
    print(f"projector idempotent/orthogonal error: {idem_u+orth_u+idem_d+orth_d:.12e}")
    print(f"Lagrange uniqueness error:             {lagrange_err:.12e}")
    print(f"commuting source error:                {comm_err:.12e}")
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
