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
OUTPUT = VALIDATED / "rank3.n3.dominant5.full8.recomposition.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_q79HeightFourDominantFiveFullResidueRecomposition_A230_v1.md"
)
TARGETS = [87, 34, 41, 30, 62]


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


def packet_path(index: int) -> Path:
    return VALIDATED / f"d{index:03d}.n3.full8.refined.json"


def main() -> int:
    boundary = load(BOUNDARY)
    ranked = boundary["difference_decomposition"]["ranked_thimble_contributions"]
    selected = ranked[: len(TARGETS)]
    if [int(row["distinguished_index"]) for row in selected] != TARGETS:
        raise AssertionError("A219 dominant-five order changed")

    packets = []
    target_rows = []
    for boundary_row in selected:
        index = int(boundary_row["distinguished_index"])
        path = packet_path(index)
        packet = load(path)
        target = packet["selected_target"]
        coefficient = int(boundary_row["signed_coefficient"])
        if int(target["distinguished_index"]) != index:
            raise AssertionError(f"d{index:03d} packet index changed")
        if target["root_id"] != boundary_row["root_id"]:
            raise AssertionError(f"d{index:03d} root ID changed")
        if int(target["selected_chain_coefficient"]) != coefficient:
            raise AssertionError(f"d{index:03d} chain coefficient changed")
        if len(packet["residue_rows"]) != 8:
            raise AssertionError(f"d{index:03d} does not contain eight rows")
        packets.append(packet)
        target_rows.append(
            {
                "distinguished_index": index,
                "root_id": target["root_id"],
                "selected_chain_coefficient": coefficient,
                "full_packet": relative(path),
                "full_packet_sha256": sha256(path),
            }
        )

    rows = []
    combined_centers = []
    combined_radii = []
    floating_centers = []
    for residue_index in range(8):
        center = 0.0 + 0.0j
        radius = 0.0
        floating = 0.0 + 0.0j
        components = []
        for packet, target_row in zip(packets, target_rows):
            row = packet["residue_rows"][residue_index]
            coefficient = int(target_row["selected_chain_coefficient"])
            component_center = complex_value(row["selected_chain_contribution_center"])
            component_radius = float(row["selected_chain_contribution_radius_upper"])
            replay_center = coefficient * complex_value(row["full_interval_center"])
            replay_radius = abs(coefficient) * float(row["full_interval_radius_upper"])
            if abs(component_center - replay_center) >= 1.0e-14:
                raise AssertionError("selected-chain component center replay failed")
            if abs(component_radius - replay_radius) >= 1.0e-14:
                raise AssertionError("selected-chain component radius replay failed")
            floating_component = coefficient * complex_value(
                row["floating_value_diagnostic_only"]
            )
            center += component_center
            radius += component_radius
            floating += floating_component
            components.append(
                {
                    "distinguished_index": target_row["distinguished_index"],
                    "root_id": target_row["root_id"],
                    "coefficient": coefficient,
                    "center": encoded_complex(component_center),
                    "radius_upper": component_radius,
                }
            )
        distance = float(abs(floating - center))
        margin = radius - distance
        if margin <= 0.0:
            raise AssertionError("dominant-five floating center escaped interval sum")
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "components": components,
                "dominant_five_interval_center": encoded_complex(center),
                "dominant_five_interval_radius_upper": radius,
                "floating_dominant_five_center_diagnostic_only": encoded_complex(
                    floating
                ),
                "floating_to_interval_center_distance": distance,
                "floating_containment_margin": margin,
                "floating_value_contained": True,
            }
        )
        combined_centers.append(center)
        combined_radii.append(radius)
        floating_centers.append(floating)

    radii = np.asarray(combined_radii, dtype=np.float64)
    distances = np.abs(
        np.asarray(floating_centers, dtype=np.complex128)
        - np.asarray(combined_centers, dtype=np.complex128)
    )
    top_five_fraction = float(
        boundary["difference_decomposition"][
            "top_five_fraction_of_individual_norm_sum"
        ]
    )
    payload = {
        "schema": "MTTQ79HeightFourDominantFiveFullResidueRecomposition.v1",
        "status": "N3_DOMINANT_FIVE_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "artifact": "A230",
        "selected_dominant_targets": target_rows,
        "residue_rows": rows,
        "summary": {
            "certified_target_count": len(TARGETS),
            "certified_residue_row_count": 8,
            "remaining_selected_thimble_count": len(ranked) - len(TARGETS),
            "maximum_coordinate_radius_upper": float(np.max(radii)),
            "product_disk_l2_radius_upper": float(np.linalg.norm(radii)),
            "maximum_floating_center_difference": float(np.max(distances)),
            "minimum_floating_containment_margin": float(
                np.min(radii - distances)
            ),
            "all_floating_dominant_five_values_contained": True,
            "A219_top_five_profile_difference_norm_fraction_diagnostic_only": top_five_fraction,
        },
        "authority": {
            "A219_floating_boundary": {
                "path": relative(BOUNDARY),
                "sha256": sha256(BOUNDARY),
            },
            "builder_source": {
                "path": relative(Path(__file__).resolve()),
                "sha256": sha256(Path(__file__).resolve()),
            },
            **{
                f"d{row['distinguished_index']:03d}_full_interval": {
                    "path": row["full_packet"],
                    "sha256": row["full_packet_sha256"],
                }
                for row in target_rows
            },
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "dominant_five_all_eight_chain_recomposition_closed": True,
            "independent_floating_dominant_five_sum_used_as_bound": False,
            "full_76_thimble_selected_chain_recomposition_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replay the exact rank-3 thimble-plus-handle-plus-PL decomposition, "
            "then certify the 71 remaining all-eight relative-thimble values or "
            "prove a homological compression that actually contains them"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Dominant-Five Full-Residue Recomposition "
        "(A230) v1\n\n"
        "The five A219-prioritized thimbles `d087`, `d034`, `d041`, `d030`, "
        "and `d062` are recomposed with their exact signed integer chain "
        "coefficients in all eight `sl(3)` residue rows. Each component is an "
        "independently certified node/main/tail interval.\n\n"
        f"The maximum coordinate radius is `{np.max(radii):.12g}` and the "
        f"product-disk L2 radius is `{np.linalg.norm(radii):.12g}`. The "
        "independent floating dominant-five sum lies inside every row and is "
        "diagnostic only.\n\n"
        "This is a dominant-five partial-chain certificate, not the full "
        "76-thimble selected chain. A209 certifies E32 primitive-handle columns; "
        "it does not replace the relative-thimble sum. The next exact object is "
        "the full rank-3 decomposition and its 71-target interval frontier. No "
        "interval Jacobian, covariant zero, or full SM closure is claimed.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
