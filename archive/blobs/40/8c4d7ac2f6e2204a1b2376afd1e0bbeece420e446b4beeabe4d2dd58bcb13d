"""Bounded retarded-lag check for the dyadic CKM component.

Let u_q = 16 - epsilon in the dyadic Z_64 coordinate, where
epsilon = rho_q/kappa_q.  The sharp survivor is the nearest primitive
order-64 label, i.e. the nearest odd label.

This script verifies the exact cell:

    0 < epsilon < 2  -> q64=15.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Optional


N = 64
QUARTER = 16


@dataclass(frozen=True)
class LagCase:
    epsilon: float
    u_q: float
    q64: Optional[int]
    r64: Optional[int]


def order_mod(label: int, modulus: int) -> int:
    return modulus // gcd(label % modulus, modulus)


def primitive_labels() -> list[int]:
    return [label for label in range(N) if order_mod(label, N) == N]


def nearest_primitive(u: float) -> Optional[int]:
    labels = primitive_labels()
    distances = [(abs(label - u), label) for label in labels]
    best_distance = min(distance for distance, _ in distances)
    winners = [label for distance, label in distances if abs(distance - best_distance) < 1e-12]
    if len(winners) != 1:
        return None
    return winners[0]


def classify(epsilon: float) -> LagCase:
    u_q = QUARTER - epsilon
    q64 = nearest_primitive(u_q)
    r64 = None if q64 is None else (-(q64 + QUARTER)) % N
    return LagCase(epsilon=epsilon, u_q=u_q, q64=q64, r64=r64)


def main() -> None:
    probes = [-2.5, -1.5, -0.5, 0.0, 0.25, 1.0, 1.75, 2.0, 2.5, 3.5]
    rows = [classify(epsilon) for epsilon in probes]

    print("Bounded retarded-lag q64 check")
    print("==============================")
    print("quarter-turn:", QUARTER)
    print("primitive labels near quarter:", [15, 17])
    print()

    print("Probe table")
    print("===========")
    for row in rows:
        q64 = "amb" if row.q64 is None else f"{row.q64:2d}"
        r64 = "amb" if row.r64 is None else f"{row.r64:2d}"
        closure = "amb" if row.q64 is None or row.r64 is None else str((row.q64 + QUARTER + row.r64) % N)
        print(
            f"epsilon={row.epsilon:5.2f} "
            f"u_q={row.u_q:6.2f} "
            f"q64={q64:>3s} "
            f"r64={r64:>3s} "
            f"closure={closure}"
        )
    print()

    interval_checks = [
        (0.001, 15),
        (0.5, 15),
        (1.999, 15),
        (-0.001, 17),
        (-1.999, 17),
        (2.001, 13),
    ]
    for epsilon, expected in interval_checks:
        got = classify(epsilon).q64
        assert got == expected, (epsilon, got, expected)
    assert classify(0.0).q64 is None
    assert classify(2.0).q64 is None

    print("Gate status")
    print("===========")
    gates = [
        ("0 < epsilon < 2 selects q64=15", "PASS", "retarded adjacent cell"),
        ("-2 < epsilon < 0 selects q64=17", "PASS", "advanced adjacent cell"),
        ("epsilon = 0 or 2 is boundary-ambiguous", "PASS", "excluded from theorem"),
        ("epsilon > 2 leaves adjacent cell", "PASS", "selects lower primitive"),
        ("MTT computes epsilon=rho_q/kappa_q", "OPEN", "needs Hessian/overlap data"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
