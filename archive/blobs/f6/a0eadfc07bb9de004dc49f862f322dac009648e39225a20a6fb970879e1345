"""Constraint battery for the current ambient Z_1344 MTT flavor candidate."""

from __future__ import annotations

import math
from functools import reduce
from math import gcd

from recursive_quotient_snf_template import invariant_factors
from candidate_quotient_mechanism_scan import dyadic_carry_matrix, block_diag


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def exponent(factors: list[int]) -> int:
    return reduce(lcm, factors, 1)


def order_mod(n: int, k: int) -> int:
    return n // gcd(n, k % n)


def majorana_allowed(n: int, k: int) -> bool:
    return (2 * k) % n == 0


def passfail(label: str, value: bool) -> None:
    print(f"{label:58s} {'PASS' if value else 'FAIL'}")


def main() -> None:
    n = 1344
    k_q = 237
    k_l = 1008
    k_31 = 99
    k_neutral_trivial = 0
    k_neutral_two_torsion = n // 2

    # CKM benchmark convention used by the existing scripts.
    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    delta_q_target = math.asin(target_j / prefactor)
    delta_q = 2.0 * math.pi * k_q / n
    j_q = prefactor * math.sin(delta_q)

    print("Ambient Z_1344 candidate")
    print("========================")
    print(f"N={n}")
    print(f"k_q={k_q}, k_l={k_l}, k_31={k_31}")
    print(f"delta_q={delta_q:.12f}, phase_error={abs(delta_q-delta_q_target):.3e}")
    print(f"J={j_q:.12e}, J_error={abs(j_q-target_j):.3e}")
    print()

    print("Finite relation matrix")
    print("======================")
    carry = dyadic_carry_matrix(6)
    wilson7 = [[7]]
    family3 = [[3]]
    matrix = block_diag(block_diag(carry, wilson7), family3)
    factors, free_rank = invariant_factors(matrix)
    print("torsion factors:", factors)
    print("exponent:", exponent(factors))
    print("free rank:", free_rank)
    print()

    print("Pass/fail")
    print("=========")
    passfail("ambient finite torsion is Z_1344", factors == [1344])
    passfail("selected CKM character order is 448", order_mod(n, k_q) == 448)
    passfail("selected lepton branch has order 4", order_mod(n, k_l) == 4)
    passfail("lepton branch is -pi/2 mod 2pi", k_l == 3 * n // 4)
    passfail("pairwise phase-sum closes", (k_q + k_l + k_31) % n == 0)
    passfail("all CP labels are family-trivial", all(k % 3 == 0 for k in (k_q, k_l, k_31)))
    passfail("CP labels are not Majorana self-characters", not any(majorana_allowed(n, k) for k in (k_q, k_l, k_31)))
    passfail("trivial neutral is Majorana-admissible", majorana_allowed(n, k_neutral_trivial))
    passfail("two-torsion neutral is Majorana-admissible", majorana_allowed(n, k_neutral_two_torsion))
    passfail("neutral two-torsion is family-trivial", k_neutral_two_torsion % 3 == 0)
    print()

    print("Orders")
    print("======")
    for label, k in (
        ("k_q", k_q),
        ("k_l", k_l),
        ("k_31", k_31),
        ("k_N0", k_neutral_trivial),
        ("k_N2", k_neutral_two_torsion),
    ):
        print(
            f"{label:5s} k={k:4d} order={order_mod(n, k):4d} "
            f"family_trivial={k % 3 == 0!s:5s} "
            f"Majorana={majorana_allowed(n, k)}"
        )


if __name__ == "__main__":
    main()
