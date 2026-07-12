"""K3 Picard and HYM gates for the determinant-seven CP candidate.

This verifies what the Fu-Yau/K3 lattice candidate gives, and what it does not
give.

The determinant-seven block is a primitive negative-definite rank-two sublattice
of U^2.  It has a positive orthogonal vector, so the lattice-realization gate is
plausible.  However, one generator is a (-2)-class.  On K3, a (-2) Picard class
is a root; a polarization orthogonal to an effective root is on a wall.  Thus
the naive "two zero-slope line bundles with c1=v,w" route is not a finished HYM
proof.  The correct HYM route should use stable higher-rank or Mukai-lattice
data, or treat the block as a fixed charge/character lattice rather than as two
line-bundle curvatures.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd


Vector = tuple[int, int, int, int]


def inner(x: Vector, y: Vector) -> int:
    a, b, c, d = x
    e, f, g, h = y
    return a * f + e * b + c * h + g * d


def gram(vectors: list[Vector]) -> list[list[int]]:
    return [[inner(x, y) for y in vectors] for x in vectors]


def minors_gcd(rows: list[Vector]) -> int:
    values: list[int] = []
    for i, j in combinations(range(4), 2):
        values.append(rows[0][i] * rows[1][j] - rows[0][j] * rows[1][i])
    g = 0
    for value in values:
        g = gcd(g, abs(value))
    return g


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main() -> None:
    v = (-1, 0, -1, 1)
    w = (1, -1, -1, 1)
    h = (0, 0, 1, 1)

    g_vw = gram([v, w])
    k = [[-entry for entry in row] for row in g_vw]
    g_vwh = gram([v, w, h])

    print("K3 Picard/HYM gate check")
    print("========================")
    print("v =", v)
    print("w =", w)
    print("h =", h)
    print()

    print("Primitive determinant-seven block")
    print("=================================")
    print("Gram(v,w) =", g_vw)
    print("-Gram(v,w) =", k)
    print("det(-Gram) =", det2(k))
    print("gcd of 2x2 minors of [v;w] =", minors_gcd([v, w]))
    print()

    print("Positive orthogonal class")
    print("=========================")
    print("h^2 =", inner(h, h))
    print("h.v =", inner(h, v))
    print("h.w =", inner(h, w))
    print("Gram(v,w,h) =", g_vwh)
    print()

    print("HYM caveat")
    print("==========")
    print("v^2 =", inner(v, v), "so v is a K3 root if it is Picard.")
    print("A polarization h with h.v=0 is on the v-wall if +/-v is effective.")
    print("Therefore the direct zero-slope line-bundle route is not a finished proof.")
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("rank-two block is primitive in U^2", "PASS", "minor gcd is 1"),
        ("block has determinant seven", "PASS", "det(-Gram)=7"),
        ("positive orthogonal class exists", "PASS", "h=(0,0,1,1), h^2=2"),
        ("naive zero-slope line bundles prove HYM", "FAIL", "(-2)-root wall issue"),
        ("stable higher-rank/Mukai realization", "OPEN", "correct next proof route"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()

