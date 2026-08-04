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
BOUNDARY = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
PACKET = VALIDATED / "rank3.n3.dominant5.full8.recomposition.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_q79HeightFourDominantFiveFullResidueRecomposition_A230_v1.md"
)
TARGETS = [87, 34, 41, 30, 62]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def close(left: float, right: float, tolerance: float = 1.0e-14) -> bool:
    return abs(float(left) - float(right)) <= tolerance * max(
        1.0, abs(float(left)), abs(float(right))
    )


def main() -> int:
    require(PACKET.exists(), "missing A230 packet")
    require(NOTE.exists(), "missing A230 note")
    packet = load(PACKET)
    boundary = load(BOUNDARY)
    require(packet["artifact"] == "A230", "A230 artifact label changed")
    require(
        packet["status"] == "N3_DOMINANT_FIVE_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "A230 status changed",
    )
    for name, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"missing A230 authority {name}")
        require(sha256(path) == authority["sha256"], f"stale A230 authority {name}")

    ranked = boundary["difference_decomposition"]["ranked_thimble_contributions"]
    require(
        [int(row["distinguished_index"]) for row in ranked[:5]] == TARGETS,
        "A230/A219 target order changed",
    )
    targets = packet["selected_dominant_targets"]
    require(
        [int(row["distinguished_index"]) for row in targets] == TARGETS,
        "A230 target order changed",
    )
    full_packets = []
    for selected, target in zip(ranked[:5], targets):
        require(target["root_id"] == selected["root_id"], "A230 root ID changed")
        require(
            int(target["selected_chain_coefficient"])
            == int(selected["signed_coefficient"]),
            "A230 chain coefficient changed",
        )
        path = ROOT / target["full_packet"]
        require(sha256(path) == target["full_packet_sha256"], "A230 target hash changed")
        full_packets.append(load(path))

    radii = []
    distances = []
    rows = packet["residue_rows"]
    require(len(rows) == 8, "A230 row count changed")
    for residue_index, stored in enumerate(rows):
        require(
            int(stored["residue_index_zero_based"]) == residue_index,
            "A230 residue ordering changed",
        )
        center = 0.0 + 0.0j
        radius = 0.0
        floating = 0.0 + 0.0j
        for component, source, target in zip(
            stored["components"], full_packets, targets
        ):
            row = source["residue_rows"][residue_index]
            coefficient = int(target["selected_chain_coefficient"])
            source_center = complex_value(row["selected_chain_contribution_center"])
            source_radius = float(row["selected_chain_contribution_radius_upper"])
            require(
                int(component["distinguished_index"])
                == int(target["distinguished_index"]),
                "A230 component index changed",
            )
            require(
                abs(complex_value(component["center"]) - source_center) < 1.0e-14,
                "A230 component center changed",
            )
            require(
                close(component["radius_upper"], source_radius),
                "A230 component radius changed",
            )
            center += source_center
            radius += source_radius
            floating += coefficient * complex_value(
                row["floating_value_diagnostic_only"]
            )
        distance = float(abs(floating - center))
        require(
            abs(complex_value(stored["dominant_five_interval_center"]) - center)
            < 1.0e-14,
            "A230 recomposed center changed",
        )
        require(
            close(stored["dominant_five_interval_radius_upper"], radius),
            "A230 recomposed radius changed",
        )
        require(
            abs(
                complex_value(stored["floating_dominant_five_center_diagnostic_only"])
                - floating
            )
            < 1.0e-14,
            "A230 floating sum changed",
        )
        require(distance < radius, "A230 floating sum escaped interval")
        require(stored["floating_value_contained"], "A230 containment flag changed")
        radii.append(radius)
        distances.append(distance)

    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    summary = packet["summary"]
    require(summary["certified_target_count"] == 5, "A230 target count changed")
    require(summary["certified_residue_row_count"] == 8, "A230 residue count changed")
    require(summary["remaining_selected_thimble_count"] == 71, "A230 remainder changed")
    require(
        close(summary["maximum_coordinate_radius_upper"], np.max(radii_array)),
        "A230 maximum radius changed",
    )
    require(
        close(summary["product_disk_l2_radius_upper"], np.linalg.norm(radii_array)),
        "A230 L2 radius changed",
    )
    require(
        close(
            summary["minimum_floating_containment_margin"],
            np.min(radii_array - distances_array),
        ),
        "A230 containment margin changed",
    )
    scope = packet["strict_scope"]
    require(scope["dominant_five_all_eight_chain_recomposition_closed"], "A230 closure reopened")
    require(not scope["full_76_thimble_selected_chain_recomposition_closed"], "A230 overclaims full chain")
    require(not scope["interval_Jacobian_certificate"], "A230 overclaims Jacobian")
    require(not scope["covariant_zero_proved"], "A230 overclaims zero")
    require(not scope["full_SM_closure_proved"], "A230 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "A230 consumed observed SM values")
    print("q79 A230 dominant-five full-residue recomposition audit: PASS")
    print(
        "closed: five exact signed chain balls across eight sl3 rows; "
        f"L2 radius={np.linalg.norm(radii_array):.6e}"
    )
    note = NOTE.read_text(encoding="utf-8")
    require(
        "A209 certifies E32 primitive-handle columns" in note,
        "A230 note retains the invalid full-chain shortcut",
    )
    print("open: 71 all-eight thimble values, moving handle/beta blocks, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
