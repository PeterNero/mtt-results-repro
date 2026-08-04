from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINITE_MODULAR = (
    ROOT / "certificates" / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
)
TWISTED_ALGEBRA = (
    ROOT
    / "certificates"
    / "q79_twisted_group_algebra_topological_character_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_seven_seed_modular_induction_stabilizers_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Seven_Seed_Modular_Induction_and_Stabilizer_Theorem_v1.md"
)


Vector = tuple[int, int]
Sector = tuple[Vector, Vector]
Matrix2 = tuple[int, int, int, int]


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def add(left: Vector, right: Vector) -> Vector:
    return ((left[0] + right[0]) % 3, (left[1] + right[1]) % 3)


def scale(value: Vector, scalar: int) -> Vector:
    return ((scalar * value[0]) % 3, (scalar * value[1]) % 3)


def mat_mul(left: Matrix2, right: Matrix2) -> Matrix2:
    a, b, c, d = left
    e, f, g, h = right
    return (
        (a * e + b * g) % 3,
        (a * f + b * h) % 3,
        (c * e + d * g) % 3,
        (c * f + d * h) % 3,
    )


def determinant(matrix: Matrix2) -> int:
    a, b, c, d = matrix
    return (a * d - b * c) % 3


def act(sector: Sector, matrix: Matrix2) -> Sector:
    # If the sector is the 2x2 matrix [g h], act on the right by matrix.
    g, h = sector
    a, b, c, d = matrix
    return (add(scale(g, a), scale(h, c)), add(scale(g, b), scale(h, d)))


def epsilon_exponent(sector: Sector) -> int:
    g, h = sector
    return (g[0] * h[1] - g[1] * h[0]) % 3


def matrix_record(matrix: Matrix2) -> list[list[int]]:
    a, b, c, d = matrix
    return [[a, b], [c, d]]


