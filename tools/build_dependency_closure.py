"""Build a portable, hash-locked dependency closure for a terminal packet."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKSPACE = ROOT.parent
DEFAULT_TERMINAL = (
    DEFAULT_WORKSPACE
    / "mtt-q79-mirror-zero-zero"
    / "q79_hessian_stratum_euler_csm_degree.packet.json"
)
DEFAULT_OUTPUT = ROOT / "release" / "dependency_closures" / "q79_qg_terminal"
SCHEMA = "MTTHashLockedDependencyClosure.v1"
CLOSURE_ID = "q79_qg_terminal"


def io_path(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with open(io_path(path), "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def references(value: Any) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    if isinstance(value, dict):
        path = value.get("path")
        sha256 = value.get("sha256")
        if isinstance(path, str) and isinstance(sha256, str):
            found.append((path, sha256.lower()))
        else:
            for child in value.values():
                found.extend(references(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(references(child))
    return found


def normalized_parts(raw: str) -> list[str]:
    return [part for part in raw.replace("\\", "/").split("/") if part]


def workspace_suffix(raw: str) -> Path | None:
    parts = normalized_parts(raw)
    folded = [part.casefold() for part in parts]
    for marker in ("texpapers", "mtt-research"):
        if marker in folded:
            index = folded.index(marker)
            if index + 1 < len(parts):
                return Path(*parts[index + 1 :])
    return None


def translated_absolute(raw: str) -> Path | None:
    normalized = raw.replace("\\", "/")
    match = re.fullmatch(r"/mnt/([A-Za-z])/(.+)", normalized)
    if match:
        return Path(f"{match.group(1).upper()}:/{match.group(2)}")
    candidate = Path(raw)
    return candidate if candidate.is_absolute() else None


def logical_hint(raw: str, context_hint: str | None = None) -> str:
    suffix = workspace_suffix(raw)
    if suffix is not None:
        return f"../{suffix.as_posix()}"

    normalized = raw.replace("\\", "/")
    if translated_absolute(raw) is not None:
        return f"legacy/{PurePosixPath(normalized).name}"

    relative = PurePosixPath(normalized)
    if context_hint:
        return (PurePosixPath(context_hint).parent / relative).as_posix()
    return relative.as_posix()


def local_candidates(
    raw: str,
    context_source: Path,
    context_hint: str,
    workspace: Path,
    terminal_root: Path,
) -> list[Path]:
    candidates: list[Path] = []
    absolute = translated_absolute(raw)
    if absolute is not None:
        candidates.append(absolute)

    suffix = workspace_suffix(raw)
    if suffix is not None:
        candidates.append(workspace / suffix)

    if absolute is None:
        relative = Path(raw)
        candidates.append(context_source.parent / relative)
        normalized_context = context_hint.replace("\\", "/")
        if normalized_context.startswith("../"):
            context_relative = PurePosixPath(normalized_context[3:])
            candidates.append(
                workspace
                / Path(*context_relative.parent.parts)
                / relative
            )
        candidates.extend((terminal_root / relative, workspace / relative))

    unique: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = os.path.normcase(os.path.abspath(candidate))
        if key not in seen:
            seen.add(key)
            unique.append(candidate)
    return unique


def resolve_reference(
    raw: str,
    expected_hash: str,
    context_source: Path,
    context_hint: str,
    workspace: Path,
    terminal_root: Path,
) -> Path:
    existing = [
        candidate
        for candidate in local_candidates(
            raw, context_source, context_hint, workspace, terminal_root
        )
        if candidate.is_file()
    ]
    for candidate in existing:
        if digest(candidate) == expected_hash:
            return candidate.resolve()
    if existing:
        mismatches = ", ".join(
            f"{candidate}={digest(candidate)}" for candidate in existing
        )
        raise ValueError(
            f"local dependency hash mismatch for {raw}: expected={expected_hash}; "
            f"found {mismatches}"
        )

    archive_blob = ROOT / "archive" / "blobs" / expected_hash[:2] / expected_hash[2:]
    if archive_blob.is_file():
        actual = digest(archive_blob)
        if actual != expected_hash:
            raise ValueError(
                f"public archive blob hash mismatch: expected={expected_hash}; actual={actual}"
            )
        return archive_blob.resolve()
    raise FileNotFoundError(f"unresolved dependency: {raw} ({expected_hash})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--terminal", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    terminal = args.terminal.resolve()
    workspace = args.workspace.resolve()
    output = args.output.resolve()
    if not terminal.is_file():
        raise FileNotFoundError(terminal)
    if ROOT not in output.parents:
        raise ValueError(f"output must remain inside {ROOT}: {output}")
    relative_output = output.relative_to(ROOT)

    terminal_hint = logical_hint(str(terminal))
    terminal_hash = digest(terminal)
    records: dict[str, dict[str, Any]] = {}
    sources: dict[str, Path] = {}
    active: set[str] = set()
    linked_input_edges = 0

    def visit(source: Path, expected_hash: str, hint: str) -> None:
        nonlocal linked_input_edges
        actual_hash = digest(source)
        if actual_hash != expected_hash:
            raise ValueError(
                f"dependency hash mismatch for {source}: "
                f"expected={expected_hash}; actual={actual_hash}"
            )

        existing = records.get(expected_hash)
        if existing is not None:
            existing["logical_source_hints"].add(hint)
            return
        if expected_hash in active:
            raise ValueError(f"dependency cycle at {hint} ({expected_hash})")

        is_json = hint.casefold().endswith(".json") or source.suffix.casefold() == ".json"
        record = {
            "sha256": expected_hash,
            "size_bytes": source.stat().st_size,
            "kind": "json" if is_json else "non_json",
            "logical_source_hints": {hint},
        }
        records[expected_hash] = record
        sources[expected_hash] = source
        if not is_json:
            return

        active.add(expected_hash)
        try:
            payload = json.loads(source.read_text(encoding="utf-8"))
            for raw, child_hash in references(payload.get("inputs", {})):
                linked_input_edges += 1
                child_hint = logical_hint(raw, hint)
                child_source = resolve_reference(
                    raw,
                    child_hash,
                    source,
                    hint,
                    workspace,
                    terminal.parent,
                )
                visit(child_source, child_hash, child_hint)
        finally:
            active.remove(expected_hash)

    visit(terminal, terminal_hash, terminal_hint)

    blobs_root = output / "blobs"
    blobs_root.mkdir(parents=True, exist_ok=True)
    expected_blob_paths: set[Path] = set()
    manifest_records: list[dict[str, Any]] = []
    for sha256 in sorted(records):
        relative_blob = relative_output / "blobs" / sha256[:2] / sha256[2:]
        destination = ROOT / relative_blob
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.is_file() or digest(destination) != sha256:
            shutil.copyfile(io_path(sources[sha256]), io_path(destination))
        if digest(destination) != sha256:
            raise ValueError(f"copied blob failed verification: {destination}")
        expected_blob_paths.add(destination.resolve())
        row = dict(records[sha256])
        row["blob_path"] = relative_blob.as_posix()
        row["logical_source_hints"] = sorted(row["logical_source_hints"])
        manifest_records.append(row)

    for stale in sorted(blobs_root.rglob("*"), reverse=True):
        if stale.is_file() and stale.resolve() not in expected_blob_paths:
            stale.unlink()
        elif stale.is_dir() and not any(stale.iterdir()):
            stale.rmdir()

    json_count = sum(row["kind"] == "json" for row in manifest_records)
    manifest = {
        "schema": SCHEMA,
        "id": CLOSURE_ID,
        "purpose": (
            "Portable exact-byte dependency closure for recursive q79 quantum-gravity "
            "terminal verification."
        ),
        "claim_scope": {
            "tier": "INTEGRITY_SUPPORT_ONLY",
            "promotes_scientific_claims": False,
            "closes_open_q79_theorems": False,
            "replaces_source_packet_checks": False,
        },
        "terminal": {
            "logical_source_hint": terminal_hint,
            "sha256": terminal_hash,
        },
        "artifact_count": len(manifest_records),
        "json_artifact_count": json_count,
        "non_json_artifact_count": len(manifest_records) - json_count,
        "linked_input_edges": linked_input_edges,
        "total_bytes": sum(row["size_bytes"] for row in manifest_records),
        "records": manifest_records,
        "build_contract": {
            "content_addressed_by_sha256": True,
            "all_declared_input_hashes_verified_before_copy": True,
            "absolute_source_paths_excluded_from_manifest": True,
            "deterministic_manifest": True,
        },
    }
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "manifest": str(manifest_path),
                "artifacts": len(manifest_records),
                "json": json_count,
                "non_json": len(manifest_records) - json_count,
                "linked_input_edges": linked_input_edges,
                "total_bytes": manifest["total_bytes"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
