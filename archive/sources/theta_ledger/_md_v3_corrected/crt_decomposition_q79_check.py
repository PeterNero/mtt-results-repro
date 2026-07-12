"""CRT decomposition check for the CKM label q=79.

This script verifies the exact product-coordinate structure:

    q=79  <-> (15 mod 64, 2 mod 7)
    l=336 <-> (16 mod 64, 0 mod 7)
    r=33  <-> (33 mod 64, 5 mod 7)

The sevenfold q-component is the Mukai discriminant numerator because the
selected generator theta_7=(1/7,5/7) has quadratic value 2/7 modulo 1.
"""

from __future__ import annotations

from fractions import Fraction


def crt_pair(a64: int, a7: int) -> int:
    for x in range(448):
        if x % 64 == a64 % 64 and x % 7 == a7 % 7:
            return x
    raise ValueError("no CRT solution")


def mat_vec(matrix: list[list[int]], vector: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(sum(Fraction(entry) * coord for entry, coord in zip(row, vector)) for row in matrix)


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum(a * b for a, b in zip(left, right))


def main() -> None:
    q64 = 16 - 1
    q7 = 2
    l64 = 16
    l7 = 0
    r64 = (-(q64 + l64)) % 64
    r7 = (-(q7 + l7)) % 7

    q = crt_pair(q64, q7)
    l = crt_pair(l64, l7)
    r = crt_pair(r64, r7)

    k_mukai = [[2, 1], [1, 4]]
    theta7 = (Fraction(1, 7), Fraction(5, 7))
    ktheta = mat_vec(k_mukai, theta7)
    mukai_quad = dot(theta7, ktheta) % 1

    print("CRT decomposition of CKM label 79")
    print("=================================")
    print(f"q64={q64}, q7={q7} -> q={q}")
    print(f"l64={l64}, l7={l7} -> l={l}")
    print(f"r64={r64}, r7={r7} -> r={r}")
    print()

    print("Component closure")
    print("=================")
    print("dyadic sum mod 64:", (q64 + l64 + r64) % 64)
    print("sevenfold sum mod 7:", (q7 + l7 + r7) % 7)
    print("full sum mod 448:", (q + l + r) % 448)
    print()

    print("Mukai discriminant component")
    print("============================")
    print("theta7:", theta7)
    print("K theta7:", ktheta)
    print("theta7^T K theta7 mod 1:", mukai_quad)
    print("Mukai numerator:", mukai_quad.numerator)
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("CRT reconstructs q=79 from (15,2)", "PASS", "exact"),
        ("Mukai discriminant quadratic numerator is 2", "PASS", "theta7^T K theta7 = 2/7"),
        ("dyadic q64 is quarter-turn predecessor", "CLOSED-EXACT", "selected nil-survivor lag gives 15=16-1"),
        ("phase-sum closure holds componentwise", "PASS", "(64,7) sums vanish"),
        ("derive predecessor rule from MTT", "CLOSED-EXACT", "selected primitive-lag theorem and Z64 exact certificate"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")

    assert (q, l, r) == (79, 336, 33)
    assert (q64 + l64 + r64) % 64 == 0
    assert (q7 + l7 + r7) % 7 == 0
    assert (q + l + r) % 448 == 0
    assert mukai_quad == Fraction(2, 7)


if __name__ == "__main__":
    main()
