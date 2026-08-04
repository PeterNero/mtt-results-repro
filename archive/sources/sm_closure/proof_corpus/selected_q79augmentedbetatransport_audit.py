from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.beta.augmented.a392.json"
A379 = VALIDATED / "n3.beta_hessian.interval.json"
EXPECTED_WAYPOINTS = [
    0 + 0j,
    0.65 + 0j,
    0.65 - 0.1j,
    0.82 - 0.1j,
    0.82 + 0j,
    1 + 0j,
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    packet = load(PACKET)
    reference = load(A379)
    require(packet["artifact"] == "A392", "A392 artifact changed")
    require(
        packet["schema"] == "MTTQ79AugmentedBetaTransportInterval.v1",
        "A392 schema changed",
    )
    require(
        packet["status"] == "N3_AUGMENTED_13_STATE_BETA_INTERVAL_EXECUTED",
        "A392 status changed",
    )
    waypoints = [complex_value(value) for value in packet["method"]["waypoints"]]
    require(waypoints == EXPECTED_WAYPOINTS, "A392 route changed")

    endpoint = packet["endpoint"]
    centers = np.asarray(
        [complex_value(value) for value in endpoint["beta_center"]],
        dtype=np.complex128,
    )
    radii = np.asarray(endpoint["component_radius_uppers"], dtype=np.float64)
    uniform = float(endpoint["uniform_component_radius_upper"])
    require(centers.shape == (8,), "A392 beta center count changed")
    require(radii.shape == (8,), "A392 component radius count changed")
    require(bool(np.all(np.isfinite(centers))), "A392 center is nonfinite")
    require(bool(np.all(np.isfinite(radii))), "A392 radius is nonfinite")
    require(bool(np.all(radii >= 0.0)), "A392 has a negative radius")
    require(
        math.isclose(float(np.max(radii)), uniform, rel_tol=3.0e-14, abs_tol=1.0e-300),
        "A392 uniform radius does not replay its component rows",
    )

    reference_centers = np.asarray(
        [complex_value(row["interval_center"]) for row in reference["beta_rows"]],
        dtype=np.complex128,
    )
    reference_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in reference["beta_rows"]],
        dtype=np.float64,
    )
    require(
        bool(np.all(np.abs(centers - reference_centers) <= radii + reference_radii)),
        "A392 endpoint balls miss A379",
    )

    execution = packet["execution"]
    steps = execution["steps"]
    require(len(steps) == int(execution["accepted_step_count"]), "step count changed")
    require(len(steps) > 0, "A392 has no validated steps")
    positions = [0.0] * (len(EXPECTED_WAYPOINTS) - 1)
    for step in steps:
        segment = int(step["segment_index"])
        require(0 <= segment < len(positions), "A392 segment index invalid")
        start = complex_value(step["start"])
        end = complex_value(step["end"])
        width = float(step["step"])
        require(width > 0.0 and abs(end - start) > 0.0, "A392 has a null step")
        expected_start = EXPECTED_WAYPOINTS[segment] + (
            EXPECTED_WAYPOINTS[segment + 1] - EXPECTED_WAYPOINTS[segment]
        ) * (positions[segment] / abs(EXPECTED_WAYPOINTS[segment + 1] - EXPECTED_WAYPOINTS[segment]))
        require(abs(start - expected_start) < 3.0e-14, "A392 path cover has a gap")
        positions[segment] += width
        require(int(step["augmented_state_dimension"]) == 13, "A392 lost dimension 13")
        require(step["full_affine_error_frame_used"] is True, "A392 lost its affine frame")
        require(step["all_returned_bounds_finite"] is True, "A392 step lost finiteness")
        require(len(step["beta_component_radius_uppers"]) == 8, "A392 step lost beta rows")
        for key in ("reduction_neumann_norm", "fundamental_inverse_neumann_norm"):
            require(0.0 <= float(step[key]) < 1.0, f"A392 lost {key}")
    for index, position in enumerate(positions):
        require(
            math.isclose(
                position,
                abs(EXPECTED_WAYPOINTS[index + 1] - EXPECTED_WAYPOINTS[index]),
                rel_tol=3.0e-13,
                abs_tol=3.0e-14,
            ),
            f"A392 does not cover segment {index}",
        )

    configuration = packet["execution_configuration"]
    checkpoint_path = ROOT / configuration["checkpoint"]
    require(checkpoint_path.exists(), "A392 checkpoint is absent")
    require(
        sha256(checkpoint_path) == configuration["checkpoint_sha256"],
        "A392 checkpoint authority changed",
    )
    checkpoint = load(checkpoint_path)
    require(checkpoint["path_name"] == configuration["path_name"], "checkpoint path identity changed")
    require(int(checkpoint["order"]) == int(configuration["order"]), "checkpoint order changed")
    require(len(checkpoint["coordinate_radii"]) == 13, "checkpoint lost augmented frame")
    require(len(checkpoint["lift_fundamental"]) == 13, "checkpoint fundamental is not 13 dimensional")
    for label, record in packet["authority"].items():
        path = ROOT / record["path"]
        require(path.exists(), f"A392 authority absent: {label}")
        require(sha256(path) == record["sha256"], f"A392 authority stale: {label}")

    comparison = packet["comparison_to_A379"]
    old_maximum = float(reference["summary"]["maximum_beta_component_radius_upper"])
    factor = old_maximum / uniform
    require(math.isclose(float(comparison["radius_tightening_factor"]), factor, rel_tol=2.0e-15), "A392 factor does not replay")
    tighter = uniform < old_maximum
    require(comparison["strictly_tighter_than_A379"] is tighter, "comparison decision changed")
    scope = packet["strict_scope"]
    for key in (
        "same_A379_selected_route_used",
        "same_selected_beta_differential_system_used",
        "full_13_state_affine_error_frame_used",
        "eight_component_beta_radii_emitted",
    ):
        require(scope[key] is True, f"A392 scope lost {key}")
    require(scope["strictly_tighter_than_A379"] is tighter, "scope tightening decision changed")
    for key in (
        "observed_SM_values_used",
        "coupled_beta_period_residual_transport_closed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A392 overclaims {key}")
    print("PASS: A392 replays the 13-state affine beta transport")
    print(f"beta-radius tightening factor over A379: {factor:.12g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
