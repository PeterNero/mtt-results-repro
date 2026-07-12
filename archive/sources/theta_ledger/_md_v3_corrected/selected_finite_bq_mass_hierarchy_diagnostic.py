"""Mass-hierarchy diagnostic for the selected finite B_q branch."""

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


def main() -> None:
    paper = read(ROOT / "Selected_Finite_Bq_Mass_Hierarchy_Diagnostic_v1.md")
    selected = read(ROOT / "Selected_Finite_Bq_Branch_Theorem_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    up = normalized_singular_values(y_selected(8.0, 1, j_profile, tau) @ g_inv_sqrt)
    down = normalized_singular_values(y_selected(2.0, 2, j_profile, tau) @ g_inv_sqrt)

    up_target = np.array([1.2e-5 / 0.53, 1.6e-3 / 0.53, 1.0])
    down_target = np.array([2.2e-4 / 0.11, 5.5e-3 / 0.11, 1.0])
    up_factor = up[:2] / up_target[:2]
    down_factor = down[:2] / down_target[:2]

    too_shallow = bool(np.all(up_factor > 10.0) and np.all(down_factor > 3.0))

    gates = [
        Gate("paper saved", "PASS" if "Mass-Hierarchy Diagnostic" in paper else "FAIL", "mass diagnostic paper present"),
        Gate("selected branch imported", "PASS" if "mu_u=8" in selected and "mu_d=2" in selected else "FAIL", "finite B_q branch imported"),
        Gate("hierarchical", "PASS" if up[0] < up[1] < up[2] and down[0] < down[1] < down[2] else "FAIL", "singular values are ordered"),
        Gate("not mass closed", "PASS" if too_shallow else "FAIL", "selected B_q hierarchy is too shallow"),
        Gate("mass layer needed", "OPEN", "derive action costs, prefactors, threshold/RG normalization"),
    ]

    print("Selected finite B_q mass hierarchy diagnostic")
    print("=============================================")
    print()
    print("canonical weighted normalized singular values:")
    print("  up:   " + " ".join(f"{x:.8f}" for x in up))
    print("  down: " + " ".join(f"{x:.8f}" for x in down))
    print("benchmark normalized targets:")
    print("  up:   " + " ".join(f"{x:.8f}" for x in up_target))
    print("  down: " + " ".join(f"{x:.8f}" for x in down_target))
    print("ratio selected/target:")
    print("  up:   " + " ".join(f"{x:.2f}" for x in up_factor))
    print("  down: " + " ".join(f"{x:.2f}" for x in down_factor))
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
