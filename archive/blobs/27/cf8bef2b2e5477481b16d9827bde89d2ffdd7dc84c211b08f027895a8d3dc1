from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.hessian_source.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCovariantHessianIntegrandSource_A378_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def decode_rows(values: list[list[dict[str, str]]]) -> list[list[acb]]:
    return [[validated.decoded_acb(value) for value in row] for row in values]


def row_matrix(row: list[acb], matrix: list[list[acb]]) -> list[acb]:
    return [
        sum((row[index] * matrix[index][column] for index in range(len(row))), acb(0))
        for column in range(len(matrix[0]))
    ]


def main() -> int:
    require(PACKET.exists(), "missing A378 packet")
    require(NOTE.exists(), "missing A378 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A378", "A378 artifact label changed")
    require(
        packet["status"]
        == "SAME_SOURCE_ALL_64_FULL_COVARIANT_HESSIAN_INTEGRAND_ROWS_DERIVED",
        "A378 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A378 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A378 authority {name}")

    charts = packet["chart_executions"]
    require([row["line_chart"] for row in charts] == ["y", "z"], "A378 chart inventory changed")
    for chart in charts:
        require(chart["direction_count"] == 8, "A378 direction count changed")
        require(chart["covariant_row_count"] == 64, "A378 row count changed")
        residue = decode_rows(chart["residue_rows_R_r"])
        require(len(residue) == 8 and all(len(row) == 5 for row in residue), "A378 residue shape changed")
        for direction, entry in enumerate(chart["deformation_directions"]):
            require(
                entry["deformation_direction_zero_based"] == direction,
                "A378 direction ordering changed",
            )
            connection = decode_rows(entry["deformation_Gauss_Manin_connection_C_s"])
            direct = decode_rows(entry["direct_residue_row_derivative_R_rs"])
            covariant = decode_rows(entry["covariant_hessian_integrand_rows"])
            source = [
                validated.decoded_acb(value)
                for value in entry["deformation_normal_function_source_eta_s"]
            ]
            beta_forcing = [
                validated.decoded_acb(value)
                for value in entry["anchored_beta_affine_forcing_R_r_eta_s"]
            ]
            require(
                len(connection) == 5 and all(len(row) == 5 for row in connection),
                "A378 connection shape changed",
            )
            require(len(direct) == 8 and len(covariant) == 8, "A378 Hessian row shape changed")
            require(len(source) == 5 and len(beta_forcing) == 8, "A378 beta source shape changed")
            for row in range(8):
                replay = [
                    direct[row][column] + value
                    for column, value in enumerate(row_matrix(residue[row], connection))
                ]
                require(
                    all(
                        covariant[row][column].overlaps(replay[column])
                        for column in range(5)
                    ),
                    "A378 covariant row identity does not replay",
                )
                forcing_replay = sum(
                    (residue[row][column] * source[column] for column in range(5)),
                    acb(0),
                )
                require(
                    beta_forcing[row].overlaps(forcing_replay),
                    "A378 beta affine forcing does not replay",
                )
            require(
                entry["Q2_discriminant_absolute_lower"] > 0.0,
                "A378 deformation Q2 discriminant contains zero",
            )
            require(
                entry["G3_quotient_norm_absolute_lower"] > 0.0,
                "A378 deformation G3 norm contains zero",
            )
        require(
            chart["maximum_verified_reduction_Neumann_norm"] < 1.0,
            "A378 verified reduction lost invertibility",
        )
        require(
            chart["minimum_chart_scale_lower"] > 0.0,
            "A378 sample left its regular chart",
        )

    theorem = packet["derived_identity"]
    require(theorem["new_scalar_source_rows"] == 0, "A378 introduced source rows")
    scope = packet["strict_scope"]
    require(scope["all_64_homogeneous_period_hessian_integrand_rows_derived"], "A378 source theorem open")
    require(scope["all_64_anchored_beta_affine_hessian_integrand_rows_derived"], "A378 beta rows open")
    require(scope["A135_log_free_tail_differentiation_rule_inherited"], "A378 lost A135 tail rule")
    require(not scope["new_scalar_source_rows_introduced"], "A378 introduced scalar rows")
    require(scope["anchored_beta_hessian_integrand_rows_derived"], "A378 beta Hessian source open")
    require(not scope["full_paths_and_tails_integrated"], "A378 overclaims path execution")
    require(not scope["interval_Jacobian_certificate"], "A378 overclaims interval Jacobian")
    require(not scope["covariant_zero_proved"], "A378 overclaims zero")
    require(not scope["observed_SM_values_used"], "A378 used observed SM values")

    print("q79 A378 covariant Hessian-integrand source audit: PASS")
    print("closed: 64 full affine same-source integrand rows in y and z charts")
    print("open: full integration, interval Jacobian enclosure, interval Newton")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
