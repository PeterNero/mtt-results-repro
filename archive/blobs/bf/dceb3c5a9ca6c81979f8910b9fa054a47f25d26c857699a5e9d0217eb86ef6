"""Character-selection gate for the Mukai Z7 charge block.

The positive Mukai block gives an integral relation matrix

    K = [[2, 1],
         [1, 4]]

with coker K ~= Z_7.  The CP characters should live in the unitary dual
Hom(coker K, U(1)), equivalently in the solutions of K^T theta = 0 mod 1.

This script proves the formal character arithmetic and keeps the MTT-specific
selection assumptions explicit.
"""

from __future__ import annotations

from fractions import Fraction

from recursive_quotient_snf_template import invariant_factors


def mat_vec_mod1(matrix: list[list[int]], vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    out = []
    for row in matrix:
        value = sum(Fraction(entry) * coord for entry, coord in zip(row, vector))
        out.append(value % 1)
    return tuple(out)  # type: ignore[return-value]


def order_mod1(vector: tuple[Fraction, Fraction]) -> int:
    for n in range(1, 100):
        if all((n * coord) % 1 == 0 for coord in vector):
            return n
    raise ValueError("order not found")


def main() -> None:
    k = [[2, 1], [1, 4]]
    kt = [[2, 1], [1, 4]]
    generator = (Fraction(1, 7), Fraction(5, 7))
    solutions = [(j * generator[0] % 1, j * generator[1] % 1) for j in range(7)]

    print("Mukai character-selection gate check")
    print("====================================")
    print("K_Mukai =", k)
    print("SNF(K_Mukai) =", invariant_factors(k))
    print("character generator theta =", generator)
    print("order(theta) =", order_mod1(generator))
    print()

    assert invariant_factors(k) == ([7], 0)
    assert order_mod1(generator) == 7

    print("Characters solving K^T theta = 0 mod 1")
    print("=======================================")
    for j, solution in enumerate(solutions):
        residual = mat_vec_mod1(kt, solution)
        print(f"j={j}: theta={solution}, residual={residual}")
        assert residual == (0, 0)
    print()

    print("Gate status")
    print("===========")
    gates = [
        (
            "Mukai block is an integral charge-pairing matrix",
            "PASS",
            "explicit primitive vectors a=(5,H,0), b=(7,3H,1)",
        ),
        (
            "coker K_Mukai has torsion Z7",
            "PASS",
            "SNF [7]",
        ),
        (
            "unitary dual Hom(coker K_Mukai,U(1)) is Z7",
            "PASS",
            "solutions of K^T theta=0",
        ),
        (
            "MTT fixed sector selects quotient by K_Mukai",
            "OPEN",
            "selection map still needed",
        ),
        (
            "CP labels are these unitary characters",
            "OPEN",
            "character-identification theorem still needed",
        ),
        (
            "same data form one HYM polystable bundle",
            "NOT CLAIMED",
            "same-slope obstruction is separate",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
