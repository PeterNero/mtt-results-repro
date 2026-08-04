from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

GERBE_PERIOD = (
    Q79 / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json"
)
OLD_PROJECTIVE_HUNT = (
    Q79 / "certificates" / "iwasawa_projective_twist_source_hunt_certificate.json"
)
FINITE_MODULAR = (
    ROOT / "certificates" / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_twisted_group_algebra_topological_character_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Twisted_Group_Algebra_and_Finite_Topological_Character_Theorem_v1.md"
)


Element = tuple[int, int]


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def add(g: Element, h: Element) -> Element:
    return ((g[0] + h[0]) % 3, (g[1] + h[1]) % 3)


def cocycle_exponent(g: Element, h: Element) -> int:
    # For U_(a,b)=X^a Z^b and XZ=omega ZX:
    # U_g U_h=omega^(-h_0 g_1) U_(g+h).
    return (-h[0] * g[1]) % 3


def epsilon_exponent(g: Element, h: Element) -> int:
    return (cocycle_exponent(g, h) - cocycle_exponent(h, g)) % 3


def cyclotomic_pair_for_power(exponent: int) -> tuple[int, int]:
    # Store a+b*omega with omega^2+omega+1=0.
    return [(1, 0), (0, 1), (-1, -1)][exponent % 3]


