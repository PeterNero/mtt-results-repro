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
PACKET = VALIDATED / "n3.rank3.residual.a394.json"
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"
A392 = VALIDATED / "n3.beta.augmented.a392.json"
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
    rows = {int(row["residue_index_zero_based"]): row for row in packet[key]}
    require(set(rows) == set(range(8)), f"{key} row indices changed")
    return rows


def main() -> int:
    packet = load(PACKET)
    prefix = load(PREFIX)
    a231 = load(A231)
    handle = load(A383)
    old_residual = load(A386)
    beta = load(A392)
    wall = load(D065)
    require(packet["artifact"] == "A394", "A394 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourAugmentedBetaResidualInterval.v1",
        "A394 schema changed",
    )
    require(len(packet["residue_rows"]) == 8, "A394 row count changed")
    require(
        int(prefix["certified_A219_priority_prefix_length"]) == 76,
        "A394 lost the 76-target prefix",
    )
    decomposition = a231["exact_floating_decomposition"]
    require(
        int(decomposition["PL_crossing_period_distinguished_index"]) == 65
        and int(decomposition["PL_wall_weight"]) == 3,
        "A394 Picard-Lefschetz correction changed",
    )
    beta_centers = [complex_value(value) for value in beta["endpoint"]["beta_center"]]
    beta_radii = np.asarray(
        [float(value) for value in beta["endpoint"]["component_radius_uppers"]],
        dtype=np.float64,
    )
    handle_rows = indexed_rows(handle, "handle_rows")
    old_rows = indexed_rows(old_residual, "residue_rows")
    centers = []
    radii = []
    source_radii = {
        "A392_beta": [],
        "raw_76_thimble_chain": [],
        "A383_handle": [],
        "three_times_d065_wall": [],
    }
    for index, row in enumerate(packet["residue_rows"]):
        require(int(row["residue_index_zero_based"]) == index, "A394 rows reordered")
        chain_row = prefix["residue_rows"][index]
        handle_row = handle_rows[index]
        wall_row = wall["residue_rows"][index]
        chain_center = complex_value(chain_row["certified_prefix_interval_center"])
        handle_center = complex_value(handle_row["interval_center"])
        wall_center = 3 * complex_value(wall_row["full_interval_center"])
        expected_center = beta_centers[index] - chain_center - handle_center - wall_center
        chain_radius = float(chain_row["certified_prefix_interval_radius_upper"])
        handle_radius = float(handle_row["component_radius_upper"])
        wall_radius = 3 * float(wall_row["full_interval_radius_upper"])
        expected_radius = float(beta_radii[index]) + chain_radius + handle_radius + wall_radius
        actual_center = complex_value(row["residual_interval_center"])
        actual_radius = float(row["residual_component_radius_upper"])
        require(abs(actual_center - expected_center) < 2.0e-14, "A394 center does not recompose")
        require(
            math.isclose(actual_radius, expected_radius, rel_tol=2.0e-15, abs_tol=1.0e-300),
            "A394 radius does not recompose",
        )
        floating = complex_value(row["floating_residual_diagnostic_only"])
        require(
            abs(floating.real - actual_center.real) <= actual_radius
            and abs(floating.imag - actual_center.imag) <= actual_radius,
            "A394 floating diagnostic escaped",
        )
        centers.append(actual_center)
        radii.append(actual_radius)
        source_radii["A392_beta"].append(float(beta_radii[index]))
        source_radii["raw_76_thimble_chain"].append(chain_radius)
        source_radii["A383_handle"].append(handle_radius)
        source_radii["three_times_d065_wall"].append(wall_radius)

    centers_array = np.asarray(centers, dtype=np.complex128)
    radii_array = np.asarray(radii, dtype=np.float64)
    summary = packet["summary"]
    new_l2 = float(np.linalg.norm(radii_array))
    old_l2 = float(old_residual["summary"]["residual_product_box_l2_radius_upper"])
    require(new_l2 < old_l2, "A394 does not improve A386")
    replay = {
        "maximum_residual_component_radius_upper": float(np.max(radii_array)),
        "residual_product_box_l2_radius_upper": new_l2,
        "residual_interval_center_l2_norm": float(np.linalg.norm(centers_array)),
        "A386_residual_product_box_l2_radius_upper": old_l2,
        "A386_to_A394_radius_reduction_factor": old_l2 / new_l2,
    }
    for key, expected in replay.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A394 summary does not replay {key}",
        )
    contribution_replay = {}
    for name, values in source_radii.items():
        array = np.asarray(values, dtype=np.float64)
        contribution_replay[name] = {
            "maximum_component_radius_upper": float(np.max(array)),
            "product_box_l2_radius_upper": float(np.linalg.norm(array)),
        }
        for key, expected in contribution_replay[name].items():
            require(
                math.isclose(
                    float(summary["source_radius_contributions"][name][key]),
                    expected,
                    rel_tol=2.0e-14,
                    abs_tol=1.0e-300,
                ),
                f"A394 source contribution does not replay {name}.{key}",
            )
    dominant = max(
        contribution_replay,
        key=lambda name: contribution_replay[name]["product_box_l2_radius_upper"],
    )
    require(
        summary["dominant_remaining_source_by_l2_radius"] == dominant,
        "A394 dominant remaining source changed",
    )
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A394 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A394 authority {name}")
    scope = packet["strict_scope"]
    require(scope["A392_beta_internal_lift_correlations_preserved"], "A394 lost A392 correlation")
    require(scope["residual_interval_strictly_tighter_than_A386"], "A394 tightening gate is false")
    require(not scope["beta_period_cross_correlation_preserved"], "A394 overclaims beta-period correlation")
    require(not scope["coupled_residual_transport_closed"], "A394 overclaims coupled transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A394 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A394 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A394 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A394")
    print(
        "PASS: A394 independently recomposes the augmented-beta residual, "
        f"tightens A386 by {old_l2 / new_l2:.6g}x, and identifies {dominant} "
        "as the remaining L2-width leader"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
