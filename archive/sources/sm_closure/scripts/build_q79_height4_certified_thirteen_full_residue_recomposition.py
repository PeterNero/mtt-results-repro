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
A245 = VALIDATED / "n3.certified12.recomposition.json"
D057 = VALIDATED / "d057.n3.full8.refined.json"
OUTPUT = VALIDATED / "n3.certified13.recomposition.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCertifiedThirteenFullResidueRecomposition_A247_v1.md"
TARGETS = (87, 34, 41, 30, 62, 82, 85, 21, 47, 79, 28, 15, 57)


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
    a245 = load(A245)
    d057 = load(D057)
    selected = d057["selected_target"]
    if (
        d057["artifact"] != "A246"
        or int(selected["distinguished_index"]) != 57
        or selected["root_id"] != "selected_008"
        or selected["line_chart"] != "y"
        or int(selected["selected_chain_coefficient"]) != 4
    ):
        raise AssertionError("A246 d057 identity changed")
    if not d057["strict_scope"]["certified_nodal_pair_selector_consumed"]:
        raise AssertionError("A246 lost certified nodal-pair provenance")
    if d057["strict_scope"]["instantaneous_closest_pair_rule_used"]:
        raise AssertionError("A246 used an instantaneous pair selector")

    ranked = a219["difference_decomposition"]["ranked_thimble_contributions"]
    priority = {
        int(row["distinguished_index"]): rank
        for rank, row in enumerate(ranked, start=1)
    }
    if [priority[index] for index in TARGETS] != list(range(1, 14)):
        raise AssertionError("certified-thirteen A219 ranks are not contiguous")

    coefficient = int(selected["selected_chain_coefficient"])
    rows = []
    radii = []
    distances = []
    for residue_index in range(8):
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
        margin = radius - distance
        if margin <= 0.0:
            raise AssertionError("certified-thirteen floating center escaped interval sum")
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "certified_thirteen_interval_center": encoded_complex(center),
                "certified_thirteen_interval_radius_upper": radius,
                "floating_certified_thirteen_center_diagnostic_only": encoded_complex(
                    floating
                ),
                "floating_to_interval_center_distance": distance,
                "floating_containment_margin": margin,
                "floating_value_contained": True,
            }
        )
        radii.append(radius)
        distances.append(distance)

    remaining = [
        row
        for row in a245["remaining_interval_frontier"][
            "targets_in_A219_profile_priority_order"
        ]
        if int(row["distinguished_index"]) != 57
    ]
    if (
        len(remaining) != 63
        or int(remaining[0]["distinguished_index"]) != 32
        or int(remaining[0]["raw_signed_coefficient"]) != -3
    ):
        raise AssertionError("A247 remaining frontier changed")
    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    payload = {
        "schema": "MTTQ79HeightFourCertifiedThirteenFullResidueRecomposition.v1",
        "status": "N3_CONTIGUOUS_TOP_THIRTEEN_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "artifact": "A247",
        "certified_targets_in_A219_priority_order": [
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
        },
        "summary": {
            "certified_all_eight_thimble_target_count": len(TARGETS),
            "certified_A219_priority_prefix_length": len(TARGETS),
            "remaining_all_eight_thimble_target_count": len(remaining),
            "maximum_coordinate_radius_upper": float(np.max(radii_array)),
            "product_disk_l2_radius_upper": float(np.linalg.norm(radii_array)),
            "maximum_floating_center_difference": float(np.max(distances_array)),
            "minimum_floating_containment_margin": float(
                np.min(radii_array - distances_array)
            ),
            "all_floating_certified_thirteen_values_contained": True,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A219_profile_priority": A219,
                "A245_certified_twelve": A245,
                "A246_d057_interval": D057,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "contiguous_top_thirteen_all_eight_chain_recomposition_closed": True,
            "remaining_63_all_eight_thimble_intervals_closed": False,
            "rank3_handle_combination_interval_closed": False,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "certify d032, the A219 priority-rank-14 target with signed "
            "coefficient minus three, then append it to this exact prefix"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Certified-Thirteen Full-Residue Recomposition "
        "(A247) v1\n\n"
        "A247 appends the A246 `d057` coefficient-plus-four ball to A245. "
        "The certified support is now the contiguous A219 priority prefix 1 "
        "through 13: "
        "`d087,d034,d041,d030,d062,d082,d085,d021,d047,d079,d028,d015,d057`.\n\n"
        f"The maximum coordinate radius is `{np.max(radii_array):.12g}` and the "
        f"product-disk L2 radius is `{np.linalg.norm(radii_array):.12g}`. Every "
        "thirteen-target floating center lies inside the corresponding certified "
        f"sum. The exact remainder is `{len(remaining)}` targets, led by "
        "`d032` at A219 rank 14 with signed coefficient `-3`.\n\n"
        "This closes the contiguous thirteen-target interval prefix, not the "
        "full chain, moving handle/beta intervals, an interval Jacobian, a "
        "covariant zero, or full SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
