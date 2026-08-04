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
A219 = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
A230 = VALIDATED / "rank3.n3.dominant5.full8.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
D085 = VALIDATED / "d085.n3.full8.refined.json"
OUTPUT = VALIDATED / "n3.certified6.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedSixFullResidueRecomposition_A233_v1.md"
TARGETS = (87, 34, 41, 30, 62, 85)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def main() -> int:
    a219 = load(A219)
    a230 = load(A230)
    a231 = load(A231)
    d085 = load(D085)
    if int(d085["selected_target"]["distinguished_index"]) != 85:
        raise AssertionError("A232 target changed")
    if int(d085["selected_target"]["selected_chain_coefficient"]) != -1:
        raise AssertionError("A232 signed coefficient changed")
    if d085["artifact"] != "A232":
        raise AssertionError("A232 artifact changed")

    ranked = a219["difference_decomposition"]["ranked_thimble_contributions"]
    priority = {
        int(row["distinguished_index"]): rank
        for rank, row in enumerate(ranked, start=1)
    }
    if [priority[index] for index in TARGETS] != [1, 2, 3, 4, 5, 7]:
        raise AssertionError("certified-six A219 priority profile changed")

    rows = []
    radii = []
    distances = []
    for residue_index in range(8):
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
        ) + int(d085["selected_target"]["selected_chain_coefficient"]) * complex_value(
            addition["floating_value_diagnostic_only"]
        )
        distance = float(abs(floating - center))
        margin = radius - distance
        if margin <= 0.0:
            raise AssertionError("certified-six floating center escaped interval sum")
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "certified_six_interval_center": encoded_complex(center),
                "certified_six_interval_radius_upper": radius,
                "floating_certified_six_center_diagnostic_only": encoded_complex(floating),
                "floating_to_interval_center_distance": distance,
                "floating_containment_margin": margin,
                "floating_value_contained": True,
            }
        )
        radii.append(radius)
        distances.append(distance)

    remaining = [
        row
        for row in a231["remaining_interval_frontier"][
            "targets_in_A219_profile_priority_order"
        ]
        if int(row["distinguished_index"]) != 85
    ]
    if len(remaining) != 70:
        raise AssertionError("A233 remaining frontier count changed")
    if int(remaining[0]["distinguished_index"]) != 82:
        raise AssertionError("d082 is no longer the leading unresolved target")
    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    payload = {
        "schema": "MTTQ79HeightFourCertifiedSixFullResidueRecomposition.v1",
        "status": "N3_SIX_TARGET_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "artifact": "A233",
        "certified_targets": [
            {
                "distinguished_index": index,
                "A219_profile_priority_rank": priority[index],
            }
            for index in TARGETS
        ],
        "residue_rows": rows,
        "remaining_interval_frontier": {
            "target_count": len(remaining),
            "leading_unresolved_target": remaining[0],
            "targets_in_A219_profile_priority_order": remaining,
            "leading_target_chart_blocker": (
                "d082 uses the z line chart; the current generic all-eight "
                "certificate is y-chart only"
            ),
        },
        "summary": {
            "certified_all_eight_thimble_target_count": len(TARGETS),
            "remaining_all_eight_thimble_target_count": len(remaining),
            "maximum_coordinate_radius_upper": float(np.max(radii_array)),
            "product_disk_l2_radius_upper": float(np.linalg.norm(radii_array)),
            "maximum_floating_center_difference": float(np.max(distances_array)),
            "minimum_floating_containment_margin": float(
                np.min(radii_array - distances_array)
            ),
            "all_floating_certified_six_values_contained": True,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A219_profile_priority": A219,
                "A230_dominant_five": A230,
                "A231_exact_chain_frontier": A231,
                "A232_d085_full_interval": D085,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "six_target_all_eight_chain_recomposition_closed": True,
            "remaining_70_all_eight_thimble_intervals_closed": False,
            "z_chart_all_eight_transport_closed": False,
            "rank3_handle_combination_interval_closed": False,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "construct the z-chart all-eight covariance adapter and certify "
            "d082 before continuing the exact A219 priority queue"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Certified-Six Full-Residue Recomposition "
        "(A233) v1\n\n"
        "A233 appends the independently certified A232 `d085` ball to the A230 "
        "dominant-five sum in all eight residue rows. The certified support is "
        "now six targets, with A219 priority ranks `[1,2,3,4,5,7]`; rank 6 "
        "(`d082`) remains open because it is a z-chart target.\n\n"
        f"The maximum coordinate radius is `{np.max(radii_array):.12g}` and the "
        f"product-disk L2 radius is `{np.linalg.norm(radii_array):.12g}`. All "
        "six-target floating centers lie inside their certified sums. The exact "
        f"A231 remainder is reduced from 71 to `{len(remaining)}` targets.\n\n"
        "This closes only the six-target partial interval sum. It does not "
        "certify the z-chart adapter, the full chain, moving handle/beta blocks, "
        "an interval Jacobian, a covariant zero, or full SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
