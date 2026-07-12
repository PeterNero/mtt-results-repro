"""Audit the Lens-Nil Bianchi component formulas against exterior calculus.

This checks the formulas as written in the Lens x Nil appendix:

    d eta^i = epsilon_ijk eta^j eta^k,
    d sigma^6 = sigma^4 sigma^5,
    beta_1 = eta^1 eta^2 eta^3 sigma^6,
    beta_3 = eta^3 sigma^4 sigma^5 sigma^6,
    F = f eta^1 eta^2 + h sigma^4 sigma^5.

The audit is intentionally algebraic and coefficient-light.  Overall lambda
and nu factors do not affect the closure and wedge-support conclusions.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations


Form = dict[tuple[int, ...], Fraction]


def basis(*idx: int) -> Form:
    return {tuple(idx): Fraction(1)}


def scale(c: int | Fraction, form: Form) -> Form:
    return {key: Fraction(c) * value for key, value in form.items() if value}


def add(*forms: Form) -> Form:
    out: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


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
    for left_key, left_value in f.items():
        for right_key, right_value in g.items():
            wb = wedge_basis(left_key, right_key)
            if wb is None:
                continue
            sign, key = wb
            out[key] += sign * left_value * right_value
    return {key: value for key, value in out.items() if value}


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


def degree_basis(degree: int) -> list[tuple[int, ...]]:
    return list(combinations(range(1, 7), degree))


def closed_degree_basis(degree: int) -> list[tuple[int, ...]]:
    closed: list[tuple[int, ...]] = []
    for key in degree_basis(degree):
        if not exterior_d({key: Fraction(1)}):
            closed.append(key)
    return closed


def main() -> None:
    eta12 = basis(1, 2)
    sigma45 = basis(4, 5)
    beta1 = basis(1, 2, 3, 6)
    beta2 = basis(1, 2, 4, 5)
    beta3 = basis(3, 4, 5, 6)

    print("Lens-Nil Bianchi consistency audit")
    print("==================================")
    print()

    print("Beta closure")
    print("============")
    print("d beta_1 =", fmt(exterior_d(beta1)))
    print("d beta_2 =", fmt(exterior_d(beta2)))
    print("d beta_3 =", fmt(exterior_d(beta3)))
    print("closure of span{beta_1,beta_3}: only zero, since d beta_1 and d beta_3 have distinct support")
    print()

    print("Abelian flux square as written")
    print("==============================")
    # Use symbolic f=h=1 to expose support.  The general coefficient is 2fh.
    f_form = add(eta12, sigma45)
    print("d(eta12) =", fmt(exterior_d(eta12)))
    print("d(sigma45) =", fmt(exterior_d(sigma45)))
    print("dF =", fmt(exterior_d(f_form)))
    print("F wedge F for f=h=1:", fmt(wedge(f_form, f_form)))
    print("Expected support for general f,h: 2 f h e^1245 = 2 f h beta_2")
    print("No f^2 beta_1 or h^2 beta_3 terms occur for this abelian 2-form.")
    print()

    print("Closed coordinate 4-forms")
    print("=========================")
    closed4 = closed_degree_basis(4)
    print(", ".join("e^" + "".join(map(str, key)) for key in closed4))
    print()

    print("Conclusion")
    print("==========")
    print("As written, nonzero dH = W1 beta_1 + W3 beta_3 is not closed, hence cannot equal d of a 3-form.")
    print("As written, F=f eta12 + h sigma45 has F^2 supported on beta_2, not beta_1 and beta_3.")
    print("Therefore the current Lens-Nil appendix cannot supply the exact Z7 block without correction.")


if __name__ == "__main__":
    main()

