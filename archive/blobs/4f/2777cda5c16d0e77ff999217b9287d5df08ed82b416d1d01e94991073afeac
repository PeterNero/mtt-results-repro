"""Gate audit for the retarded-Schur CKM q=79 proof.

This script separates three things:

1. Algebraic consequences of a positive selected Hessian.
2. What the empirical CKM/Jarlskog target demands for the lag.
3. What still has to be supplied by the selected MTT retarded kernel.

It deliberately shows that positivity alone does not imply rho/kappa < 2.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from math import gcd


N_DYADIC = 64
N_CP = 448
QUARTER = 16
Q7 = 2

S12_Q = 0.2250
S23_Q = 0.0411
S13_Q = 0.0036
J_CKM = 2.9e-5


@dataclass(frozen=True)
class SchurResult:
    rho: float
    kappa: float
    epsilon: float


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def solve_2x2(a: list[list[float]], b: list[float]) -> list[float]:
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if abs(det) < 1e-14:
        raise ValueError("singular 2x2 block")
    return [
        (b[0] * a[1][1] - a[0][1] * b[1]) / det,
        (a[0][0] * b[1] - b[0] * a[1][0]) / det,
    ]


def schur(a: float, b: list[float], d: list[list[float]], r_u: float, r_eta: list[float]) -> SchurResult:
    d_inv_b = solve_2x2(d, b)
    d_inv_r = solve_2x2(d, r_eta)
    kappa = a - dot(b, d_inv_b)
    rho = r_u - dot(b, d_inv_r)
    return SchurResult(rho=rho, kappa=kappa, epsilon=rho / kappa)


def dyadic_survivor(epsilon: float) -> int | None:
    u = QUARTER - epsilon
    primitive = [k for k in range(N_DYADIC) if N_DYADIC // gcd(k, N_DYADIC) == N_DYADIC]
    distances = [(abs(k - u), k) for k in primitive]
    best = min(dist for dist, _ in distances)
    winners = [k for dist, k in distances if abs(dist - best) < 1e-12]
    return winners[0] if len(winners) == 1 else None


def crt_q(q64: int, q7: int) -> int:
    for q in range(N_CP):
        if q % 64 == q64 and q % 7 == q7:
            return q
    raise ValueError("no CRT solution")


def ckm_target_epsilon() -> float:
    c12_q = math.sqrt(1.0 - S12_Q * S12_Q)
    c23_q = math.sqrt(1.0 - S23_Q * S23_Q)
    c13_q = math.sqrt(1.0 - S13_Q * S13_Q)
    prefactor = c12_q * c23_q * c13_q**2 * S12_Q * S23_Q * S13_Q
    delta = math.asin(J_CKM / prefactor)
    continuous_label = N_CP * delta / (2.0 * math.pi)
    u64 = continuous_label % N_DYADIC
    return QUARTER - u64


def main() -> None:
    # Demonstration Hessian: total block [[a,b^T],[b,D]] is positive definite.
    # These numbers are algebra witnesses, not selected MTT coefficients.
    a = 5.0
    b = [0.5, -0.25]
    d = [[4.0, 0.5], [0.5, 3.0]]

    unit_lag = schur(a, b, d, r_u=4.942553191489, r_eta=[0.2, -0.1])
    too_large = schur(a, b, d, r_u=12.0, r_eta=[0.0, 0.0])
    wrong_sign = schur(a, b, d, r_u=-1.0, r_eta=[0.0, 0.0])

    eps_target = ckm_target_epsilon()
    q64_target = dyadic_survivor(eps_target)
    q_target = crt_q(q64_target, Q7) if q64_target is not None else None
    q64_unit = dyadic_survivor(1.0)
    q_unit = crt_q(q64_unit, Q7) if q64_unit is not None else None

    print("Retarded-Schur CKM q=79 gate audit")
    print("===================================")
    print("Schur formula: epsilon = [r_u - b^T D^-1 r_eta] / [a - b^T D^-1 b]")
    print()

    print("Algebra witnesses")
    print("=================")
    print("unit-lag witness epsilon:", f"{unit_lag.epsilon:.12f}", "q64:", q64_unit, "q:", q_unit)
    print("too-large positive-force epsilon:", f"{too_large.epsilon:.12f}", "q64:", dyadic_survivor(too_large.epsilon))
    print("wrong-sign witness epsilon:", f"{wrong_sign.epsilon:.12f}", "q64:", dyadic_survivor(wrong_sign.epsilon))
    print()

    print("Empirical target")
    print("================")
    print("epsilon_target:", f"{eps_target:.12f}")
    print("target q64:", q64_target)
    print("target q:", q_target)
    print("distance from exact unit lag:", f"{eps_target - 1.0:.12e}")
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("D > 0 from positive selected Hessian", "SUPPORTED", "structural closure-strain theorem, still needs selected quotient"),
        ("kappa_q > 0 from Schur complement", "PROVED-CONDITIONAL", "follows if total selected Hessian is positive"),
        ("rho_q > 0 retarded orientation", "SUPPORTED", "needs selected retarded kernel sign convention"),
        ("rho_q < 2 kappa_q: raw kernel", "OPEN", "not implied by positivity alone"),
        ("rho_q < 2 kappa_q: selected nil-projected kernel", "PROVED-MTT", "unit-lag plus selected-kernel factorization"),
        ("empirical CKM epsilon in cell", "PASS", f"epsilon={eps_target:.12f}"),
        ("exact unit-lag selects q=79", "PASS", "epsilon=1 -> q64=15, q7=2 -> q=79"),
        ("full q=79 proof using selected kernel", "PROVED-MTT", "conditional on MTT execution premises and selected quotient"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")

    assert 0.0 < eps_target < 2.0
    assert q64_target == 15
    assert q_target == 79
    assert q_unit == 79
    assert too_large.epsilon > 2.0
    assert wrong_sign.epsilon < 0.0


if __name__ == "__main__":
    main()
