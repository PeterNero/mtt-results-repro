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
PACKET = PROBE / "validated_transport" / "n3.certified7.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedSevenFullResidueRecomposition_A235_v1.md"


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
    require(PACKET.exists(), "missing A235 packet")
    require(NOTE.exists(), "missing A235 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A235", "A235 artifact changed")
    require(
        packet["status"]
        == "N3_CONTIGUOUS_TOP_SEVEN_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A235 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A235 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A235 authority {name}")
    a233 = load(ROOT / packet["authority"]["A233_certified_six"]["path"])
    d082 = load(ROOT / packet["authority"]["A234_d082_native_z_interval"]["path"])
    radii = []
    distances = []
    for residue_index, stored in enumerate(packet["residue_rows"]):
        base = a233["residue_rows"][residue_index]
        addition = d082["residue_rows"][residue_index]
        center = complex_value(base["certified_six_interval_center"]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base["certified_six_interval_radius_upper"]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(
            base["floating_certified_six_center_diagnostic_only"]
        ) - 2 * complex_value(addition["floating_value_diagnostic_only"])
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["certified_seven_interval_center"]) - center)
            < 1.0e-14,
            "A235 center replay failed",
        )
        require(
            abs(float(stored["certified_seven_interval_radius_upper"]) - radius)
            < 1.0e-14,
            "A235 radius replay failed",
        )
        require(distance < radius, "A235 floating center escaped interval")
        radii.append(radius)
        distances.append(distance)
    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(int(summary["certified_all_eight_thimble_target_count"]) == 7, "A235 count changed")
    require(int(summary["certified_A219_priority_prefix_length"]) == 7, "A235 prefix changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 69, "A235 remainder changed")
    require(
        abs(float(summary["product_disk_l2_radius_upper"]) - np.linalg.norm(radii_array))
        < 1.0e-14,
        "A235 L2 radius changed",
    )
    require(
        abs(
            float(summary["minimum_floating_containment_margin"])
            - np.min(radii_array - distances_array)
        )
        < 1.0e-14,
        "A235 containment margin changed",
    )
    targets = packet["certified_targets_in_A219_priority_order"]
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == list(range(1, 8)),
        "A235 priority prefix is not contiguous",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 69, "A235 frontier count changed")
    require(
        int(frontier["leading_unresolved_target"]["distinguished_index"]) == 21,
        "A235 leading unresolved target changed",
    )
    scope = packet["strict_scope"]
    require(scope["contiguous_top_seven_all_eight_chain_recomposition_closed"], "A235 reopened")
    require(scope["A233_leading_z_chart_target_closed"], "A235 z target reopened")
    require(not scope["remaining_69_all_eight_thimble_intervals_closed"], "A235 overclaims chain")
    require(not scope["interval_Jacobian_certificate"], "A235 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A235 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A235 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A235 consumed observed SM values")
    print("q79 A235 certified-seven full-residue recomposition audit: PASS")
    print(
        "closed: contiguous A219 ranks 1-7 across eight rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    print("open: d021 and 68 successors, moving handle/beta intervals, interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
