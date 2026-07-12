"""Lift the N=1 phase coboundary obstruction to finite solvable carriers.

The N=1 phase obstruction proves that every F_p-valued source-level flat table
is a source-key-compatible coboundary for p in the certified prime set.  This
script records the standard derived-series consequence:

If a finite solvable carrier G has only those certified primes in its abelian
composition factors, then any non-coboundary G-valued source-level flat table
would project at some derived quotient to a non-coboundary F_p-valued table.
The phase obstruction forbids that projection.

This does not rule out perfect/non-solvable finite carriers, larger meshes, or
selected D_E-response promotion.
"""

from __future__ import annotations

import argparse
import json
from math import prod
from typing import Any

from analyze_iwasawa_n1_phase_coboundary_obstruction import analyze_modulus


DEFAULT_CERTIFIED_PRIMES = [2, 3, 5, 7]
CARRIER_EXAMPLES: dict[str, dict[str, Any]] = {
    "cyclic_phase_Cp": {
        "carrier_type": "abelian phase",
        "order_prime_factors": [2, 3, 5, 7],
        "solvable": True,
        "rank_three_realization": "scalar or diagonal phase matrices",
    },
    "dihedral_D4_D5_D7": {
        "carrier_type": "dihedral",
        "order_prime_factors": [2, 5, 7],
        "solvable": True,
        "rank_three_realization": "orthogonal permutation/rotation-reflection blocks",
    },
    "quaternion_Q8": {
        "carrier_type": "nilpotent 2-group",
        "order_prime_factors": [2],
        "solvable": True,
        "rank_three_realization": "unitary block plus spectator line",
    },
    "heisenberg_p_2_3_5_7": {
        "carrier_type": "finite nilpotent Heisenberg group",
        "order_prime_factors": [2, 3, 5, 7],
        "solvable": True,
        "rank_three_realization": "upper triangular or Schrodinger finite representation",
    },
    "S3_permutation": {
        "carrier_type": "symmetric group S3",
        "order_prime_factors": [2, 3],
        "solvable": True,
        "rank_three_realization": "3x3 permutation matrices",
    },
    "A4_tetrahedral": {
        "carrier_type": "alternating group A4",
        "order_prime_factors": [2, 3],
        "solvable": True,
        "rank_three_realization": "3D tetrahedral rotation representation",
    },
    "S4_octahedral": {
        "carrier_type": "symmetric group S4",
        "order_prime_factors": [2, 3],
        "solvable": True,
        "rank_three_realization": "3D octahedral rotation representation",
    },
    "GL2_F3_binary_octahedral_solvable": {
        "carrier_type": "binary octahedral / GL(2,F3)",
        "order_prime_factors": [2, 3],
        "solvable": True,
        "rank_three_realization": "unitary representation with rank-three reduction required",
    },
}


def parse_primes(value: str) -> list[int]:
    primes = [int(part.strip()) for part in value.split(",") if part.strip()]
    if not primes:
        raise argparse.ArgumentTypeError("expected at least one certified prime")
    return primes


def carrier_is_covered(factors: list[int], certified_primes: list[int]) -> bool:
    return set(factors).issubset(set(certified_primes))


def analyze(certified_primes: list[int]) -> dict[str, Any]:
    phase_results = [analyze_modulus(1, prime) for prime in certified_primes]
    h1_zero_primes = [
        entry["modulus"]
        for entry in phase_results
        if entry["flat_solution_space_equals_source_key_coboundaries"] is True
    ]
    h1_zero_set = set(h1_zero_primes)

    examples: dict[str, dict[str, Any]] = {}
    for name, entry in CARRIER_EXAMPLES.items():
        factors = entry["order_prime_factors"]
        covered = entry["solvable"] is True and set(factors).issubset(h1_zero_set)
        examples[name] = {
            **entry,
            "certified_by_phase_primes": covered,
            "obstruction_reason": (
                "finite solvable carrier; every nontrivial derived quotient has "
                "a cyclic prime-order abelian factor in the certified zero-H1 set"
                if covered
                else "not covered by the certified prime set or not solvable"
            ),
        }

    all_examples_covered = all(
        entry["certified_by_phase_primes"]
        for entry in examples.values()
    )
    return {
        "calculation": "IwasawaN1SolvableCarrierObstruction",
        "mesh_N": 1,
        "certified_primes": certified_primes,
        "phase_zero_h1_primes": h1_zero_primes,
        "phase_results": phase_results,
        "derived_series_lift": {
            "statement": (
                "A non-coboundary flat table in a finite solvable carrier would "
                "descend at some derived quotient to a non-coboundary abelian "
                "prime-order phase table."
            ),
            "requires_zero_h1_for_all_abelian_composition_primes": True,
            "applies_to_source_level_rhoE_promotion_only": True,
        },
        "covered_matrix_carrier_examples": examples,
        "global_verdict": {
            "all_listed_solvable_matrix_carriers_blocked_at_N1_source_level": all_examples_covered,
            "blocks_finite_solvable_carriers_with_certified_prime_factors": len(h1_zero_primes)
            == len(certified_primes),
            "does_not_rule_out_perfect_or_non_solvable_carriers": True,
            "does_not_rule_out_larger_meshes": True,
            "does_not_rule_out_selected_D_E_response_promotion": True,
            "next_step": (
                "Either test a perfect/non-solvable carrier such as A5/PSL(2,7), "
                "move to N>1, or construct selected D_E/dotD response data."
            ),
        },
        "example_prime_factor_product": prod(certified_primes),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certified-primes", type=parse_primes, default=DEFAULT_CERTIFIED_PRIMES)
    args = parser.parse_args()
    print(json.dumps(analyze(args.certified_primes), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
