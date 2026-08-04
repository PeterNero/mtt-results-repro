"""Test sibling primitive C1 rows as right-channel label source adapters."""

from __future__ import annotations

import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SMP = TEXPAPERS / "mtt-sm-parity-closure"

Q = 79
N = 448
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25

PRIMITIVE_ROWS = (
    SMP
    / "candidate_data"
    / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
    / "inputs"
    / "primitive_contraction_terms.packet.json"
)
ZERO_MODE_BASIS = (
    SMP
    / "candidate_data"
    / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
    / "inputs"
    / "zero_mode_basis.packet.json"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported primitive row value: {value!r}")


def row_matrix(rows: list[dict[str, Any]], sector: str, response: str) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    for row in rows:
        if row.get("sector") == sector and row.get("response") == response:
            coordinate = row["coordinate"]
            i = int(coordinate[1])
            j = int(coordinate[3])
            matrix[i, j] = to_complex(row["value"])
    return matrix


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


def right_projectors(mu: float, phase_shift: int) -> list[np.ndarray]:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    y = y_selected(mu, phase_shift, j_profile, tau)
    z = y @ g_inv_sqrt
    k = z.conj().T @ z
    values, vectors = np.linalg.eigh(k)
    idx = np.argsort(values)
    vectors = vectors[:, idx]
    return [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]


def projected_traces(projectors: list[np.ndarray], matrix: np.ndarray) -> np.ndarray:
    return np.array([float(np.real_if_close(np.trace(p @ matrix))) for p in projectors], dtype=float)


def best_affine_fit(values: np.ndarray, target: np.ndarray) -> tuple[float, float, float]:
    design = np.column_stack([values, np.ones_like(values)])
    scale, offset = np.linalg.lstsq(design, target, rcond=None)[0]
    residual = float(np.linalg.norm(scale * values + offset - target))
    return float(scale), float(offset), residual


def main() -> None:
    note = read_text(ROOT / "Cross_Repo_Primitive_Row_Adapter_for_Right_Channel_Labels_v1.md")
    primitive = load_json(PRIMITIVE_ROWS)
    basis = load_json(ZERO_MODE_BASIS)
    rows = primitive["rows"]

    matrices = {
        (sector, response): (row_matrix(rows, sector, response) + row_matrix(rows, sector, response).conj().T) / 2.0
        for sector in ("u", "d")
        for response in ("phase", "shift")
    }
    pu = right_projectors(8.0, 1)
    pd = right_projectors(2.0, 2)

    up_target = np.array([-1.0, 1.0], dtype=float)
    down_dyad_target = np.array([1.0, 0.0], dtype=float)
    down_nil_target = np.array([0.0, 1.0], dtype=float)

    up_traces = projected_traces(pu, matrices[("u", "phase")])[:2]
    down_traces = projected_traces(pd, matrices[("d", "phase")])[:2]
    up_scale, up_offset, up_residual = best_affine_fit(up_traces, up_target)
    dyad_scale, dyad_offset, dyad_residual = best_affine_fit(down_traces, down_dyad_target)
    nil_scale, nil_offset, nil_residual = best_affine_fit(down_traces, down_nil_target)

    source_flags = [
        bool(row.get("selected_emitted")) or bool(row.get("source_owner_verified"))
        for row in rows
        if row.get("sector") in {"u", "d"}
    ]
    support_only = not any(source_flags)

    gates = [
        Gate("adapter note saved", "PASS" if "Cross-Repo Primitive Row Adapter" in note else "FAIL", "adapter note present"),
        Gate("primitive rows found", "PASS" if primitive.get("schema") else "FAIL", primitive.get("status", "missing")),
        Gate("zero-mode basis found", "PASS" if basis.get("basis_dimension") == 9 else "FAIL", basis.get("status", "missing")),
        Gate("u/d matrix rows present", "PASS" if all(np.linalg.norm(m) > 0 for m in matrices.values()) else "FAIL", "u,d phase/shift matrices reconstruct"),
        Gate("source promotion", "SUPPORT-ONLY" if support_only else "PASS", "all imported u/d rows have selected_emitted=false and source_owner_verified=false"),
        Gate("up affine trace adapter", "DIAGNOSTIC" if up_residual < 1e-8 else "NO-GO", f"scale={up_scale:+.12g}, offset={up_offset:+.12g}, residual={up_residual:.3e}"),
        Gate("down dyad affine adapter", "DIAGNOSTIC" if dyad_residual < 1e-8 else "NO-GO", f"scale={dyad_scale:+.12g}, offset={dyad_offset:+.12g}, residual={dyad_residual:.3e}"),
        Gate("down nil affine adapter", "DIAGNOSTIC" if nil_residual < 1e-8 else "NO-GO", f"scale={nil_scale:+.12g}, offset={nil_offset:+.12g}, residual={nil_residual:.3e}"),
        Gate("proof-source status", "OPEN", "needs independent selected source/provenance before importing any adapter labels"),
    ]

    print("Cross-repo primitive row adapter right-label check")
    print("==================================================")
    print()
    for key, matrix in matrices.items():
        eig = np.linalg.eigvalsh(matrix)
        traces = projected_traces(pu if key[0] == "u" else pd, matrix)
        print(
            f"{key[0]}:{key[1]} "
            f"eig=({eig[0]:+.6f},{eig[1]:+.6f},{eig[2]:+.6f}) "
            f"proj=({traces[0]:+.6f},{traces[1]:+.6f},{traces[2]:+.6f})"
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
