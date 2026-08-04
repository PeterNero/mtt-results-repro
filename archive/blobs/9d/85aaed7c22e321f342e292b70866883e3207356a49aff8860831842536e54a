"""Diagnostic for the lean canonical anchored-bridge seed.

This script intentionally uses no observed masses or CKM angles as inputs.
It tests the fully specified structural seed obtained from:

  J=(0, lambda_nil/lambda_lens, 1),
  C_u[b]=exp(-J_b) tau^b,
  C_d[b]=exp(-J_b) tau^(2b),
  G_A^{-1}=diag(exp(-2J_b)).

The output is compared qualitatively to CKM only after computation.
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


def main() -> None:
    paper = read(ROOT / "Canonical_Anchored_Bridge_Seed_Diagnostic_v1.md")
    tau = cmath.exp(2j * math.pi * Q / N)
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))

    cu = np.exp(-j_profile) * np.array([tau**b for b in range(3)], dtype=complex)
    cd = np.exp(-j_profile) * np.array([tau ** (2 * b) for b in range(3)], dtype=complex)
    yu = bridge_matrix(cu)
    yd = bridge_matrix(cd)

    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    vu, uu = sorted_eigh(hu)
    vd, ud = sorted_eigh(hd)
    v_seed = uu.conj().T @ ud
    abs_v = np.abs(v_seed)
    comm = np.linalg.norm(hu @ hd - hd @ hu)

    # Broad qualitative CKM sanity thresholds, used only after the seed is fixed.
    ckm_like = abs_v[0, 0] > 0.9 and abs_v[0, 1] < 0.35 and abs_v[0, 2] < 0.05 and abs_v[1, 2] < 0.08
    large_mixing = abs_v[0, 1] > 0.5 or abs_v[1, 2] > 0.3

    gates = [
        Gate("paper saved", "PASS" if "Universal Seed Is Not Quark-Closed" in paper else "FAIL", "diagnostic theorem present"),
        Gate("q79 phase source", "PASS" if N // math.gcd(Q, N) == 448 else "FAIL", "tau has exact order 448"),
        Gate("no empirical inputs", "PASS", "seed uses J and q79 only"),
        Gate("nonzero commutator", "PASS" if comm > 1e-3 else "FAIL", f"||[Hu,Hd]||={comm:.6e}"),
        Gate("large mixing", "PASS" if large_mixing else "FAIL", f"|V01|={abs_v[0,1]:.4f}, |V12|={abs_v[1,2]:.4f}"),
        Gate("not CKM-like", "PASS" if not ckm_like else "FAIL", "seed should be diagnosed as not quark-closed"),
        Gate("next source", "OPEN", "derive quark stiffness or bridge hierarchy from Sigma_MTT"),
    ]

    print("Canonical anchored-bridge seed diagnostic")
    print("=========================================")
    print()
    print(f"J profile: {[round(float(x), 6) for x in j_profile]}")
    print(f"Hu eigenvalues: {[round(float(x), 6) for x in vu]}")
    print(f"Hd eigenvalues: {[round(float(x), 6) for x in vd]}")
    print(f"commutator norm: {comm:.12e}")
    print("|V_seed|:")
    for row in abs_v:
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
