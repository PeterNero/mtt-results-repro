from __future__ import annotations

import hashlib
import json
import math
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
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A377 = VALIDATED / "n3.rank3.full_residual.interval.json"
A379 = VALIDATED / "n3.beta_hessian.interval.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
OUTPUT = VALIDATED / "n3.rank3.residual.a386.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourHessianAlignedResidualInterval_A386_v1.md"
ARTIFACT = "A386"


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


def vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def indexed_rows(packet: dict, key: str) -> dict[int, dict]:
    rows = {int(row["residue_index_zero_based"]): row for row in packet[key]}
    if set(rows) != set(range(8)):
        raise AssertionError(f"{key} does not contain exactly residues 0 through 7")
    return rows


def main() -> int:
    prefix = load(PREFIX)
    if (
        prefix.get("artifact") != "A373"
        or int(prefix["certified_A219_priority_prefix_length"]) != 76
        or not prefix["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A386 requires the final 76-target certified prefix")
    a231 = load(A231)
    a377 = load(A377)
    beta = load(A379)
    handle = load(A383)
    d065 = load(D065)
    n3 = load(N3)
    if (
        beta.get("artifact") != "A379"
        or not beta["strict_scope"]["rank3_anchored_beta_Hessian_interval_closed"]
        or not authorities_current(beta)
    ):
        raise AssertionError("A379 beta Hessian packet is open or stale")
    if (
        handle.get("artifact") != "A383"
        or not handle["strict_scope"]["rank3_handle_Hessian_interval_closed"]
        or not authorities_current(handle)
    ):
        raise AssertionError("A383 handle Hessian packet is open or stale")
    if d065["selected_target"]["distinguished_index"] != 65:
        raise AssertionError("d065 full interval identity changed")

    decomposition = a231["exact_floating_decomposition"]
    wall_index = int(decomposition["PL_crossing_period_distinguished_index"])
    wall_weight = int(decomposition["PL_wall_weight"])
    if wall_index != 65 or wall_weight != 3:
        raise AssertionError("A231 Picard-Lefschetz wall correction changed")

    beta_rows = indexed_rows(beta, "beta_rows")
    handle_rows = indexed_rows(handle, "handle_rows")
    candidate_rows = [
        row for row in n3["candidate_residuals"] if int(row["A132_objective_rank"]) == 3
    ]
    if len(candidate_rows) != 1:
        raise AssertionError("n3 probe no longer contains exactly one rank-3 row")
    floating_residual = vector(candidate_rows[0]["PL_corrected_residual"])

    rows = []
    for residue_index in range(8):
        chain_row = prefix["residue_rows"][residue_index]
        beta_row = beta_rows[residue_index]
        handle_row = handle_rows[residue_index]
        wall_row = d065["residue_rows"][residue_index]

        beta_center = complex_value(beta_row["interval_center"])
        beta_radius = float(beta_row["component_radius_upper"])
        chain_center = complex_value(chain_row["certified_prefix_interval_center"])
        chain_radius = float(chain_row["certified_prefix_interval_radius_upper"])
        handle_center = complex_value(handle_row["interval_center"])
        handle_radius = float(handle_row["component_radius_upper"])
        wall_center = wall_weight * complex_value(wall_row["full_interval_center"])
        wall_radius = abs(wall_weight) * float(wall_row["full_interval_radius_upper"])

        period_center = chain_center + handle_center + wall_center
        period_radius = chain_radius + handle_radius + wall_radius
        residual_center = beta_center - period_center
        residual_radius = beta_radius + period_radius
        floating = floating_residual[residue_index]
        real_difference = abs(floating.real - residual_center.real)
        imaginary_difference = abs(floating.imag - residual_center.imag)
        contained = real_difference <= residual_radius and imaginary_difference <= residual_radius
        if not contained:
            raise AssertionError("floating rank-3 residual left the A386 residual box")

        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "A379_beta_interval_center": encoded_complex(beta_center),
                "A379_beta_component_radius_upper": beta_radius,
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
    old_l2_radius = float(a377["summary"]["residual_product_box_l2_radius_upper"])
    new_l2_radius = float(np.linalg.norm(residual_radii))
    if not new_l2_radius < old_l2_radius:
        raise AssertionError("A386 does not tighten the A377 residual box")

    payload = {
        "schema": "MTTQ79HeightFourHessianAlignedResidualInterval.v1",
        "status": "N3_RANK3_HESSIAN_ALIGNED_EIGHT_RESIDUAL_ROWS_INTERVAL_RECOMPOSED",
        "artifact": ARTIFACT,
        "identity": "R_n3 = beta_A379 - (sum_76 m_I Pi_I + H_A383 + 3 Pi_d065)",
        "source_alignment": (
            "the ordinary beta and handle rows are taken from the same A379/A383 "
            "executions that supply the A384 residual Jacobian"
        ),
        "PL_wall_correction": {
            "source_distinguished_index": int(
                decomposition["PL_wall_source_distinguished_index"]
            ),
            "crossing_period_distinguished_index": wall_index,
            "integer_weight": wall_weight,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": len(rows),
            "maximum_residual_component_radius_upper": float(np.max(residual_radii)),
            "residual_product_box_l2_radius_upper": new_l2_radius,
            "residual_interval_center_l2_norm": float(np.linalg.norm(residual_centers)),
            "A377_residual_product_box_l2_radius_upper": old_l2_radius,
            "A377_to_A386_radius_reduction_factor": old_l2_radius / new_l2_radius,
            "minimum_floating_containment_margin": min(
                row["floating_containment_margin"] for row in rows
            ),
            "all_floating_residual_diagnostics_contained": True,
            "zero_contained_in_every_residual_component_box": all(
                row["zero_contained_in_residual_box"] for row in rows
            ),
        },
        "authority": {
            "A373_final_76_target_prefix": authority(PREFIX),
            "A231_chain_and_PL_identity": authority(A231),
            "A377_prior_residual_interval": authority(A377),
            "A379_beta_Hessian_and_ordinary_rows": authority(A379),
            "A383_handle_Hessian_and_ordinary_rows": authority(A383),
            "d065_full_interval": authority(D065),
            "n3_ultra_probe": authority(N3),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_target_intervals_closed": True,
            "A379_beta_value_and_Jacobian_source_aligned": True,
            "A383_handle_value_and_Jacobian_source_aligned": True,
            "PL_wall_correction_interval_closed": True,
            "residual_interval_strictly_tighter_than_A377": True,
            "independent_component_radii_still_dependency_forgetting": True,
            "coupled_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "preserve beta-period cancellation in a coupled residual enclosure, "
            "then transport the A384 Jacobian over a wall-free A385 polydisk"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Hessian-Aligned Residual Interval (A386) v1\n\n"
        "A386 recomposes the rank-3 residual using the ordinary rows emitted by "
        "the same A379 beta and A383 handle executions that supply the A384 "
        "Jacobian. This removes the obsolete A376/A374 widths from the active "
        "value packet.\n\n"
        f"The residual product-box L2 radius falls from `{old_l2_radius:.12g}` "
        f"to `{new_l2_radius:.12g}`, a factor `{old_l2_radius / new_l2_radius:.12g}`. "
        "Every floating diagnostic remains contained.\n\n"
        "The remaining width still adds independently certified beta and period "
        "radii, so it does not preserve their cancellation. A386 is therefore a "
        "strict tightening and source synchronization, not an interval-Newton "
        "zero theorem.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
