"""Scan recursive shared-circle relation templates for torsion factors.

This is a diagnostic, not a derivation.  It asks:

Given secure rows
  e_l = a_l e_c,
  e_n = a_n e_c,
  3 e_l = 0,
  e_12 + e_23 + e_31 = 0,
and one candidate flux/projector row
  q_c e_c + q_l e_l + q_n e_n = 0,
what torsion does the quotient produce?

The script reports small integer rows that can generate a torsion factor with
exponent divisible by 448.  Any such row would still need to be derived from
MTT flux/projector/bundle data.
"""

from __future__ import annotations

from math import gcd

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def exponent(factors: list[int]) -> int:
    out = 1
    for factor in factors:
        out = lcm(out, factor)
    return out


def central_torsion_order(a_l: int, a_n: int, q_c: int, q_l: int, q_n: int) -> int:
    """Order forced on e_c in the one-flux-row shared-circle template.

    Relations:
      e_l = a_l e_c
      e_n = a_n e_c
      3 e_l = 0
      q_c e_c + q_l e_l + q_n e_n = 0

    reduce to:
      3 a_l e_c = 0
      (q_c + a_l q_l + a_n q_n) e_c = 0.

    Thus the order of e_c divides gcd(3 a_l, q_c + a_l q_l + a_n q_n).
    """
    m = q_c + a_l * q_l + a_n * q_n
    return gcd(abs(3 * a_l), abs(m))


def main() -> None:
    target = 448
    hits: list[tuple[int, int, int, int, int, list[int], int]] = []

    # Small diagnostic range.  These are not claimed physical bounds.
    for a_l in range(1, 13):
        for a_n in range(0, 13):
            for q_c in range(-64, 65):
                for q_l in range(-16, 17):
                    for q_n in range(-16, 17):
                        if q_c == q_l == q_n == 0:
                            continue
                        order = central_torsion_order(a_l, a_n, q_c, q_l, q_n)
                        if order and order % target == 0:
                            hits.append((a_l, a_n, q_c, q_l, q_n, [order], 3))
                            if len(hits) >= 20:
                                break
                    if len(hits) >= 20:
                        break
                if len(hits) >= 20:
                    break
            if len(hits) >= 20:
                break
        if len(hits) >= 20:
            break

    print(f"First hits with torsion exponent divisible by {target}:")
    if not hits:
        print("  none in scan range")
    else:
        for a_l, a_n, q_c, q_l, q_n, factors, free_rank in hits:
            print(
                "  "
                f"a_l={a_l:2d}, a_n={a_n:2d}, "
                f"q=({q_c:3d},{q_l:3d},{q_n:3d}) -> "
                f"torsion={factors}, free_rank={free_rank}"
            )

    print()
    print("Template consequence:")
    print("  central order divides gcd(3*a_l, q_c + a_l*q_l + a_n*q_n)")
    print("  since gcd(3, 448)=1, this one-row template needs a_l divisible by 448")
    print("  before a Z_448 central torsion factor can appear.")


if __name__ == "__main__":
    main()
