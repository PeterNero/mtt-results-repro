from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentGaussManin,
    Q79SelectedAlignmentPeriodRootTransport,
)
from q79genus2_period_transport import FORM_NAMES


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
HANDLE_DIRECTORY = DIRECTORY / "selected_alignment_handle_monodromy"
HANDLE_ATLAS = DIRECTORY / "selected_alignment_handle_period_atlas.packet.json"
CENTRAL_LIFTS = DIRECTORY / "selected_alignment_handle_central_lifts.interval.packet.json"
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
ORIENTATION = (
    DIRECTORY
    / "selected_alignment_thimble_periods"
    / "selected_alignment_thimble_orientation_synchronization.packet.json"
)
IDENTITY_ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
SELECTED_ADAPTER = ROOT / "scripts" / "q79_selected_alignment_period_transport.py"
OUTPUT_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
DEFAULT_OUTPUT = OUTPUT_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
OMITTED = 2 + 3j


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def complex_matrix(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [
        [
            complex_pair(complex(matrix[row, column]))
            for column in range(matrix.shape[1])
        ]
        for row in range(matrix.shape[0])
    ]


def marked_base_periods() -> tuple[np.ndarray, dict]:
    packet = load(ORIENTATION)
    basis = np.asarray(
        [
            [
                complex(float(value["real"]), float(value["imaginary"]))
                for value in row
            ]
            for row in packet["marked_base_period_matrix"]
        ],
        dtype=np.complex128,
    )
    if basis.shape != (5, 4):
        raise AssertionError("selected synchronized marking shape")
    return basis, {
        "basis": ["a1", "b1", "a2", "b2"],
        "line_chart": "y",
        "source": "selected 90-thimble/A130 orientation synchronization",
        "orientation_packet_sha256": sha256(ORIENTATION),
        **packet["checks"],
    }


def execute_handle(
    name: str,
    displacement: complex,
    action: np.ndarray,
    expected_lift: int,
    initial_periods: np.ndarray,
    homology: dict,
    *,
    dps: int,
    rtol: float,
    atol: float,
) -> tuple[np.ndarray, dict]:
    transport = Q79SelectedAlignmentPeriodRootTransport(
        FIBRATION, homology, omitted=OMITTED, dps=dps
    )
    gauss_manin = Q79SelectedAlignmentGaussManin(
        FIBRATION,
        transport,
        coordinate="t",
        omitted=OMITTED,
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
                * gauss_manin.residue_rows(
                    periods[:, column], a_value, b_value
                )
                for column in range(4)
            ]
        )
        return np.concatenate(
            [
                period_derivative.reshape(-1),
                integral_derivative.reshape(-1),
            ]
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
    endpoint_periods = solution.y[:20, -1].reshape(5, 4)
    handle_integrals = solution.y[20:, -1].reshape(8, 4)
    initial_holomorphic = initial_periods[:2, :]
    endpoint_holomorphic = endpoint_periods[:2, :]
    predicted = initial_holomorphic @ action
    positive_error = float(
        np.linalg.norm(endpoint_holomorphic - predicted)
        / max(np.linalg.norm(endpoint_holomorphic), np.linalg.norm(predicted))
    )
    negative_error = float(
        np.linalg.norm(endpoint_holomorphic + predicted)
        / max(np.linalg.norm(endpoint_holomorphic), np.linalg.norm(predicted))
    )
    period_selected_lift = 1 if positive_error <= negative_error else -1
    selected_error = min(positive_error, negative_error)
    if period_selected_lift != expected_lift:
        raise AssertionError(f"selected handle {name} central-lift disagreement")
    if selected_error >= 5.0e-7:
        raise AssertionError(f"selected handle {name} endpoint residual")
    return handle_integrals, {
        "name": name,
        "base_path": (
            "w(s)=(1+i)/4+s"
            if name == "A"
            else "w(s)=(1+i)/4+i*s"
        ),
        "line_chart": "y",
        "primitive_fiber_cycle_order": ["a1", "b1", "a2", "b2"],
        "period_values": complex_matrix(handle_integrals),
        "endpoint_holomorphic_periods": complex_matrix(
            endpoint_holomorphic
        ),
        "promoted_braid_action": action.astype(int).tolist(),
        "interval_selected_central_lift": expected_lift,
        "independent_period_continuation_lift": period_selected_lift,
        "selected_action": (expected_lift * action).astype(int).tolist(),
        "positive_lift_scaled_residual": format(positive_error, ".17g"),
        "negative_lift_scaled_residual": format(negative_error, ".17g"),
        "selected_lift_scaled_residual": format(selected_error, ".17g"),
        "numerics": {
            "working_decimal_digits": dps,
            "ODE_method": "DOP853",
            "ODE_rtol": format(rtol, ".17g"),
            "ODE_atol": format(atol, ".17g"),
            "ODE_function_evaluations": solution.nfev,
            "Gauss_Manin_coordinate": "t",
            "Gauss_Manin_connection_evaluations": (
                gauss_manin.connection_evaluation_count
            ),
            "high_precision_Gauss_Manin_connection_evaluations": (
                gauss_manin.high_precision_connection_evaluation_count
            ),
            "maximum_reduction_condition_number": format(
                gauss_manin.maximum_reduction_condition_number, ".17g"
            ),
            "maximum_equilibrated_reduction_condition_number": format(
                gauss_manin.maximum_equilibrated_reduction_condition_number,
                ".17g",
            ),
            "maximum_reduction_relative_residual": format(
                gauss_manin.maximum_reduction_relative_residual, ".17g"
            ),
            "maximum_high_precision_solution_radius": format(
                gauss_manin.maximum_high_precision_solution_radius, ".17g"
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inner-order", type=int, default=384)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-13)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-save", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    started = time.perf_counter()
    factorization = load(FACTORIZATION)
    homology = load(HOMOLOGY)["homology_convention"]
    atlas = load(HANDLE_ATLAS)
    if any(row["selected_line_chart"] != "y" for row in atlas["rows"]):
        raise AssertionError("selected handle period atlas changed")
    central_lifts = {
        name: int(value)
        for name, value in load(CENTRAL_LIFTS)["selected_lifts"].items()
    }
    initial_periods, marking = marked_base_periods()
    actions = {
        name: np.asarray(
            factorization["handle_actions"][name], dtype=np.int64
        )
        for name in ("A", "B")
    }
    handle_rows = []
    handle_blocks = []
    for name, displacement in (("A", 1 + 0j), ("B", 1j)):
        block, row = execute_handle(
            name,
            displacement,
            actions[name],
            central_lifts[name],
            initial_periods,
            homology,
            dps=arguments.dps,
            rtol=arguments.rtol,
            atol=arguments.atol,
        )
        handle_blocks.append(block)
        handle_rows.append(row)
    primitive = np.hstack(handle_blocks)
    handle_packet_paths = {
        name: HANDLE_DIRECTORY / f"handle_{name}.packet.json"
        for name in ("A", "B")
    }
    payload = {
        "schema": "MTTQ79SelectedAlignmentPrimitiveHandlePeriods.v1",
        "status": "SELECTED_ALIGNMENT_EIGHT_PRIMITIVE_HANDLE_PERIOD_COLUMNS_COMPUTED",
        "authority": {
            "selected_y_fibration_sha256": sha256(FIBRATION),
            "selected_global_factorization_sha256": sha256(FACTORIZATION),
            "selected_handle_period_atlas_sha256": sha256(HANDLE_ATLAS),
            "selected_interval_central_lifts_sha256": sha256(CENTRAL_LIFTS),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "selected_thimble_orientation_sha256": sha256(ORIENTATION),
            "handle_A_packet_sha256": sha256(handle_packet_paths["A"]),
            "handle_B_packet_sha256": sha256(handle_packet_paths["B"]),
            "handle_trajectory_sha256": {
                name: load(path)["trajectory"]["sha256"]
                for name, path in handle_packet_paths.items()
            },
            "unchanged_identity_period_engine_sha256": sha256(
                IDENTITY_ENGINE
            ),
            "selected_period_adapter_sha256": sha256(SELECTED_ADAPTER),
            "runner_sha256": sha256(Path(__file__).resolve()),
        },
        "marking": marking,
        "forms": FORM_NAMES,
        "primitive_column_order": [
            "A:a1",
            "A:b1",
            "A:a2",
            "A:b2",
            "B:a1",
            "B:b1",
            "B:a2",
            "B:b2",
        ],
        "primitive_handle_period_matrix": complex_matrix(primitive),
        "handles": handle_rows,
        "central_lift_result": {
            "interval_selected_lifts": central_lifts,
            "independent_period_continuation_agrees": True,
            "period_values_used_to_select_lifts": False,
        },
        "execution": {
            "inner_Gauss_Legendre_order": arguments.inner_order,
            "working_decimal_digits": arguments.dps,
            "ODE_rtol": format(arguments.rtol, ".17g"),
            "ODE_atol": format(arguments.atol, ".17g"),
            "elapsed_seconds": format(
                time.perf_counter() - started, ".17g"
            ),
        },
        "strict_scope": {
            "same_selected_carrier_as_A127_beta": True,
            "primitive_handle_cylinders_executed": 8,
            "A123_alignment_dependent_residue_rows_used": True,
            "A129_selected_handle_actions_used": True,
            "A130_interval_central_lifts_used": True,
            "floating_convergence_only": True,
            "interval_period_enclosure": False,
            "rank_92_period_table_assembled": False,
            "observed_SM_values_used": False,
        },
    }
    if not arguments.no_save:
        output = arguments.output
        if not output.is_absolute():
            output = ROOT / output
        dump(output, payload)
        print(f"wrote {output.relative_to(ROOT)}")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
