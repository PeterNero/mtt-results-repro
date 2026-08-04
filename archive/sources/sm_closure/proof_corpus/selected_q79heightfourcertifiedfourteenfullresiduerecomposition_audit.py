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
PACKET = PROBE / "validated_transport" / "n3.certified14.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedFourteenFullResidueRecomposition_A249_v1.md"
EXPECTED_TARGETS = (87, 34, 41, 30, 62, 82, 85, 21, 47, 79, 28, 15, 57, 32)


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
    require(PACKET.exists(), "missing A249 packet")
    require(NOTE.exists(), "missing A249 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A249", "A249 artifact changed")
    require(
        packet["status"]
        == "N3_CONTIGUOUS_TOP_FOURTEEN_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A249 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A249 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A249 authority {name}")

    a247 = load(ROOT / packet["authority"]["A247_certified_thirteen"]["path"])
    d032 = load(ROOT / packet["authority"]["A248_d032_interval"]["path"])
    coefficient = int(d032["selected_target"]["selected_chain_coefficient"])
    require(coefficient == -3, "A249 d032 coefficient changed")
    require(
        d032["strict_scope"]["certified_nodal_pair_selector_consumed"],
        "A249 d032 lost nodal-pair provenance",
    )
    require(
        not d032["strict_scope"]["instantaneous_closest_pair_rule_used"],
        "A249 d032 used instantaneous pair selection",
    )

    radii = []
    distances = []
    for residue_index, stored in enumerate(packet["residue_rows"]):
        base = a247["residue_rows"][residue_index]
        addition = d032["residue_rows"][residue_index]
        center = complex_value(base["certified_thirteen_interval_center"]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base["certified_thirteen_interval_radius_upper"]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(
            base["floating_certified_thirteen_center_diagnostic_only"]
        ) + coefficient * complex_value(addition["floating_value_diagnostic_only"])
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["certified_fourteen_interval_center"]) - center)
            < 1.0e-14,
            "A249 center replay failed",
        )
        require(
            abs(float(stored["certified_fourteen_interval_radius_upper"]) - radius)
            < 1.0e-14,
            "A249 radius replay failed",
        )
        require(
            abs(
                complex_value(stored["floating_certified_fourteen_center_diagnostic_only"])
                - floating
            )
            < 1.0e-14,
            "A249 floating diagnostic replay failed",
        )
        require(distance < radius, "A249 floating center escaped interval")
        radii.append(radius)
        distances.append(distance)

    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(int(summary["certified_all_eight_thimble_target_count"]) == 14, "A249 count changed")
    require(int(summary["certified_A219_priority_prefix_length"]) == 14, "A249 prefix changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 62, "A249 remainder changed")
    require(
        abs(float(summary["product_disk_l2_radius_upper"]) - np.linalg.norm(radii_array))
        < 1.0e-14,
        "A249 L2 radius changed",
    )
    require(
        abs(
            float(summary["minimum_floating_containment_margin"])
            - np.min(radii_array - distances_array)
        )
        < 1.0e-14,
        "A249 containment margin changed",
    )
    require(
        summary["all_floating_certified_fourteen_values_contained"],
        "A249 lost floating containment",
    )
    targets = packet["certified_targets_in_A219_priority_order"]
    require(
        tuple(int(row["distinguished_index"]) for row in targets) == EXPECTED_TARGETS,
        "A249 certified target prefix changed",
    )
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == list(range(1, 15)),
        "A249 priority prefix is not contiguous",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 62, "A249 frontier count changed")
    require(
        int(frontier["leading_unresolved_target"]["distinguished_index"]) == 27,
        "A249 leading unresolved target changed",
    )
    require(
        int(frontier["leading_unresolved_target"]["raw_signed_coefficient"]) == -2,
        "A249 d027 signed coefficient changed",
    )
    scope = packet["strict_scope"]
    require(scope["contiguous_top_fourteen_all_eight_chain_recomposition_closed"], "A249 reopened")
    require(not scope["remaining_62_all_eight_thimble_intervals_closed"], "A249 overclaims chain")
    require(not scope["interval_Jacobian_certificate"], "A249 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A249 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A249 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A249 consumed observed SM values")
    note = NOTE.read_text(encoding="utf-8")
    require("d027` at A219 rank 15" in note, "A249 note lost exact frontier")
    print("q79 A249 certified-fourteen full-residue recomposition audit: PASS")
    print(
        "closed: contiguous A219 ranks 1-14 across eight rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    print("open: d027 and 61 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
