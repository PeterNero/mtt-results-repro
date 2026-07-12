"""Formal checks for coefficient-to-character descent of the Lens-Nil Z_7 block.

This script separates the formal lattice facts from the still-open MTT
identification.

If the integral Lens-Nil component lattice has relation matrix

    K = [[2, 1],
         [1, 4]],

then the finite quotient and its Pontryagin dual character group have the same
Smith normal form.  Since K is symmetric this is immediate, but the script also
checks transpose and sample unimodular basis changes.
"""

from __future__ import annotations

from itertools import product
from math import gcd

from recursive_quotient_snf_template import invariant_factors


def det2(m: list[list[int]]) -> int:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(m: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*m)]


def factors(m: list[list[int]]) -> tuple[list[int], int]:
    return invariant_factors(m)


def is_unimodular(m: list[list[int]]) -> bool:
    return abs(det2(m)) == 1


def main() -> None:
    k = [[2, 1], [1, 4]]
    kt = transpose(k)

    print("Formal Lens-Nil descent lattice check")
    print("=====================================")
    print("K =", k)
    print("det(K) =", det2(k))
    print("SNF(K) =", factors(k))
    print("SNF(K^T) =", factors(kt))
    print()

    print("Unimodular basis-change samples")
    print("===============================")
    gl2 = [
        [[1, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[1, 1], [0, 1]],
        [[1, 0], [1, 1]],
        [[-1, 0], [0, 1]],
        [[1, 0], [0, -1]],
    ]
    for i, u in enumerate(gl2):
        for j, v in enumerate(gl2):
            if not (is_unimodular(u) and is_unimodular(v)):
                raise AssertionError("bad GL2 sample")
            changed = matmul(matmul(u, k), v)
            f, r = factors(changed)
            if f != [7] or r != 0:
                raise AssertionError((i, j, changed, f, r))
    print(f"checked {len(gl2) * len(gl2)} GL(2,Z) row/column basis changes: all preserve [7]")
    print()

    print("Small integer correction sensitivity")
    print("====================================")
    total = 0
    preserve_det7 = 0
    preserve_snf7 = 0
    for entries in product((-1, 0, 1), repeat=4):
        delta = [[entries[0], entries[1]], [entries[2], entries[3]]]
        if delta == [[0, 0], [0, 0]]:
            continue
        total += 1
        perturbed = [[k[r][c] + delta[r][c] for c in range(2)] for r in range(2)]
        if abs(det2(perturbed)) == 7:
            preserve_det7 += 1
        f, free_rank = factors(perturbed)
        if f == [7] and free_rank == 0:
            preserve_snf7 += 1
    print(f"nonzero perturbations in {{-1,0,1}}^4: {total}")
    print(f"preserve |det|=7: {preserve_det7}")
    print(f"preserve SNF [7]: {preserve_snf7}")
    print("Interpretation: exactness of the descended integer block matters.")
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("integral beta_1,beta_3 component lattice, not naive H^4", "CORPUS-SUPPORTED"),
        ("left-invariant truncation equals coherent projector", "CORPUS-SUPPORTED"),
        ("coefficient fingerprint [[2,1],[1,4]]", "PASS"),
        ("dual character lattice has same Z_7 torsion", "FORMAL PASS"),
        ("residual CP labels identified with the dual lattice", "OPEN"),
        ("higher-order corrections shown not to alter the integer block", "OPEN"),
    ]
    width = max(len(label) for label, _ in gates)
    for label, status in gates:
        print(f"{label:{width}s}  {status}")


if __name__ == "__main__":
    main()
