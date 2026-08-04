from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from flint import ctx

import certify_q79_height4_dynamic_target_full_residue_interval as dynamic
import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PROBE = generic.PROBE_DIRECTORY
VALIDATED = PROBE / "validated_transport"
TIGHT = VALIDATED / "tight"
BOUNDARY = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
THIMBLE_DIRECTORY = PROBE.parent
ORIGINAL_PATHS = generic.paths
ORIGINAL_TARGET = generic.target
ORIGINAL_EXACT_TARGET_SYSTEM = generic.main_engine.exact_target_system


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


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def canonical_paths(index: int) -> dict[str, Path]:
    return ORIGINAL_PATHS(index)


def tight_paths(index: int) -> dict[str, Path]:
    canonical = canonical_paths(index)
    stem = f"d{index:03d}.n3.tight"
    return {
        "thimble": canonical["thimble"],
        "node": TIGHT / f"{stem}.node.json",
        "main": TIGHT / f"{stem}.main8.json",
        "main_checkpoint": TIGHT / f"{stem}.main8.checkpoint.json",
        "tail": TIGHT / f"{stem}.tail8.json",
        "full": TIGHT / f"{stem}.full8.json",
    }


def configure_selected_target(index: int) -> tuple[int, dict, Path]:
    boundary = load(BOUNDARY)
    ranked = boundary["difference_decomposition"]["ranked_thimble_contributions"]
    matches = [
        (rank, row)
        for rank, row in enumerate(ranked, start=1)
        if int(row["distinguished_index"]) == index
    ]
    if len(matches) != 1:
        raise AssertionError(f"A219 does not select exactly one d{index:03d} row")
    rank, row = matches[0]
    thimble = load(canonical_paths(index)["thimble"])
    if thimble["root_id"] != row["root_id"]:
        raise AssertionError("A219 and the n3 thimble cache disagree on root ID")
    prior_node = THIMBLE_DIRECTORY / (
        f"d{index:03d}_{row['root_id']}.nodal_factor.interval.packet.json"
    )
    prior = load(prior_node)
    expected_pair = [
        int(value)
        for value in prior["certified_node"]["incoming_closest_pair_zero_based"]
    ]
    if len(expected_pair) != 2 or expected_pair[0] >= expected_pair[1]:
        raise AssertionError("predeclared E32 nodal pair is malformed")

    dynamic.INDEX = index
    dynamic.RANK = rank
    dynamic.ROOT_ID = row["root_id"]
    dynamic.COEFFICIENT = int(row["signed_coefficient"])
    dynamic.CHART = thimble["line_chart"]
    dynamic.EXPECTED_PAIR = expected_pair
    dynamic.PRIOR_NODE = prior_node
    dynamic.NODE_ROOT_BALL = None
    dynamic.z_helper.INDEX = index
    dynamic.z_helper.ADAPTER = Path(__file__).resolve()
    dynamic.z_helper.NODE_ROOT_BALL = None
    return rank, row, prior_node


def install_target_adapters(index: int, chart: str) -> None:
    generic.paths = tight_paths
    if chart == "z":
        generic.target = dynamic.z_helper.z_target
        generic.main_engine.exact_target_system = dynamic.z_helper.exact_z_system
        generic.main_engine.fast_certify_node = dynamic.certify_z_node
    elif chart == "y":
        generic.target = ORIGINAL_TARGET
        generic.main_engine.exact_target_system = ORIGINAL_EXACT_TARGET_SYSTEM
        generic.main_engine.fast_certify_node = dynamic.certify_y_node
    else:
        raise AssertionError(f"unsupported target chart {chart!r}")


