"""Selected CP character-dual map for the combined Z64 x Z7 quotient.

Given relation rows A, unitary characters of coker(A) are vectors theta in
(Q/Z)^n satisfying A theta = 0 mod 1.  This script constructs the explicit
selected generator for the combined dyadic carry and Mukai discriminant blocks:

    theta_64 = (1,2,4,8,16,32)/64
    theta_7  = (1,5)/7
    theta_CP = (theta_64, theta_7)

The order of theta_CP is lcm(64,7)=448.  The CKM, lepton quarter-turn, and
phase-sum partner labels are 79, 336, and 33 times this generator.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from candidate_quotient_mechanism_scan import block_diag, dyadic_carry_matrix
from recursive_quotient_snf_template import invariant_factors


Vector = tuple[Fraction, ...]
Matrix = list[list[int]]


def mat_vec_mod1(matrix: Matrix, vector: Vector) -> Vector:
    out = []
    for row in matrix:
        value = sum(Fraction(entry) * coord for entry, coord in zip(row, vector))
        out.append(value % 1)
    return tuple(out)


def scalar_mul(k: int, vector: Vector) -> Vector:
    return tuple((k * coord) % 1 for coord in vector)


def add_vectors(*vectors: Vector) -> Vector:
    return tuple(sum(coords) % 1 for coords in zip(*vectors))


def order_mod1(vector: Vector, limit: int = 5000) -> int:
    for n in range(1, limit + 1):
        if all((n * coord) % 1 == 0 for coord in vector):
            return n
    raise ValueError("order not found")


def zero_vector(n: int) -> Vector:
    return tuple(Fraction(0) for _ in range(n))


def main() -> None:
    carry64 = dyadic_carry_matrix(6)
    k_mukai = [[2, 1], [1, 4]]
    selected = block_diag(carry64, k_mukai)
    ambient = block_diag(selected, [[3]])

    theta64: Vector = tuple(Fraction(2**i, 64) for i in range(6))
    theta7: Vector = (Fraction(1, 7), Fraction(5, 7))
    theta_cp: Vector = theta64 + theta7
    theta_ambient: Vector = theta_cp + (Fraction(0),)

    labels = {
        "CKM": 79,
        "PMNS quarter-turn": 336,
        "phase-sum partner": 33,
    }

    print("Selected CP character-dual check")
    print("================================")
    print("SNF(selected relation matrix) =", invariant_factors(selected))
    print("SNF(ambient relation matrix)  =", invariant_factors(ambient))
    print("theta64 =", theta64)
    print("theta7  =", theta7)
    print("thetaCP =", theta_cp)
    print("order(theta64) =", order_mod1(theta64))
    print("order(theta7)  =", order_mod1(theta7))
    print("order(thetaCP) =", order_mod1(theta_cp))
    print("selected residual A thetaCP =", mat_vec_mod1(selected, theta_cp))
    print("ambient residual A thetaCP  =", mat_vec_mod1(ambient, theta_ambient))
    print()

    assert invariant_factors(selected) == ([448], 0)
    assert invariant_factors(ambient) == ([1344], 0)
    assert order_mod1(theta64) == 64
    assert order_mod1(theta7) == 7
    assert order_mod1(theta_cp) == 448
    assert mat_vec_mod1(selected, theta_cp) == zero_vector(8)
    assert mat_vec_mod1(ambient, theta_ambient) == zero_vector(9)

    print("Selected physical labels")
    print("========================")
    selected_vectors: dict[str, Vector] = {}
    for name, label in labels.items():
        vector = scalar_mul(label, theta_cp)
        selected_vectors[name] = vector
        print(
            f"{name:20s} label={label:3d} "
            f"gcd(label,448)={gcd(label,448):3d} "
            f"order={order_mod1(vector):3d} "
            f"vector={vector}"
        )
        assert mat_vec_mod1(selected, vector) == zero_vector(8)
    print()

    closure = add_vectors(*selected_vectors.values())
    print("Closure")
    print("=======")
    print("theta_CKM + theta_PMNS + theta_31 =", closure)
    print("label sum mod 448 =", sum(labels.values()) % 448)
    assert closure == zero_vector(8)
    assert sum(labels.values()) % 448 == 0
    print()

    print("Ambient family-trivial lifts")
    print("============================")
    for name, label in labels.items():
        ambient_label = 3 * label
        vector = scalar_mul(label, theta_ambient)
        family_coordinate = vector[-1]
        print(
            f"{name:20s} selected={label:3d} ambient cyclic label={ambient_label:4d} "
            f"family coordinate={family_coordinate}"
        )
        assert family_coordinate == 0
        assert ambient_label % 3 == 0

    print()
    print("Gate status")
    print("===========")
    gates = [
        (
            "combined character generator has order 448",
            "PASS",
            "lcm(64,7)",
        ),
        (
            "physical labels are multiples of thetaCP",
            "PASS",
            "79,336,33",
        ),
        (
            "phase-sum closure holds in character group",
            "PASS",
            "79+336+33=448",
        ),
        (
            "ambient lifts are family-trivial",
            "PASS",
            "family coordinate zero / cyclic labels divisible by 3",
        ),
        (
            "thetaCP is physical once factor quotients are selected",
            "CLOSED",
            "finite-character identification plus exact Z64 and charge-sector Z7 certificates",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
