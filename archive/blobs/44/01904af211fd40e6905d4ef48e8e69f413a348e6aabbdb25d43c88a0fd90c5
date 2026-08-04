from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import acb, acb_mat, arb, ctx

import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_rank3_beta_hessian_interval as beta_hessian
import certify_q79_height4_rank3_handle_hessian_interval as handle_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = main_hessian.VALIDATED
HESSIAN = main_hessian.OUTPUT_DIRECTORY
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A377 = VALIDATED / "n3.rank3.full_residual.interval.json"
A379 = beta_hessian.OUTPUT
A383 = handle_hessian.OUTPUT
PRECISION_MANIFEST = HESSIAN / "precision.manifest.json"
OUTPUT = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3ResidualJacobianInterval_A384_v1.md"
ARTIFACT = "A384"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def matrix(packet: dict, key: str) -> tuple[np.ndarray, np.ndarray]:
    rows = packet[key]
    if len(rows) != 8 or any(len(row) != 8 for row in rows):
        raise AssertionError(f"{key} is not 8 by 8")
    centers = np.asarray(
        [
            [complex_value(entry["interval_center"]) for entry in row]
            for row in rows
        ],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [
            [float(entry["component_radius_upper"]) for entry in row]
            for row in rows
        ],
        dtype=np.float64,
    )
    if not bool(np.all(np.isfinite(radii))) or not bool(np.all(radii >= 0.0)):
        raise AssertionError(f"{key} has invalid interval radii")
    return centers, radii


def authorities_current(packet: dict) -> bool:
    authority = packet.get("authority", {})
    if not authority:
        return False
    for row in authority.values():
        path = ROOT / row.get("path", "")
        if not path.is_file() or row.get("sha256") != sha256(path):
            return False
    return True


def full_target_authority_tree_current(packet: dict) -> bool:
    if not authorities_current(packet):
        return False
    authority = packet["authority"]
    for key in ("A380_main_Hessian", "A381_tail_Hessian"):
        path = ROOT / authority[key]["path"]
        nested = load(path)
        if not authorities_current(nested):
            return False
    return True


def rigorous_preconditioned_neumann(
    centers: np.ndarray,
    radii: np.ndarray,
) -> dict:
    center_ball = acb_mat(
        [
            [
                acb(
                    format(float(centers[row, column].real), ".17g"),
                    format(float(centers[row, column].imag), ".17g"),
                )
                for column in range(8)
            ]
            for row in range(8)
        ]
    )
    inverse_ball = center_ball.inv()
    identity = acb_mat(8, 8)
    for index in range(8):
        identity[index, index] = acb(1)
    inverse_defect = identity - inverse_ball * center_ball
    bounds_arb: list[list[arb]] = []
    for row in range(8):
        bound_row = []
        for column in range(8):
            value = abs(inverse_defect[row, column])
            for inner in range(8):
                value += abs(inverse_ball[row, inner]) * arb(
                    format(float(radii[inner, column]), ".17g")
                )
            bound_row.append(value)
        bounds_arb.append(bound_row)
    bounds = np.asarray(
        [
            [float(value.upper()) for value in row]
            for row in bounds_arb
        ],
        dtype=np.float64,
    )
    infinity_row_bounds = [
        float(sum(row, arb(0)).upper()) for row in bounds_arb
    ]

    weights = np.ones(8, dtype=np.float64)
    for _ in range(256):
        updated = bounds @ weights + 1.0e-300
        weights = updated / float(np.max(updated))
    weights = np.maximum(weights, 1.0e-300)
    weighted_row_bounds = []
    for row in range(8):
        numerator = sum(
            (
                bounds_arb[row][column]
                * arb(format(float(weights[column]), ".17g"))
                for column in range(8)
            ),
            arb(0),
        )
        denominator = arb(format(float(weights[row]), ".17g"))
        weighted_row_bounds.append(float((numerator / denominator).upper()))
    weighted_contraction = max(weighted_row_bounds)
    return {
        "method": (
            "ACB center inverse with componentwise bound "
            "B=|I-Y*C|+|Y|*radius(J), tested in a positive weighted infinity norm"
        ),
        "componentwise_preconditioned_defect_upper_8_by_8": bounds.tolist(),
        "unweighted_infinity_row_sum_uppers": infinity_row_bounds,
        "unweighted_infinity_norm_upper": max(infinity_row_bounds),
        "positive_weights": [float(value) for value in weights],
        "weighted_infinity_row_uppers": weighted_row_bounds,
        "weighted_infinity_contraction_upper": weighted_contraction,
        "every_matrix_in_Jacobian_product_box_nonsingular": (
            weighted_contraction < 1.0
        ),
    }


def target_candidates(index: int) -> list[Path]:
    return [
        HESSIAN / f"d{index:03d}.fullH.interval.json",
        HESSIAN / "detour" / f"d{index:03d}.fullH.json",
        HESSIAN / "far" / f"d{index:03d}.far.fullH.interval.json",
        HESSIAN / "far2" / f"d{index:03d}.fullH.json",
    ]


