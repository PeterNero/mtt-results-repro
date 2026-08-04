from __future__ import annotations

import argparse
import json
import tempfile
import types
from pathlib import Path

import numpy as np
from flint import arb, ctx
from scipy.linalg import expm

import compute_q79genus2normalfunction as normal_function_module
from analyze_q79_picard_lefschetz_wall import complex_matrix, complex_value
from compute_q79genus2normalfunction import Q79DeltaNormalFunction
from explore_q79_pgl3_beta_zero import PGL3BetaEvaluator


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
A124 = DIRECTORY / "pgl3_transverse_simple_node_and_transport_pl_jump.packet.json"
WALL = DIRECTORY / "pgl3_transverse_simple_node.interval.packet.json"
SOURCE = DIRECTORY / "pgl3_projective_ychart_broyden_04.exploratory.json"
BASE_LIFT = DIRECTORY / "pgl3_selected_side_base_lift.interval.packet.json"
DEFAULT_OUTPUT = DIRECTORY / "pgl3_selected_side_contour_regularization.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def midpoint(value: dict) -> complex:
    real = (arb(value["real"]["lower"]) + arb(value["real"]["upper"])) / 2
    imaginary = (
        arb(value["imaginary"]["lower"])
        + arb(value["imaginary"]["upper"])
    ) / 2
    return complex(
        float(real.mid()),
        float(imaginary.mid()),
    )


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--rtol", type=float, default=2.0e-10)
    parser.add_argument("--atol", type=float, default=2.0e-12)
    arguments = parser.parse_args()
    ctx.dps = 70

    a124 = load(A124)
    wall = load(WALL)
    source = load(SOURCE)
    base_lift = load(BASE_LIFT)
    evaluator = PGL3BetaEvaluator()
    alignment_0 = complex_matrix(source["final_alignment"])
    direction = np.asarray(
        [complex_value(value) for value in a124["search_direction"]["coordinates"]]
    )
    tangent = sum(
        (
            direction[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    selected_carrier = float(wall["initial_box"][0]["lower"]) - 0.005
    alignment = alignment_0 @ expm(selected_carrier * tangent)
    initial_lift = np.asarray(
        [midpoint(value) for value in base_lift["y_chart_base_lift"]],
        dtype=np.complex128,
    )
    fibration = evaluator.fibration_packet(alignment, line_chart="y")
    original_fibration = normal_function_module.FIBRATION
    with tempfile.TemporaryDirectory(prefix="q79-selected-contour-") as directory:
        path = Path(directory) / "selected_fibration.json"
        path.write_text(json.dumps(fibration), encoding="utf-8")
        normal_function_module.FIBRATION = path
        try:
            engine = Q79DeltaNormalFunction()
        finally:
            normal_function_module.FIBRATION = original_fibration
    engine.gauss_manin.residue_rows = types.MethodType(
        lambda _self, periods, a_value, b_value: evaluator.residue_rows(
            alignment,
            periods,
            a_value,
            b_value,
            line_chart="y",
        ),
        engine.gauss_manin,
    )

    def execute(waypoints: list[complex]) -> tuple[np.ndarray, dict]:
        lift = initial_lift.copy()
        beta = np.zeros(8, dtype=np.complex128)
        evaluations = 0
        engine.maximum_reduction_condition_number = 0.0
        engine.maximum_equilibrated_condition_number = 0.0
        engine.high_precision_reduction_count = 0
        for left, right in zip(waypoints, waypoints[1:]):
            displacement = right - left
            lift, contribution, count = engine.execute_path(
                lift,
                lambda parameter, start=left, delta=displacement: (
                    engine.root_transport.base + 1j * (start + parameter * delta)
                ),
                lambda _parameter, delta=displacement: 1j * delta,
                rtol=arguments.rtol,
                atol=arguments.atol,
            )
            beta += contribution
            evaluations += count
        return beta, {
            "function_evaluations": evaluations,
            "maximum_raw_reduction_condition_number": (
                engine.maximum_reduction_condition_number
            ),
            "maximum_equilibrated_reduction_condition_number": (
                engine.maximum_equilibrated_condition_number
            ),
            "high_precision_reduction_count": engine.high_precision_reduction_count,
        }

    straight_waypoints = [0 + 0j, 1 + 0j]
    detour_waypoints = [
        0 + 0j,
        0.65 + 0j,
        0.65 - 0.1j,
        0.82 - 0.1j,
        0.82 + 0j,
        1 + 0j,
    ]
    full_lower_waypoints = [
        0 + 0j,
        0 - 0.1j,
        1 - 0.1j,
        1 + 0j,
    ]
    straight, straight_diagnostics = execute(straight_waypoints)
    detour, detour_diagnostics = execute(detour_waypoints)
    full_lower, full_lower_diagnostics = execute(full_lower_waypoints)
    maximum_difference = float(np.max(abs(straight - detour)))
    projective_overlap = float(
        abs(np.vdot(straight, detour))
        / (np.linalg.norm(straight) * np.linalg.norm(detour))
    )
    condition_reduction = (
        straight_diagnostics["maximum_equilibrated_reduction_condition_number"]
        / detour_diagnostics["maximum_equilibrated_reduction_condition_number"]
    )
    full_lower_difference = float(np.max(abs(straight - full_lower)))
    full_lower_overlap = float(
        abs(np.vdot(straight, full_lower))
        / (np.linalg.norm(straight) * np.linalg.norm(full_lower))
    )
    full_lower_condition_reduction = (
        straight_diagnostics["maximum_equilibrated_reduction_condition_number"]
        / full_lower_diagnostics["maximum_equilibrated_reduction_condition_number"]
    )
    if maximum_difference >= 5.0e-7 or projective_overlap <= 0.999999999999:
        raise AssertionError("lower contour does not reproduce the selected beta branch")

    packet = {
        "schema": "MTTQ79SelectedSideContourRegularizationDiagnostic.v1",
        "status": "FLOATING_SAME_BRANCH_LOWER_CONTOUR_EXECUTED_INTERVAL_TRANSPORT_OPEN",
        "selected_carrier": format(selected_carrier, ".17g"),
        "base_lift_source": str(BASE_LIFT.relative_to(ROOT)).replace("\\", "/"),
        "straight": {
            "waypoints": [complex_pair(value) for value in straight_waypoints],
            "beta": [complex_pair(value) for value in straight],
            "beta_norm": float(np.linalg.norm(straight)),
            **straight_diagnostics,
        },
        "lower_contour": {
            "waypoints": [complex_pair(value) for value in detour_waypoints],
            "beta": [complex_pair(value) for value in detour],
            "beta_norm": float(np.linalg.norm(detour)),
            **detour_diagnostics,
        },
        "full_lower_contour": {
            "waypoints": [
                complex_pair(value) for value in full_lower_waypoints
            ],
            "beta": [complex_pair(value) for value in full_lower],
            "beta_norm": float(np.linalg.norm(full_lower)),
            **full_lower_diagnostics,
        },
        "comparison": {
            "maximum_absolute_component_difference": maximum_difference,
            "projective_overlap": projective_overlap,
            "equilibrated_condition_number_reduction_factor": condition_reduction,
            "full_lower_maximum_absolute_component_difference": full_lower_difference,
            "full_lower_projective_overlap": full_lower_overlap,
            "full_lower_equilibrated_condition_number_reduction_factor": (
                full_lower_condition_reduction
            ),
        },
        "strict_scope": {
            "same_branch_contour_evidence_floating": True,
            "contour_homotopy_interval_certified": False,
            "endpoint_beta_interval_certified": False,
            "next_numerical_method": (
                "validated high-order Taylor-model Gauss-Manin transport on the "
                "lower contour, consuming the certified base-lift ball"
            ),
            "observed_SM_values_used": False,
        },
    }
    dump(arguments.output, packet)
    print(json.dumps(packet["comparison"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
