from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
HANDLES = DIRECTORY / "selected_alignment_handle_monodromy"
ADAPTERS = DIRECTORY / "selected_alignment_meridian_monodromy"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    for index, name in ((91, "A"), (92, "B")):
        source_path = HANDLES / f"handle_{name}.packet.json"
        source = json.loads(source_path.read_text(encoding="utf-8"))
        trajectory_path = ROOT / source["trajectory"]["path"]
        if sha256(trajectory_path) != source["trajectory"]["sha256"]:
            raise AssertionError(f"selected handle {name} trajectory hash mismatch")
        adapter = {
            "schema": "MTTQ79SelectedAlignmentHandleRootTubeAdapter.v1",
            "status": "SELECTED_ALIGNMENT_HANDLE_TRAJECTORY_TYPED_FOR_ROOT_TUBE_CERTIFIER",
            "root_id": f"handle_{name}",
            "distinguished_index": index,
            "authority": {
                "handle_monodromy_packet_path": str(source_path.relative_to(ROOT)).replace("\\", "/"),
                "handle_monodromy_packet_sha256": sha256(source_path),
                "fibration_sha256": source["authority"]["fibration_sha256"],
                "handle_paths_sha256": source["authority"]["handle_paths_sha256"],
                "homology_convention_sha256": source["authority"]["homology_convention_sha256"],
            },
            "branch_chart": source["branch_chart"],
            "trajectory": source["trajectory"],
            "transport": source["transport"],
            "strict_scope": {
                "adapter_changes_numeric_data": False,
                "continuous_root_tubes_certified": False,
                "handle_monodromy_promoted": False,
            },
        }
        output = ADAPTERS / f"d{index:03d}_handle_{name}.packet.json"
        output.write_text(
            json.dumps(adapter, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
