from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.pgl3.polydisk_chart_source.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_authorities(packet: dict, label: str) -> None:
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.is_file(), f"{label} authority absent: {name}")
        require(sha256(path) == row["sha256"], f"{label} authority stale: {name}")


def matrix_maximum_radius(matrix: list[list[dict]]) -> float:
    require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), "matrix is not 3 by 3")
    return max(float(entry["complex_radius_upper"]) for row in matrix for entry in row)


def main() -> int:
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourPGL3PolydiskChartSource.v1",
        "A385S schema changed",
    )
    require(
        packet["status"]
        == "PGL3_COMPLEX_BOX_CHART_AND_ALL_EIGHT_FRECHET_DERIVATIVES_CERTIFIED",
        "A385S status weakened",
    )
    require(packet["artifact"] == "A385S", "A385S artifact changed")
    require(
        packet["chart_definition"] == "A(z)=A_n3*exp(Z), Z=sum_{s=1}^8 z_s G_s",
        "A385S chart changed",
    )
    charts = packet["charts"]
    require([row["line_chart"] for row in charts] == ["y", "z"], "A385S chart inventory changed")
    determinant_lowers = []
    derivative_radii = []
    frame_radii = []
    replay_bounds = []
    for chart in charts:
        box = chart["coordinate_complex_box"]
        require(int(box["coordinate_count"]) == 8, "A385S coordinate count changed")
        require(float(box["real_radius_requested"]) > 0.0, "A385S real radius is nonpositive")
        require(float(box["imaginary_radius_requested"]) > 0.0, "A385S imaginary radius is nonpositive")
        determinant_lower = float(chart["alignment_determinant_absolute_lower"])
        require(math.isfinite(determinant_lower) and determinant_lower > 0.0, "A385S alignment can be singular")
        determinant_lowers.append(determinant_lower)
        require(matrix_maximum_radius(chart["alignment_box"]) >= 0.0, "A385S alignment radius invalid")
        derivatives = chart["coordinate_derivatives"]
        require(len(derivatives) == 8, "A385S derivative inventory changed")
        for direction, row in enumerate(derivatives):
            require(int(row["direction_zero_based"]) == direction, "A385S direction order changed")
            replayed = matrix_maximum_radius(row["alignment_coordinate_derivative"])
            require(
                math.isclose(
                    replayed,
                    float(row["maximum_alignment_derivative_component_radius_upper"]),
                    rel_tol=2.0e-15,
                    abs_tol=1.0e-300,
                ),
                "A385S derivative radius does not replay",
            )
            derivative_radii.append(replayed)
            frame_radii.append(float(row["maximum_moving_right_frame_derivative_component_radius_upper"]))
        replay = chart["center_A378_replay"]
        require(len(replay["directions"]) == 8, "A385S center direction replay changed")
        replay_bounds.extend(
            float(replay[key])
            for key in (
                "maximum_alignment_center_replay_absolute_upper",
                "maximum_coordinate_derivative_center_replay_absolute_upper",
                "maximum_moving_right_frame_center_replay_absolute_upper",
            )
        )
    summary = packet["summary"]
    require(int(summary["coordinate_count"]) == 8, "A385S summary coordinate count changed")
    require(int(summary["certified_chart_count"]) == 2, "A385S summary chart count changed")
    require(int(summary["certified_alignment_derivative_matrices"]) == 16, "A385S derivative count changed")
    require(
        math.isclose(
            float(summary["minimum_alignment_determinant_absolute_lower"]),
            min(determinant_lowers),
            rel_tol=2.0e-15,
        ),
        "A385S determinant summary does not replay",
    )
    require(
        math.isclose(
            float(summary["maximum_alignment_derivative_component_radius_upper"]),
            max(derivative_radii),
            rel_tol=2.0e-15,
        ),
        "A385S derivative summary does not replay",
    )
    require(
        math.isclose(
            float(summary["maximum_moving_right_frame_derivative_component_radius_upper"]),
            max(frame_radii),
            rel_tol=2.0e-15,
        ),
        "A385S frame summary does not replay",
    )
    require(
        math.isclose(
            float(summary["maximum_A378_center_replay_absolute_upper"]),
            max(replay_bounds),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A385S A378 replay summary changed",
    )
    require(max(replay_bounds) < 1.0e-70, "A385S does not replay A378 at the center")
    require(float(summary["maximum_y_z_alignment_center_difference"]) == 0.0, "A385S y/z centers differ")
    audit_authorities(packet, "A385S")
    a378_path = ROOT / packet["authority"]["A378_Hessian_integrand_source"]["path"]
    audit_authorities(load(a378_path), "A378")
    scope = packet["strict_scope"]
    for key in (
        "same_selected_n3_alignment_and_PGL3_generators_used",
        "multivariate_exponential_chart_fixed",
        "all_eight_Frechet_coordinate_derivatives_interval_closed",
        "moving_right_residue_frame_derivatives_interval_closed",
        "A378_point_source_replayed_at_chart_center",
    ):
        require(scope[key] is True, f"A385S strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered A385S")
    require(scope["full_residual_Jacobian_polydisk_transport_closed"] is False, "A385S overclaims transport")
    require(scope["interval_Newton_existence_and_uniqueness_closed"] is False, "A385S overclaims interval Newton")
    require(scope["full_SM_closure_proved"] is False, "A385S overclaims full SM closure")
    print("PASS: A385S certifies the multivariate PGL3 box chart and all 16 chart-specific Frechet derivative matrices")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
