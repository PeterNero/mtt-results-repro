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
PACKET = VALIDATED / "n3.rank3.residual.a386.json"
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A377 = VALIDATED / "n3.rank3.full_residual.interval.json"
A379 = VALIDATED / "n3.beta_hessian.interval.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def indexed_rows(packet: dict, key: str) -> dict[int, dict]:
    return {int(row["residue_index_zero_based"]): row for row in packet[key]}


def main() -> int:
    packet = load(PACKET)
    prefix = load(PREFIX)
    a231 = load(A231)
    a377 = load(A377)
    beta = load(A379)
    handle = load(A383)
    wall = load(D065)
    require(packet["artifact"] == "A386", "A386 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourHessianAlignedResidualInterval.v1",
        "A386 schema changed",
    )
    require(len(packet["residue_rows"]) == 8, "A386 row count changed")
    require(
        int(prefix["certified_A219_priority_prefix_length"]) == 76,
        "A386 lost the 76-target prefix",
    )
    decomposition = a231["exact_floating_decomposition"]
    require(
        int(decomposition["PL_crossing_period_distinguished_index"]) == 65
        and int(decomposition["PL_wall_weight"]) == 3,
        "A386 Picard-Lefschetz correction changed",
    )
    beta_rows = indexed_rows(beta, "beta_rows")
    handle_rows = indexed_rows(handle, "handle_rows")

    centers = []
    radii = []
    for index, row in enumerate(packet["residue_rows"]):
        require(int(row["residue_index_zero_based"]) == index, "A386 rows reordered")
        chain_row = prefix["residue_rows"][index]
        wall_row = wall["residue_rows"][index]
        beta_center = complex_value(beta_rows[index]["interval_center"])
        chain_center = complex_value(chain_row["certified_prefix_interval_center"])
        handle_center = complex_value(handle_rows[index]["interval_center"])
        wall_center = 3 * complex_value(wall_row["full_interval_center"])
        expected_center = beta_center - chain_center - handle_center - wall_center
        expected_radius = (
            float(beta_rows[index]["component_radius_upper"])
            + float(chain_row["certified_prefix_interval_radius_upper"])
            + float(handle_rows[index]["component_radius_upper"])
            + 3 * float(wall_row["full_interval_radius_upper"])
        )
        actual_center = complex_value(row["residual_interval_center"])
        actual_radius = float(row["residual_component_radius_upper"])
        require(abs(actual_center - expected_center) < 2.0e-14, "A386 center does not recompose")
        require(
            math.isclose(actual_radius, expected_radius, rel_tol=2.0e-15, abs_tol=1.0e-300),
            "A386 radius does not recompose",
        )
        floating = complex_value(row["floating_residual_diagnostic_only"])
        require(
            abs(floating.real - actual_center.real) <= actual_radius
            and abs(floating.imag - actual_center.imag) <= actual_radius,
            "A386 floating diagnostic escaped",
        )
        centers.append(actual_center)
        radii.append(actual_radius)

    centers_array = np.asarray(centers, dtype=np.complex128)
    radii_array = np.asarray(radii, dtype=np.float64)
    summary = packet["summary"]
    new_l2 = float(np.linalg.norm(radii_array))
    old_l2 = float(a377["summary"]["residual_product_box_l2_radius_upper"])
    require(new_l2 < old_l2, "A386 does not improve A377")
    checks = {
        "maximum_residual_component_radius_upper": float(np.max(radii_array)),
        "residual_product_box_l2_radius_upper": new_l2,
        "residual_interval_center_l2_norm": float(np.linalg.norm(centers_array)),
        "A377_residual_product_box_l2_radius_upper": old_l2,
        "A377_to_A386_radius_reduction_factor": old_l2 / new_l2,
    }
    for key, expected in checks.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A386 summary does not replay {key}",
        )

    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A386 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A386 authority {name}")
    scope = packet["strict_scope"]
    require(scope["A379_beta_value_and_Jacobian_source_aligned"], "A386 lost A379 alignment")
    require(scope["A383_handle_value_and_Jacobian_source_aligned"], "A386 lost A383 alignment")
    require(scope["residual_interval_strictly_tighter_than_A377"], "A386 tightening gate is false")
    require(scope["independent_component_radii_still_dependency_forgetting"], "A386 hides dependency loss")
    require(not scope["coupled_residual_transport_closed"], "A386 overclaims coupled transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A386 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A386 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A386 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A386")
    print(
        "PASS: A386 independently recomposes the Hessian-aligned rank-3 residual "
        f"and tightens A377 by {old_l2 / new_l2:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
