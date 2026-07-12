"""Build a deterministic cross-repository inventory of MTT result artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "source_repositories.json"
INVENTORY = ROOT / "inventory"
AUTHORITY_PATTERN = re.compile(r"^- \*\*(A\d{2})\*\* `([^`]+)`: (.+)$")
INDEXED_SUFFIXES = {".json", ".py", ".md", ".txt", ".csv", ".tsv", ".npz", ".npy"}
INDEXED_ROOTS = ("certificates", "candidate_data", "scripts", "proof_corpus", "reports")
IMPORTANT_KEY_PATTERN = re.compile(
    r"matrix|matrices|spectrum|spectra|eigen|covariance|correlation|yukawa|ckm|pmns|"
    r"mass|higgs|gauge|threshold|constant|coupling|operator|hessian|dirac|phase|q79|"
    r"logdet|determinant|residual|error|value|row",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(path: Path, *args: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), *args],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
            count += 1
    return count


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def numeric_shape(value: Any) -> tuple[int, ...] | None:
    if is_number(value):
        return ()
    if not isinstance(value, list) or not value:
        return None
    child_shapes = [numeric_shape(item) for item in value]
    if any(shape is None for shape in child_shapes):
        return None
    first = child_shapes[0]
    if any(shape != first for shape in child_shapes):
        return None
    return (len(value),) + first


def flatten_numeric(value: Any) -> list[float]:
    if is_number(value):
        return [float(value)]
    output: list[float] = []
    for item in value:
        output.extend(flatten_numeric(item))
    return output


def walk_json(value: Any, pointer: str = "") -> Iterable[tuple[str, str, Any]]:
    if isinstance(value, dict):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from walk_json(value[key], f"{pointer}/{escaped}")
    elif isinstance(value, list):
        shape = numeric_shape(value)
        if shape is not None and shape:
            yield pointer or "/", "numeric_array", value
        else:
            for index, item in enumerate(value):
                yield from walk_json(item, f"{pointer}/{index}")
    elif isinstance(value, bool):
        yield pointer or "/", "boolean", value
    elif is_number(value):
        yield pointer or "/", "number", value
    elif isinstance(value, str):
        yield pointer or "/", "string", value


def infer_tier(payload: dict[str, Any], path: str) -> tuple[str, list[str]]:
    status = str(payload.get("status", "")).upper()
    text = f"{status} {path.upper()}"
    reasons: list[str] = []
    if payload.get("target_fitting_used") is True:
        reasons.append("target_fitting_used=true")
    if any(token in text for token in ("RETIRED", "WITHDRAWN", "SUPERSEDED")):
        return "RETIRED", reasons + ["status/path keyword"]
    if any(token in text for token in ("NO_GO", "NOGO", "REFUT", "IMPOSSIB", "OBSTRUCTION")):
        return "NO_GO", reasons + ["status/path keyword"]
    if any(token in text for token in ("PROFILE", "REPLAY", "BENCHMARK", "CALIBRAT")):
        return "PROFILE_REPLAY", reasons + ["status/path keyword"]
    if any(token in text for token in ("CONDITIONAL", "IF_GATE", "PREMISE")):
        return "CONDITIONAL", reasons + ["status/path keyword"]
    if any(token in text for token in ("OPEN", "PARTIAL", "UNDERDETERMINED", "VALUES_REQUIRED", "BLOCKED")):
        return "OPEN", reasons + ["status/path keyword"]
    closed_flags = (
        payload.get("closure_claimed") is True
        or payload.get("theorem_proved") is True
        or payload.get("proved") is True
    )
    if closed_flags and not reasons:
        return "NUMERIC_CERTIFIED", ["top-level closure/proof flag"]
    return "UNCLASSIFIED", reasons


def artifact_kind(relative: Path, source_type: str = "repository") -> str:
    if source_type == "standalone_document":
        return "authority_document"
    first = relative.parts[0] if relative.parts else "root"
    suffix = relative.suffix.lower()
    if first == "certificates":
        return "certificate"
    if first == "candidate_data":
        return "result_packet"
    if first == "scripts":
        return "calculation"
    if first == "proof_corpus" and suffix == ".py":
        return "audit"
    if first == "proof_corpus":
        return "proof_note"
    if first == "reports":
        return "report"
    if suffix in {".py", ".c", ".cc", ".cpp", ".h", ".hpp", ".js", ".jsx", ".ts", ".tsx", ".m"}:
        return "source_code"
    if suffix in {".json", ".csv", ".tsv", ".npy", ".npz"}:
        return "data"
    if suffix in {".toml", ".yaml", ".yml", ".ini", ".cfg"}:
        return "configuration"
    if suffix in {".md", ".txt", ".rst", ".tex"}:
        return "documentation"
    return "other"


def tracked_files(repo_path: Path) -> list[Path]:
    try:
        raw = subprocess.check_output(
            ["git", "-C", str(repo_path), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    output = []
    for encoded in raw.split(b"\0"):
        if not encoded:
            continue
        relative = Path(encoded.decode("utf-8", errors="surrogateescape"))
        path = repo_path / relative
        if path.is_file():
            output.append(path)
    return sorted(output)


def iter_artifacts(repo_path: Path, source_type: str = "repository") -> Iterable[Path]:
    if repo_path.is_file():
        yield repo_path
        return

    if source_type == "document_directory":
        for path in sorted(repo_path.rglob("*")):
            if path.is_file() and path.suffix.lower() in INDEXED_SUFFIXES:
                yield path
        return

    tracked = tracked_files(repo_path)
    if tracked:
        yield from tracked
        return

    seen: set[Path] = set()
    for root_name in INDEXED_ROOTS:
        base = repo_path / root_name
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.suffix.lower() in INDEXED_SUFFIXES and path not in seen:
                seen.add(path)
                yield path
    for name in ("README.md", "requirements.txt", "pyproject.toml", "CITATION.cff"):
        path = repo_path / name
        if path.is_file() and path not in seen:
            yield path


def extract_authority_entries(
    source_root: Path,
    repo_lookup: dict[str, str],
    standalone_lookup: dict[str, tuple[str, str]],
) -> list[dict[str, Any]]:
    ledger = source_root / "18 Theta-Closure & Execution Program" / "MTT_CORPUS_REVISION_UPDATE_LEDGER_2026-07-11.md"
    if not ledger.exists():
        return []
    rows = []
    for line_number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), start=1):
        match = AUTHORITY_PATTERN.match(line)
        if not match:
            continue
        authority_id, raw_path, description = match.groups()
        normalized = raw_path.replace("\\", "/")
        repo_id = None
        relative_path = None
        standalone = standalone_lookup.get(normalized.lower())
        if standalone:
            repo_id, relative_path = standalone
        for name, candidate_id in repo_lookup.items():
            if repo_id is not None:
                break
            marker = f"/{name}/"
            if marker.lower() in normalized.lower():
                repo_id = candidate_id
                relative_path = normalized.lower().split(marker.lower(), 1)[1]
                break
        rows.append(
            {
                "authority_id": authority_id,
                "description": description,
                "ledger_line": line_number,
                "repo_id": repo_id,
                "relative_path": relative_path,
                "source_path_recorded": raw_path,
            }
        )
    return sorted(rows, key=lambda row: int(row["authority_id"][1:]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))

    repository_rows = []
    artifact_rows: list[dict[str, Any]] = []
    numerical_rows: list[dict[str, Any]] = []
    summary_by_repo: dict[str, Counter] = defaultdict(Counter)
    tier_counts: Counter = Counter()

    for repo in config["repositories"]:
        repo_path = source_root / Path(repo["local_relative_path"])
        exists = repo_path.exists()
        git_source = exists and repo_path.is_dir() and (repo_path / ".git").exists()
        head = git(repo_path, "rev-parse", "HEAD") if git_source else None
        upstream = git(repo_path, "rev-parse", "@{upstream}") if git_source else None
        remote = git(repo_path, "remote", "get-url", "origin") if git_source else None
        status_porcelain = git(repo_path, "status", "--porcelain") if git_source else None
        dirty = bool(status_porcelain) if git_source else None
        repository_rows.append(
            {
                **repo,
                "exists_in_build_environment": exists,
                "git_repository": git_source,
                "git_head": head,
                "git_upstream": upstream,
                "git_synced": bool(head and upstream and head == upstream),
                "git_dirty": dirty,
                "git_status_porcelain": status_porcelain.splitlines() if status_porcelain else [],
                "remote": remote,
            }
        )
        if not exists:
            continue

        for path in iter_artifacts(repo_path, repo.get("source_type", "repository")):
            relative = Path(path.name) if repo_path.is_file() else path.relative_to(repo_path)
            kind = artifact_kind(relative, repo.get("source_type", "repository"))
            row: dict[str, Any] = {
                "repo_id": repo["id"],
                "repo_name": repo["name"],
                "path": relative.as_posix(),
                "kind": kind,
                "suffix": path.suffix.lower(),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            summary_by_repo[repo["id"]][kind] += 1
            if path.suffix.lower() == ".json":
                try:
                    payload = json.loads(path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                    row["json_error"] = str(exc)
                else:
                    if isinstance(payload, dict):
                        tier, reasons = infer_tier(payload, relative.as_posix())
                        row.update(
                            {
                                "schema": payload.get("schema"),
                                "status": payload.get("status"),
                                "certificate": payload.get("certificate"),
                                "next_required_artifact": payload.get("next_required_artifact"),
                                "heuristic_tier": tier,
                                "tier_reasons": reasons,
                                "needs_curated_review": True,
                            }
                        )
                        tier_counts[tier] += 1
                        counts = Counter()
                        for pointer, leaf_kind, leaf in walk_json(payload):
                            counts[leaf_kind] += 1
                            if leaf_kind == "numeric_array":
                                shape = numeric_shape(leaf)
                                values = flatten_numeric(leaf)
                                key_text = pointer.rsplit("/", 1)[-1]
                                numerical_rows.append(
                                    {
                                        "repo_id": repo["id"],
                                        "artifact_path": relative.as_posix(),
                                        "json_pointer": pointer,
                                        "shape": list(shape or ()),
                                        "element_count": len(values),
                                        "minimum": min(values),
                                        "maximum": max(values),
                                        "important_key": bool(IMPORTANT_KEY_PATTERN.search(key_text)),
                                        "artifact_sha256": row["sha256"],
                                    }
                                )
                        row["json_leaf_counts"] = dict(counts)
            artifact_rows.append(row)

    artifact_rows_by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for artifact in artifact_rows:
        artifact_rows_by_repo[artifact["repo_id"]].append(artifact)
    for repository in repository_rows:
        indexed = sorted(artifact_rows_by_repo[repository["id"]], key=lambda row: row["path"])
        digest = hashlib.sha256()
        for artifact in indexed:
            digest.update(artifact["path"].encode("utf-8"))
            digest.update(b"\0")
            digest.update(artifact["sha256"].encode("ascii"))
            digest.update(b"\n")
        repository["indexed_artifact_count"] = len(indexed)
        repository["indexed_artifact_tree_sha256"] = digest.hexdigest()

    repo_lookup = {repo["name"]: repo["id"] for repo in config["repositories"]}
    standalone_lookup = {
        str((source_root / Path(repo["local_relative_path"])).resolve()).replace("\\", "/").lower(): (
            repo["id"],
            Path(repo["local_relative_path"]).name.lower(),
        )
        for repo in config["repositories"]
        if repo.get("source_type") == "standalone_document"
    }
    authority_rows = extract_authority_entries(source_root, repo_lookup, standalone_lookup)
    artifact_index = {(row["repo_id"], row["path"].lower()): row for row in artifact_rows}
    for authority in authority_rows:
        key = (authority["repo_id"], str(authority["relative_path"]).lower())
        matched = artifact_index.get(key)
        authority["artifact_indexed"] = matched is not None
        authority["artifact_sha256"] = matched["sha256"] if matched else None

    repository_rows = sorted(repository_rows, key=lambda row: row["id"])
    artifact_rows = sorted(artifact_rows, key=lambda row: (row["repo_id"], row["path"]))
    numerical_rows = sorted(
        numerical_rows,
        key=lambda row: (row["repo_id"], row["artifact_path"], row["json_pointer"]),
    )
    dump(INVENTORY / "source_repositories.json", {"schema": "MTTSourceRepositorySnapshot.v1", "repositories": repository_rows})
    dump(INVENTORY / "authority_entries.json", {"schema": "MTTAuthorityEntryInventory.v1", "entries": authority_rows})
    artifact_count = write_jsonl(INVENTORY / "artifacts.jsonl", artifact_rows)
    numerical_count = write_jsonl(INVENTORY / "numerical_objects.jsonl", numerical_rows)
    summary = {
        "schema": "MTTCrossRepositoryInventorySummary.v1",
        "source_root_recorded_as": "<LOCAL_SOURCE_ROOT>",
        "repository_count_configured": len(config["repositories"]),
        "repository_count_found": sum(row["exists_in_build_environment"] for row in repository_rows),
        "artifact_count": artifact_count,
        "numerical_object_count": numerical_count,
        "authority_entry_count": len(authority_rows),
        "authority_entries_indexed": sum(row["artifact_indexed"] for row in authority_rows),
        "heuristic_tier_counts": dict(sorted(tier_counts.items())),
        "artifact_counts_by_repo": {
            repo_id: dict(sorted(counts.items())) for repo_id, counts in sorted(summary_by_repo.items())
        },
        "completeness_policy": {
            "all_configured_repositories_found": all(row["exists_in_build_environment"] for row in repository_rows),
            "all_authority_entries_indexed": all(row["artifact_indexed"] for row in authority_rows),
            "heuristic_tiers_are_authority": False,
            "curated_release_must_reference_inventory_hashes": True,
        },
    }
    dump(INVENTORY / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
