from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import explore_q79_height4_covariant_floating_probe as probe
from diagnose_q79_covariant_deformed_B_handle import execute_deformed_handle


ROOT = probe.ROOT
DIAGNOSTIC = (
    probe.PROBE_DIRECTORY
    / "deformed_B_handle_diagnostic"
    / "scale_1.000000"
    / "diagnostic.packet.json"
)
TRIAL = (
    probe.PROBE_DIRECTORY
    / "tr4_PL_unconstrained_deformedB_step01"
    / "trial.packet.json"
)
OUTPUT = probe.PROBE_DIRECTORY / "B_handle_wall_jump_analysis.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    diagnostic = load(DIAGNOSTIC)
    trial = load(TRIAL)
    directory = DIAGNOSTIC.parent
    y_path = directory / "fy.packet.json"
    marked_basis = probe.complex_matrix(diagnostic["moving_marked_basis"])
    factorization = load(probe.FACTORIZATION)
    action = np.asarray(factorization["handle_actions"]["B"], dtype=np.int64)
    expected_lift = int(load(probe.CENTRAL_LIFTS)["selected_lifts"]["B"])
    homology = load(probe.HOMOLOGY)["homology_convention"]
    base = 0.25 + 0.25j

    straight, straight_diagnostics = execute_deformed_handle(
        lambda parameter: base + 1j * parameter,
        lambda parameter: 1j,
        action,
        expected_lift,
        marked_basis,
        homology,
        y_path,
    )
    deformed = probe.complex_matrix(diagnostic["deformed_B_handle_integrals"])
    difference = deformed - straight
    period41 = probe.complex_vector(
        load(
            TRIAL.parent / "thimbles" / "t041.json"
        )["period_values"]
    )
    denominator = float(np.vdot(period41, period41).real)
    column_rows = []
    for column in range(4):
        value = difference[:, column]
        complex_coefficient = np.vdot(period41, value) / denominator
        integer_tests = []
        for coefficient in range(-4, 5):
            residual = value - coefficient * period41
            integer_tests.append(
                {
                    "coefficient": coefficient,
                    "residual_l2_norm": float(np.linalg.norm(residual)),
                }
            )
        ordered = sorted(integer_tests, key=lambda row: row["residual_l2_norm"])
        column_rows.append(
            {
                "column_zero_based": column,
                "complex_projection_coefficient": probe.complex_pair(
                    complex_coefficient
                ),
                "difference_l2_norm": float(np.linalg.norm(value)),
                "integer_tests": integer_tests,
                "best_integer_coefficient": ordered[0]["coefficient"],
                "best_integer_residual_l2_norm": ordered[0]["residual_l2_norm"],
            }
        )
    rank4 = next(
        row
        for row in load(probe.A208)["height_four_candidates"]
        if int(row["A132_objective_rank"]) == 4
    )
    B_coordinates = np.asarray(
        rank4["primitive_handle_coordinates"][4:], dtype=np.float64
    )
    contracted_difference = difference @ B_coordinates
    contracted_projection = np.vdot(period41, contracted_difference) / denominator
    packet = {
        "schema": "MTTQ79BHandleWallJumpAnalysis.v1",
        "status": "STRAIGHT_AND_DEFORMED_B_HANDLES_COMPARED",
        "straight_B_handle_integrals": probe.encoded_complex_matrix(straight),
        "deformed_B_handle_integrals": probe.encoded_complex_matrix(deformed),
        "deformed_minus_straight": probe.encoded_complex_matrix(difference),
        "straight_monodromy_diagnostics": straight_diagnostics,
        "deformed_monodromy_diagnostics": diagnostic["monodromy_diagnostics"],
        "P41_column_analysis": column_rows,
        "rank4_B_coordinates": [float(value) for value in B_coordinates],
        "rank4_contracted_difference": probe.encoded_complex_vector(
            contracted_difference
        ),
        "rank4_contracted_difference_l2_norm": float(
            np.linalg.norm(contracted_difference)
        ),
        "rank4_contracted_P41_projection": probe.complex_pair(
            contracted_projection
        ),
        "summary": {
            "straight_expected_lift_recovered": straight_diagnostics[
                "expected_lift_recovered"
            ],
            "straight_monodromy_scaled_residual": straight_diagnostics[
                "selected_lift_scaled_residual"
            ],
            "deformed_expected_lift_recovered": diagnostic["summary"][
                "expected_lift_recovered"
            ],
            "deformed_monodromy_scaled_residual": diagnostic["summary"][
                "monodromy_scaled_residual"
            ],
            "difference_matrix_l2_norm": float(np.linalg.norm(difference)),
            "rank4_contracted_difference_l2_norm": float(
                np.linalg.norm(contracted_difference)
            ),
        },
        "authority": {
            "deformed_diagnostic": relative(DIAGNOSTIC),
            "deformed_diagnostic_sha256": sha256(DIAGNOSTIC),
            "trial": relative(TRIAL),
            "trial_sha256": sha256(TRIAL),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "floating_handle_comparison": True,
            "interval_jump_certificate": False,
            "candidate_zero_proved": False,
        },
    }
    dump(OUTPUT, packet)
    print(f"wrote {relative(OUTPUT)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
