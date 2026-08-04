# Reproducibility

## Verify A Checkout

The quick verifier uses only the Python standard library:

```powershell
python verify.py
```

It verifies release hashes, the frozen baseline, the current promoted layer,
the paper-corpus lock, the commercial-book exclusion, and the independent
mathematical/scope checks. To hash every archived source artifact as well:

```powershell
python verify.py --full-archive
```

The result is written to `verification_report.json`.

## Rebuild From Source Repositories

Place this checkout next to the source repositories listed in
`config/source_repositories.json`, then run:

```powershell
python tools/build_inventory.py --source-root ..
python tools/snapshot_sources.py --source-root ..
python tools/build_release.py
python verify.py --full-archive
```

`inventory/source_repositories.json` records every Git HEAD, upstream state,
working-tree status, artifact count, and artifact-tree SHA-256. The artifact
tree hash covers uncommitted non-ignored files as well as committed files, so a
dirty source tree is not mistaken for the named commit.

## Layout

- `inventory/artifacts.jsonl`: one SHA-256 row per configured source artifact.
- `inventory/numerical_objects.jsonl`: detected JSON scalar-array objects.
- `archive/sources/`: byte-preserving snapshots for publication-safe artifacts.
- `archive/hash_only_artifacts.jsonl`: exact SHA-256 and size rows for large raw
  diagnostics omitted from the Git mirror.
- `release/authority/`: frozen A01-A62 baseline plus the A63-A99 authority
  extension, with notes, certificates, calculations, and cited dependencies.
- `release/results/`: 28 baseline result objects and 50 promoted current result
  objects.
- `release/current_snapshot.json`: version boundary, current result IDs, source
  states, claim guard, and unified-source frontier.
- `release/paper_corpus_lock.json`: exact public-paper commit and Zenodo identity
  census for 139 canonical papers.
- `release/machine_evidence_catalog.jsonl`: complete machine-evidence index.

Historical files retain original absolute provenance paths. These are evidence
strings, not runtime dependencies. Portable release paths are recorded in the
generated manifests.

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
