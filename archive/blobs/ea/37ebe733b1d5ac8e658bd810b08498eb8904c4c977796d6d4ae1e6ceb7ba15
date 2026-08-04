from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np

from build_selected_q79_effective_integral_branch_quotient import (
    BETA,
    CONVERGENCE,
    INTEGRAL_BASIS,
    MARKER_MULTIPLIERS,
    PERIODS,
    SEARCH_SCALE,
    SEARCH_WEIGHTS,
    complex_value,
)
from explore_q79_a126_integral_period_branch_lll import (
    candidate_record,
    kannan_candidates,
    realification,
)


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A132 = PERIOD_DIRECTORY / "selected_alignment_effective_branch_quotient_and_height4_seed.packet.json"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
A207 = PERIOD_DIRECTORY / "selected_alignment_E32_weighted_71_thimble_and_frozen_carrier_decision.packet.json"
REFINED_BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfoursurvivorqueueande32priority.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfoursurvivorqueueande32priority.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HeightFourSurvivorQueueAndE32Priority_A208_v1.md"
E32_INDEX = 5


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def vector_id(values: list[int]) -> str:
    canonical = json.dumps(values, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(canonical).hexdigest()[:16]


def search_inputs() -> dict[str, object]:
    period_packet = load(PERIODS)
    convergence_packet = load(CONVERGENCE)
    beta_packet = load(BETA)
    basis_packet = load(INTEGRAL_BASIS)
    period_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in period_packet["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    beta = np.asarray(
        [complex_value(value) for value in beta_packet["tight_endpoint"]["beta_center"]],
        dtype=np.complex128,
    )
    entrywise_primary = np.asarray(
        [
            [float(value) for value in row]
            for row in convergence_packet[
                "primary_entrywise_absolute_difference_envelope_rows"
            ]
        ],
        dtype=np.float64,
    )
    return {
        "period_matrix": period_matrix,
        "beta": beta,
        "beta_radius": float(
            beta_packet["tight_endpoint"]["uniform_component_radius_upper"]
        ),
        "entrywise_error": np.hstack(
            [entrywise_primary, np.zeros((8, 2), dtype=np.float64)]
        ),
        "primary_basis": np.asarray(
            basis_packet["primary_basis"]["basis_columns"], dtype=object
        ),
    }


def collect_records(inputs: dict[str, object]) -> list[dict]:
    period_matrix = inputs["period_matrix"]
    beta = inputs["beta"]
    real_matrix = np.vstack([period_matrix[:, :90].real, period_matrix[:, :90].imag])
    real_beta = realification(beta)
    active_indices = np.arange(90, dtype=np.int64)
    seen: set[tuple[int, ...]] = set()
    records: list[dict] = []
    for coefficient_weight in SEARCH_WEIGHTS:
        for marker_multiplier in MARKER_MULTIPLIERS:
            marker_weight = coefficient_weight * marker_multiplier
            for method, ell_active in kannan_candidates(
                real_matrix,
                real_beta,
                scale=SEARCH_SCALE,
                coefficient_weight=coefficient_weight,
                marker_weight=marker_weight,
            ):
                key = tuple(int(value) for value in ell_active)
                if key in seen:
                    continue
                seen.add(key)
                records.append(
                    candidate_record(
                        ell_active=ell_active,
                        active_indices=active_indices,
                        period_matrix=period_matrix,
                        beta=beta,
                        entrywise_error=inputs["entrywise_error"],
                        primary_basis=inputs["primary_basis"],
                        beta_radius=inputs["beta_radius"],
                        method=method,
                        scale=SEARCH_SCALE,
                        coefficient_weight=coefficient_weight,
                        marker_weight=marker_weight,
                    )
                )
    return records


def objective(record: dict) -> tuple[float, float, int]:
    return (
        float(record["residual_maximum_absolute_value"]),
        float(record["residual_l2_norm"]),
        int(record["coefficient_l1_norm"]),
    )


def main() -> int:
    inputs = search_inputs()
    period_matrix = inputs["period_matrix"]
    primary_basis = inputs["primary_basis"]
    records = collect_records(inputs)
    beta_radius = float(inputs["beta_radius"])
    center_nonseparated = [
        row
        for row in records
        if float(row["residual_maximum_absolute_value"]) < beta_radius
    ]
    height_four = sorted(
        [row for row in center_nonseparated if row["coefficient_height"] == 4],
        key=objective,
    )
    if len(records) != 575 or len(center_nonseparated) != 85 or len(height_four) != 5:
        raise AssertionError("A132 fixed-grid multiplicities changed")

    a132 = load(A132)
    a134 = load(A134)
    a207 = load(A207)
    if not a207["scope"]["frozen_height_four_carrier_rejected_by_E32_zero_exclusion"]:
        raise AssertionError("A207 frozen-carrier rejection is not closed")
    selected_ell = a132["height_four_continuation_seed"]["ell_Z92"]
    if height_four[0]["ell_Z92"] != selected_ell:
        raise AssertionError("A132 published objective winner changed")

    old_support = {
        int(row["distinguished_index"])
        for row in a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    }
    refined_beta_packet = load(REFINED_BETA)
    refined_beta = np.asarray(
        [
            complex(float(value["real"]), float(value["imaginary"]))
            for value in refined_beta_packet["endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )

    candidates: list[dict] = []
    for rank, record in enumerate(height_four, start=1):
        ell = [int(value) for value in record["ell_Z92"]]
        primitive = np.asarray(
            primary_basis @ np.asarray(ell[:90], dtype=object), dtype=object
        )
        thimble = [int(value) for value in primitive[:90]]
        handles = [int(value) for value in primitive[90:]]
        support = {index + 1 for index, value in enumerate(thimble) if value}
        missing = sorted(support - old_support)
        residual = refined_beta - period_matrix @ np.asarray(ell, dtype=np.float64)
        candidates.append(
            {
                "candidate_id": vector_id(ell),
                "A132_objective_rank": rank,
                "A132_published_seed": rank == 1,
                "A207_decision": "REJECTED_BY_CERTIFIED_E32_ZERO_EXCLUSION" if rank == 1 else "UNTESTED",
                "Kannan_witness": {
                    "method": record["method"],
                    "embedding_scale": record["embedding_scale"],
                    "coefficient_weight": record["coefficient_weight"],
                    "marker_weight": record["marker_weight"],
                },
                "effective_coordinates_Z90": ell[:90],
                "effective_height": record["coefficient_height"],
                "effective_support": record["support_size"],
                "effective_l1_norm": record["coefficient_l1_norm"],
                "A132_center_residual_maximum": record[
                    "residual_maximum_absolute_value"
                ],
                "A132_center_residual_l2": record["residual_l2_norm"],
                "primitive_thimble_chain": [
                    {"distinguished_index": index + 1, "coefficient": value}
                    for index, value in enumerate(thimble)
                    if value
                ],
                "primitive_thimble_support": len(support),
                "primitive_thimble_l1_norm": sum(abs(value) for value in thimble),
                "primitive_handle_coordinates": handles,
                "new_E32_interval_indices_relative_to_A207": missing,
                "new_E32_interval_support": len(missing),
                "new_E32_interval_l1_weight": sum(
                    abs(thimble[index - 1]) for index in missing
                ),
                "refined_floating_residual_rows": [complex_pair(value) for value in residual],
                "refined_floating_residual_maximum": float(np.max(np.abs(residual))),
                "refined_floating_residual_l2": float(np.linalg.norm(residual)),
                "refined_floating_E32_residual": complex_pair(residual[E32_INDEX]),
                "refined_floating_E32_residual_absolute_value": float(
                    abs(residual[E32_INDEX])
                ),
            }
        )

    e32_order = sorted(
        candidates,
        key=lambda row: (
            row["refined_floating_E32_residual_absolute_value"],
            row["A132_objective_rank"],
        ),
    )
    for rank, row in enumerate(e32_order, start=1):
        row["E32_priority_rank"] = rank
    priority = e32_order[0]
    if priority["A132_objective_rank"] != 3:
        raise AssertionError("floating E32-priority survivor changed")
    missing_union = sorted(
        {
            index
            for row in candidates[1:]
            for index in row["new_E32_interval_indices_relative_to_A207"]
        }
    )
    vectors = {tuple(row["effective_coordinates_Z90"]) for row in candidates}
    sign_collisions = sum(tuple(-value for value in vector) in vectors for vector in vectors) // 2

    best_objective = objective(height_four[0])
    packet = {
        "schema": "MTTQ79SelectedAlignmentHeightFourSurvivorQueueAndE32Priority.v1",
        "status": "A132_FIXED_GRID_HEIGHT4_MULTIPLICITY_FROZEN_A207_SURVIVORS_QUEUED",
        "artifact": "A208",
        "authority": {
            "A132_packet": relative(A132),
            "A132_packet_sha256": sha256(A132),
            "A134_support_packet": relative(A134),
            "A134_support_packet_sha256": sha256(A134),
            "A207_decision_packet": relative(A207),
            "A207_decision_packet_sha256": sha256(A207),
            "period_table": relative(PERIODS),
            "period_table_sha256": sha256(PERIODS),
            "period_convergence": relative(CONVERGENCE),
            "period_convergence_sha256": sha256(CONVERGENCE),
            "A132_beta_packet": relative(BETA),
            "A132_beta_packet_sha256": sha256(BETA),
            "refined_beta_packet": relative(REFINED_BETA),
            "refined_beta_packet_sha256": sha256(REFINED_BETA),
            "integral_basis": relative(INTEGRAL_BASIS),
            "integral_basis_sha256": sha256(INTEGRAL_BASIS),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "fixed_grid_reconstruction": {
            "method": "the unchanged A132 FLINT LLL Kannan embedding grid",
            "embedding_scale": SEARCH_SCALE,
            "coefficient_weights": SEARCH_WEIGHTS,
            "marker_multipliers": MARKER_MULTIPLIERS,
            "unique_candidates": len(records),
            "height_distribution": {
                str(key): value
                for key, value in sorted(
                    Counter(row["coefficient_height"] for row in records).items()
                )
            },
            "center_nonseparated_candidates": len(center_nonseparated),
            "center_nonseparated_height_distribution": {
                str(key): value
                for key, value in sorted(
                    Counter(
                        row["coefficient_height"] for row in center_nonseparated
                    ).items()
                )
            },
            "height_four_center_nonseparated_candidates": len(height_four),
            "exact_A132_objective_ties_at_winner": sum(
                objective(row) == best_objective for row in height_four
            ),
            "A132_published_winner_is_unique_under_recorded_objective": True,
            "fixed_grid_is_not_exhaustive_over_Z90": True,
        },
        "symmetry_policy": {
            "quotient_applied": False,
            "reason": (
                "no proved symmetry action preserving the targeted refined beta equation "
                "and its retarded branch has been supplied"
            ),
            "exact_sign_pairs_inside_height_four_set": sign_collisions,
            "antiunitary_or_conjugate_partners_discarded": False,
        },
        "height_four_candidates": candidates,
        "A207_survivor_ledger": {
            "height_four_candidates": len(candidates),
            "rigorously_rejected": 1,
            "untested_survivors": len(candidates) - 1,
            "A207_certified_support": len(old_support),
            "additional_interval_union": missing_union,
            "additional_interval_union_support": len(missing_union),
            "floating_E32_priority_candidate_id": priority["candidate_id"],
            "floating_E32_priority_A132_rank": priority["A132_objective_rank"],
            "floating_E32_priority_absolute_residual": priority[
                "refined_floating_E32_residual_absolute_value"
            ],
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "A132_grid_reconstructed_without_changing_weights": True,
            "all_A132_fixed_grid_height_four_center_nonseparated_rows_recorded": True,
            "A132_published_winner_unique_in_fixed_grid": True,
            "A132_published_winner_rejected_by_A207": True,
            "remaining_rows_are_computational_survivors_not_newly_selected_theorems": True,
            "floating_E32_priority_is_not_exact_membership": True,
            "global_height_four_completeness_over_Z90_proved": False,
            "alternative_carrier_exactly_solved": False,
        },
        "next_required_artifact": (
            "certify the 15-row additional E32 interval union and the survivor-specific "
            "handle combinations, then apply rigorous E32 zero-exclusion to all four survivors"
        ),
    }
    dump(PACKET, packet)

    table_lines = []
    for row in candidates:
        table_lines.append(
            "| {rank} | `{candidate}` | {residual:.9g} | {support} | {missing} | {decision} |".format(
                rank=row["A132_objective_rank"],
                candidate=row["candidate_id"],
                residual=row["refined_floating_E32_residual_absolute_value"],
                support=row["primitive_thimble_support"],
                missing=row["new_E32_interval_support"],
                decision=row["A207_decision"],
            )
        )
    note = f"""# MTT Selected q79 Height-Four Survivor Queue and E32 Priority A208 v1

## Result

A208 reruns the unchanged A132 Kannan grid and retains every height-four vector
whose eight floating centers enter the A132 beta component balls. The grid emits
575 distinct vectors, 85 center-nonseparated vectors, and exactly five such
height-four vectors. The published A132 seed is the unique winner under A132's
recorded lexicographic objective. A207 rigorously rejects that one seed only.

| A132 rank | candidate | refined floating |E32 residual| | primitive support | new intervals | decision |
|---:|---|---:|---:|---:|---|
{chr(10).join(table_lines)}

The floating E32-priority survivor is A132 rank
`{priority['A132_objective_rank']}`, candidate `{priority['candidate_id']}`, at
`{priority['refined_floating_E32_residual_absolute_value']:.17g}`. This is a
candidate-prioritization diagnostic, not a proof of equality and not a new MTT
selection theorem.

## Exact scope

The fixed A132 grid has now been enumerated without changing its scale, weights,
or marker multipliers. There is one exact objective winner and four untested
height-four survivors. No symmetry quotient is applied because no proved
symmetry preserving the refined retarded beta equation is available. In
particular, antiunitary or conjugate partners are not silently discarded.

This is still not an exhaustive theorem over `Z^90`. It proves completeness only
for the finite Kannan grid that A132 actually used. The four survivors must be
decided by interval arithmetic before any stronger carrier claim is made.

## Next computation

The union of new thimble indices required by all four survivors is
`{missing_union}`: 15 intervals. After those rows and the survivor-specific
handle combinations are certified, the same E32 zero-exclusion gate used by
A207 can decide every fixed-grid height-four survivor.

No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")

    candidate = {
        "schema": "MTTSelectedQ79HeightFourSurvivorQueueAndE32Priority.v1",
        "status": packet["status"],
        "artifact": "A208",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "what_closes": {
            "A132_fixed_grid_height_four_multiplicity": True,
            "A132_winner_uniqueness_inside_fixed_grid": True,
            "A207_survivor_queue": True,
            "additional_E32_interval_union": True,
        },
        "what_remains_open": {
            "four_survivor_E32_interval_decisions": True,
            "global_height_four_completeness_over_Z90": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": packet["next_required_artifact"],
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourSurvivorQueueAndE32Priority",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "height_four_candidates": len(candidates),
                "A207_survivors": len(candidates) - 1,
                "additional_E32_intervals": missing_union,
                "floating_E32_priority": priority["candidate_id"],
                "floating_E32_priority_absolute_residual": priority[
                    "refined_floating_E32_residual_absolute_value"
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
