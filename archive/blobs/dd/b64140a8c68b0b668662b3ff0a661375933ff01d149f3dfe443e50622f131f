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
PACKET = VALIDATED / "n3.rank3.krawczyk.seed.a395.json"
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
A387 = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"
A394 = VALIDATED / "n3.rank3.residual.a394.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def upper(value: float) -> float:
    return math.nextafter(float(value), math.inf)


def positive_matvec_upper(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    result = np.zeros(matrix.shape[0], dtype=np.float64)
    for row in range(matrix.shape[0]):
        total = 0.0
        for column in range(matrix.shape[1]):
            total = upper(total + upper(matrix[row, column] * vector[column]))
        result[row] = total
    return result


def post_fixed_point_upper(constant: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    spectral_radius = float(np.max(abs(np.linalg.eigvals(matrix))))
    require(spectral_radius < 1.0, "A395 defect matrix is not contractive")
    candidate = np.nextafter(
        np.maximum(np.linalg.solve(np.eye(matrix.shape[0]) - matrix, constant), 0.0),
        math.inf,
    )
    for _ in range(128):
        image = np.nextafter(constant + positive_matvec_upper(matrix, candidate), math.inf)
        if bool(np.all(image <= candidate)):
            return candidate
        candidate = np.nextafter(np.maximum(candidate, image) * (1.0 + 1.0e-12), math.inf)
    raise AssertionError("A395 positive post-fixed point did not replay")


def scaled_point_radius(
    center_correction: np.ndarray,
    error_correction: np.ndarray,
    defect: np.ndarray,
    scale: float,
) -> np.ndarray:
    constant = np.nextafter(center_correction + scale * error_correction, math.inf)
    return post_fixed_point_upper(constant, defect)


def close_array(actual: np.ndarray, expected: np.ndarray, message: str) -> None:
    require(
        bool(np.allclose(actual, expected, rtol=2.0e-14, atol=1.0e-300)),
        message,
    )


def main() -> int:
    packet = load(PACKET)
    jacobian = load(A384)
    chart = load(A385S)
    old_seed = load(A387)
    residual = load(A394)
    require(packet["artifact"] == "A395", "A395 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourAugmentedBetaKrawczykFeasibilitySeed.v1",
        "A395 schema changed",
    )
    residual_centers = np.asarray(
        [complex_value(row["residual_interval_center"]) for row in residual["residue_rows"]],
        dtype=np.complex128,
    )
    residual_radii = np.asarray(
        [float(row["residual_component_radius_upper"]) for row in residual["residue_rows"]],
        dtype=np.float64,
    )
    floating = np.asarray(
        [complex_value(row["floating_residual_diagnostic_only"]) for row in residual["residue_rows"]],
        dtype=np.complex128,
    )
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    floating_correction = -(inverse @ floating)
    floating_bounds = np.nextafter(abs(floating_correction), math.inf)
    recentered_radii = np.nextafter(
        residual_radii + abs(residual_centers - floating), math.inf
    )
    correction_errors = positive_matvec_upper(abs(inverse), recentered_radii)
    defect = np.nextafter(
        np.asarray(
            jacobian["verified_interval_nonsingularity"][
                "componentwise_preconditioned_defect_upper_8_by_8"
            ],
            dtype=np.float64,
        ),
        math.inf,
    )
    nominal = scaled_point_radius(floating_bounds, correction_errors, defect, 0.0)
    rigorous = scaled_point_radius(floating_bounds, correction_errors, defect, 1.0)
    section = packet["minimal_point_Krawczyk_product_disks"]
    close_array(
        np.asarray(section["floating_seed_only_coordinate_radii"], dtype=np.float64),
        nominal,
        "A395 floating point radii do not replay",
    )
    close_array(
        np.asarray(section["full_A394_residual_interval_coordinate_radii"], dtype=np.float64),
        rigorous,
        "A395 rigorous point radii do not replay",
    )
    nominal_disk = float(np.max(nominal))
    rigorous_disk = float(np.max(rigorous))
    old_disk = float(
        old_seed["minimal_point_Krawczyk_product_disks"][
            "full_A386_maximum_complex_disk_radius"
        ]
    )
    scalar_replay = {
        "floating_seed_maximum_complex_disk_radius": nominal_disk,
        "full_A394_maximum_complex_disk_radius": rigorous_disk,
        "floating_seed_equivalent_real_imaginary_square_radius": nominal_disk
        / math.sqrt(2.0),
        "full_A394_equivalent_real_imaginary_square_radius": rigorous_disk
        / math.sqrt(2.0),
        "A387_full_A386_maximum_complex_disk_radius": old_disk,
        "A387_to_A395_required_disk_reduction_factor": old_disk / rigorous_disk,
    }
    for key, expected in scalar_replay.items():
        require(
            math.isclose(float(section[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A395 scalar does not replay {key}",
        )
    require(rigorous_disk < old_disk, "A395 does not improve A387")
    chart_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    require(len(chart_radii) == 1, "A395 chart radii changed")
    chart_disk = math.sqrt(2.0) * chart_radii.pop()
    chart_test = packet["selected_A385S_chart_test"]
    require(
        bool(chart_test["full_A394_point_Krawczyk_image_fits"])
        == (rigorous_disk <= chart_disk),
        "A395 selected chart decision does not replay",
    )
    close_array(
        np.asarray(packet["A394_rigorous_radii_recentered_on_floating_diagnostic"]),
        recentered_radii,
        "A395 recentered residual radii do not replay",
    )
    close_array(
        np.asarray(packet["A394_residual_uncertainty_correction_uppers"]),
        correction_errors,
        "A395 correction errors do not replay",
    )
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A395 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A395 authority {name}")
    scope = packet["strict_scope"]
    require(scope["A394_residual_uncertainty_propagated"], "A395 lost A394 uncertainty")
    require(scope["A384_point_Jacobian_defect_propagated"], "A395 lost A384 defect")
    require(scope["strictly_tighter_point_test_than_A387"], "A395 tightening gate is false")
    require(not scope["failure_of_sufficient_test_promoted_to_nonexistence"], "A395 promotes failure")
    require(not scope["Jacobian_polydisk_extension_closed"], "A395 overclaims a polydisk Jacobian")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A395 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A395 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A395 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A395")
    print(
        "PASS: A395 independently replays the A384/A394 point-Krawczyk scale "
        f"and improves A387 by {old_disk / rigorous_disk:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
