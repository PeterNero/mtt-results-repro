from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from flint import arb


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A402 = VALIDATED / "n3.beta_minus_B.augmented.a402.json"
A407 = VALIDATED / "n3.chain.d057d027far.a407.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A_HANDLE = VALIDATED / "n3.handleA.hessian.checkpoint.json"
B_HANDLE = VALIDATED / "n3.handleB.hessian.checkpoint.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"
PACKET = VALIDATED / "n3.correlated_partial_residual.a408.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def checkpoint_rows(packet: dict) -> tuple[np.ndarray, np.ndarray]:
    centers = np.asarray(
        [validated.midpoint(validated.decoded_acb(value)) for value in packet["center"][5:13]],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [validated.upper(arb(value)) for value in packet["output_radii"][:8]],
        dtype=np.float64,
    )
    return centers, radii


def main() -> int:
    packet = load(PACKET)
    correlated = load(A402)
    chain = load(A407)
    handle = load(A383)
    a_checkpoint = load(A_HANDLE)
    b_checkpoint = load(B_HANDLE)
    wall = load(D065)
    old = load(A386)
    require(packet["artifact"] == "A408", "A408 artifact label changed")
    require(packet["schema"] == "MTTQ79HeightFourCorrelatedPartialResidual.v1", "A408 schema changed")
    require(packet["identity"] == "R_n3=(beta-H_B)-C_76-H_A-3*Pi_d065", "A408 identity changed")
    require(packet["correlation_partition"]["joint_block"] == ["beta", "H_B"], "A408 joint block changed")
    require(not packet["correlation_partition"]["full_common_path_execution_claimed"], "A408 overclaims common transport")

    a_centers, a_radii = checkpoint_rows(a_checkpoint)
    b_centers, b_radii = checkpoint_rows(b_checkpoint)
    handle_centers = np.asarray([complex_value(row["interval_center"]) for row in handle["handle_rows"]])
    handle_radii = np.asarray([float(row["component_radius_upper"]) for row in handle["handle_rows"]])
    require(bool(np.all(abs(a_centers + b_centers - handle_centers) <= a_radii + b_radii + handle_radii)), "A408 handle split misses A383")
    require(bool(np.allclose(a_radii + b_radii, handle_radii, rtol=2.0e-14, atol=1.0e-300)), "A408 handle radius split changed")

    relative_centers = np.asarray([complex_value(value) for value in correlated["endpoint"]["beta_center"]])
    relative_radii = np.asarray(correlated["endpoint"]["component_radius_uppers"], dtype=np.float64)
    chain_centers = np.asarray([complex_value(row["recomposed_chain_interval_center"]) for row in chain["residue_rows"]])
    chain_radii = np.asarray([float(row["recomposed_chain_interval_radius_upper"]) for row in chain["residue_rows"]])
    wall_centers = np.asarray([3.0 * complex_value(row["full_interval_center"]) for row in wall["residue_rows"]])
    wall_radii = np.asarray([3.0 * float(row["full_interval_radius_upper"]) for row in wall["residue_rows"]])
    centers = relative_centers - chain_centers - a_centers - wall_centers
    radii = relative_radii + chain_radii + a_radii + wall_radii
    rows = packet["residue_rows"]
    require(len(rows) == 8, "A408 row count changed")
    stored_centers = np.asarray([complex_value(row["residual_interval_center"]) for row in rows])
    stored_radii = np.asarray([float(row["residual_component_radius_upper"]) for row in rows])
    require(float(np.max(abs(centers - stored_centers))) < 2.0e-14, "A408 centers do not replay")
    require(bool(np.allclose(radii, stored_radii, rtol=2.0e-14, atol=1.0e-300)), "A408 radii do not replay")
    floating = np.asarray([complex_value(row["floating_residual_diagnostic_only"]) for row in old["residue_rows"]])
    distances = abs(floating - centers)
    require(bool(np.all(distances <= radii)), "A408 floating residual escaped")

    old_l2 = float(old["summary"]["residual_product_box_l2_radius_upper"])
    old_maximum = float(old["summary"]["maximum_residual_component_radius_upper"])
    new_l2 = float(np.linalg.norm(radii))
    new_maximum = float(np.max(radii))
    summary = packet["summary"]
    expected = {
        "maximum_residual_component_radius_upper": new_maximum,
        "residual_product_box_l2_radius_upper": new_l2,
        "A386_maximum_residual_component_radius_upper": old_maximum,
        "A386_residual_product_box_l2_radius_upper": old_l2,
        "A386_to_A408_L2_radius_tightening_factor": old_l2 / new_l2,
        "A386_to_A408_maximum_radius_tightening_factor": old_maximum / new_maximum,
        "minimum_floating_containment_margin": float(np.min(radii - distances)),
    }
    for key, value in expected.items():
        require(math.isclose(float(summary[key]), value, rel_tol=2.0e-14, abs_tol=1.0e-300), f"A408 summary changed: {key}")
    require(new_l2 < old_l2 and new_maximum < old_maximum, "A408 does not tighten A386")
    require(summary["all_floating_residual_diagnostics_contained"], "A408 containment summary false")

    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A408 authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A408 authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "exact_relative_chain_identity_consumed",
        "beta_minus_B_cross_correlation_preserved",
        "current_A407_chain_consumed",
        "A_handle_extracted_from_A383_same_source_checkpoint",
        "A_handle_chain_wall_combined_by_independent_Minkowski_sum",
        "all_eight_endpoint_residual_rows_interval_closed",
        "strictly_tighter_than_A386",
    ):
        require(scope[key], f"A408 strict gate false: {key}")
    require(not scope["full_common_relative_chain_transport_executed"], "A408 overclaims common transport")
    require(not scope["full_polydisk_residual_Jacobian_closed"], "A408 overclaims a full Jacobian")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A408 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A408 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A408 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A408")
    print(f"PASS: A408 preserves beta/B correlation and tightens A386 L2 by {old_l2 / new_l2:.6g}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
