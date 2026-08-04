from __future__ import annotations

import copy
import sys

import certify_q79_height4_dynamic_target_full_residue_interval as dynamic


def main() -> int:
    """Run only the frozen dynamic adapter's target-local main phase."""
    if "--phase" not in sys.argv or sys.argv[sys.argv.index("--phase") + 1] != "main":
        raise ValueError("precompute worker requires --phase main")

    dynamic.configure()
    generic = dynamic.generic
    target_paths = generic.paths(dynamic.INDEX)
    dynamic.validate_checkpoint(target_paths["main_checkpoint"])
    dynamic.z_helper.INDEX = dynamic.INDEX
    dynamic.z_helper.ADAPTER = dynamic.ADAPTER
    dynamic.z_helper.NODE_ROOT_BALL = None

    if dynamic.CHART == "z":
        generic.target = dynamic.z_helper.z_target
        generic.main_engine.exact_target_system = dynamic.z_helper.exact_z_system
        generic.main_engine.fast_certify_node = dynamic.certify_z_node
    else:
        generic.main_engine.fast_certify_node = dynamic.certify_y_node

    original_dump = generic.dump
    original_atomic_dump = dynamic.validated.atomic_dump

    def adapted_dump(path, payload: dict) -> None:
        original_dump(path, dynamic.stamp_payload(copy.deepcopy(payload)))

    generic.dump = adapted_dump
    dynamic.validated.atomic_dump = dynamic.checkpoint_dump(original_atomic_dump)
    return generic.main()


if __name__ == "__main__":
    raise SystemExit(main())
