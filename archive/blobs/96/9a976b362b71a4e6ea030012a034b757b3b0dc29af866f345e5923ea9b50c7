from __future__ import annotations

import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from flint import ctx

import certify_q79_height4_d027_continued_pair_full_residue_interval as adapter
import certify_q79_height4_target_full_residue_interval as generic
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
INDEX = 27
EPSILON = 1.0e-3
SOURCE = VALIDATED / "far_source" / "d027.1em03.json"
NODE = VALIDATED / "d027.n3.node.refined.json"
CANONICAL_PATHS = generic.paths(INDEX)
OUTPUT = VALIDATED / "far_residue" / "d027.tail_segmented.a406r.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD027FarCutSegmentedTailReference_A406R_v1.md"
ARTIFACT = "A406R"


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


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def selected_paths(index: int) -> dict[str, Path]:
    if index != INDEX:
        raise ValueError("A406R is frozen to d027")
    return {
        **CANONICAL_PATHS,
        "node": NODE,
        "tail": OUTPUT,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--factor-order", type=int, default=32)
    parser.add_argument("--node-width", type=float, default=1.0e-10)
    parser.add_argument("--outer-segments", type=int, default=9600)
    parser.add_argument("--theta-segments", type=int, default=32)
    arguments = parser.parse_args()
    if arguments.dps < 90 or arguments.factor_order < 24:
        raise ValueError("A406R requires at least 90 digits and factor order 24")
    if not 0.0 < arguments.node_width < EPSILON:
        raise ValueError("A406R node width must lie inside the selected tail")
    source = load(SOURCE)
    target = source["selected_target"]
    if (
        source.get("artifact") != "A380FS"
        or int(target["distinguished_index"]) != INDEX
        or target["root_id"] != "selected_011"
        or list(target["preselected_pair_zero_based"]) != [1, 2]
        or float(target["selected_far_cut_epsilon"]) != EPSILON
    ):
        raise AssertionError("A406R selected source changed")
    ctx.dps = arguments.dps
    node = load(NODE)
    adapter.NODE_ROOT_BALL = validated.decoded_acb(
        node["certified_node"]["double_root_ball"]
    )
    original_paths = generic.paths
    original_pilot_pair = generic.pilot.closest_pair
    original_nodal_pair = generic.nodal.closest_pair
    adapter.install_pair_selectors()
    generic.paths = selected_paths
    try:
        packet = generic.execute_tail(
            Namespace(
                index=INDEX,
                epsilon=EPSILON,
                tail_dps=arguments.dps,
                factor_order=arguments.factor_order,
                node_width=arguments.node_width,
                outer_segments=arguments.outer_segments,
                theta_segments=arguments.theta_segments,
            )
        )
    finally:
        generic.paths = original_paths
        generic.pilot.closest_pair = original_pilot_pair
        generic.nodal.closest_pair = original_nodal_pair
    packet["artifact"] = ARTIFACT
    packet["status"] = "D027_FAR_CUT_SEGMENTED_TAIL_BRANCH_REFERENCE_CERTIFIED"
    packet["authority"]["A380FS_d027_far_cut_source"] = authority(SOURCE)
    packet["authority"]["d027_continued_pair_adapter"] = authority(
        Path(adapter.__file__).resolve()
    )
    packet["authority"]["builder_source"] = authority(Path(__file__).resolve())
    packet["strict_scope"].update(
        {
            "selected_far_cut_epsilon_used": True,
            "certified_nodal_pair_selector_consumed": True,
            "instantaneous_closest_pair_rule_used": False,
            "accepted_as_final_d027_tail_bound": False,
            "branch_overlap_reference_only": True,
            "full_d027_period_vector_interval_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        }
    )
    packet["next_required_artifact"] = (
        "use this independent enclosure only to choose the unique sign of the "
        "tight A406F quantitative-Hensel/Frobenius tail"
    )
    endpoint = packet["all_eight_endpoint_tails"]
    serialized_balls = [
        validated.interval_from_bounds(value) for value in endpoint["intervals"]
    ]
    endpoint["interval_centers"] = [
        encoded_complex(validated.midpoint(value)) for value in serialized_balls
    ]
    endpoint["interval_radius_uppers"] = [
        validated.radius_upper(value) for value in serialized_balls
    ]
    endpoint["maximum_interval_radius_upper"] = max(
        endpoint["interval_radius_uppers"]
    )
    packet["strict_scope"]["full_precision_interval_round_trip_used"] = True
    dump(OUTPUT, packet)
    maximum = float(
        packet["all_eight_endpoint_tails"]["maximum_interval_radius_upper"]
    )
    NOTE.write_text(
        "# MTT q79 Height-Four d027 Far-Cut Segmented Tail Reference (A406R) v1\n\n"
        "A406R executes the independently certified continued d027 pair over the "
        "epsilon `1e-3` tail. Its role is only to select the global sign of the "
        "tight Frobenius tail; its radii are not promoted into the final d027 bound.\n\n"
        f"The maximum coarse reference radius is `{maximum:.12g}`.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(json.dumps({"maximum_reference_radius_upper": maximum}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
