from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"
A392 = VALIDATED / "n3.beta.augmented.a392.json"
A393 = VALIDATED / "n3.chain.relation_l1.a393.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
OUTPUT = VALIDATED / "n3.rank3.residual.a394.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourAugmentedBetaResidual_A394_v1.md"
ARTIFACT = "A394"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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


def indexed_rows(packet: dict, key: str) -> dict[int, dict]:
    rows = {int(row["residue_index_zero_based"]): row for row in packet[key]}
    if set(rows) != set(range(8)):
        raise AssertionError(f"{key} does not contain residues 0 through 7")
    return rows


def source_summary(values: np.ndarray) -> dict[str, float]:
    return {
        "maximum_component_radius_upper": float(np.max(values)),
        "product_box_l2_radius_upper": float(np.linalg.norm(values)),
    }


def main() -> int:
    prefix = load(PREFIX)
    a231 = load(A231)
    handle = load(A383)
    old_residual = load(A386)
    beta = load(A392)
    relation = load(A393)
    wall = load(D065)
    if (
        prefix.get("artifact") != "A373"
        or int(prefix["certified_A219_priority_prefix_length"]) != 76
        or not prefix["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A394 requires the final 76-target certified prefix")
    if (
        beta.get("artifact") != "A392"
        or beta.get("status") != "N3_AUGMENTED_13_STATE_BETA_INTERVAL_EXECUTED"
        or not beta["strict_scope"]["full_13_state_affine_error_frame_used"]
        or not beta["strict_scope"]["eight_component_beta_radii_emitted"]
        or not beta["strict_scope"]["strictly_tighter_than_A379"]
        or not authorities_current(beta)
    ):
        raise AssertionError("A392 is absent, stale, or did not tighten A379")
    if (
        handle.get("artifact") != "A383"
        or not handle["strict_scope"]["rank3_handle_Hessian_interval_closed"]
        or not authorities_current(handle)
    ):
        raise AssertionError("A383 handle packet is absent or stale")
    if old_residual.get("artifact") != "A386" or not authorities_current(old_residual):
        raise AssertionError("A386 comparison packet is absent or stale")
    if (
        relation.get("artifact") != "A393"
        or not relation["strict_scope"][
            "unweighted_L1_relation_compression_closed_by_optimality"
        ]
        or not authorities_current(relation)
    ):
        raise AssertionError("A393 relation-compression theorem is absent or stale")

    decomposition = a231["exact_floating_decomposition"]
    wall_index = int(decomposition["PL_crossing_period_distinguished_index"])
    wall_weight = int(decomposition["PL_wall_weight"])
    if wall_index != 65 or wall_weight != 3:
        raise AssertionError("the selected Picard-Lefschetz correction changed")
    if int(wall["selected_target"]["distinguished_index"]) != wall_index:
        raise AssertionError("the d065 wall packet identity changed")

    beta_centers = [complex_value(value) for value in beta["endpoint"]["beta_center"]]
    beta_radii = np.asarray(
        [float(value) for value in beta["endpoint"]["component_radius_uppers"]],
        dtype=np.float64,
    )
    if len(beta_centers) != 8 or beta_radii.shape != (8,):
        raise AssertionError("A392 endpoint does not contain eight beta rows")
    if not bool(np.all(np.isfinite(beta_radii))) or bool(np.any(beta_radii < 0.0)):
        raise AssertionError("A392 emitted invalid beta radii")

    handle_rows = indexed_rows(handle, "handle_rows")
    old_rows = indexed_rows(old_residual, "residue_rows")
    chain_radii = np.zeros(8, dtype=np.float64)
    handle_radii = np.zeros(8, dtype=np.float64)
    wall_radii = np.zeros(8, dtype=np.float64)
    rows = []
    for residue_index in range(8):
        chain_row = prefix["residue_rows"][residue_index]
        handle_row = handle_rows[residue_index]
        wall_row = wall["residue_rows"][residue_index]
        old_row = old_rows[residue_index]

        chain_center = complex_value(chain_row["certified_prefix_interval_center"])
        chain_radius = float(chain_row["certified_prefix_interval_radius_upper"])
        handle_center = complex_value(handle_row["interval_center"])
        handle_radius = float(handle_row["component_radius_upper"])
        wall_center = wall_weight * complex_value(wall_row["full_interval_center"])
        wall_radius = abs(wall_weight) * float(wall_row["full_interval_radius_upper"])
        period_center = chain_center + handle_center + wall_center
        period_radius = chain_radius + handle_radius + wall_radius
        residual_center = beta_centers[residue_index] - period_center
        residual_radius = float(beta_radii[residue_index]) + period_radius
        floating = complex_value(old_row["floating_residual_diagnostic_only"])
        real_difference = abs(floating.real - residual_center.real)
        imaginary_difference = abs(floating.imag - residual_center.imag)
        if max(real_difference, imaginary_difference) > residual_radius:
            raise AssertionError("the floating residual left the A394 interval box")

        chain_radii[residue_index] = chain_radius
        handle_radii[residue_index] = handle_radius
        wall_radii[residue_index] = wall_radius
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "A392_beta_interval_center": encoded_complex(beta_centers[residue_index]),
                "A392_beta_component_radius_upper": float(beta_radii[residue_index]),
                "raw_76_thimble_interval_center": encoded_complex(chain_center),
                "raw_76_thimble_component_radius_upper": chain_radius,
                "A383_rank3_handle_interval_center": encoded_complex(handle_center),
                "A383_rank3_handle_component_radius_upper": handle_radius,
                "PL_wall_correction_interval_center": encoded_complex(wall_center),
                "PL_wall_correction_component_radius_upper": wall_radius,
                "PL_corrected_period_interval_center": encoded_complex(period_center),
                "PL_corrected_period_component_radius_upper": period_radius,
                "residual_interval_center": encoded_complex(residual_center),
                "residual_component_radius_upper": residual_radius,
                "A386_residual_component_radius_upper": float(
                    old_row["residual_component_radius_upper"]
                ),
                "zero_contained_in_residual_box": (
                    abs(residual_center.real) <= residual_radius
                    and abs(residual_center.imag) <= residual_radius
                ),
                "floating_residual_diagnostic_only": encoded_complex(floating),
                "floating_real_center_difference": real_difference,
                "floating_imaginary_center_difference": imaginary_difference,
                "floating_residual_contained": True,
                "floating_containment_margin": residual_radius
                - max(real_difference, imaginary_difference),
            }
        )

    residual_radii = np.asarray(
        [row["residual_component_radius_upper"] for row in rows], dtype=np.float64
    )
    residual_centers = np.asarray(
        [complex_value(row["residual_interval_center"]) for row in rows],
        dtype=np.complex128,
    )
    old_l2 = float(old_residual["summary"]["residual_product_box_l2_radius_upper"])
    new_l2 = float(np.linalg.norm(residual_radii))
    if not new_l2 < old_l2:
        raise AssertionError("A392 does not tighten the recomposed A386 residual")

    source_contributions = {
        "A392_beta": source_summary(beta_radii),
        "raw_76_thimble_chain": source_summary(chain_radii),
        "A383_handle": source_summary(handle_radii),
        "three_times_d065_wall": source_summary(wall_radii),
    }
    dominant_source = max(
        source_contributions,
        key=lambda name: source_contributions[name]["product_box_l2_radius_upper"],
    )
    payload = {
        "schema": "MTTQ79HeightFourAugmentedBetaResidualInterval.v1",
        "status": "N3_AUGMENTED_BETA_EIGHT_RESIDUAL_ROWS_INTERVAL_RECOMPOSED",
        "artifact": ARTIFACT,
        "identity": "R_n3 = beta_A392 - (sum_76 m_I Pi_I + H_A383 + 3 Pi_d065)",
        "residue_rows": rows,
        "summary": {
            "certified_rows": len(rows),
            "maximum_residual_component_radius_upper": float(np.max(residual_radii)),
            "residual_product_box_l2_radius_upper": new_l2,
            "residual_interval_center_l2_norm": float(np.linalg.norm(residual_centers)),
            "A386_residual_product_box_l2_radius_upper": old_l2,
            "A386_to_A394_radius_reduction_factor": old_l2 / new_l2,
            "minimum_floating_containment_margin": min(
                row["floating_containment_margin"] for row in rows
            ),
            "all_floating_residual_diagnostics_contained": True,
            "zero_contained_in_every_residual_component_box": all(
                row["zero_contained_in_residual_box"] for row in rows
            ),
            "source_radius_contributions": source_contributions,
            "dominant_remaining_source_by_l2_radius": dominant_source,
        },
        "authority": {
            "A373_final_76_target_prefix": authority(PREFIX),
            "A231_chain_and_PL_identity": authority(A231),
            "A383_handle_Hessian_and_ordinary_rows": authority(A383),
            "A386_prior_Hessian_aligned_residual": authority(A386),
            "A392_augmented_beta_transport": authority(A392),
            "A393_relation_L1_optimality": authority(A393),
            "d065_full_interval": authority(D065),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "A392_beta_internal_lift_correlations_preserved": True,
            "A383_handle_value_and_Jacobian_source_aligned": True,
            "all_76_target_intervals_closed": True,
            "unweighted_chain_relation_L1_compression_closed_by_A393": True,
            "weighted_chain_radius_optimality_proved": False,
            "residual_interval_strictly_tighter_than_A386": True,
            "beta_period_cross_correlation_preserved": False,
            "coupled_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "feed A394 into the A384 point-Krawczyk scale test; then construct a "
            "coupled beta-period residual enclosure or tighten the reported "
            f"dominant source {dominant_source}"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Augmented-Beta Residual (A394) v1\n\n"
        "A394 replaces the dependency-forgetting A379 beta widths in A386 by the "
        "13-state correlation-preserving A392 beta enclosure. The 76-cycle, "
        "handle, and Picard-Lefschetz wall sources remain unchanged.\n\n"
        f"The residual product-box L2 radius changes from `{old_l2:.12g}` to "
        f"`{new_l2:.12g}`, a factor `{old_l2 / new_l2:.12g}`. The largest "
        f"remaining source in L2 radius is `{dominant_source}`.\n\n"
        "A392 preserves correlations inside the beta flow, but A394 still adds "
        "the beta and period enclosures independently. It therefore does not yet "
        "prove a Krawczyk self-map or a covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
