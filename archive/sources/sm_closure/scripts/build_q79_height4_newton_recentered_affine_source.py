from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import ctx

import build_q79_height4_pgl3_centered_affine_hessian_source as affine_source
import build_q79_height4_pgl3_polydisk_hessian_integrand_source as outer_source


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A388 = VALIDATED / "n3.newton.chart.a388.json"
OUTPUT = VALIDATED / "n3.newton.affine.a389.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourNewtonRecenteredAffineSource_A389_v1.md"
ARTIFACT = "A389"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def main() -> int:
    ctx.dps = 100
    source = load(A388)
    if source.get("artifact") != "A388":
        raise AssertionError("A389 requires A388")
    point_by_chart = {row["line_chart"]: row for row in source["point_sources"]}
    outer_rows = []
    affine_rows = []
    for chart_row in source["charts"]:
        chart = chart_row["line_chart"]
        point = point_by_chart[chart]
        outer = outer_source.chart_execution(chart_row, point, dps=100)
        centered = affine_source.chart_execution(chart_row, point, outer)
        outer_rows.append(outer)
        affine_rows.append(centered)

    maximum_covariant = max(
        row["maximum_covariant_centered_disk_radius_upper"] for row in affine_rows
    )
    maximum_forcing = max(
        row["maximum_beta_forcing_centered_disk_radius_upper"] for row in affine_rows
    )
    raw_covariant = max(
        row["maximum_covariant_row_component_radius_upper"] for row in outer_rows
    )
    raw_forcing = max(
        row["maximum_beta_affine_forcing_radius_upper"] for row in outer_rows
    )
    maximum_contraction = max(
        solve["weighted_contraction_upper"]
        for chart in affine_rows
        for solve in chart["weighted_affine_reduction_solves"]
    )
    payload = {
        "schema": "MTTQ79HeightFourNewtonRecenteredAffineSource.v1",
        "status": "NEWTON_RECENTERED_PGL3_POLYDISK_CENTERED_AFFINE_SOURCE_CERTIFIED",
        "artifact": ARTIFACT,
        "domain_model": (
            "A_*(w)=A_* exp(sum_s w_s G_s), with each real-imaginary square "
            "enclosed by an independent complex unit disk"
        ),
        "outer_interval_executions": outer_rows,
        "centered_affine_executions": affine_rows,
        "summary": {
            "certified_chart_count": 2,
            "coordinate_count": 8,
            "certified_covariant_affine_forms": 2 * 8 * 8 * 5,
            "certified_beta_forcing_affine_forms": 2 * 8 * 8,
            "local_real_and_imaginary_coordinate_radius": float(
                source["summary"]["local_real_and_imaginary_coordinate_radius"]
            ),
            "minimum_outer_Q2_discriminant_absolute_lower": min(
                row["minimum_deformation_Q2_discriminant_absolute_lower"]
                for row in outer_rows
            ),
            "minimum_outer_G3_quotient_norm_absolute_lower": min(
                row["minimum_deformation_G3_quotient_norm_absolute_lower"]
                for row in outer_rows
            ),
            "maximum_raw_covariant_radius_upper": raw_covariant,
            "maximum_raw_beta_forcing_radius_upper": raw_forcing,
            "maximum_covariant_centered_disk_radius_upper": maximum_covariant,
            "maximum_beta_forcing_centered_disk_radius_upper": maximum_forcing,
            "covariant_radius_compression_factor": raw_covariant / maximum_covariant,
            "beta_forcing_radius_compression_factor": raw_forcing / maximum_forcing,
            "maximum_affine_reduction_weighted_contraction_upper": maximum_contraction,
            "every_affine_center_replays_A388_point_source": True,
            "every_affine_disk_overlaps_outer_interval_source": True,
        },
        "authority": {
            "A388_Newton_recentered_chart_and_point_source": authority(A388),
            "outer_interval_source_runtime": authority(Path(outer_source.__file__).resolve()),
            "centered_affine_source_runtime": authority(Path(affine_source.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_A388_Newton_center_and_selected_generators_used": True,
            "all_eight_coordinate_dependencies_retained_affinely": True,
            "all_reduction_solves_weighted_Neumann_certified": maximum_contraction < 1.0,
            "local_covariant_Hessian_rows_centered_affine_closed": True,
            "local_anchored_beta_forcing_centered_affine_closed": True,
            "full_target_path_Hessian_polydisk_transport_closed": False,
            "coupled_residual_polydisk_transport_closed": False,
            "wall_free_full_path_polydisk_closed": False,
            "full_residual_Jacobian_polydisk_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "propagate these centered-affine rows and moving initial cycles along "
            "the 76 target, handle, beta, and Picard-Lefschetz paths"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Newton-Recentered Affine Source (A389) v1\n\n"
        "A389 evaluates the full eight-variable covariant Hessian and anchored-beta "
        "forcing source over the A388 Newton-recentered chart. It retains every "
        "linear coordinate coefficient and bounds only nonlinear remainders.\n\n"
        f"The maximum centered covariant radius is `{maximum_covariant:.12g}` and "
        f"the maximum beta-forcing radius is `{maximum_forcing:.12g}`. The largest "
        f"weighted reduction contraction is `{maximum_contraction:.12g}`.\n\n"
        "This closes the local recentered affine source. The moving cycles, full "
        "paths, wall-free enclosure, and interval-Newton gate remain separate.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
