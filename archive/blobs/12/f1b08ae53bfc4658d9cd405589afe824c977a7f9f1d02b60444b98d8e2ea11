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
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)
ADAPTER = Path(__file__).resolve()
DEEP_SEED = Path(deep_seed.__file__).resolve()
INDEX = 82
NODE_ROOT_BALL = None


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_arguments() -> tuple[int, str]:
    try:
        index = int(sys.argv[sys.argv.index("--index") + 1])
    except (ValueError, IndexError) as error:
        raise ValueError("d082 z adapter requires --index 82") from error
    artifact = "A226"
    if "--artifact" in sys.argv:
        artifact = sys.argv[sys.argv.index("--artifact") + 1]
    if index != INDEX:
        raise ValueError("this adapter is frozen to d082")
    if artifact != "A234":
        raise ValueError("this adapter is frozen to artifact A234")
    return index, artifact


def exact_z_system(dps: int) -> validated.SelectedQ79IntervalSystem:
    theorem = load(A123)
    if not theorem["theorem"]["proved"]:
        raise AssertionError("A123 projective chart covariance is unavailable")
    packet = generic.load(generic.FIBRATION)
    if packet["source"]["line_chart"] != "y":
        raise AssertionError("n3 homogeneous alignment source changed")
    system = validated.SelectedQ79IntervalSystem(dps=dps, line_chart="z")
    system.alignment = validated.decoded_matrix(packet["source"]["alignment_interval"])
    system.alignment_0 = system.alignment
    system.diagnostics = validated.IntervalSystemDiagnostics()
    if validated.lower(abs(system.alignment.det())) <= 0:
        raise AssertionError("n3 homogeneous alignment determinant contains zero")
    print("constructed A123-covariant native n3 z-chart interval system", flush=True)
    return system


def z_target(index: int) -> tuple[dict, dict[str, Path]]:
    target_paths = generic.paths(index)
    thimble = generic.load(target_paths["thimble"])
    if int(thimble["distinguished_index"]) != index:
        raise AssertionError("z adapter target cache identity changed")
    if thimble["line_chart"] != "z":
        raise AssertionError("d082 is no longer a z-chart target")
    return thimble, target_paths


def certify_z_node(system, critical: complex, *, epsilon: float, iterations: int):
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
    install_certified_node_pair_selectors()
    return result


def certified_node_pair(roots) -> tuple[tuple[int, int], dict]:
    if NODE_ROOT_BALL is None:
        raise AssertionError("certified d082 node root is unavailable")
    rows = []
    for left in range(len(roots)):
        for right in range(left + 1, len(roots)):
            midpoint = (roots[left] + roots[right]) / 2
            midpoint_distance = abs(midpoint - NODE_ROOT_BALL)
            separation = abs(roots[left] - roots[right])
            rows.append(
                {
                    "pair": (left, right),
                    "midpoint_to_certified_node_lower": validated.lower(
                        midpoint_distance
                    ),
                    "midpoint_to_certified_node_upper": validated.upper(
                        midpoint_distance
                    ),
                    "pair_distance_lower": validated.lower(separation),
                    "pair_distance_upper": validated.upper(separation),
                }
            )
    rows.sort(key=lambda row: row["midpoint_to_certified_node_upper"])
    selected, runner_up = rows[:2]
    if not (
        selected["midpoint_to_certified_node_upper"]
        < runner_up["midpoint_to_certified_node_lower"]
    ):
        raise AssertionError("continued d082 vanishing pair is not interval-separated")
    pair = selected["pair"]
    minimum_root_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    return pair, {
        "pair_selection_method": (
            "unique root-pair midpoint nearest the certified interval-Newton "
            "double root"
        ),
        "selected_pair_distance_lower": selected["pair_distance_lower"],
        "selected_pair_distance_upper": selected["pair_distance_upper"],
        "selected_pair_midpoint_to_node_upper": selected[
            "midpoint_to_certified_node_upper"
        ],
        "second_pair_midpoint_to_node_lower": runner_up[
            "midpoint_to_certified_node_lower"
        ],
        "second_to_selected_midpoint_distance_ratio_lower": (
            runner_up["midpoint_to_certified_node_lower"]
            / selected["midpoint_to_certified_node_upper"]
        ),
        "minimum_root_ball_separation_lower": minimum_root_separation,
    }


def certified_node_pair_only(roots) -> tuple[int, int]:
    return certified_node_pair(roots)[0]


def install_certified_node_pair_selectors() -> None:
    generic.pilot.closest_pair = certified_node_pair
    generic.nodal.closest_pair = certified_node_pair_only


def load_certified_node_for_tail() -> None:
    global NODE_ROOT_BALL
    node_path = generic.paths(INDEX)["node"]
    if not node_path.exists():
        raise FileNotFoundError("d082 tail requires the certified node packet")
    node = load(node_path)
    NODE_ROOT_BALL = validated.decoded_acb(
        node["certified_node"]["double_root_ball"]
    )
    install_certified_node_pair_selectors()


