"""HYM/primitivity gate for the repaired closed Lens-Nil flux candidate.

For the displayed SU(3) structure with real pairs
    (1,2), (3,6), (4,5),
we test the invariant closed primitive (1,1) two-form space.

This is a gate check: the closed Chern-character matrix can realize the Z7
block, but simple line-bundle representatives must also be type (1,1) and
primitive to qualify as HYM in the invariant ansatz.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

from lens_nil_bianchi_consistency_audit import add, basis, exterior_d, fmt, scale, wedge


Form = dict[tuple[int, ...], Fraction]


def neg(form: Form) -> Form:
    return {key: -value for key, value in form.items()}


J_ON_ONE_FORMS: dict[int, Form] = {
    1: basis(2),
    2: scale(-1, basis(1)),
    3: basis(6),
    6: scale(-1, basis(3)),
    4: basis(5),
    5: scale(-1, basis(4)),
}


def j_star(form: Form) -> Form:
    out: Form = {}
    for monomial, coeff in form.items():
        term: Form = {(): coeff}
        for idx in monomial:
            term = wedge(term, J_ON_ONE_FORMS[idx])
        out = add(out, term)
    return out


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivots: list[int] = []
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [a[i][j] - factor * a[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return a, pivots


def nullspace(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    cols = len(matrix[0]) if matrix else 0
    free_cols = [j for j in range(cols) if j not in pivots]
    out: list[list[Fraction]] = []
    for free_col in free_cols:
        vec = [Fraction(0) for _ in range(cols)]
        vec[free_col] = Fraction(1)
        for row_idx, pivot_col in enumerate(pivots):
            vec[pivot_col] = -reduced[row_idx][free_col]
        out.append(vec)
    return out


def main() -> None:
    two_basis = list(combinations(range(1, 7), 2))
    j_form = add(basis(1, 2), basis(3, 6), basis(4, 5))
    j_squared = wedge(j_form, j_form)

    def conditions_for(form: Form) -> list[Form]:
        return [
            exterior_d(form),
            add(j_star(form), neg(form)),
            wedge(form, j_squared),
        ]

    rows: list[list[Fraction]] = []
    for condition_index in range(3):
        target_keys = sorted(
            set().union(
                *[
                    set(conditions_for({two_key: Fraction(1)})[condition_index].keys())
                    for two_key in two_basis
                ]
            )
        )
        for target_key in target_keys:
            row = [
                conditions_for({two_key: Fraction(1)})[condition_index].get(target_key, Fraction(0))
                for two_key in two_basis
            ]
            if any(row):
                rows.append(row)

    ns = nullspace(rows)

    print("Repaired Lens-Nil HYM gate check")
    print("================================")
    print("SU(3) pairs: (1,2), (3,6), (4,5)")
    print("conditions: closed, J-invariant (1,1), primitive")
    print()
    print("dimension:", len(ns))
    for vec in ns:
        form = {key: coeff for key, coeff in zip(two_basis, vec) if coeff}
        print("basis:", fmt(form))
        print("  d =", fmt(exterior_d(form)))
        print("  J*F-F =", fmt(add(j_star(form), neg(form))))
        print("  F wedge J^2 =", fmt(wedge(form, j_squared)))

    u1 = basis(1, 2)
    u2 = basis(1, 3)
    v1 = basis(4, 5)
    v2 = basis(4, 6)
    c1_l1 = add(u1, scale(2, v1), v2)
    c1_l2 = add(u2, v1, scale(4, v2))
    print()
    print("Simple repaired line classes")
    print("============================")
    for name, form in [("c1(L1)", c1_l1), ("c1(L2)", c1_l2)]:
        print(name, "=", fmt(form))
        print("  d =", fmt(exterior_d(form)))
        print("  J*F-F =", fmt(add(j_star(form), neg(form))))
        print("  F wedge J^2 =", fmt(wedge(form, j_squared)))
    print()
    print("Conclusion")
    print("==========")
    print("The simple closed line-bundle repair realizes the Z7 matrix but fails the invariant HYM gate.")
    print("A full repair needs a stable higher-rank bundle, a different admissible complex structure,")
    print("or another Z7 source.")


if __name__ == "__main__":
    main()

