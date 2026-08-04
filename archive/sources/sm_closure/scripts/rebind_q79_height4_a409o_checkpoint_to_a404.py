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
DIRECTORY = VALIDATED / "ol"
CHECKPOINT = DIRECTORY / "d057.a409o.ckpt.json"
OUTPUT = DIRECTORY / "a409or.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA409OAuthorityOnlyCheckpointRebind_v1.md"


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
    normalized.pop("A409O_A404_sha256", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    arguments = parser.parse_args()

    baseline_a404 = git_head_json(A404)
    current_a404 = load(A404)
    a404_differences = difference_paths(baseline_a404, current_a404)
    if a404_differences != ["authority.A403_common_junction_edge_ledger.sha256"]:
        raise AssertionError(f"A404 change is not authority-only: {a404_differences}")

    checkpoint = load(CHECKPOINT)
    if not checkpoint.get("complete"):
        raise AssertionError("A409O checkpoint is incomplete")
    before_sha256 = sha256(CHECKPOINT)
    normalized_sha256 = normalized_checkpoint_sha256(checkpoint)
    rebound = copy.deepcopy(checkpoint)
    rebound["A409O_A404_sha256"] = sha256(A404)
    differences = difference_paths(checkpoint, rebound)
    if differences not in ([], ["A409O_A404_sha256"]):
        raise AssertionError(f"A409O checkpoint change is not authority-only: {differences}")
    if normalized_checkpoint_sha256(rebound) != normalized_sha256:
        raise AssertionError("A409O numerical checkpoint payload changed")

    if arguments.apply and differences:
        atomic_dump(CHECKPOINT, rebound)
    if arguments.apply and normalized_checkpoint_sha256(load(CHECKPOINT)) != normalized_sha256:
        raise AssertionError("written A409O numerical checkpoint payload changed")

    payload = {
        "schema": "MTTQ79HeightFourA409OAuthorityOnlyCheckpointRebind.v1",
        "status": (
            "A409O_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED"
            if arguments.apply
            else "A409O_AUTHORITY_ONLY_CHECKPOINT_REBIND_DRY_RUN"
        ),
        "artifact": "A409OR",
        "current_authority": {
            "A404": authority(A404),
            "checkpoint": authority(CHECKPOINT),
            "rebind_source": authority(Path(__file__).resolve()),
        },
        "checkpoint": {
            "before_sha256": before_sha256,
            "after_sha256": sha256(CHECKPOINT) if arguments.apply else None,
            "normalized_numerical_payload_sha256": normalized_sha256,
        },
        "proved_exact_change_paths": {
            "A404": a404_differences,
            "A409O_checkpoint": ["A409O_A404_sha256"],
        },
        "strict_scope": {
            "A404_change_proved_authority_only": True,
            "A409O_checkpoint_numerical_payload_preserved": True,
            "native_A409O_and_A412_replay_still_required": True,
            "new_transport_execution_claimed": False,
        },
    }
    if arguments.apply:
        atomic_dump(OUTPUT, payload)
        NOTE.write_text(
            "# MTT q79 Height-Four A409O Authority-Only Checkpoint Rebind v1\n\n"
            "A404 differs from its Git baseline only in the certified A403 authority "
            "hash. This packet rebinds the complete d057 A409O checkpoint to current "
            "A404 while preserving its normalized numerical payload. Native A409O "
            "and A412 replay and their dedicated audits remain required.\n",
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
