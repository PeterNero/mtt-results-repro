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
PACKET = VALIDATED / "n3.certified.current.recomposition.json"
A251 = VALIDATED / "n3.certified15.recomposition.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def close(left: float, right: float) -> bool:
    return abs(float(left) - float(right)) <= 1.0e-14 * max(
        1.0, abs(float(left)), abs(float(right))
    )


def main() -> int:
    require(PACKET.exists(), "missing dynamic current-prefix packet")
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourDynamicCertifiedPrefixRecomposition.v1",
        "dynamic prefix schema changed",
    )
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing dynamic prefix authority {name}")
        require(sha256(path) == row["sha256"], f"stale dynamic prefix authority {name}")
    rank = int(packet["certified_A219_priority_prefix_length"])
    require(16 <= rank <= 76, "dynamic prefix rank is outside 16..76")
    entries = packet["appended_dynamic_target_intervals"]
    require(
        [int(row["A219_priority_rank"]) for row in entries]
        == list(range(16, rank + 1)),
        "dynamic appended target ranks are not contiguous",
    )

    base = load(A251)
    centers = np.asarray(
        [
            complex_value(row["certified_fifteen_interval_center"])
            for row in base["residue_rows"]
        ],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [
            float(row["certified_fifteen_interval_radius_upper"])
            for row in base["residue_rows"]
        ],
        dtype=np.float64,
    )
    floating = np.asarray(
        [
            complex_value(row["floating_certified_fifteen_center_diagnostic_only"])
            for row in base["residue_rows"]
        ],
        dtype=np.complex128,
    )
    for entry in entries:
        path = ROOT / entry["full_interval_path"]
        require(path.exists(), "missing appended dynamic target interval")
        require(sha256(path) == entry["full_interval_sha256"], "stale appended target interval")
        target = load(path)
        coefficient = int(entry["signed_coefficient"])
        require(
            int(target["selected_target"]["selected_chain_coefficient"])
            == coefficient,
            "dynamic target coefficient changed",
        )
        centers += np.asarray(
            [
                complex_value(row["selected_chain_contribution_center"])
                for row in target["residue_rows"]
            ],
            dtype=np.complex128,
        )
        radii += np.asarray(
            [
                float(row["selected_chain_contribution_radius_upper"])
                for row in target["residue_rows"]
            ],
            dtype=np.float64,
        )
        floating += coefficient * np.asarray(
            [
                complex_value(row["floating_value_diagnostic_only"])
                for row in target["residue_rows"]
            ],
            dtype=np.complex128,
        )

    stored_centers = np.asarray(
        [
            complex_value(row["certified_prefix_interval_center"])
            for row in packet["residue_rows"]
        ],
        dtype=np.complex128,
    )
    stored_radii = np.asarray(
        [
            float(row["certified_prefix_interval_radius_upper"])
            for row in packet["residue_rows"]
        ],
        dtype=np.float64,
    )
    stored_floating = np.asarray(
        [
            complex_value(row["floating_certified_prefix_center_diagnostic_only"])
            for row in packet["residue_rows"]
        ],
        dtype=np.complex128,
    )
    require(np.max(abs(stored_centers - centers)) < 1.0e-14, "dynamic prefix centers failed replay")
    require(np.max(abs(stored_radii - radii)) < 1.0e-14, "dynamic prefix radii failed replay")
    require(np.max(abs(stored_floating - floating)) < 1.0e-14, "dynamic floating replay failed")
    distances = abs(floating - centers)
    require(np.all(distances < radii), "dynamic prefix floating value escaped")
    summary = packet["summary"]
    require(int(summary["certified_A219_priority_prefix_length"]) == rank, "prefix summary rank changed")
    require(int(summary["remaining_all_eight_thimble_target_count"]) == 76 - rank, "prefix remainder changed")
    require(close(summary["maximum_coordinate_radius_upper"], np.max(radii)), "prefix max radius changed")
    require(close(summary["product_disk_l2_radius_upper"], np.linalg.norm(radii)), "prefix L2 radius changed")
    require(
        close(summary["minimum_floating_containment_margin"], np.min(radii - distances)),
        "prefix containment margin changed",
    )
    targets = packet["certified_targets_in_A219_priority_order"]
    require(
        [int(row["A219_profile_priority_rank"]) for row in targets]
        == list(range(1, rank + 1)),
        "dynamic certified target prefix changed",
    )
    frontier = packet["remaining_interval_frontier"]
    require(int(frontier["target_count"]) == 76 - rank, "dynamic frontier count changed")
    if rank < 76:
        require(
            int(frontier["leading_unresolved_target"]["A219_profile_priority_rank"])
            == rank + 1,
            "dynamic leading frontier rank changed",
        )
    scope = packet["strict_scope"]
    require(scope["contiguous_dynamic_prefix_all_eight_chain_recomposition_closed"], "prefix reopened")
    require(scope["all_76_target_intervals_closed"] == (rank == 76), "full-target scope changed")
    require(not scope["interval_Jacobian_certificate"], "prefix overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "prefix overclaims zero")
    require(not scope["full_SM_closure_proved"], "prefix overclaims SM closure")
    require(not scope["observed_SM_values_used"], "prefix consumed observed SM values")
    print("q79 dynamic certified-prefix recomposition audit: PASS")
    print(
        f"closed: contiguous A219 ranks 1-{rank} across eight rows; "
        f"L2 radius={np.linalg.norm(radii):.6e}"
    )
    print(f"open target count: {76 - rank}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
