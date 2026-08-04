from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, ctx

import certify_q79_height4_target_tail_hessian_interval as frobenius
import certify_q79_height4_d027_disk_cauchy_frobenius as disk_frobenius
import certify_q79_selected_side_base_lift_interval as interval_serializer


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
INDEX = 27
EPSILON = 1.0e-3
SOURCE = VALIDATED / "far_source" / "d027.1em03.json"
MAIN = VALIDATED / "far_residue" / "d027.main.a406m.json"
REFERENCE = VALIDATED / "far_residue" / "d027.tail_segmented.a406r.json"
NODE = VALIDATED / "d027.n3.node.refined.json"
CANONICAL = VALIDATED / "d027.n3.full8.refined.json"
THIMBLE = VALIDATED.parent / "cplx" / "n3ud" / "thimbles" / "t027.json"
TAIL = VALIDATED / "far_residue" / "d027.tail_frobenius.a406f.json"
FULL = VALIDATED / "far_residue" / "d027.full.a406.json"
TAIL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD027FarCutFrobeniusTail_A406F_v1.md"
FULL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD027FarCutFullResidue_A406_v1.md"
DISK_THEOREM = ROOT / "proof_corpus" / "MTT_q79D027DiskCauchyMajorant_A406D_v1.md"


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


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=64)
    parser.add_argument("--series-terms", type=int, default=24)
    arguments = parser.parse_args()
    if arguments.dps < 90 or arguments.order < 48:
        raise ValueError("A406F requires at least 90 digits and order 48")
    if not 8 <= arguments.series_terms <= arguments.order // 2:
        raise ValueError("A406F series terms must lie in [8, order/2]")
    ctx.dps = arguments.dps
    started = time.perf_counter()

    source = load(SOURCE)
    main_packet = load(MAIN)
    reference = load(REFERENCE)
    node = load(NODE)
    canonical = load(CANONICAL)
    thimble = load(THIMBLE)
    target = main_packet["selected_target"]
    if (
        main_packet.get("artifact") != "A406M"
        or int(target["distinguished_index"]) != INDEX
        or target["root_id"] != "selected_011"
        or int(target["A219_contribution_rank"]) != 15
        or int(target["signed_chain_coefficient"]) != -2
        or float(target["endpoint_cutoff_epsilon"]) != EPSILON
    ):
        raise AssertionError("A406F main target identity changed")
    if source.get("artifact") != "A380FS" or reference.get("artifact") != "A406R":
        raise AssertionError("A406F source/reference identity changed")
    system, rank, row = frobenius.main_hessian.selected_system(INDEX, arguments.dps)
    if rank != 15 or row["root_id"] != target["root_id"]:
        raise AssertionError("A406F selected n3 system changed")
    node_parameter = frobenius.validated.decoded_acb(
        node["certified_node"]["parameter_ball"]
    )
    node_root = frobenius.validated.decoded_acb(
        node["certified_node"]["double_root_ball"]
    )
    factors, factor_diagnostics = frobenius.tail.factor_taylor_models(
        system,
        node_parameter,
        node_root,
        epsilon=EPSILON,
        order=arguments.order,
    )
    values, _derivatives, tail_diagnostics = disk_frobenius.direction_tail(
        system,
        factors,
        node_parameter,
        node_root,
        0,
        epsilon=EPSILON,
        order=arguments.order,
        series_terms=arguments.series_terms,
    )

    reference_tail = reference["all_eight_endpoint_tails"]
    reference_centers = np.asarray(
        [complex_value(value) for value in reference_tail["interval_centers"]],
        dtype=np.complex128,
    )
    reference_radii = np.asarray(
        reference_tail["interval_radius_uppers"], dtype=np.float64
    )
    raw_centers = np.asarray(
        [frobenius.validated.midpoint(value) for value in values],
        dtype=np.complex128,
    )
    raw_radii = np.asarray(
        [frobenius.validated.radius_upper(value) for value in values],
        dtype=np.float64,
    )
    plus_overlap = abs(raw_centers - reference_centers) <= raw_radii + reference_radii
    minus_overlap = abs(-raw_centers - reference_centers) <= raw_radii + reference_radii
    if bool(np.all(plus_overlap)) == bool(np.all(minus_overlap)):
        raise AssertionError("A406F branch sign is not uniquely separated")
    branch_sign = 1 if bool(np.all(plus_overlap)) else -1
    in_memory_values = [acb(branch_sign) * value for value in values]
    encoded_values = [
        interval_serializer.complex_interval(value) for value in in_memory_values
    ]
    persisted_values = [
        frobenius.validated.interval_from_bounds(value) for value in encoded_values
    ]
    tail_centers = np.asarray(
        [frobenius.validated.midpoint(value) for value in persisted_values],
        dtype=np.complex128,
    )
    tail_radii = np.asarray(
        [frobenius.validated.radius_upper(value) for value in persisted_values],
        dtype=np.float64,
    )
    differences = abs(tail_centers - reference_centers)
    if not bool(np.all(differences <= tail_radii + reference_radii)):
        raise AssertionError("A406F tail misses the independent segmented reference")
    tail_rows = [
        {
            "residue_index_zero_based": index,
            "interval_bounds": encoded_values[index],
            "interval_center": encoded_complex(tail_centers[index]),
            "interval_radius_upper": float(tail_radii[index]),
            "segmented_reference_center_difference": float(differences[index]),
            "segmented_reference_interval_overlaps": True,
        }
        for index in range(8)
    ]
    tail_payload = {
        "schema": "MTTQ79HeightFourD027FarCutFrobeniusTailInterval.v1",
        "status": "D027_FAR_CUT_FROBENIUS_TAIL_ALL_EIGHT_ROWS_CERTIFIED",
        "artifact": "A406F",
        "selected_target": {
            **target,
            "Frobenius_branch_sign_against_A406R": branch_sign,
        },
        "all_eight_endpoint_tails": {
            "rows": tail_rows,
            "interval_centers": [encoded_complex(value) for value in tail_centers],
            "interval_radius_uppers": tail_radii.tolist(),
            "maximum_interval_radius_upper": float(np.max(tail_radii)),
        },
        "quantitative_Hensel_disk": factor_diagnostics,
        "Frobenius_integral_diagnostics": tail_diagnostics,
        "comparison_to_A406R_segmented_reference": {
            "segmented_maximum_radius_upper": float(np.max(reference_radii)),
            "Frobenius_maximum_radius_upper": float(np.max(tail_radii)),
            "in_memory_Frobenius_maximum_radius_upper": float(np.max(raw_radii)),
            "radius_tightening_factor": float(np.max(reference_radii) / np.max(tail_radii)),
            "maximum_center_difference": float(np.max(differences)),
            "all_eight_intervals_overlap": True,
            "unique_branch_sign": branch_sign,
        },
        "numerics": {
            "dps": arguments.dps,
            "Taylor_order": arguments.order,
            "Frobenius_series_terms": arguments.series_terms,
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "A380FS_far_cut_source": authority(SOURCE),
            "A406M_completed_far_main": authority(MAIN),
            "A406R_segmented_branch_reference": authority(REFERENCE),
            "certified_d027_node": authority(NODE),
            "Frobenius_tail_engine": authority(Path(frobenius.__file__).resolve()),
            "A406D_disk_Cauchy_engine": authority(
                Path(disk_frobenius.__file__).resolve()
            ),
            "A406D_disk_Cauchy_theorem": authority(DISK_THEOREM),
            "full_precision_interval_serializer": authority(
                Path(interval_serializer.__file__).resolve()
            ),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_d027_geometry_used": True,
            "same_far_cut_epsilon_used": True,
            "quantitative_Hensel_factor_disk_closed": True,
            "finite_Frobenius_period_series_with_Cauchy_tail_used": True,
            "disk_specific_Cauchy_majorant_used": True,
            "full_precision_interval_round_trip_used": True,
            "all_eight_far_cut_tail_rows_interval_closed": True,
            "A406R_segmented_reference_used_as_bound": False,
            "full_d027_splice_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
    }
    dump(TAIL, tail_payload)

    orientation = int(main_packet["orientation"]["selected_sign"])
    coefficient = int(target["signed_chain_coefficient"])
    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    floating_differences = abs(floating - full_centers)
    if not bool(np.all(floating_differences <= full_radii)):
        raise AssertionError("A406 Frobenius splice misses a floating diagnostic")
    canonical_maximum = float(canonical["summary"]["maximum_full_interval_radius_upper"])
    maximum = float(np.max(full_radii))
    if not maximum < canonical_maximum:
        raise AssertionError("A406 does not tighten canonical d027")
    rows = [
        {
            "residue_index_zero_based": index,
            "full_interval_center": encoded_complex(full_centers[index]),
            "full_interval_radius_upper": float(full_radii[index]),
            "selected_chain_contribution_center": encoded_complex(
                coefficient * full_centers[index]
            ),
            "selected_chain_contribution_radius_upper": float(
                abs(coefficient) * full_radii[index]
            ),
            "floating_value_diagnostic_only": encoded_complex(floating[index]),
            "floating_to_interval_center_distance": float(floating_differences[index]),
            "floating_value_contained": True,
            "containment_margin": float(full_radii[index] - floating_differences[index]),
        }
        for index in range(8)
    ]
    chain_radii = abs(coefficient) * full_radii
    full_payload = {
        "schema": "MTTQ79HeightFourD027FarCutFullResidueInterval.v1",
        "status": "D027_FAR_CUT_FROBENIUS_FULL_EIGHT_ROW_CHAIN_INTERVAL_CERTIFIED",
        "artifact": "A406",
        "selected_target": {**target, "orientation_sign": orientation},
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": maximum,
            "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
            "selected_chain_product_disk_l2_radius_upper": float(np.linalg.norm(chain_radii)),
            "maximum_floating_center_difference": float(np.max(floating_differences)),
            "minimum_floating_containment_margin": float(np.min(full_radii - floating_differences)),
            "canonical_d027_maximum_full_interval_radius_upper": canonical_maximum,
            "canonical_to_A406_maximum_radius_tightening_factor": canonical_maximum / maximum,
            "all_floating_values_contained": True,
        },
        "authority": {
            "A380FS_d027_far_cut_period_source": authority(SOURCE),
            "A406M_far_cut_main": authority(MAIN),
            "A406F_Frobenius_tail": authority(TAIL),
            "canonical_d027_interval": authority(CANONICAL),
            "n3_target_cache": authority(THIMBLE),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_eight_far_cut_main_rows_interval_closed": True,
            "all_eight_Frobenius_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_period_vector_interval_closed": True,
            "selected_chain_contribution_interval_closed": True,
            "strictly_tighter_than_canonical_d027": True,
            "floating_values_used_as_bounds": False,
            "full_76_target_chain_recomposition_updated": False,
            "coupled_beta_period_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replace canonical d027 in the current 76-target chain and rerank "
            "the remaining width sources"
        ),
    }
    dump(FULL, full_payload)
    TAIL_NOTE.write_text(
        "# MTT q79 Height-Four d027 Far-Cut Frobenius Tail (A406F) v1\n\n"
        "A406F evaluates the epsilon `1e-3` d027 nodal tail with the quantitative "
        "Hensel factor disk, finite Frobenius series, Cauchy remainder, and "
        "full-precision serialized interval round trip. A406R selects only its sign.\n\n"
        f"The maximum tail radius is `{np.max(tail_radii):.12g}`.\n",
        encoding="utf-8",
    )
    FULL_NOTE.write_text(
        "# MTT q79 Height-Four d027 Far-Cut Full Residue (A406) v1\n\n"
        "A406 combines the independent A406M main transport with the A406F "
        "Frobenius tail on the selected d027 geometry.\n\n"
        f"The maximum full-row radius is `{maximum:.12g}`, tightening the canonical "
        f"d027 interval by `{canonical_maximum / maximum:.12g}`.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(TAIL)}")
    print(f"wrote {relative(FULL)}")
    print(json.dumps(full_payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
