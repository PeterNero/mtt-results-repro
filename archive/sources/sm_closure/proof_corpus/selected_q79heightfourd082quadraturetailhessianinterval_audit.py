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
    / "hessian"
    / "d082.tailH.interval.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = load(PACKET)
    require(
        packet["schema"]
        == "MTTQ79HeightFourTargetTailHessianQuadratureInterval.v1",
        "d082 quadrature tail-Hessian schema changed",
    )
    require(
        packet["status"]
        == "TARGET_A135_DUAL_QUADRATURE_TAIL_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "d082 quadrature tail-Hessian status weakened",
    )
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 82, "target is not d082")
    require(int(target["A219_contribution_rank"]) == 6, "A219 rank changed")
    require(target["root_id"] == "selected_082", "d082 root changed")
    require(target["line_chart"] == "z", "d082 chart changed")
    require(int(target["signed_chain_coefficient"]) == -2, "chain weight changed")
    require(
        int(target["quadrature_branch_sign_against_canonical_tail"]) in {-1, 1},
        "quadrature branch is not separated to a sign",
    )

    rows = packet["tail_residue_rows"]
    matrix = packet["complex_tail_Hessian_8_by_8"]
    require(len(rows) == 8, "tail row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        "tail Hessian is not 8 by 8",
    )
    require(
        all(row["canonical_intervals_overlap"] for row in rows),
        "quadrature rows no longer overlap the canonical tail",
    )
    radii = np.asarray(
        [
            [float(entry["component_radius_upper"]) for entry in row]
            for row in matrix
        ],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(radii))), "nonfinite Hessian radius")
    require(bool(np.all(radii >= 0.0)), "negative Hessian radius")
    summary = packet["summary"]
    require(int(summary["certified_tail_rows"]) == 8, "eight-row gate lost")
    require(int(summary["certified_tail_Hessian_entries"]) == 64, "64-entry gate lost")
    require(
        summary["all_canonical_tail_intervals_overlap"] is True,
        "canonical tail overlap summary failed",
    )
    require(
        summary["ordinary_rows_overlap_across_all_eight_dual_executions"] is True,
        "ordinary-row dual-execution cross-check failed",
    )
    require(
        math.isclose(
            float(summary["maximum_tail_Hessian_component_radius_upper"]),
            float(np.max(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "maximum Hessian radius summary does not replay",
    )
    require(
        math.isclose(
            float(summary["tail_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "Hessian product-box radius summary does not replay",
    )

    method = packet["A135_dual_quadrature_method"]
    require(
        method["identity"]
        == "differentiate the certified A135 x-theta interval quadrature",
        "A135 differentiated-quadrature identity changed",
    )
    require(
        method["regular_segment_method"]
        == "adaptive radial boxes and rotated half-plane square-root continuation",
        "regular-tail proof method changed",
    )
    covers = method["accepted_radial_intervals_by_direction"]
    require(len(covers) == 8, "eight directional radial covers not recorded")
    diagnostics = method["direction_diagnostics"]
    require(len(diagnostics) == 8, "deformation-direction inventory changed")
    epsilon = float(target["endpoint_cutoff_epsilon"])
    node_width = float(method["node_width"])
    for index, (row, cover) in enumerate(zip(diagnostics, covers)):
        require(int(row["direction_zero_based"]) == index, "direction order changed")
        require(
            int(cover["direction_zero_based"]) == index,
            "radial-cover direction order changed",
        )
        intervals = cover["intervals"]
        require(len(intervals) > 0, "empty directional radial cover")
        require(
            int(row["adaptive_regular_interval_count"]) == len(intervals),
            "directional interval count does not replay",
        )
        cover_lower = min(float(interval["lower"]) for interval in intervals)
        cover_upper = max(float(interval["upper"]) for interval in intervals)
        cover_width = sum(
            float(interval["upper"]) - float(interval["lower"])
            for interval in intervals
        )
        require(
            math.isclose(cover_lower, node_width, rel_tol=1.0e-14, abs_tol=1.0e-16),
            "directional radial cover does not start at the nodal segment",
        )
        require(
            math.isclose(cover_upper, epsilon, rel_tol=1.0e-14, abs_tol=1.0e-16),
            "directional radial cover does not reach the endpoint cutoff",
        )
        require(
            math.isclose(
                cover_width,
                epsilon - node_width,
                rel_tol=2.0e-13,
                abs_tol=2.0e-16,
            ),
            "directional radial cover has a gap or overlap",
        )
        require(
            math.isclose(
                float(row["regular_cover_total_width"]),
                cover_width,
                rel_tol=2.0e-15,
                abs_tol=1.0e-300,
            ),
            "directional radial-cover diagnostic does not replay",
        )
        require(
            float(row["node_deformation_jacobian_determinant_absolute_lower"]) > 0.0,
            "moving-node implicit derivative is singular",
        )
        require(
            float(row["factor_derivative_solve_neumann_norm"]) < 1.0,
            "moving Hensel-factor derivative solve is not verified",
        )
        require(
            0.0 < float(row["nodal_series_ratio_upper"]) < 1.0,
            "local nodal series is not contractive",
        )
        require(
            float(row["quartic_absolute_lower_on_Cauchy_disk"]) > 0.0,
            "local nodal quartic Cauchy disk meets zero",
        )
        require(
            float(row["minimum_quartic_half_plane_margin"]) > 0.0,
            "regular quadrature lost square-root half-plane separation",
        )
        require(
            float(row["minimum_outer_orientation_margin"]) > 0.0,
            "regular quadrature lost period-orientation separation",
        )
        require(
            float(row["node_derivative_radius_upper"]) >= 0.0,
            "node derivative contribution is not enclosed",
        )

    scope = packet["strict_scope"]
    for key in (
        "moving_node_implicit_derivative_interval_closed",
        "moving_Hensel_factor_derivative_interval_closed",
        "A135_dual_quadrature_tail_Hessian_interval_closed",
        "target_tail_Hessian_interval_closed",
    ):
        require(scope[key] is True, f"strict scope lost {key}")
    require(
        scope["target_Frobenius_tail_Hessian_interval_closed"] is False,
        "A381Q falsely claims the global Frobenius route",
    )
    require(scope["observed_SM_values_used"] is False, "observed values entered A381Q")
    require(scope["target_main_Hessian_interval_closed"] is False, "tail overpromoted main")
    require(scope["target_full_Hessian_interval_closed"] is False, "tail overpromoted full")
    require(scope["full_SM_closure_proved"] is False, "A381Q overpromoted SM closure")

    for authority in packet["authority"].values():
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {authority['path']}")
        require(sha256(path) == authority["sha256"], f"stale authority {authority['path']}")
    print(
        "PASS: d082 differentiated A135 quadrature certifies all eight tail rows "
        "and all 64 complex Hessian entries on a common interval cover"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
