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
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
MANIFEST = VALIDATED / "hessian" / "tailH.manifest.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def audit_authorities(packet: dict, label: str) -> None:
    authority = packet.get("authority", {})
    require(bool(authority), f"{label} has no authority inventory")
    for name, row in authority.items():
        path = ROOT / row["path"]
        require(path.is_file(), f"{label} authority absent: {name}")
        require(sha256(path) == row["sha256"], f"{label} authority stale: {name}")


def audit_matrix(packet: dict, label: str) -> None:
    rows = packet["tail_residue_rows"]
    matrix = packet["complex_tail_Hessian_8_by_8"]
    require(len(rows) == 8, f"{label} tail row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        f"{label} Hessian is not 8 by 8",
    )
    require(
        all(row["canonical_intervals_overlap"] for row in rows),
        f"{label} ordinary rows lost canonical overlap",
    )
    radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in matrix],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(radii))), f"{label} has a nonfinite radius")
    require(bool(np.all(radii >= 0.0)), f"{label} has a negative radius")
    summary = packet["summary"]
    require(int(summary["certified_tail_rows"]) == 8, f"{label} lost eight rows")
    require(int(summary["certified_tail_Hessian_entries"]) == 64, f"{label} lost 64 entries")
    require(summary["all_canonical_tail_intervals_overlap"] is True, f"{label} overlap failed")
    require(
        summary["ordinary_rows_overlap_across_all_eight_dual_executions"] is True,
        f"{label} dual ordinary-row replay failed",
    )
    require(
        math.isclose(
            float(summary["maximum_tail_Hessian_component_radius_upper"]),
            float(np.max(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        f"{label} maximum radius does not replay",
    )
    require(
        math.isclose(
            float(summary["tail_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        f"{label} Frobenius radius does not replay",
    )


def audit_quadrature(packet: dict, label: str) -> None:
    method = packet["A135_dual_quadrature_method"]
    require(
        method["identity"]
        == "differentiate the certified A135 x-theta interval quadrature",
        f"{label} differentiated-tail identity changed",
    )
    factor = method["factor_disk"]
    require(factor["quantitative_Hensel_disk_closed"] is True, f"{label} Hensel disk open")
    require(0.0 <= float(factor["contraction_bound_upper"]) < 1.0, f"{label} Hensel map not contractive")
    covers = method["accepted_radial_intervals_by_direction"]
    diagnostics = method["direction_diagnostics"]
    require(len(covers) == len(diagnostics) == 8, f"{label} direction count changed")
    epsilon = float(packet["selected_target"]["endpoint_cutoff_epsilon"])
    node_width = float(method["node_width"])
    for direction, (cover, diagnostic) in enumerate(zip(covers, diagnostics)):
        require(int(cover["direction_zero_based"]) == direction, f"{label} cover order changed")
        require(int(diagnostic["direction_zero_based"]) == direction, f"{label} diagnostic order changed")
        intervals = cover["intervals"]
        require(len(intervals) > 0, f"{label} has an empty radial cover")
        require(
            int(diagnostic["adaptive_regular_interval_count"]) == len(intervals),
            f"{label} radial interval count changed",
        )
        for interval in intervals:
            require(float(interval["lower"]) < float(interval["upper"]), f"{label} nonpositive interval")
        ordered = sorted(intervals, key=lambda row: float(row["lower"]))
        require(
            math.isclose(float(ordered[0]["lower"]), node_width, rel_tol=1.0e-14, abs_tol=1.0e-16),
            f"{label} radial cover misses the node segment",
        )
        require(
            math.isclose(float(ordered[-1]["upper"]), epsilon, rel_tol=1.0e-14, abs_tol=1.0e-16),
            f"{label} radial cover misses the cutoff",
        )
        for left, right in zip(ordered, ordered[1:]):
            require(
                math.isclose(float(left["upper"]), float(right["lower"]), rel_tol=2.0e-13, abs_tol=2.0e-16),
                f"{label} radial cover has a gap or overlap",
            )
        width = sum(float(row["upper"]) - float(row["lower"]) for row in ordered)
        require(
            math.isclose(width, epsilon - node_width, rel_tol=2.0e-13, abs_tol=2.0e-16),
            f"{label} radial width does not replay",
        )
        require(
            float(diagnostic["node_deformation_jacobian_determinant_absolute_lower"]) > 0.0,
            f"{label} moving-node derivative is singular",
        )
        require(
            float(diagnostic["factor_derivative_solve_neumann_norm"]) < 1.0,
            f"{label} factor derivative solve is not verified",
        )
        require(
            0.0 < float(diagnostic["nodal_series_ratio_upper"]) < 1.0,
            f"{label} nodal series is not contractive",
        )
        require(
            float(diagnostic["quartic_absolute_lower_on_Cauchy_disk"]) > 0.0,
            f"{label} local quartic meets zero",
        )
        require(
            float(diagnostic["minimum_quartic_half_plane_margin"]) > 0.0,
            f"{label} square-root continuation lost separation",
        )
        require(
            float(diagnostic["minimum_outer_orientation_margin"]) > 0.0,
            f"{label} period orientation lost separation",
        )


def audit_source_derived_far_route(packet: dict, label: str) -> None:
    authority = packet["authority"]
    route = packet.get("source_derived_far_route", {})
    require(
        route.get("adapter") == authority.get("source_derived_far_adapter"),
        f"{label} far-cut adapter authority changed",
    )
    require(
        route.get("A380FS_source") == authority.get("A380FS_far_cut_source"),
        f"{label} A380FS source authority changed",
    )
    require(
        bool(authority.get("selected_far_tail_interval")),
        f"{label} selected far-tail authority is absent",
    )
    require(
        bool(authority.get("derived_far_main_replay_source")),
        f"{label} derived far-main authority is absent",
    )


def main() -> int:
    prefix = load(PREFIX)
    manifest = load(MANIFEST)
    require(
        manifest["schema"] == "MTTQ79HeightFourTailHessianQueueManifest.v1",
        "tail manifest schema changed",
    )
    require(manifest["status"] == "ALL_76_TAIL_HESSIANS_CERTIFIED", "tail queue is incomplete")
    require(int(manifest["completed_count"]) == 76, "tail completed count changed")
    require(int(manifest["remaining_count"]) == 0, "tail remaining count is nonzero")
    targets = manifest["targets"]
    inventory = prefix["certified_targets_in_A219_priority_order"]
    require(len(targets) == len(inventory) == 76, "tail inventory is not 76 rows")

    artifacts = {"A381": 0, "A381Q": 0, "A381QFF": 0}
    total_entries = 0
    for expected, row in zip(inventory, targets):
        rank = int(expected["A219_profile_priority_rank"])
        index = int(expected["distinguished_index"])
        label = f"rank {rank} d{index:03d}"
        require(int(row["A219_profile_priority_rank"]) == rank, f"{label} rank changed")
        require(int(row["distinguished_index"]) == index, f"{label} index changed")
        require(row["complete"] is True, f"{label} is not complete")
        path = ROOT / row["output"]
        require(path.is_file(), f"{label} packet is absent")
        require(sha256(path) == row["output_sha256"], f"{label} packet hash changed")
        packet = load(path)
        require(
            int(packet["selected_target"]["distinguished_index"]) == index,
            f"{label} packet identity changed",
        )
        artifact = packet["artifact"]
        require(artifact in artifacts, f"{label} has an unsupported artifact")
        artifacts[artifact] += 1
        audit_matrix(packet, label)
        if artifact in {"A381Q", "A381QFF"}:
            require(
                packet["schema"]
                == "MTTQ79HeightFourTargetTailHessianQuadratureInterval.v1",
                f"{label} quadrature schema changed",
            )
            audit_quadrature(packet, label)
            if artifact == "A381QFF":
                audit_source_derived_far_route(packet, label)
        else:
            require(
                packet["schema"] == "MTTQ79HeightFourTargetTailHessianInterval.v1",
                f"{label} Frobenius schema changed",
            )
            require(
                packet["strict_scope"]["target_Frobenius_tail_Hessian_interval_closed"] is True,
                f"{label} Frobenius tail is open",
            )
        require(packet["strict_scope"]["observed_SM_values_used"] is False, f"observed values entered {label}")
        require(packet["strict_scope"]["target_full_Hessian_interval_closed"] is False, f"{label} tail overclaims full")
        audit_authorities(packet, label)
        total_entries += 64

    require(total_entries == 4864, "tail Hessian entry total changed")
    require(
        artifacts["A381"] >= 1
        and artifacts["A381Q"] + artifacts["A381QFF"] >= 1,
        "both Frobenius and certified quadrature tail routes are not represented",
    )
    audit_authorities(manifest, "tail manifest")
    print(
        "PASS: all 76 differentiated tails, 608 ordinary rows, 4,864 Hessian "
        f"entries, and authority trees replay ({artifacts})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
