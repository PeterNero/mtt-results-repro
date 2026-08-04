from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import build_q79_height4_d057_far_cut_chain_recomposition as prior
import build_q79_height4_krawczyk_feasibility_seed as seed


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = prior.VALIDATED
A373 = prior.A373
A383 = prior.A383
A384 = prior.A384
A385S = prior.A385S
A398 = prior.OUTPUT
A397 = prior.A397
A406 = VALIDATED / "far_residue" / "d027.full.a406.json"
D065 = prior.D065
OUTPUT = VALIDATED / "n3.chain.d057d027far.a407.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057D027FarCutChainRecomposition_A407_v1.md"


def main() -> int:
    old_chain = prior.load(A373)
    handle = prior.load(A383)
    jacobian = prior.load(A384)
    chart = prior.load(A385S)
    a398 = prior.load(A398)
    wall = prior.load(D065)
    replacements = {57: (A397, prior.load(A397)), 27: (A406, prior.load(A406))}
    if (
        old_chain.get("artifact") != "A373"
        or int(old_chain["certified_A219_priority_prefix_length"]) != 76
        or not old_chain["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A407 requires the final A373 76-target chain")
    if (
        a398.get("artifact") != "A398"
        or not prior.authorities_current(a398)
        or int(a398["summary"]["next_dominant_target_by_selected_l2_width"]) != 27
    ):
        raise AssertionError("A407 requires the current d057-only A398 state")
    expected_replacements = {
        57: ("A397", "strictly_tighter_than_canonical_A246"),
        27: ("A406", "strictly_tighter_than_canonical_d027"),
    }
    for index, (_path, packet) in replacements.items():
        artifact, gate = expected_replacements[index]
        if packet.get("artifact") != artifact or not packet["strict_scope"][gate]:
            raise AssertionError(f"A407 requires tightened {artifact}")
        if not prior.authorities_current(packet):
            raise AssertionError(f"A407 replacement authority is stale: {artifact}")
    for packet, artifact in ((handle, "A383"), (jacobian, "A384"), (chart, "A385S")):
        if packet.get("artifact") != artifact or not prior.authorities_current(packet):
            raise AssertionError(f"A407 requires a current {artifact} packet")

    target_entries = old_chain["certified_targets_in_A219_priority_order"]
    if len(target_entries) != 76:
        raise AssertionError("A407 target count changed")
    canonical_centers = np.zeros(8, dtype=np.complex128)
    canonical_radii = np.zeros(8, dtype=np.float64)
    d057_centers = np.zeros(8, dtype=np.complex128)
    d057_radii = np.zeros(8, dtype=np.float64)
    selected_centers = np.zeros(8, dtype=np.complex128)
    selected_radii = np.zeros(8, dtype=np.float64)
    manifest = []
    ranking = []
    for expected_rank, entry in enumerate(target_entries, start=1):
        rank = int(entry["A219_profile_priority_rank"])
        index = int(entry["distinguished_index"])
        if rank != expected_rank:
            raise AssertionError("A407 target priority order changed")
        canonical_path = VALIDATED / f"d{index:03d}.n3.full8.refined.json"
        canonical = prior.load(canonical_path)
        canonical_rows = prior.indexed_rows(canonical)
        d057_packet = replacements[57][1] if index == 57 else canonical
        d057_rows = prior.indexed_rows(d057_packet)
        selected_path, selected_packet = replacements.get(index, (canonical_path, canonical))
        selected_rows = prior.indexed_rows(selected_packet)
        target_radii = np.zeros(8, dtype=np.float64)
        canonical_target_radii = np.zeros(8, dtype=np.float64)
        for residue_index in range(8):
            canonical_row = canonical_rows[residue_index]
            d057_row = d057_rows[residue_index]
            selected_row = selected_rows[residue_index]
            canonical_centers[residue_index] += prior.complex_value(
                canonical_row["selected_chain_contribution_center"]
            )
            canonical_radius = float(canonical_row["selected_chain_contribution_radius_upper"])
            canonical_radii[residue_index] += canonical_radius
            canonical_target_radii[residue_index] = canonical_radius
            d057_centers[residue_index] += prior.complex_value(
                d057_row["selected_chain_contribution_center"]
            )
            d057_radii[residue_index] += float(
                d057_row["selected_chain_contribution_radius_upper"]
            )
            selected_centers[residue_index] += prior.complex_value(
                selected_row["selected_chain_contribution_center"]
            )
            selected_radius = float(selected_row["selected_chain_contribution_radius_upper"])
            selected_radii[residue_index] += selected_radius
            target_radii[residue_index] = selected_radius
        manifest.append(
            {
                "A219_profile_priority_rank": rank,
                "distinguished_index": index,
                "selected_packet_path": prior.relative(selected_path),
                "selected_packet_sha256": prior.sha256(selected_path),
                "replacement_artifact": selected_packet.get("artifact") if index in replacements else None,
            }
        )
        ranking.append(
            {
                "A219_profile_priority_rank": rank,
                "distinguished_index": index,
                "selected_chain_product_box_l2_radius_upper": float(np.linalg.norm(target_radii)),
                "maximum_selected_chain_component_radius_upper": float(np.max(target_radii)),
                "canonical_chain_product_box_l2_radius_upper": float(np.linalg.norm(canonical_target_radii)),
            }
        )

    a373_centers = np.asarray(
        [prior.complex_value(row["certified_prefix_interval_center"]) for row in old_chain["residue_rows"]],
        dtype=np.complex128,
    )
    a373_radii = np.asarray(
        [float(row["certified_prefix_interval_radius_upper"]) for row in old_chain["residue_rows"]],
        dtype=np.float64,
    )
    a398_centers = np.asarray(
        [prior.complex_value(row["recomposed_chain_interval_center"]) for row in a398["residue_rows"]],
        dtype=np.complex128,
    )
    a398_radii = np.asarray(
        [float(row["recomposed_chain_interval_radius_upper"]) for row in a398["residue_rows"]],
        dtype=np.float64,
    )
    if float(np.max(abs(canonical_centers - a373_centers))) > 2.0e-14 or not bool(
        np.allclose(canonical_radii, a373_radii, rtol=2.0e-14, atol=1.0e-300)
    ):
        raise AssertionError("A407 canonical reconstruction misses A373")
    if float(np.max(abs(d057_centers - a398_centers))) > 2.0e-14 or not bool(
        np.allclose(d057_radii, a398_radii, rtol=2.0e-14, atol=1.0e-300)
    ):
        raise AssertionError("A407 d057-only reconstruction misses A398")

    rows = []
    floating_distances = []
    for residue_index in range(8):
        floating = prior.complex_value(
            old_chain["residue_rows"][residue_index]["floating_certified_prefix_center_diagnostic_only"]
        )
        distance = float(abs(floating - selected_centers[residue_index]))
        if distance > selected_radii[residue_index]:
            raise AssertionError("A407 floating chain diagnostic escaped")
        floating_distances.append(distance)
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "recomposed_chain_interval_center": prior.encoded_complex(selected_centers[residue_index]),
                "recomposed_chain_interval_radius_upper": float(selected_radii[residue_index]),
                "A398_chain_interval_radius_upper": float(d057_radii[residue_index]),
                "floating_chain_diagnostic_only": prior.encoded_complex(floating),
                "floating_to_recomposed_center_distance": distance,
                "floating_containment_margin": float(selected_radii[residue_index] - distance),
                "floating_value_contained": True,
            }
        )

    handle_rows = {int(row["residue_index_zero_based"]): row for row in handle["handle_rows"]}
    handle_radii = np.asarray(
        [float(handle_rows[index]["component_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    wall_radii = np.asarray(
        [3.0 * float(wall["residue_rows"][index]["full_interval_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    period_radii = selected_radii + handle_radii + wall_radii
    inverse = np.asarray(
        [[prior.complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    defect = np.nextafter(
        np.asarray(
            jacobian["verified_interval_nonsingularity"]["componentwise_preconditioned_defect_upper_8_by_8"],
            dtype=np.float64,
        ),
        math.inf,
    )
    correction_errors = seed.positive_matvec_upper(abs(inverse), np.nextafter(period_radii, math.inf))
    method_radii = seed.scaled_point_radius(np.zeros(8), correction_errors, defect, 1.0)
    method_disk = float(np.max(method_radii))
    method_square = method_disk / math.sqrt(2.0)
    chart_radii = {float(row["coordinate_complex_box"]["real_radius_requested"]) for row in chart["charts"]}
    if len(chart_radii) != 1:
        raise AssertionError("A407 A385S chart radii differ")
    chart_square = chart_radii.pop()
    ranking.sort(key=lambda row: row["selected_chain_product_box_l2_radius_upper"], reverse=True)
    old_l2 = float(np.linalg.norm(d057_radii))
    new_l2 = float(np.linalg.norm(selected_radii))
    if not new_l2 < old_l2:
        raise AssertionError("A407 does not tighten A398")

    payload = {
        "schema": "MTTQ79HeightFourD057D027FarCutChainRecomposition.v1",
        "status": "N3_76_TARGET_CHAIN_RECOMPOSED_WITH_TIGHTER_D057_AND_D027",
        "artifact": "A407",
        "replacements": [
            {"distinguished_index": 57, "canonical_artifact": "A246", "replacement_artifact": "A397"},
            {"distinguished_index": 27, "canonical_artifact": "A246", "replacement_artifact": "A406"},
        ],
        "component_authority_manifest": manifest,
        "residue_rows": rows,
        "period_component_radius_uppers_after_A407": period_radii.tolist(),
        "optimistic_beta_zero_method_coordinate_disk_radii": method_radii.tolist(),
        "remaining_target_width_ranking": ranking,
        "summary": {
            "certified_target_count": 76,
            "A373_chain_product_box_l2_radius_upper": float(np.linalg.norm(canonical_radii)),
            "A398_chain_product_box_l2_radius_upper": old_l2,
            "A407_chain_product_box_l2_radius_upper": new_l2,
            "A398_to_A407_chain_radius_tightening_factor": old_l2 / new_l2,
            "A398_maximum_chain_component_radius_upper": float(np.max(d057_radii)),
            "A407_maximum_chain_component_radius_upper": float(np.max(selected_radii)),
            "minimum_floating_chain_containment_margin": float(
                np.min(selected_radii - np.asarray(floating_distances))
            ),
            "optimistic_beta_zero_method_maximum_complex_disk_radius": method_disk,
            "optimistic_beta_zero_method_equivalent_square_radius": method_square,
            "A385S_square_radius": chart_square,
            "optimistic_method_to_A385S_gap_factor": method_square / chart_square,
            "next_dominant_target_by_selected_l2_width": int(ranking[0]["distinguished_index"]),
            "all_floating_chain_diagnostics_contained": True,
        },
        "authority": {
            "A373_canonical_76_target_chain": prior.authority(A373),
            "A383_handle_interval": prior.authority(A383),
            "A384_point_residual_Jacobian": prior.authority(A384),
            "A385S_selected_polydisk_chart": prior.authority(A385S),
            "A398_d057_only_recomposition": prior.authority(A398),
            "A397_tighter_d057_interval": prior.authority(A397),
            "A406_tighter_d027_interval": prior.authority(A406),
            "d065_wall_interval": prior.authority(D065),
            "A387_numerical_algorithm_source": prior.authority(Path(seed.__file__).resolve()),
            "builder_source": prior.authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_76_selected_chain_coefficients_used": True,
            "only_d057_and_d027_interval_certificates_replaced": True,
            "A398_d057_tightening_preserved": True,
            "all_76_target_interval_authorities_current": True,
            "full_76_target_chain_recomposition_updated": True,
            "strictly_tighter_than_A398": True,
            "beta_period_cross_correlation_preserved": False,
            "lower_bound_on_true_residual_uncertainty_proved": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replace the next dominant target reported by the ranking or consume "
            "the correlated beta-minus-B block in the relative-chain residual"
        ),
    }
    prior.dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d057+d027 Far-Cut Chain Recomposition (A407) v1\n\n"
        "A407 rebuilds all 76 selected chain contributions from their current "
        "authorities. It preserves A397/d057 and additionally replaces canonical "
        "d027 by A406. The reconstruction independently replays both A373 and A398.\n\n"
        f"The chain product-box L2 radius changes from `{old_l2:.12g}` to "
        f"`{new_l2:.12g}`. The independent-box chart gap is "
        f"`{method_square / chart_square:.12g}`; the next target is "
        f"`d{int(ranking[0]['distinguished_index']):03d}`.\n",
        encoding="utf-8",
    )
    print(f"wrote {prior.relative(OUTPUT)}")
    print(f"wrote {prior.relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
