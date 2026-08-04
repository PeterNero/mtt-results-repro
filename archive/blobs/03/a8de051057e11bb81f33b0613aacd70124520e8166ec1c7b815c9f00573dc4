from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed as deep_seed
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = Path(__file__).resolve()
DEEP_SEED = Path(deep_seed.__file__).resolve()
INDEX = 57
ARTIFACT = "A246"
EXPECTED_PAIR = [3, 4]
NODE_ROOT_BALL = None


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_arguments() -> None:
    if "--index" not in sys.argv or int(sys.argv[sys.argv.index("--index") + 1]) != INDEX:
        raise ValueError("this adapter is frozen to --index 57")
    artifact = ""
    if "--artifact" in sys.argv:
        artifact = sys.argv[sys.argv.index("--artifact") + 1]
    if artifact != ARTIFACT:
        raise ValueError("this adapter is frozen to artifact A246")


def certify_node(system, critical: complex, *, epsilon: float, iterations: int):
    global NODE_ROOT_BALL
    result = deep_seed.certify_node_with_deep_pair_seed(
        system,
        critical,
        epsilon=epsilon,
        initial_parameter_radius=1.0e-20,
        initial_root_radius=1.0e-20,
        iterations=iterations,
    )
    NODE_ROOT_BALL = result[1]
    install_pair_selectors()
    return result


def continued_pair(roots) -> tuple[tuple[int, int], dict]:
    if NODE_ROOT_BALL is None:
        raise AssertionError("certified d057 node root is unavailable")
    distances = sorted(
        (
            validated.upper(abs(root - NODE_ROOT_BALL)),
            validated.lower(abs(root - NODE_ROOT_BALL)),
            index,
        )
        for index, root in enumerate(roots)
    )
    if distances[1][0] >= distances[2][1]:
        raise AssertionError(
            "two d057 roots nearest the certified node are not interval-separated"
        )
    pair = tuple(sorted((distances[0][2], distances[1][2])))
    pair_distance = abs(roots[pair[0]] - roots[pair[1]])
    other_pair_distances = [
        abs(roots[left] - roots[right])
        for left in range(len(roots))
        for right in range(left)
        if {left, right} != set(pair)
    ]
    minimum_root_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    if minimum_root_separation <= 0.0:
        raise AssertionError("d057 cutoff root balls overlap")
    return pair, {
        "pair_selection_method": (
            "two cutoff roots nearest the independently certified nodal "
            "double-root ball"
        ),
        "instantaneous_closest_pair_rule_used": False,
        "selected_pair_distance_lower": validated.lower(pair_distance),
        "selected_pair_distance_upper": validated.upper(pair_distance),
        "second_pair_distance_lower": min(
            validated.lower(value) for value in other_pair_distances
        ),
        "minimum_root_ball_separation_lower": minimum_root_separation,
        "selected_root_to_node_distance_upper": max(distances[0][0], distances[1][0]),
        "next_root_to_node_distance_lower": distances[2][1],
        "node_affinity_separation_margin_lower": (
            distances[2][1] - max(distances[0][0], distances[1][0])
        ),
    }


def continued_pair_only(roots) -> tuple[int, int]:
    return continued_pair(roots)[0]


def install_pair_selectors() -> None:
    generic.pilot.closest_pair = continued_pair
    generic.nodal.closest_pair = continued_pair_only


def load_node_for_tail() -> None:
    global NODE_ROOT_BALL
    path = generic.paths(INDEX)["node"]
    if not path.exists():
        raise FileNotFoundError("d057 tail requires the certified node packet")
    node = load(path)
    NODE_ROOT_BALL = validated.decoded_acb(
        node["certified_node"]["double_root_ball"]
    )
    install_pair_selectors()


def stamp_payload(payload: dict) -> dict:
    value = copy.deepcopy(payload)
    authority = value.get("authority")
    if isinstance(authority, dict):
        authority["d057_continued_pair_adapter"] = {
            "path": relative(ADAPTER),
            "sha256": sha256(ADAPTER),
        }
        authority["deep_radial_pair_seed_engine"] = {
            "path": relative(DEEP_SEED),
            "sha256": sha256(DEEP_SEED),
        }
    scope = value.get("strict_scope")
    if isinstance(scope, dict):
        scope["certified_nodal_pair_selector_consumed"] = True
        scope["instantaneous_closest_pair_rule_used"] = False
    value["continued_pair_adapter"] = {
        "method": (
            "two cutoff roots nearest the independently certified nodal "
            "double-root ball"
        ),
        "adapter_source": relative(ADAPTER),
        "adapter_source_sha256": sha256(ADAPTER),
    }
    return value


def main() -> int:
    selected_arguments()
    paths = generic.paths(INDEX)
    checkpoint_path = paths["main_checkpoint"]
    adapter_hash = sha256(ADAPTER)
    if checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        if checkpoint.get("d057_continued_pair_adapter_sha256") != adapter_hash:
            raise ValueError("d057 checkpoint adapter authority is stale")
        if checkpoint.get("cutoff_pair_zero_based") != EXPECTED_PAIR:
            raise ValueError("d057 checkpoint used a different cutoff pair")

    phase = "all"
    if "--phase" in sys.argv:
        phase = sys.argv[sys.argv.index("--phase") + 1]
    if phase in {"tail", "full"}:
        load_node_for_tail()

    original_dump = generic.dump
    original_atomic_dump = validated.atomic_dump

    def adapted_dump(path: Path, payload: dict) -> None:
        original_dump(path, stamp_payload(payload))

    def adapted_atomic_dump(path: Path, payload: dict) -> None:
        value = copy.deepcopy(payload)
        if value.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            value["d057_continued_pair_adapter_sha256"] = adapter_hash
            value["deep_radial_pair_seed_engine_sha256"] = sha256(DEEP_SEED)
            value["cutoff_pair_zero_based"] = EXPECTED_PAIR
            value["cutoff_pair_selection_method"] = (
                "two roots nearest the certified double root"
            )
        original_atomic_dump(path, value)

    generic.main_engine.fast_certify_node = certify_node
    generic.dump = adapted_dump
    validated.atomic_dump = adapted_atomic_dump
    result = generic.main()

    full = load(paths["full"])
    summary = full["summary"]
    note = (
        ROOT
        / "proof_corpus"
        / "MTT_q79HeightFourD057RefinedFullResidueInterval_A246_v1.md"
    )
    note.write_text(
        "# MTT q79 Height-Four d057 Refined Full-Residue Interval "
        "(A246) v1\n\n"
        "A246 transports the frozen certified-node pair theorem to the n3 "
        "all-eight geometry. A deep radial seed identifies the vanishing pair; "
        "at the cutoff the two roots nearest the interval-Newton double-root "
        "ball are strictly separated from the next root and used in both main "
        "and tail transports. The instantaneous shortest-pair shortcut is not "
        "used.\n\n"
        f"The maximum full-row radius is "
        f"`{float(summary['maximum_full_interval_radius_upper']):.12g}` and the "
        f"coefficient-plus-four product-disk L2 radius is "
        f"`{float(summary['selected_chain_product_disk_l2_radius_upper']):.12g}`. "
        "All eight independent floating values are contained and were not used "
        "as error bounds.\n\n"
        "This closes A219 rank 13 only. It does not close the remaining chain, "
        "moving handle/beta intervals, an interval Jacobian, a covariant zero, "
        "or full SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(note)}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
