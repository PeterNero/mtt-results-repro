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
PROBE_DIRECTORY = PERIOD_DIRECTORY / "covariant_floating_probe"
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
OUTPUT = PROBE_DIRECTORY / "height4_covariant_floating_jacobian.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCovariantFloatingJacobianProbe_v1.md"
STEP = 1.0e-6


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


def vector(rows: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in rows], dtype=np.complex128)


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def encoded_vector(value: np.ndarray) -> list[dict[str, str]]:
    return [pair(complex(row)) for row in value]


def encoded_matrix(value: np.ndarray) -> list[list[dict[str, str]]]:
    return [[pair(complex(row)) for row in column] for column in value]


def tag(direction: int, sign: int) -> str:
    return f"d{direction + 1:02d}_{'p' if sign > 0 else 'm'}_h1d0em06"


def realification(vector_value: np.ndarray) -> np.ndarray:
    return np.concatenate([vector_value.real, vector_value.imag])


def main() -> int:
    a208 = load(A208)
    central_candidates = {
        row["candidate_id"]: row for row in a208["height_four_candidates"][1:]
    }
    direction_pairs = []
    for direction in range(8):
        plus_path = PROBE_DIRECTORY / tag(direction, 1) / "probe.packet.json"
        minus_path = PROBE_DIRECTORY / tag(direction, -1) / "probe.packet.json"
        if plus_path.exists() != minus_path.exists():
            raise AssertionError(f"direction {direction + 1} has only one signed probe")
        if not plus_path.exists():
            continue
        plus = load(plus_path)
        minus = load(minus_path)
        for packet, sign in ((plus, 1), (minus, -1)):
            perturbation = packet["perturbation"]
            if (
                int(perturbation["direction_zero_based"]) != direction
                or int(perturbation["sign"]) != sign
                or float(perturbation["step"]) != STEP
                or not packet["strict_scope"]["same_source_beta_and_period_geometry_used"]
            ):
                raise AssertionError("covariant probe identity or scope changed")
        plus_rows = {row["candidate_id"]: row for row in plus["candidate_residuals"]}
        minus_rows = {row["candidate_id"]: row for row in minus["candidate_residuals"]}
        if set(plus_rows) != set(central_candidates) or set(minus_rows) != set(
            central_candidates
        ):
            raise AssertionError("covariant probe candidate inventory changed")
        direction_pairs.append(
            {
                "direction_zero_based": direction,
                "plus_path": plus_path,
                "minus_path": minus_path,
                "plus": plus,
                "minus": minus,
                "plus_rows": plus_rows,
                "minus_rows": minus_rows,
            }
        )
    if not direction_pairs:
        raise FileNotFoundError("no complete signed covariant probe pair exists")

    beta_columns = []
    direction_inventory = []
    for row in direction_pairs:
        plus_beta = vector(
            row["plus"]["moving_beta"]["certified_center_anchored_perturbed_beta"]
        )
        minus_beta = vector(
            row["minus"]["moving_beta"]["certified_center_anchored_perturbed_beta"]
        )
        beta_columns.append((plus_beta - minus_beta) / (2 * STEP))
        direction_inventory.append(
            {
                "direction_one_based": row["direction_zero_based"] + 1,
                "plus_probe": relative(row["plus_path"]),
                "plus_probe_sha256": sha256(row["plus_path"]),
                "minus_probe": relative(row["minus_path"]),
                "minus_probe_sha256": sha256(row["minus_path"]),
                "plus_fixed_handle_wall_diagnostics": row["plus"][
                    "critical_continuation"
                ]["fixed_handle_path_wall_diagnostics"],
                "minus_fixed_handle_wall_diagnostics": row["minus"][
                    "critical_continuation"
                ]["fixed_handle_path_wall_diagnostics"],
            }
        )
    beta_jacobian = np.column_stack(beta_columns)

    candidate_rows = []
    for candidate_id, central in central_candidates.items():
        central_residual = vector(central["refined_floating_residual_rows"])
        period_columns = []
        residual_columns = []
        midpoint_errors = []
        for row in direction_pairs:
            plus = row["plus_rows"][candidate_id]
            minus = row["minus_rows"][candidate_id]
            plus_period = vector(plus["moving_period"])
            minus_period = vector(minus["moving_period"])
            plus_residual = vector(plus["covariant_residual_F"])
            minus_residual = vector(minus["covariant_residual_F"])
            period_columns.append((plus_period - minus_period) / (2 * STEP))
            residual_columns.append((plus_residual - minus_residual) / (2 * STEP))
            midpoint_errors.append(
                float(
                    np.max(
                        abs((plus_residual + minus_residual) / 2 - central_residual)
                    )
                )
            )
        period_jacobian = np.column_stack(period_columns)
        residual_jacobian = np.column_stack(residual_columns)
        identity_error = float(
            np.max(abs(residual_jacobian - (beta_jacobian - period_jacobian)))
        )
        real_jacobian = np.vstack([residual_jacobian.real, residual_jacobian.imag])
        singular_values = np.linalg.svd(real_jacobian, compute_uv=False)
        rank = int(np.linalg.matrix_rank(real_jacobian))
        least_squares_step, *_ = np.linalg.lstsq(
            real_jacobian, -realification(central_residual), rcond=None
        )
        predicted = central_residual + residual_jacobian @ least_squares_step
        candidate_rows.append(
            {
                "candidate_id": candidate_id,
                "A132_objective_rank": central["A132_objective_rank"],
                "center_residual": encoded_vector(central_residual),
                "center_residual_l2_norm": float(np.linalg.norm(central_residual)),
                "center_residual_maximum_absolute_value": float(
                    np.max(abs(central_residual))
                ),
                "moving_period_Jacobian_8_by_k": encoded_matrix(period_jacobian),
                "covariant_residual_Jacobian_8_by_k": encoded_matrix(
                    residual_jacobian
                ),
                "same_source_Jacobian_identity_maximum_error": identity_error,
                "signed_midpoint_replay_maximum_errors": midpoint_errors,
                "maximum_signed_midpoint_replay_error": max(midpoint_errors),
                "realified_Jacobian_shape": list(real_jacobian.shape),
                "realified_Jacobian_rank": rank,
                "realified_Jacobian_singular_values": [
                    float(value) for value in singular_values
                ],
                "local_least_squares_step_on_available_directions": [
                    float(value) for value in least_squares_step
                ],
                "linearized_residual": encoded_vector(predicted),
                "linearized_residual_l2_norm": float(np.linalg.norm(predicted)),
                "linearized_residual_maximum_absolute_value": float(
                    np.max(abs(predicted))
                ),
            }
        )
    packet = {
        "schema": "MTTQ79HeightFourCovariantFloatingJacobianProbe.v1",
        "status": "PARTIAL_SAME_SOURCE_COVARIANT_JACOBIAN_EXECUTED",
        "finite_difference": {
            "scheme": "central",
            "step": STEP,
            "available_direction_count": len(direction_pairs),
            "available_directions_one_based": [
                row["direction_zero_based"] + 1 for row in direction_pairs
            ],
            "target_direction_count": 8,
        },
        "direction_inventory": direction_inventory,
        "moving_beta_Jacobian_8_by_k": encoded_matrix(beta_jacobian),
        "candidate_Jacobians": candidate_rows,
        "summary": {
            "candidate_count": len(candidate_rows),
            "available_direction_count": len(direction_pairs),
            "maximum_center_replay_error": max(
                row["maximum_signed_midpoint_replay_error"] for row in candidate_rows
            ),
            "maximum_same_source_identity_error": max(
                row["same_source_Jacobian_identity_maximum_error"]
                for row in candidate_rows
            ),
            "best_linearized_residual_l2_norm": min(
                row["linearized_residual_l2_norm"] for row in candidate_rows
            ),
        },
        "authority": {
            "A208": relative(A208),
            "A208_sha256": sha256(A208),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "same_source_moving_beta_and_period_Jacobian": True,
            "floating_finite_difference_only": True,
            "all_eight_directions_executed": len(direction_pairs) == 8,
            "interval_Jacobian_certificate": False,
            "covariant_zero_found": False,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
        "next_required_artifact": (
            "complete all eight signed direction pairs, verify step-halving convergence, "
            "then execute a chamber-aware trust-region continuation of F(A,m)"
        ),
    }
    dump(OUTPUT, packet)
    table = []
    for row in candidate_rows:
        table.append(
            "| {rank} | {replay:.3e} | {rank_j} | {before:.6g} | {after:.6g} |".format(
                rank=row["A132_objective_rank"],
                replay=row["maximum_signed_midpoint_replay_error"],
                rank_j=row["realified_Jacobian_rank"],
                before=row["center_residual_l2_norm"],
                after=row["linearized_residual_l2_norm"],
            )
        )
    NOTE.write_text(
        f"""# MTT q79 Height-Four Covariant Floating Jacobian Probe v1

This artifact computes the same-source central finite difference of

`F(A,m)=beta(A)-Pi(A)m`

using a moving selected beta branch, moving critical values, 86 moving thimble
columns, the moving marked fiber basis, and moving A/B handles. It currently
contains {len(direction_pairs)} of 8 real PGL3 directions.

| A132 rank | center replay max | real rank | center L2 | linearized L2 |
|---:|---:|---:|---:|---:|
{chr(10).join(table)}

This is a floating derivative probe, not an interval Jacobian certificate or a
covariant zero proof. The fixed handle representatives are required to remain
in the same Picard-Lefschetz chamber for every signed sample.
""",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
