from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import build_q79_height4_krawczyk_feasibility_seed as seed


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A373 = VALIDATED / "n3.certified76.recomposition.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
A396 = VALIDATED / "n3.beta_floor.a396.json"
A397 = VALIDATED / "far_residue" / "d057.full.a397.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
OUTPUT = VALIDATED / "n3.chain.d057far.a398.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057FarCutChainRecomposition_A398_v1.md"
ARTIFACT = "A398"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def authorities_current(packet: dict) -> bool:
    for row in packet.get("authority", {}).values():
        path = ROOT / row["path"]
        if not path.exists() or sha256(path) != row["sha256"]:
            return False
    return True


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def indexed_rows(packet: dict) -> dict[int, dict]:
    rows = {int(row["residue_index_zero_based"]): row for row in packet["residue_rows"]}
    if set(rows) != set(range(8)):
        raise AssertionError("target packet does not contain residues 0 through 7")
    return rows


def main() -> int:
    old_chain = load(A373)
    handle = load(A383)
    jacobian = load(A384)
    chart = load(A385S)
    old_floor = load(A396)
    replacement = load(A397)
    wall = load(D065)
    if (
        old_chain.get("artifact") != "A373"
        or int(old_chain["certified_A219_priority_prefix_length"]) != 76
        or not old_chain["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A398 requires the final A373 76-target chain")
    if (
        replacement.get("artifact") != "A397"
        or not replacement["strict_scope"]["strictly_tighter_than_canonical_A246"]
        or not authorities_current(replacement)
    ):
        raise AssertionError("A398 requires a current tightened A397 d057 packet")
    for packet, artifact in ((handle, "A383"), (jacobian, "A384"), (chart, "A385S")):
        if packet.get("artifact") != artifact or not authorities_current(packet):
            raise AssertionError(f"A398 requires a current {artifact} packet")
    if old_floor.get("artifact") != "A396" or not authorities_current(old_floor):
        raise AssertionError("A398 requires the current A396 method-floor packet")

    target_entries = old_chain["certified_targets_in_A219_priority_order"]
    if len(target_entries) != 76 or [int(row["A219_profile_priority_rank"]) for row in target_entries] != list(range(1, 77)):
        raise AssertionError("A398 target order changed")
    canonical_centers = np.zeros(8, dtype=np.complex128)
    canonical_radii = np.zeros(8, dtype=np.float64)
    replacement_centers = np.zeros(8, dtype=np.complex128)
    replacement_radii = np.zeros(8, dtype=np.float64)
    component_manifest = []
    contribution_ranking = []
    for entry in target_entries:
        rank = int(entry["A219_profile_priority_rank"])
        index = int(entry["distinguished_index"])
        canonical_path = VALIDATED / f"d{index:03d}.n3.full8.refined.json"
        canonical = load(canonical_path)
        selected = canonical["selected_target"]
        if int(selected["distinguished_index"]) != index:
            raise AssertionError(f"canonical d{index:03d} identity changed")
        canonical_rows = indexed_rows(canonical)
        selected_path = A397 if index == 57 else canonical_path
        selected_packet = replacement if index == 57 else canonical
        selected_rows = indexed_rows(selected_packet)
        canonical_component_radii = np.zeros(8, dtype=np.float64)
        selected_component_radii = np.zeros(8, dtype=np.float64)
        for residue_index in range(8):
            canonical_row = canonical_rows[residue_index]
            selected_row = selected_rows[residue_index]
            canonical_centers[residue_index] += complex_value(
                canonical_row["selected_chain_contribution_center"]
            )
            canonical_radius = float(
                canonical_row["selected_chain_contribution_radius_upper"]
            )
            canonical_radii[residue_index] += canonical_radius
            canonical_component_radii[residue_index] = canonical_radius
            replacement_centers[residue_index] += complex_value(
                selected_row["selected_chain_contribution_center"]
            )
            selected_radius = float(
                selected_row["selected_chain_contribution_radius_upper"]
            )
            replacement_radii[residue_index] += selected_radius
            selected_component_radii[residue_index] = selected_radius
        component_manifest.append(
            {
                "A219_profile_priority_rank": rank,
                "distinguished_index": index,
                "selected_packet_path": relative(selected_path),
                "selected_packet_sha256": sha256(selected_path),
                "canonical_packet_replaced": index == 57,
            }
        )
        contribution_ranking.append(
            {
                "A219_profile_priority_rank": rank,
                "distinguished_index": index,
                "selected_chain_product_box_l2_radius_upper": float(
                    np.linalg.norm(selected_component_radii)
                ),
                "maximum_selected_chain_component_radius_upper": float(
                    np.max(selected_component_radii)
                ),
                "canonical_chain_product_box_l2_radius_upper": float(
                    np.linalg.norm(canonical_component_radii)
                ),
            }
        )

    old_stored_centers = np.asarray(
        [
            complex_value(row["certified_prefix_interval_center"])
            for row in old_chain["residue_rows"]
        ],
        dtype=np.complex128,
    )
    old_stored_radii = np.asarray(
        [
            float(row["certified_prefix_interval_radius_upper"])
            for row in old_chain["residue_rows"]
        ],
        dtype=np.float64,
    )
    if float(np.max(abs(canonical_centers - old_stored_centers))) > 2.0e-14:
        raise AssertionError("A398 canonical center reconstruction does not replay A373")
    if not bool(np.allclose(canonical_radii, old_stored_radii, rtol=2.0e-14, atol=1.0e-300)):
        raise AssertionError("A398 canonical radius reconstruction does not replay A373")

    rows = []
    floating_distances = []
    for residue_index in range(8):
        floating = complex_value(
            old_chain["residue_rows"][residue_index][
                "floating_certified_prefix_center_diagnostic_only"
            ]
        )
        distance = float(abs(floating - replacement_centers[residue_index]))
        if distance > replacement_radii[residue_index]:
            raise AssertionError("A398 floating chain diagnostic escaped")
        floating_distances.append(distance)
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "recomposed_chain_interval_center": encoded_complex(
                    replacement_centers[residue_index]
                ),
                "recomposed_chain_interval_radius_upper": float(
                    replacement_radii[residue_index]
                ),
                "A373_chain_interval_radius_upper": float(
                    canonical_radii[residue_index]
                ),
                "floating_chain_diagnostic_only": encoded_complex(floating),
                "floating_to_recomposed_center_distance": distance,
                "floating_containment_margin": float(
                    replacement_radii[residue_index] - distance
                ),
                "floating_value_contained": True,
            }
        )

    handle_rows = {
        int(row["residue_index_zero_based"]): row for row in handle["handle_rows"]
    }
    handle_radii = np.asarray(
        [float(handle_rows[index]["component_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    wall_radii = np.asarray(
        [3.0 * float(wall["residue_rows"][index]["full_interval_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    period_radii = replacement_radii + handle_radii + wall_radii
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    defect = np.nextafter(
        np.asarray(
            jacobian["verified_interval_nonsingularity"][
                "componentwise_preconditioned_defect_upper_8_by_8"
            ],
            dtype=np.float64,
        ),
        math.inf,
    )
    correction_errors = seed.positive_matvec_upper(
        abs(inverse), np.nextafter(period_radii, math.inf)
    )
    method_radii = seed.scaled_point_radius(
        np.zeros(8, dtype=np.float64), correction_errors, defect, 1.0
    )
    method_disk = float(np.max(method_radii))
    method_square = method_disk / math.sqrt(2.0)
    chart_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    if len(chart_radii) != 1:
        raise AssertionError("A398 A385S chart radii differ")
    chart_square = chart_radii.pop()
    contribution_ranking.sort(
        key=lambda row: row["selected_chain_product_box_l2_radius_upper"],
        reverse=True,
    )
    old_chain_l2 = float(np.linalg.norm(canonical_radii))
    new_chain_l2 = float(np.linalg.norm(replacement_radii))
    if not new_chain_l2 < old_chain_l2:
        raise AssertionError("A398 does not tighten the A373 chain")
    payload = {
        "schema": "MTTQ79HeightFourD057FarCutChainRecomposition.v1",
        "status": "N3_76_TARGET_CHAIN_RECOMPOSED_WITH_TIGHTER_D057",
        "artifact": ARTIFACT,
        "replacement": {
            "distinguished_index": 57,
            "canonical_artifact": "A246",
            "replacement_artifact": "A397",
            "chain_coefficients_changed": False,
            "selected_geometry_changed": False,
        },
        "component_authority_manifest": component_manifest,
        "residue_rows": rows,
        "period_component_radius_uppers_after_A397": period_radii.tolist(),
        "optimistic_beta_zero_method_coordinate_disk_radii": method_radii.tolist(),
        "remaining_target_width_ranking": contribution_ranking,
        "summary": {
            "certified_target_count": 76,
            "A373_chain_product_box_l2_radius_upper": old_chain_l2,
            "A398_chain_product_box_l2_radius_upper": new_chain_l2,
            "A373_to_A398_chain_radius_tightening_factor": old_chain_l2 / new_chain_l2,
            "A373_maximum_chain_component_radius_upper": float(np.max(canonical_radii)),
            "A398_maximum_chain_component_radius_upper": float(np.max(replacement_radii)),
            "minimum_floating_chain_containment_margin": float(
                np.min(replacement_radii - np.asarray(floating_distances))
            ),
            "optimistic_beta_zero_method_maximum_complex_disk_radius": method_disk,
            "optimistic_beta_zero_method_equivalent_square_radius": method_square,
            "A385S_square_radius": chart_square,
            "optimistic_method_to_A385S_gap_factor": method_square / chart_square,
            "A396_pre_A397_method_to_A385S_gap_factor": float(
                old_floor["summary"]["method_floor_to_A385S_square_gap_factor"]
            ),
            "next_dominant_target_by_selected_l2_width": int(
                contribution_ranking[0]["distinguished_index"]
            ),
            "all_floating_chain_diagnostics_contained": True,
        },
        "authority": {
            "A373_canonical_76_target_chain": authority(A373),
            "A383_handle_interval": authority(A383),
            "A384_point_residual_Jacobian": authority(A384),
            "A385S_selected_polydisk_chart": authority(A385S),
            "A396_prior_beta_only_method_floor": authority(A396),
            "A397_tighter_d057_interval": authority(A397),
            "d065_wall_interval": authority(D065),
            "A387_numerical_algorithm_source": authority(Path(seed.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_76_selected_chain_coefficients_used": True,
            "only_d057_interval_certificate_replaced": True,
            "all_76_target_interval_authorities_current": True,
            "full_76_target_chain_recomposition_updated": True,
            "strictly_tighter_than_A373": True,
            "beta_period_cross_correlation_preserved": False,
            "lower_bound_on_true_residual_uncertainty_proved": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replace the next dominant target interval reported by the ranking, "
            "or construct the coupled beta-period residual enclosure"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d057 Far-Cut Chain Recomposition (A398) v1\n\n"
        "A398 rebuilds the selected 76-thimble chain from all 76 current source "
        "packets, replacing only canonical d057/A246 by far-cut d057/A397. No "
        "interval subtraction is used.\n\n"
        f"The chain product-box L2 radius changes from `{old_chain_l2:.12g}` to "
        f"`{new_chain_l2:.12g}`, a factor `{old_chain_l2 / new_chain_l2:.12g}`. "
        f"The optimistic independent-box beta-zero gap to A385S becomes "
        f"`{method_square / chart_square:.12g}`. The next largest target width "
        f"is `d{int(contribution_ranking[0]['distinguished_index']):03d}`.\n\n"
        "The calculation updates the chain enclosure only. It does not preserve "
        "beta-period cross-correlation or prove a Krawczyk self-map.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
