"""Sensitivity checks for protecting the Lens-Nil determinant-seven block.

The goal is to make explicit why the O(lambda^2 nu^2) curvature terms require
a proof of arithmetic invisibility or an exact period computation.
"""

from __future__ import annotations

from itertools import product

from recursive_quotient_snf_template import invariant_factors


def det2(m: list[list[int]]) -> int:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def report(name: str, matrix: list[list[int]]) -> None:
    factors, free_rank = invariant_factors(matrix)
    print(name)
    print("-" * len(name))
    print("matrix:", matrix)
    print("determinant:", det2(matrix))
    print("SNF:", factors, "free rank:", free_rank)
    print()


def main() -> None:
    k0 = [[2, 1], [1, 4]]

    print("Integer-block protection check")
    print("==============================")
    print()

    report("protected reduced block", k0)
    report("diagonal A correction enters integer matrix", [[3, 1], [1, 4]])
    report("diagonal B correction enters integer matrix", [[2, 1], [1, 5]])
    report("mixed correction enters integer matrix", [[2, 2], [2, 4]])

    total = 0
    preserve = 0
    examples: list[list[list[int]]] = []
    for entries in product((-1, 0, 1), repeat=4):
        delta = [[entries[0], entries[1]], [entries[2], entries[3]]]
        if delta == [[0, 0], [0, 0]]:
            continue
        total += 1
        perturbed = [[k0[r][c] + delta[r][c] for c in range(2)] for r in range(2)]
        factors, free_rank = invariant_factors(perturbed)
        if factors == [7] and free_rank == 0:
            preserve += 1
            examples.append(perturbed)

    print("Perturbation scan")
    print("=================")
    print("nonzero integer perturbations in {-1,0,1}^4:", total)
    print("preserve SNF [7]:", preserve)
    print("preserving examples:", examples)
    print()

    print("Gate status")
    print("===========")
    gates = [
        (
            "reduced block has SNF [7]",
            "FORMAL PASS",
            "K0=[[2,1],[1,4]]",
        ),
        (
            "arbitrary integer corrections preserve Z7",
            "FAIL",
            "only 2 of 80 small perturbations preserve SNF [7]",
        ),
        (
            "O(lambda^2 nu^2) terms are excluded from character matrix",
            "OPEN",
            "prove by exact periods, differential cohomology, or P_char",
        ),
        (
            "full Lens-Nil exact period matrix has SNF [7]",
            "OPEN",
            "next required computation",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()

