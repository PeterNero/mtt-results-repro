from __future__ import annotations

import sys
from pathlib import Path

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed as deep_seed


TARGET_INDEX = 30
ADAPTER_SOURCE = Path(__file__).resolve()
DEEP_SEED_SOURCE = Path(deep_seed.__file__).resolve()
ORIGINAL_DUMP = generic.dump
ORIGINAL_ATOMIC_DUMP = generic.validated.atomic_dump
PRE_ATOMIC_ADAPTER_SHA256 = (
    "b869aa31f570117a61430837cc7aae5d8376f1f41f597b96b17229bb2d9773e0"
)


def source_entry(path: Path) -> dict[str, str]:
    return {
        "path": generic.relative(path),
        "sha256": generic.sha256(path),
    }


def selected_index(value: dict) -> int | None:
    selected = value.get("selected_target")
    if isinstance(selected, dict) and "distinguished_index" in selected:
        return int(selected["distinguished_index"])
    configuration = value.get("configuration")
    if isinstance(configuration, dict) and "index" in configuration:
        return int(configuration["index"])
    return None


def annotate_provenance(value: dict) -> None:
    if selected_index(value) == TARGET_INDEX:
        schema = value.get("schema")
        if schema == "MTTQ79HeightFourAllRowMainCheckpoint.v1":
            value["d030_seed_adapter"] = source_entry(ADAPTER_SOURCE)
            value["deep_radial_pair_seed_engine"] = source_entry(DEEP_SEED_SOURCE)
        elif schema in {
            "MTTQ79HeightFourTargetNodeInterval.v1",
            "MTTQ79HeightFourTargetFullResidueMainInterval.v1",
        }:
            authority = value.setdefault("authority", {})
            authority["d030_seed_adapter"] = source_entry(ADAPTER_SOURCE)
            authority["deep_radial_pair_seed_engine"] = source_entry(
                DEEP_SEED_SOURCE
            )
            value.setdefault("strict_scope", {})[
                "deep_radial_pair_used_for_seed_only"
            ] = True


def provenance_dump(path: Path, value: dict) -> None:
    annotate_provenance(value)
    ORIGINAL_DUMP(path, value)


def provenance_atomic_dump(path: Path, value: dict) -> None:
    annotate_provenance(value)
    ORIGINAL_ATOMIC_DUMP(path, value)


def certify_d030_node(system, critical: complex, *, epsilon: float, iterations: int):
    return deep_seed.certify_node_with_deep_pair_seed(
        system,
        critical,
        epsilon=epsilon,
        initial_parameter_radius=1.0e-20,
        initial_root_radius=1.0e-20,
        iterations=iterations,
    )


def requested_index(arguments: list[str]) -> int | None:
    for position, argument in enumerate(arguments):
        if argument == "--index" and position + 1 < len(arguments):
            return int(arguments[position + 1])
        if argument.startswith("--index="):
            return int(argument.split("=", 1)[1])
    return None


def validate_checkpoint_authority() -> None:
    checkpoint_path = generic.paths(TARGET_INDEX)["main_checkpoint"]
    if not checkpoint_path.exists():
        return
    checkpoint = generic.load(checkpoint_path)
    expected = {
        "d030_seed_adapter": source_entry(ADAPTER_SOURCE),
        "deep_radial_pair_seed_engine": source_entry(DEEP_SEED_SOURCE),
    }
    if all(checkpoint.get(key) == value for key, value in expected.items()):
        return
    node_path = generic.paths(TARGET_INDEX)["node"]
    node = generic.load(node_path) if node_path.exists() else {}
    node_authority = node.get("authority", {})
    adapter_hash = node_authority.get("d030_seed_adapter", {}).get("sha256")
    deep_hash = node_authority.get("deep_radial_pair_seed_engine", {}).get(
        "sha256"
    )
    missing_only = all(checkpoint.get(key) is None for key in expected)
    exact_pre_atomic_checkpoint = (
        missing_only
        and checkpoint.get("schema")
        == "MTTQ79HeightFourAllRowMainCheckpoint.v1"
        and int(checkpoint.get("configuration", {}).get("index", -1))
        == TARGET_INDEX
        and checkpoint.get("configuration", {}).get("root_id") == "selected_034"
        and checkpoint.get("source_sha256")
        == generic.sha256(Path(generic.__file__).resolve())
        and adapter_hash == PRE_ATOMIC_ADAPTER_SHA256
        and deep_hash == generic.sha256(DEEP_SEED_SOURCE)
    )
    if not exact_pre_atomic_checkpoint:
        raise ValueError(
            "d030 checkpoint adapter authority is absent or stale; "
            "refusing an ambiguous resume"
        )
    annotate_provenance(checkpoint)
    ORIGINAL_ATOMIC_DUMP(checkpoint_path, checkpoint)
    print("migrated exact pre-atomic d030 checkpoint authority", flush=True)


def main() -> int:
    index = requested_index(sys.argv[1:])
    if index != TARGET_INDEX:
        raise ValueError("the deep-pair adapter is restricted to --index 30")
    validate_checkpoint_authority()
    generic.main_engine.fast_certify_node = certify_d030_node
    generic.dump = provenance_dump
    generic.validated.atomic_dump = provenance_atomic_dump
    return generic.main()


if __name__ == "__main__":
    raise SystemExit(main())
