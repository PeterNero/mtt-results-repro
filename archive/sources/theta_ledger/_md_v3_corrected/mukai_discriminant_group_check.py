"""Discriminant-group check for the Mukai Z7 block.

For an integral lattice P with Gram matrix K, the discriminant group is

    A_P = P^*/P.

In a basis of P, P^* is represented by rational vectors theta with

    K theta in Z^n.

Thus A_P is naturally coker K, and its order is |det K|.  For the positive
Mukai block K=[[2,1],[1,4]], A_P ~= Z_7.  This is a more canonical version of
the odd CP character quotient.
"""

from __future__ import annotations

from fractions import Fraction

from recursive_quotient_snf_template import invariant_factors


Vector = tuple[Fraction, Fraction]
Matrix = list[list[int]]


def det2(matrix: Matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(sum(Fraction(entry) * coord for entry, coord in zip(row, vector)) for row in matrix)  # type: ignore[return-value]


def bilinear_mod1(matrix: Matrix, x: Vector, y: Vector) -> Fraction:
    ky = mat_vec(matrix, y)
    value = sum(xi * yi for xi, yi in zip(x, ky))
    return value % 1


def order_mod_lattice(vector: Vector) -> int:
    for n in range(1, 100):
        if all((n * coord) % 1 == 0 for coord in vector):
            return n
    raise ValueError("order not found")


def inverse_2x2(matrix: Matrix) -> list[list[Fraction]]:
    d = det2(matrix)
    return [
        [Fraction(matrix[1][1], d), Fraction(-matrix[0][1], d)],
        [Fraction(-matrix[1][0], d), Fraction(matrix[0][0], d)],
    ]


def main() -> None:
    k = [[2, 1], [1, 4]]
    theta = (Fraction(1, 7), Fraction(5, 7))

    print("Mukai discriminant-group check")
    print("==============================")
    print("K_Mukai =", k)
    print("det(K_Mukai) =", det2(k))
    print("SNF(K_Mukai) =", invariant_factors(k))
    print("K_Mukai^-1 =", inverse_2x2(k))
    print()

    assert det2(k) == 7
    assert invariant_factors(k) == ([7], 0)

    print("Discriminant generator")
    print("======================")
    print("theta =", theta)
    print("K theta =", mat_vec(k, theta))
    print("order of theta in P*/P =", order_mod_lattice(theta))
    print("b(theta,theta) mod 1 =", bilinear_mod1(k, theta, theta))
    print()

    assert mat_vec(k, theta) == (1, 3)
    assert order_mod_lattice(theta) == 7
    assert bilinear_mod1(k, theta, theta) == Fraction(2, 7)

    print("All discriminant classes")
    print("========================")
    for j in range(7):
        cls = ((j * theta[0]) % 1, (j * theta[1]) % 1)
        k_cls = mat_vec(k, cls)
        pairing = bilinear_mod1(k, cls, theta)
        print(f"j={j}: class={cls}, K class={k_cls}, b(class,theta)={pairing}")
        assert all(coord.denominator == 1 for coord in k_cls)
    print()

    print("Gate status")
    print("===========")
    gates = [
        (
            "Mukai block defines an integral rank-two lattice P",
            "PASS",
            "Gram matrix K_Mukai",
        ),
        (
            "discriminant group A_P=P*/P has order seven",
            "PASS",
            "det K=7",
        ),
        (
            "A_P is cyclic",
            "PASS",
            "SNF [7]",
        ),
        (
            "discriminant character generator is explicit",
            "PASS",
            "theta=(1/7,5/7)",
        ),
        (
            "MTT CP odd sector equals Hom(A_P,U(1))",
            "CLOSED-CHARGE",
            "Z7 charge-sector certificate supplies the global Fu-Yau/Mukai sector",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
