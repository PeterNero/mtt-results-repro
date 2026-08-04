"""Phase-lattice checks for complex/orthogonal nested carrier options.

The scan treats complex nesting as a unitary phase lattice rather than as real
containment rows.  A lens quarter-turn contributes order 4, a nil sevenfold
rotor contributes order 7, and a dyadic circle lift contributes order 64 when
such a lift is actually derived.
"""

from __future__ import annotations

from math import gcd, pi, sin
from functools import reduce


TARGET_DELTA_Q = 1.107978573420
TARGET_J = 2.9e-5
TARGET_DELTA_L = -pi / 2
AMPLITUDE = TARGET_J / sin(TARGET_DELTA_Q)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(moduli: tuple[int, ...]) -> int:
    return reduce(lcm, moduli, 1)


def best_phase_error(order: int, target: float) -> tuple[int, float, float, float]:
    """Return k, phase, phase error, J error for a cyclic phase grid."""
    x = (target % (2 * pi)) / (2 * pi)
    k = round(order * x) % order
    phase = 2 * pi * k / order
    # compare on the shortest branch
    err = (phase - target + pi) % (2 * pi) - pi
    j = AMPLITUDE * sin(phase)
    return k, phase, abs(err), abs(j - TARGET_J)


def exact_lepton_quarter_turn(order: int) -> bool:
    return order % 4 == 0


def report(name: str, moduli: tuple[int, ...]) -> None:
    exp = exponent(moduli)
    k, phase, phase_err, j_err = best_phase_error(exp, TARGET_DELTA_Q)
    print(name)
    print(f"  source moduli: {moduli}")
    print(f"  effective exponent: {exp}")
    print(f"  CKM best k/order: {k}/{exp}")
    print(f"  CKM phase: {phase:.12f}")
    print(f"  CKM phase error: {phase_err:.3e}")
    print(f"  CKM J error: {j_err:.3e}")
    print(f"  exact lepton -pi/2 available: {exact_lepton_quarter_turn(exp)}")
    if exact_lepton_quarter_turn(exp):
        print(f"  lepton k/order for -pi/2: {(-exp // 4) % exp}/{exp}")
    print()


def main() -> None:
    report("Lens quarter-turn only", (4,))
    report("Lens quarter-turn plus nil sevenfold rotor", (4, 7))
    report("Gaussian-style dyadic exponent 8 plus nil seven", (8, 7))
    report("Dyadic circle order 64 only", (64,))
    report("Dyadic circle order 64 plus nil seven", (64, 7))
    report("Lens quarter-turn, dyadic circle order 64, plus nil seven", (4, 64, 7))
    report("Full benchmark cyclic order", (448,))


if __name__ == "__main__":
    main()
