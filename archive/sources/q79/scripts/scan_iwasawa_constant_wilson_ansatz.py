"""Scan the first constant rank-three Weyl/Wilson rho_E ansatz.

The ansatz models each constant transition generator by one rank-three
finite Heisenberg clock/shift pair:

    R_i = P**a_i Q**b_i,     (a_i,b_i) in F_3^2,
    P Q = omega Q P.

The commutator phase is omega**(<v_i,v_j>) with
<v_i,v_j> = a_i b_j - b_i a_j.  The Iwasawa rho_E relations in the existing
constant validator then impose the finite symplectic equations scanned here.
"""

from __future__ import annotations

import json
from itertools import product
from typing import Iterable


FieldVector = tuple[int, int]
Phase = tuple[int, int]
MODULUS = 3


def symplectic(left: FieldVector, right: FieldVector) -> int:
    """Return the F_3 symplectic pairing for clock/shift exponents."""

    return (left[0] * right[1] - left[1] * right[0]) % MODULUS


def vectors() -> Iterable[FieldVector]:
    return product(range(MODULUS), repeat=2)


def relation_passes(
    v1: FieldVector,
    v2: FieldVector,
    v3: FieldVector,
    v4: FieldVector,
    s5: int,
    s6: int,
) -> bool:
    """Check the scalar-central Weyl form of the Iwasawa relations."""

    return (
        symplectic(v1, v2) == 0
        and symplectic(v3, v4) == 0
        and symplectic(v1, v3) == s5
        and symplectic(v1, v4) == s6
        and symplectic(v2, v3) == s6
        and symplectic(v2, v4) == (-s5) % MODULUS
    )


def scan() -> dict[str, object]:
    counts: dict[Phase, int] = {
        (s5, s6): 0 for s5 in range(MODULUS) for s6 in range(MODULUS)
    }

    all_vectors = list(vectors())
    assignments = 0
    isotropic_pair_assignments = 0
    for v1, v2, v3, v4 in product(all_vectors, repeat=4):
        assignments += 1
        if symplectic(v1, v2) == 0 and symplectic(v3, v4) == 0:
            isotropic_pair_assignments += 1
        for s5, s6 in counts:
            if relation_passes(v1, v2, v3, v4, s5, s6):
                counts[(s5, s6)] += 1

    nontrivial = {
        f"{s5},{s6}": count
        for (s5, s6), count in sorted(counts.items())
        if (s5, s6) != (0, 0) and count
    }
    counts_as_text = {f"{s5},{s6}": count for (s5, s6), count in sorted(counts.items())}

    return {
        "calculation": "IwasawaConstantWilsonScalarCentralWeylAnsatzScan",
        "field": "F3",
        "modulus": MODULUS,
        "rank": 3,
        "ansatz": {
            "generator_form": "R_i=P^a_i Q^b_i with (a_i,b_i) in F3^2",
            "clock_shift_relation": "P Q = omega Q P",
            "central_generators": "g5=omega^s5 I, g6=omega^s6 I",
            "commutator_pairing": "<v_i,v_j>=a_i b_j-b_i a_j mod 3",
        },
        "relation_equations": {
            "<v1,v2>": 0,
            "<v3,v4>": 0,
            "<v1,v3>": "s5",
            "<v1,v4>": "s6",
            "<v2,v3>": "s6",
            "<v2,v4>": "-s5",
        },
        "linear_algebra_obstruction": {
            "rank_reason": "in F3^2, <v1,v2>=0 and <v3,v4>=0 make each pair span dimension at most one, so the cross-pairing matrix has determinant zero",
            "cross_pairing_matrix": "[[s5, s6], [s6, -s5]]",
            "determinant": "-(s5^2+s6^2)",
            "over_F3": "determinant zero only for s5=s6=0",
        },
        "total_vector_assignments": assignments,
        "isotropic_pair_assignments": isotropic_pair_assignments,
        "central_phase_solution_counts": counts_as_text,
        "trivial_phase_solution_count": counts[(0, 0)],
        "nontrivial_scalar_central_solutions": sum(nontrivial.values()),
        "nontrivial_solution_counts": nontrivial,
        "verdict": {
            "nontrivial_rank3_scalar_central_constant_weyl_rhoE_exists": False,
            "identity_phase_schema_solutions_exist": counts[(0, 0)] > 0,
            "closes_all_constant_3x3_rhoE": False,
            "closes_coordinate_dependent_or_table_valued_rhoE": False,
            "next_route": "coordinate-dependent/table-valued rho_E, typed Cech/monad transitions, or a higher auxiliary carrier with a rank-three selected quotient",
        },
    }


def main() -> int:
    print(json.dumps(scan(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
