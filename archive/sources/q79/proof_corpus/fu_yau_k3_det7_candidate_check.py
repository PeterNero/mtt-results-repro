"""Fu-Yau/K3 determinant-seven flux candidate.

The K3 lattice contains U^2 with basis (e1,f1,e2,f2) and pairing
    e_i.f_i = 1, e_i^2=f_i^2=0.

This script exhibits two integral classes whose Gram matrix has determinant 7.
After changing one generator sign, the positive relation matrix is
    [[2, 1],
     [1, 4]],
so the character quotient has a Z7 factor.

This is a candidate source only.  The remaining mathematical gates are:
realize the sublattice as primitive (1,1) on a K3 in the Fu-Yau base, choose a
polarization orthogonal to it so the corresponding flux is HYM/polystable, and
show MTT selects this sector.
"""

from __future__ import annotations

from recursive_quotient_snf_template import invariant_factors


Vector = tuple[int, int, int, int]


def inner(x: Vector, y: Vector) -> int:
    a, b, c, d = x
    e, f, g, h = y
    return a * f + e * b + c * h + g * d


def gram(vectors: list[Vector]) -> list[list[int]]:
    return [[inner(x, y) for y in vectors] for x in vectors]


def negate(matrix: list[list[int]]) -> list[list[int]]:
    return [[-entry for entry in row] for row in matrix]


def main() -> None:
    v = (-1, 0, -1, 1)
    w = (1, -1, -1, 1)  # sign-flipped from another norm -4 class, giving v.w=-1
    g = gram([v, w])
    k = negate(g)

    print("Fu-Yau/K3 determinant-seven candidate")
    print("====================================")
    print("K3 sublattice: U^2 with basis (e1,f1,e2,f2)")
    print("v =", v, "v^2 =", inner(v, v))
    print("w =", w, "w^2 =", inner(w, w))
    print("v.w =", inner(v, w))
    print("Gram(v,w) =", g)
    print("K = -Gram(v,w) =", k)
    print("SNF(K) =", invariant_factors(k))
    print()

    assert g == [[-2, -1], [-1, -4]]
    assert k == [[2, 1], [1, 4]]
    assert invariant_factors(k) == ([7], 0)

    print("Gate status")
    print("===========")
    gates = [
        (
            "K3 lattice contains primitive determinant-seven rank-two block",
            "FORMAL PASS",
            "explicit U^2 vectors above",
        ),
        (
            "block is negative definite, so can plausibly sit in Picard lattice",
            "STANDARD K3 GATE",
            "requires period-map/Nikulin-style embedding citation",
        ),
        (
            "Fu-Yau provides admissible Strominger/HYM flux slice",
            "CORPUS-SUPPORTED",
            "Strominger paper: stable bundle + Li-Yau HYM",
        ),
        (
            "line/polystable or stable bundle realizes this exact ch2 block",
            "OPEN",
            "construct bundle or cite existence theorem",
        ),
        (
            "MTT selects this determinant-seven sector as CP quotient",
            "OPEN",
            "selection/character identification theorem needed",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()