def stamp_payload(payload: dict) -> dict:
    stamped = copy.deepcopy(payload)
    selected = stamped.get("selected_target")
    if isinstance(selected, dict):
        selected["line_chart"] = "z"
    authority = stamped.get("authority")
    if isinstance(authority, dict):
        if "n3_y_fibration" in authority:
            authority["n3_homogeneous_alignment_interval"] = authority.pop(
                "n3_y_fibration"
            )
        authority["A123_projective_chart_covariance"] = {
            "path": relative(A123),
            "sha256": sha256(A123),
        }
        authority["d082_z_chart_adapter"] = {
            "path": relative(ADAPTER),
            "sha256": sha256(ADAPTER),
        }
        authority["deep_radial_pair_seed_engine"] = {
            "path": relative(DEEP_SEED),
            "sha256": sha256(DEEP_SEED),
        }
    scope = stamped.get("strict_scope")
    if isinstance(scope, dict):
        scope["A123_projective_z_chart_covariance_consumed"] = True
        scope["native_z_chart_interval_system_used"] = True
    stamped["chart_adapter"] = {
        "line_chart": "z",
        "A123_transition": "t_z=-(L0+L2*t_y)/L1",
        "fiber_scaling": "U_z=(L2/L1)^3*U_y",
        "five_period_transition_determinant": -1,
        "homogeneous_alignment_source": relative(generic.FIBRATION),
        "adapter_source": relative(ADAPTER),
        "adapter_source_sha256": sha256(ADAPTER),
        "cutoff_pair_selection": (
            "unique pair midpoint nearest the certified double root"
        ),
    }
    return stamped


def main() -> int:
    selected_arguments()
    target_paths = generic.paths(INDEX)
    checkpoint_path = target_paths["main_checkpoint"]
    adapter_hash = sha256(ADAPTER)
    if checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        if checkpoint.get("z_chart_adapter_source_sha256") != adapter_hash:
            raise ValueError("d082 checkpoint predates or differs from the z adapter")
        if checkpoint.get("cutoff_pair_zero_based") != [4, 5]:
            raise ValueError("d082 checkpoint used a different cutoff pair")

    phase = "all"
    if "--phase" in sys.argv:
        phase = sys.argv[sys.argv.index("--phase") + 1]
    if phase in {"tail", "full"}:
        load_certified_node_for_tail()

    original_dump = generic.dump
    original_atomic_dump = validated.atomic_dump

    def adapted_dump(path: Path, payload: dict) -> None:
        original_dump(path, stamp_payload(payload))

    def adapted_atomic_dump(path: Path, payload: dict) -> None:
        value = copy.deepcopy(payload)
        if value.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            value["line_chart"] = "z"
            value["z_chart_adapter_source_sha256"] = adapter_hash
            value["A123_sha256"] = sha256(A123)
            value["deep_radial_pair_seed_engine_sha256"] = sha256(DEEP_SEED)
            value["cutoff_pair_selection_method"] = (
                "continued midpoint to certified double root"
            )
            value["cutoff_pair_zero_based"] = [4, 5]
        original_atomic_dump(path, value)

    generic.target = z_target
    generic.main_engine.exact_target_system = exact_z_system
    generic.main_engine.fast_certify_node = certify_z_node
    generic.dump = adapted_dump
    validated.atomic_dump = adapted_atomic_dump
    result = generic.main()

    note = (
        ROOT
        / "proof_corpus"
        / "MTT_q79HeightFourD082ZChartRefinedFullResidueInterval_A234_v1.md"
    )
    full = load(target_paths["full"])
    summary = full["summary"]
    note.write_text(
        "# MTT q79 Height-Four d082 z-Chart Refined Full-Residue Interval "
        "(A234) v1\n\n"
        "A234 is the native-z conservative extension of the frozen generic "
        "all-eight target engine. It consumes the exact A123 y/z projective "
        "chart theorem, instantiates the same homogeneous n3 alignment with "
        "`line_chart=\"z\"`, and certifies the node, main transport, local "
        "tail, orientation, and signed chain contribution for `d082`.\n\n"
        "The deep radial seed identifies pair `[4,5]`; at the integration "
        "cutoff that pair is selected by its interval-separated midpoint "
        "continuation to the certified double root, rather than by raw pair "
        "length.\n\n"
        f"The maximum full-row radius is "
        f"`{float(summary['maximum_full_interval_radius_upper']):.12g}` and the "
        f"coefficient-minus-two product-disk L2 radius is "
        f"`{float(summary['selected_chain_product_disk_l2_radius_upper']):.12g}`. "
        "All eight independent floating values lie inside their intervals and "
        "were not used as error bounds.\n\n"
        "This closes the first n3 all-eight z-chart target and the A233 leading "
        "chart blocker. It does not close the remaining chain, moving "
        "handle/beta intervals, an interval Jacobian, a covariant zero, or full "
        "SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(note)}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
