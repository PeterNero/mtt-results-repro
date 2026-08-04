"""Compare candidate mechanisms for the effective order-448 flavor quotient.

The point is to distinguish real quotient mechanisms from look-alikes:

* six independent binary memories give 64 states but exponent 2;
* a dyadic carry chain gives a genuine cyclic Z_64;
* Gaussian-integer dyadic ideals can have 64 states but insufficient exponent;
* adding a sevenfold nil/source row to a true Z_64 gives effective Z_448.
"""

from __future__ import annotations

from math import gcd
from functools import reduce

from recursive_quotient_snf_template import invariant_factors


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("  torsion factors:", factors if factors else "none")
    print("  exponent:", exponent(factors) if factors else 1)
    print("  free rank:", free_rank)
    print()


def dyadic_carry_matrix(levels: int) -> list[list[int]]:
    """Rows for x_1=2x_0, ..., x_{n-1}=2x_{n-2}, 2x_{n-1}=0."""
    rows: list[list[int]] = []
    for i in range(levels - 1):
        row = [0] * levels
        row[i] = 2
        row[i + 1] = -1
        rows.append(row)
    row = [0] * levels
    row[-1] = 2
    rows.append(row)
    return rows


def gaussian_power_matrix(n: int) -> list[list[int]]:
    """Multiplication by (1+i)^n on Z[i] in the basis (1,i)."""
    # Repeatedly multiply a+bi by 1+i: (a-b) + (a+b)i.
    a, b = 1, 0
    for _ in range(n):
        a, b = a - b, a + b
    # Matrix for multiplication by a+bi:
    # (x+iy)(a+bi) = (ax-by) + (bx+ay)i.
    return [[a, -b], [b, a]]


def block_diag(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows: list[list[int]] = []
    ca = len(a[0]) if a else 0
    cb = len(b[0]) if b else 0
    for row in a:
        rows.append(row + [0] * cb)
    for row in b:
        rows.append([0] * ca + row)
    return rows


def main() -> None:
    z2_six = [[0] * 6 for _ in range(6)]
    for i in range(6):
        z2_six[i][i] = 2
    report("Six independent binary closures: 2 x_i = 0", z2_six)

    carry64 = dyadic_carry_matrix(6)
    report("Six-level dyadic carry chain: cyclic Z_64", carry64)

    carry64_nil7 = block_diag(carry64, [[7]])
    report("Dyadic carry Z_64 plus nil sevenfold source", carry64_nil7)

    for n in (4, 6, 8, 10, 12):
        report(f"Gaussian dyadic ideal Z[i]/(1+i)^{n}", gaussian_power_matrix(n))

    gaussian6_nil7 = block_diag(gaussian_power_matrix(6), [[7]])
    report("Gaussian 64-state quotient plus nil seven", gaussian6_nil7)

    gaussian12_nil7 = block_diag(gaussian_power_matrix(12), [[7]])
    report("Gaussian exponent-64 quotient plus nil seven", gaussian12_nil7)


if __name__ == "__main__":
    main()
