from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import certify_q79_height4_d082_zchart_full_residue_interval as z_helper
import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed as deep_seed
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = Path(__file__).resolve()
DEEP_SEED = Path(deep_seed.__file__).resolve()
PROBE = generic.PROBE_DIRECTORY
THIMBLE_DIRECTORY = PROBE.parent
BOUNDARY = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
VALIDATED = PROBE / "validated_transport"
MANIFEST = VALIDATED / "n3.dynamic_targets.manifest.json"

INDEX = -1
ARTIFACT = ""
RANK = -1
ROOT_ID = ""
COEFFICIENT = 0
CHART = ""
EXPECTED_PAIR: list[int] = []
PRIOR_NODE = Path()
NODE_ROOT_BALL = None


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def requested(name: str) -> str:
    try:
        return sys.argv[sys.argv.index(name) + 1]
    except (ValueError, IndexError) as error:
        raise ValueError(f"dynamic target adapter requires {name}") from error


def configure() -> None:
    global INDEX, ARTIFACT, RANK, ROOT_ID, COEFFICIENT, CHART, EXPECTED_PAIR, PRIOR_NODE
    INDEX = int(requested("--index"))
    ARTIFACT = requested("--artifact")
    boundary = load(BOUNDARY)
    ranked = boundary["difference_decomposition"]["ranked_thimble_contributions"]
    matches = [
        (rank, row)
        for rank, row in enumerate(ranked, start=1)
        if int(row["distinguished_index"]) == INDEX
    ]
    if len(matches) != 1:
        raise AssertionError(f"A219 does not select exactly one d{INDEX:03d} row")
    RANK, row = matches[0]
    if RANK < 16:
        raise ValueError("dynamic target adapter is frozen to A219 ranks 16 and later")
    expected_artifact = f"A{220 + 2 * RANK}"
    if ARTIFACT != expected_artifact:
        raise ValueError(
            f"A219 rank {RANK} requires artifact {expected_artifact}, not {ARTIFACT}"
        )
    ROOT_ID = row["root_id"]
    COEFFICIENT = int(row["signed_coefficient"])
    thimble = load(generic.paths(INDEX)["thimble"])
    if thimble["root_id"] != ROOT_ID:
        raise AssertionError("dynamic target cache root ID changed")
    CHART = thimble["line_chart"]
    if CHART not in {"y", "z"}:
        raise AssertionError(f"unsupported dynamic target chart {CHART!r}")
    PRIOR_NODE = THIMBLE_DIRECTORY / (
        f"d{INDEX:03d}_{ROOT_ID}.nodal_factor.interval.packet.json"
    )
    if not PRIOR_NODE.exists():
        raise FileNotFoundError(f"missing prior node-pair clue {PRIOR_NODE}")
    prior = load(PRIOR_NODE)
    EXPECTED_PAIR = [
        int(value)
        for value in prior["certified_node"]["incoming_closest_pair_zero_based"]
    ]
    if len(EXPECTED_PAIR) != 2 or EXPECTED_PAIR[0] >= EXPECTED_PAIR[1]:
        raise AssertionError("prior node-pair clue is malformed")


def assert_expected_pair(pair: tuple[int, int]) -> tuple[int, int]:
    if list(pair) != EXPECTED_PAIR:
        raise AssertionError(
            f"n3 node selected pair {list(pair)}, expected independently declared "
            f"pair {EXPECTED_PAIR}"
        )
    return pair


def y_pair(roots) -> tuple[tuple[int, int], dict]:
    if NODE_ROOT_BALL is None:
        raise AssertionError("dynamic y-chart certified node root is unavailable")
    distances = sorted(
        (
            validated.upper(abs(root - NODE_ROOT_BALL)),
            validated.lower(abs(root - NODE_ROOT_BALL)),
            index,
        )
        for index, root in enumerate(roots)
    )
    if distances[1][0] >= distances[2][1]:
        raise AssertionError("dynamic y-chart nodal roots are not interval-separated")
    pair = assert_expected_pair(tuple(sorted((distances[0][2], distances[1][2]))))
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
        raise AssertionError("dynamic y-chart cutoff root balls overlap")
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


def y_pair_only(roots) -> tuple[int, int]:
    return y_pair(roots)[0]


def install_y_pair_selectors() -> None:
    generic.pilot.closest_pair = y_pair
    generic.nodal.closest_pair = y_pair_only


def certify_y_node(system, critical: complex, *, epsilon: float, iterations: int):
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
    install_y_pair_selectors()
    return result


