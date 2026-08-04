from __future__ import annotations

import argparse
import hashlib
import json
import math
import tempfile
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import mpmath as mp
import numpy as np
from flint import acb, acb_mat, acb_poly, ctx
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from scipy.optimize import linear_sum_assignment

import build_q79_selected_alignment_dual_discriminant as dual
import build_q79_selected_alignment_fibration_seed as y_seed
import build_q79_selected_alignment_zchart_fibration_seed as z_seed
from certify_q79_selected_side_beta_defect_transport import (
    encoded_acb,
    encoded_matrix,
    lower,
    radius_upper,
)
from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator
from q79_selected_alignment_genus2_root_transport import decode_acb
from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentGaussManin,
    Q79SelectedAlignmentPeriodRootTransport,
    execute_selected_alignment_thimble_period,
)
from q79genus2_root_transport import midpoint


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
PROBE_DIRECTORY = PERIOD_DIRECTORY / "covariant_floating_probe"
Y_FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
DUAL = DIRECTORY / "selected_alignment_dual_discriminant.interval.packet.json"
TRAJECTORY_DIRECTORY = DIRECTORY / "selected_alignment_meridian_monodromy"
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
CENTRAL_HANDLES = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmenthandlesandglobalsurfacerelation"
    / "selected_alignment_global_integral_gauss_manin_factorization.packet.json"
)
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
CENTRAL_LIFTS = DIRECTORY / "selected_alignment_handle_central_lifts.interval.packet.json"
OLD_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
NEW_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order44_step002.interval.packet.json"
)
BROYDEN_SOURCE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_projective_ychart_broyden_04.exploratory.json"
)
CENTER_BETA_PROBE = PROBE_DIRECTORY / "selected_alignment_beta_floating_anchor.packet.json"
OMITTED = 2 + 3j
THIMBLE_CACHE_ALGORITHM = "fan_lift_representative_and_approach_root_rebase_v1"
HIGH_ACCURACY_THIMBLE_CACHE_ALGORITHM = (
    "fan_lift_representative_and_approach_root_rebase_high_accuracy_v1"
)
ULTRA_ACCURACY_THIMBLE_CACHE_ALGORITHM = (
    "fan_lift_representative_and_approach_root_rebase_ultra_accuracy_v1"
)
EXTREME_ACCURACY_THIMBLE_CACHE_ALGORITHM = (
    "fan_lift_representative_and_approach_root_rebase_extreme_accuracy_v1"
)
BETA_BRANCH_ROUTE = "z_source_clockwise_winding_then_exact_y_transition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_vector(rows: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in rows], dtype=np.complex128)


