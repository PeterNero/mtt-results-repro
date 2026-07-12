"""Check the finite-label right-channel source-operator schema."""

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


def right_gram_projectors(y: np.ndarray, g_inv_sqrt: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    z = y @ g_inv_sqrt
    k = z.conj().T @ z
    values, vectors = np.linalg.eigh(k)
    idx = np.argsort(values)
    vectors = vectors[:, idx]
    projectors = [np.outer(vectors[:, i], vectors[:, i].conj()) for i in range(3)]
    return k, projectors[0], projectors[1], projectors[2]


def hermitian_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a - a.conj().T))


def commutator_norm(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a @ b - b @ a))


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


def apply_right_operator(y: np.ndarray, action_eigs_light: np.ndarray, g_inv_sqrt: np.ndarray, g_sqrt: np.ndarray) -> np.ndarray:
    z = y @ g_inv_sqrt
    u, singular_values, vh = np.linalg.svd(z, full_matrices=True)
    actions_desc = np.array([0.0, action_eigs_light[1], action_eigs_light[0]], dtype=float)
    adjusted_z = u @ np.diag(singular_values * np.exp(-actions_desc)) @ vh
    return adjusted_z @ g_sqrt


def main() -> None:
    paper = read(ROOT / "Finite_Label_Right_Channel_Source_Operator_Schema_v1.md")
    candidate = read(ROOT / "Finite_Label_Right_Channel_Mass_Operator_Candidate_v1.md")
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    tau = cmath.exp(2j * math.pi * Q / N)
    yu = y_selected(8.0, 1, j_profile, tau)
    yd = y_selected(2.0, 2, j_profile, tau)
    g_inv_sqrt = np.diag(np.exp(-1.0 * j_profile))
    g_sqrt = np.diag(np.exp(1.0 * j_profile))

    ku, pu1, pu2, _pu3 = right_gram_projectors(yu, g_inv_sqrt)
    kd, pd1, pd2, _pd3 = right_gram_projectors(yd, g_inv_sqrt)
    j = LAMBDA_NIL / LAMBDA_LENS
    iu_light = pu1 + pu2
    xi_u = -pu1 + pu2
    r_u = j * (-0.5 * iu_light + xi_u)
    r_d = (1.0 / 64.0) * pd1 + (1.5 * LAMBDA_NIL) * pd2

    eig_ru = np.linalg.eigvalsh(r_u)
    eig_rd = np.linalg.eigvalsh(r_d)
    expected_ru = np.array([-1.5 * j, 0.0, 0.5 * j])
    expected_rd = np.array([0.0, 1.0 / 64.0, 1.5 * LAMBDA_NIL])
    eig_err = float(np.linalg.norm(np.sort(eig_ru) - expected_ru) + np.linalg.norm(np.sort(eig_rd) - expected_rd))
    comm_err = commutator_norm(r_u, ku) + commutator_norm(r_d, kd)
    herm_err = hermitian_norm(r_u) + hermitian_norm(r_d)

    au_light = np.array([4.0 * math.log(math.pi) - 1.5 * j, 4.0 * math.log(math.pi) + 0.5 * j])
    ad_light = np.array([math.log(math.pi) + 1.0 / 64.0, math.log(math.pi) + 1.5 * LAMBDA_NIL])
    ckm_before = ckm_matrix(yu, yd, j_profile)
    ckm_after = ckm_matrix(
        apply_right_operator(yu, au_light, g_inv_sqrt, g_sqrt),
        apply_right_operator(yd, ad_light, g_inv_sqrt, g_sqrt),
        j_profile,
    )
    ckm_delta = float(np.linalg.norm(ckm_after - ckm_before))

    gates = [
        Gate("paper saved", "PASS" if "Finite-Label Right-Channel Source Operator" in paper else "FAIL", "operator schema present"),
        Gate("candidate imported", "PASS" if "eig(R_u)" in candidate and "eig(R_d)" in candidate else "FAIL", "finite-label candidate imported"),
        Gate("Hermitian operators", "PASS" if herm_err < 1e-12 else "FAIL", f"||R-R*|| sum={herm_err:.3e}"),
        Gate("right Gram commutation", "PASS" if comm_err < 1e-10 else "FAIL", f"commutator sum={comm_err:.3e}"),
        Gate("finite eigenvalues", "PASS" if eig_err < 1e-12 else "FAIL", f"eigenvalue error={eig_err:.3e}"),
        Gate("CKM preserved", "PASS" if ckm_delta < 1e-10 else "FAIL", f"||Delta CKM||={ckm_delta:.3e}"),
        Gate("projector selection", "OPEN", "identify Xi_u, P_dyad, P_nil from Sigma_MTT"),
    ]

    print("Finite-label right-channel source-operator schema check")
    print("=======================================================")
    print()
    print(f"J=lambda_nil/lambda_lens={j:.12f}")
    print("R_u eigenvalues: " + " ".join(f"{x:.12f}" for x in np.sort(eig_ru)))
    print("expected:        " + " ".join(f"{x:.12f}" for x in expected_ru))
    print("R_d eigenvalues: " + " ".join(f"{x:.12f}" for x in np.sort(eig_rd)))
    print("expected:        " + " ".join(f"{x:.12f}" for x in expected_rd))
    print(f"Hermitian error: {herm_err:.12e}")
    print(f"Commutator sum:  {comm_err:.12e}")
    print(f"CKM delta:       {ckm_delta:.12e}")
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