def add_pair(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    return (left[0] + right[0], left[1] + right[1])


def scale_pair(value: tuple[int, int], factor: int) -> tuple[int, int]:
    return (factor * value[0], factor * value[1])


def exact_matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def main() -> None:
    gerbe = load(GERBE_PERIOD)
    old_hunt = load(OLD_PROJECTIVE_HUNT)
    modular = load(FINITE_MODULAR)

    group = list(product(range(3), repeat=2))
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    identity3 = sp.eye(3)
    zero3 = sp.zeros(3)
    shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    clock = sp.diag(1, omega, sp.simplify(omega**2))

    relation_residual = sp.simplify(shift * clock - omega * clock * shift)
    order_checks = {
        "X_cubed": exact_matrix_equal(shift**3, identity3),
        "Z_cubed": exact_matrix_equal(clock**3, identity3),
        "XZ_equals_omega_ZX": exact_matrix_equal(relation_residual, zero3),
    }

    def u(g: Element) -> sp.Matrix:
        return sp.simplify((shift ** g[0]) * (clock ** g[1]))

    multiplication_failures: list[tuple[Element, Element]] = []
    for g, h in product(group, repeat=2):
        expected = sp.simplify(
            (omega ** cocycle_exponent(g, h)) * u(add(g, h))
        )
        if not exact_matrix_equal(u(g) * u(h), expected):
            multiplication_failures.append((g, h))

    gram = sp.Matrix(
        [
            [sp.simplify(sp.trace(u(g).conjugate().T * u(h))) for h in group]
            for g in group
        ]
    )
    gram_is_3_identity = exact_matrix_equal(gram, 3 * sp.eye(9))
    flattened = sp.Matrix.hstack(
        *[sp.Matrix([u(g)[row, col] for row in range(3) for col in range(3)]) for g in group]
    )
    matrix_span_rank = flattened.rank()

    central_labels = [
        g
        for g in group
        if all(epsilon_exponent(g, h) == 0 for h in group)
    ]
    projective_character = {
        f"{g[0]},{g[1]}": str(sp.simplify(sp.trace(u(g)))) for g in group
    }
    character_values = [sp.simplify(sp.trace(u(g))) for g in group]
    trace_three_count = sum(value == 3 for value in character_values)
    trace_zero_count = sum(value == 0 for value in character_values)

    phase_counts = {
        int(exponent): int(count)
        for exponent, count in modular["finite_data"][
            "phase_exponent_multiplicities"
        ].items()
    }
    torus_sum_pair = (0, 0)
    for exponent, count in phase_counts.items():
        torus_sum_pair = add_pair(
            torus_sum_pair,
            scale_pair(cyclotomic_pair_for_power(exponent), count),
        )
    normalized_torus_index = sp.Rational(torus_sum_pair[0], len(group))
    stabilizer_orders = sorted(
        24 // row["size"] for row in modular["finite_data"]["modular_orbits"]
    )

    checks = {
        "selected_q79_F_m1_period_table_is_exact": gerbe["status"]
        == "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
        "selected_period_table_matches_qutrit_orientation": gerbe[
            "calculation_results"
        ]["commutator_matrix_matches_qutrit_F_orientation"],
        "selected_cocycle_is_nondegenerate": gerbe["calculation_results"][
            "commutator_rank_two"
        ],
        "older_projective_source_hunt_was_open": old_hunt["status"]
        == "IWASAWA_PROJECTIVE_TWIST_SOURCE_HUNT_ALIGNED_SOURCE_MAP_OPEN",
        "clock_shift_orders_and_relation_are_exact": all(order_checks.values()),
        "all_81_twisted_multiplication_rows_pass": not multiplication_failures,
        "nine_Weyl_operators_are_Hilbert_Schmidt_orthogonal": gram_is_3_identity,
        "nine_Weyl_operators_span_Mat3": matrix_span_rank == 9,
        "twisted_algebra_center_is_scalar": central_labels == [(0, 0)],
        "projective_character_is_3_then_eight_zeros": trace_three_count == 1
        and trace_zero_count == 8,
        "finite_topological_torus_sum_is_nine": torus_sum_pair == (9, 0),
        "normalized_finite_topological_torus_index_is_one": normalized_torus_index
        == 1,
        "seven_seed_stabilizer_orders_are_exact": stabilizer_orders
        == [1, 1, 3, 3, 3, 3, 24],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    cert = {
        "certificate": "q79_twisted_group_algebra_topological_character",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SELECTED_FINITE_TWISTED_GROUP_ALGEBRA_MAT3_AND_TOPOLOGICAL_INDEX_CLOSED_EXACT_FULL_WORLDSHEET_CHARACTERS_OPEN",
        "inputs": {
            "selected_q79_m1_gerbe_period_table": str(GERBE_PERIOD),
            "older_projective_source_hunt": str(OLD_PROJECTIVE_HUNT),
            "finite_modular_orbit_theorem": str(FINITE_MODULAR),
        },
        "definition": {
            "finite_group": "G=F_3^2",
            "selected_cocycle": "c((a,b),(c,d))=omega^(-c b)",
            "Weyl_operator": "U_(a,b)=X^a Z^b",
            "clock_shift_relation": "XZ=omega ZX",
            "twisted_product": "U_g U_h=c(g,h) U_(g+h)",
        },
        "finite_data": {
            "group_order": len(group),
            "twisted_group_algebra_dimension": len(group),
            "matrix_span_rank": matrix_span_rank,
            "twisted_algebra_center_dimension": len(central_labels),
            "unique_projective_irrep_count": 1,
            "unique_projective_irrep_dimension": 3,
            "projective_character": projective_character,
            "projective_character_trace_distribution": {
                "trace_3": trace_three_count,
                "trace_0": trace_zero_count,
            },
            "discrete_torsion_phase_multiplicities": {
                str(key): value for key, value in phase_counts.items()
            },
            "unnormalized_finite_torus_sum_in_basis_1_omega": list(
                torus_sum_pair
            ),
            "normalized_finite_topological_torus_index": str(
                normalized_torus_index
            ),
            "closed_string_modular_seed_orbit_count": modular["finite_data"][
                "modular_orbit_count"
            ],
            "seed_stabilizer_orders_in_SL2_F3": stabilizer_orders,
        },
        "theorem": {
            "name": "q79SelectedFiniteTwistedGroupAlgebraTheorem",
            "statement": (
                "The selected q79/F m=1 finite gerbe cocycle has twisted group algebra C^c[F3^2] isomorphic to Mat_3(C). "
                "It therefore has one irreducible c-projective module up to equivalence, of dimension three, with character 3 at the identity and zero elsewhere. "
                "Its normalized finite discrete-torsion torus index is exactly one."
            ),
            "proof_summary": (
                "The nine Weyl operators X^a Z^b obey the selected cocycle multiplication, are Hilbert-Schmidt orthogonal, and span all 3 by 3 complex matrices. "
                "The nondegenerate alternating commutator leaves only the identity label in the center. "
                "Finally 33+24 omega+24 omega^2=9, and division by |F3^2|=9 gives one."
            ),
        },
        "supersession": {
            "artifact": "IwasawaProjectiveTwistSourceHunt",
            "old_status": old_hunt["status"],
            "new_finite_tier_status": "SUPERSEDED_AT_SELECTED_FINITE_COCYCLE_AND_PROJECTIVE_MODULE_TIER",
            "still_valid_open_boundary": (
                "The older warning remains valid for full geometric Deligne/Cech promotion, twisted projector retention, visible bundle operators, and worldsheet characters."
            ),
        },
        "claim_tiers": {
            "selected_q79_finite_projective_cocycle": "CLOSED_EXACT",
            "selected_q79_twisted_group_algebra": "CLOSED_EXACT_ISOMORPHIC_TO_MAT3C",
            "selected_q79_projective_module": "CLOSED_UNIQUE_IRREP_DIMENSION_3",
            "finite_discrete_torsion_topological_torus_index": "CLOSED_EXACT_ONE",
            "finite_projective_source_hunt": "CLOSED_AFTER_SELECTED_M1_PERIOD_TABLE",
            "global_Deligne_Cech_gerbe": "OPEN",
            "twisted_worldsheet_projector_retention": "OPEN",
            "seven_closed_string_seed_characters": "OPEN",
            "full_heterotic_GSO_partition_function": "OPEN",
            "exact_q79_worldsheet_CFT": "OPEN",
        },
        "guardrails": {
            "claims_unique_projective_module_is_full_closed_string_spectrum": False,
            "claims_finite_topological_index_is_full_heterotic_partition_function": False,
            "claims_twisted_projector_retention_closed": False,
            "claims_global_Deligne_gerbe_closed": False,
            "claims_exact_q79_worldsheet_CFT_closed": False,
            "claims_UV_complete_QG_closed": False,
            "uses_observed_data": False,
            "adds_fitted_parameter": False,
        },
        "primary_sources": {
            "discrete_torsion_B_field_and_projective_representations": "https://arxiv.org/abs/hep-th/0008154",
            "twisted_group_ring_algebra": "https://arxiv.org/abs/math/0208081",
            "heterotic_GLSM_torus_partition_functions": "https://arxiv.org/abs/1403.2380",
        },
        "next_required_artifact": "q79_Seven_Seed_Heterotic_Character_Stabilizer_and_GSO_Packet_v1",
        "checks": checks,
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Twisted Group Algebra and Finite Topological Character Theorem v1

Date: 2026-07-16

## Exact promotion

The older Iwasawa projective carrier was only a prototype because no selected
MTT gerbe period table had been connected to its qutrit clock/shift cocycle.
That finite-tier source gap is now closed. The selected time-oriented
`q=79/F, m=1` period table is exactly

```text
c((a,b),(c,d)) = omega^(-c b),
U_(a,b) = X^a Z^b,
X Z = omega Z X.
```

All 81 multiplication rows satisfy `U_g U_h=c(g,h)U_(g+h)` exactly.

## Twisted algebra theorem

The nine matrices `X^a Z^b` are Hilbert-Schmidt orthogonal:

```text
Tr(U_g^* U_h) = 3 delta_(g,h).
```

They therefore span the nine-dimensional algebra `Mat_3(C)`. Hence

```text
C^c[F_3^2] = Mat_3(C)
```

as complex algebras. Its center is one-dimensional, and it has exactly one
irreducible module up to equivalence. That selected projective module has
dimension three and character

```text
chi(0,0)=3,
chi(g)=0 for g != (0,0).
```

No continuous or discrete fit was introduced.

## Finite torus index

The exact discrete-torsion phase multiplicities are `33,24,24`, so

```text
sum_(g,h) epsilon(g,h)
  = 33 + 24 omega + 24 omega^2
  = 9,

(1/|F_3^2|) sum_(g,h) epsilon(g,h) = 1.
```

This is the normalized finite topological torus index. It agrees with the one
irreducible projective module of the nondegenerate twisted algebra.

## What remains separate

This theorem does not make the full heterotic partition function equal to one.
The unique projective module concerns the selected finite gerbe/topological
factor. Closed-string twisted boundary conditions still form seven modular
orbits, with finite stabilizer orders `{stabilizer_orders}`. Their seven
tau-dependent oscillator, gauge-current, spin-structure, and GSO seed
characters remain to be built and checked for factorization.

The global Deligne/Cech gerbe, twisted spectral-projector retention, exact q79
`(0,2)` worldsheet CFT, and nonperturbative/all-genus completion also remain
open.

## Primary sources

- [Discrete Torsion](https://arxiv.org/abs/hep-th/0008154)
- [The algebra of discrete torsion](https://arxiv.org/abs/math/0208081)
- [Torus partition functions and spectra of gauged linear sigma models](https://arxiv.org/abs/1403.2380)
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
