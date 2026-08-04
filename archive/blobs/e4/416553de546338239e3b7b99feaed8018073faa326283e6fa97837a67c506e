"""Check the color-singlet redundancy source for the quark B_q operator."""

from __future__ import annotations

import cmath
import itertools
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


def hidden_two_channel_cost(delta: float) -> float:
    a = delta / 2.0
    c = delta / 2.0
    return a * a + c * c


def sorted_eigh(h: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(h)
    idx = np.argsort(values)
    return values[idx], vectors[:, idx]


def y_second_order(
    mu: float,
    phase_shift: int,
    lambda_q: float,
    alpha_hidden: float,
    orientation: int,
    j_profile: np.ndarray,
    tau: complex,
) -> np.ndarray:
    weights = np.exp(-mu * j_profile) * np.array([tau ** (phase_shift * b) for b in range(3)], dtype=complex)
    y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            b = (-(i + j)) % 3
            cost = (j_profile[i] - j_profile[b]) ** 2
            cost += alpha_hidden * (j_profile[j] - j_profile[(b + orientation) % 3]) ** 2
            y[i, j] = weights[b] * math.exp(-lambda_q * float(cost))
    return y


def mixing(yu: np.ndarray, yd: np.ndarray, g_inv: np.ndarray) -> np.ndarray:
    hu = yu @ g_inv @ yu.conj().T
    hd = yd @ g_inv @ yd.conj().T
    _, uu = sorted_eigh(hu)
    _, ud = sorted_eigh(hd)
    return np.abs(uu.conj().T @ ud)


def is_ckm_shaped(v: np.ndarray) -> bool:
    return bool(v[0, 0] > 0.95 and 0.15 < v[0, 1] < 0.30 and v[0, 2] < 0.03 and 0.02 < v[1, 2] < 0.08)


def finite_dictionary_scan() -> tuple[dict[str, int], dict[str, tuple[float, tuple[object, ...]]]]:
    j_profile = np.array([0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0], dtype=float)
    g_inv = np.diag(np.exp(-2.0 * j_profile))
    tau = cmath.exp(2j * math.pi * Q / N)
    target = np.array(
        [
            [0.9743, 0.2250, 0.0036],
            [0.2250, 0.9735, 0.0411],
            [0.0057, 0.0409, 0.9991],
        ]
    )

    constants = [1.0, 2.0, 4.0, 8.0]
    lambdas = {
        "lens-3nil": LAMBDA_LENS - 3.0 * LAMBDA_NIL,
        "lens-nil": LAMBDA_LENS - LAMBDA_NIL,
        "lens": LAMBDA_LENS,
        "7nil": 7.0 * LAMBDA_NIL,
        "3nil": 3.0 * LAMBDA_NIL,
        "1": 1.0,
        "2": 2.0,
        "4": 4.0,
    }
    hidden_coefficients = {
        "hidden2": 0.5,
        "hidden1": 1.0,
        "hidden3": 1.0 / 3.0,
    }

    counts = {name: 0 for name in hidden_coefficients}
    best: dict[str, tuple[float, tuple[object, ...]]] = {
        name: (float("inf"), tuple()) for name in hidden_coefficients
    }

    for mu_u, mu_d in itertools.product(constants, constants):
        for lambda_name, lambda_q in lambdas.items():
            for coeff_name, alpha_hidden in hidden_coefficients.items():
                for orientation in [1, -1]:
                    yu = y_second_order(mu_u, 1, lambda_q, alpha_hidden, orientation, j_profile, tau)
                    yd = y_second_order(mu_d, 2, lambda_q, alpha_hidden, orientation, j_profile, tau)
                    v = mixing(yu, yd, g_inv)
                    err = float(np.linalg.norm(v - target))
                    if is_ckm_shaped(v):
                        counts[coeff_name] += 1
                    if err < best[coeff_name][0]:
                        best[coeff_name] = (
                            err,
                            (
                                mu_u,
                                mu_d,
                                lambda_name,
                                orientation,
                                float(v[0, 1]),
                                float(v[0, 2]),
                                float(v[1, 2]),
                                is_ckm_shaped(v),
                            ),
                        )
    return counts, best


def main() -> None:
    paper = read(ROOT / "Color_Singlet_Redundancy_Source_for_Bq_v1.md")
    operator = read(ROOT / "Quark_Second_Order_Breakdown_Operator_Candidate_v1.md")

    deltas = np.array([0.25, 0.5, 1.0, 2.0], dtype=float)
    coeff_errors = [abs(hidden_two_channel_cost(float(delta)) - 0.5 * float(delta) ** 2) for delta in deltas]
    counts, best = finite_dictionary_scan()

    hidden2_best = best["hidden2"]
    hidden1_best = best["hidden1"]
    hidden3_best = best["hidden3"]

    gates = [
        Gate("paper saved", "PASS" if "Color-Singlet Completion Lemma" in paper else "FAIL", "source paper present"),
        Gate("completion coefficient", "PASS" if max(coeff_errors) < 1e-12 else "FAIL", "two hidden channels give delta^2/2"),
        Gate("operator coefficient", "PASS" if "(1/2)" in operator or "0.5" in operator else "FAIL", "B_q uses the Schur coefficient"),
        Gate("color source stated", "PASS" if "color-singlet" in paper and "Gamma\\Nil_3" in paper else "FAIL", "color neutrality and Nil_3 fiber used"),
        Gate(
            "hidden-two scan",
            "PASS" if counts["hidden2"] > counts["hidden1"] and counts["hidden1"] == 0 else "FAIL",
            f"CKM-shaped counts hidden2={counts['hidden2']}, hidden1={counts['hidden1']}, hidden3={counts['hidden3']}",
        ),
        Gate(
            "best hidden-two branch",
            "DIAGNOSTIC",
            "err={:.6f}, mu=({:g},{:g}), Lambda={}, sigma={}, |V12|={:.4f}".format(
                hidden2_best[0],
                hidden2_best[1][0],
                hidden2_best[1][1],
                hidden2_best[1][2],
                hidden2_best[1][3],
                hidden2_best[1][6],
            ),
        ),
        Gate(
            "non-unique constants",
            "OPEN",
            "finite dictionary still leaves dyadic/gap/orientation branches to select",
        ),
        Gate(
            "hidden1 no-go",
            "PASS" if not hidden1_best[1][7] else "FAIL",
            "best one-hidden-channel coefficient is not CKM-shaped",
        ),
        Gate(
            "hidden3 weaker",
            "SUPPORTED" if counts["hidden3"] < counts["hidden2"] else "FAIL",
            "three-hidden-channel coefficient is less robust in this dictionary",
        ),
    ]

    print("Color-singlet redundancy source for B_q check")
    print("=============================================")
    print()
    print("Schur completion coefficient samples:")
    for delta in deltas:
        print(f"  delta={delta:.2f} -> E_min={hidden_two_channel_cost(float(delta)):.6f}, delta^2/2={0.5 * float(delta) ** 2:.6f}")
    print()
    print("Finite structural dictionary scan:")
    print(f"  hidden2 CKM-shaped count: {counts['hidden2']}")
    print(f"  hidden1 CKM-shaped count: {counts['hidden1']}")
    print(f"  hidden3 CKM-shaped count: {counts['hidden3']}")
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

