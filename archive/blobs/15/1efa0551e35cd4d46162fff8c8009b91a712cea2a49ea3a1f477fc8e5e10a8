"""Check closure of the Lens-Nil invariant beta component forms.

This guards against a common overstatement.  The beta_i used in the Lens x Nil
Bianchi system form an invariant component basis, but the individual forms need
not be closed de Rham representatives.  The descent proof should therefore be
phrased in terms of the integral component/differential-cohomology lattice of
the Bianchi system unless closed combinations are explicitly identified.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction


Form = dict[tuple[int, ...], Fraction]


def wedge_basis(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    if set(a) & set(b):
        return None
    merged = list(a) + list(b)
    sign = 1
    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                sign *= -1
    return sign, tuple(sorted(merged))


def wedge(f: Form, g: Form) -> Form:
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for a, ca in f.items():
        for b, cb in g.items():
            wb = wedge_basis(a, b)
            if wb is None:
                continue
            sign, basis = wb
            out[basis] += ca * cb * sign
    return {basis: coeff for basis, coeff in out.items() if coeff}


def basis(*idx: int) -> Form:
    return {tuple(idx): Fraction(1)}


def add(*forms: Form) -> Form:
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for form in forms:
        for basis_key, coeff in form.items():
            out[basis_key] += coeff
    return {basis_key: coeff for basis_key, coeff in out.items() if coeff}


def scale(c: int | Fraction, form: Form) -> Form:
    return {basis_key: Fraction(c) * coeff for basis_key, coeff in form.items()}


# Basis convention:
# 1,2,3 = eta^1,eta^2,eta^3 on L(3,1)
# 4,5,6 = sigma^4,sigma^5,sigma^6 on Nil_3
# Coefficients are normalized to expose support; overall lambda/nu factors do
# not affect whether the forms are closed.
d_basis: dict[int, Form] = {
    1: basis(2, 3),
    2: scale(-1, basis(1, 3)),
    3: basis(1, 2),
    4: {},
    5: {},
    6: basis(4, 5),
}


def exterior_d(form: Form) -> Form:
    out: Form = {}
    for monomial, coeff in form.items():
        terms: list[Form] = []
        for i, idx in enumerate(monomial):
            left = basis(*monomial[:i]) if i else {(): Fraction(1)}
            right = basis(*monomial[i + 1 :]) if i + 1 < len(monomial) else {(): Fraction(1)}
            term = wedge(wedge(left, d_basis[idx]), right)
            terms.append(scale(coeff * ((-1) ** i), term))
        out = add(out, *terms)
    return out


def fmt(form: Form) -> str:
    if not form:
        return "0"
    pieces = []
    for monomial, coeff in sorted(form.items()):
        name = "".join(str(i) for i in monomial)
        pieces.append(f"{coeff:+g} e^{name}")
    return " ".join(pieces).lstrip("+")


def main() -> None:
    beta1 = basis(1, 2, 3, 6)
    beta3 = basis(3, 4, 5, 6)
    print("Lens-Nil beta closure check")
    print("===========================")
    print("beta_1 = eta^1 eta^2 eta^3 sigma^6")
    print("beta_3 = eta^3 sigma^4 sigma^5 sigma^6")
    print("d beta_1 =", fmt(exterior_d(beta1)))
    print("d beta_3 =", fmt(exterior_d(beta3)))
    print()
    print("Conclusion")
    print("==========")
    print("The individual beta component forms are not closed under the Lens-Nil structure equations.")
    print("Use them as an invariant Bianchi component basis, not automatically as H^4 generators.")


if __name__ == "__main__":
    main()
