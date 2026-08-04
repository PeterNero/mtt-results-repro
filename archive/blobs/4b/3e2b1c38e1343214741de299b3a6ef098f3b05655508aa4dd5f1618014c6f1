from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.rank3.residual_jacobian.interval.json"
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


def matrix(packet: dict, key: str) -> tuple[np.ndarray, np.ndarray]:
    rows = packet[key]
    require(
        len(rows) == 8 and all(len(row) == 8 for row in rows),
        f"{key} is not 8 by 8",
    )
    centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in rows],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in rows],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(centers))), f"{key} has a nonfinite center")
    require(bool(np.all(np.isfinite(radii))), f"{key} has a nonfinite radius")
    require(bool(np.all(radii >= 0.0)), f"{key} has a negative radius")
    return centers, radii


def audit_authorities(packet: dict, label: str) -> None:
    authority = packet.get("authority", {})
    require(bool(authority), f"{label} has no authority inventory")
    for name, row in authority.items():
        path = ROOT / row["path"]
        require(path.is_file(), f"{label} authority absent: {name}")
        require(sha256(path) == row["sha256"], f"{label} authority stale: {name}")


def preconditioned_bounds(
    centers: np.ndarray,
    radii: np.ndarray,
    weights: list[float],
) -> tuple[np.ndarray, list[float], float]:
    center_ball = acb_mat(
        [
            [
                acb(
                    format(float(centers[row, column].real), ".17g"),
                    format(float(centers[row, column].imag), ".17g"),
                )
                for column in range(8)
            ]
            for row in range(8)
        ]
    )
    inverse = center_ball.inv()
    identity = acb_mat(8, 8)
    for index in range(8):
        identity[index, index] = acb(1)
    defect = identity - inverse * center_ball
    bounds_arb = []
    for row in range(8):
        bound_row = []
        for column in range(8):
            value = abs(defect[row, column])
            for inner in range(8):
                value += abs(inverse[row, inner]) * arb(
                    format(float(radii[inner, column]), ".17g")
                )
            bound_row.append(value)
        bounds_arb.append(bound_row)
    bounds = np.asarray(
        [[float(value.upper()) for value in row] for row in bounds_arb],
        dtype=np.float64,
    )
    weighted_rows = []
    for row in range(8):
        numerator = sum(
            (
                bounds_arb[row][column]
                * arb(format(float(weights[column]), ".17g"))
                for column in range(8)
            ),
            arb(0),
        )
        weighted_rows.append(
            float(
                (
                    numerator / arb(format(float(weights[row]), ".17g"))
                ).upper()
            )
        )
    return bounds, weighted_rows, max(weighted_rows)


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourRank3ResidualJacobianInterval.v1",
        "A384 schema changed",
    )
    require(
        packet["status"]
        == "N3_RANK3_FULL_COMPLEX_8_BY_8_RESIDUAL_JACOBIAN_INTERVAL_RECOMPOSED",
        "A384 status weakened",
    )
    require(packet["artifact"] == "A384", "A384 artifact changed")
    require(
        packet["identity"]
        == "D R_n3 = D beta_n3 - (sum_76 m_I D Pi_I + D H_rank3 + 3 D Pi_d065)",
        "A384 recomposition identity changed",
    )

    inventory = packet["target_chain_inventory"]
    require(len(inventory) == 76, "A384 target inventory is not 76 rows")
    require(
        [int(row["A219_profile_priority_rank"]) for row in inventory]
        == list(range(1, 77)),
        "A384 priority ordering changed",
    )
    indices = [int(row["distinguished_index"]) for row in inventory]
    require(len(set(indices)) == 76, "A384 repeats a target")

    chain_centers = np.zeros((8, 8), dtype=np.complex128)
    chain_radii = np.zeros((8, 8), dtype=np.float64)
    target_packets: dict[int, dict] = {}
    for row in inventory:
        index = int(row["distinguished_index"])
        coefficient = int(row["signed_chain_coefficient"])
        path = ROOT / row["certificate_path"]
        require(path.is_file(), f"A384 target certificate absent: d{index:03d}")
        require(sha256(path) == row["certificate_sha256"], f"A384 target hash stale: d{index:03d}")
        target = load(path)
        target_packets[index] = target
        require(target["artifact"] == row["certificate_artifact"], f"d{index:03d} artifact changed")
        require(
            int(target["selected_target"]["distinguished_index"]) == index,
            f"d{index:03d} certificate identity changed",
        )
        require(
            int(target["selected_target"]["signed_chain_coefficient"]) == coefficient,
            f"d{index:03d} coefficient changed",
        )
        audit_authorities(target, f"d{index:03d} full Hessian")
        for nested_key in ("A380_main_Hessian", "A381_tail_Hessian"):
            nested_path = ROOT / target["authority"][nested_key]["path"]
            audit_authorities(load(nested_path), f"d{index:03d} {nested_key}")
        centers, radii = matrix(target, "complex_full_Hessian_8_by_8")
        chain_centers += coefficient * centers
        chain_radii += abs(coefficient) * radii
        require(
            math.isclose(
                float(row["selected_contribution_frobenius_radius_upper"]),
                float(abs(coefficient) * np.linalg.norm(radii)),
                rel_tol=2.0e-15,
                abs_tol=1.0e-300,
            ),
            f"d{index:03d} contribution radius does not replay",
        )

    authority = packet["authority"]
    beta = load(ROOT / authority["A379_beta_Hessian"]["path"])
    handle = load(ROOT / authority["A383_handle_Hessian"]["path"])
    beta_centers, beta_radii = matrix(beta, "complex_beta_Hessian_8_by_8")
    handle_centers, handle_radii = matrix(handle, "complex_handle_Hessian_8_by_8")
    audit_authorities(beta, "A379")
    audit_authorities(handle, "A383")

    wall = packet["Picard_Lefschetz_wall_correction"]
    wall_index = int(wall["distinguished_index"])
    wall_weight = int(wall["integer_weight"])
    require(wall_index == 65 and wall_weight == 3, "A384 PL correction changed")
    wall_packet = target_packets[wall_index]
    wall_centers, wall_radii = matrix(wall_packet, "complex_full_Hessian_8_by_8")
    period_centers = chain_centers + handle_centers + wall_weight * wall_centers
    period_radii = chain_radii + handle_radii + abs(wall_weight) * wall_radii
    expected_centers = beta_centers - period_centers
    expected_radii = beta_radii + period_radii
    centers, radii = matrix(packet, "complex_residual_Jacobian_8_by_8")
    require(
        float(np.max(abs(centers - expected_centers))) < 2.0e-13,
        "A384 Jacobian centers do not recompose",
    )
    require(
        bool(np.allclose(radii, expected_radii, rtol=2.0e-15, atol=1.0e-300)),
        "A384 Jacobian radii do not recompose",
    )

    singular_values = np.linalg.svd(centers, compute_uv=False)
    minimum_singular = float(np.min(singular_values))
    perturbation = float(np.linalg.norm(radii))
    summary = packet["summary"]
    require(int(summary["certified_target_Hessian_count"]) == 76, "A384 target count changed")
    require(int(summary["certified_target_Hessian_entries"]) == 4864, "A384 target entry count changed")
    require(int(summary["certified_handle_Hessian_entries"]) == 64, "A384 handle entry count changed")
    require(int(summary["certified_beta_Hessian_entries"]) == 64, "A384 beta entry count changed")
    numeric_checks = {
        "maximum_Jacobian_component_radius_upper": float(np.max(radii)),
        "Jacobian_product_box_frobenius_radius_upper": perturbation,
        "Jacobian_center_frobenius_norm": float(np.linalg.norm(centers)),
        "Jacobian_center_minimum_singular_value": minimum_singular,
        "Weyl_nonsingularity_margin": minimum_singular - perturbation,
    }
    for key, expected in numeric_checks.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A384 summary does not replay {key}",
        )
    require(
        bool(summary["every_matrix_in_Jacobian_product_box_nonsingular_by_Weyl"])
        == (minimum_singular > perturbation),
        "A384 Weyl gate does not replay",
    )
    require(
        abs(complex_value(summary["Jacobian_center_determinant"]) - np.linalg.det(centers))
        < 2.0e-10,
        "A384 center determinant does not replay",
    )
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in packet["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    inverse_residual = float(np.linalg.norm(np.eye(8) - inverse @ centers))
    require(
        math.isclose(
            float(summary["center_inverse_replay_frobenius_residual"]),
            inverse_residual,
            rel_tol=2.0e-12,
            abs_tol=1.0e-16,
        ),
        "A384 inverse replay changed",
    )
    neumann = packet["verified_interval_nonsingularity"]
    weights = [float(value) for value in neumann["positive_weights"]]
    require(len(weights) == 8 and min(weights) > 0.0, "A384 weights are not positive")
    bounds, weighted_rows, contraction = preconditioned_bounds(centers, radii, weights)
    recorded_bounds = np.asarray(
        neumann["componentwise_preconditioned_defect_upper_8_by_8"],
        dtype=np.float64,
    )
    require(
        bool(np.all(recorded_bounds >= bounds)),
        "A384 recorded preconditioned bounds do not enclose the replay",
    )
    require(
        bool(
            np.allclose(
                neumann["weighted_infinity_row_uppers"],
                weighted_rows,
                rtol=2.0e-15,
                atol=1.0e-300,
            )
        ),
        "A384 weighted row bounds do not replay",
    )
    require(
        math.isclose(
            float(neumann["weighted_infinity_contraction_upper"]),
            contraction,
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A384 weighted contraction does not replay",
    )
    neumann_gate = contraction < 1.0
    require(
        bool(neumann["every_matrix_in_Jacobian_product_box_nonsingular"])
        == neumann_gate,
        "A384 preconditioned Neumann gate changed",
    )
    require(
        bool(
            summary[
                "every_matrix_in_Jacobian_product_box_nonsingular_by_preconditioned_Neumann"
            ]
        )
        == neumann_gate,
        "A384 summary Neumann gate changed",
    )

    audit_authorities(packet, "A384")
    precision_authority = packet["authority"][
        "coefficient_weighted_precision_manifest"
    ]
    precision = load(ROOT / precision_authority["path"])
    require(
        precision["status"]
        == "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED",
        "A384 precision manifest is not complete",
    )
    require(
        int(precision["counts"]["full_budget"]) == 76,
        "A384 precision manifest does not close 76 full budgets",
    )
    precision_rows = {
        int(row["distinguished_index"]): row for row in precision["targets"]
    }
    require(len(precision_rows) == 76, "A384 precision inventory changed")
    for row in inventory:
        selected = precision_rows[int(row["distinguished_index"])]
        require(selected["full_budget_pass"] is True, "A384 selected an over-budget Hessian")
        require(
            row["certificate_path"] == selected["full_path"]
            and row["certificate_sha256"] == selected["full_sha256"],
            "A384 certificate differs from the precision-manifest selection",
        )
    scope = packet["strict_scope"]
    for key in (
        "all_76_target_Hessian_intervals_closed",
        "all_76_coefficient_weighted_precision_budgets_closed",
        "rank3_handle_Hessian_interval_closed",
        "rank3_anchored_beta_Hessian_interval_closed",
        "PL_wall_Hessian_correction_closed",
        "full_residual_point_Jacobian_interval_closed",
    ):
        require(scope[key] is True, f"A384 strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered A384")
    require(
        bool(scope["point_Jacobian_product_box_nonsingularity_closed"])
        == neumann_gate,
        "A384 strict-scope nonsingularity gate changed",
    )
    require(scope["Jacobian_polydisk_extension_closed"] is False, "A384 overclaims a polydisk")
    require(scope["interval_Newton_existence_and_uniqueness_closed"] is False, "A384 overclaims interval Newton")
    require(scope["full_SM_closure_proved"] is False, "A384 overclaims full SM closure")
    print(
        "PASS: A384 independently recomposes the 76-target, handle, PL, and beta "
        "same-source 8x8 residual Jacobian interval"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