def main() -> None:
    modular = load(FINITE_MODULAR)
    twisted = load(TWISTED_ALGEBRA)

    group_vectors = list(product(range(3), repeat=2))
    sectors = list(product(group_vectors, repeat=2))
    sl2 = [
        matrix
        for matrix in product(range(3), repeat=4)
        if determinant(matrix) == 1
    ]
    identity = (1, 0, 0, 1)
    generator_s = (0, 2, 1, 0)
    generator_t = (1, 1, 0, 1)

    generated = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in (generator_s, generator_t):
            candidate = mat_mul(current, generator)
            if candidate not in generated:
                generated.add(candidate)
                frontier.append(candidate)

    unseen = set(sectors)
    orbit_sets: list[set[Sector]] = []
    while unseen:
        seed = min(unseen)
        orbit = {act(seed, matrix) for matrix in sl2}
        unseen -= orbit
        orbit_sets.append(orbit)

    orbit_records = []
    for orbit in orbit_sets:
        seed = min(orbit)
        stabilizer = [matrix for matrix in sl2 if act(seed, matrix) == seed]
        phase_set = sorted({epsilon_exponent(sector) for sector in orbit})
        orbit_records.append(
            {
                "seed": [list(seed[0]), list(seed[1])],
                "size": len(orbit),
                "phase_exponent": phase_set[0],
                "phase_is_constant": len(phase_set) == 1,
                "stabilizer_order": len(stabilizer),
                "orbit_stabilizer_product": len(orbit) * len(stabilizer),
                "stabilizer_matrices": [matrix_record(matrix) for matrix in stabilizer],
            }
        )
    orbit_records.sort(
        key=lambda row: (row["phase_exponent"], row["size"], row["seed"])
    )

    orbit_sizes = sorted(row["size"] for row in orbit_records)
    stabilizer_orders = sorted(row["stabilizer_order"] for row in orbit_records)
    phase_orbit_counts = {
        str(exponent): sum(
            row["phase_exponent"] == exponent for row in orbit_records
        )
        for exponent in range(3)
    }
    phase_sector_counts = {
        str(exponent): sum(
            row["size"]
            for row in orbit_records
            if row["phase_exponent"] == exponent
        )
        for exponent in range(3)
    }

    # A scalar function on the 81 labels is invariant under both generators
    # exactly when it is constant on each connected modular orbit.
    finite_invariant_dimension = len(orbit_sets)
    finite_invariance_constraint_rank = len(sectors) - finite_invariant_dimension

    all_stabilizers_closed = True
    for row in orbit_records:
        encoded = {
            tuple(entry for matrix_row in matrix for entry in matrix_row)
            for matrix in row["stabilizer_matrices"]
        }
        if identity not in encoded:
            all_stabilizers_closed = False
        for left, right in product(encoded, repeat=2):
            if mat_mul(left, right) not in encoded:
                all_stabilizers_closed = False

    checks = {
        "finite_modular_orbit_theorem_is_closed": modular["finite_data"][
            "modular_orbit_count"
        ]
        == 7,
        "selected_twisted_algebra_is_Mat3": twisted["claim_tiers"][
            "selected_q79_twisted_group_algebra"
        ]
        == "CLOSED_EXACT_ISOMORPHIC_TO_MAT3C",
        "SL2_F3_has_order_24": len(sl2) == 24,
        "S_and_T_generate_all_SL2_F3": generated == set(sl2),
        "seven_orbits_recomputed": len(orbit_sets) == 7,
        "orbit_sizes_match": orbit_sizes == [1, 8, 8, 8, 8, 24, 24],
        "stabilizer_orders_match": stabilizer_orders
        == [1, 1, 3, 3, 3, 3, 24],
        "all_stabilizers_are_subgroups": all_stabilizers_closed,
        "orbit_stabilizer_holds_for_every_seed": all(
            row["orbit_stabilizer_product"] == 24 for row in orbit_records
        ),
        "discrete_torsion_phase_is_constant_on_every_orbit": all(
            row["phase_is_constant"] for row in orbit_records
        ),
        "phase_orbit_split_is_5_1_1": phase_orbit_counts
        == {"0": 5, "1": 1, "2": 1},
        "phase_sector_split_is_33_24_24": phase_sector_counts
        == {"0": 33, "1": 24, "2": 24},
        "finite_covariant_seed_dimension_is_exactly_seven": finite_invariant_dimension
        == 7,
        "finite_modular_constraints_have_rank_74": finite_invariance_constraint_rank
        == 74,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    cert = {
        "certificate": "q79_seven_seed_modular_induction_stabilizers",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SEVEN_SEED_MODULAR_INDUCTION_AND_STABILIZER_THEOREM_CLOSED_EXACT_SEED_FUNCTIONS_GSO_OPEN",
        "inputs": {
            "finite_modular_orbit_theorem": str(FINITE_MODULAR),
            "selected_twisted_group_algebra": str(TWISTED_ALGEBRA),
        },
        "finite_data": {
            "SL2_F3_order": len(sl2),
            "sector_count": len(sectors),
            "modular_orbit_count": len(orbit_sets),
            "orbit_sizes": orbit_sizes,
            "stabilizer_orders": stabilizer_orders,
            "phase_orbit_counts": phase_orbit_counts,
            "phase_sector_counts": phase_sector_counts,
            "finite_invariant_seed_dimension": finite_invariant_dimension,
            "finite_invariance_constraint_rank": finite_invariance_constraint_rank,
            "orbit_records": orbit_records,
        },
        "theorem": {
            "name": "q79SevenSeedModularInductionTheorem",
            "statement": (
                "The SL(2,F3) action generated by the selected modular S and T maps splits the 81 F3^2 torus boundary-condition labels into exactly seven orbits. "
                "A modular-covariant character family is determined by one seed per orbit together with covariance under that seed's stabilizer and the invisible congruence subgroup Gamma(3). "
                "Conversely those stabilizer-compatible seeds induce a well-defined 81-sector family, and its discrete-torsion-weighted orbifold sum is modular invariant whenever the analytic character multipliers are consistent."
            ),
            "minimality": (
                "Finite label covariance alone has a seven-dimensional invariant space and cannot relate different orbits. Thus fewer than seven analytic seeds requires extra q79 worldsheet geometry, not more finite-group algebra."
            ),
        },
        "analytic_seed_contract": {
            "required_seed_count": 7,
            "per_seed_fields": [
                "tau-dependent oscillator and internal sigma-model character",
                "left-moving E8xE8 or Spin(32)/Z2 current-lattice character",
                "right-moving spin structure and supersymmetric character",
                "GSO phase and projection",
                "covariance under the listed finite stabilizer",
                "multiplier/covariance under Gamma(3)",
                "factorization and level-matching data",
            ],
            "shared_fields": [
                "q79 exact (0,2) SCFT or fully specified torsion GLSM",
                "global anomaly and differential-gerbe data",
                "tachyon exclusion",
                "tadpole and infrared prescription",
            ],
        },
        "claim_tiers": {
            "finite_SL2_F3_sector_action": "CLOSED_EXACT",
            "seven_modular_orbits_and_stabilizers": "CLOSED_EXACT",
            "seven_seed_modular_induction_theorem": "CLOSED_CONDITIONAL_ON_ANALYTIC_STABILIZER_MULTIPLIERS",
            "finite_symmetry_reduces_below_seven_seeds": "CLOSED_NO_GO",
            "seven_tau_dependent_seed_characters": "OPEN",
            "Gamma3_character_multiplier": "OPEN",
            "GSO_and_level_matching": "OPEN",
            "full_q79_heterotic_partition_function": "OPEN",
        },
        "guardrails": {
            "claims_finite_orbit_induction_constructs_analytic_seed_functions": False,
            "claims_stabilizer_orders_fix_Gamma3_multipliers": False,
            "claims_projective_module_is_closed_string_character": False,
            "claims_full_GSO_partition_function_closed": False,
            "claims_exact_q79_worldsheet_CFT_closed": False,
            "claims_UV_complete_QG_closed": False,
            "uses_observed_data": False,
            "adds_fitted_parameter": False,
        },
        "next_required_artifact": "q79_Exact_Torsion_GLSM_Charge_EJ_and_Seven_Analytic_Seed_Packet_v1",
        "checks": checks,
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Seven-Seed Modular Induction and Stabilizer Theorem v1

Date: 2026-07-16

## Exact finite result

The modular generators act on torus boundary-condition labels by

```text
S:(g,h) -> (h,-g),
T:(g,h) -> (g,g+h).
```

Their reduction modulo three generates all `SL(2,F_3)`, of order 24. On the
81 labels in `F_3^2 x F_3^2`, the exact orbit/stabilizer decomposition is

```text
orbit sizes:      1,8,8,8,8,24,24
stabilizer orders: 24,3,3,3,3,1,1.
```

The five rank-zero/rank-one orbits have trivial discrete-torsion phase and
contain 33 sectors. The two full-rank determinant orbits contain 24 sectors
each and carry `omega` and `omega^2` respectively.

## Modular induction theorem

Choose one analytic seed character for each orbit. A seed may be transported
to every label in its orbit. This transport is path-independent exactly when
the seed obeys the analytic modular multiplier associated with its listed
stabilizer and with the kernel `Gamma(3)` of reduction modulo three.

Under those hypotheses, the seven seeds induce all 81 sector characters, and
the discrete-torsion-weighted orbifold sum is modular invariant. Thus the
finite part of the worldsheet problem is no longer an 81-function problem.

## Exact minimality

The simultaneous finite `S,T` invariance equations on scalar label data have

```text
81 variables,
rank 74,
nullity 7.
```

Therefore finite modular covariance cannot reduce the seven analytic seeds
any further. Any reduction below seven must come from additional q79
worldsheet geometry, spectral degeneracy, supersymmetry, or factorization.

## Remaining analytic packet

For each of the seven seeds one still needs the tau-dependent internal
oscillator/sigma-model character, heterotic current-lattice character,
right-moving spin structure, GSO phase, level matching, and factorization.
The q79 corpus does not presently supply a typed Fu-Yau torsion-GLSM charge
matrix, its `E/J` maps, torsion-multiplet anomaly-cancellation charges, or the
`Gamma(3)` character multiplier.

The exact finite projective `Mat_3(C)` module and topological torus index one
remain separate from these closed-string analytic characters.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
