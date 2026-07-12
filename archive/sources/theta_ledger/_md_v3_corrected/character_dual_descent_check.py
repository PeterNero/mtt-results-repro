"""Formal character-dual checks for the Lens-Nil Z_7 descent.

If K is the relation matrix on an integral lattice Lambda_Z, then the unitary
characters of coker(K) are solutions of K^T theta = 0 in (R/Z)^n.  For the
Lens-Nil candidate K=[[2,1],[1,4]], the matrix is symmetric and the solution
group has seven elements.
"""

from __future__ import annotations

from fractions import Fraction

from recursive_quotient_snf_template import invariant_factors


def matvec_mod(matrix: list[list[int]], vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    out: list[Fraction] = []
    for row in matrix:
        value = sum(Fraction(entry) * vector[i] for i, entry in enumerate(row))
        out.append(value % 1)
    return tuple(out)


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def main() -> None:
    k = [[2, 1], [1, 4]]
    kt = transpose(k)
    factors, free_rank = invariant_factors(k)
    dual_factors, dual_free_rank = invariant_factors(kt)

    print("Character-dual Lens-Nil descent check")
    print("=====================================")
    print("K:", k)
    print("K^T:", kt)
    print("SNF(K):", factors, "free rank:", free_rank)
    print("SNF(K^T):", dual_factors, "free rank:", dual_free_rank)
    print()

    assert factors == [7] and free_rank == 0
    assert dual_factors == [7] and dual_free_rank == 0

    print("Solutions of K^T theta = 0 in (R/Z)^2")
    print("======================================")
    solutions: list[tuple[Fraction, Fraction]] = []
    for j in range(7):
        theta = (Fraction(j, 7), Fraction(-2 * j, 7) % 1)
        residual = matvec_mod(kt, theta)
        print(f"j={j}: w={theta[0]}, n={theta[1]}, residual={residual}")
        assert residual == (Fraction(0), Fraction(0))
        solutions.append(theta)

    assert len(set(solutions)) == 7
    print()

    print("Generator")
    print("=========")
    print("(w,n) = (1/7, 5/7) = (1/7, -2/7 mod 1)")
    print("order: 7")
    print()

    print("Gate status")
    print("===========")
    gates = [
        (
            "CP phases are Wilson/holonomy data",
            "CORPUS-SUPPORTED",
            "finite projection and topology-only papers",
        ),
        (
            "families are finite character sectors",
            "CORPUS-SUPPORTED",
            "central circle/book papers",
        ),
        (
            "fixed integral gerbe/cohomology lattice exists",
            "CORPUS-SUPPORTED",
            "Strominger/M-theory papers",
        ),
        (
            "dual character equations use K^T",
            "FORMAL PASS",
            "standard Hom(coker K,U(1)) calculation",
        ),
        (
            "Lens-Nil K is symmetric, so character rows match component rows",
            "FORMAL PASS",
            "K^T=K",
        ),
        (
            "residual w,n are exactly these Lens-Nil quotient characters",
            "OPEN",
            "main MTT identification lemma",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()

