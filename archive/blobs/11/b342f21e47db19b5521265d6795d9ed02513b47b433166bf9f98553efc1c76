from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
GERBE_PERIOD = Q79 / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json"
TIME_BRANCH = Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json"

OUT_CERT = ROOT / "certificates" / "q79_f3x2_discrete_torsion_modular_orbit_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_F3x2_Discrete_Torsion_Modular_Orbit_Theorem_v1.md"


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def add(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    return ((g[0] + h[0]) % 3, (g[1] + h[1]) % 3)


def neg(g: tuple[int, int]) -> tuple[int, int]:
    return ((-g[0]) % 3, (-g[1]) % 3)


def cocycle_exponent(g: tuple[int, int], h: tuple[int, int]) -> int:
    # B_1((a,b),(c,d))=-cb/3, so c(g,h)=zeta_3^(-h_0 g_1).
    return (-h[0] * g[1]) % 3


def epsilon_exponent(g: tuple[int, int], h: tuple[int, int]) -> int:
    # The discrete-torsion commutator c(g,h)/c(h,g).
    return (cocycle_exponent(g, h) - cocycle_exponent(h, g)) % 3


def modular_s(pair: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    g, h = pair
    return (h, neg(g))


def modular_t(pair: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    g, h = pair
    return (g, add(g, h))


def main() -> None:
    gerbe = load(GERBE_PERIOD)
    branch = load(TIME_BRANCH)
    group = list(product(range(3), repeat=2))
    zero = (0, 0)

    normalized = all(
        cocycle_exponent(zero, g) == 0 and cocycle_exponent(g, zero) == 0
        for g in group
    )
    cocycle_failures = []
    for g, h, k in product(group, repeat=3):
        left = (cocycle_exponent(g, h) + cocycle_exponent(add(g, h), k)) % 3
        right = (cocycle_exponent(h, k) + cocycle_exponent(g, add(h, k))) % 3
        if left != right:
            cocycle_failures.append((g, h, k))

    sectors = list(product(group, repeat=2))
    phase_counts = {0: 0, 1: 0, 2: 0}
    s_failures = []
    t_failures = []
    for pair in sectors:
        exponent = epsilon_exponent(*pair)
        phase_counts[exponent] += 1
        if epsilon_exponent(*modular_s(pair)) != exponent:
            s_failures.append(pair)
        if epsilon_exponent(*modular_t(pair)) != exponent:
            t_failures.append(pair)

    # Verify the modular relations on all finite twist labels. The action is on
    # oriented torus cycles, so S^2 is simultaneous inversion and (ST)^3 agrees.
    s2_failures = []
    st3_failures = []
    for pair in sectors:
        s2 = modular_s(modular_s(pair))
        expected_s2 = (neg(pair[0]), neg(pair[1]))
        if s2 != expected_s2:
            s2_failures.append(pair)

        st = lambda value: modular_s(modular_t(value))
        st3 = st(st(st(pair)))
        if st3 != expected_s2:
            st3_failures.append(pair)

    # Reduce the 81 character slots to modular-orbit seeds. Treat (g,h) as a
    # 2x2 matrix with columns g,h. Right SL(2,F3) action preserves its rank and,
    # at full rank, its determinant.
    unseen = set(sectors)
    modular_orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        frontier = [seed]
        while frontier:
            current = frontier.pop()
            for image in (modular_s(current), modular_t(current)):
                if image not in orbit:
                    orbit.add(image)
                    frontier.append(image)
        unseen -= orbit
        modular_orbits.append(orbit)

    orbit_records = []
    for orbit in modular_orbits:
        seed = min(orbit)
        g, h = seed
        determinant = (g[0] * h[1] - g[1] * h[0]) % 3
        rank = 0 if g == zero and h == zero else (2 if determinant else 1)
        orbit_records.append(
            {
                "seed": [list(g), list(h)],
                "size": len(orbit),
                "matrix_rank_over_F3": rank,
                "determinant_mod_3": determinant,
                "discrete_torsion_exponent": epsilon_exponent(g, h),
            }
        )
    orbit_records.sort(
        key=lambda row: (
            row["matrix_rank_over_F3"],
            row["determinant_mod_3"],
            row["seed"],
        )
    )
    orbit_sizes = sorted(row["size"] for row in orbit_records)
    orbit_rank_counts = {
        str(rank): sum(row["matrix_rank_over_F3"] == rank for row in orbit_records)
        for rank in range(3)
    }

    checks = {
        "selected_q79_m1_period_table_is_available": gerbe["status"]
        == "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
        "selected_branch_is_q79_F": branch["calculation_results"]
        ["time_oriented_retarded_branch_selects_q79"],
        "gerbe_certificate_reports_normalized_cocycle": gerbe["calculation_results"]
        ["period_table_is_normalized_two_cocycle"],
        "normalization_verified_directly": normalized,
        "all_729_cocycle_equations_pass": not cocycle_failures,
        "all_81_S_phase_equations_pass": not s_failures,
        "all_81_T_phase_equations_pass": not t_failures,
        "S_squared_is_simultaneous_inversion": not s2_failures,
        "ST_cubed_is_simultaneous_inversion": not st3_failures,
        "phase_multiplicities_are_33_24_24": phase_counts == {0: 33, 1: 24, 2: 24},
        "clock_shift_commutator_is_nontrivial": epsilon_exponent((1, 0), (0, 1)) == 1,
        "modular_character_slots_reduce_to_seven_orbits": len(modular_orbits) == 7,
        "modular_orbit_sizes_are_1_8x4_24x2": orbit_sizes
        == [1, 8, 8, 8, 8, 24, 24],
        "modular_orbit_rank_counts_are_1_4_2": orbit_rank_counts
        == {"0": 1, "1": 4, "2": 2},
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    cert = {
        "certificate": "q79_f3x2_discrete_torsion_modular_orbit",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_F3X2_DISCRETE_TORSION_MODULAR_ST_ORBIT_CLOSED_EXACT_FULL_HETEROTIC_PARTITION_FUNCTION_OPEN",
        "inputs": {
            "selected_q79_m1_gerbe_period_table": str(GERBE_PERIOD),
            "time_oriented_q79_branch": str(TIME_BRANCH),
        },
        "definition": {
            "finite_group": "G=F_3^2",
            "selected_cocycle": "c((a,b),(c,d))=zeta_3^(-c b)",
            "discrete_torsion_phase": "epsilon(g,h)=c(g,h)/c(h,g)=zeta_3^(a d-b c)",
            "modular_S": "S:(g,h)->(h,-g)",
            "modular_T": "T:(g,h)->(g,g+h)",
        },
        "finite_data": {
            "group_order": len(group),
            "torus_twist_sector_count": len(sectors),
            "cocycle_triples_checked": len(group) ** 3,
            "cocycle_failures": len(cocycle_failures),
            "S_phase_failures": len(s_failures),
            "T_phase_failures": len(t_failures),
            "S2_relation_failures": len(s2_failures),
            "ST3_relation_failures": len(st3_failures),
            "phase_exponent_multiplicities": {str(k): v for k, v in phase_counts.items()},
            "nontrivial_phase_sector_count": phase_counts[1] + phase_counts[2],
            "modular_orbit_count": len(modular_orbits),
            "modular_orbit_sizes": orbit_sizes,
            "modular_orbit_rank_counts": orbit_rank_counts,
            "modular_orbits": orbit_records,
        },
        "theorem": {
            "name": "q79FiniteDiscreteTorsionModularOrbitTheorem",
            "statement": (
                "The selected q79/F m=1 Heisenberg gerbe cocycle defines a normalized nontrivial discrete-torsion phase on all 81 commuting F3^2 torus sectors. "
                "The phase is invariant under the modular S and T actions, and the finite action obeys S^2=(ST)^3=charge conjugation. "
                "The 81 full character slots split into seven modular orbits of sizes 1,8,8,8,8,24,24, so a future character construction needs seven seed blocks rather than 81 unrelated functions."
            ),
            "scope": (
                "This proves modular covariance of the finite gerbe phase only. It does not construct oscillator characters, the gauge lattice, GSO projection, q79 sigma-model measure, or a modular-invariant full heterotic partition function."
            ),
        },
        "claim_tiers": {
            "selected_q79_finite_gerbe_two_cocycle": "CLOSED_EXACT",
            "finite_discrete_torsion_S_T_phase_covariance": "CLOSED_EXACT_81_OF_81",
            "finite_modular_group_relations": "CLOSED_EXACT",
            "q79_full_torus_partition_function": "OPEN_FINITE_TORSION_PHASE_SUBSECTOR_CLOSED",
            "q79_exact_worldsheet_CFT": "OPEN",
            "fixed_genus_string_UV_inheritance": "STILL_CONDITIONAL_ON_FULL_WORLDSHEET_PACKET",
        },
        "guardrails": {
            "claims_finite_phase_covariance_is_full_modular_invariance": False,
            "claims_oscillator_or_gauge_characters_constructed": False,
            "claims_GSO_projection_constructed": False,
            "claims_exact_q79_CFT_closed": False,
            "claims_UV_complete_QG_closed": False,
            "uses_observed_data": False,
            "adds_fitted_parameter": False,
        },
        "next_required_artifact": "q79_Full_Heterotic_Torus_Character_and_GSO_Modular_Packet_v1",
        "note_written": str(OUT_NOTE),
        "checks": checks,
    }

    note = """# q79 F3x2 Discrete-Torsion Modular-Orbit Theorem v1

Date: 2026-07-16

## Exact finite theorem

The selected time-oriented q79/F gerbe has finite quotient `G=F3^2` and

```text
c((a,b),(c,d)) = zeta_3^(-c b).
```

Its discrete-torsion commutator phase is

```text
epsilon(g,h)=c(g,h)/c(h,g)=zeta_3^(a d-b c).
```

The executable calculation checks all `9^3=729` cocycle equations and all
`9^2=81` torus twist sectors. There are no failures. Under

```text
S:(g,h)->(h,-g),
T:(g,h)->(g,g+h),
```

the phase is unchanged in every sector. The finite actions also obey
`S^2=(ST)^3=charge conjugation`. The phase multiplicities are exactly
`33,24,24` for exponents `0,1,2`; 48 sectors carry nontrivial torsion phase.

## What moved

The finite q79 gerbe contribution to a torus orbifold sum is no longer an open
modular-phase guess. Its complete discrete-torsion `S,T` orbit is exact.
The 81 sector labels form exactly seven modular orbits:

```text
rank 0: 1 orbit of size 1,
rank 1: 4 orbits of size 8,
rank 2: 2 determinant-labelled orbits of size 24.
```

Consequently the missing oscillator/gauge character problem reduces to seven
seed character blocks and their factorization data, not 81 independent blocks.

## Honest boundary

This does not construct a full heterotic torus partition function. The
oscillator characters, gauge/current lattice, spin structures, GSO phases,
q79 sigma-model measure, and factorization coefficients remain absent.
Therefore the exact q79 worldsheet CFT and string UV-inheritance theorem remain
conditional on the full character packet.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
