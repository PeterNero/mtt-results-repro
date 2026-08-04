"""Scan odd prime companions to the dyadic order-64 CP character.

If the missing odd factor is a finite Wilson/holonomy subgroup of U(1), the
minimal prime-order candidates are Z_p.  This scan checks which prime p makes
N=64*p approximate the CKM CP branch.
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
        if not is_prime(p):
            continue
        n = 64 * p
        k = round(delta_q * n / (2.0 * math.pi)) % n
        delta = 2.0 * math.pi * k / n
        j = prefactor * math.sin(delta)
        rows.append(
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

    print("Odd prime companions p for N=64*p, ranked by CKM phase error")
    print("p   N     k    char_order  phase_error    J_error")
    for phase_error, j_error, p, n, k, order, _ in sorted(rows)[:20]:
        print(
            f"{p:3d} {n:5d} {k:4d} {order:10d} "
            f"{phase_error:12.3e} {j_error:10.3e}"
        )

    print()
    print("Small prime companions")
    print("p   N     k    char_order  phase_error    J_error")
    for phase_error, j_error, p, n, k, order, _ in rows:
        if p <= 31:
            print(
                f"{p:3d} {n:5d} {k:4d} {order:10d} "
                f"{phase_error:12.3e} {j_error:10.3e}"
            )


if __name__ == "__main__":
    main()
