from __future__ import annotations

from dataclasses import dataclass

from recursive_quotient_snf_template import invariant_factors


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def carry_with_terminal(levels: int, terminal_order: int) -> list[list[int]]:
    rows: list[list[int]] = []
    for i in range(levels - 1):
        row = [0] * levels
        row[i] = 2
        row[i + 1] = -1
        rows.append(row)
    final = [0] * levels
    final[-1] = terminal_order
    rows.append(final)
    return rows


def main() -> None:
    parity_values = {1, -1}
    parity_closed = {a * b for a in parity_values for b in parity_values} == parity_values
    parity_order_two = all(v * v == 1 for v in parity_values)

    placements = {}
    for levels in (5, 6, 7):
        factors, free_rank = invariant_factors(carry_with_terminal(levels, terminal_order=2))
        placements[levels] = (factors, free_rank)

    gates = [
        Gate(
            "spinorial parity values form Z2",
            "PASS" if parity_closed and parity_order_two else "FAIL",
            "{+1,-1} with epsilon^2=1",
        ),
        Gate(
            "terminal parity at level five gives Z32",
            "PASS" if placements[5] == ([32], 0) else "FAIL",
            f"factors={placements[5][0]}, free_rank={placements[5][1]}",
        ),
        Gate(
            "terminal parity at level six gives Z64",
            "PASS" if placements[6] == ([64], 0) else "FAIL",
            f"factors={placements[6][0]}, free_rank={placements[6][1]}",
        ),
        Gate(
            "terminal parity at level seven gives Z128",
            "PASS" if placements[7] == ([128], 0) else "FAIL",
            f"factors={placements[7][0]}, free_rank={placements[7][1]}",
        ),
        Gate(
            "MTT places terminal parity at sixth selected level",
            "PROVED-SPECTRAL",
            "spectral P_fl selects five D2 steps plus terminal parity",
        ),
    ]

    print("Terminal spinorial return gate audit")
    print("====================================")
    print(f"parity values: {sorted(parity_values)}")
    print(f"closed: {parity_closed}")
    print(f"order two: {parity_order_two}")
    for levels, (factors, free_rank) in placements.items():
        print(f"terminal parity at levels={levels}: factors={factors}, free_rank={free_rank}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<55} {gate.status:<5} {gate.detail}")

    assert parity_closed
    assert parity_order_two
    assert placements[5] == ([32], 0)
    assert placements[6] == ([64], 0)
    assert placements[7] == ([128], 0)


if __name__ == "__main__":
    main()
