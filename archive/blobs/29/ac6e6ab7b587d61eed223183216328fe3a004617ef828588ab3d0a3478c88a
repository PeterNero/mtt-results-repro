from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
DIRECTORY = VALIDATED / "ol"
SOURCE = DIRECTORY / "ha.src.a418.json"
CHECKPOINT = DIRECTORY / "ha.a418.ckpt.json"
OUTPUT = DIRECTORY / "ha.a418r.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA418AuthorityOnlyCheckpointRebind_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def atomic_dump(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def git_head_json(path: Path) -> dict[str, Any]:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative(path)}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def difference_paths(left: Any, right: Any, prefix: str = "") -> list[str]:
    if type(left) is not type(right):
        return [prefix or "<root>"]
    if isinstance(left, dict):
        paths: list[str] = []
        for key in sorted(set(left) | set(right)):
            child = f"{prefix}.{key}" if prefix else str(key)
            if key not in left or key not in right:
                paths.append(child)
            else:
                paths.extend(difference_paths(left[key], right[key], child))
        return paths
    if isinstance(left, list):
        if len(left) != len(right):
            return [prefix or "<root>"]
        paths: list[str] = []
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            paths.extend(difference_paths(left_item, right_item, f"{prefix}[{index}]"))
        return paths
    return [] if left == right else [prefix or "<root>"]


def normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A418_source_sha256", None)
    normalized.pop("path_name", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    arguments = parser.parse_args()

    source = load(SOURCE)
    source_differences = difference_paths(git_head_json(SOURCE), source)
    expected_source_differences = [
        "authority.A404_operational_path.sha256",
        "authority.A411_terminal_trunk.sha256",
    ]
    if source_differences != expected_source_differences:
        raise AssertionError(
            f"A418 source change is not authority-only: {source_differences}"
        )
    if source["authority"]["A404_operational_path"]["sha256"] != sha256(A404):
        raise AssertionError("A418 source does not bind current A404")
    if source["authority"]["A411_terminal_trunk"]["sha256"] != sha256(A411):
        raise AssertionError("A418 source does not bind current A411")

    checkpoint = load(CHECKPOINT)
    if (
        int(checkpoint.get("segment_index", -1)) != 1
        or abs(float(checkpoint.get("segment_position", -1.0)) - 0.9) > 1.0e-14
        or len(checkpoint.get("center", [])) != 13
        or len(checkpoint.get("waypoints", [])) != 3
    ):
        raise AssertionError("A418 checkpoint has not reached its final endpoint")
    before_sha256 = sha256(CHECKPOINT)
    normalized_sha256 = normalized_checkpoint_sha256(checkpoint)
    rebound = copy.deepcopy(checkpoint)
    rebound["A418_source_sha256"] = sha256(SOURCE)
    rebound["path_name"] = (
        "A418 selected A-handle hub-to-endpoint dps=100 "
        f"source={sha256(SOURCE)[:16]} "
        f"builder={checkpoint['A418_builder_sha256'][:16]}"
    )
    differences = difference_paths(checkpoint, rebound)
    if any(
        difference not in {"A418_source_sha256", "path_name"}
        for difference in differences
    ):
        raise AssertionError(f"A418 checkpoint change is not authority-only: {differences}")
    if normalized_checkpoint_sha256(rebound) != normalized_sha256:
        raise AssertionError("A418 numerical checkpoint payload changed")

    if arguments.apply and differences:
        atomic_dump(CHECKPOINT, rebound)
    if arguments.apply and normalized_checkpoint_sha256(load(CHECKPOINT)) != normalized_sha256:
        raise AssertionError("written A418 numerical checkpoint payload changed")

    payload = {
        "schema": "MTTQ79HeightFourA418AuthorityOnlyCheckpointRebind.v1",
        "status": (
            "A418_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED"
            if arguments.apply
            else "A418_AUTHORITY_ONLY_CHECKPOINT_REBIND_DRY_RUN"
        ),
        "artifact": "A418R",
        "current_authority": {
            "A404": authority(A404),
            "A411": authority(A411),
            "source": authority(SOURCE),
            "checkpoint": authority(CHECKPOINT),
            "rebind_source": authority(Path(__file__).resolve()),
        },
        "checkpoint": {
            "before_sha256": before_sha256,
            "after_sha256": sha256(CHECKPOINT) if arguments.apply else None,
            "normalized_numerical_payload_sha256": normalized_sha256,
        },
        "proved_exact_change_paths": {
            "A418_source": source_differences,
            "A418_checkpoint": [
                "A418_source_sha256",
                "path_name",
            ],
        },
        "strict_scope": {
            "A418_source_change_proved_authority_only": True,
            "A418_checkpoint_numerical_payload_preserved": True,
            "native_A418_replay_still_required": True,
            "new_transport_execution_claimed": False,
        },
    }
    if arguments.apply:
        atomic_dump(OUTPUT, payload)
        NOTE.write_text(
            "# MTT q79 Height-Four A418 Authority-Only Checkpoint Rebind v1\n\n"
            "The regenerated A418 source differs from its Git baseline only in its "
            "current A404 and A411 authority hashes. This packet rebinds the complete "
            "A418 checkpoint to that source while preserving its normalized numerical "
            "payload. Native A418 replay and its dedicated audit remain required.\n",
            encoding="utf-8",
        )
        print(f"wrote {relative(OUTPUT)}")
        print(f"wrote {relative(NOTE)}")
    else:
        print("dry run passed; use --apply to write the authority-only rebind")
    print("checkpoints=1; numerical payload changes=0; solver reruns=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