def z_pair(roots) -> tuple[tuple[int, int], dict]:
    pair, diagnostics = z_helper.certified_node_pair(roots)
    pair = assert_expected_pair(pair)
    value = dict(diagnostics)
    value["instantaneous_closest_pair_rule_used"] = False
    return pair, value


def z_pair_only(roots) -> tuple[int, int]:
    return z_pair(roots)[0]


def install_z_pair_selectors() -> None:
    generic.pilot.closest_pair = z_pair
    generic.nodal.closest_pair = z_pair_only


def certify_z_node(system, critical: complex, *, epsilon: float, iterations: int):
    result = z_helper.certify_z_node(
        system,
        critical,
        epsilon=epsilon,
        iterations=iterations,
    )
    install_z_pair_selectors()
    return result


def load_node_for_tail() -> None:
    global NODE_ROOT_BALL
    node_path = generic.paths(INDEX)["node"]
    if not node_path.exists():
        raise FileNotFoundError("dynamic tail requires the certified node packet")
    node = load(node_path)
    ball = validated.decoded_acb(node["certified_node"]["double_root_ball"])
    if CHART == "z":
        z_helper.NODE_ROOT_BALL = ball
        install_z_pair_selectors()
    else:
        NODE_ROOT_BALL = ball
        install_y_pair_selectors()


def stamp_payload(payload: dict) -> dict:
    if CHART == "z":
        stamped = z_helper.stamp_payload(payload)
    else:
        stamped = copy.deepcopy(payload)
    selected = stamped.get("selected_target")
    if isinstance(selected, dict):
        selected["line_chart"] = CHART
    authority = stamped.get("authority")
    if isinstance(authority, dict):
        authority.pop("d082_z_chart_adapter", None)
        authority["dynamic_target_adapter"] = {
            "path": relative(ADAPTER),
            "sha256": sha256(ADAPTER),
        }
        authority["deep_radial_pair_seed_engine"] = {
            "path": relative(DEEP_SEED),
            "sha256": sha256(DEEP_SEED),
        }
        authority["prior_E32_node_pair_clue"] = {
            "path": relative(PRIOR_NODE),
            "sha256": sha256(PRIOR_NODE),
        }
        if CHART == "z":
            authority["A234_z_chart_helper_engine"] = {
                "path": relative(Path(z_helper.__file__).resolve()),
                "sha256": sha256(Path(z_helper.__file__).resolve()),
            }
    scope = stamped.get("strict_scope")
    if isinstance(scope, dict):
        scope["certified_nodal_pair_selector_consumed"] = True
        scope["instantaneous_closest_pair_rule_used"] = False
        scope["prior_E32_pair_used_only_as_predeclared_consistency_check"] = True
    stamped["dynamic_target_adapter"] = {
        "A219_priority_rank": RANK,
        "artifact": ARTIFACT,
        "line_chart": CHART,
        "expected_pair_zero_based": EXPECTED_PAIR,
        "adapter_source": relative(ADAPTER),
        "adapter_source_sha256": sha256(ADAPTER),
        "prior_pair_clue": relative(PRIOR_NODE),
        "pair_reselected_by_n3_certified_node_geometry": True,
    }
    return stamped


def checkpoint_dump(original_atomic_dump):
    def adapted(path: Path, payload: dict) -> None:
        value = copy.deepcopy(payload)
        if value.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            value["line_chart"] = CHART
            value["dynamic_target_adapter_sha256"] = sha256(ADAPTER)
            value["deep_radial_pair_seed_engine_sha256"] = sha256(DEEP_SEED)
            value["prior_E32_node_pair_clue_sha256"] = sha256(PRIOR_NODE)
            value["cutoff_pair_zero_based"] = EXPECTED_PAIR
            value["cutoff_pair_selection_method"] = (
                "continued midpoint to certified double root"
                if CHART == "z"
                else "two roots nearest the certified double root"
            )
            if CHART == "z":
                value["A123_sha256"] = sha256(z_helper.A123)
        original_atomic_dump(path, value)

    return adapted


def validate_checkpoint(path: Path) -> None:
    if not path.exists():
        return
    checkpoint = load(path)
    if checkpoint.get("dynamic_target_adapter_sha256") != sha256(ADAPTER):
        raise ValueError("dynamic checkpoint adapter authority is stale")
    if checkpoint.get("cutoff_pair_zero_based") != EXPECTED_PAIR:
        raise ValueError("dynamic checkpoint used a different cutoff pair")
    if checkpoint.get("line_chart") != CHART:
        raise ValueError("dynamic checkpoint used a different line chart")


