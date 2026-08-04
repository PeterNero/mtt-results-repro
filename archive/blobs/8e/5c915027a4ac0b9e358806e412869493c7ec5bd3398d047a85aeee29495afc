"""Lens x Nil / Wilson-line relation scan for the MTT CP quotient.

Generators used in the templates:

  c  shared central-circle phase
  n  nil survivor / nil terminal phase
  w  Wilson-line phase
  f  integer flux label reduced to a phase congruence
  z  already-known family Z3 character

Rows are integer relations in the listed generator basis.  The scan separates
corpus-supported relation *types* from the new order-seven hypotheses still
needed to obtain a sevenfold CP factor.
"""

from __future__ import annotations

from functools import reduce
from math import gcd

from recursive_quotient_snf_template import invariant_factors
from candidate_quotient_mechanism_scan import dyadic_carry_matrix, block_diag


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def character_order(k: int, n: int) -> int:
    return n // gcd(k, n)


def report(name: str, generators: list[str], rows: list[list[int]], note: str) -> None:
    factors, free_rank = invariant_factors(rows)
    print(name)
    print("  generators:", ", ".join(generators))
    print("  rows:")
    for row in rows:
        terms = []
        for coeff, gen in zip(row, generators):
            if coeff:
                terms.append(f"{coeff:+d}{gen}")
        print("   ", " ".join(terms).lstrip("+") or "0")
    print("  torsion factors:", factors if factors else "none")
    print("  exponent:", exponent(factors) if factors else 1)
    print("  free rank:", free_rank)
    print("  note:", note)
    print()


def extend_rows(rows: list[list[int]], extra_cols: int) -> list[list[int]]:
    return [row + [0] * extra_cols for row in rows]


def with_family(rows: list[list[int]]) -> list[list[int]]:
    widened = extend_rows(rows, 1)
    family_row = [0] * (len(rows[0]) + 1)
    family_row[-1] = 3
    return widened + [family_row]


def main() -> None:
    # c,n,w,f basis.
    gens = ["c", "n", "w", "f"]

    cases = [
        (
            "Flux labels only",
            gens,
            [[0, 0, 0, 1]],
            "Flux integrality alone labels sectors; it does not create seven-torsion.",
        ),
        (
            "Shared-circle/nil lock only",
            gens,
            [[1, -1, 0, 0]],
            "Locks c and n but leaves one free phase; no finite CP character yet.",
        ),
        (
            "Wilson-flux congruence only",
            gens,
            [[0, 0, 1, -1]],
            "Relates Wilson phase to flux label but needs a finite Wilson row.",
        ),
        (
            "Nil monodromy only",
            gens,
            [[-7, 1, 0, 0]],
            "Bare n=7c monodromy leaves a free phase; downgraded as standalone.",
        ),
        (
            "Shared-circle/nil lock plus nil seven",
            gens,
            [[1, -1, 0, 0], [0, 7, 0, 0]],
            "Strongest MTT-native sevenfold hypothesis.",
        ),
        (
            "Wilson-flux congruence plus Wilson seven",
            gens,
            [[0, 0, 1, -1], [0, 0, 7, 0]],
            "Strongest string/KK Wilson-line hypothesis.",
        ),
        (
            "Nil monodromy plus terminal nil closure",
            gens,
            [[-7, 1, 0, 0], [0, 1, 0, 0]],
            "Restores seven-torsion by adding terminal closure.",
        ),
        (
            "Nil lock plus Wilson-flux plus Wilson seven",
            gens,
            [[1, -1, 0, 0], [0, 0, 1, -1], [0, 0, 7, 0]],
            "Combines nil placement with Wilson order-seven selection.",
        ),
        (
            "Nil seven plus Wilson seven, independent",
            gens,
            [[0, 7, 0, 0], [0, 0, 7, 0]],
            "Overlarge unless a diagonal character or lock selects one sevenfold phase.",
        ),
    ]

    for name, generators, rows, note in cases:
        report(name, generators, rows, note)

    print("Combined with dyadic carry")
    print("==========================")
    carry = dyadic_carry_matrix(6)
    seven_rows = {
        "dyadic + nil lock/seven": [[1, -1, 0, 0], [0, 7, 0, 0]],
        "dyadic + Wilson-flux/seven": [[0, 0, 1, -1], [0, 0, 7, 0]],
        "dyadic + monodromy/terminal": [[-7, 1, 0, 0], [0, 1, 0, 0]],
    }
    for name, rows in seven_rows.items():
        combined = block_diag(carry, rows)
        factors, free_rank = invariant_factors(combined)
        print(name)
        print("  torsion factors:", factors)
        print("  exponent:", exponent(factors))
        print("  free rank:", free_rank)
        print()

    print("Family Z3 ambient check")
    print("=======================")
    cp_rows = [[1, -1, 0, 0], [0, 7, 0, 0]]
    ambient = block_diag(carry, with_family(cp_rows))
    factors, free_rank = invariant_factors(ambient)
    print("dyadic + nil seven + family Z3")
    print("  torsion factors:", factors)
    print("  exponent:", exponent(factors))
    print("  free rank:", free_rank)
    print("  selected character example in Z1344: k=237")
    print("  selected character order:", character_order(237, 1344))


if __name__ == "__main__":
    main()
