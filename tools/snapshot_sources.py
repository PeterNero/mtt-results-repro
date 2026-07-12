"""Copy every indexed source artifact into a hash-verified local archive."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "source_repositories.json"
INVENTORY = ROOT / "inventory"
ARCHIVE = ROOT / "archive" / "sources"


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


def copy_bytes(source: Path, destination: Path) -> None:
    """Avoid the Windows CopyFile2 path-length failure on deep packet names."""
    with open(io_path(source), "rb") as input_handle, open(io_path(destination), "wb") as output_handle:
        shutil.copyfileobj(input_handle, output_handle, length=1024 * 1024)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    args = parser.parse_args()
    source_root = args.source_root.resolve()

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    repos = {row["id"]: row for row in config["repositories"]}
    artifacts = load_jsonl(INVENTORY / "artifacts.jsonl")
    snapshot = json.loads((INVENTORY / "source_repositories.json").read_text(encoding="utf-8"))

    copied = 0
    copied_bytes = 0
    reused = 0
    by_repo: Counter[str] = Counter()
    for artifact in artifacts:
        repo = repos[artifact["repo_id"]]
        source_base = (source_root / Path(repo["local_relative_path"])).resolve()
        source = source_base if source_base.is_file() else source_base / Path(artifact["path"])
        destination = ARCHIVE / artifact["repo_id"] / Path(artifact["path"])
        if not source.is_file():
            raise FileNotFoundError(f"indexed source disappeared: {source}")

        os.makedirs(io_path(destination.parent), exist_ok=True)
        if os.path.isfile(io_path(destination)) and os.path.getsize(io_path(destination)) == artifact["size_bytes"]:
            if sha256(destination) == artifact["sha256"]:
                reused += 1
                by_repo[artifact["repo_id"]] += 1
                copied_bytes += artifact["size_bytes"]
                continue
        copy_bytes(source, destination)
        actual_hash = sha256(destination)
        if actual_hash != artifact["sha256"]:
            raise RuntimeError(f"hash mismatch after copy: {destination}")
        copied += 1
        copied_bytes += artifact["size_bytes"]
        by_repo[artifact["repo_id"]] += 1

    manifest = {
        "schema": "MTTHashVerifiedSourceArchive.v1",
        "source_root_recorded_as": "<LOCAL_SOURCE_ROOT>",
        "artifact_count": len(artifacts),
        "total_bytes": copied_bytes,
        "copied_this_run": copied,
        "reused_this_run": reused,
        "artifact_count_by_source": dict(sorted(by_repo.items())),
        "source_snapshots": snapshot["repositories"],
        "integrity_source": "inventory/artifacts.jsonl",
        "policy": {
            "bytes_preserved_exactly": True,
            "absolute_paths_inside_historical_files_rewritten": False,
            "historical_status_promoted_to_current_authority": False,
        },
    }
    dump(ROOT / "archive" / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
