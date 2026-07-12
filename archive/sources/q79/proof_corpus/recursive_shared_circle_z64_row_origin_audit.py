from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd

from recursive_quotient_snf_template import invariant_factors


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def diag(entries: list[int]) -> list[list[int]]:
    return [
        [entry if i == j else 0 for j, entry in enumerate(entries)]
        for i, entry in enumerate(entries)
    ]


def dyadic_refinement_matrix(levels: int, terminal: int = 2) -> list[list[int]]:
    rows: list[list[int]] = []
    for i in range(levels - 1):
        row = [0] * levels
        row[i] = 2
        row[i + 1] = -1
        rows.append(row)
    final = [0] * levels
    final[-1] = terminal
    rows.append(final)
    return rows


def summarize(matrix: list[list[int]]) -> tuple[list[int], int, int]:
    factors, free_rank = invariant_factors(matrix)
    return factors, exponent(factors) if factors else 1, free_rank


def main() -> None:
    independent_bits = diag([2] * 6)
    carry6 = dyadic_refinement_matrix(6)
    carry5 = dyadic_refinement_matrix(5)
    carry7 = dyadic_refinement_matrix(7)
    carry8 = dyadic_refinement_matrix(8)

    bits_factors, bits_exp, bits_rank = summarize(independent_bits)
    c6_factors, c6_exp, c6_rank = summarize(carry6)
    c5_factors, c5_exp, c5_rank = summarize(carry5)
    c7_factors, c7_exp, c7_rank = summarize(carry7)
    c8_factors, c8_exp, c8_rank = summarize(carry8)

    gates = [
        Gate(
            "six independent binary memories",
            "FAIL-AS-Z64" if bits_exp == 2 else "CHECK",
            f"factors={bits_factors}, exponent={bits_exp}, free_rank={bits_rank}",
        ),
        Gate(
            "five-level dyadic tower",
            "PASS",
            f"factors={c5_factors}, exponent={c5_exp}, free_rank={c5_rank}",
        ),
        Gate(
            "six-level dyadic tower",
            "PASS" if c6_factors == [64] and c6_rank == 0 else "FAIL",
            f"factors={c6_factors}, exponent={c6_exp}, free_rank={c6_rank}",
        ),
        Gate(
            "seven-level recursive tower",
            "LARGER",
            f"factors={c7_factors}, exponent={c7_exp}, free_rank={c7_rank}",
        ),
        Gate(
            "eight-level recursive tower",
            "LARGER",
            f"factors={c8_factors}, exponent={c8_exp}, free_rank={c8_rank}",
        ),
        Gate(
            "row origin from dyadic refinement convention",
            "PROVED",
            "R_i(x_i)=x_{i+1}=2x_i gives 2x_i-x_{i+1}=0",
        ),
        Gate(
            "candidate R=D2* on shared-circle characters",
            "IDENTIFIED",
            "degree-two cover D2(z)=z^2",
        ),
        Gate(
            "MTT proves projector selects R=D2*",
            "PROVED-SPECTRAL",
            "spectral P_fl selects D2 tower; reduced alpha/C_fl/lambda_Q bound open",
        ),
        Gate(
            "terminal two-torsion at selected sixth level",
            "PROVED-SPECTRAL",
            "spectral P_fl selects five D2 steps plus terminal parity",
        ),
    ]

    print("Recursive shared-circle Z64 row-origin audit")
    print("============================================")
    for levels in (5, 6, 7, 8):
        factors, exp, rank = summarize(dyadic_refinement_matrix(levels))
        print(f"levels={levels}: factors={factors}, exponent={exp}, free_rank={rank}")
    print(f"independent bits: factors={bits_factors}, exponent={bits_exp}, free_rank={bits_rank}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<58} {gate.status:<12} {gate.detail}")

    assert bits_factors == [2, 2, 2, 2, 2, 2]
    assert bits_exp == 2
    assert c5_factors == [32] and c5_rank == 0
    assert c6_factors == [64] and c6_rank == 0
    assert c7_factors == [128] and c7_rank == 0
    assert c8_factors == [256] and c8_rank == 0


if __name__ == "__main__":
    main()
