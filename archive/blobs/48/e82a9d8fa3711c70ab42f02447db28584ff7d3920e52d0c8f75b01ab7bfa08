"""Same-slope HYM obstruction for using the Mukai Z7 block as bundle summands.

The positive Mukai block

    a=(5,H,0), b=(7,3H,1), H^2=2

has Gram matrix [[2,1],[1,4]], but the two vectors have different H-slopes.
Therefore they should not be described as two summands of a single polystable
HYM gauge bundle.

More generally, two Picard-rank-one Mukai vectors with the same slope cannot
have determinant-seven Gram matrix.  If

    x=(r,nH,s), y=(R,NH,S), H^2=2, and n/r = N/R,

write A=n^2/r-s and B=N^2/R-S.  Then

    x^2 = 2rA, y^2 = 2RB, x.y = rB + RA,
    det Gram(x,y) = -(rB-RA)^2.

So the Gram determinant is a negative rational square.  It cannot be +7, and
it cannot have absolute value 7 over rational data.  This is an obstruction to
the "two same-slope HYM summands with determinant-seven Gram" route, not an
obstruction to using the Mukai block as a charge-lattice block.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


Vector = tuple[int, int, int]  # (rank, n, s), with c1=nH and H^2=2


def mukai_pair(x: Vector, y: Vector) -> int:
    r, n, s = x
    rp, m, sp = y
    return 2 * n * m - r * sp - rp * s


def slope(x: Vector) -> Fraction:
    r, n, _ = x
    return Fraction(2 * n, r)


def det2(matrix: list[list[int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def gram(x: Vector, y: Vector) -> list[list[int]]:
    return [[mukai_pair(x, x), mukai_pair(x, y)], [mukai_pair(y, x), mukai_pair(y, y)]]


def primitive(x: Vector) -> bool:
    r, n, s = x
    return gcd(gcd(abs(r), abs(n)), abs(s)) == 1


def search_same_slope_det7(limit: int = 8) -> list[tuple[Vector, Vector, int]]:
    hits: list[tuple[Vector, Vector, int]] = []
    vectors = [
        (r, n, s)
        for r in range(1, limit + 1)
        for n in range(-limit, limit + 1)
        for s in range(-2 * limit, 2 * limit + 1)
        if primitive((r, n, s))
    ]
    for i, x in enumerate(vectors):
        for y in vectors[i + 1 :]:
            if slope(x) != slope(y):
                continue
            d = det2(gram(x, y))
            if abs(d) == 7:
                hits.append((x, y, d))
    return hits


def main() -> None:
    a = (5, 1, 0)
    b = (7, 3, 1)
    k = gram(a, b)

    print("Mukai same-slope HYM obstruction check")
    print("======================================")
    print("a =", a, "slope =", slope(a))
    print("b =", b, "slope =", slope(b))
    print("Gram(a,b) =", k)
    print("det Gram(a,b) =", det2(k))
    print()

    assert k == [[2, 1], [1, 4]]
    assert det2(k) == 7
    assert slope(a) != slope(b)

    print("Same-slope determinant formula")
    print("==============================")
    print("If n/r=N/R, then det Gram(x,y)=-(rB-RA)^2.")
    print("So a same-slope determinant-seven Gram block is impossible.")
    print()

    hits = search_same_slope_det7()
    print("Bounded same-slope search")
    print("=========================")
    print("limit: rank<=8, |n|<=8, |s|<=16")
    print("same-slope primitive pairs with |det Gram|=7:", len(hits))
    print()
    assert not hits

    print("Interpretation")
    print("==============")
    print("The Mukai Z7 block is valid as a charge-lattice block.")
    print("It is not yet a two-summand polystable HYM bundle construction.")


if __name__ == "__main__":
    main()
