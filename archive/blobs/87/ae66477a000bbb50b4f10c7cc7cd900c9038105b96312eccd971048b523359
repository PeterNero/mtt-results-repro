"""Scan CP characters in ambient carriers that also include family Z3.

Ambient model:
    Z_(64*p*3)

The final factor 3 represents the already-known family holonomy.  Requiring
the CP character to ignore that factor means using a character lifted from the
quotient Z_(64*p), equivalently k is a multiple of 3 in the cyclic presentation.
"""

from __future__ import annotations

import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def character_order(k: int, n: int) -> int:
    return n // math.gcd(k, n)


def best_family_trivial_character(p: int, delta_q: float, prefactor: float, target_j: float):
    n = 64 * p * 3
    # CP characters that ignore the family Z3 factor are multiples of 3.
    continuous_k = delta_q * n / (2.0 * math.pi)
    nearest_lift = round(continuous_k / 3.0)
    candidates = []
    for lift in range(nearest_lift - 3, nearest_lift + 4):
        k = (3 * lift) % n
        delta = 2.0 * math.pi * k / n
        j = prefactor * math.sin(delta)
        candidates.append(
            (
                abs(delta - delta_q),
                abs(j - target_j),
                p,
                n,
                k,
                character_order(k, n),
                delta,
            )
        )
    return min(candidates)


def main() -> None:
    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    delta_q = math.asin(target_j / prefactor)

    rows = []
    for p in range(3, 128):
        if is_prime(p):
            rows.append(best_family_trivial_character(p, delta_q, prefactor, target_j))

    print("Ambient Z_(64*p*3), CP character trivial on family Z3")
    print("p   N      k     char_order  phase_error    J_error")
    for phase_error, j_error, p, n, k, order, _ in sorted(rows)[:20]:
        print(
            f"{p:3d} {n:6d} {k:5d} {order:10d} "
            f"{phase_error:12.3e} {j_error:10.3e}"
        )

    print()
    print("Small prime companions with family Z3 present")
    print("p   N      k     char_order  phase_error    J_error")
    for phase_error, j_error, p, n, k, order, _ in rows:
        if p <= 31:
            print(
                f"{p:3d} {n:6d} {k:5d} {order:10d} "
                f"{phase_error:12.3e} {j_error:10.3e}"
            )

    print()
    print("Lepton quarter-turn check for the selected p=7 ambient carrier")
    n = 64 * 7 * 3
    k_l = 3 * n // 4
    print(f"N={n}, k_l={k_l}, delta_l=2pi*k_l/N=3pi/2=-pi/2 mod 2pi")
    print(f"k_l multiple of 3 (family-trivial lift): {k_l % 3 == 0}")
    print(f"character order: {character_order(k_l, n)}")

    print()
    print("Pairwise phase-sum closure in the selected p=7 ambient carrier")
    k_q = 237
    k_31 = (-(k_q + k_l)) % n
    print(f"k_q={k_q}, k_l={k_l}, k_31={k_31}")
    print(f"(k_q + k_l + k_31) mod N = {(k_q + k_l + k_31) % n}")
    print(f"all labels family-trivial: {all(k % 3 == 0 for k in (k_q, k_l, k_31))}")
    print(f"orders: q={character_order(k_q, n)}, l={character_order(k_l, n)}, 31={character_order(k_31, n)}")


if __name__ == "__main__":
    main()
