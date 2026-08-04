"""Build a publication-safe archive plus a hash-only index for bulk outputs."""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "source_repositories.json"
ARCHIVE_POLICY = ROOT / "config" / "archive_policy.json"
INVENTORY = ROOT / "inventory"
ARCHIVE = ROOT / "archive" / "blobs"
LEGACY_ARCHIVE = ROOT / "archive" / "sources"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(io_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


def archive_eligible(artifact: dict[str, Any], policy: dict[str, Any]) -> tuple[bool, str]:
    combined_path = f"{artifact['repo_id']}/{artifact['path']}".casefold()
    if any(
        fnmatch.fnmatchcase(combined_path, pattern.casefold())
        for pattern in policy.get("always_hash_only_globs", [])
    ):
        return False, "configured_bulk_diagnostic_hash_only"
    if artifact["suffix"].casefold() in {
        suffix.casefold() for suffix in policy["always_archive_suffixes"]
    }:
        return True, "source_or_document_suffix"
    if artifact["size_bytes"] <= policy["max_default_artifact_bytes"]:
        return True, "within_public_archive_size_limit"
    return False, "large_raw_output_hash_only"


def copy_bytes(source: Path, destination: Path) -> None:
    """Avoid the Windows CopyFile2 path-length failure on deep packet names."""
    with open(io_path(source), "rb") as input_handle, open(io_path(destination), "wb") as output_handle:
        shutil.copyfileobj(input_handle, output_handle, length=1024 * 1024)


def blob_relative_path(digest: str) -> Path:
    return Path(digest[:2]) / digest[2:]


def remove_tree(root: Path) -> int:
    """Remove a verified in-repository tree with Windows long-path support."""
    resolved = root.resolve()
    if ROOT.resolve() not in resolved.parents:
        raise RuntimeError(f"unsafe archive cleanup path: {resolved}")
    if not resolved.exists():
        return 0
    removed = 0
    root_io = io_path(resolved)
    for directory, directories, files in os.walk(root_io, topdown=False):
        for name in files:
            os.unlink(os.path.join(directory, name))
            removed += 1
        for name in directories:
            os.rmdir(os.path.join(directory, name))
    os.rmdir(root_io)
    return removed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    args = parser.parse_args()
    source_root = args.source_root.resolve()

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    archive_policy = json.loads(ARCHIVE_POLICY.read_text(encoding="utf-8"))
    repos = {row["id"]: row for row in config["repositories"]}
    artifacts = load_jsonl(INVENTORY / "artifacts.jsonl")
    snapshot = json.loads((INVENTORY / "source_repositories.json").read_text(encoding="utf-8"))

    archive_root = ARCHIVE.resolve()
    if ROOT.resolve() not in archive_root.parents:
        raise RuntimeError(f"unsafe archive cleanup path: {archive_root}")
    decisions = {
        (artifact["repo_id"], artifact["path"]): archive_eligible(artifact, archive_policy)
        for artifact in artifacts
    }
    archived_artifacts = [
        artifact
        for artifact in artifacts
        if decisions[(artifact["repo_id"], artifact["path"])][0]
    ]
    hash_only_artifacts = [
        {
            "repo_id": artifact["repo_id"],
            "path": artifact["path"],
            "size_bytes": artifact["size_bytes"],
            "sha256": artifact["sha256"],
            "reason": decisions[(artifact["repo_id"], artifact["path"])][1],
        }
        for artifact in artifacts
        if not decisions[(artifact["repo_id"], artifact["path"])][0]
    ]
    blobs: dict[str, dict[str, Any]] = {}
    artifact_blob_rows = []
    for artifact in archived_artifacts:
        existing = blobs.get(artifact["sha256"])
        if existing is not None and existing["size_bytes"] != artifact["size_bytes"]:
            raise RuntimeError(f"same hash with inconsistent size: {artifact['sha256']}")
        blobs.setdefault(artifact["sha256"], artifact)
        artifact_blob_rows.append(
            {
                "repo_id": artifact["repo_id"],
                "path": artifact["path"],
                "size_bytes": artifact["size_bytes"],
                "sha256": artifact["sha256"],
                "blob_path": f"archive/blobs/{blob_relative_path(artifact['sha256']).as_posix()}",
            }
        )
    expected_paths = {
        blob_relative_path(digest).as_posix().casefold() for digest in blobs
    }
    removed_legacy = remove_tree(LEGACY_ARCHIVE)
    removed_stale = 0
    if archive_root.exists():
        archive_io = io_path(archive_root)
        for directory, directories, files in os.walk(archive_io, topdown=False):
            for name in files:
                path = os.path.join(directory, name)
                relative = os.path.relpath(path, archive_io).replace("\\", "/").casefold()
                if relative not in expected_paths:
                    os.unlink(path)
                    removed_stale += 1
            for name in directories:
                path = os.path.join(directory, name)
                try:
                    os.rmdir(path)
                except OSError:
                    pass

    copied = 0
    unique_blob_bytes = 0
    reused = 0
    by_repo: Counter[str] = Counter()
    for artifact in archived_artifacts:
        by_repo[artifact["repo_id"]] += 1
    for digest, artifact in blobs.items():
        repo = repos[artifact["repo_id"]]
        source_base = (source_root / Path(repo["local_relative_path"])).resolve()
        source = source_base if source_base.is_file() else source_base / Path(artifact["path"])
        destination = ARCHIVE / blob_relative_path(digest)
        if not os.path.isfile(io_path(source)):
            raise FileNotFoundError(f"indexed source disappeared: {source}")

        os.makedirs(io_path(destination.parent), exist_ok=True)
        actual_hash = sha256(destination) if os.path.isfile(io_path(destination)) else None
        if actual_hash == artifact["sha256"]:
            reused += 1
        else:
            copy_bytes(source, destination)
            actual_hash = sha256(destination)
            copied += 1
        if actual_hash != artifact["sha256"]:
            raise RuntimeError(f"hash mismatch after copy: {destination}")
        unique_blob_bytes += artifact["size_bytes"]

    write_jsonl(ROOT / "archive" / "hash_only_artifacts.jsonl", hash_only_artifacts)
    write_jsonl(ROOT / "archive" / "artifact_blob_map.jsonl", artifact_blob_rows)
    manifest = {
        "schema": "MTTPublicSourceArchive.v3",
        "source_root_recorded_as": "<LOCAL_SOURCE_ROOT>",
        "artifact_count": len(archived_artifacts),
        "unique_blob_count": len(blobs),
        "inventory_artifact_count": len(artifacts),
        "hash_only_artifact_count": len(hash_only_artifacts),
        "total_bytes": unique_blob_bytes,
        "mirrored_artifact_bytes_before_deduplication": sum(row["size_bytes"] for row in archived_artifacts),
        "inventory_total_bytes": sum(row["size_bytes"] for row in artifacts),
        "hash_only_total_bytes": sum(row["size_bytes"] for row in hash_only_artifacts),
        "copied_this_run": copied,
        "reused_this_run": reused,
        "removed_stale_this_run": removed_stale,
        "removed_legacy_source_paths_this_run": removed_legacy,
        "artifact_count_by_source": dict(sorted(by_repo.items())),
        "source_snapshots": snapshot["repositories"],
        "integrity_source": "inventory/artifacts.jsonl",
        "hash_only_index": "archive/hash_only_artifacts.jsonl",
        "artifact_blob_map": "archive/artifact_blob_map.jsonl",
        "policy": {
            "bytes_preserved_exactly": True,
            "absolute_paths_inside_historical_files_rewritten": False,
            "historical_status_promoted_to_current_authority": False,
            **archive_policy["policy"],
            "max_default_artifact_bytes": archive_policy["max_default_artifact_bytes"],
            "always_archive_suffixes": archive_policy["always_archive_suffixes"],
            "always_hash_only_globs": archive_policy.get("always_hash_only_globs", []),
            "content_addressed_short_paths": True,
        },
    }
    dump(ROOT / "archive" / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
