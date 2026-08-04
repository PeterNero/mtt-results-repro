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
    / "d065.tailH.interval.json"
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
        packet["schema"] == "MTTQ79HeightFourTargetTailHessianInterval.v1",
        "d065 tail-Hessian schema changed",
    )
    require(
        packet["status"]
        == "TARGET_LOG_FREE_FROBENIUS_TAIL_AND_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "d065 tail-Hessian status weakened",
    )
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 65, "target is not d065")
    require(target["root_id"] == "selected_038", "d065 root changed")
    require(target["line_chart"] == "z", "d065 chart changed")
    require(int(target["signed_chain_coefficient"]) == 1, "d065 chain weight changed")
    require(
        int(target["Frobenius_square_root_branch_sign_against_canonical_tail"])
        in {-1, 1},
        "Frobenius branch is not separated to a sign",
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
        "ordinary Frobenius rows no longer overlap the canonical tail",
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
    require(int(summary["certified_tail_Hessian_entries"]) == 64, "64-row gate lost")
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

    method = packet["Frobenius_method"]
    require(method["Cauchy_remainder_certified"] is True, "Cauchy tail gate lost")
    require(
        "binom(2m,m)" in method["identity"] and "Delta(x)/16" in method["identity"],
        "log-free period identity changed",
    )
    require(
        method["moving_coordinate"] == "w=w_c(s)*(1-x)",
        "moving nodal coordinate changed",
    )
    diagnostics = method["direction_diagnostics"]
    require(len(diagnostics) == 8, "deformation-direction inventory changed")
    for index, row in enumerate(diagnostics):
        require(int(row["direction_zero_based"]) == index, "direction order changed")
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
            "nodal Cauchy series is not contractive",
        )
        require(
            float(row["quartic_absolute_lower_on_Cauchy_disk"]) > 0.0,
            "nodal quartic Cauchy disk meets zero",
        )
        require(
            row["period_connection_identity_overlaps_all_five_rows"] is True,
            "D_s P=C_s P cross-check failed",
        )
        require(
            float(row["endpoint_coordinate_sliver_width_upper"]) >= 0.0,
            "endpoint sliver was not enclosed",
        )

    scope = packet["strict_scope"]
    for key in (
        "A135_log_free_branch_used",
        "moving_node_implicit_derivative_interval_closed",
        "moving_Hensel_factor_derivative_interval_closed",
        "automatic_finite_cutoff_exactness_used",
        "Cauchy_series_remainder_closed",
        "target_Frobenius_tail_Hessian_interval_closed",
    ):
        require(scope[key] is True, f"strict scope lost {key}")
    require(scope["observed_SM_values_used"] is False, "observed values entered A381")
    require(scope["target_main_Hessian_interval_closed"] is False, "tail overpromoted main")
    require(scope["target_full_Hessian_interval_closed"] is False, "tail overpromoted full")
    require(scope["full_SM_closure_proved"] is False, "A381 overpromoted SM closure")

    for authority in packet["authority"].values():
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {authority['path']}")
        require(sha256(path) == authority["sha256"], f"stale authority {authority['path']}")
    print(
        "PASS: d065 moving-node Hensel/Frobenius tail and all 64 complex "
        "Hessian entries are interval-certified with Cauchy and D_sP=C_sP gates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
