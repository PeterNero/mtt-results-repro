from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import certify_q79_height4_d082_zchart_full_residue_interval as z_helper
import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = Path(__file__).resolve()
HELPER = Path(z_helper.__file__).resolve()
INDEX = 79
ARTIFACT = "A240"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_arguments() -> None:
    try:
        index = int(sys.argv[sys.argv.index("--index") + 1])
    except (ValueError, IndexError) as error:
        raise ValueError("d079 z adapter requires --index 79") from error
    artifact = ""
    if "--artifact" in sys.argv:
        artifact = sys.argv[sys.argv.index("--artifact") + 1]
    if index != INDEX or artifact != ARTIFACT:
        raise ValueError("this adapter is frozen to d079/A240")


def stamp_payload(payload: dict) -> dict:
    stamped = z_helper.stamp_payload(payload)
    authority = stamped.get("authority")
    if isinstance(authority, dict):
        inherited = authority.pop("d082_z_chart_adapter", None)
        if inherited is not None:
            authority["d079_z_chart_adapter"] = inherited
        authority["A234_z_chart_helper_engine"] = {
            "path": relative(HELPER),
            "sha256": sha256(HELPER),
        }
    adapter = stamped.get("chart_adapter")
    if isinstance(adapter, dict):
        adapter["target"] = "d079/selected_066"
        adapter["helper_source"] = relative(HELPER)
        adapter["helper_source_sha256"] = sha256(HELPER)
    return stamped


def main() -> int:
    selected_arguments()
    z_helper.INDEX = INDEX
    z_helper.ADAPTER = ADAPTER
    z_helper.NODE_ROOT_BALL = None
    target_paths = generic.paths(INDEX)
    checkpoint_path = target_paths["main_checkpoint"]
    adapter_hash = sha256(ADAPTER)
    if checkpoint_path.exists():
        checkpoint = load(checkpoint_path)
        if checkpoint.get("z_chart_adapter_source_sha256") != adapter_hash:
            raise ValueError("d079 checkpoint predates or differs from the z adapter")
        if checkpoint.get("cutoff_pair_zero_based") != [4, 5]:
            raise ValueError("d079 checkpoint used a different cutoff pair")

    phase = "all"
    if "--phase" in sys.argv:
        phase = sys.argv[sys.argv.index("--phase") + 1]
    if phase in {"tail", "full"}:
        z_helper.load_certified_node_for_tail()

    original_dump = generic.dump
    original_atomic_dump = validated.atomic_dump

    def adapted_dump(path: Path, payload: dict) -> None:
        original_dump(path, stamp_payload(payload))

    def adapted_atomic_dump(path: Path, payload: dict) -> None:
        value = copy.deepcopy(payload)
        if value.get("schema") == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            value["line_chart"] = "z"
            value["z_chart_adapter_source_sha256"] = adapter_hash
            value["A123_sha256"] = sha256(z_helper.A123)
            value["z_chart_helper_engine_sha256"] = sha256(HELPER)
            value["cutoff_pair_selection_method"] = (
                "continued midpoint to certified double root"
            )
            value["cutoff_pair_zero_based"] = [4, 5]
        original_atomic_dump(path, value)

    generic.target = z_helper.z_target
    generic.main_engine.exact_target_system = z_helper.exact_z_system
    generic.main_engine.fast_certify_node = z_helper.certify_z_node
    generic.dump = adapted_dump
    validated.atomic_dump = adapted_atomic_dump
    result = generic.main()

    note = (
        ROOT
        / "proof_corpus"
        / "MTT_q79HeightFourD079ZChartRefinedFullResidueInterval_A240_v1.md"
    )
    full = load(target_paths["full"])
    summary = full["summary"]
    note.write_text(
        "# MTT q79 Height-Four d079 z-Chart Refined Full-Residue Interval "
        "(A240) v1\n\n"
        "A240 applies the A123-covariant native-z extension to `d079`. It "
        "instantiates the unchanged homogeneous n3 alignment in the z chart "
        "and certifies the node, main transport, local tail, orientation, and "
        "signed all-eight chain contribution.\n\n"
        "The deep radial node seed and interval-separated midpoint rule select "
        "the continued pair `[4,5]`; no instantaneous closest-pair premise is "
        "used.\n\n"
        f"The maximum full-row radius is "
        f"`{float(summary['maximum_full_interval_radius_upper']):.12g}` and the "
        f"coefficient-plus-two product-disk L2 radius is "
        f"`{float(summary['selected_chain_product_disk_l2_radius_upper']):.12g}`. "
        "All eight independent floating values lie inside their certified "
        "intervals and were not used as bounds.\n\n"
        "This closes A219 priority rank 10 only. It does not close the "
        "remaining chain, moving handle/beta intervals, an interval Jacobian, "
        "a covariant zero, or full SM closure.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(note)}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
