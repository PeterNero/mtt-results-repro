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
VALIDATED = PROBE / "validated_transport"
PACKET = VALIDATED / "n3.certified6.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedSixFullResidueRecomposition_A233_v1.md"


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
    require(PACKET.exists(), "missing A233 packet")
    require(NOTE.exists(), "missing A233 note")
    packet = load(PACKET)
    require(packet["artifact"] == "A233", "A233 artifact label changed")
    require(
        packet["status"] == "N3_SIX_TARGET_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A233 status changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A233 authority {name}")
        require(sha256(path) == row["sha256"], f"stale A233 authority {name}")

    a230 = load(ROOT / packet["authority"]["A230_dominant_five"]["path"])
    d085 = load(ROOT / packet["authority"]["A232_d085_full_interval"]["path"])
    radii = []
    distances = []
    for residue_index, stored in enumerate(packet["residue_rows"]):
        base = a230["residue_rows"][residue_index]
        addition = d085["residue_rows"][residue_index]
        center = complex_value(base["dominant_five_interval_center"]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base["dominant_five_interval_radius_upper"]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(
            base["floating_dominant_five_center_diagnostic_only"]
        ) - complex_value(addition["floating_value_diagnostic_only"])
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["certified_six_interval_center"]) - center)
            < 1.0e-14,
            "A233 center replay failed",
        )
        require(
            abs(float(stored["certified_six_interval_radius_upper"]) - radius)
            < 1.0e-14,
            "A233 radius replay failed",
        )
        require(distance < radius, "A233 floating value escaped interval")
        require(stored["floating_value_contained"], "A233 containment flag changed")
        radii.append(radius)
        distances.append(distance)

    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(int(summary["certified_all_eight_thimble_target_count"]) == 6, "A233 certified count changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 70, "A233 remainder changed")
    require(
        abs(float(summary["product_disk_l2_radius_upper"]) - np.linalg.norm(radii_array))
        < 1.0e-14,
        "A233 L2 radius changed",
    )
    require(
        abs(
            float(summary["minimum_floating_containment_margin"])
            - np.min(radii_array - distances_array)
        )
        < 1.0e-14,
        "A233 containment margin changed",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 70, "A233 frontier count changed")
    require(
        int(frontier["leading_unresolved_target"]["distinguished_index"]) == 82,
        "A233 leading unresolved target changed",
    )
    scope = packet["strict_scope"]
    require(scope["six_target_all_eight_chain_recomposition_closed"], "A233 closure reopened")
    require(not scope["remaining_70_all_eight_thimble_intervals_closed"], "A233 overclaims chain")
    require(not scope["z_chart_all_eight_transport_closed"], "A233 overclaims z chart")
    require(not scope["interval_Jacobian_certificate"], "A233 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A233 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A233 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A233 consumed observed SM values")
    print("q79 A233 certified-six full-residue recomposition audit: PASS")
    print(
        "closed: six exact signed chain balls across eight rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    print("open: d082 z-chart adapter, 70-target remainder, handle/beta intervals, Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
