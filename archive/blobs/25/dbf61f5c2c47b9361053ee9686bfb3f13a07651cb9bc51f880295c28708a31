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
DIRECTORY = VALIDATED / "ol"
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A410 = VALIDATED / "pt" / "a410.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = DIRECTORY / "all76.a413.json"
OUTPUT = DIRECTORY / "a413r.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA413AuthorityOnlyCheckpointRebind_v1.md"

EXPECTED_PARENT_CHANGE_PATHS = {
    "A400": ["authority.builder_source.sha256"],
    "A404": ["authority.A403_common_junction_edge_ledger.sha256"],
    "A405": [
        "authority.A404_manifest.sha256",
        "authority.basis_0_result.sha256",
        "authority.basis_0_snapshots.sha256",
        "authority.basis_1_result.sha256",
        "authority.basis_1_snapshots.sha256",
        "authority.basis_2_result.sha256",
        "authority.basis_2_snapshots.sha256",
        "authority.basis_3_result.sha256",
        "authority.basis_3_snapshots.sha256",
        "authority.basis_4_result.sha256",
        "authority.basis_4_snapshots.sha256",
    ],
    "A410": ["authority.A404_common_junction_manifest.sha256"],
    "A411": [
        "authority.A404_manifest.sha256",
        "authority.A405_operator_sweep.sha256",
        "authority.basis_0_snapshots.sha256",
        "authority.basis_1_snapshots.sha256",
        "authority.basis_2_snapshots.sha256",
        "authority.basis_3_snapshots.sha256",
        "authority.basis_4_snapshots.sha256",
    ],
}
EXPECTED_A413_CHANGE_PATHS = [
    "authority.A400_exact_relative_chain_identity.sha256",
    "authority.A404_common_junction_manifest.sha256",
    "authority.A405_entry_operators.sha256",
    "authority.A410_native_z_transitions.sha256",
    "authority.A411_terminal_trunk.sha256",
]


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


def git_head_blob(path: Path) -> bytes:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative(path)}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def windows_worktree_bytes(git_blob: bytes) -> bytes:
    """Reproduce the CRLF byte serialization used by recorded worktree hashes."""
    normalized = git_blob.replace(b"\r\n", b"\n")
    return normalized.replace(b"\n", b"\r\n")


def serialized_worktree_sha256(value: dict[str, Any]) -> str:
    rendered = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")
    return sha256_bytes(windows_worktree_bytes(rendered))


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
        paths = []
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            paths.extend(
                difference_paths(
                    left_item,
                    right_item,
                    f"{prefix}[{index}]",
                )
            )
        return paths
    return [] if left == right else [prefix or "<root>"]


def normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A414_A413_sha256", None)
    normalized.pop("A414_A404_sha256", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def predecessor_normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A414_A413_sha256", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the authority-only checkpoint rebind after all invariance checks pass",
    )
    arguments = parser.parse_args()

    parents = {
        "A400": A400,
        "A404": A404,
        "A405": A405,
        "A410": A410,
        "A411": A411,
    }
    old_parent_blobs = {label: git_head_blob(path) for label, path in parents.items()}
    old_parents = {
        label: json.loads(blob) for label, blob in old_parent_blobs.items()
    }
    current_parents = {label: load(path) for label, path in parents.items()}
    old_a413_blob = git_head_blob(A413)
    old_a413 = json.loads(old_a413_blob)
    current_a413 = load(A413)

    parent_differences = {
        label: difference_paths(old_parents[label], current_parents[label])
        for label in parents
    }
    a413_differences = difference_paths(old_a413, current_a413)
    for label, expected in EXPECTED_PARENT_CHANGE_PATHS.items():
        if parent_differences[label] != expected:
            raise AssertionError(
                f"{label} change is not the expected authority-only delta: "
                f"{parent_differences[label]}"
            )
    if a413_differences != EXPECTED_A413_CHANGE_PATHS:
        raise AssertionError(f"A413 change is not authority-only: {a413_differences}")

    old_parent_sha256 = {
        label: sha256_bytes(windows_worktree_bytes(blob))
        for label, blob in old_parent_blobs.items()
    }
    current_parent_sha256 = {
        label: sha256(path) for label, path in parents.items()
    }
    old_a413_sha256 = sha256_bytes(windows_worktree_bytes(old_a413_blob))
    current_a413_sha256 = sha256(A413)
    prior_rebind = load(OUTPUT)
    if (
        prior_rebind.get("schema")
        != "MTTQ79HeightFourA413AuthorityOnlyCheckpointRebind.v1"
        or prior_rebind.get("status")
        != "A413_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED"
        or prior_rebind.get("baseline", {}).get("A413_sha256") != old_a413_sha256
    ):
        raise AssertionError("prior A413R certificate is unavailable or incompatible")
    prior_a413_sha256 = prior_rebind["current_authority"]["A413"]["sha256"]
    prior_rows = {
        int(row["distinguished_index"]): row
        for row in prior_rebind["checkpoint_rows"]
    }
    a413_parent_authority_keys = {
        "A400": "A400_exact_relative_chain_identity",
        "A404": "A404_common_junction_manifest",
        "A405": "A405_entry_operators",
        "A410": "A410_native_z_transitions",
        "A411": "A411_terminal_trunk",
    }
    for label, authority_key in a413_parent_authority_keys.items():
        if old_a413["authority"][authority_key]["sha256"] != old_parent_sha256[label]:
            raise AssertionError(f"baseline A413 does not bind baseline {label}")
        if (
            current_a413["authority"][authority_key]["sha256"]
            != current_parent_sha256[label]
        ):
            raise AssertionError(f"current A413 does not bind current {label}")
    if old_a413_sha256 == current_a413_sha256:
        raise AssertionError("A413 did not change")

    supported = sorted(
        int(row["distinguished_index"])
        for row in current_a413["target_rows"]
        if int(row["distinguished_index"]) != 57
    )
    if len(supported) != 75:
        raise AssertionError(f"expected 75 A414 checkpoints, found {len(supported)}")

    rows: list[dict[str, Any]] = []
    for index in supported:
        path = DIRECTORY / f"d{index:03d}.a414.ckpt.json"
        checkpoint = load(path)
        if not checkpoint.get("complete"):
            raise AssertionError(f"d{index:03d} checkpoint is incomplete")
        bound_a413_sha256 = checkpoint.get("A414_A413_sha256")
        if bound_a413_sha256 not in {
            old_a413_sha256,
            prior_a413_sha256,
            current_a413_sha256,
        }:
            raise AssertionError(
                f"d{index:03d} binds neither baseline, certified predecessor, "
                "nor current A413"
            )
        baseline = copy.deepcopy(checkpoint)
        baseline["A414_A413_sha256"] = old_a413_sha256
        before_sha256 = serialized_worktree_sha256(baseline)
        if bound_a413_sha256 == old_a413_sha256 and before_sha256 != sha256(path):
            raise AssertionError(f"d{index:03d} baseline checkpoint serialization changed")
        normalized_sha256 = normalized_checkpoint_sha256(checkpoint)
        if bound_a413_sha256 == prior_a413_sha256:
            prior_row = prior_rows.get(index)
            if (
                prior_row is None
                or prior_row["checkpoint"]["after_sha256"] != sha256(path)
                or prior_row["normalized_checkpoint_payload_sha256"]
                != predecessor_normalized_checkpoint_sha256(checkpoint)
            ):
                raise AssertionError(
                    f"d{index:03d} is not the payload certified by predecessor A413R"
                )
        rebound = copy.deepcopy(checkpoint)
        rebound["A414_A413_sha256"] = current_a413_sha256
        rebound["A414_A404_sha256"] = current_parent_sha256["A404"]
        expected_rebound_delta = sorted(
            field
            for field in ("A414_A404_sha256", "A414_A413_sha256")
            if checkpoint.get(field) != rebound[field]
        )
        if difference_paths(checkpoint, rebound) != expected_rebound_delta:
            raise AssertionError(f"d{index:03d} rebind changed numerical state")
        if normalized_checkpoint_sha256(rebound) != normalized_sha256:
            raise AssertionError(f"d{index:03d} normalized checkpoint payload changed")
        if arguments.apply and expected_rebound_delta:
            atomic_dump(path, rebound)
        if arguments.apply:
            if normalized_checkpoint_sha256(load(path)) != normalized_sha256:
                raise AssertionError(f"d{index:03d} written checkpoint payload changed")
            if sha256(path) != serialized_worktree_sha256(rebound):
                raise AssertionError(f"d{index:03d} written checkpoint serialization changed")
        rows.append(
            {
                "distinguished_index": index,
                "checkpoint": {
                    "path": relative(path),
                    "before_sha256": before_sha256,
                    "after_sha256": sha256(path) if arguments.apply else None,
                },
                "normalized_checkpoint_payload_sha256": normalized_sha256,
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourA413AuthorityOnlyCheckpointRebind.v1",
        "status": (
            "A413_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED"
            if arguments.apply
            else "A413_AUTHORITY_ONLY_CHECKPOINT_REBIND_DRY_RUN"
        ),
        "artifact": "A413R",
        "baseline": {
            "git_revision": "HEAD",
            **{
                f"{label}_sha256": digest
                for label, digest in old_parent_sha256.items()
            },
            "A413_sha256": old_a413_sha256,
            "predecessor_A413R_sha256": sha256(OUTPUT),
            "predecessor_A413_sha256": prior_a413_sha256,
        },
        "current_authority": {
            **{label: authority(path) for label, path in parents.items()},
            "A413": authority(A413),
            "rebind_source": authority(Path(__file__).resolve()),
        },
        "proved_exact_change_paths": {
            **parent_differences,
            "A413": a413_differences,
            "each_A414_checkpoint": [
                "A414_A404_sha256",
                "A414_A413_sha256",
            ],
        },
        "checkpoint_rows": rows,
        "summary": {
            "checkpoint_count": len(rows),
            "numerical_checkpoint_payloads_changed": 0,
            "authority_fields_rebound_per_checkpoint": 2,
        },
        "strict_scope": {
            "all_A400_A404_A405_A410_A411_changes_proved_authority_only": True,
            "A413_change_proved_parent_authority_only": True,
            "all_75_complete_A414_checkpoint_payloads_preserved": True,
            "native_A414_and_A415_producers_still_required_after_rebind": True,
            "new_numerical_transport_execution_claimed": False,
            "covariant_zero_proved": False,
        },
    }
    if arguments.apply:
        atomic_dump(OUTPUT, payload)
        NOTE.write_text(
            "# MTT q79 Height-Four A413 Authority-Only Checkpoint Rebind v1\n\n"
            "The regenerated A400, A404, A405, A410, and A411 packets differ from "
            "their Git baselines only in their enumerated authority hashes. The "
            "regenerated A413 manifest consequently differs only in those five parent "
            "authority hashes. This certificate rebinds the 75 complete "
            "A414 checkpoints to the current A404 and A413 hashes while proving that every "
            "normalized numerical checkpoint payload is unchanged.\n\n"
            "This is not a replacement for producer replay. The native A414 and A415 "
            "builders and their dedicated auditors must run after the rebind.\n",
            encoding="utf-8",
        )
        print(f"wrote {relative(OUTPUT)}")
        print(f"wrote {relative(NOTE)}")
    else:
        print("dry run passed; use --apply to write the authority-only rebind")
    print(f"checkpoints={len(rows)}; numerical payload changes=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
