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
PACKET = VALIDATED / "n3.betaH.full_lower.a390.json"
A379 = VALIDATED / "n3.beta_hessian.interval.json"
EXPECTED_WAYPOINTS = [0 + 0j, -0.1j, 1 - 0.1j, 1 + 0j]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def finite_nonnegative(values: np.ndarray, label: str) -> None:
    require(bool(np.all(np.isfinite(values))), f"A390B has a nonfinite {label}")
    require(bool(np.all(values >= 0.0)), f"A390B has a negative {label}")


def main() -> int:
    packet = load(PACKET)
    selected = load(A379)
    require(
        packet["schema"] == "MTTQ79HeightFourRank3BetaHessianInterval.v1",
        "A390B schema changed",
    )
    require(packet["artifact"] == "A390B", "A390B artifact label changed")
    require(
        packet["status"]
        == "N3_FULL_LOWER_ROUTE_BETA_HESSIAN_INTERVAL_EXECUTED_HOMOTOPY_OPEN",
        "A390B status changed",
    )

    route = packet["route"]
    require(
        route["route_id"] == "endpoint_fixed_full_lower_minus_0p1i",
        "A390B route id changed",
    )
    route_waypoints = [complex_value(value) for value in route["waypoints"]]
    execution_waypoints = [
        complex_value(value) for value in packet["execution"]["waypoints"]
    ]
    require(route_waypoints == EXPECTED_WAYPOINTS, "A390B route waypoints changed")
    require(
        execution_waypoints == EXPECTED_WAYPOINTS,
        "A390B execution waypoints changed",
    )
    require(route["same_start_and_endpoint_as_A379"] is True, "endpoint flag lost")
    require(
        route["homotopy_to_A379_selected_route_interval_certified"] is False,
        "A390B improperly promotes an uncertified contour homotopy",
    )

    rows = packet["beta_rows"]
    matrix = packet["complex_beta_Hessian_8_by_8"]
    require(len(rows) == 8, "A390B beta row count changed")
    require(
        len(matrix) == 8 and all(len(row) == 8 for row in matrix),
        "A390B Hessian is not 8 by 8",
    )
    beta_centers = np.asarray(
        [complex_value(row["interval_center"]) for row in rows], dtype=np.complex128
    )
    beta_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in rows], dtype=np.float64
    )
    hessian_centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in matrix],
        dtype=np.complex128,
    )
    hessian_radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in matrix],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(beta_centers))), "A390B beta center is nonfinite")
    require(
        bool(np.all(np.isfinite(hessian_centers))),
        "A390B Hessian center is nonfinite",
    )
    finite_nonnegative(beta_radii, "beta radius")
    finite_nonnegative(hessian_radii, "Hessian radius")

    summary = packet["summary"]
    require(int(summary["certified_beta_rows"]) == 8, "A390B lost beta rows")
    require(int(summary["certified_Hessian_entries"]) == 64, "A390B lost entries")
    require(
        math.isclose(
            float(summary["maximum_beta_component_radius_upper"]),
            float(np.max(beta_radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A390B maximum beta radius does not replay",
    )
    require(
        math.isclose(
            float(summary["maximum_Hessian_component_radius_upper"]),
            float(np.max(hessian_radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A390B maximum Hessian radius does not replay",
    )
    require(
        math.isclose(
            float(summary["Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(hessian_radii)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A390B Hessian Frobenius radius does not replay",
    )
    require(
        math.isclose(
            float(summary["Hessian_center_Frobenius_norm"]),
            float(np.linalg.norm(hessian_centers)),
            rel_tol=2.0e-15,
            abs_tol=1.0e-300,
        ),
        "A390B Hessian center norm does not replay",
    )

    steps = packet["execution"]["steps"]
    require(len(steps) == int(summary["accepted_step_count"]), "step count changed")
    require(len(steps) > 0, "A390B has no validated steps")
    positions = [0.0 for _ in range(len(EXPECTED_WAYPOINTS) - 1)]
    for step in steps:
        segment = int(step["segment_index"])
        require(0 <= segment < len(positions), "A390B segment index is invalid")
        width = float(step["step"])
        position = float(step["position"])
        require(width > 0.0, "A390B has a nonpositive step")
        require(
            math.isclose(
                position - positions[segment],
                width,
                rel_tol=2.0e-13,
                abs_tol=2.0e-15,
            ),
            "A390B path cover has a gap",
        )
        require(
            position
            <= abs(EXPECTED_WAYPOINTS[segment + 1] - EXPECTED_WAYPOINTS[segment])
            + 2.0e-15,
            "A390B step leaves its segment",
        )
        require(step["all_returned_bounds_finite"] is True, "step finiteness lost")
        for key in (
            "maximum_reduction_neumann_norm",
            "fundamental_inverse_neumann_norm",
        ):
            require(0.0 <= float(step[key]) < 1.0, f"A390B lost {key}")
        positions[segment] = position
    for index, position in enumerate(positions):
        require(
            math.isclose(
                position,
                abs(EXPECTED_WAYPOINTS[index + 1] - EXPECTED_WAYPOINTS[index]),
                rel_tol=2.0e-14,
                abs_tol=2.0e-15,
            ),
            f"A390B does not cover segment {index}",
        )

    execution = packet["execution"]
    checkpoint = ROOT / execution["checkpoint"]
    require(checkpoint.exists(), "A390B checkpoint is absent")
    require(
        sha256(checkpoint) == execution["checkpoint_sha256"],
        "A390B checkpoint authority changed",
    )
    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A390B authority path absent: {label}")
        require(sha256(path) == authority["sha256"], f"A390B authority stale: {label}")

    selected_rows = selected["beta_rows"]
    selected_matrix = selected["complex_beta_Hessian_8_by_8"]
    selected_beta_centers = np.asarray(
        [complex_value(row["interval_center"]) for row in selected_rows],
        dtype=np.complex128,
    )
    selected_beta_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in selected_rows],
        dtype=np.float64,
    )
    selected_hessian_centers = np.asarray(
        [
            [complex_value(entry["interval_center"]) for entry in row]
            for row in selected_matrix
        ],
        dtype=np.complex128,
    )
    selected_hessian_radii = np.asarray(
        [
            [float(entry["component_radius_upper"]) for entry in row]
            for row in selected_matrix
        ],
        dtype=np.float64,
    )
    beta_overlap = np.abs(beta_centers - selected_beta_centers) <= (
        beta_radii + selected_beta_radii
    )
    hessian_overlap = np.abs(hessian_centers - selected_hessian_centers) <= (
        hessian_radii + selected_hessian_radii
    )
    require(bool(np.all(beta_overlap)), "A390B beta endpoint balls miss A379")
    require(bool(np.all(hessian_overlap)), "A390B Hessian endpoint balls miss A379")

    scope = packet["strict_scope"]
    for key in (
        "endpoint_fixed_full_lower_route_interval_executed",
        "C_backed_polynomial_acceleration_equivalence_audited",
        "zero_defect_regular_affine_growth_bound_audited",
        "all_step_bounds_finite",
    ):
        require(scope[key] is True, f"A390B strict scope lost {key}")
    for key in (
        "homotopy_to_A379_selected_route_interval_certified",
        "full_lower_route_promoted_to_selected_beta_branch",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A390B overclaims {key}")

    old_beta_radius = float(
        selected["summary"]["maximum_beta_component_radius_upper"]
    )
    old_hessian_radius = float(
        selected["summary"]["maximum_Hessian_component_radius_upper"]
    )
    new_beta_radius = float(np.max(beta_radii))
    new_hessian_radius = float(np.max(hessian_radii))
    print("PASS: A390B independently replays 8 beta and 64 Hessian enclosures")
    print(
        "endpoint overlap with A379: 8/8 beta rows and 64/64 Hessian entries; "
        "this is not a homotopy proof"
    )
    print(f"beta-radius tightening factor: {old_beta_radius / new_beta_radius:.12g}")
    print(
        f"Hessian-radius tightening factor: {old_hessian_radius / new_hessian_radius:.12g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
