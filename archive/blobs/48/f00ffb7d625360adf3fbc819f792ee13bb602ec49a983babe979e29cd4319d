from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb, acb_mat, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import build_q79_height4_pgl3_polydisk_hessian_integrand_source as outer_source
import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.newton.chart.a388.json"
A387 = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def candidate_alignment(chart: str, coordinates: list[complex]) -> acb_mat:
    system = hessian_source.exact_n3_system(chart, dps=100)
    z_matrix = acb_mat(3, 3)
    for coordinate, generator in zip(coordinates, system.generators):
        z_matrix += acb(
            format(coordinate.real, ".17g"), format(coordinate.imag, ".17g")
        ) * generator
    return system.alignment * z_matrix.exp()


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    seed = load(A387)
    require(packet["artifact"] == "A388", "A388 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourNewtonRecenteredChartSource.v1",
        "A388 schema changed",
    )
    coordinates = [
        complex_value(value) for value in seed["floating_residual_newton_seed"]
    ]
    chart_rows = {row["line_chart"]: row for row in packet["charts"]}
    point_rows = {row["line_chart"]: row for row in packet["point_sources"]}
    require(set(chart_rows) == {"y", "z"}, "A388 chart inventory changed")
    require(set(point_rows) == {"y", "z"}, "A388 point-source inventory changed")
    for chart in ("y", "z"):
        expected_alignment = candidate_alignment(chart, coordinates)
        stored_center = validated.decoded_matrix(
            chart_rows[chart]["affine_center_alignment"]
        )
        require(
            all(
                stored_center[row, column].overlaps(expected_alignment[row, column])
                for row in range(3)
                for column in range(3)
            ),
            f"A388 {chart}-chart candidate center does not replay",
        )
        alignment_box = outer_source.decode_box_matrix(chart_rows[chart]["alignment_box"])
        require(
            all(
                alignment_box[row, column].overlaps(expected_alignment[row, column])
                for row in range(3)
                for column in range(3)
            ),
            f"A388 {chart}-chart box misses its candidate center",
        )
        require(
            float(chart_rows[chart]["alignment_determinant_absolute_lower"]) > 0.0,
            f"A388 {chart}-chart determinant gate failed",
        )

        system = hessian_source.exact_n3_system(chart, dps=100)
        system.alignment = expected_alignment
        system.alignment_0 = expected_alignment
        elliptic, line, f_coefficients, _f_w, _connection_w = hessian_source.local_geometry(
            system, acb(0)
        )
        base_rows = hessian_source.residue_rows(system, elliptic, line)
        stored_directions = point_rows[chart]["deformation_directions"]
        require(len(stored_directions) == 8, f"A388 {chart}-chart direction count changed")
        for direction in range(8):
            expected = hessian_source.direction_packet(
                system,
                elliptic,
                line,
                f_coefficients,
                base_rows,
                direction,
            )
            stored = stored_directions[direction]
            for row in range(8):
                for column in range(5):
                    left = validated.decoded_acb(
                        stored["covariant_hessian_integrand_rows"][row][column]
                    )
                    right = validated.decoded_acb(
                        expected["covariant_hessian_integrand_rows"][row][column]
                    )
                    require(left.overlaps(right), f"A388 {chart} covariant point row changed")
                left = validated.decoded_acb(
                    stored["anchored_beta_affine_forcing_R_r_eta_s"][row]
                )
                right = validated.decoded_acb(
                    expected["anchored_beta_affine_forcing_R_r_eta_s"][row]
                )
                require(left.overlaps(right), f"A388 {chart} beta forcing changed")
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A388 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A388 authority {name}")
    scope = packet["strict_scope"]
    require(
        scope["Newton_coordinates_derived_from_A384_and_A386_floating_diagnostic"],
        "A388 lost seed provenance",
    )
    require(
        not scope["floating_diagnostic_promoted_to_rigorous_residual_bound"],
        "A388 overpromotes a floating diagnostic",
    )
    require(scope["same_selected_n3_fibration_and_PGL3_generators_used"], "A388 changed geometry")
    require(scope["candidate_alignment_locally_nondegenerate"], "A388 local gate is false")
    require(not scope["full_target_paths_reexecuted_at_candidate"], "A388 overclaims path execution")
    require(not scope["wall_free_full_path_polydisk_closed"], "A388 overclaims wall freedom")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A388 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A388 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A388 overclaims SM closure")
    print(
        "PASS: A388 independently replays the Newton-recentered PGL3 chart and "
        "both 64-row point Hessian sources"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
