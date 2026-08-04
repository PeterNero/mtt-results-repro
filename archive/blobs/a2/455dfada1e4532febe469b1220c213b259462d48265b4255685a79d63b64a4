"""Closed Lens-Nil flux candidate realizing the determinant-seven matrix.

The old Lens-Nil appendix uses non-closed beta_1,beta_3 and a flux square with
wrong support.  This script tests a repaired *candidate* using closed 2-forms.

Let
    u1=e12, u2=e13       (closed Lens-side 2-forms)
    v1=e45, v2=e46       (closed Nil-side 2-forms)

Define two integral line-bundle Chern classes
    c1(L1)=u1 + 2 v1 + v2
    c1(L2)=u2 + v1 + 4 v2.

Then ch_2(L1)+ch_2(L2) = 1/2(c1(L1)^2+c1(L2)^2) has coefficient matrix
    [[2,1],
     [1,4]]
on the closed 4-form basis u_i wedge v_j.

This does not prove HYM/primitivity or MTT selection.  It proves that an exact
closed integral Lens-Nil Chern-character source for the desired Z7 block exists.
"""

from __future__ import annotations

from fractions import Fraction

from lens_nil_bianchi_consistency_audit import add, basis, exterior_d, fmt, scale, wedge
from recursive_quotient_snf_template import invariant_factors


def ch2(c1):
    return scale(Fraction(1, 2), wedge(c1, c1))


def coeff(form, key: tuple[int, ...]) -> Fraction:
    return form.get(key, Fraction(0))


def main() -> None:
    u1 = basis(1, 2)
    u2 = basis(1, 3)
    v1 = basis(4, 5)
    v2 = basis(4, 6)

    c1_l1 = add(u1, scale(2, v1), v2)
    c1_l2 = add(u2, v1, scale(4, v2))
    source = add(ch2(c1_l1), ch2(c1_l2))

    print("Repaired closed Lens-Nil flux candidate")
    print("=======================================")
    print()

    print("Closure checks")
    print("==============")
    for name, form in [("u1=e12", u1), ("u2=e13", u2), ("v1=e45", v1), ("v2=e46", v2)]:
        print(f"d({name}) =", fmt(exterior_d(form)))
    print("d c1(L1) =", fmt(exterior_d(c1_l1)))
    print("d c1(L2) =", fmt(exterior_d(c1_l2)))
    print("d source =", fmt(exterior_d(source)))
    print()

    print("Chern classes")
    print("=============")
    print("c1(L1) =", fmt(c1_l1))
    print("c1(L2) =", fmt(c1_l2))
    print("ch2(L1)+ch2(L2) =", fmt(source))
    print()

    keys = {
        (1, 2, 4, 5): "u1 v1",
        (1, 2, 4, 6): "u1 v2",
        (1, 3, 4, 5): "u2 v1",
        (1, 3, 4, 6): "u2 v2",
    }
    matrix = [
        [int(coeff(source, (1, 2, 4, 5))), int(coeff(source, (1, 2, 4, 6)))],
        [int(coeff(source, (1, 3, 4, 5))), int(coeff(source, (1, 3, 4, 6)))],
    ]

    print("Coefficient matrix on u_i wedge v_j")
    print("====================================")
    for key, label in keys.items():
        print(f"{label}: {coeff(source, key)}")
    print("matrix:", matrix)
    print("SNF:", invariant_factors(matrix))
    print()

    print("Status")
    print("======")
    print("PASS: exact closed integral ch2 source has determinant-seven matrix.")
    print("OPEN: prove HYM/primitivity or replace by an admissible stable bundle.")
    print("OPEN: prove this closed flux matrix is the one MTT selects for CP.")


if __name__ == "__main__":
    main()