def selected_target_packet(index: int, precision_rows: dict[int, dict]) -> tuple[Path, dict]:
    row = precision_rows.get(index)
    if row is None or row.get("full_budget_pass") is not True:
        raise FileNotFoundError(
            f"precision manifest has no accepted full Hessian for d{index:03d}"
        )
    path = ROOT / row["full_path"]
    if not path.is_file() or sha256(path) != row.get("full_sha256"):
        raise AssertionError(f"precision-manifest full hash is stale for d{index:03d}")
    packet = load(path)
    if (
        packet.get("schema") != "MTTQ79HeightFourTargetFullHessianInterval.v1"
        or packet.get("strict_scope", {}).get(
            "target_full_Hessian_interval_closed", False
        )
        is not True
        or int(packet.get("selected_target", {}).get("distinguished_index", -1))
        != index
        or not full_target_authority_tree_current(packet)
    ):
        raise AssertionError(f"selected full Hessian is invalid for d{index:03d}")
    return path, packet


def main() -> int:
    ctx.dps = 100
    prefix = load(PREFIX)
    if (
        prefix.get("artifact") != "A373"
        or int(prefix.get("certified_A219_priority_prefix_length", 0)) != 76
    ):
        raise AssertionError("A384 requires the final A373 target inventory")
    inventory = prefix["certified_targets_in_A219_priority_order"]
    if len(inventory) != 76:
        raise AssertionError("A373 target count changed")
    a231 = load(A231)
    coefficient_rows = {
        int(row["distinguished_index"]): row
        for row in a231["exact_floating_decomposition"]["thimble_rows"]
    }
    if len(coefficient_rows) != 76:
        raise AssertionError("A231 coefficient inventory changed")
    precision = load(PRECISION_MANIFEST)
    if (
        precision.get("schema")
        != "MTTQ79HeightFourPrecisionHessianQueueManifest.v1"
        or precision.get("status")
        != "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED"
        or int(precision.get("counts", {}).get("full_budget", 0)) != 76
        or not authorities_current(precision)
    ):
        raise AssertionError("A384 requires the completed current precision manifest")
    precision_rows = {
        int(row["distinguished_index"]): row for row in precision["targets"]
    }
    if len(precision_rows) != 76:
        raise AssertionError("precision target inventory changed")

    chain_centers = np.zeros((8, 8), dtype=np.complex128)
    chain_radii = np.zeros((8, 8), dtype=np.float64)
    target_rows = []
    target_packets: dict[int, tuple[Path, dict]] = {}
    for item in inventory:
        rank = int(item["A219_profile_priority_rank"])
        index = int(item["distinguished_index"])
        path, packet = selected_target_packet(index, precision_rows)
        target_packets[index] = (path, packet)
        target = packet["selected_target"]
        coefficient = int(target["signed_chain_coefficient"])
        expected = int(coefficient_rows[index]["raw_signed_coefficient"])
        if coefficient != expected:
            raise AssertionError(f"d{index:03d} chain coefficient changed")
        centers, radii = matrix(packet, "complex_full_Hessian_8_by_8")
        chain_centers += coefficient * centers
        chain_radii += abs(coefficient) * radii
        target_rows.append(
            {
                "A219_profile_priority_rank": rank,
                "distinguished_index": index,
                "root_id": target["root_id"],
                "signed_chain_coefficient": coefficient,
                "certificate_path": relative(path),
                "certificate_sha256": sha256(path),
                "certificate_artifact": packet["artifact"],
                "selected_contribution_frobenius_radius_upper": float(
                    abs(coefficient) * np.linalg.norm(radii)
                ),
            }
        )

    beta_packet = load(A379)
    if (
        not beta_packet["strict_scope"][
            "rank3_anchored_beta_Hessian_interval_closed"
        ]
        or not authorities_current(beta_packet)
    ):
        raise AssertionError("A379 beta Hessian is open")
    beta_centers, beta_radii = matrix(
        beta_packet, "complex_beta_Hessian_8_by_8"
    )
    handle_packet = load(A383)
    if (
        not handle_packet["strict_scope"]["rank3_handle_Hessian_interval_closed"]
        or not authorities_current(handle_packet)
    ):
        raise AssertionError("A383 handle Hessian is open")
    handle_centers, handle_radii = matrix(
        handle_packet, "complex_handle_Hessian_8_by_8"
    )

    wall = a231["exact_floating_decomposition"]
    wall_index = int(wall["PL_crossing_period_distinguished_index"])
    wall_weight = int(wall["PL_wall_weight"])
    if wall_index != 65 or wall_weight != 3:
        raise AssertionError("A231 Picard-Lefschetz correction changed")
    wall_path, wall_packet = target_packets[wall_index]
    wall_centers, wall_radii = matrix(
        wall_packet, "complex_full_Hessian_8_by_8"
    )

    period_centers = chain_centers + handle_centers + wall_weight * wall_centers
    period_radii = chain_radii + handle_radii + abs(wall_weight) * wall_radii
    jacobian_centers = beta_centers - period_centers
    jacobian_radii = beta_radii + period_radii
    singular_values = np.linalg.svd(jacobian_centers, compute_uv=False)
    center_minimum_singular = float(np.min(singular_values))
    perturbation_frobenius = float(np.linalg.norm(jacobian_radii))
    nonsingular_by_weyl = center_minimum_singular > perturbation_frobenius
    determinant_center = complex(np.linalg.det(jacobian_centers))
    center_inverse = np.linalg.inv(jacobian_centers)
    inverse_residual_frobenius = float(
        np.linalg.norm(np.eye(8, dtype=np.complex128) - center_inverse @ jacobian_centers)
    )
    preconditioned_neumann = rigorous_preconditioned_neumann(
        jacobian_centers,
        jacobian_radii,
    )

    payload = {
        "schema": "MTTQ79HeightFourRank3ResidualJacobianInterval.v1",
        "status": "N3_RANK3_FULL_COMPLEX_8_BY_8_RESIDUAL_JACOBIAN_INTERVAL_RECOMPOSED",
        "artifact": ARTIFACT,
        "identity": (
            "D R_n3 = D beta_n3 - (sum_76 m_I D Pi_I + D H_rank3 + 3 D Pi_d065)"
        ),
        "coordinate_convention": beta_packet["coordinate_convention"],
        "target_chain_inventory": target_rows,
        "Picard_Lefschetz_wall_correction": {
            "distinguished_index": wall_index,
            "integer_weight": wall_weight,
            "certificate_path": relative(wall_path),
            "certificate_sha256": sha256(wall_path),
        },
        "complex_residual_Jacobian_8_by_8": [
            [
                {
                    "row_zero_based": row,
                    "column_zero_based": column,
                    "interval_center": pair(jacobian_centers[row, column]),
                    "component_radius_upper": float(jacobian_radii[row, column]),
                }
                for column in range(8)
            ]
            for row in range(8)
        ],
        "center_inverse_8_by_8": [
            [pair(center_inverse[row, column]) for column in range(8)]
            for row in range(8)
        ],
        "verified_interval_nonsingularity": preconditioned_neumann,
        "summary": {
            "certified_target_Hessian_count": len(target_rows),
            "certified_target_Hessian_entries": 64 * len(target_rows),
            "certified_handle_Hessian_entries": 64,
            "certified_beta_Hessian_entries": 64,
            "maximum_Jacobian_component_radius_upper": float(np.max(jacobian_radii)),
            "Jacobian_product_box_frobenius_radius_upper": perturbation_frobenius,
            "Jacobian_center_frobenius_norm": float(np.linalg.norm(jacobian_centers)),
            "Jacobian_center_minimum_singular_value": center_minimum_singular,
            "Weyl_nonsingularity_margin": center_minimum_singular
            - perturbation_frobenius,
            "every_matrix_in_Jacobian_product_box_nonsingular_by_Weyl": nonsingular_by_weyl,
            "Jacobian_center_determinant": pair(determinant_center),
            "center_inverse_replay_frobenius_residual": inverse_residual_frobenius,
            "preconditioned_weighted_infinity_contraction_upper": (
                preconditioned_neumann["weighted_infinity_contraction_upper"]
            ),
            "every_matrix_in_Jacobian_product_box_nonsingular_by_preconditioned_Neumann": (
                preconditioned_neumann[
                    "every_matrix_in_Jacobian_product_box_nonsingular"
                ]
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A373_final_76_target_prefix": PREFIX,
                "A231_chain_and_PL_identity": A231,
                "A377_full_residual_interval": A377,
                "A379_beta_Hessian": A379,
                "A383_handle_Hessian": A383,
                "coefficient_weighted_precision_manifest": PRECISION_MANIFEST,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_target_Hessian_intervals_closed": True,
            "all_76_coefficient_weighted_precision_budgets_closed": True,
            "rank3_handle_Hessian_interval_closed": True,
            "rank3_anchored_beta_Hessian_interval_closed": True,
            "PL_wall_Hessian_correction_closed": True,
            "full_residual_point_Jacobian_interval_closed": True,
            "point_Jacobian_product_box_nonsingularity_closed": (
                preconditioned_neumann[
                    "every_matrix_in_Jacobian_product_box_nonsingular"
                ]
            ),
            "Jacobian_polydisk_extension_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "extend this point-Jacobian interval over an explicit wall-free "
            "parameter polydisk and execute interval Newton or Krawczyk"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Residual Jacobian Interval (A384) v1\n\n"
        "A384 recomposes the same-source complex residual Jacobian from A379, "
        "all 76 selected target Hessians, A383, and the preselected `3*d065` "
        "Picard-Lefschetz correction.\n\n"
        f"The center minimum singular value is `{center_minimum_singular:.12g}` "
        f"and the interval perturbation Frobenius bound is "
        f"`{perturbation_frobenius:.12g}`. The resulting Weyl margin is "
        f"`{center_minimum_singular - perturbation_frobenius:.12g}`.\n\n"
        "This packet certifies the Jacobian at the selected alignment. A separate "
        "polydisk variation bound is still required before interval Newton.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
