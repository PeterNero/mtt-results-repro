# Reproducibility

## Verify A Checkout

The quick verifier uses only the Python standard library:

```powershell
python verify.py
```

It verifies release hashes, the frozen baseline, the current promoted layer,
the paper-corpus lock, the commercial-book exclusion, and the independent
mathematical/scope checks. It also hashes all 77 files in the portable q79
terminal dependency closure on every run. To hash every artifact in the larger
general source archive as well:

```powershell
python verify.py --full-archive
```

The result is written to `verification_report.json`.

## Rebuild From Source Repositories

Place this checkout next to the source repositories listed in
`config/source_repositories.json`, then run:

```powershell
python tools/build_inventory.py --source-root .. --committed-only
python tools/snapshot_sources.py --source-root ..
python tools/build_release.py
python tools/build_dependency_closure.py
python verify.py --full-archive
```

`inventory/source_repositories.json` records every Git HEAD, upstream state,
remote refs containing the selected head, working-tree status, artifact count,
artifact-tree SHA-256 and inventory scope. The publication command above uses
only Git-tracked paths for repository sources. A dirty source tree is still
reported and must be replaced by a detached clean worktree when selected paths
could differ from the commit.

Public snapshots must be built from clean checkouts of every repository that
contributes promoted or exhaustive evidence. When a research checkout contains
ongoing work, create a detached clean worktree at the selected commit and expose
that worktree under the same configured relative path in a staging source root.
This prevents uncommitted calculations from entering the public archive while
preserving the exact selected Git object bytes.

## Layout

- `inventory/artifacts.jsonl`: one SHA-256 row per configured source artifact.
- `inventory/numerical_objects.jsonl`: detected JSON scalar-array objects.
- `archive/blobs/`: byte-preserving, content-addressed snapshots for
  publication-safe artifacts; original paths remain in the inventory and map.
- `archive/artifact_blob_map.jsonl`: source-path to short blob-path mapping.
- `archive/hash_only_artifacts.jsonl`: exact SHA-256 and size rows for large raw
  diagnostics omitted from the Git mirror.
- `release/authority/`: frozen A01-A62 baseline plus the A63-A99 authority
  extension, with notes, certificates, calculations, and cited dependencies.
- `release/results/`: 28 baseline result objects and 133 promoted current result
  objects.
- `release/current_snapshot.json`: version boundary, current result IDs, source
  states, claim guard, and unified-source frontier.
- `release/paper_corpus_lock.json`: exact public-paper commit and Zenodo identity
  census for 139 canonical papers.
- `release/machine_evidence_catalog.jsonl`: complete machine-evidence index.
- `release/dependency_closures/q79_qg_terminal/`: portable exact-byte closure of
  the recursive q79 QG terminal graph, with its own content-addressed manifest.

Historical files retain original absolute provenance paths. These are evidence
strings, not runtime dependencies. Portable release paths are recorded in the
generated manifests.

The q79 closure builder first verifies all 206 declared input hashes against the
source workspace, then copies 77 unique files into a deterministic SHA-256
layout. It may use an already archived blob only when the historical source path
is absent. A present local source with the wrong hash is an error, so the
portability fallback cannot hide source drift. The closure is classified as
`INTEGRITY_SUPPORT_ONLY` and does not change the claim tier of any contained
packet.

The snapshot builder applies explicit source and archive policies. Files above
the public size threshold are hash-only unless they are source/document formats;
the large covariant floating-probe campaign is hash-only as one coherent raw
dataset. All promoted results and authority dependencies must remain mirrored.
Forbidden commercial-book path tokens are rejected during inventory construction
and again by the release verifier. The commercial manuscript and its companion
application are not reproducibility dependencies.

## Historical Calculators

The top-level verifier needs no third-party packages. Re-executing all archived
historical calculators additionally requires Python 3.11+, NumPy 2.2.6, and
CRunDec 0.7. The SMDR C source and its own license are archived at the pinned
source state.
