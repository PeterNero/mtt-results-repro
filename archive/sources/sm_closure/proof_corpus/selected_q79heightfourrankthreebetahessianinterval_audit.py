from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.beta_hessian.interval.json"
)


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
    require(
        packet["schema"] == "MTTQ79HeightFourRank3BetaHessianInterval.v1",
        "A379 schema changed",
    )
    require(
        packet["status"]
        == "N3_RANK3_ANCHORED_BETA_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "A379 status weakened",
    )
    require(packet["artifact"] == "A379", "A379 artifact changed")

    rows = packet["beta_rows"]
    matrix = packet["complex_beta_Hessian_8_by_8"]
    require(len(rows) == 8, "A379 beta row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        "A379 Hessian is not 8 by 8",
    )
    require(
        all(row["A376_intervals_overlap"] for row in rows),
        "A379 ordinary beta rows no longer overlap A376",
    )
    beta_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in rows],
        dtype=np.float64,
    )
    centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in matrix],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in matrix],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(beta_radii))), "A379 has a nonfinite beta radius")
    require(bool(np.all(np.isfinite(centers))), "A379 has a nonfinite center")
    require(bool(np.all(np.isfinite(radii))), "A379 has a nonfinite Hessian radius")
    require(bool(np.all(beta_radii >= 0.0)), "A379 has a negative beta radius")
    require(bool(np.all(radii >= 0.0)), "A379 has a negative Hessian radius")

    summary = packet["summary"]
    require(int(summary["certified_beta_rows"]) == 8, "A379 beta row gate changed")
    require(int(summary["certified_Hessian_entries"]) == 64, "A379 lost 64 entries")
    require(
        math.isclose(
            float(summary["maximum_beta_component_radius_upper"]),
            float(np.max(beta_radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A379 maximum beta radius does not replay",
    )
    require(
        math.isclose(
            float(summary["maximum_Hessian_component_radius_upper"]),
            float(np.max(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A379 maximum Hessian radius does not replay",
    )
    require(
        math.isclose(
            float(summary["Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A379 Frobenius radius does not replay",
    )
    require(
        math.isclose(
            float(summary["Hessian_center_Frobenius_norm"]),
            float(np.linalg.norm(centers)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A379 center norm does not replay",
    )
    require(
        summary["all_A376_beta_intervals_overlap"] is True,
        "A379 A376 overlap summary failed",
    )

    execution = packet["execution"]
    waypoints = [complex_value(value) for value in execution["waypoints"]]
    require(len(waypoints) == 6, "A379 waypoint count changed")
    steps = execution["steps"]
    require(len(steps) == int(summary["accepted_step_count"]), "A379 step count changed")
    require(len(steps) > 0, "A379 has no certified steps")
    segment_positions = [0.0 for _ in range(len(waypoints) - 1)]
    for step in steps:
        segment = int(step["segment_index"])
        require(0 <= segment < len(segment_positions), "A379 segment index is invalid")
        width = float(step["step"])
        position = float(step["position"])
        require(width > 0.0, "A379 has a nonpositive step")
        require(
            math.isclose(
                position - segment_positions[segment],
                width,
                rel_tol=2.0e-13,
                abs_tol=2.0e-15,
            ),
            "A379 path cover has a gap",
        )
        require(
            0.0 < position <= abs(waypoints[segment + 1] - waypoints[segment]) + 2.0e-15,
            "A379 step leaves its waypoint segment",
        )
        for key in (
            "maximum_reduction_neumann_norm",
            "fundamental_inverse_neumann_norm",
        ):
            require(0.0 <= float(step[key]) < 1.0, f"A379 lost {key}")
        segment_positions[segment] = position
    for index, position in enumerate(segment_positions):
        require(
            math.isclose(
                position,
                abs(waypoints[index + 1] - waypoints[index]),
                rel_tol=2.0e-14,
                abs_tol=2.0e-15,
            ),
            f"A379 does not cover waypoint segment {index}",
        )

    checkpoint = ROOT / execution["checkpoint"]
    require(checkpoint.exists(), "A379 checkpoint is absent")
    require(
        sha256(checkpoint) == execution["checkpoint_sha256"],
        "A379 checkpoint authority changed",
    )
    smoke = packet["smoke_test"]
    require(
        int(smoke["derived_hessian_row_count"]) == 64,
        "A379 smoke test lost the 64 differentiated rows",
    )
    require(
        float(smoke["maximum_original_beta_system_coefficient_difference"])
        < 1.0e-35,
        "A379 no longer replays the ordinary beta transport system",
    )
    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A379 authority path absent: {label}")
        require(sha256(path) == authority["sha256"], f"A379 authority stale: {label}")

    scope = packet["strict_scope"]
    for key in (
        "same_source_beta_and_Hessian_integrands_used",
        "A378_affine_Hessian_source_consumed",
        "A376_beta_rows_independently_replayed",
        "rank3_anchored_beta_Hessian_interval_closed",
    ):
        require(scope[key] is True, f"A379 strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered A379")
    require(scope["interval_Newton_existence_and_uniqueness_closed"] is False, "A379 overclaims interval Newton")
    require(scope["full_SM_closure_proved"] is False, "A379 overclaims full SM closure")
    print("PASS: A379 certifies all 8 beta rows and 64 same-source Hessian entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
