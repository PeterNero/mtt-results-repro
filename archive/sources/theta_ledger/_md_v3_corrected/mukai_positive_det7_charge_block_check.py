"""Mukai positive determinant-seven charge block for the Fu-Yau/K3 route.

The earlier K3 H^2 block used a negative-definite rank-two lattice whose
negative Gram matrix was

    [[2, 1],
     [1, 4]].

That proves the arithmetic but runs into a root-wall obstruction for an
anti-self-dual (1,1) Fu-Yau curvature realization: an even rank-two determinant
seven lattice necessarily represents norm 2.

This script records the better replacement.  Work on a Picard-rank-one K3 with
primitive ample class H and H^2=2.  In the algebraic Mukai lattice use

    a = (5, H, 0)
    b = (7, 3H, 1)

where a Mukai vector is written as (rank, nH, s).  With the Mukai pairing

    <(r,nH,s),(r',mH,s')> = 2*n*m - r*s' - r'*s,

these have Gram matrix exactly [[2,1],[1,4]], hence cokernel Z_7.
"""

from __future__ import annotations

from math import gcd

from recursive_quotient_snf_template import invariant_factors


MukaiVector = tuple[int, int, int]  # (rank, coefficient of H, s), H^2=2


def mukai_pair(x: MukaiVector, y: MukaiVector) -> int:
    r, n, s = x
    rp, m, sp = y
    return 2 * n * m - r * sp - rp * s


def gram(vectors: list[MukaiVector]) -> list[list[int]]:
    return [[mukai_pair(x, y) for y in vectors] for x in vectors]


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def c2(vector: MukaiVector) -> int:
    r, n, s = vector
    # On a K3, v(E)=(r,c1,c1^2/2-c2+r).  Here c1=nH and H^2=2.
    return r + n * n - s


def primitive(vector: MukaiVector) -> bool:
    r, n, s = vector
    return gcd(gcd(abs(r), abs(n)), abs(s)) == 1


def reduced_even_det7_root_argument() -> str:
    return (
        "In a reduced even positive rank-two lattice K=[[2a,b],[b,2c]] "
        "with det(K)=7, one has |b|<=a<=c.  Hence "
        "7=4ac-b^2 >= 4a^2-a^2 = 3a^2, so a=1.  The lattice therefore "
        "represents norm 2."
    )


def main() -> None:
    a = (5, 1, 0)
    b = (7, 3, 1)
    k = gram([a, b])

    print("Mukai positive determinant-seven charge block")
    print("============================================")
    print("K3 base: Picard rank one, primitive H with H^2=2")
    print("a = (rank, nH, s) =", a)
    print("b = (rank, nH, s) =", b)
    print("c2(a) =", c2(a))
    print("c2(b) =", c2(b))
    print("primitive(a) =", primitive(a))
    print("primitive(b) =", primitive(b))
    print("Gram(a,b) =", k)
    print("det Gram =", det2(k))
    print("SNF(Gram) =", invariant_factors(k))
    print()

    assert primitive(a)
    assert primitive(b)
    assert c2(a) == 6
    assert c2(b) == 15
    assert k == [[2, 1], [1, 4]]
    assert det2(k) == 7
    assert invariant_factors(k) == ([7], 0)

    print("Why this replaces the H^2 root-wall route")
    print("==========================================")
    print(reduced_even_det7_root_argument())
    print()

    print("Gate status")
    print("===========")
    gates = [
        (
            "negative H^2 curvature-pair route",
            "OBSTRUCTED",
            "even determinant-seven rank-two lattice forces a norm-two root",
        ),
        (
            "positive Mukai charge matrix has SNF [7]",
            "PASS",
            "explicit primitive Mukai vectors a,b",
        ),
        (
            "stable sheaf existence on K3",
            "STANDARD THEOREM",
            "primitive positive Mukai vectors with v^2 >= -2",
        ),
        (
            "HYM connection",
            "STANDARD IF LOCALLY FREE/STABLE",
            "Hitchin-Kobayashi/DUY; Fu-Yau total-space version still separate",
        ),
        (
            "Fu-Yau anomaly and MTT selection",
            "OPEN",
            "must prove this charge block is selected, not merely allowed",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
