from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sys

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_q79_height4_covariant_hessian_integrand_source as hessian_source
import certify_q79_selected_side_beta_defect_transport as validated
import q79_multivariate_affine_runtime as affine


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "n3.pgl3.centered_affine_hessian_source.json"
A378 = VALIDATED / "n3.hessian_source.json"
A385I = VALIDATED / "n3.pgl3.polydisk_hessian_source.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, *, tolerance: float = 2.0e-12) -> bool:
    return abs(left - right) <= tolerance * max(1.0, abs(left), abs(right))


def authority_current(packet: dict) -> bool:
    rows = packet.get("authority", {})
    return bool(rows) and all(
        (ROOT / row.get("path", "")).is_file()
        and sha256(ROOT / row["path"]) == row.get("sha256")
        for row in rows.values()
    )


def decoded_form(row: dict) -> tuple[acb, list[acb], float, float]:
    center = validated.decoded_acb(row["center"])
    coefficients = [
        validated.decoded_acb(value) for value in row["unit_disk_coefficients"]
    ]
    remainder = float(row["uniform_nonlinear_remainder_upper"])
    stored_radius = float(row["centered_complex_disk_radius_upper"])
    require(len(coefficients) == 8, "affine coefficient count changed")
    require(math.isfinite(remainder) and remainder >= 0.0, "invalid affine remainder")
    require(
        math.isfinite(stored_radius) and stored_radius >= 0.0,
        "invalid affine disk radius",
    )
    reconstructed = (
        validated.radius_upper(center)
        + sum(float(abs(value).upper()) for value in coefficients)
        + remainder
    )
    require(
        reconstructed <= stored_radius * (1.0 + 2.0e-14) + 1.0e-300,
        "stored affine disk radius is not outward",
    )
    return center, coefficients, remainder, stored_radius


