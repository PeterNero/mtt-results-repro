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
PACKET = VALIDATED / "n3.betaH.left_upper.a391.json"
A379 = VALIDATED / "n3.beta_hessian.interval.json"
HOMOTOPY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_left_upper_0p05_homotopy.a390h.interval.json"
)
EXPECTED_WAYPOINTS = [
    0 + 0j,
    0 + 0.05j,
    0.65 + 0.05j,
    0.65 - 0.1j,
    0.82 - 0.1j,
    0.82 + 0j,
    1 + 0j,
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def centers_and_radii(packet: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    beta_centers = np.asarray(
        [complex_value(row["interval_center"]) for row in packet["beta_rows"]],
        dtype=np.complex128,
    )
    beta_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in packet["beta_rows"]],
        dtype=np.float64,
    )
    hessian_centers = np.asarray(
        [
            [complex_value(entry["interval_center"]) for entry in row]
            for row in packet["complex_beta_Hessian_8_by_8"]
        ],
        dtype=np.complex128,
    )
    hessian_radii = np.asarray(
        [
            [float(entry["component_radius_upper"]) for entry in row]
            for row in packet["complex_beta_Hessian_8_by_8"]
        ],
        dtype=np.float64,
    )
    return beta_centers, beta_radii, hessian_centers, hessian_radii


def main() -> int:
    packet = load(PACKET)
    selected = load(A379)
    homotopy = load(HOMOTOPY)
    require(packet["artifact"] == "A391", "A391 artifact changed")
    require(
        packet["schema"] == "MTTQ79HeightFourRank3BetaHessianInterval.v1",
        "A391 schema changed",
    )
    require(
        packet["status"]
        == "N3_LEFT_UPPER_SELECTED_ROUTE_BETA_HESSIAN_INTERVAL_EXECUTED",
        "A391 status changed",
    )
    require(
        homotopy["status"] == "LEFT_UPPER_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED"
        and homotopy["decision"]["A379_to_left_upper_route_homotopy_certified"]
        is True,
        "A390H no longer certifies A391",
    )
    route = packet["route"]
    require(route["route_id"] == "A390H_certified_left_upper_0p05", "route id changed")
    require(
        [complex_value(value) for value in route["waypoints"]] == EXPECTED_WAYPOINTS,
        "A391 route changed",
    )
    require(
        [complex_value(value) for value in packet["execution"]["waypoints"]]
        == EXPECTED_WAYPOINTS,
        "A391 execution route changed",
    )
    require(route["homotopy_to_A379_selected_route_interval_certified"] is True, "homotopy flag lost")
    require(route["homotopy_certificate_sha256"] == sha256(HOMOTOPY), "homotopy hash changed")

    require(len(packet["beta_rows"]) == 8, "A391 beta row count changed")
    matrix = packet["complex_beta_Hessian_8_by_8"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "A391 Hessian is not 8 by 8")
    bc, br, hc, hr = centers_and_radii(packet)
    sbc, sbr, shc, shr = centers_and_radii(selected)
    for values, label in ((bc, "beta center"), (br, "beta radius"), (hc, "Hessian center"), (hr, "Hessian radius")):
        require(bool(np.all(np.isfinite(values))), f"A391 has a nonfinite {label}")
    require(bool(np.all(br >= 0.0)) and bool(np.all(hr >= 0.0)), "A391 has a negative radius")
    require(bool(np.all(np.abs(bc - sbc) <= br + sbr)), "A391 beta endpoint balls miss A379")
    require(bool(np.all(np.abs(hc - shc) <= hr + shr)), "A391 Hessian endpoint balls miss A379")

    summary = packet["summary"]
    require(int(summary["certified_beta_rows"]) == 8, "A391 lost beta rows")
    require(int(summary["certified_Hessian_entries"]) == 64, "A391 lost Hessian entries")
    require(math.isclose(float(summary["maximum_beta_component_radius_upper"]), float(np.max(br)), rel_tol=2.0e-15, abs_tol=1.0e-300), "beta maximum does not replay")
    require(math.isclose(float(summary["maximum_Hessian_component_radius_upper"]), float(np.max(hr)), rel_tol=2.0e-15, abs_tol=1.0e-300), "Hessian maximum does not replay")
    require(math.isclose(float(summary["Hessian_product_box_frobenius_radius_upper"]), float(np.linalg.norm(hr)), rel_tol=2.0e-15, abs_tol=1.0e-300), "Hessian Frobenius radius does not replay")

    steps = packet["execution"]["steps"]
    require(len(steps) == int(summary["accepted_step_count"]) and len(steps) > 0, "A391 step count changed")
    positions = [0.0] * (len(EXPECTED_WAYPOINTS) - 1)
    for step in steps:
        segment = int(step["segment_index"])
        require(0 <= segment < len(positions), "A391 segment index invalid")
        width = float(step["step"])
        position = float(step["position"])
        require(width > 0.0, "A391 has a nonpositive step")
        require(math.isclose(position - positions[segment], width, rel_tol=2.0e-13, abs_tol=2.0e-15), "A391 path cover has a gap")
        require(step["all_returned_bounds_finite"] is True, "A391 step lost finiteness")
        for key in ("maximum_reduction_neumann_norm", "fundamental_inverse_neumann_norm"):
            require(0.0 <= float(step[key]) < 1.0, f"A391 lost {key}")
        positions[segment] = position
    for index, position in enumerate(positions):
        require(math.isclose(position, abs(EXPECTED_WAYPOINTS[index + 1] - EXPECTED_WAYPOINTS[index]), rel_tol=2.0e-14, abs_tol=2.0e-15), f"A391 does not cover segment {index}")

    execution = packet["execution"]
    checkpoint = ROOT / execution["checkpoint"]
    require(checkpoint.exists(), "A391 checkpoint absent")
    require(sha256(checkpoint) == execution["checkpoint_sha256"], "A391 checkpoint stale")
    for label, record in packet["authority"].items():
        path = ROOT / record["path"]
        require(path.exists(), f"A391 authority absent: {label}")
        require(sha256(path) == record["sha256"], f"A391 authority stale: {label}")

    comparison = packet["comparison_to_A379"]
    beta_factor = float(np.max(sbr)) / float(np.max(br))
    hessian_factor = float(np.max(shr)) / float(np.max(hr))
    require(math.isclose(float(comparison["beta_radius_tightening_factor"]), beta_factor, rel_tol=2.0e-15), "beta factor does not replay")
    require(math.isclose(float(comparison["Hessian_radius_tightening_factor"]), hessian_factor, rel_tol=2.0e-15), "Hessian factor does not replay")
    both_tighter = beta_factor > 1.0 and hessian_factor > 1.0
    require(comparison["both_maximum_radii_tighter_than_A379"] is both_tighter, "tightening decision changed")
    scope = packet["strict_scope"]
    require(scope["A390H_selected_branch_homotopy_consumed"] is True, "A390H consumption lost")
    require(scope["left_upper_route_beta_Hessian_interval_executed"] is True, "route execution lost")
    require(scope["both_maximum_radii_tighter_than_A379"] is both_tighter, "scope tightening decision changed")
    for key in ("interval_Newton_existence_and_uniqueness_closed", "covariant_zero_proved", "full_SM_closure_proved"):
        require(scope[key] is False, f"A391 overclaims {key}")
    print("PASS: A391 replays the certified selected-branch beta/Hessian route")
    print(f"beta-radius tightening factor: {beta_factor:.12g}")
    print(f"Hessian-radius tightening factor: {hessian_factor:.12g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
