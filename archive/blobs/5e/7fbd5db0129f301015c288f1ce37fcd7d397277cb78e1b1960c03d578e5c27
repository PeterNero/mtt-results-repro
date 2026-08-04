from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.integrate import solve_ivp
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe


ROOT = probe.ROOT
JACOBIAN = probe.PROBE_DIRECTORY / "height4_covariant_PL_recentered_jacobian.packet.json"
BASE_TRIAL = probe.PROBE_DIRECTORY / "tr3_s1d000ep00" / "trial.packet.json"
OUTPUT_DIRECTORY = probe.PROBE_DIRECTORY / "deformed_B_handle_diagnostic"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=float, default=0.125)
    parser.add_argument("--margin", type=float, default=5.0e-5)
    parser.add_argument("--sigma", type=float, default=0.03)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def execute_deformed_handle(
    path,
    derivative,
    action: np.ndarray,
    expected_lift: int,
    initial_periods: np.ndarray,
    homology: dict,
    fibration: Path,
) -> tuple[np.ndarray, dict]:
    transport = probe.Q79SelectedAlignmentPeriodRootTransport(
        fibration, homology, omitted=probe.OMITTED, dps=80
    )
    gauss_manin = probe.Q79SelectedAlignmentGaussManin(
        fibration, transport, coordinate="t", omitted=probe.OMITTED
    )
    initial_state = np.concatenate(
        [
            initial_periods.reshape(-1),
            np.zeros((8, 4), dtype=np.complex128).reshape(-1),
        ]
    )

    def differential(parameter: float, state: np.ndarray) -> np.ndarray:
        periods = state[:20].reshape(5, 4)
        w_value = path(parameter)
        velocity = derivative(parameter)
        connection, a_value, b_value = gauss_manin.connection(w_value)
        period_derivative = velocity * connection @ periods
        integral_derivative = np.column_stack(
            [
                gauss_manin.period_length
                * velocity
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
        rtol=2.0e-10,
        atol=2.0e-13,
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
    return handle_integrals, {
        "selected_lift": selected_lift,
        "expected_lift": expected_lift,
        "positive_lift_scaled_residual": positive,
        "negative_lift_scaled_residual": negative,
        "selected_lift_scaled_residual": selected_error,
        "expected_lift_recovered": selected_lift == expected_lift,
        "production_gate_5e_7_passed": selected_error < 5.0e-7,
        "ODE_function_evaluations": solution.nfev,
        "maximum_reduction_relative_residual": (
            gauss_manin.maximum_reduction_relative_residual
        ),
    }


def main() -> int:
    arguments = parse_args()
    if not 0 < arguments.scale <= 1:
        raise ValueError("scale must lie in (0,1]")
    if arguments.margin <= 0 or arguments.sigma <= 0:
        raise ValueError("margin and sigma must be positive")
    ctx.dps = 100
    started = time.perf_counter()
    output = OUTPUT_DIRECTORY / f"scale_{arguments.scale:.6f}" / "diagnostic.packet.json"
    if output.exists() and not arguments.force:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    jacobian_packet = load(JACOBIAN)
    selected = next(
        row
        for row in jacobian_packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == 4
    )
    full_step = np.asarray(
        selected["local_least_squares_step_on_available_directions"],
        dtype=np.float64,
    )
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (full_step[index] * evaluator.generators[index] for index in range(8)),
        np.zeros((3, 3), dtype=np.complex128),
    )
    base_alignment = probe.complex_matrix(load(BASE_TRIAL)["alignment"])
    alignment = base_alignment @ expm(arguments.scale * tangent)
    directory = output.parent
    y_path = directory / "fy.packet.json"
    z_path = directory / "fz.packet.json"
    dump(y_path, probe.build_point_fibration(alignment, "y"))
    dump(z_path, probe.build_point_fibration(alignment, "z"))
    centers, critical_diagnostics = probe.continued_critical_centers(alignment)

    orientation = load(probe.ORIENTATION)
    pivots = [
        int(value) for value in orientation["unimodular_pivot_indices_one_based"]
    ]
    fan_by_index = {
        int(row["distinguished_index"]): row
        for row in load(probe.FAN)["distinguished_positive_meridians"]
    }
    pivot_rows = {}
    for index in pivots:
        fan_row = fan_by_index[index]
        task = {
            "distinguished_index": index,
            "root_id": fan_row["root_id"],
            "central_packet_path": str(
                probe.central_period_path(index, fan_row["root_id"])
            ),
            "critical_center": [
                centers[fan_row["root_id"]].real,
                centers[fan_row["root_id"]].imag,
            ],
            "y_fibration": str(y_path),
            "z_fibration": str(z_path),
        }
        pivot_rows[index] = probe.thimble_worker(task)

    factorization = load(probe.FACTORIZATION)
    vectors = np.asarray(
        [
            row["positive_vanishing_cycle_up_to_sign"]
            for row in factorization["factors"]
        ],
        dtype=np.int64,
    ).T
    pivot_zero = np.asarray([value - 1 for value in pivots], dtype=np.int64)
    homology = load(probe.HOMOLOGY)["homology_convention"]
    y_to_z = probe.moving_y_to_z_transition(y_path, alignment, homology)
    pivot_columns = []
    for index in pivots:
        row = pivot_rows[index]
        values = probe.complex_vector(row["base_fiber_propagated_periods"])
        if row["line_chart"] == "z":
            values = np.linalg.solve(y_to_z, values)
        pivot_columns.append(values)
    pivot_periods = np.column_stack(pivot_columns)
    pivot_signs = np.asarray(orientation["pivot_signs"], dtype=np.int64)
    marked_basis = (pivot_periods * pivot_signs[np.newaxis, :]) @ np.linalg.inv(
        vectors[:, pivot_zero]
    )

    base = 0.25 + 0.25j
    selected_090 = centers["selected_090"]
    dx = float((selected_090.real - 0.25) - round(selected_090.real - 0.25))
    t0 = float((selected_090.imag - 0.25) % 1.0)
    amplitude = max(0.0, dx) + arguments.margin
    normalization = math.sin(math.pi * t0) ** 2

    def bump(parameter: float) -> float:
        sine = math.sin(math.pi * parameter)
        gaussian = math.exp(-((parameter - t0) / arguments.sigma) ** 2)
        return amplitude * sine**2 * gaussian / normalization

    def bump_derivative(parameter: float) -> float:
        sine = math.sin(math.pi * parameter)
        cosine = math.cos(math.pi * parameter)
        gaussian = math.exp(-((parameter - t0) / arguments.sigma) ** 2)
        return amplitude / normalization * gaussian * (
            2 * math.pi * sine * cosine
            - 2 * (parameter - t0) / arguments.sigma**2 * sine**2
        )

    def path(parameter: float) -> complex:
        return base + 1j * parameter + bump(parameter)

    def derivative(parameter: float) -> complex:
        return 1j + bump_derivative(parameter)

    enclosed = []
    for root_id, center in centers.items():
        root_dx = float((center.real - 0.25) - round(center.real - 0.25))
        root_t = float((center.imag - 0.25) % 1.0)
        path_dx = bump(root_t)
        if 0 < root_dx < path_dx:
            enclosed.append(
                {
                    "root_id": root_id,
                    "signed_x_from_straight_path": root_dx,
                    "deformed_path_x_at_root_height": path_dx,
                    "height_parameter": root_t,
                }
            )
    if [row["root_id"] for row in enclosed] != ["selected_090"]:
        raise AssertionError(f"deformed B homotopy strip inventory changed: {enclosed}")
    grid = np.linspace(0.0, 1.0, 4001)
    path_values = np.asarray([path(float(value)) for value in grid])
    minimum_clearance = float("inf")
    nearest_root = None
    for root_id, center in centers.items():
        differences = path_values - center
        differences = (
            differences.real - np.round(differences.real)
        ) + 1j * (differences.imag - np.round(differences.imag))
        clearance = float(np.min(abs(differences)))
        if clearance < minimum_clearance:
            minimum_clearance = clearance
            nearest_root = root_id

    action = np.asarray(factorization["handle_actions"]["B"], dtype=np.int64)
    expected_lift = int(load(probe.CENTRAL_LIFTS)["selected_lifts"]["B"])
    integrals, diagnostics = execute_deformed_handle(
        path,
        derivative,
        action,
        expected_lift,
        marked_basis,
        homology,
        y_path,
    )
    packet = {
        "schema": "MTTQ79CovariantDeformedBHandleDiagnostic.v1",
        "status": "DEFORMED_B_HANDLE_EXECUTED",
        "rank4_unconstrained_scale": arguments.scale,
        "alignment": probe.encoded_complex_matrix(alignment),
        "critical_continuation": critical_diagnostics,
        "path": {
            "model": "localized positive horizontal Gaussian-sine detour",
            "selected_090_signed_x_from_straight_path": dx,
            "selected_090_height_parameter": t0,
            "margin": arguments.margin,
            "sigma": arguments.sigma,
            "amplitude": amplitude,
            "homotopy_strip_inventory": enclosed,
            "sampled_minimum_critical_clearance": minimum_clearance,
            "sampled_nearest_root_id": nearest_root,
        },
        "moving_marked_basis": probe.encoded_complex_matrix(marked_basis),
        "deformed_B_handle_integrals": probe.encoded_complex_matrix(integrals),
        "monodromy_diagnostics": diagnostics,
        "summary": {
            "rank4_unconstrained_scale": arguments.scale,
            "homotopy_strip_root_count": len(enclosed),
            "homotopy_strip_root_ids": [row["root_id"] for row in enclosed],
            "sampled_minimum_critical_clearance": minimum_clearance,
            "sampled_nearest_root_id": nearest_root,
            "expected_lift_recovered": diagnostics["expected_lift_recovered"],
            "monodromy_scaled_residual": diagnostics[
                "selected_lift_scaled_residual"
            ],
            "production_gate_5e_7_passed": diagnostics[
                "production_gate_5e_7_passed"
            ],
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "base_trial": relative(BASE_TRIAL),
            "base_trial_sha256": sha256(BASE_TRIAL),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "single_global_handle_diagnostic": True,
            "selected_090_only_in_homotopy_strip": True,
            "deformed_path_floating_execution": True,
            "interval_path_certificate": False,
            "full_candidate_residual_executed": False,
            "covariant_zero_proved": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
