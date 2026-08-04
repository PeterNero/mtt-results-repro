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
HESSIAN = VALIDATED / "hessian"
SELFCHECK = VALIDATED / "n3.batched_taylor_solve.selfcheck.json"
MAIN = HESSIAN / "d065.mainH.interval.json"
TAIL = HESSIAN / "d065.tailH.interval.json"
FULL = HESSIAN / "d065.fullH.interval.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def check_authority(packet: dict, label: str) -> None:
    for authority in packet["authority"].values():
        path = ROOT / authority["path"]
        require(path.exists(), f"{label} missing authority {authority['path']}")
        require(
            sha256(path) == authority["sha256"],
            f"{label} stale authority {authority['path']}",
        )


def main() -> int:
    selfcheck = load(SELFCHECK)
    require(
        selfcheck["schema"] == "MTTQ79HeightFourBatchedTaylorSolveSelfcheck.v1",
        "A380S schema changed",
    )
    require(
        selfcheck["status"]
        == "BATCHED_TAYLOR_SOLVE_INDEPENDENT_RESIDUAL_COVERAGE_CERTIFIED",
        "A380S status weakened",
    )
    checks = selfcheck["chart_checks"]
    require({row["line_chart"] for row in checks} == {"y", "z"}, "chart gate lost")
    for row in checks:
        require(int(row["right_hand_side_count"]) == 9, "RHS count changed")
        require(int(row["target_column_count"]) == 45, "target count changed")
        require(
            float(row["fast_solver_Neumann_norm"]) < 1.0,
            "batched solve is not contractive",
        )
        require(
            float(row["maximum_generic_center_coefficient_difference"]) < 1.0e-50,
            "generic center recurrence no longer replays",
        )
        require(
            row["all_45_independent_residual_corrections_covered"] is True,
            "independent residual coverage lost",
        )
        require(
            float(row["minimum_assigned_minus_required_margin"]) >= 0.0,
            "independent residual correction is under-enclosed",
        )
    require(
        selfcheck["strict_scope"]["observed_SM_values_used"] is False,
        "observed values entered A380S",
    )
    check_authority(selfcheck, "A380S")

    main_packet = load(MAIN)
    require(
        main_packet["schema"] == "MTTQ79HeightFourTargetMainHessianInterval.v1",
        "A380 schema changed",
    )
    require(
        main_packet["status"]
        in {
            "TARGET_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
            "TARGET_REVERSE_MAIN_EIGHT_ROWS_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        },
        "A380 status weakened",
    )
    target = main_packet["selected_target"]
    require(int(target["distinguished_index"]) == 65, "A380 target changed")
    require(target["root_id"] == "selected_038", "A380 root changed")
    require(target["line_chart"] == "z", "A380 chart changed")
    rows = main_packet["main_residue_rows"]
    matrix = main_packet["complex_main_Hessian_8_by_8"]
    require(len(rows) == 8, "A380 row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        "A380 Hessian is not 8 by 8",
    )
    require(
        all(row["canonical_intervals_overlap"] for row in rows),
        "A380 ordinary rows lost canonical overlap",
    )
    main_radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in matrix]
    )
    require(bool(np.all(np.isfinite(main_radii))), "A380 has nonfinite radii")
    require(bool(np.all(main_radii >= 0.0)), "A380 has negative radii")
    summary = main_packet["summary"]
    require(int(summary["certified_main_Hessian_entries"]) == 64, "A380 lost 64 entries")
    require(
        math.isclose(
            float(summary["maximum_main_Hessian_component_radius_upper"]),
            float(np.max(main_radii)),
            rel_tol=2.0e-15,
        ),
        "A380 maximum radius summary does not replay",
    )
    require(
        math.isclose(
            float(summary["main_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(main_radii)),
            rel_tol=2.0e-15,
        ),
        "A380 Frobenius radius summary does not replay",
    )
    smoke = main_packet["smoke_test"]
    require(int(smoke["batched_reduction_right_hand_side_count"]) == 9, "batch lost")
    require(int(smoke["batched_reduction_target_column_count"]) == 45, "batch width changed")
    replay_difference = smoke.get(
        "maximum_original_main_system_coefficient_difference",
        smoke.get("maximum_original_main_system_polynomial_center_difference_bound"),
    )
    require(
        replay_difference is not None and float(replay_difference) < 1.0e-40,
        "ordinary main-system replay failed",
    )
    if "maximum_original_main_system_disk_nonoverlap_excess" in smoke:
        require(
            float(smoke["maximum_original_main_system_disk_nonoverlap_excess"]) <= 0.0,
            "reverse main-system interval replay lost overlap",
        )
    require(
        float(smoke["maximum_A378_hessian_source_difference"]) < 1.0e-70,
        "A378 source replay failed",
    )
    execution = main_packet["execution"]
    require(
        len(execution["steps"]) == int(summary["accepted_step_count"]),
        "A380 step inventory changed",
    )
    checkpoint = ROOT / execution["checkpoint"]
    require(checkpoint.exists(), "A380 checkpoint missing")
    require(sha256(checkpoint) == execution["checkpoint_sha256"], "A380 checkpoint stale")
    scope = main_packet["strict_scope"]
    require(scope["target_main_Hessian_interval_closed"] is True, "A380 main open")
    require(scope["observed_SM_values_used"] is False, "observed values entered A380")
    require(scope["target_full_Hessian_interval_closed"] is False, "A380 overpromoted full")
    check_authority(main_packet, "A380")

    tail_packet = load(TAIL)
    full_packet = load(FULL)
    require(
        full_packet["schema"] == "MTTQ79HeightFourTargetFullHessianInterval.v1",
        "A382 schema changed",
    )
    require(
        full_packet["status"] == "TARGET_FULL_COMPLEX_8_BY_8_HESSIAN_INTERVAL_SPLICED",
        "A382 status weakened",
    )
    full_target = full_packet["selected_target"]
    orientation = int(full_target["orientation_sign"])
    coefficient = int(full_target["signed_chain_coefficient"])
    require(orientation in {-1, 1}, "A382 orientation is not a sign")
    main_centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in matrix]
    )
    tail_matrix = tail_packet["complex_tail_Hessian_8_by_8"]
    tail_centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in tail_matrix]
    )
    tail_radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in tail_matrix]
    )
    full_matrix = full_packet["complex_full_Hessian_8_by_8"]
    full_centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in full_matrix]
    )
    full_radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in full_matrix]
    )
    require(
        float(np.max(abs(full_centers - (main_centers + orientation * tail_centers))))
        < 1.0e-14,
        "A382 Hessian centers do not replay the oriented splice",
    )
    require(
        bool(
            np.allclose(
                full_radii,
                main_radii + tail_radii,
                rtol=2.0e-15,
                atol=1.0e-300,
            )
        ),
        "A382 Hessian radii do not replay the interval sum",
    )
    for row_index, row in enumerate(full_matrix):
        for column_index, entry in enumerate(row):
            require(
                abs(
                    complex_value(entry["selected_chain_contribution_center"])
                    - coefficient * full_centers[row_index, column_index]
                )
                < 1.0e-14,
                "A382 selected-chain center does not replay",
            )
            require(
                math.isclose(
                    float(entry["selected_chain_contribution_radius_upper"]),
                    abs(coefficient) * full_radii[row_index, column_index],
                    rel_tol=2.0e-15,
                ),
                "A382 selected-chain radius does not replay",
            )
    full_summary = full_packet["summary"]
    require(int(full_summary["certified_full_Hessian_entries"]) == 64, "A382 lost 64 entries")
    require(full_summary["all_canonical_full_intervals_overlap"] is True, "full overlap lost")
    require(
        math.isclose(
            float(full_summary["full_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(full_radii)),
            rel_tol=2.0e-15,
        ),
        "A382 Frobenius radius summary does not replay",
    )
    full_scope = full_packet["strict_scope"]
    require(full_scope["target_full_Hessian_interval_closed"] is True, "A382 full open")
    require(full_scope["observed_SM_values_used"] is False, "observed values entered A382")
    require(
        full_scope["full_76_target_chain_Hessian_interval_closed"] is False,
        "A382 overpromoted the 76-chain",
    )
    check_authority(full_packet, "A382")
    print(
        "PASS: A380S batched solve, d065 main 8x8 Hessian, and A382 "
        "oriented full-Hessian splice replay with current authorities"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
