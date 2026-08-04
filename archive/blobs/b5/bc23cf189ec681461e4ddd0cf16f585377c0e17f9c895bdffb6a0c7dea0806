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
PACKET = PROBE / "validated_transport" / "n3.certified13.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedThirteenFullResidueRecomposition_A247_v1.md"
EXPECTED_TARGETS = (87, 34, 41, 30, 62, 82, 85, 21, 47, 79, 28, 15, 57)


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
    require(PACKET.exists(), "missing A247 packet")
    require(NOTE.exists(), "missing A247 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A247", "A247 artifact changed")
    require(
        packet["status"]
        == "N3_CONTIGUOUS_TOP_THIRTEEN_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A247 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A247 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A247 authority {name}")

    a245 = load(ROOT / packet["authority"]["A245_certified_twelve"]["path"])
    d057 = load(ROOT / packet["authority"]["A246_d057_interval"]["path"])
    coefficient = int(d057["selected_target"]["selected_chain_coefficient"])
    require(coefficient == 4, "A247 d057 coefficient changed")
    require(
        d057["strict_scope"]["certified_nodal_pair_selector_consumed"],
        "A247 d057 lost nodal-pair provenance",
    )
    require(
        not d057["strict_scope"]["instantaneous_closest_pair_rule_used"],
        "A247 d057 used instantaneous pair selection",
    )

    radii = []
    distances = []
    for residue_index, stored in enumerate(packet["residue_rows"]):
        base = a245["residue_rows"][residue_index]
        addition = d057["residue_rows"][residue_index]
        center = complex_value(base["certified_twelve_interval_center"]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base["certified_twelve_interval_radius_upper"]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(
            base["floating_certified_twelve_center_diagnostic_only"]
        ) + coefficient * complex_value(addition["floating_value_diagnostic_only"])
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["certified_thirteen_interval_center"]) - center)
            < 1.0e-14,
            "A247 center replay failed",
        )
        require(
            abs(float(stored["certified_thirteen_interval_radius_upper"]) - radius)
            < 1.0e-14,
            "A247 radius replay failed",
        )
        require(
            abs(
                complex_value(stored["floating_certified_thirteen_center_diagnostic_only"])
                - floating
            )
            < 1.0e-14,
            "A247 floating diagnostic replay failed",
        )
        require(distance < radius, "A247 floating center escaped interval")
        radii.append(radius)
        distances.append(distance)

    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(int(summary["certified_all_eight_thimble_target_count"]) == 13, "A247 count changed")
    require(int(summary["certified_A219_priority_prefix_length"]) == 13, "A247 prefix changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 63, "A247 remainder changed")
    require(
        abs(float(summary["product_disk_l2_radius_upper"]) - np.linalg.norm(radii_array))
        < 1.0e-14,
        "A247 L2 radius changed",
    )
    require(
        abs(
            float(summary["minimum_floating_containment_margin"])
            - np.min(radii_array - distances_array)
        )
        < 1.0e-14,
        "A247 containment margin changed",
    )
    require(
        summary["all_floating_certified_thirteen_values_contained"],
        "A247 lost floating containment",
    )

    targets = packet["certified_targets_in_A219_priority_order"]
    require(
        tuple(int(row["distinguished_index"]) for row in targets) == EXPECTED_TARGETS,
        "A247 certified target prefix changed",
    )
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == list(range(1, 14)),
        "A247 priority prefix is not contiguous",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 63, "A247 frontier count changed")
    require(
        int(frontier["leading_unresolved_target"]["distinguished_index"]) == 32,
        "A247 leading unresolved target changed",
    )
    require(
        int(frontier["leading_unresolved_target"]["raw_signed_coefficient"]) == -3,
        "A247 d032 signed coefficient changed",
    )
    scope = packet["strict_scope"]
    require(scope["contiguous_top_thirteen_all_eight_chain_recomposition_closed"], "A247 reopened")
    require(not scope["remaining_63_all_eight_thimble_intervals_closed"], "A247 overclaims chain")
    require(not scope["interval_Jacobian_certificate"], "A247 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A247 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A247 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A247 consumed observed SM values")
    note = NOTE.read_text(encoding="utf-8")
    require("d032` at A219 rank 14" in note, "A247 note lost exact frontier")
    print("q79 A247 certified-thirteen full-residue recomposition audit: PASS")
    print(
        "closed: contiguous A219 ranks 1-13 across eight rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    print("open: d032 and 62 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
