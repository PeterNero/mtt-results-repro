from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from flint import arb

import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A402 = VALIDATED / "n3.beta_minus_B.augmented.a402.json"
A407 = VALIDATED / "n3.chain.d057d027far.a407.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A_HANDLE = VALIDATED / "n3.handleA.hessian.checkpoint.json"
B_HANDLE = VALIDATED / "n3.handleB.hessian.checkpoint.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"
OUTPUT = VALIDATED / "n3.correlated_partial_residual.a408.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCorrelatedPartialResidual_A408_v1.md"


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
    return all(
        (ROOT / entry["path"]).is_file()
        and sha256(ROOT / entry["path"]) == entry["sha256"]
        for entry in packet.get("authority", {}).values()
    )


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}


def checkpoint_rows(packet: dict) -> tuple[np.ndarray, np.ndarray]:
    balls = [validated.decoded_acb(value) for value in packet["center"][5:13]]
    centers = np.asarray([validated.midpoint(value) for value in balls], dtype=np.complex128)
    radii = np.asarray(
        [validated.upper(arb(value)) for value in packet["output_radii"][:8]],
        dtype=np.float64,
    )
    return centers, radii


def main() -> int:
    identity = load(A400)
    correlated = load(A402)
    chain = load(A407)
    handle = load(A383)
    a_checkpoint = load(A_HANDLE)
    b_checkpoint = load(B_HANDLE)
    wall = load(D065)
    old_residual = load(A386)
    expected = (
        (identity, "A400"),
        (correlated, "A402"),
        (chain, "A407"),
        (handle, "A383"),
        (old_residual, "A386"),
    )
    for packet, artifact in expected:
        if packet.get("artifact") != artifact or not authorities_current(packet):
            raise AssertionError(f"A408 requires current {artifact}")
    if not identity["theorem"]["proved"] or not identity["strict_scope"]["same_carrier_relative_period_identity_closed"]:
        raise AssertionError("A408 relative-chain identity is open")
    if not correlated["strict_scope"]["joint_beta_minus_B_handle_transport_executed"]:
        raise AssertionError("A408 correlated beta-minus-B source is open")
    if not chain["strict_scope"]["full_76_target_chain_recomposition_updated"]:
        raise AssertionError("A408 current 76-target chain is open")
    a_authority = handle["authority"]["A_path_checkpoint"]
    b_authority = handle["authority"]["B_path_checkpoint"]
    if a_authority["sha256"] != sha256(A_HANDLE) or b_authority["sha256"] != sha256(B_HANDLE):
        raise AssertionError("A408 handle checkpoint authority changed")

    a_centers, a_radii = checkpoint_rows(a_checkpoint)
    b_centers, b_radii = checkpoint_rows(b_checkpoint)
    combined_handle_centers = np.asarray(
        [complex_value(row["interval_center"]) for row in handle["handle_rows"]],
        dtype=np.complex128,
    )
    combined_handle_radii = np.asarray(
        [float(row["component_radius_upper"]) for row in handle["handle_rows"]],
        dtype=np.float64,
    )
    if not bool(np.all(abs(a_centers + b_centers - combined_handle_centers) <= a_radii + b_radii + combined_handle_radii)):
        raise AssertionError("A408 A/B handle extraction misses A383")
    if not bool(np.allclose(a_radii + b_radii, combined_handle_radii, rtol=2.0e-14, atol=1.0e-300)):
        raise AssertionError("A408 A/B handle radii do not replay A383")

    relative_centers = np.asarray(
        [complex_value(value) for value in correlated["endpoint"]["beta_center"]],
        dtype=np.complex128,
    )
    relative_radii = np.asarray(
        correlated["endpoint"]["component_radius_uppers"], dtype=np.float64
    )
    chain_centers = np.asarray(
        [complex_value(row["recomposed_chain_interval_center"]) for row in chain["residue_rows"]],
        dtype=np.complex128,
    )
    chain_radii = np.asarray(
        [float(row["recomposed_chain_interval_radius_upper"]) for row in chain["residue_rows"]],
        dtype=np.float64,
    )
    wall_centers = np.asarray(
        [3.0 * complex_value(row["full_interval_center"]) for row in wall["residue_rows"]],
        dtype=np.complex128,
    )
    wall_radii = np.asarray(
        [3.0 * float(row["full_interval_radius_upper"]) for row in wall["residue_rows"]],
        dtype=np.float64,
    )
    residual_centers = relative_centers - chain_centers - a_centers - wall_centers
    residual_radii = relative_radii + chain_radii + a_radii + wall_radii
    floating = np.asarray(
        [complex_value(row["floating_residual_diagnostic_only"]) for row in old_residual["residue_rows"]],
        dtype=np.complex128,
    )
    distances = abs(floating - residual_centers)
    if not bool(np.all(distances <= residual_radii)):
        raise AssertionError("A408 floating residual diagnostic escaped")

    rows = [
        {
            "residue_index_zero_based": index,
            "A402_beta_minus_B_interval_center": encoded_complex(relative_centers[index]),
            "A402_beta_minus_B_component_radius_upper": float(relative_radii[index]),
            "A407_chain_interval_center": encoded_complex(chain_centers[index]),
            "A407_chain_component_radius_upper": float(chain_radii[index]),
            "A383_A_handle_interval_center": encoded_complex(a_centers[index]),
            "A383_A_handle_component_radius_upper": float(a_radii[index]),
            "PL_wall_interval_center": encoded_complex(wall_centers[index]),
            "PL_wall_component_radius_upper": float(wall_radii[index]),
            "residual_interval_center": encoded_complex(residual_centers[index]),
            "residual_component_radius_upper": float(residual_radii[index]),
            "floating_residual_diagnostic_only": encoded_complex(floating[index]),
            "floating_to_residual_center_distance": float(distances[index]),
            "floating_containment_margin": float(residual_radii[index] - distances[index]),
            "floating_residual_contained": True,
            "zero_contained_in_residual_box": bool(
                abs(residual_centers[index].real) <= residual_radii[index]
                and abs(residual_centers[index].imag) <= residual_radii[index]
            ),
        }
        for index in range(8)
    ]
    old_l2 = float(old_residual["summary"]["residual_product_box_l2_radius_upper"])
    new_l2 = float(np.linalg.norm(residual_radii))
    old_maximum = float(old_residual["summary"]["maximum_residual_component_radius_upper"])
    new_maximum = float(np.max(residual_radii))
    if not new_l2 < old_l2 or not new_maximum < old_maximum:
        raise AssertionError("A408 does not tighten A386")
    payload = {
        "schema": "MTTQ79HeightFourCorrelatedPartialResidual.v1",
        "status": "BETA_MINUS_B_CORRELATION_PRESERVED_IN_FULL_ENDPOINT_RESIDUAL",
        "artifact": "A408",
        "identity": "R_n3=(beta-H_B)-C_76-H_A-3*Pi_d065",
        "correlation_partition": {
            "joint_block": ["beta", "H_B"],
            "independent_blocks": ["C_76", "H_A", "3*Pi_d065"],
            "full_common_path_execution_claimed": False,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_residual_component_radius_upper": new_maximum,
            "residual_product_box_l2_radius_upper": new_l2,
            "residual_interval_center_l2_norm": float(np.linalg.norm(residual_centers)),
            "A386_maximum_residual_component_radius_upper": old_maximum,
            "A386_residual_product_box_l2_radius_upper": old_l2,
            "A386_to_A408_L2_radius_tightening_factor": old_l2 / new_l2,
            "A386_to_A408_maximum_radius_tightening_factor": old_maximum / new_maximum,
            "minimum_floating_containment_margin": float(np.min(residual_radii - distances)),
            "all_floating_residual_diagnostics_contained": True,
            "zero_contained_in_every_residual_component_box": all(
                row["zero_contained_in_residual_box"] for row in rows
            ),
        },
        "authority": {
            "A400_exact_relative_chain_identity": authority(A400),
            "A402_correlated_beta_minus_B": authority(A402),
            "A407_current_76_target_chain": authority(A407),
            "A383_handle_decomposition": authority(A383),
            "A383_A_handle_checkpoint": authority(A_HANDLE),
            "A383_B_handle_checkpoint": authority(B_HANDLE),
            "d065_wall_interval": authority(D065),
            "A386_prior_residual": authority(A386),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "exact_relative_chain_identity_consumed": True,
            "beta_minus_B_cross_correlation_preserved": True,
            "current_A407_chain_consumed": True,
            "A_handle_extracted_from_A383_same_source_checkpoint": True,
            "A_handle_chain_wall_combined_by_independent_Minkowski_sum": True,
            "all_eight_endpoint_residual_rows_interval_closed": True,
            "strictly_tighter_than_A386": True,
            "full_common_relative_chain_transport_executed": False,
            "full_polydisk_residual_Jacobian_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "use A405 junction operators to transport the remaining chain/A-handle/wall "
            "blocks in one common affine frame, then certify the full-polydisk Jacobian"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Correlated Partial Residual (A408) v1\n\n"
        "A408 evaluates the exact A400 residual identity as `(beta-H_B)-C_76-H_A-wall`. "
        "It preserves the jointly transported A402 beta/B cancellation and uses independent "
        "Minkowski sums only for A407, the separately extracted A383 A-handle, and d065.\n\n"
        f"The residual product-box L2 radius tightens from `{old_l2:.12g}` to "
        f"`{new_l2:.12g}`, a factor `{old_l2 / new_l2:.12g}`. This is not yet the "
        "full common-path relative-chain transport or an interval-Newton theorem.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