def update_manifest(full_path: Path) -> None:
    if MANIFEST.exists():
        manifest = load(MANIFEST)
        if manifest["schema"] != "MTTQ79HeightFourDynamicTargetManifest.v1":
            raise ValueError("dynamic target manifest schema changed")
        entries = [
            row
            for row in manifest["targets_in_A219_priority_order"]
            if int(row["distinguished_index"]) != INDEX
        ]
    else:
        entries = []
    entries.append(
        {
            "A219_priority_rank": RANK,
            "distinguished_index": INDEX,
            "root_id": ROOT_ID,
            "signed_coefficient": COEFFICIENT,
            "line_chart": CHART,
            "expected_pair_zero_based": EXPECTED_PAIR,
            "artifact": ARTIFACT,
            "full_interval_path": relative(full_path),
            "full_interval_sha256": sha256(full_path),
        }
    )
    entries.sort(key=lambda row: int(row["A219_priority_rank"]))
    ranks = [int(row["A219_priority_rank"]) for row in entries]
    if ranks != list(range(16, max(ranks) + 1)):
        raise AssertionError("dynamic target manifest is not a contiguous A219 suffix")
    dump(
        MANIFEST,
        {
            "schema": "MTTQ79HeightFourDynamicTargetManifest.v1",
            "status": "CONTIGUOUS_DYNAMIC_TARGET_INTERVALS_CERTIFIED",
            "target_count": len(entries),
            "first_A219_priority_rank": 16,
            "last_A219_priority_rank": max(ranks),
            "targets_in_A219_priority_order": entries,
            "authority": {
                "A219_profile_priority": {
                    "path": relative(BOUNDARY),
                    "sha256": sha256(BOUNDARY),
                },
                "dynamic_target_adapter": {
                    "path": relative(ADAPTER),
                    "sha256": sha256(ADAPTER),
                },
            },
        },
    )


def main() -> int:
    configure()
    target_paths = generic.paths(INDEX)
    validate_checkpoint(target_paths["main_checkpoint"])
    z_helper.INDEX = INDEX
    z_helper.ADAPTER = ADAPTER
    z_helper.NODE_ROOT_BALL = None

    phase = "all"
    if "--phase" in sys.argv:
        phase = sys.argv[sys.argv.index("--phase") + 1]
    if CHART == "z":
        generic.target = z_helper.z_target
        generic.main_engine.exact_target_system = z_helper.exact_z_system
        generic.main_engine.fast_certify_node = certify_z_node
    else:
        generic.main_engine.fast_certify_node = certify_y_node
    if phase in {"tail", "full"}:
        load_node_for_tail()

    original_dump = generic.dump
    original_atomic_dump = validated.atomic_dump

    def adapted_dump(path: Path, payload: dict) -> None:
        original_dump(path, stamp_payload(payload))

    generic.dump = adapted_dump
    validated.atomic_dump = checkpoint_dump(original_atomic_dump)
    result = generic.main()

    full = load(target_paths["full"])
    selected = full["selected_target"]
    if (
        full["artifact"] != ARTIFACT
        or int(selected["distinguished_index"]) != INDEX
        or selected["root_id"] != ROOT_ID
        or selected["line_chart"] != CHART
        or int(selected["selected_chain_coefficient"]) != COEFFICIENT
    ):
        raise AssertionError("dynamic full packet identity changed")
    summary = full["summary"]
    note = (
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{INDEX:03d}RefinedFullResidueInterval_{ARTIFACT}_v1.md"
    )
    note.write_text(
        f"# MTT q79 Height-Four d{INDEX:03d} Dynamic Full-Residue Interval "
        f"({ARTIFACT}) v1\n\n"
        f"{ARTIFACT} closes A219 priority rank {RANK} in the native `{CHART}` "
        f"chart with signed coefficient `{COEFFICIENT:+d}`. The prior E32 node "
        f"declares pair `{EXPECTED_PAIR}` only as a consistency target; the n3 "
        "interval-Newton node geometry independently reselects and separates "
        "that pair before both main and tail transport. No instantaneous "
        "closest-pair rule is used.\n\n"
        f"The maximum full-row radius is "
        f"`{float(summary['maximum_full_interval_radius_upper']):.12g}` and the "
        f"signed-chain product-disk L2 radius is "
        f"`{float(summary['selected_chain_product_disk_l2_radius_upper']):.12g}`. "
        "All eight floating diagnostics are contained and were not used as "
        "bounds.\n\n"
        "This closes one A219 target interval only. It does not close the "
        "remaining chain, moving handle/beta intervals, an interval Jacobian, "
        "a covariant zero, or full SM closure.\n",
        encoding="utf-8",
    )
    update_manifest(target_paths["full"])
    print(f"wrote {relative(note)}", flush=True)
    print(f"updated {relative(MANIFEST)}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
