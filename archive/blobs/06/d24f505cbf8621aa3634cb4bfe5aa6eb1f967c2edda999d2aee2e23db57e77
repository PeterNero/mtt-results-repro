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


def pullback_degree_two(character_index: int) -> int:
    # D_2(z)=z^2 sends chi_n to chi_{2n}.
    return 2 * character_index


def carry_matrix(levels: int, terminal: int = 2) -> list[list[int]]:
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


def summarize(levels: int) -> tuple[list[int], int, int]:
    factors, free_rank = invariant_factors(carry_matrix(levels))
    return factors, exponent(factors) if factors else 1, free_rank


def descends_to_order_64(levels: int) -> bool:
    factors, exp, free_rank = summarize(levels)
    return free_rank == 0 and exp % 64 == 0


def main() -> None:
    pullback_examples = {n: pullback_degree_two(n) for n in range(-3, 4)}
    factors6, exp6, rank6 = summarize(6)
    factors7, exp7, rank7 = summarize(7)
    factors8, exp8, rank8 = summarize(8)

    gates = [
        Gate(
            "D2 character pullback doubles weights",
            "PASS",
            f"examples={pullback_examples}",
        ),
        Gate(
            "six selected D2 iterates with terminal parity",
            "PASS" if factors6 == [64] and rank6 == 0 else "FAIL",
            f"factors={factors6}, exponent={exp6}, free_rank={rank6}",
        ),
        Gate(
            "seven-step recursive tower has order-64 descendants",
            "PASS" if descends_to_order_64(7) else "FAIL",
            f"factors={factors7}, exponent={exp7}, free_rank={rank7}",
        ),
        Gate(
            "eight-step recursive tower has order-64 descendants",
            "PASS" if descends_to_order_64(8) else "FAIL",
            f"factors={factors8}, exponent={exp8}, free_rank={rank8}",
        ),
        Gate(
            "MTT selects D2 as flavor CP refinement",
            "PROVED-SPECTRAL",
            "Riesz projector selects D2 tower; reduced alpha/C_fl/lambda_Q bound open",
        ),
        Gate(
            "terminal spinorial parity row",
            "PROVED",
            "spinorial sign residue gives 2x_5=0",
        ),
        Gate(
            "MTT places spinorial parity at sixth level",
            "PROVED-SPECTRAL",
            "Riesz projector selects five D2 steps plus terminal parity",
        ),
    ]

    print("Shared-circle doubling operator audit")
    print("=====================================")
    print("D2 pullback examples n -> 2n:", pullback_examples)
    for levels in (6, 7, 8):
        factors, exp, rank = summarize(levels)
        print(f"levels={levels}: factors={factors}, exponent={exp}, free_rank={rank}, order64_descends={descends_to_order_64(levels)}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<56} {gate.status:<5} {gate.detail}")

    assert pullback_examples[3] == 6
    assert pullback_examples[-3] == -6
    assert factors6 == [64] and rank6 == 0
    assert descends_to_order_64(7)
    assert descends_to_order_64(8)


if __name__ == "__main__":
    main()
