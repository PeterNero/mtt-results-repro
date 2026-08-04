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
PACKET = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = load(PACKET)
    jacobian = load(A384)
    chart = load(A385S)
    residual = load(A386)
    require(packet["artifact"] == "A387", "A387 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourKrawczykFeasibilitySeed.v1",
        "A387 schema changed",
    )
    centers = np.asarray(
        [complex_value(row["residual_interval_center"]) for row in residual["residue_rows"]],
        dtype=np.complex128,
    )
    radii = np.asarray(
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
    expected_midpoint_correction = -(inverse @ centers)
    actual_midpoint_correction = np.asarray(
        [
            complex_value(value)
            for value in packet[
                "interval_box_midpoint_preconditioned_correction_diagnostic"
            ]
        ],
        dtype=np.complex128,
    )
    require(
        float(np.max(abs(actual_midpoint_correction - expected_midpoint_correction)))
        < 2.0e-18,
        "A387 midpoint correction does not replay",
    )
    expected_floating_correction = -(inverse @ floating)
    actual_floating_correction = np.asarray(
        [complex_value(value) for value in packet["floating_residual_newton_seed"]],
        dtype=np.complex128,
    )
    require(
        float(np.max(abs(actual_floating_correction - expected_floating_correction)))
        < 2.0e-18,
        "A387 floating Newton seed does not replay",
    )
    recentered_radii = np.asarray(
        packet["A386_rigorous_radii_recentered_on_floating_diagnostic"],
        dtype=np.float64,
    )
    require(
        bool(np.all(recentered_radii >= radii + abs(centers - floating))),
        "A387 recentered residual radii are not outward",
    )
    expected_error = abs(inverse) @ recentered_radii
    actual_error = np.asarray(
        packet["A386_residual_uncertainty_correction_uppers"], dtype=np.float64
    )
    require(
        bool(np.all(actual_error >= expected_error))
        and bool(np.allclose(actual_error, expected_error, rtol=3.0e-15, atol=1.0e-300)),
        "A387 residual uncertainty propagation changed",
    )
    defect = np.asarray(
        packet["point_preconditioned_defect"]["componentwise_upper_8_by_8"],
        dtype=np.float64,
    )
    source_defect = np.asarray(
        jacobian["verified_interval_nonsingularity"][
            "componentwise_preconditioned_defect_upper_8_by_8"
        ],
        dtype=np.float64,
    )
    require(bool(np.all(defect >= source_defect)), "A387 defect is not outward")
    require(float(np.max(abs(defect - source_defect))) < 2.0e-16, "A387 defect changed")
    nominal = np.asarray(
        packet["minimal_point_Krawczyk_product_disks"][
            "floating_seed_only_coordinate_radii"
        ],
        dtype=np.float64,
    )
    full = np.asarray(
        packet["minimal_point_Krawczyk_product_disks"][
            "full_A386_residual_interval_coordinate_radii"
        ],
        dtype=np.float64,
    )
    center_bound = np.asarray(packet["floating_newton_seed_absolute_uppers"])
    require(bool(np.all(center_bound + defect @ nominal <= nominal * (1.0 + 2.0e-12))), "nominal A387 radii are not post-fixed")
    require(bool(np.all(center_bound + actual_error + defect @ full <= full * (1.0 + 2.0e-12))), "full A387 radii are not post-fixed")
    selected_square = float(
        chart["charts"][0]["coordinate_complex_box"]["real_radius_requested"]
    )
    selected_disk = math.sqrt(2.0) * selected_square
    selected = packet["selected_A385S_chart_test"]
    require(
        math.isclose(float(selected["enclosing_complex_disk_radius"]), selected_disk, rel_tol=2.0e-15),
        "A387 selected chart radius changed",
    )
    require(
        bool(selected["floating_seed_point_Krawczyk_image_fits"])
        == (float(np.max(nominal)) <= selected_disk),
        "A387 floating-seed chart gate changed",
    )
    require(
        bool(selected["full_A386_point_Krawczyk_image_fits"]) == (float(np.max(full)) <= selected_disk),
        "A387 full chart gate changed",
    )
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A387 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A387 authority {name}")
    scope = packet["strict_scope"]
    require(scope["floating_residual_Newton_seed_computed"], "A387 lost floating seed")
    require(scope["interval_box_midpoint_not_treated_as_true_residual"], "A387 confuses midpoint and residual")
    require(scope["A386_residual_uncertainty_propagated"], "A387 lost residual uncertainty")
    require(not scope["failure_of_sufficient_test_promoted_to_nonexistence"], "A387 overclaims nonexistence")
    require(not scope["Jacobian_polydisk_extension_closed"], "A387 overclaims a Jacobian polydisk")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A387 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A387 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A387 overclaims SM closure")
    print(
        "PASS: A387 independently separates the A386 floating Newton seed from "
        "the rigorous interval midpoint and replays the "
        "point-Krawczyk scale diagnostic"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
