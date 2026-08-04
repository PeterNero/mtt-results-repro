from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from flint import acb, arb, ctx

import certify_q79_height4_target_tail_hessian_interval as frobenius
import certify_q79_height4_target_full_residue_interval as generic
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
FAR_SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
MAIN = VALIDATED / "far_residue" / "d057.main.a397.json"
SEGMENTED_TAIL = VALIDATED / "far_residue" / "d057.tail.a397.json"
NODE = VALIDATED / "d057.n3.node.refined.json"
CANONICAL = VALIDATED / "d057.n3.full8.refined.json"
THIMBLE = VALIDATED.parent / "cplx" / "n3ud" / "thimbles" / "t057.json"
TAIL = VALIDATED / "far_residue" / "d057.tail_frobenius.a397f.json"
FULL = VALIDATED / "far_residue" / "d057.full.a397.json"
TAIL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057FarCutFrobeniusTail_A397F_v1.md"
FULL_NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD057FarCutFullResidue_A397_v1.md"
ARTIFACT = "A397F"
INDEX = 57
EPSILON = 1.0e-3


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


def centered_ball(center: complex, radius: float) -> acb:
    return acb(
        arb(format(center.real, ".17g"), format(radius, ".17g")),
        arb(format(center.imag, ".17g"), format(radius, ".17g")),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=64)
    parser.add_argument("--series-terms", type=int, default=24)
    arguments = parser.parse_args()
    if arguments.dps < 90 or arguments.order < 48:
        raise ValueError("A397F requires at least 90 digits and order 48")
    if not 8 <= arguments.series_terms <= arguments.order // 2:
        raise ValueError("A397F series terms must lie in [8, order/2]")
    ctx.dps = arguments.dps
    started = time.perf_counter()

    main_packet = load(MAIN)
    segmented = load(SEGMENTED_TAIL)
    node = load(NODE)
    source = load(FAR_SOURCE)
    canonical = load(CANONICAL)
    thimble = load(THIMBLE)
    target = main_packet["selected_target"]
    if (
        int(target["distinguished_index"]) != INDEX
        or float(target["endpoint_cutoff_epsilon"]) != EPSILON
        or int(target["signed_chain_coefficient"]) != 4
    ):
        raise AssertionError("A397 main target identity changed")
    system, rank, row = frobenius.main_hessian.selected_system(INDEX, arguments.dps)
    if rank != int(target["A219_contribution_rank"]) or row["root_id"] != target["root_id"]:
        raise AssertionError("A397F selected n3 system changed")
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
    values, _derivatives, tail_diagnostics = frobenius.direction_tail(
        system,
        factors,
        node_parameter,
        node_root,
        0,
        epsilon=EPSILON,
        order=arguments.order,
        series_terms=arguments.series_terms,
    )

    generic_centers = np.asarray(
        [
            complex_value(value)
            for value in segmented["all_eight_endpoint_tails"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    generic_radii = np.asarray(
        segmented["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    raw_centers = np.asarray(
        [frobenius.validated.midpoint(value) for value in values],
        dtype=np.complex128,
    )
    raw_radii = np.asarray(
        [frobenius.validated.radius_upper(value) for value in values],
        dtype=np.float64,
    )
    plus_overlap = abs(raw_centers - generic_centers) <= raw_radii + generic_radii
    minus_overlap = abs(-raw_centers - generic_centers) <= raw_radii + generic_radii
    if bool(np.all(plus_overlap)) == bool(np.all(minus_overlap)):
        raise AssertionError("A397F branch sign is not uniquely separated")
    branch_sign = 1 if bool(np.all(plus_overlap)) else -1
    oriented_in_memory = [acb(branch_sign) * value for value in values]
    encoded_values = [
        interval_serializer.complex_interval(value) for value in oriented_in_memory
    ]
    oriented_values = [
        frobenius.validated.interval_from_bounds(value) for value in encoded_values
    ]
    tail_centers = np.asarray(
        [frobenius.validated.midpoint(value) for value in oriented_values],
        dtype=np.complex128,
    )
    tail_radii = np.asarray(
        [frobenius.validated.radius_upper(value) for value in oriented_values],
        dtype=np.float64,
    )
    generic_differences = abs(tail_centers - generic_centers)
    if not bool(np.all(generic_differences <= tail_radii + generic_radii)):
        raise AssertionError("A397F tail misses the independent segmented enclosure")

    tail_rows = [
        {
            "residue_index_zero_based": index,
            "interval_bounds": encoded_values[index],
            "interval_center": encoded_complex(tail_centers[index]),
            "interval_radius_upper": float(tail_radii[index]),
            "segmented_tail_center_difference": float(generic_differences[index]),
            "segmented_tail_interval_overlaps": True,
        }
        for index in range(8)
    ]
    tail_payload = {
        "schema": "MTTQ79HeightFourD057FarCutFrobeniusTailInterval.v1",
        "status": "D057_FAR_CUT_FROBENIUS_TAIL_ALL_EIGHT_ROWS_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            **target,
            "endpoint_cutoff_epsilon": EPSILON,
            "Frobenius_branch_sign_against_segmented_tail": branch_sign,
        },
        "all_eight_endpoint_tails": {
            "rows": tail_rows,
            "interval_centers": [encoded_complex(value) for value in tail_centers],
            "interval_radius_uppers": tail_radii.tolist(),
            "maximum_interval_radius_upper": float(np.max(tail_radii)),
        },
        "quantitative_Hensel_disk": factor_diagnostics,
        "Frobenius_integral_diagnostics": tail_diagnostics,
        "comparison_to_segmented_tail": {
            "segmented_maximum_radius_upper": float(np.max(generic_radii)),
            "Frobenius_maximum_radius_upper": float(np.max(tail_radii)),
            "in_memory_Frobenius_maximum_radius_upper": float(np.max(raw_radii)),
            "radius_tightening_factor": float(np.max(generic_radii) / np.max(tail_radii)),
            "maximum_center_difference": float(np.max(generic_differences)),
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
            "A380FS_far_cut_source": authority(FAR_SOURCE),
            "A397_completed_far_main": authority(MAIN),
            "A397_segmented_tail_overlap_reference": authority(SEGMENTED_TAIL),
            "certified_d057_node": authority(NODE),
            "Frobenius_tail_engine": authority(Path(frobenius.__file__).resolve()),
            "full_precision_interval_serializer": authority(
                Path(interval_serializer.__file__).resolve()
            ),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_d057_geometry_used": True,
            "same_far_cut_epsilon_used": True,
            "quantitative_Hensel_factor_disk_closed": True,
            "finite_Frobenius_period_series_with_Cauchy_tail_used": True,
            "full_precision_interval_round_trip_used": True,
            "all_eight_far_cut_tail_rows_interval_closed": True,
            "segmented_tail_used_as_bound": False,
            "full_d057_splice_closed": False,
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
    differences = abs(floating - full_centers)
    if not bool(np.all(differences <= full_radii)):
        raise AssertionError("A397 Frobenius splice misses a floating diagnostic")
    canonical_maximum = float(canonical["summary"]["maximum_full_interval_radius_upper"])
    new_maximum = float(np.max(full_radii))
    if not new_maximum < canonical_maximum:
        raise AssertionError("A397 Frobenius splice does not tighten A246")
    rows = []
    for index in range(8):
        rows.append(
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
                "floating_to_interval_center_distance": float(differences[index]),
                "floating_value_contained": True,
                "containment_margin": float(full_radii[index] - differences[index]),
            }
        )
    chain_radii = abs(coefficient) * full_radii
    full_payload = {
        "schema": "MTTQ79HeightFourD057FarCutFullResidueInterval.v1",
        "status": "D057_FAR_CUT_FROBENIUS_FULL_EIGHT_ROW_CHAIN_INTERVAL_CERTIFIED",
        "artifact": "A397",
        "selected_target": {**target, "orientation_sign": orientation},
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": new_maximum,
            "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
            "selected_chain_product_disk_l2_radius_upper": float(np.linalg.norm(chain_radii)),
            "maximum_floating_center_difference": float(np.max(differences)),
            "minimum_floating_containment_margin": float(np.min(full_radii - differences)),
            "canonical_A246_maximum_full_interval_radius_upper": canonical_maximum,
            "A246_to_A397_maximum_radius_tightening_factor": canonical_maximum / new_maximum,
            "all_floating_values_contained": True,
        },
        "authority": {
            "A380FS_d057_far_cut_period_source": authority(FAR_SOURCE),
            "far_cut_main": authority(MAIN),
            "A397F_Frobenius_tail": authority(TAIL),
            "canonical_A246_d057_interval": authority(CANONICAL),
            "n3_target_cache": authority(THIMBLE),
            "A219_chain_coefficient": authority(generic.BOUNDARY),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "far_cut_period_source_interval_closed": True,
            "all_eight_far_cut_main_rows_interval_closed": True,
            "all_eight_Frobenius_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_period_vector_interval_closed": True,
            "selected_chain_contribution_interval_closed": True,
            "strictly_tighter_than_canonical_A246": True,
            "floating_values_used_as_bounds": False,
            "full_76_target_chain_recomposition_updated": False,
            "coupled_beta_period_residual_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "replace canonical d057 in the 76-target chain and rerank the "
            "remaining width sources"
        ),
    }
    dump(FULL, full_payload)
    TAIL_NOTE.write_text(
        "# MTT q79 Height-Four d057 Far-Cut Frobenius Tail (A397F) v1\n\n"
        "A397F evaluates the epsilon `1e-3` nodal tail with the existing "
        "quantitative-Hensel factor disk, finite Frobenius period series, Cauchy "
        "tail bound, and symmetric Taylor integration.\n\n"
        f"The maximum tail radius is `{np.max(tail_radii):.12g}`, compared with "
        f"`{np.max(generic_radii):.12g}` for the retired segmented enclosure.\n",
        encoding="utf-8",
    )
    FULL_NOTE.write_text(
        "# MTT q79 Height-Four d057 Far-Cut Full Residue (A397) v1\n\n"
        "A397 combines the completed far-cut main transport with the A397F "
        "Frobenius tail on the same selected d057 geometry.\n\n"
        f"The maximum full-row radius is `{new_maximum:.12g}`, tightening A246 "
        f"by `{canonical_maximum / new_maximum:.12g}`. All eight independent "
        "floating diagnostics are contained and are not used as bounds.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(TAIL)}")
    print(f"wrote {relative(FULL)}")
    print(json.dumps(full_payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