def complex_matrix(rows: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def encoded_complex_matrix(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [[complex_pair(complex(value)) for value in row] for row in matrix]


def encoded_complex_vector(vector: np.ndarray) -> list[dict[str, str]]:
    return [complex_pair(complex(value)) for value in vector]


def point_ball(value: complex) -> acb:
    return acb(format(value.real, ".17g"), format(value.imag, ".17g"))


def point_matrix(matrix: np.ndarray) -> acb_mat:
    return acb_mat([[point_ball(complex(value)) for value in row] for row in matrix])


def central_alignment() -> np.ndarray:
    packet = load(Y_FIBRATION)
    return np.asarray(
        [
            [midpoint(decode_acb(value)) for value in row]
            for row in packet["source"]["alignment_interval"]
        ],
        dtype=np.complex128,
    )


def build_point_fibration(alignment: np.ndarray, chart: str) -> dict:
    alignment_ball = point_matrix(alignment)
    determinant = alignment_ball.det()
    if lower(abs(determinant)) <= 0:
        raise AssertionError("perturbed alignment determinant contains zero")
    line = y_seed.line_polynomials(alignment_ball)
    tables = PGL3BetaEvaluator().tables
    coefficient_builder = (
        y_seed.aligned_chart_y_coefficients
        if chart == "y"
        else z_seed.aligned_chart_z_coefficients
    )
    f6 = coefficient_builder(tables["F6"], line)
    g3 = coefficient_builder(tables["G3"], line)
    q2 = coefficient_builder(tables["Q2"], line)
    h4 = coefficient_builder(tables["H4"], line)
    residual = y_seed.t_subtract(
        f6,
        y_seed.t_convolution(g3, g3),
        y_seed.t_convolution(q2, h4),
    )
    residual_values = [value for row in residual for value in row.values()]
    if not residual_values or not all(value.contains(0) for value in residual_values):
        raise AssertionError("perturbed splitting identity failed")
    return {
        "schema": "MTTQ79CovariantFloatingPointFibration.v1",
        "status": "PERTURBED_ALIGNMENT_POINT_FIBRATION_EMITTED",
        "source": {
            "alignment_constructor": "A_selected*exp(sign*h*T_s)",
            "carrier_side": "local continuation from A125/A126 selected side",
            "line": "L=A*[a,b,1]^T and L0*x+L1*y+L2*z=0",
            "line_chart": chart,
            "alignment_interval": encoded_matrix(alignment_ball),
            "alignment_determinant": encoded_acb(determinant),
            "alignment_determinant_absolute_lower": format(
                lower(abs(determinant)), ".17g"
            ),
        },
        "fiber_polynomials": {
            "coefficient_order": "ascending powers of t",
            "coefficient_encoding": "sparse ACB polynomial in a,b",
            "F6": [y_seed.encode_poly(value) for value in f6],
            "G3": [y_seed.encode_poly(value) for value in g3],
            "Q2": [y_seed.encode_poly(value) for value in q2],
            "H4": [y_seed.encode_poly(value) for value in h4],
        },
        "splitting_identity": {
            "formula": "F6=G3^2+Q2*H4",
            "coefficient_balls_checked": len(residual_values),
            "every_residual_coefficient_contains_zero": True,
            "maximum_residual_coefficient_radius_upper": format(
                max(radius_upper(value) for value in residual_values), ".17g"
            ),
        },
        "strict_scope": {
            "point_ball_rounding_only": True,
            "alignment_neighborhood_certified": False,
            "floating_probe_only": True,
            "observed_SM_values_used": False,
        },
    }


def torus_distance(left: complex, right: complex) -> float:
    difference = left - right
    difference -= round(difference.real) + 1j * round(difference.imag)
    return float(abs(difference))


def uniformizing_lift(a_value: complex, b_value: complex, reference: complex) -> complex:
    mp.mp.dps = 80
    a_mp = mp.mpc(a_value.real, a_value.imag)
    b_mp = mp.mpc(b_value.real, b_value.imag)
    parameter = mp.mpf("0.5")
    period_length = mp.sqrt(2) * mp.ellipk(parameter)
    inverse_argument = mp.asin(mp.sqrt(2 / (a_mp + 1)))
    value = mp.ellipf(inverse_argument, parameter) / mp.sqrt(2)
    sn = mp.ellipfun("sn")
    cn = mp.ellipfun("cn")
    dn = mp.ellipfun("dn")

    def elliptic_b(z_value: mp.mpc) -> mp.mpc:
        argument = mp.sqrt(2) * z_value
        sn_value = sn(argument, parameter)
        return -2 * mp.sqrt(2) * cn(argument, parameter) * dn(
            argument, parameter
        ) / sn_value**3

    if abs(elliptic_b(value) - b_mp) > abs(elliptic_b(-value) - b_mp):
        value = -value
    w_value = complex(value / period_length)
    difference = w_value - reference
    return w_value - round(difference.real) - 1j * round(difference.imag)


def continued_critical_centers(alignment: np.ndarray) -> tuple[dict[str, complex], dict]:
    packet = load(DUAL)
    fan_reference = {
        row["root_id"]: complex_value(row["canonical_lift"])
        for row in load(FAN)["distinguished_positive_meridians"]
    }
    alignment_ball = point_matrix(alignment)
    lines: list[dual.EllipticPair] = [
        (
            {0: alignment_ball[row, 2], 1: alignment_ball[row, 0]},
            {0: alignment_ball[row, 1]},
        )
        for row in range(3)
    ]
    selected: dual.EllipticPair = ({}, {})
    for row in packet["dual_discriminant"]["integer_coefficient_rows"]:
        contribution: dual.EllipticPair = ({0: acb(int(row["coefficient"]))}, {})
        for source, power in zip(lines, row["powers_L0_L1_L2"]):
            contribution = dual.pair_multiply(
                contribution, dual.pair_power(source, int(power))
            )
        selected = dual.pair_add(selected, contribution)
    p_value, q_value = selected
    norm = dual.poly_add(
        dual.poly_multiply(p_value, p_value),
        dual.poly_scale(
            dual.poly_add(
                dual.poly_shift(dual.poly_multiply(q_value, q_value), 3),
                dual.poly_scale(
                    dual.poly_shift(dual.poly_multiply(q_value, q_value), 1), -1
                ),
            ),
            -1,
        ),
    )
    roots = acb_poly([norm.get(index, acb(0)) for index in range(91)]).roots(
        tol=1.0e-38,
        maxprec=4096,
    )
    if len(roots) != 90 or not all(root.is_finite() for root in roots):
        raise AssertionError("perturbed discriminant root isolation failed")
    central_points = packet["critical_points_on_E"]["points"]
    central_a = np.asarray(
        [midpoint(decode_acb(row["a"])) for row in central_points],
        dtype=np.complex128,
    )
    new_a = np.asarray([midpoint(root) for root in roots], dtype=np.complex128)
    assignment_cost = np.abs(central_a[:, np.newaxis] - new_a[np.newaxis, :])
    central_rows, new_columns = linear_sum_assignment(assignment_cost)
    if not np.array_equal(central_rows, np.arange(90)):
        raise AssertionError("critical continuation assignment order changed")
    maximum_a_shift = float(np.max(assignment_cost[central_rows, new_columns]))
    centers: dict[str, complex] = {}
    maximum_w_shift = 0.0
    maximum_elliptic_residual = 0.0
    maximum_dual_residual = 0.0
    for central_index, root_index in zip(central_rows, new_columns):
        root = roots[int(root_index)]
        p_at_root = dual.poly_evaluate(p_value, root)
        q_at_root = dual.poly_evaluate(q_value, root)
        if lower(abs(q_at_root)) <= 0:
            raise AssertionError("perturbed Q coefficient contains zero")
        b_ball = -p_at_root / q_at_root
        a_center = midpoint(root)
        b_center = midpoint(b_ball)
        central_row = central_points[int(central_index)]
        reference = fan_reference[central_row["root_id"]]
        w_value = uniformizing_lift(a_center, b_center, reference)
        centers[central_row["root_id"]] = w_value
        maximum_w_shift = max(maximum_w_shift, torus_distance(w_value, reference))
        maximum_elliptic_residual = max(
            maximum_elliptic_residual, abs(b_center**2 - a_center**3 + a_center)
        )
        maximum_dual_residual = max(
            maximum_dual_residual, abs(midpoint(p_at_root + b_ball * q_at_root))
        )
    minimum_new_separation = min(
        torus_distance(left, right)
        for index, left in enumerate(centers.values())
        for right in list(centers.values())[:index]
    )
    if minimum_new_separation <= 0:
        raise AssertionError("perturbed critical centers collide")
    handle_coordinates = {
        "A": lambda value: value.imag - 0.25,
        "B": lambda value: value.real - 0.25,
    }
    handle_wall_diagnostics = {}
    for name, coordinate in handle_coordinates.items():
        central_signed = {
            root_id: coordinate(value) - round(coordinate(value))
            for root_id, value in fan_reference.items()
        }
        perturbed_signed = {
            root_id: coordinate(value) - round(coordinate(value))
            for root_id, value in centers.items()
        }
        crossings = sorted(
            root_id
            for root_id in centers
            if central_signed[root_id] * perturbed_signed[root_id] < 0
        )
        handle_wall_diagnostics[name] = {
            "central_minimum_transverse_clearance": min(
                abs(value) for value in central_signed.values()
            ),
            "perturbed_minimum_transverse_clearance": min(
                abs(value) for value in perturbed_signed.values()
            ),
            "crossed_critical_root_ids": crossings,
            "same_fixed_handle_chamber": not crossings,
        }
    return centers, {
        "isolated_roots": len(roots),
        "matching_method": "Hungarian continuation from selected a-roots",
        "maximum_a_root_shift": maximum_a_shift,
        "maximum_torus_lift_shift": maximum_w_shift,
        "minimum_pairwise_torus_separation": minimum_new_separation,
        "maximum_midpoint_elliptic_residual": maximum_elliptic_residual,
        "maximum_midpoint_dual_residual": maximum_dual_residual,
        "fixed_handle_path_wall_diagnostics": handle_wall_diagnostics,
    }


def central_period_path(index: int, root_id: str) -> Path:
    return PERIOD_DIRECTORY / f"d{index:03d}_{root_id}.thimble_period.candidate.json"


def thimble_worker(task: dict) -> dict:
    index = int(task["distinguished_index"])
    root_id = task["root_id"]
    central_packet_path = Path(task["central_packet_path"])
    central_packet = load(central_packet_path)
    line_chart = central_packet.get("line_chart", "y")
    fibration = Path(task["y_fibration"] if line_chart == "y" else task["z_fibration"])
    stem = f"d{index:03d}_{root_id}"
    trajectory_packet_path = TRAJECTORY_DIRECTORY / f"{stem}.packet.json"
    trajectory_packet = load(trajectory_packet_path)
    if line_chart == "y":
        trajectory_path = ROOT / trajectory_packet["trajectory"]["path"]
    else:
        trajectory_path = (
            PERIOD_DIRECTORY
            / "adapted_line_chart_approaches"
            / f"{stem}.y_to_z_approach.trajectory.npz"
        )
    homology = load(HOMOLOGY)["homology_convention"]
    critical_center = complex(*task["critical_center"])
    with np.load(trajectory_path) as saved:
        saved_w = np.asarray(saved["w"], dtype=np.complex128)
        saved_roots = np.asarray(saved["roots"], dtype=np.complex128)
        saved_radii = np.asarray(saved["root_radius_uppers"], dtype=np.float64)
    saved_distances = np.abs(saved_w - critical_center)
    saved_minimum = float(np.min(saved_distances))
    approach_indices = np.flatnonzero(saved_distances <= saved_minimum * 1.001)
    if not len(approach_indices):
        raise AssertionError("saved trajectory has no perturbed approach point")
    approach_index = int(approach_indices[0])
    approach = complex(saved_w[approach_index])
    numerical_profile = task.get("numerical_profile", "production")
    if numerical_profile == "production":
        cache_algorithm = THIMBLE_CACHE_ALGORITHM
        dps = 70
        inner_order = 160
        root_step_ratio = 0.12
        rtol = 2.0e-10
        atol = 2.0e-13
        local_outer_order = 32
        tail_outer_order = 24
    elif numerical_profile == "high_accuracy":
        cache_algorithm = HIGH_ACCURACY_THIMBLE_CACHE_ALGORITHM
        dps = 90
        inner_order = 256
        root_step_ratio = 0.08
        rtol = 2.0e-12
        atol = 2.0e-15
        local_outer_order = 48
        tail_outer_order = 40
    elif numerical_profile == "ultra_accuracy":
        cache_algorithm = ULTRA_ACCURACY_THIMBLE_CACHE_ALGORITHM
        dps = 110
        inner_order = 384
        root_step_ratio = 0.05
        rtol = 2.0e-13
        atol = 2.0e-16
        local_outer_order = 72
        tail_outer_order = 64
    elif numerical_profile == "extreme_accuracy":
        cache_algorithm = EXTREME_ACCURACY_THIMBLE_CACHE_ALGORITHM
        dps = 130
        inner_order = 512
        root_step_ratio = 0.035
        rtol = 5.0e-14
        atol = 5.0e-17
        local_outer_order = 96
        tail_outer_order = 80
    else:
        raise ValueError(f"unknown thimble numerical profile: {numerical_profile}")
    transport = Q79SelectedAlignmentPeriodRootTransport(
        fibration, homology, omitted=OMITTED, dps=dps
    )
    unordered, unordered_radii = transport.roots_at(approach)
    rebased, rebased_radii, rebase_ratio = transport.match(
        saved_roots[approach_index], unordered, unordered_radii
    )
    rebased_roots = saved_roots.copy()
    rebased_root_radii = saved_radii.copy()
    rebased_roots[approach_index] = rebased
    rebased_root_radii[approach_index] = rebased_radii
    with tempfile.TemporaryDirectory(prefix=f"q79-rebase-{index:03d}-") as directory:
        rebased_path = Path(directory) / "trajectory.npz"
        np.savez_compressed(
            rebased_path,
            w=saved_w,
            roots=rebased_roots,
            root_radius_uppers=rebased_root_radii,
        )
        execution = execute_selected_alignment_thimble_period(
            fibration_path=fibration,
            homology_convention=homology,
            trajectory_path=rebased_path,
            trajectory_packet=trajectory_packet,
            critical_center=critical_center,
            omitted=OMITTED,
            epsilon=1.0e-5,
            inner_order=inner_order,
            dps=dps,
            root_step_ratio=root_step_ratio,
            rtol=rtol,
            atol=atol,
            gauss_manin_chart="t",
            local_direct_cutoff=0.0,
            local_outer_order=local_outer_order,
            tail_outer_order=tail_outer_order,
        )
    period = complex_vector(execution["period_values"])
    base = complex_vector(
        [row["value"] for row in execution["base_fiber_propagated_periods"]]
    )
    central_period = complex_vector(central_packet["execution"]["period_values"])
    positive = float(np.linalg.norm(period - central_period))
    negative = float(np.linalg.norm(period + central_period))
    continuity_sign = 1 if positive <= negative else -1
    period *= continuity_sign
    base *= continuity_sign
    return {
        "schema": "MTTQ79CovariantFloatingThimbleCache.v1",
        "cache_algorithm": cache_algorithm,
        "numerical_profile": numerical_profile,
        "distinguished_index": index,
        "root_id": root_id,
        "line_chart": line_chart,
        "critical_center": complex_pair(complex(*task["critical_center"])),
        "period_values": encoded_complex_vector(period),
        "base_fiber_propagated_periods": encoded_complex_vector(base),
        "continuity_sign_relative_to_selected_packet": continuity_sign,
        "positive_continuity_residual": positive,
        "negative_continuity_residual": negative,
        "approach_root_rebase": {
            "approach_index": approach_index,
            "approach_parameter": complex_pair(approach),
            "central_to_perturbed_matching_ratio": rebase_ratio,
            "maximum_root_displacement": float(
                np.max(abs(rebased - saved_roots[approach_index]))
            ),
        },
        "runner_source_sha256": sha256(Path(__file__).resolve()),
        "numerics": execution["numerics"],
    }


def beta_anchor(alignment: np.ndarray, *, force: bool = False) -> tuple[np.ndarray, complex, dict]:
    if CENTER_BETA_PROBE.exists() and not force:
        packet = load(CENTER_BETA_PROBE)
        if packet.get("beta_branch_route") == BETA_BRANCH_ROUTE:
            return (
                complex_vector(packet["floating_beta"]),
                complex_value(packet["wound_branch_point"]),
                packet,
            )
    evaluator = PGL3BetaEvaluator()
    source_reference_row = load(BROYDEN_SOURCE)["final_winding_reference"]
    source_reference = complex(
        float(source_reference_row["r"]), float(source_reference_row["i"])
    )
    beta, diagnostics = evaluator.evaluate(
        alignment,
        line_chart="y",
        base_lift_source_chart="z",
        rtol=2.0e-9,
        atol=2.0e-11,
        winding_reference=source_reference,
    )
    beta_packet_path = min(
        [path for path in (OLD_BETA, NEW_BETA) if path.exists()],
        key=lambda path: float(load(path)["endpoint"]["uniform_component_radius_upper"]),
    )
    certified = complex_vector(load(beta_packet_path)["endpoint"]["beta_center"])
    wound = complex_value(
        diagnostics["base_lift_diagnostics"]["wound_branch_point"]
    )
    packet = {
        "schema": "MTTQ79SelectedAlignmentFloatingBetaAnchor.v1",
        "status": "FLOATING_BETA_ANCHORED_TO_CERTIFIED_SELECTED_SIDE_CENTER",
        "beta_branch_route": BETA_BRANCH_ROUTE,
        "alignment": encoded_complex_matrix(alignment),
        "floating_beta": encoded_complex_vector(beta),
        "certified_beta": encoded_complex_vector(certified),
        "floating_to_certified_maximum_absolute_difference": float(
            np.max(abs(beta - certified))
        ),
        "wound_branch_point": complex_pair(wound),
        "source_winding_reference": complex_pair(source_reference),
        "diagnostics": diagnostics,
        "authority": {
            "certified_beta_packet": relative(beta_packet_path),
            "certified_beta_packet_sha256": sha256(beta_packet_path),
            "Broyden_branch_source": relative(BROYDEN_SOURCE),
            "Broyden_branch_source_sha256": sha256(BROYDEN_SOURCE),
        },
        "strict_scope": {
            "floating_derivative_anchor_only": True,
            "interval_derivative_certificate": False,
            "observed_SM_values_used": False,
        },
    }
    dump(CENTER_BETA_PROBE, packet)
    return beta, wound, packet


def selected_certified_beta() -> tuple[np.ndarray, Path]:
    path = min(
        [path for path in (OLD_BETA, NEW_BETA) if path.exists()],
        key=lambda item: float(load(item)["endpoint"]["uniform_component_radius_upper"]),
    )
    return complex_vector(load(path)["endpoint"]["beta_center"]), path


def moving_y_to_z_transition(
    y_fibration: Path,
    alignment: np.ndarray,
    homology: dict,
) -> np.ndarray:
    transport = Q79SelectedAlignmentPeriodRootTransport(
        y_fibration, homology, omitted=OMITTED, dps=80
    )
    a_value, b_value = [midpoint(value) for value in transport.ab_at(transport.base)]
    line = alignment @ np.asarray([a_value, b_value, 1 + 0j], dtype=np.complex128)
    alpha = -line[0] / line[1]
    gamma = -line[2] / line[1]
    common = -(line[1] ** 2) / (line[2] ** 2)
    transition = np.zeros((5, 5), dtype=np.complex128)
    for power in range(5):
        for index in range(power + 1):
            transition[power, index] = (
                common
                * math.comb(power, index)
                * alpha ** (power - index)
                * gamma**index
            )
    return transition


def execute_moving_handle(
    name: str,
    displacement: complex,
    action: np.ndarray,
    expected_lift: int,
    initial_periods: np.ndarray,
    homology: dict,
    fibration: Path,
    numerical_profile: str = "production",
) -> tuple[np.ndarray, dict]:
    if numerical_profile == "production":
        dps = 80
        rtol = 2.0e-10
        atol = 2.0e-13
    elif numerical_profile == "high_accuracy":
        dps = 100
        rtol = 2.0e-12
        atol = 2.0e-15
    elif numerical_profile == "ultra_accuracy":
        dps = 120
        rtol = 2.0e-13
        atol = 2.0e-16
    elif numerical_profile == "extreme_accuracy":
        dps = 140
        rtol = 5.0e-14
        atol = 5.0e-17
    else:
        raise ValueError(f"unknown handle numerical profile: {numerical_profile}")
    transport = Q79SelectedAlignmentPeriodRootTransport(
        fibration, homology, omitted=OMITTED, dps=dps
    )
    gauss_manin = Q79SelectedAlignmentGaussManin(
        fibration, transport, coordinate="t", omitted=OMITTED
    )
    initial_state = np.concatenate(
        [
            initial_periods.reshape(-1),
            np.zeros((8, 4), dtype=np.complex128).reshape(-1),
        ]
    )

    def differential(parameter: float, state: np.ndarray) -> np.ndarray:
        periods = state[:20].reshape(5, 4)
        w_value = transport.base + parameter * displacement
        connection, a_value, b_value = gauss_manin.connection(w_value)
        period_derivative = displacement * connection @ periods
        integral_derivative = np.column_stack(
            [
                gauss_manin.period_length
                * displacement
                * gauss_manin.residue_rows(periods[:, column], a_value, b_value)
                for column in range(4)
            ]
        )
        return np.concatenate(
            [period_derivative.reshape(-1), integral_derivative.reshape(-1)]
        )

    solution = solve_ivp(
        differential,
        (0.0, 1.0),
        initial_state,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )
    if not solution.success:
        raise AssertionError(solution.message)
    endpoint = solution.y[:20, -1].reshape(5, 4)
    handle_integrals = solution.y[20:, -1].reshape(8, 4)
    predicted = initial_periods[:2, :] @ action
    endpoint_holomorphic = endpoint[:2, :]
    scale = max(np.linalg.norm(endpoint_holomorphic), np.linalg.norm(predicted))
    positive = float(np.linalg.norm(endpoint_holomorphic - predicted) / scale)
    negative = float(np.linalg.norm(endpoint_holomorphic + predicted) / scale)
    selected_lift = 1 if positive <= negative else -1
    selected_error = min(positive, negative)
    if selected_lift != expected_lift:
        raise AssertionError(f"moving handle {name} changed its central lift")
    if selected_error >= 1.0e-4:
        raise AssertionError(
            f"moving handle {name} monodromy residual too large: {selected_error}"
        )
    return handle_integrals, {
        "name": name,
        "numerical_profile": numerical_profile,
        "selected_lift": selected_lift,
        "expected_lift": expected_lift,
        "positive_lift_scaled_residual": positive,
        "negative_lift_scaled_residual": negative,
        "selected_lift_scaled_residual": selected_error,
        "production_gate_5e_7_passed": selected_error < 5.0e-7,
        "exploratory_gate_1e_4_passed": True,
        "ODE_function_evaluations": solution.nfev,
        "maximum_reduction_relative_residual": (
            gauss_manin.maximum_reduction_relative_residual
        ),
    }


def probe_tag(direction: int, sign: int, step: float) -> str:
    step_tag = format(step, ".1e").replace("+", "p").replace("-", "m").replace(".", "d")
    sign_tag = "p" if sign > 0 else "m"
    return f"d{direction + 1:02d}_{sign_tag}_h{step_tag}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direction", type=int, required=True, help="zero-based sl3 direction")
    parser.add_argument("--sign", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--step", type=float, default=1.0e-6)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--critical-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    if not 0 <= arguments.direction < 8:
        raise ValueError("direction must lie in 0,...,7")
    if arguments.step <= 0:
        raise ValueError("step must be positive")
    ctx.dps = 100
    started = time.perf_counter()
    tag = probe_tag(arguments.direction, arguments.sign, arguments.step)
    output_directory = PROBE_DIRECTORY / tag
    output = output_directory / "probe.packet.json"
    if output.exists() and not arguments.force and not arguments.critical_only:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    a208 = load(A208)
    candidates = a208["height_four_candidates"][1:]
    support = sorted(
        {
            int(row["distinguished_index"])
            for candidate in candidates
            for row in candidate["primitive_thimble_chain"]
        }
    )
    orientation = load(ORIENTATION)
    support = sorted(
        set(support)
        | {int(value) for value in orientation["unimodular_pivot_indices_one_based"]}
    )
    base_alignment = central_alignment()
    generator = PGL3BetaEvaluator().generators[arguments.direction]
    alignment = base_alignment @ expm(
        arguments.sign * arguments.step * generator
    )
    output_directory.mkdir(parents=True, exist_ok=True)
    y_path = output_directory / "fy.packet.json"
    z_path = output_directory / "fz.packet.json"
    dump(y_path, build_point_fibration(alignment, "y"))
    dump(z_path, build_point_fibration(alignment, "z"))
    centers, critical_diagnostics = continued_critical_centers(alignment)
    if arguments.critical_only:
        result = {
            "tag": tag,
            "support": len(support),
            "critical_continuation": critical_diagnostics,
            "elapsed_seconds": time.perf_counter() - started,
        }
        dump(output_directory / "critical.packet.json", result)
        print(json.dumps(result, indent=2))
        return 0
    crossed_handles = [
        name
        for name, row in critical_diagnostics[
            "fixed_handle_path_wall_diagnostics"
        ].items()
        if not row["same_fixed_handle_chamber"]
    ]
    if crossed_handles:
        raise AssertionError(
            "perturbation crosses fixed handle path wall(s): "
            + ", ".join(crossed_handles)
            + "; reduce the finite-difference step or transport the handle path"
        )

    fan_by_index = {
        int(row["distinguished_index"]): row
        for row in load(FAN)["distinguished_positive_meridians"]
    }
    cache_directory = output_directory / "thimbles"
    cache_directory.mkdir(parents=True, exist_ok=True)
    thimbles: dict[int, dict] = {}
    tasks = []
    for index in support:
        fan_row = fan_by_index[index]
        cache = cache_directory / f"t{index:03d}.json"
        if cache.exists() and not arguments.force:
            cached = load(cache)
            expected_center = centers[fan_row["root_id"]]
            cached_center = complex_value(cached["critical_center"])
            if (
                cached.get("cache_algorithm") == THIMBLE_CACHE_ALGORITHM
                and abs(cached_center - expected_center) <= 1.0e-14
            ):
                thimbles[index] = cached
                continue
        center = centers[fan_row["root_id"]]
        tasks.append(
            {
                "distinguished_index": index,
                "root_id": fan_row["root_id"],
                "central_packet_path": str(central_period_path(index, fan_row["root_id"])),
                "critical_center": [center.real, center.imag],
                "y_fibration": str(y_path),
                "z_fibration": str(z_path),
            }
        )
    if tasks:
        with ProcessPoolExecutor(max_workers=arguments.workers) as executor:
            futures = {executor.submit(thimble_worker, task): task for task in tasks}
            for completed, future in enumerate(as_completed(futures), start=1):
                row = future.result()
                index = int(row["distinguished_index"])
                thimbles[index] = row
                dump(cache_directory / f"t{index:03d}.json", row)
                print(f"[{completed}/{len(tasks)}] continued d{index:03d}", flush=True)

    factorization = load(FACTORIZATION)
    vectors = np.asarray(
        [row["positive_vanishing_cycle_up_to_sign"] for row in factorization["factors"]],
        dtype=np.int64,
    ).T
    pivots = np.asarray(
        [int(value) - 1 for value in orientation["unimodular_pivot_indices_one_based"]],
        dtype=np.int64,
    )
    homology = load(HOMOLOGY)["homology_convention"]
    y_to_z = moving_y_to_z_transition(y_path, alignment, homology)
    pivot_columns = []
    for index in pivots:
        row = thimbles[int(index) + 1]
        values = complex_vector(row["base_fiber_propagated_periods"])
        if row["line_chart"] == "z":
            values = np.linalg.solve(y_to_z, values)
        pivot_columns.append(values)
    pivot_periods = np.column_stack(pivot_columns)
    pivot_signs = np.asarray(orientation["pivot_signs"], dtype=np.int64)
    marked_basis = (pivot_periods * pivot_signs[np.newaxis, :]) @ np.linalg.inv(
        vectors[:, pivots]
    )
    actions = {
        name: np.asarray(factorization["handle_actions"][name], dtype=np.int64)
        for name in ("A", "B")
    }
    central_lifts = {
        name: int(value) for name, value in load(CENTRAL_LIFTS)["selected_lifts"].items()
    }
    handle_rows = []
    handle_blocks = []
    for name, displacement in (("A", 1 + 0j), ("B", 1j)):
        block, diagnostics = execute_moving_handle(
            name,
            displacement,
            actions[name],
            central_lifts[name],
            marked_basis,
            homology,
            y_path,
        )
        handle_blocks.append(block)
        handle_rows.append(diagnostics)
    handles = np.hstack(handle_blocks)

    center_floating_beta, wound_reference, anchor_packet = beta_anchor(base_alignment)
    evaluator = PGL3BetaEvaluator()
    perturbed_floating_beta, beta_diagnostics = evaluator.evaluate(
        alignment,
        line_chart="y",
        base_lift_source_chart="z",
        rtol=2.0e-9,
        atol=2.0e-11,
        winding_reference=wound_reference,
    )
    certified_beta, certified_beta_path = selected_certified_beta()
    anchored_beta = certified_beta + perturbed_floating_beta - center_floating_beta

    column_signs = np.asarray(orientation["column_signs"], dtype=np.int64)
    candidate_rows = []
    for candidate in candidates:
        period = np.zeros(8, dtype=np.complex128)
        for row in candidate["primitive_thimble_chain"]:
            index = int(row["distinguished_index"])
            value = complex_vector(thimbles[index]["period_values"])
            period += int(row["coefficient"]) * column_signs[index - 1] * value
        period += handles @ np.asarray(
            candidate["primitive_handle_coordinates"], dtype=np.float64
        )
        residual = anchored_beta - period
        candidate_rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "A132_objective_rank": candidate["A132_objective_rank"],
                "moving_period": encoded_complex_vector(period),
                "covariant_residual_F": encoded_complex_vector(residual),
                "residual_maximum_absolute_value": float(np.max(abs(residual))),
                "residual_l2_norm": float(np.linalg.norm(residual)),
            }
        )
    continuity_flips = [
        index
        for index, row in thimbles.items()
        if int(row["continuity_sign_relative_to_selected_packet"]) == -1
    ]
    central_handles = complex_matrix(load(CENTRAL_HANDLES)["primitive_handle_period_matrix"])
    packet = {
        "schema": "MTTQ79HeightFourCovariantFloatingProbe.v1",
        "status": "SAME_SOURCE_MOVING_BETA_AND_PERIOD_PROBE_EXECUTED",
        "tag": tag,
        "perturbation": {
            "direction_zero_based": arguments.direction,
            "direction_one_based": arguments.direction + 1,
            "sign": arguments.sign,
            "step": arguments.step,
            "formula": "A=A_selected*exp(sign*h*T_s)",
            "alignment": encoded_complex_matrix(alignment),
            "determinant": complex_pair(np.linalg.det(alignment)),
        },
        "critical_continuation": critical_diagnostics,
        "thimble_continuation": {
            "requested_indices": support,
            "continued_columns": len(thimbles),
            "continuity_sign_flips": continuity_flips,
            "all_cached_packets": [
                relative(cache_directory / f"t{index:03d}.json") for index in support
            ],
        },
        "moving_marked_basis": {
            "pivot_indices_one_based": [int(value) + 1 for value in pivots],
            "marked_base_period_matrix": encoded_complex_matrix(marked_basis),
        },
        "moving_handles": {
            "primitive_handle_period_matrix": encoded_complex_matrix(handles),
            "maximum_absolute_change_from_selected_center": float(
                np.max(abs(handles - central_handles))
            ),
            "diagnostics": handle_rows,
        },
        "moving_beta": {
            "floating_center_anchor_path": relative(CENTER_BETA_PROBE),
            "floating_center_anchor_sha256": sha256(CENTER_BETA_PROBE),
            "certified_center_path": relative(certified_beta_path),
            "certified_center_sha256": sha256(certified_beta_path),
            "center_floating_to_certified_maximum_absolute_difference": anchor_packet[
                "floating_to_certified_maximum_absolute_difference"
            ],
            "perturbed_floating_beta": encoded_complex_vector(perturbed_floating_beta),
            "certified_center_anchored_perturbed_beta": encoded_complex_vector(anchored_beta),
            "diagnostics": beta_diagnostics,
        },
        "candidate_residuals": candidate_rows,
        "summary": {
            "candidate_count": len(candidate_rows),
            "continued_thimble_columns": len(thimbles),
            "maximum_critical_torus_shift": critical_diagnostics[
                "maximum_torus_lift_shift"
            ],
            "minimum_critical_torus_separation": critical_diagnostics[
                "minimum_pairwise_torus_separation"
            ],
            "minimum_candidate_residual_maximum": min(
                row["residual_maximum_absolute_value"] for row in candidate_rows
            ),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "A208_sha256": sha256(A208),
            "selected_alignment_fibration_sha256": sha256(Y_FIBRATION),
            "dual_discriminant_sha256": sha256(DUAL),
            "orientation_sha256": sha256(ORIENTATION),
            "factorization_sha256": sha256(FACTORIZATION),
            "runner_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "same_source_beta_and_period_geometry_used": True,
            "moving_critical_values_used": True,
            "moving_thimble_periods_used": True,
            "moving_marked_fiber_basis_used_for_handles": True,
            "fixed_topological_braid_labels_continued_locally": True,
            "floating_probe_only": True,
            "finite_difference_Jacobian_assembled": False,
            "interval_neighborhood_certificate": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
