from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
THIMBLES = N3.parent / "thimbles"
A219 = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
A230 = VALIDATED / "rank3.n3.dominant5.full8.recomposition.json"
OUTPUT = VALIDATED / "n3.chain.frontier.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourN3ChainDecompositionFrontier_A231_v1.md"
CERTIFIED_TARGETS = (87, 34, 41, 30, 62)


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


def complex_vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def complex_matrix(values: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def encoded_vector(values: np.ndarray) -> list[dict[str, str]]:
    return [encoded_complex(value) for value in values]


def max_error(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.max(abs(left - right)))


def main() -> int:
    a208 = load(A208)
    orientation = load(ORIENTATION)
    n3 = load(N3)
    a219 = load(A219)
    a230 = load(A230)

    candidate = next(
        row
        for row in a208["height_four_candidates"]
        if int(row["A132_objective_rank"]) == 3
    )
    n3_row = next(
        row
        for row in n3["candidate_residuals"]
        if int(row["A132_objective_rank"]) == 3
    )
    chain = candidate["primitive_thimble_chain"]
    if len(chain) != 76 or len({int(row["distinguished_index"]) for row in chain}) != 76:
        raise AssertionError("rank-3 primitive thimble support changed")

    signs = [int(value) for value in orientation["column_signs"]]
    if len(signs) != 90 or any(value not in (-1, 1) for value in signs):
        raise AssertionError("canonical orientation table changed")
    profile_rows = a219["difference_decomposition"]["ranked_thimble_contributions"]
    profile_rank = {
        int(row["distinguished_index"]): rank
        for rank, row in enumerate(profile_rows, start=1)
    }
    if set(profile_rank) != {int(row["distinguished_index"]) for row in chain}:
        raise AssertionError("A219 profile inventory differs from the rank-3 chain")

    thimble_sum = np.zeros(8, dtype=np.complex128)
    coefficient_by_index: dict[int, int] = {}
    signed_by_index: dict[int, int] = {}
    period_by_index: dict[int, np.ndarray] = {}
    cache_authority = []
    rows = []
    for chain_row in chain:
        index = int(chain_row["distinguished_index"])
        coefficient = int(chain_row["coefficient"])
        orientation_sign = signs[index - 1]
        signed_coefficient = coefficient * orientation_sign
        path = THIMBLES / f"t{index:03d}.json"
        packet = load(path)
        period = complex_vector(packet["period_values"])
        if len(period) != 8:
            raise AssertionError(f"d{index:03d} residue-row count changed")
        contribution = signed_coefficient * period
        thimble_sum += contribution
        coefficient_by_index[index] = coefficient
        signed_by_index[index] = signed_coefficient
        period_by_index[index] = period
        cache_authority.append(
            {"distinguished_index": index, "path": relative(path), "sha256": sha256(path)}
        )
        rows.append(
            {
                "distinguished_index": index,
                "root_id": packet["root_id"],
                "chain_coefficient": coefficient,
                "canonical_orientation_sign": orientation_sign,
                "raw_signed_coefficient": signed_coefficient,
                "A219_profile_priority_rank": profile_rank[index],
                "n3_floating_period": encoded_vector(period),
                "raw_chain_contribution": encoded_vector(contribution),
                "raw_chain_contribution_l2_norm": float(np.linalg.norm(contribution)),
            }
        )

    handles = complex_matrix(n3["moving_handles"]["primitive_handle_period_matrix"])
    coordinates = np.asarray(candidate["primitive_handle_coordinates"], dtype=np.int64)
    if handles.shape != (8, 8) or coordinates.shape != (8,):
        raise AssertionError("primitive-handle dimensions changed")
    handle_contribution = handles @ coordinates
    raw_recomposition = thimble_sum + handle_contribution

    # The selected radial wall crossing adds c_64*sigma_64 times moving d065.
    wall_source_index = 64
    wall_period_index = 65
    wall_weight = coefficient_by_index[wall_source_index] * signs[wall_source_index - 1]
    wall_correction = wall_weight * period_by_index[wall_period_index]
    corrected_recomposition = raw_recomposition + wall_correction
    effective_signed = dict(signed_by_index)
    effective_signed[wall_period_index] += wall_weight
    if any(value == 0 for value in effective_signed.values()):
        raise AssertionError("wall correction unexpectedly cancels a support element")
    for row in rows:
        row["PL_corrected_effective_signed_coefficient"] = effective_signed[
            int(row["distinguished_index"])
        ]

    stored_raw = complex_vector(n3_row["raw_moving_period"])
    stored_wall = complex_vector(n3_row["PL_period_correction"])
    stored_corrected = complex_vector(n3_row["PL_corrected_moving_period"])
    stored_residual = complex_vector(n3_row["PL_corrected_residual"])
    raw_error = max_error(raw_recomposition, stored_raw)
    wall_error = max_error(wall_correction, stored_wall)
    corrected_error = max_error(corrected_recomposition, stored_corrected)
    residual_identity_error = max_error(
        corrected_recomposition + stored_residual,
        stored_corrected + stored_residual,
    )
    if max(raw_error, wall_error, corrected_error, residual_identity_error) >= 1.0e-12:
        raise AssertionError("n3 floating decomposition replay failed")

    certified = set(CERTIFIED_TARGETS)
    if [int(row["distinguished_index"]) for row in profile_rows[:5]] != list(
        CERTIFIED_TARGETS
    ):
        raise AssertionError("A219 dominant-five priority changed")
    remaining = [
        row
        for row in sorted(rows, key=lambda item: int(item["A219_profile_priority_rank"]))
        if int(row["distinguished_index"]) not in certified
    ]
    if len(remaining) != 71:
        raise AssertionError("remaining rank-3 target count changed")

    certified_floating = np.zeros(8, dtype=np.complex128)
    for row in rows:
        if int(row["distinguished_index"]) in certified:
            certified_floating += complex_vector(row["raw_chain_contribution"])
    a230_floating = np.asarray(
        [
            complex_value(row["floating_dominant_five_center_diagnostic_only"])
            for row in a230["residue_rows"]
        ],
        dtype=np.complex128,
    )
    a230_error = max_error(certified_floating, a230_floating)
    if a230_error >= 1.0e-12:
        raise AssertionError("A230 dominant-five floating replay failed")

    certified_radii = np.asarray(
        [float(row["dominant_five_interval_radius_upper"]) for row in a230["residue_rows"]],
        dtype=np.float64,
    )
    remaining_manifest = [
        {
            "A219_profile_priority_rank": int(row["A219_profile_priority_rank"]),
            "distinguished_index": int(row["distinguished_index"]),
            "root_id": row["root_id"],
            "chain_coefficient": int(row["chain_coefficient"]),
            "canonical_orientation_sign": int(row["canonical_orientation_sign"]),
            "raw_signed_coefficient": int(row["raw_signed_coefficient"]),
            "PL_corrected_effective_signed_coefficient": int(
                row["PL_corrected_effective_signed_coefficient"]
            ),
            "n3_floating_contribution_l2_norm_diagnostic_only": float(
                row["raw_chain_contribution_l2_norm"]
            ),
        }
        for row in remaining
    ]

    payload = {
        "schema": "MTTQ79HeightFourN3ChainDecompositionFrontier.v1",
        "status": "N3_FULL_FLOATING_CHAIN_IDENTITY_REPLAYED_INTERVAL_FRONTIER_EXACT",
        "artifact": "A231",
        "selected_candidate": {
            "candidate_id": candidate["candidate_id"],
            "A132_objective_rank": 3,
            "primitive_handle_coordinates": coordinates.astype(int).tolist(),
        },
        "exact_floating_decomposition": {
            "raw_thimble_sum": encoded_vector(thimble_sum),
            "primitive_handle_contribution": encoded_vector(handle_contribution),
            "raw_moving_period_recomposition": encoded_vector(raw_recomposition),
            "PL_wall_source_distinguished_index": wall_source_index,
            "PL_crossing_period_distinguished_index": wall_period_index,
            "PL_wall_weight": wall_weight,
            "PL_period_correction": encoded_vector(wall_correction),
            "PL_corrected_moving_period_recomposition": encoded_vector(
                corrected_recomposition
            ),
            "stored_raw_replay_maximum_error": raw_error,
            "stored_wall_replay_maximum_error": wall_error,
            "stored_corrected_replay_maximum_error": corrected_error,
            "stored_residual_identity_maximum_error": residual_identity_error,
            "thimble_rows": rows,
        },
        "certified_dominant_five": {
            "distinguished_indices_in_A219_priority_order": list(CERTIFIED_TARGETS),
            "floating_replay_maximum_error": a230_error,
            "coordinate_radius_upper": certified_radii.tolist(),
            "product_disk_l2_radius_upper": float(np.linalg.norm(certified_radii)),
        },
        "remaining_interval_frontier": {
            "unique_thimble_target_count": len(remaining_manifest),
            "raw_coefficient_l1_norm": sum(
                abs(int(row["raw_signed_coefficient"])) for row in remaining_manifest
            ),
            "PL_corrected_effective_coefficient_l1_norm": sum(
                abs(int(row["PL_corrected_effective_signed_coefficient"]))
                for row in remaining_manifest
            ),
            "targets_in_A219_profile_priority_order": remaining_manifest,
            "separate_moving_blocks_requiring_interval_authority": [
                "the 71 listed all-eight thimble periods",
                "the selected rank-3 all-eight primitive-handle combination",
                "the selected all-eight anchored beta branch",
                "an interval Jacobian on one wall-free neighborhood of n3",
            ],
        },
        "summary": {
            "raw_thimble_support": len(rows),
            "raw_thimble_coefficient_l1_norm": sum(abs(value) for value in signed_by_index.values()),
            "PL_corrected_support": sum(value != 0 for value in effective_signed.values()),
            "PL_corrected_coefficient_l1_norm": sum(abs(value) for value in effective_signed.values()),
            "certified_all_eight_thimble_target_count": len(certified),
            "remaining_all_eight_thimble_target_count": len(remaining_manifest),
            "A209_replaces_rank3_thimble_frontier": False,
        },
        "authority": {
            "A208_rank3_chain": {"path": relative(A208), "sha256": sha256(A208)},
            "A131_orientation": {"path": relative(ORIENTATION), "sha256": sha256(ORIENTATION)},
            "n3_ultra_probe": {"path": relative(N3), "sha256": sha256(N3)},
            "A219_profile_priority": {"path": relative(A219), "sha256": sha256(A219)},
            "A230_dominant_five_intervals": {"path": relative(A230), "sha256": sha256(A230)},
            "builder_source": {
                "path": relative(Path(__file__).resolve()),
                "sha256": sha256(Path(__file__).resolve()),
            },
            "n3_thimble_caches": cache_authority,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "full_n3_floating_chain_decomposition_identity_closed": True,
            "PL_wall_correction_assignment_closed": True,
            "dominant_five_all_eight_interval_balls_inherited": True,
            "remaining_71_all_eight_thimble_intervals_closed": False,
            "rank3_handle_combination_interval_closed": False,
            "rank3_anchored_beta_interval_closed": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "certify the remaining A231 manifest by a combined-chain validated "
            "transport or its exact homological compression; A209 alone cannot "
            "replace these relative-thimble values"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four n3 Chain Decomposition Frontier (A231) v1\n\n"
        "A231 replays the complete rank-3 n3 floating identity in all eight "
        "residue rows. The stored raw moving period is exactly the canonically "
        "oriented 76-thimble sum plus the `8 x 8` primitive-handle matrix "
        "contracted with `[1,1,1,-1,1,0,0,1]`. The PL correction is separately "
        "identified as the signed `d064` coefficient multiplying the moving "
        "`d065` period. Maximum replay error is "
        f"`{max(raw_error, wall_error, corrected_error):.3e}`.\n\n"
        "The five A230 all-eight interval balls replay their n3 floating "
        f"contributions to `{a230_error:.3e}` and leave an exact manifest of "
        f"`{len(remaining_manifest)}` distinct thimble targets. A209 certifies "
        "E32 primitive handles at the selected center; it does not replace "
        "these relative-thimble periods and is not a full-chain reduction.\n\n"
        "Thus the algebraic decomposition and wall assignment are closed. The "
        "remaining interval work is explicitly the 71 all-eight thimble values "
        "(or a proved homological compression), the selected moving handle "
        "combination, the anchored beta branch, and an interval Jacobian. No "
        "covariant zero or full SM closure is claimed.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
