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
    / "n3.rank3.handle_hessian.interval.json"
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


def audit_path(label: str, execution: dict, endpoint: complex) -> None:
    require(execution["label"] == label, f"{label} identity changed")
    require(
        abs(complex_value(execution["endpoint"]) - endpoint) <= 1.0e-15,
        f"{label} endpoint changed",
    )
    steps = execution["accepted_steps"]
    require(len(steps) == int(execution["accepted_step_count"]), f"{label} step count changed")
    require(len(steps) > 0, f"{label} has no certified steps")
    position = 0.0
    for step in steps:
        start = float(step["start_position"])
        end = float(step["end_position"])
        width = float(step["step"])
        require(
            math.isclose(start, position, rel_tol=2.0e-14, abs_tol=2.0e-15),
            f"{label} path cover has a gap",
        )
        require(width > 0.0 and end > start, f"{label} has a nonpositive step")
        require(
            math.isclose(end - start, width, rel_tol=2.0e-13, abs_tol=2.0e-15),
            f"{label} step width does not replay",
        )
        for key in (
            "maximum_reduction_neumann_norm",
            "fundamental_inverse_neumann_norm",
        ):
            require(0.0 <= float(step[key]) < 1.0, f"{label} lost {key}")
        position = end
    require(
        math.isclose(position, 1.0, rel_tol=2.0e-14, abs_tol=2.0e-15),
        f"{label} path does not reach its endpoint",
    )
    checkpoint = ROOT / execution["checkpoint"]
    require(checkpoint.exists(), f"{label} checkpoint is absent")
    require(
        sha256(checkpoint) == execution["checkpoint_sha256"],
        f"{label} checkpoint authority changed",
    )


def main() -> int:
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourRank3HandleHessianInterval.v1",
        "A383 schema changed",
    )
    require(
        packet["status"]
        == "N3_RANK3_HANDLE_COMPLEX_8_BY_8_HESSIAN_INTERVAL_CERTIFIED",
        "A383 status weakened",
    )
    require(packet["artifact"] == "A383", "A383 artifact changed")
    coordinates = packet["selected_rank3_chain"]["primitive_handle_coordinates"]
    require(len(coordinates) == 8, "rank-3 handle coordinate count changed")
    require(
        packet["selected_rank3_chain"]["Hessian_identity"]
        == "D H_n3 = D transport_A + D transport_B",
        "handle-Hessian identity changed",
    )

    rows = packet["handle_rows"]
    matrix = packet["complex_handle_Hessian_8_by_8"]
    require(len(rows) == 8, "A383 handle row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        "A383 Hessian is not 8 by 8",
    )
    require(
        all(row["A374_intervals_overlap"] for row in rows),
        "A383 ordinary rows no longer overlap A374",
    )
    centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in matrix],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in matrix],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(centers))), "A383 has a nonfinite center")
    require(bool(np.all(np.isfinite(radii))), "A383 has a nonfinite radius")
    require(bool(np.all(radii >= 0.0)), "A383 has a negative radius")
    summary = packet["summary"]
    require(int(summary["certified_handle_rows"]) == 8, "A383 row gate changed")
    require(
        int(summary["certified_handle_Hessian_entries"]) == 64,
        "A383 64-entry gate changed",
    )
    require(
        math.isclose(
            float(summary["maximum_handle_Hessian_component_radius_upper"]),
            float(np.max(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A383 maximum radius does not replay",
    )
    require(
        math.isclose(
            float(summary["handle_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A383 Frobenius radius does not replay",
    )
    require(
        summary["all_A374_handle_intervals_overlap"] is True,
        "A383 A374 overlap summary failed",
    )

    executions = packet["path_executions"]
    audit_path("n3 rank-3 A-handle combination", executions["A"], -1j)
    audit_path("n3 rank-3 B-handle combination", executions["B"], 1 + 0j)
    smoke = packet["smoke_test"]
    require(
        float(smoke["maximum_original_main_system_disk_nonoverlap_excess"]) == 0.0,
        "A383 homogeneous Taylor disks do not replay the ordinary system",
    )
    require(
        math.isfinite(float(smoke["maximum_A378_hessian_source_difference"])),
        "A383 A378 source replay is nonfinite",
    )

    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A383 authority path absent: {label}")
        require(sha256(path) == authority["sha256"], f"A383 authority stale: {label}")

    scope = packet["strict_scope"]
    for key in (
        "selected_handle_coordinates_inherited_before_Hessian_execution",
        "same_source_A378_homogeneous_Hessian_rows_used",
        "ordinary_handle_rows_independently_replayed",
        "rank3_handle_Hessian_interval_closed",
    ):
        require(scope[key] is True, f"A383 strict scope lost {key}")
    require(scope["interval_Newton_existence_and_uniqueness_closed"] is False, "A383 overclaims interval Newton")
    require(scope["full_SM_closure_proved"] is False, "A383 overclaims full SM closure")
    print("PASS: A383 certifies both handle paths and all 64 same-source Hessian entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
