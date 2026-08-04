from __future__ import annotations

import argparse
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
A251 = VALIDATED / "n3.certified15.recomposition.json"
MANIFEST = VALIDATED / "n3.dynamic_targets.manifest.json"
CURRENT = VALIDATED / "n3.certified.current.recomposition.json"


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


def previous_fields(rank: int) -> tuple[str, str, str]:
    if rank == 16:
        return (
            "certified_fifteen_interval_center",
            "certified_fifteen_interval_radius_upper",
            "floating_certified_fifteen_center_diagnostic_only",
        )
    return (
        "certified_prefix_interval_center",
        "certified_prefix_interval_radius_upper",
        "floating_certified_prefix_center_diagnostic_only",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, required=True)
    arguments = parser.parse_args()
    rank = arguments.rank
    if not 16 <= rank <= 76:
        raise ValueError("dynamic prefix rank must lie in 16..76")
    artifact = f"A{221 + 2 * rank}"
    previous_path = A251 if rank == 16 else VALIDATED / f"n3.certified{rank - 1}.recomposition.json"
    output = VALIDATED / f"n3.certified{rank}.recomposition.json"
    manifest_snapshot = VALIDATED / f"n3.dynamic_targets.rank{rank:03d}.manifest.json"
    note = (
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourDynamicCertifiedPrefixRank{rank:03d}_{artifact}_v1.md"
    )
    previous = load(previous_path)
    manifest = load(MANIFEST)
    entries = manifest["targets_in_A219_priority_order"]
    if [int(row["A219_priority_rank"]) for row in entries] != list(
        range(16, rank + 1)
    ):
        raise AssertionError("dynamic manifest does not end at requested rank")
    target_entry = entries[-1]
    index = int(target_entry["distinguished_index"])
    target_path = ROOT / target_entry["full_interval_path"]
    if sha256(target_path) != target_entry["full_interval_sha256"]:
        raise AssertionError("dynamic target manifest hash is stale")
    target = load(target_path)
    selected = target["selected_target"]
    coefficient = int(selected["selected_chain_coefficient"])
    if (
        target["artifact"] != target_entry["artifact"]
        or int(selected["distinguished_index"]) != index
        or selected["root_id"] != target_entry["root_id"]
        or selected["line_chart"] != target_entry["line_chart"]
        or coefficient != int(target_entry["signed_coefficient"])
    ):
        raise AssertionError("dynamic target identity changed")

    center_key, radius_key, floating_key = previous_fields(rank)
    rows = []
    radii = []
    distances = []
    for residue_index in range(8):
        base = previous["residue_rows"][residue_index]
        addition = target["residue_rows"][residue_index]
        center = complex_value(base[center_key]) + complex_value(
            addition["selected_chain_contribution_center"]
        )
        radius = float(base[radius_key]) + float(
            addition["selected_chain_contribution_radius_upper"]
        )
        floating = complex_value(base[floating_key]) + coefficient * complex_value(
            addition["floating_value_diagnostic_only"]
        )
        distance = float(abs(floating - center))
        margin = radius - distance
        if margin <= 0.0:
            raise AssertionError("dynamic certified-prefix floating center escaped")
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "certified_prefix_interval_center": encoded_complex(center),
                "certified_prefix_interval_radius_upper": radius,
                "floating_certified_prefix_center_diagnostic_only": encoded_complex(
                    floating
                ),
                "floating_to_interval_center_distance": distance,
                "floating_containment_margin": margin,
                "floating_value_contained": True,
            }
        )
        radii.append(radius)
        distances.append(distance)

    previous_targets = previous["certified_targets_in_A219_priority_order"]
    targets = previous_targets + [
        {
            "distinguished_index": index,
            "A219_profile_priority_rank": rank,
        }
    ]
    if [int(row["A219_profile_priority_rank"]) for row in targets] != list(
        range(1, rank + 1)
    ):
        raise AssertionError("dynamic certified prefix is not contiguous")
    remaining = [
        row
        for row in previous["remaining_interval_frontier"][
            "targets_in_A219_profile_priority_order"
        ]
        if int(row["distinguished_index"]) != index
    ]
    if len(remaining) != 76 - rank:
        raise AssertionError("dynamic remaining-frontier count changed")
    if remaining and int(remaining[0]["A219_profile_priority_rank"]) != rank + 1:
        raise AssertionError("dynamic leading frontier rank changed")

    dump(manifest_snapshot, manifest)
    radii_array = np.asarray(radii, dtype=np.float64)
    distances_array = np.asarray(distances, dtype=np.float64)
    authority_paths = {
        "A219_profile_priority": A219,
        "A251_certified_fifteen_base": A251,
        "previous_certified_prefix": previous_path,
        "appended_target_interval": target_path,
        "dynamic_target_manifest_snapshot": manifest_snapshot,
        "builder_source": Path(__file__).resolve(),
    }
    payload = {
        "schema": "MTTQ79HeightFourDynamicCertifiedPrefixRecomposition.v1",
        "status": "N3_CONTIGUOUS_DYNAMIC_PREFIX_ALL_EIGHT_CHAIN_BALLS_RECOMPOSED",
        "artifact": artifact,
        "certified_A219_priority_prefix_length": rank,
        "certified_targets_in_A219_priority_order": targets,
        "appended_dynamic_target_intervals": entries,
        "residue_rows": rows,
        "remaining_interval_frontier": {
            "target_count": len(remaining),
            "leading_unresolved_target": remaining[0] if remaining else None,
            "targets_in_A219_profile_priority_order": remaining,
        },
        "summary": {
            "certified_all_eight_thimble_target_count": rank,
            "certified_A219_priority_prefix_length": rank,
            "remaining_all_eight_thimble_target_count": len(remaining),
            "maximum_coordinate_radius_upper": float(np.max(radii_array)),
            "product_disk_l2_radius_upper": float(np.linalg.norm(radii_array)),
            "maximum_floating_center_difference": float(np.max(distances_array)),
            "minimum_floating_containment_margin": float(
                np.min(radii_array - distances_array)
            ),
            "all_floating_certified_prefix_values_contained": True,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in authority_paths.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "contiguous_dynamic_prefix_all_eight_chain_recomposition_closed": True,
            "all_76_target_intervals_closed": rank == 76,
            "remaining_target_intervals_closed": rank == 76,
            "rank3_handle_combination_interval_closed": False,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "all 76 target intervals are certified; proceed to moving handle/beta "
            "and interval-Jacobian closure"
            if rank == 76
            else (
                f"certify A219 priority rank {rank + 1}, d"
                f"{int(remaining[0]['distinguished_index']):03d}, then append it"
            )
        ),
    }
    dump(output, payload)
    dump(CURRENT, payload)
    next_text = (
        "none; the target queue is exhausted"
        if not remaining
        else (
            f"d{int(remaining[0]['distinguished_index']):03d} at A219 rank "
            f"{rank + 1} with signed coefficient "
            f"{int(remaining[0]['raw_signed_coefficient']):+d}"
        )
    )
    note.write_text(
        f"# MTT q79 Height-Four Dynamic Certified Prefix Rank {rank} "
        f"({artifact}) v1\n\n"
        f"{artifact} appends `d{index:03d}` to the exact certified A219 prefix. "
        f"The all-eight interval prefix is now `{rank}/76`; `{len(remaining)}` "
        f"targets remain and the next frontier is {next_text}.\n\n"
        f"The maximum coordinate radius is `{np.max(radii_array):.12g}`, the "
        f"product-disk L2 radius is `{np.linalg.norm(radii_array):.12g}`, and "
        f"the minimum floating containment margin is "
        f"`{np.min(radii_array - distances_array):.12g}`. Floating values are "
        "diagnostic only.\n\n"
        "This closes the stated target prefix. Moving handle/beta intervals, "
        "an interval Jacobian, a covariant zero, and full SM closure are not "
        "claimed.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(output)}")
    print(f"wrote {relative(CURRENT)}")
    print(f"wrote {relative(manifest_snapshot)}")
    print(f"wrote {relative(note)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
