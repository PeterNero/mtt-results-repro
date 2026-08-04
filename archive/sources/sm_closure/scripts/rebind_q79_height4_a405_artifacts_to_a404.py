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
DIRECTORY = VALIDATED / "jop"
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
OUTPUT = DIRECTORY / "a404r.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA404AuthorityOnlyA405Rebind_v1.md"


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
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def git_head_json(path: Path) -> tuple[dict[str, Any], bytes]:
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative(path)}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return json.loads(result.stdout), result.stdout


def windows_bytes(value: bytes) -> bytes:
    return value.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")


def difference_paths(left: Any, right: Any, prefix: str = "") -> list[str]:
    if type(left) is not type(right):
        return [prefix or "<root>"]
    if isinstance(left, dict):
        result: list[str] = []
        for key in sorted(set(left) | set(right)):
            child = f"{prefix}.{key}" if prefix else str(key)
            if key not in left or key not in right:
                result.append(child)
            else:
                result.extend(difference_paths(left[key], right[key], child))
        return result
    if isinstance(left, list):
        if len(left) != len(right):
            return [prefix or "<root>"]
        result = []
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            result.extend(
                difference_paths(left_item, right_item, f"{prefix}[{index}]")
            )
        return result
    return [] if left == right else [prefix or "<root>"]


