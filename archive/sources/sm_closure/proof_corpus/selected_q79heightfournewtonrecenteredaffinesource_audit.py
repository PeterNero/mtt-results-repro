from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_q79_height4_pgl3_centered_affine_hessian_source as affine_source
import build_q79_height4_pgl3_polydisk_hessian_integrand_source as outer_source


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.newton.affine.a389.json"
A388 = VALIDATED / "n3.newton.chart.a388.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compare_float(actual: float, expected: float, label: str) -> None:
    require(
        math.isclose(float(actual), float(expected), rel_tol=2.0e-13, abs_tol=1.0e-300),
        f"A389 changed {label}",
    )


def main() -> int:
    packet = load(PACKET)
    source = load(A388)
    require(packet["artifact"] == "A389", "A389 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourNewtonRecenteredAffineSource.v1",
        "A389 schema changed",
    )
    point_by_chart = {row["line_chart"]: row for row in source["point_sources"]}
    stored_outer = {row["line_chart"]: row for row in packet["outer_interval_executions"]}
    stored_affine = {row["line_chart"]: row for row in packet["centered_affine_executions"]}
    require(set(stored_outer) == {"y", "z"}, "A389 outer chart inventory changed")
    require(set(stored_affine) == {"y", "z"}, "A389 affine chart inventory changed")

    for chart_row in source["charts"]:
        chart = chart_row["line_chart"]
        expected_outer = outer_source.chart_execution(chart_row, point_by_chart[chart], dps=100)
        expected_affine = affine_source.chart_execution(
            chart_row, point_by_chart[chart], expected_outer
        )
        for key in (
            "minimum_deformation_Q2_discriminant_absolute_lower",
            "minimum_deformation_G3_quotient_norm_absolute_lower",
            "maximum_covariant_row_component_radius_upper",
            "maximum_beta_affine_forcing_radius_upper",
            "maximum_verified_weighted_reduction_contraction_upper",
        ):
            compare_float(stored_outer[chart][key], expected_outer[key], f"{chart} outer {key}")
        for key in (
            "minimum_reduction_weighted_contraction_margin",
            "maximum_reduction_solution_component_error_upper",
            "maximum_covariant_centered_disk_radius_upper",
            "maximum_beta_forcing_centered_disk_radius_upper",
        ):
            compare_float(stored_affine[chart][key], expected_affine[key], f"{chart} affine {key}")
        require(stored_affine[chart]["all_A378_point_centers_overlap"], f"A389 {chart} lost point overlap")
        require(stored_affine[chart]["all_A385I_raw_boxes_overlap"], f"A389 {chart} lost outer overlap")
        require(len(stored_affine[chart]["deformation_directions"]) == 8, f"A389 {chart} direction count changed")

    summary = packet["summary"]
    require(int(summary["certified_covariant_affine_forms"]) == 640, "A389 covariant count changed")
    require(int(summary["certified_beta_forcing_affine_forms"]) == 128, "A389 beta count changed")
    require(float(summary["maximum_affine_reduction_weighted_contraction_upper"]) < 1.0, "A389 contraction gate failed")
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A389 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A389 authority {name}")
    scope = packet["strict_scope"]
    require(scope["same_A388_Newton_center_and_selected_generators_used"], "A389 changed source")
    require(scope["all_reduction_solves_weighted_Neumann_certified"], "A389 solve gate is false")
    require(scope["local_covariant_Hessian_rows_centered_affine_closed"], "A389 local rows open")
    require(not scope["full_target_path_Hessian_polydisk_transport_closed"], "A389 overclaims paths")
    require(not scope["coupled_residual_polydisk_transport_closed"], "A389 overclaims residual transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A389 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A389 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A389 overclaims SM closure")
    print(
        "PASS: A389 independently reexecutes both Newton-recentered outer and "
        "centered-affine eight-variable source systems"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
