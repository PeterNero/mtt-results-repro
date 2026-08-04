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
A373 = VALIDATED / "n3.certified76.recomposition.json"
A398 = VALIDATED / "n3.chain.d057far.a398.json"
A397 = VALIDATED / "far_residue" / "d057.full.a397.json"
A406 = VALIDATED / "far_residue" / "d027.full.a406.json"
PACKET = VALIDATED / "n3.chain.d057d027far.a407.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def indexed_rows(packet: dict) -> dict[int, dict]:
    rows = {int(row["residue_index_zero_based"]): row for row in packet["residue_rows"]}
    require(set(rows) == set(range(8)), "A407 source row set changed")
    return rows


def main() -> int:
    packet = load(PACKET)
    a373 = load(A373)
    a398 = load(A398)
    replacements = {57: load(A397), 27: load(A406)}
    require(packet["artifact"] == "A407", "A407 artifact label changed")
    require(packet["schema"] == "MTTQ79HeightFourD057D027FarCutChainRecomposition.v1", "A407 schema changed")
    require(packet["status"] == "N3_76_TARGET_CHAIN_RECOMPOSED_WITH_TIGHTER_D057_AND_D027", "A407 status changed")
    require(replacements[57]["artifact"] == "A397", "A407 d057 source changed")
    require(replacements[27]["artifact"] == "A406", "A407 d027 source changed")

    centers = np.zeros(8, dtype=np.complex128)
    radii = np.zeros(8, dtype=np.float64)
    manifest = packet["component_authority_manifest"]
    targets = a373["certified_targets_in_A219_priority_order"]
    require(len(manifest) == len(targets) == 76, "A407 target count changed")
    for offset, (entry, authority_row) in enumerate(zip(targets, manifest), start=1):
        rank = int(entry["A219_profile_priority_rank"])
        index = int(entry["distinguished_index"])
        require(rank == offset, "A407 target order changed")
        path = VALIDATED / f"d{index:03d}.n3.full8.refined.json"
        selected = replacements.get(index, load(path))
        selected_path = A397 if index == 57 else A406 if index == 27 else path
        require(int(authority_row["A219_profile_priority_rank"]) == rank, "A407 manifest rank changed")
        require(int(authority_row["distinguished_index"]) == index, "A407 manifest target changed")
        require(authority_row["selected_packet_sha256"] == sha256(selected_path), "A407 manifest hash changed")
        rows = indexed_rows(selected)
        for residue_index in range(8):
            centers[residue_index] += complex_value(rows[residue_index]["selected_chain_contribution_center"])
            radii[residue_index] += float(rows[residue_index]["selected_chain_contribution_radius_upper"])

    stored_rows = packet["residue_rows"]
    stored_centers = np.asarray([complex_value(row["recomposed_chain_interval_center"]) for row in stored_rows])
    stored_radii = np.asarray([float(row["recomposed_chain_interval_radius_upper"]) for row in stored_rows])
    require(float(np.max(abs(centers - stored_centers))) < 2.0e-14, "A407 centers do not replay")
    require(bool(np.allclose(radii, stored_radii, rtol=2.0e-14, atol=1.0e-300)), "A407 radii do not replay")
    a398_centers = np.asarray([complex_value(row["recomposed_chain_interval_center"]) for row in a398["residue_rows"]])
    a398_radii = np.asarray([float(row["recomposed_chain_interval_radius_upper"]) for row in a398["residue_rows"]])
    require(float(np.max(abs(centers - a398_centers))) <= float(np.max(radii + a398_radii)), "A407 lost A398 branch consistency")
    old_l2 = float(np.linalg.norm(a398_radii))
    new_l2 = float(np.linalg.norm(radii))
    require(new_l2 < old_l2, "A407 does not tighten A398")
    summary = packet["summary"]
    expected_summary = {
        "A398_chain_product_box_l2_radius_upper": old_l2,
        "A407_chain_product_box_l2_radius_upper": new_l2,
        "A398_to_A407_chain_radius_tightening_factor": old_l2 / new_l2,
        "A398_maximum_chain_component_radius_upper": float(np.max(a398_radii)),
        "A407_maximum_chain_component_radius_upper": float(np.max(radii)),
    }
    for key, expected in expected_summary.items():
        require(math.isclose(float(summary[key]), expected, rel_tol=2.0e-14), f"A407 summary changed: {key}")
    require(int(summary["certified_target_count"]) == 76, "A407 summary target count changed")
    require(summary["all_floating_chain_diagnostics_contained"], "A407 containment summary false")

    for index, row in enumerate(stored_rows):
        require(int(row["residue_index_zero_based"]) == index, "A407 rows reordered")
        floating = complex_value(row["floating_chain_diagnostic_only"])
        distance = abs(floating - stored_centers[index])
        require(distance <= stored_radii[index], f"A407 row {index} floating diagnostic escaped")
        require(row["floating_value_contained"], f"A407 row {index} containment flag false")
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A407 authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A407 authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "same_76_selected_chain_coefficients_used",
        "only_d057_and_d027_interval_certificates_replaced",
        "A398_d057_tightening_preserved",
        "all_76_target_interval_authorities_current",
        "full_76_target_chain_recomposition_updated",
        "strictly_tighter_than_A398",
    ):
        require(scope[key], f"A407 strict gate false: {key}")
    require(not scope["beta_period_cross_correlation_preserved"], "A407 overclaims correlation")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A407 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A407 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A407 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A407")
    print(f"PASS: A407 independently rebuilds all 76 targets and tightens A398 by {old_l2 / new_l2:.6g}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
