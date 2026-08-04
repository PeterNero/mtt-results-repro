from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2basedpathsystemandmonodromycandidate"
STATUS = "MTT_U6_Q79_92_BASED_MONODROMY_PATH_CARRIERS_CLOSED_90_SP4Z_CANDIDATES_UNPROMOTED"
NEXT = "MTT_Selected_q79GenusTwoValidatedBraidTubeAndGlobalMonodromyExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoBasedPathSystemAndMonodromyCandidate_v1.md"

CRITICAL_BALLS = OUT / "normalized_torus_critical_point_balls.packet.json"
PATHS = OUT / "certified_based_meridian_and_handle_paths.packet.json"
MONODROMY = OUT / "ninety_monodromy_candidates.unpromoted.packet.json"
GLOBAL_OPEN = OUT / "global_monodromy_and_braid_tube_execution.open.json"
FRONTIER = OUT / "U6_frontier_after_A113.packet.json"

A111_DISCRIMINANT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "degree90_nodal_discriminant_certificate.packet.json"
)
A112_ROOTS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2criticalvalueandnodeisolation"
    / "N90_certified_root_disks.packet.json"
)
EXPLORATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def polyval(coefficients: list[mp.mpf], value: mp.mpc) -> mp.mpc:
    result = mp.mpc(0)
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def complex_packet(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def packet_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def segment_distance(start: complex, end: complex, point: complex) -> float:
    direction = end - start
    if direction == 0:
        return abs(point - start)
    parameter = ((point - start).conjugate() * direction).real / abs(direction) ** 2
    parameter = min(1.0, max(0.0, parameter))
    return abs(point - (start + parameter * direction))


def torus_distance(left: complex, right: complex) -> float:
    return min(
        abs(left - (right + horizontal + 1j * vertical))
        for horizontal in (-1, 0, 1)
        for vertical in (-1, 0, 1)
    )


def matrix(rows: list[list[int]]) -> sp.Matrix:
    return sp.Matrix(rows)


def main() -> int:
    mp.mp.dps = 90
    for path in (A111_DISCRIMINANT, A112_ROOTS, EXPLORATION):
        if not path.exists():
            raise FileNotFoundError(path)

    discriminant = load(A111_DISCRIMINANT)
    roots112 = load(A112_ROOTS)
    exploration = load(EXPLORATION)

    n90 = [
        mp.mpf(value)
        for value in discriminant["norm_certificate"]["coefficients_descending"]
    ]
    n90_derivative = [
        coefficient * (len(n90) - 1 - index)
        for index, coefficient in enumerate(n90[:-1])
    ]
    p45 = [
        mp.mpf(value)
        for value in discriminant["discriminant_on_E"]["P45_coefficients_descending"]
    ]
    q43 = [
        mp.mpf(value)
        for value in discriminant["discriminant_on_E"]["Q43_coefficients_descending"]
    ]

    elliptic_parameter = mp.mpf("0.5")
    period_length = mp.sqrt(2) * mp.ellipk(elliptic_parameter)
    sn = mp.ellipfun("sn")
    cn = mp.ellipfun("cn")
    dn = mp.ellipfun("dn")

    def elliptic_ab(z_value: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
        argument = mp.sqrt(2) * z_value
        sn_value = sn(argument, elliptic_parameter)
        cn_value = cn(argument, elliptic_parameter)
        dn_value = dn(argument, elliptic_parameter)
        return (
            -1 + 2 / sn_value**2,
            -2 * mp.sqrt(2) * cn_value * dn_value / sn_value**3,
        )

    critical_entries: list[dict] = []
    critical_centers: list[complex] = []
    critical_radii: list[float] = []
    for disk in roots112["root_disks"]:
        disk_center = mp.mpc(disk["center_real"], disk["center_imaginary"])
        disk_radius = mp.mpf(disk["radius"])
        a_value = disk_center
        for _ in range(24):
            a_value -= polyval(n90, a_value) / polyval(n90_derivative, a_value)
        a_uncertainty = disk_radius + abs(a_value - disk_center)
        b_value = -polyval(p45, a_value) / polyval(q43, a_value)

        inverse_argument = mp.asin(mp.sqrt(2 / (a_value + 1)))
        z_value = mp.ellipf(inverse_argument, elliptic_parameter) / mp.sqrt(2)
        _, inverse_b = elliptic_ab(z_value)
        if abs(inverse_b - b_value) > abs(-inverse_b - b_value):
            z_value = -z_value
        w_value = z_value / period_length
        w_value -= mp.nint(mp.re(w_value)) + 1j * mp.nint(mp.im(w_value))

        # On the A112 a-disk, |a^3-a| stays away from zero. Since
        # dw/da=1/(2*L*b), this gives a direct inverse-function radius.
        cubic_center = a_value**3 - a_value
        cubic_variation = a_uncertainty * (3 * (abs(a_value) + a_uncertainty) ** 2 + 1)
        cubic_lower = abs(cubic_center) - cubic_variation
        if cubic_lower <= 0:
            raise AssertionError(f"elliptic branch overlap at {disk['root_id']}")
        inverse_derivative_upper = 1 / (2 * period_length * mp.sqrt(cubic_lower))
        w_radius = a_uncertainty * inverse_derivative_upper + mp.mpf("1e-40")

        center = complex(w_value)
        radius = float(w_radius)
        critical_centers.append(center)
        critical_radii.append(radius)
        critical_entries.append(
            {
                "root_id": disk["root_id"],
                "a_disk": {
                    "mpsolve_center_real": disk["center_real"],
                    "mpsolve_center_imaginary": disk["center_imaginary"],
                    "mpsolve_radius": disk["radius"],
                },
                "refined_a": {
                    "real": mp.nstr(mp.re(a_value), 50),
                    "imaginary": mp.nstr(mp.im(a_value), 50),
                    "N90_residual_upper": mp.nstr(abs(polyval(n90, a_value)), 8),
                },
                "b": {
                    "real": mp.nstr(mp.re(b_value), 50),
                    "imaginary": mp.nstr(mp.im(b_value), 50),
                },
                "w_ball_mod_Z_plus_iZ": {
                    "center": complex_packet(center),
                    "radius_upper": format(radius, ".17g"),
                    "inverse_derivative_upper": mp.nstr(inverse_derivative_upper, 18),
                    "elliptic_cubic_absolute_lower": mp.nstr(cubic_lower, 18),
                },
            }
        )

    pairwise_lower = math.inf
    for left in range(90):
        for right in range(left):
            pairwise_lower = min(
                pairwise_lower,
                torus_distance(critical_centers[left], critical_centers[right])
                - critical_radii[left]
                - critical_radii[right],
            )
    if pairwise_lower <= 0:
        raise AssertionError("critical balls overlap on normalized torus")

    critical_balls = {
        "schema": "MTTQ79NormalizedTorusCriticalPointBalls.v1",
        "status": "ALL_90_CRITICAL_POINTS_LIFTED_TO_DISJOINT_NORMALIZED_TORUS_BALLS",
        "uniformization": {
            "normalized_coordinate": "w=z/L mod Z+iZ",
            "L": "sqrt(2)*K(1/2)",
            "a": "wp(w;i)/L^2",
            "b": "wp'(w;i)/(2*L^3)",
            "period_length_decimal": mp.nstr(period_length, 60),
            "base_w": "(1+i)/4",
            "base_a": "-i",
            "base_b": "1+i",
        },
        "critical_point_count": len(critical_entries),
        "minimum_pairwise_torus_ball_separation_lower": format(pairwise_lower, ".17g"),
        "maximum_w_ball_radius_upper": format(max(critical_radii), ".17g"),
        "critical_points": critical_entries,
    }

    base = 0.25 + 0.25j

    def clearance_to_critical_balls(
        start: complex,
        end: complex,
        excluded_index: int | None = None,
        excluded_lift: complex | None = None,
    ) -> float:
        clearance = math.inf
        for index, center in enumerate(critical_centers):
            for horizontal in range(-2, 3):
                for vertical in range(-2, 3):
                    lift = center + horizontal + 1j * vertical
                    if (
                        excluded_index == index
                        and excluded_lift is not None
                        and abs(lift - excluded_lift) < 1e-13
                    ):
                        continue
                    clearance = min(
                        clearance,
                        segment_distance(start, end, lift) - critical_radii[index],
                    )
        return clearance - 1e-14

    def pole_clearance(start: complex, end: complex) -> float:
        return min(
            segment_distance(start, end, horizontal + 1j * vertical)
            for horizontal in range(-2, 3)
            for vertical in range(-2, 3)
        ) - 1e-14

    meridians: list[dict] = []
    for index, entry in enumerate(critical_entries):
        center = critical_centers[index]
        lift_candidates: list[tuple[float, float, float, complex]] = []
        for horizontal in (-1, 0, 1):
            for vertical in (-1, 0, 1):
                target_lift = center + horizontal + 1j * vertical
                critical_clearance = clearance_to_critical_balls(
                    base, target_lift, index, target_lift
                )
                infinity_clearance = pole_clearance(base, target_lift)
                if critical_clearance > 4e-4 and infinity_clearance > 0.04:
                    lift_candidates.append(
                        (
                            abs(target_lift - base),
                            -critical_clearance,
                            -infinity_clearance,
                            target_lift,
                        )
                    )
        if not lift_candidates:
            raise AssertionError(f"no safe direct lift for {entry['root_id']}")
        _, _, _, target_lift = min(lift_candidates, key=lambda row: row[:3])

        nearest_other_lower = min(
            torus_distance(center, other_center)
            - critical_radii[index]
            - critical_radii[other]
            for other, other_center in enumerate(critical_centers)
            if other != index
        )
        nearest_pole = min(
            abs(target_lift - (horizontal + 1j * vertical))
            for horizontal in range(-2, 3)
            for vertical in range(-2, 3)
        )
        loop_radius = min(0.004, nearest_other_lower / 8, nearest_pole / 8)
        if loop_radius <= 20 * critical_radii[index]:
            raise AssertionError(f"meridian too small for certified target ball: {entry['root_id']}")
        direction = (base - target_lift) / abs(base - target_lift)
        loop_start = target_lift + loop_radius * direction

        outbound_critical_clearance = clearance_to_critical_balls(base, loop_start)
        outbound_pole_clearance = pole_clearance(base, loop_start)
        circle_other_clearance = min(
            torus_distance(center, other_center) - loop_radius - critical_radii[other]
            for other, other_center in enumerate(critical_centers)
            if other != index
        )
        circle_target_margin = loop_radius - critical_radii[index]
        circle_pole_clearance = nearest_pole - loop_radius
        if min(
            outbound_critical_clearance,
            outbound_pole_clearance,
            circle_other_clearance,
            circle_target_margin,
            circle_pole_clearance,
        ) <= 0:
            raise AssertionError(f"uncertified based meridian: {entry['root_id']}")

        meridians.append(
            {
                "root_id": entry["root_id"],
                "target_lift": complex_packet(target_lift),
                "target_ball_radius_upper": format(critical_radii[index], ".17g"),
                "outbound_segment": {
                    "start": complex_packet(base),
                    "end": complex_packet(loop_start),
                    "critical_ball_clearance_lower": format(outbound_critical_clearance, ".17g"),
                    "elliptic_infinity_clearance_lower": format(outbound_pole_clearance, ".17g"),
                },
                "positive_meridian": {
                    "center": complex_packet(target_lift),
                    "radius": format(loop_radius, ".17g"),
                    "start_angle": format(math.atan2(direction.imag, direction.real), ".17g"),
                    "orientation": "counterclockwise",
                    "target_winding_number": 1,
                    "other_critical_ball_clearance_lower": format(circle_other_clearance, ".17g"),
                    "target_enclosure_margin_lower": format(circle_target_margin, ".17g"),
                    "elliptic_infinity_clearance_lower": format(circle_pole_clearance, ".17g"),
                },
                "return_segment": "exact reverse of outbound_segment",
            }
        )

    handle_rows: list[dict] = []
    for name, endpoint, lattice_class in (
        ("A", base + 1, "1"),
        ("B", base + 1j, "i"),
    ):
        critical_clearance = clearance_to_critical_balls(base, endpoint)
        infinity_clearance = pole_clearance(base, endpoint)
        if min(critical_clearance, infinity_clearance) <= 0:
            raise AssertionError(f"uncertified torus handle {name}")
        handle_rows.append(
            {
                "name": name,
                "universal_cover_start": complex_packet(base),
                "universal_cover_end": complex_packet(endpoint),
                "lattice_class": lattice_class,
                "critical_ball_clearance_lower": format(critical_clearance, ".17g"),
                "elliptic_infinity_clearance_lower": format(infinity_clearance, ".17g"),
            }
        )

    paths = {
        "schema": "MTTQ79GenusTwoBasedPathSystem.v1",
        "status": "90_POSITIVE_BASED_MERIDIANS_AND_2_TORUS_HANDLE_CARRIERS_CLOSED",
        "base_point": {
            "w": "(1+i)/4",
            "a": "-i",
            "b": "1+i",
            "regular_fiber": True,
        },
        "positive_based_meridians": meridians,
        "torus_handle_paths": handle_rows,
        "counts": {
            "critical_meridians": len(meridians),
            "torus_handles": len(handle_rows),
            "total_based_loops": len(meridians) + len(handle_rows),
        },
        "topology_guard": {
            "fundamental_group_type": "pi1(E_i minus 90 points)",
            "surface_relation_shape": "[A,B]*m1*...*m90=1 after conversion to one ordered distinguished cut system",
            "ordered_distinguished_cut_system_closed": False,
            "reason": "The 90 independently based meridians are certified carriers, but their mutual arc ordering has not yet been normalized into the displayed surface relation.",
        },
    }

    if exploration["status"] != "NUMERICAL_BRAID_MONODROMY_EXECUTED_INTERVAL_TUBE_CERTIFICATION_OPEN":
        raise AssertionError("unexpected numerical exploration status")
    if len(exploration["monodromies"]) != 90:
        raise AssertionError("numerical monodromy count")

    intersection = matrix(exploration["homology_convention"]["intersection_matrix"])
    identity = sp.eye(4)
    chain_vectors = [sp.Matrix(vector) for vector in exploration["homology_convention"]["chain_vectors_for_sigma_1_to_sigma_5"]]
    generators = [identity - vector * vector.T * intersection for vector in chain_vectors]
    generator_inverses = [generator.inv() for generator in generators]
    vectors: list[list[int]] = []
    matrix_rows: list[dict] = []
    raw_word_total = 0
    for index, row in enumerate(exploration["monodromies"]):
        if row["root_id"] != meridians[index]["root_id"]:
            raise AssertionError("root ordering mismatch")
        if abs(packet_complex(row["target_lift"]) - packet_complex(meridians[index]["target_lift"])) > 1e-13:
            raise AssertionError("path lift mismatch")
        monodromy_matrix = matrix(row["homology"]["picard_lefschetz_matrix"])
        delta = monodromy_matrix - identity
        if monodromy_matrix.T * intersection * monodromy_matrix != intersection:
            raise AssertionError("nonsymplectic monodromy candidate")
        if delta.rank() != 1 or delta * delta != sp.zeros(4):
            raise AssertionError("non-Lefschetz monodromy candidate")

        replay = identity
        for generator_index, sign in row["braid"]["raw_word"]:
            replay = (
                generators[generator_index - 1]
                if sign == 1
                else generator_inverses[generator_index - 1]
            ) * replay
        if replay != monodromy_matrix:
            raise AssertionError("braid word/matrix mismatch")
        permutation = row["braid"]["final_permutation"]
        moved = [position for position, value in enumerate(permutation) if position != value]
        if len(moved) != 2 or permutation[moved[0]] != moved[1] or permutation[moved[1]] != moved[0]:
            raise AssertionError("local root permutation is not a transposition")

        vector = row["homology"]["vanishing_cycle_primitive_up_to_sign"]
        vectors.append(vector)
        raw_word_total += row["braid"]["raw_length"]
        matrix_rows.append(
            {
                "root_id": row["root_id"],
                "vanishing_cycle_candidate_up_to_sign": vector,
                "picard_lefschetz_matrix_candidate": row["homology"]["picard_lefschetz_matrix"],
                "raw_braid_word_length": row["braid"]["raw_length"],
                "free_reduced_word_length": row["braid"]["free_reduced_length"],
                "root_permutation": permutation,
                "exact_algebraic_checks": {
                    "integral_symplectic": True,
                    "rank_M_minus_I": 1,
                    "M_minus_I_square_zero": True,
                    "raw_word_replays_matrix": True,
                },
                "promotion_accepted": False,
            }
        )

    span_rank = sp.Matrix(vectors).rank()
    if span_rank != 4:
        raise AssertionError("vanishing-cycle candidates do not span H1")

    monodromy = {
        "schema": "MTTQ79NinetyPicardLefschetzMonodromyCandidates.v1",
        "status": "90_INTEGRAL_SP4Z_TRANSVECTION_CANDIDATES_EXACTLY_REPLAYED_NUMERICAL_BRAID_ISOTOPY_UNCERTIFIED",
        "source_exploration": {
            "path": str(EXPLORATION.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(EXPLORATION),
            "root_solver": "python-flint 0.9.0 acb_poly pointwise root isolation",
            "projection": "s=1/(t-(2+3i)), angle pi/7",
            "active_verifier_policy": "hash and exact word/matrix replay; expensive trajectory regeneration is not run by default",
        },
        "common_fiber_homology_basis": ["a1", "b1", "a2", "b2"],
        "intersection_matrix": [list(map(int, row)) for row in intersection.tolist()],
        "candidate_rows": matrix_rows,
        "aggregate": {
            "candidate_matrix_count": len(matrix_rows),
            "exact_integral_symplectic_transvection_checks": len(matrix_rows),
            "transposition_checks": len(matrix_rows),
            "raw_braid_word_replay_checks": len(matrix_rows),
            "raw_braid_generator_total": raw_word_total,
            "vanishing_cycle_span_rank": span_rank,
            "distinct_vanishing_vectors_up_to_sign": exploration["aggregate"]["distinct_vanishing_vectors_up_to_sign"],
            "promoted_integral_monodromy_matrices": 0,
        },
        "promotion_guard": {
            "pointwise_root_disks_certified": True,
            "continuous_disjoint_root_tubes_certified": False,
            "piecewise_linear_braid_isotopy_certified": False,
            "torus_handle_monodromies_computed": False,
            "global_surface_relation_checked": False,
            "therefore_candidates_are_proof_rows": False,
        },
    }

    global_open = {
        "schema": "MTTQ79ValidatedBraidTubeAndGlobalMonodromyOpen.v1",
        "status": "CONTINUOUS_ROOT_TUBES_HANDLE_MONODROMIES_AND_GLOBAL_RELATION_OPEN",
        "required": {
            "Arb_Rouche_tubes_for_90_meridian_paths": None,
            "certified_piecewise_linear_braid_isotopies": None,
            "integral_A_handle_monodromy": None,
            "integral_B_handle_monodromy": None,
            "ordered_distinguished_cut_system": None,
            "global_relation_commutator_A_B_times_90_meridians": None,
        },
        "acceptance": {
            "promote_90_candidate_matrices": False,
            "rank4_Gauss_Manin_local_system_closed": False,
            "H2_Leray_basis_closed": False,
            "beta_C_period_rows_emitted": 0,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA113.v1",
        "status": STATUS,
        "critical_values_closed": 90,
        "nodal_points_closed": 90,
        "critical_meridian_path_carriers_closed": 90,
        "torus_handle_path_carriers_closed": 2,
        "integral_monodromy_candidates_computed": 90,
        "integral_monodromy_matrices_promoted": 0,
        "candidate_vanishing_cycle_span_rank": 4,
        "beta_C_period_rows_emitted": 0,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }

    outputs = {
        "critical_balls": str(CRITICAL_BALLS.relative_to(ROOT)).replace("\\", "/"),
        "based_paths": str(PATHS.relative_to(ROOT)).replace("\\", "/"),
        "monodromy_candidates": str(MONODROMY.relative_to(ROOT)).replace("\\", "/"),
        "global_open": str(GLOBAL_OPEN.relative_to(ROOT)).replace("\\", "/"),
        "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in (
        (CRITICAL_BALLS, critical_balls),
        (PATHS, paths),
        (MONODROMY, monodromy),
        (GLOBAL_OPEN, global_open),
        (FRONTIER, frontier),
    ):
        dump(path, payload)

    authority_hashes = [
        {"path": str(path), "sha256": sha256(path)}
        for path in (A111_DISCRIMINANT, A112_ROOTS, EXPLORATION)
    ]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoBasedPathSystemAndMonodromyCandidate.v1",
        "status": STATUS,
        "authority_hashes": authority_hashes,
        "outputs": outputs,
        "checks": {
            "all_90_torus_critical_balls_disjoint": True,
            "all_90_positive_based_meridians_certified": True,
            "two_torus_handle_path_carriers_certified": True,
            "all_90_candidate_matrices_integral_symplectic_transvections": True,
            "all_90_raw_braid_words_replay_exactly": True,
            "candidate_vanishing_cycles_span_rank4": True,
            "continuous_braid_tubes_not_invented": True,
            "handle_monodromies_not_invented": True,
            "beta_rows_not_invented": True,
            "trial_not_selected": True,
        },
        "results": frontier,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "next_required_artifact": NEXT,
    }
    certificate = {
        "certificate": "MTT_Selected_q79GenusTwoBasedPathSystemAndMonodromyCandidate_v1",
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": None,
        "checks": candidate["checks"],
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate["candidate_sha256"] = sha256(CANDIDATE)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Genus-Two Based Path System and Monodromy Candidate v1

Status: `{STATUS}`

## What A113 closes

The square elliptic base is now used in its normalized uniformization

```text
E_i = C/(Z+iZ),
a=wp(w;i)/L^2,
b=wp'(w;i)/(2 L^3),
L=sqrt(2) K(1/2).
```

The diagonal four-torsion point `w_*=(1+i)/4` is the exact regular base point
`(a_*,b_*)=(-i,1+i)`. A112's 90 `a`-disks lift to 90 pairwise-disjoint torus
balls. The inverse bound uses `dw/da=1/(2 L b)` and a direct lower bound for
`|a^3-a|` on every A112 disk.

For each critical ball A113 chooses a universal-cover lift, a straight outbound
segment, and a positive circle enclosing that ball alone. Every segment and
circle has an explicit positive lower clearance from every other critical ball
and from the elliptic-coordinate pole. This closes 90 reproducible based
meridian carriers. The two torus-handle paths `A:w_* -> w_*+1` and
`B:w_* -> w_*+i` are also certified. The base-monodromy problem therefore has
92 path carriers, not only the 90 local meridians.

## What the long numerical execution found

The frozen FLINT exploration transports all six hyperelliptic branch points
around each meridian. Its 90 root permutations are transpositions. Replaying
all `{raw_word_total}` Artin generators in the common chain basis gives 90
integral `Sp(4,Z)` matrices. Every matrix satisfies

```text
rank(M-I)=1,
(M-I)^2=0,
M^T J M=J.
```

The candidate vanishing cycles contain
`{exploration['aggregate']['distinct_vanishing_vectors_up_to_sign']}` distinct
primitive vectors up to sign and span all of `H_1(F_*,Z)=Z^4`. This is strong
consistency evidence and a concrete input to the next proof, not yet a promoted
monodromy theorem.

## Exact remaining promotion

The pointwise branch roots were isolated with FLINT, but no saved continuous
Rouche tube currently proves that each true strand is isotopic to the recorded
piecewise-linear strand over every adaptive segment. Consequently A113 keeps
all 90 matrices at candidate status. A114 must emit those disjoint tubes,
compute the `A` and `B` handle monodromies, normalize one ordered distinguished
cut system, and check the genus-one surface relation. Only then may the rank-four
Gauss-Manin local system feed the `8x92` period execution.

No beta period, gerbe zero, source selection, or strong-CP closure is inferred.
The constructive carrier still removes zero strict MTT source moduli.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