def disk_ball(center: acb, radius: float) -> acb:
    midpoint = affine.midpoint_acb(center)
    return acb(
        arb(str(midpoint.real), format(radius, ".17g")),
        arb(str(midpoint.imag), format(radius, ".17g")),
    )


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    point = load(A378)
    raw = load(A385I)
    require(
        packet.get("schema")
        == "MTTQ79HeightFourPGL3CenteredAffineHessianSource.v1",
        "A385A schema changed",
    )
    require(packet.get("artifact") == "A385A", "A385A artifact changed")
    require(authority_current(packet), "A385A authority is stale")
    require(packet["authority"]["A378_point_Hessian_source"]["sha256"] == sha256(A378), "A378 authority mismatch")
    require(packet["authority"]["A385I_raw_polydisk_outer_source"]["sha256"] == sha256(A385I), "A385I authority mismatch")

    point_by_chart = {row["line_chart"]: row for row in point["chart_executions"]}
    raw_by_chart = {row["line_chart"]: row for row in raw["chart_executions"]}
    charts = packet["chart_executions"]
    require([row["line_chart"] for row in charts] == ["y", "z"], "chart order changed")
    covariant_count = 0
    forcing_count = 0
    maximum_covariant = 0.0
    maximum_forcing = 0.0
    maximum_contraction = 0.0
    for chart_row in charts:
        chart = chart_row["line_chart"]
        system = hessian_source.exact_n3_system(chart, dps=100)
        box = chart_row["coordinate_box"]
        requested = float(box["real_and_imaginary_coordinate_radius"])
        disk_radius = float(box["enclosing_independent_complex_disk_radius_upper"])
        require(
            disk_radius >= math.sqrt(2.0) * requested,
            "complex disk does not enclose the real-imaginary square",
        )
        generator_norms = [
            affine.matrix_infinity_norm(generator) for generator in system.generators
        ]
        rho = arb(format(disk_radius, ".17g"))
        z_norm = sum((rho * value for value in generator_norms), arb(0))
        exponential_tail = z_norm.exp() - arb(1) - z_norm
        diagnostics = chart_row["chart_affine_source_diagnostics"]
        require(
            close(
                float(diagnostics["Z_matrix_infinity_norm_upper"]),
                affine.upper(z_norm),
            ),
            "Z norm was not independently reproduced",
        )
        require(
            close(
                float(diagnostics["matrix_exponential_second_order_tail_upper"]),
                affine.upper(exponential_tail),
            ),
            "matrix exponential tail was not independently reproduced",
        )
        solves = chart_row["weighted_affine_reduction_solves"]
        require(len(solves) == 8, "affine reduction solve count changed")
        for solve in solves:
            contraction = float(solve["weighted_contraction_upper"])
            require(0.0 <= contraction < 1.0, "affine solve is not contractive")
            require(
                len(solve["positive_weights"]) == 11
                and min(float(value) for value in solve["positive_weights"]) > 0.0,
                "affine solve weights are not positive",
            )
            maximum_contraction = max(maximum_contraction, contraction)

        point_directions = point_by_chart[chart]["deformation_directions"]
        raw_directions = raw_by_chart[chart]["deformation_directions"]
        directions = chart_row["deformation_directions"]
        require(len(directions) == 8, "deformation direction count changed")
        for direction, row in enumerate(directions):
            point_covariant = [
                [validated.decoded_acb(value) for value in values]
                for values in point_directions[direction][
                    "covariant_hessian_integrand_rows"
                ]
            ]
            raw_covariant = [
                [validated.decoded_acb(value) for value in values]
                for values in raw_directions[direction][
                    "covariant_hessian_integrand_rows"
                ]
            ]
            affine_covariant = row["covariant_hessian_integrand_rows"]
            require(
                len(affine_covariant) == 8
                and all(len(values) == 5 for values in affine_covariant),
                "covariant affine shape changed",
            )
            for residue_row in range(8):
                for column in range(5):
                    center, _coefficients, _remainder, radius = decoded_form(
                        affine_covariant[residue_row][column]
                    )
                    require(
                        center.overlaps(point_covariant[residue_row][column]),
                        "affine center misses A378",
                    )
                    require(
                        disk_ball(center, radius).overlaps(
                            raw_covariant[residue_row][column]
                        ),
                        "affine enclosure misses the independent A385I outer box",
                    )
                    maximum_covariant = max(maximum_covariant, radius)
                    covariant_count += 1

            point_forcing = [
                validated.decoded_acb(value)
                for value in point_directions[direction][
                    "anchored_beta_affine_forcing_R_r_eta_s"
                ]
            ]
            raw_forcing = [
                validated.decoded_acb(value)
                for value in raw_directions[direction][
                    "anchored_beta_affine_forcing_R_r_eta_s"
                ]
            ]
            affine_forcing = row["anchored_beta_affine_forcing_R_r_eta_s"]
            require(len(affine_forcing) == 8, "beta forcing affine shape changed")
            for residue_row in range(8):
                center, _coefficients, _remainder, radius = decoded_form(
                    affine_forcing[residue_row]
                )
                require(center.overlaps(point_forcing[residue_row]), "forcing center misses A378")
                require(
                    disk_ball(center, radius).overlaps(raw_forcing[residue_row]),
                    "forcing enclosure misses A385I",
                )
                maximum_forcing = max(maximum_forcing, radius)
                forcing_count += 1

    summary = packet["summary"]
    require(covariant_count == 640, "covariant affine total changed")
    require(forcing_count == 128, "forcing affine total changed")
    require(
        close(maximum_covariant, float(summary["maximum_covariant_centered_disk_radius_upper"])),
        "covariant maximum changed",
    )
    require(
        close(maximum_forcing, float(summary["maximum_beta_forcing_centered_disk_radius_upper"])),
        "forcing maximum changed",
    )
    require(
        close(maximum_contraction, float(summary["maximum_affine_reduction_weighted_contraction_upper"])),
        "contraction maximum changed",
    )
    require(
        float(summary["covariant_radius_compression_factor"]) > 1.0e6
        and float(summary["beta_forcing_radius_compression_factor"]) > 1.0e6,
        "dependency-preserving contraction disappeared",
    )
    scope = packet["strict_scope"]
    for key in (
        "same_selected_n3_alignment_and_PGL3_generators_used",
        "all_eight_coordinate_dependencies_retained_affinely",
        "matrix_exponential_quadratic_remainder_closed",
        "all_sixteen_Frechet_derivative_quadratic_remainders_closed",
        "all_reduction_solves_weighted_Neumann_certified",
        "local_covariant_Hessian_rows_centered_affine_closed",
        "local_anchored_beta_forcing_centered_affine_closed",
    ):
        require(scope[key] is True, f"A385A closed flag {key} changed")
    for key in (
        "moving_initial_cycle_polydisk_enclosure_closed",
        "full_path_Hessian_polydisk_transport_closed",
        "wall_free_polydisk_closed",
        "full_residual_Jacobian_polydisk_transport_closed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A385A overclaims {key}")
    require(scope["observed_SM_values_used"] is False, "A385A imported SM data")
    print(
        "PASS: A385A independently audits 640 covariant and 128 beta-forcing "
        "eight-variable centered-affine forms"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
