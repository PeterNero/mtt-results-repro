from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROBE = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
)
PACKET = PROBE / "validated_transport" / "n3.certified15.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedFifteenFullResidueRecomposition_A251_v1.md"
EXPECTED_TARGETS = (87, 34, 41, 30, 62, 82, 85, 21, 47, 79, 28, 15, 57, 32, 27)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    require(PACKET.exists(), "missing A251 packet")
    require(NOTE.exists(), "missing A251 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A251", "A251 artifact changed")
    require(
        packet["status"]
        == "N3_CONTIGUOUS_TOP_FIFTEEN_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A251 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A251 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A251 authority {name}")

    a249 = load(ROOT / packet["authority"]["A249_certified_fourteen"]["path"])
    d027 = load(ROOT / packet["authority"]["A250_d027_interval"]["path"])
    coefficient = int(d027["selected_target"]["selected_chain_coefficient"])
    require(coefficient == -2, "A251 d027 coefficient changed")
    require(
        d027["strict_scope"]["certified_nodal_pair_selector_consumed"],
        "A251 d027 lost nodal-pair provenance",
    )
    require(
        not d027["strict_scope"]["instantaneous_closest_pair_rule_used"],
        "A251 d027 used instantaneous pair selection",
    )

    radii = []
    distances = []
    for residue_index, stored in enumerate(packet["residue_rows"]):
        base = a249["residue_rows"][residue_index]
        addition = d027["residue_rows"][residue_index]
        center = complex_value(base["certified_fourteen_interval_center"]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base["certified_fourteen_interval_radius_upper"]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(
            base["floating_certified_fourteen_center_diagnostic_only"]
        ) + coefficient * complex_value(addition["floating_value_diagnostic_only"])
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["certified_fifteen_interval_center"]) - center)
            < 1.0e-14,
            "A251 center replay failed",
        )
        require(
            abs(float(stored["certified_fifteen_interval_radius_upper"]) - radius)
            < 1.0e-14,
            "A251 radius replay failed",
        )
        require(
            abs(
                complex_value(stored["floating_certified_fifteen_center_diagnostic_only"])
                - floating
            )
            < 1.0e-14,
            "A251 floating diagnostic replay failed",
        )
        require(distance < radius, "A251 floating center escaped interval")
        radii.append(radius)
        distances.append(distance)

    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(int(summary["certified_all_eight_thimble_target_count"]) == 15, "A251 count changed")
    require(int(summary["certified_A219_priority_prefix_length"]) == 15, "A251 prefix changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 61, "A251 remainder changed")
    require(
        abs(float(summary["product_disk_l2_radius_upper"]) - np.linalg.norm(radii_array))
        < 1.0e-14,
        "A251 L2 radius changed",
    )
    require(
        abs(
            float(summary["minimum_floating_containment_margin"])
            - np.min(radii_array - distances_array)
        )
        < 1.0e-14,
        "A251 containment margin changed",
    )
    require(
        summary["all_floating_certified_fifteen_values_contained"],
        "A251 lost floating containment",
    )
    targets = packet["certified_targets_in_A219_priority_order"]
    require(
        tuple(int(row["distinguished_index"]) for row in targets) == EXPECTED_TARGETS,
        "A251 certified target prefix changed",
    )
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == list(range(1, 16)),
        "A251 priority prefix is not contiguous",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 61, "A251 frontier count changed")
    require(
        int(frontier["leading_unresolved_target"]["distinguished_index"]) == 31,
        "A251 leading unresolved target changed",
    )
    require(
        int(frontier["leading_unresolved_target"]["raw_signed_coefficient"]) == 2,
        "A251 d031 signed coefficient changed",
    )
    scope = packet["strict_scope"]
    require(scope["contiguous_top_fifteen_all_eight_chain_recomposition_closed"], "A251 reopened")
    require(not scope["remaining_61_all_eight_thimble_intervals_closed"], "A251 overclaims chain")
    require(not scope["interval_Jacobian_certificate"], "A251 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A251 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A251 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A251 consumed observed SM values")
    note = NOTE.read_text(encoding="utf-8")
    require("d031` at A219 rank 16" in note, "A251 note lost exact frontier")
    print("q79 A251 certified-fifteen full-residue recomposition audit: PASS")
    print(
        "closed: contiguous A219 ranks 1-15 across eight rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    print("open: d031 and 60 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