def combine_full(
    arguments: argparse.Namespace,
    *,
    rank: int,
    row: dict,
    prior_node: Path,
) -> dict:
    target_paths = tight_paths(arguments.index)
    canonical = canonical_paths(arguments.index)
    thimble = load(target_paths["thimble"])
    main_packet = load(target_paths["main"])
    tail_path = target_paths["tail"] if target_paths["tail"].exists() else canonical["tail"]
    tail_packet = load(tail_path)
    canonical_full = load(canonical["full"])

    orientation = int(canonical_full["selected_target"]["orientation_sign"])
    if int(main_packet["orientation"]["selected_sign"]) != orientation:
        raise AssertionError("tight main transport changed the preselected orientation")
    coefficient = int(row["signed_coefficient"])
    if coefficient != int(canonical_full["selected_target"]["selected_chain_coefficient"]):
        raise AssertionError("tight refinement changed the selected chain coefficient")

    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [
            complex_value(value)
            for value in tail_packet["all_eight_endpoint_tails"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    differences = abs(floating - full_centers)
    contained = differences <= full_radii
    if not bool(np.all(contained)):
        raise AssertionError(
            f"d{arguments.index:03d} floating vector left tight intervals: "
            f"{np.flatnonzero(~contained).tolist()}"
        )
    chain_radii = abs(coefficient) * full_radii
    old_l2 = float(
        canonical_full["summary"]["selected_chain_product_disk_l2_radius_upper"]
    )
    new_l2 = float(np.linalg.norm(chain_radii))
    radius_improved = new_l2 < old_l2
    if not radius_improved and not arguments.allow_nonimproving_full:
        raise AssertionError(
            f"tight refinement did not improve the chain radius: {new_l2} >= {old_l2}"
        )

    rows = []
    for residue_index in range(8):
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "full_interval_center": encoded_complex(full_centers[residue_index]),
                "full_interval_radius_upper": float(full_radii[residue_index]),
                "selected_chain_contribution_center": encoded_complex(
                    coefficient * full_centers[residue_index]
                ),
                "selected_chain_contribution_radius_upper": float(
                    abs(coefficient) * full_radii[residue_index]
                ),
                "floating_value_diagnostic_only": encoded_complex(
                    floating[residue_index]
                ),
                "floating_to_interval_center_distance": float(
                    differences[residue_index]
                ),
                "floating_value_contained": bool(contained[residue_index]),
                "containment_margin": float(
                    full_radii[residue_index] - differences[residue_index]
                ),
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourTightTargetFullResidueInterval.v1",
        "status": (
            "N3_TIGHT_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_CERTIFIED"
            if radius_improved
            else "N3_MATCHED_CUTOFF_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_CERTIFIED"
        ),
        "selected_target": {
            "A219_priority_rank": rank,
            "distinguished_index": arguments.index,
            "root_id": row["root_id"],
            "line_chart": dynamic.CHART,
            "orientation_sign": orientation,
            "selected_chain_coefficient": coefficient,
            "expected_pair_zero_based": dynamic.EXPECTED_PAIR,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": float(np.max(full_radii)),
            "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
            "selected_chain_product_disk_l2_radius_upper": new_l2,
            "canonical_chain_product_disk_l2_radius_upper": old_l2,
            "radius_reduction_factor": old_l2 / new_l2,
            "strict_radius_improvement": radius_improved,
            "maximum_floating_center_difference": float(np.max(differences)),
            "minimum_floating_containment_margin": float(
                np.min(full_radii - differences)
            ),
            "all_floating_values_contained": bool(np.all(contained)),
            "canonical_tail_reused": tail_path == canonical["tail"],
        },
        "authority": {
            "A219_profile_boundary": {
                "path": relative(BOUNDARY),
                "sha256": sha256(BOUNDARY),
            },
            "canonical_full_interval": {
                "path": relative(canonical["full"]),
                "sha256": sha256(canonical["full"]),
            },
            "tight_main_interval": {
                "path": relative(target_paths["main"]),
                "sha256": sha256(target_paths["main"]),
            },
            "tail_interval": {
                "path": relative(tail_path),
                "sha256": sha256(tail_path),
            },
            "prior_E32_node_pair_clue": {
                "path": relative(prior_node),
                "sha256": sha256(prior_node),
            },
            "frozen_dynamic_target_kernel": {
                "path": relative(Path(dynamic.__file__).resolve()),
                "sha256": sha256(Path(dynamic.__file__).resolve()),
            },
            "generic_interval_kernel": {
                "path": relative(Path(generic.__file__).resolve()),
                "sha256": sha256(Path(generic.__file__).resolve()),
            },
            "builder_source": {
                "path": relative(Path(__file__).resolve()),
                "sha256": sha256(Path(__file__).resolve()),
            },
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "selected_chain_and_orientation_inherited_before_refinement": True,
            "predeclared_nodal_pair_reselected_by_interval_geometry": True,
            "tight_main_rows_interval_closed": True,
            "tight_tail_rows_interval_closed": tail_path == target_paths["tail"],
            "canonical_tail_interval_reused": tail_path == canonical["tail"],
            "tight_full_period_vector_interval_closed": True,
            "tight_radius_improvement_closed": radius_improved,
            "floating_values_used_as_bounds": False,
            "interval_Jacobian_certificate": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "replace the dominant canonical target radii by tight refinements, "
            "then build a tight full-chain residual and interval Jacobian gate"
        ),
    }
    dump(target_paths["full"], payload)
    print(f"wrote {relative(target_paths['full'])}", flush=True)
    print(json.dumps(payload["summary"], indent=2), flush=True)
    return payload


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--phase", choices=("main", "tail", "full", "all"), default="all")
    value.add_argument("--epsilon", type=float, default=1.0e-5)
    value.add_argument("--node-iterations", type=int, default=3)
    value.add_argument("--main-dps", type=int, default=100)
    value.add_argument("--order", type=int, default=40)
    value.add_argument("--maximum-step", type=float, default=0.0015)
    value.add_argument("--minimum-step", type=float, default=1.0e-13)
    value.add_argument("--maximum-lift-correction", type=float, default=1.0e-15)
    value.add_argument("--maximum-integral-radius", type=float, default=2.0e-6)
    value.add_argument("--cut-segments", type=int, default=40)
    value.add_argument("--cut-tolerance", type=float, default=1.0e-50)
    value.add_argument("--tail-dps", type=int, default=110)
    value.add_argument("--node-width", type=float, default=1.0e-11)
    value.add_argument("--outer-segments", type=int, default=19200)
    value.add_argument("--theta-segments", type=int, default=48)
    value.add_argument("--factor-order", type=int, default=40)
    value.add_argument("--cooling-pause-every", type=int, default=20)
    value.add_argument("--cooling-pause-seconds", type=float, default=2.0)
    value.add_argument("--allow-nonimproving-full", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    if not 0.0 < arguments.node_width < arguments.epsilon < 0.01:
        raise ValueError("require 0 < node width < epsilon < 0.01")
    rank, row, prior_node = configure_selected_target(arguments.index)
    install_target_adapters(arguments.index, dynamic.CHART)
    TIGHT.mkdir(parents=True, exist_ok=True)
    priority_lowered = generic.set_below_normal_priority()
    print(
        f"tight refinement below-normal priority applied={priority_lowered}; "
        f"rank={rank} d{arguments.index:03d} chart={dynamic.CHART}",
        flush=True,
    )

    if arguments.phase in {"main", "all"}:
        ctx.dps = arguments.main_dps
        generic.execute_main(arguments)
    if arguments.phase in {"tail", "all"}:
        dynamic.load_node_for_tail()
        ctx.dps = arguments.tail_dps
        generic.execute_tail(arguments)
    if arguments.phase in {"full", "all"}:
        combine_full(arguments, rank=rank, row=row, prior_node=prior_node)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