def normalized_sha256(value: dict[str, Any], kind: str) -> str:
    normalized = copy.deepcopy(value)
    if kind == "checkpoint":
        normalized.pop("A405_manifest_sha256", None)
    elif kind == "snapshots":
        normalized.pop("A404_manifest_sha256", None)
    elif kind == "result":
        authority_rows = normalized["authority"]
        authority_rows["A404_manifest"].pop("sha256", None)
        authority_rows["completed_checkpoint"].pop("sha256", None)
        authority_rows["snapshot_packet"].pop("sha256", None)
    else:
        raise ValueError(f"unknown normalization kind: {kind}")
    rendered = json.dumps(
        normalized, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(rendered)


def paths(column: int) -> dict[str, Path]:
    prefix = DIRECTORY / f"basis_{column}.a405"
    return {
        "checkpoint": Path(str(prefix) + ".ckpt.json"),
        "snapshots": Path(str(prefix) + ".snapshots.json"),
        "result": Path(str(prefix) + ".json"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    arguments = parser.parse_args()

    old_a403, old_a403_blob = git_head_json(A403)
    old_a404, old_a404_blob = git_head_json(A404)
    current_a403 = load(A403)
    current_a404 = load(A404)
    a403_differences = difference_paths(old_a403, current_a403)
    a404_differences = difference_paths(old_a404, current_a404)
    if a403_differences != ["authority.A400_relative_chain_identity.sha256"]:
        raise AssertionError(f"A403 change is not authority-only: {a403_differences}")
    if a404_differences != ["authority.A403_common_junction_edge_ledger.sha256"]:
        raise AssertionError(f"A404 change is not authority-only: {a404_differences}")

    old_a403_sha256 = sha256_bytes(windows_bytes(old_a403_blob))
    old_a404_sha256 = sha256_bytes(windows_bytes(old_a404_blob))
    current_a403_sha256 = sha256(A403)
    current_a404_sha256 = sha256(A404)
    if old_a404["authority"]["A403_common_junction_edge_ledger"]["sha256"] != old_a403_sha256:
        raise AssertionError("baseline A404 does not bind baseline A403")
    if (
        current_a404["authority"]["A403_common_junction_edge_ledger"]["sha256"]
        != current_a403_sha256
    ):
        raise AssertionError("current A404 does not bind current A403")

    rows: list[dict[str, Any]] = []
    for column in range(5):
        selected = paths(column)
        checkpoint = load(selected["checkpoint"])
        snapshots = load(selected["snapshots"])
        result = load(selected["result"])
        if checkpoint.get("A405_manifest_sha256") not in {
            old_a404_sha256,
            current_a404_sha256,
        }:
            raise AssertionError(f"A405 basis {column} checkpoint authority is unknown")
        if snapshots.get("A404_manifest_sha256") not in {
            old_a404_sha256,
            current_a404_sha256,
        }:
            raise AssertionError(f"A405 basis {column} snapshot authority is unknown")
        if result["authority"]["A404_manifest"]["sha256"] not in {
            old_a404_sha256,
            current_a404_sha256,
        }:
            raise AssertionError(f"A405 basis {column} result authority is unknown")

        before = {
            kind: sha256(path) for kind, path in selected.items()
        }
        normalized = {
            "checkpoint": normalized_sha256(checkpoint, "checkpoint"),
            "snapshots": normalized_sha256(snapshots, "snapshots"),
            "result": normalized_sha256(result, "result"),
        }
        rebound_checkpoint = copy.deepcopy(checkpoint)
        rebound_checkpoint["A405_manifest_sha256"] = current_a404_sha256
        rebound_snapshots = copy.deepcopy(snapshots)
        rebound_snapshots["A404_manifest_sha256"] = current_a404_sha256

        if arguments.apply:
            atomic_dump(selected["checkpoint"], rebound_checkpoint)
            atomic_dump(selected["snapshots"], rebound_snapshots)
        rebound_result = copy.deepcopy(result)
        rebound_result["authority"]["A404_manifest"]["sha256"] = current_a404_sha256
        rebound_result["authority"]["completed_checkpoint"]["sha256"] = (
            sha256(selected["checkpoint"]) if arguments.apply else ""
        )
        rebound_result["authority"]["snapshot_packet"]["sha256"] = (
            sha256(selected["snapshots"]) if arguments.apply else ""
        )
        if arguments.apply:
            atomic_dump(selected["result"], rebound_result)
            for kind, value in (
                ("checkpoint", rebound_checkpoint),
                ("snapshots", rebound_snapshots),
                ("result", rebound_result),
            ):
                if normalized_sha256(value, kind) != normalized[kind]:
                    raise AssertionError(
                        f"A405 basis {column} {kind} numerical payload changed"
                    )
        rows.append(
            {
                "basis_column_zero_based": column,
                "artifacts": {
                    kind: {
                        "path": relative(path),
                        "before_sha256": before[kind],
                        "after_sha256": sha256(path) if arguments.apply else None,
                        "normalized_payload_sha256": normalized[kind],
                    }
                    for kind, path in selected.items()
                },
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourA404AuthorityOnlyA405Rebind.v1",
        "status": (
            "A404_AUTHORITY_ONLY_A405_REBIND_APPLIED"
            if arguments.apply
            else "A404_AUTHORITY_ONLY_A405_REBIND_DRY_RUN"
        ),
        "artifact": "A404R",
        "baseline": {
            "git_revision": "HEAD",
            "A403_sha256": old_a403_sha256,
            "A404_sha256": old_a404_sha256,
        },
        "current_authority": {
            "A403": authority(A403),
            "A404": authority(A404),
            "rebind_source": authority(Path(__file__).resolve()),
        },
        "proved_exact_change_paths": {
            "A403": a403_differences,
            "A404": a404_differences,
            "checkpoint": ["A405_manifest_sha256"],
            "snapshots": ["A404_manifest_sha256"],
            "result": [
                "authority.A404_manifest.sha256",
                "authority.completed_checkpoint.sha256",
                "authority.snapshot_packet.sha256",
            ],
        },
        "basis_rows": rows,
        "summary": {
            "basis_count": len(rows),
            "artifact_count": 3 * len(rows),
            "normalized_numerical_payloads_changed": 0,
            "solver_reruns": 0,
        },
        "strict_scope": {
            "A403_change_proved_A400_authority_only": True,
            "A404_change_proved_A403_authority_only": True,
            "all_five_completed_A405_artifact_triples_preserved": True,
            "native_A405_aggregate_and_audit_still_required": True,
            "new_numerical_transport_execution_claimed": False,
            "covariant_zero_proved": False,
        },
    }
    if arguments.apply:
        atomic_dump(OUTPUT, payload)
        NOTE.write_text(
            "# MTT q79 Height-Four A404 Authority-Only A405 Rebind v1\n\n"
            "A403 differs from its Git baseline only in the A400 authority hash, "
            "and A404 differs only in the resulting A403 authority hash. This "
            "certificate rebinds all five completed A405 checkpoints, snapshot "
            "packets, and result packets while preserving every normalized "
            "numerical payload. No transport solve is rerun.\n\n"
            "The native A405 aggregate builder and dedicated audit remain required.\n",
            encoding="utf-8",
        )
        print(f"wrote {relative(OUTPUT)}")
        print(f"wrote {relative(NOTE)}")
    else:
        print("dry run passed; use --apply to write the authority-only rebind")
    print("basis artifacts=15; normalized numerical payload changes=0; solver reruns=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
