# Reproducibility

## Verify A Checkout

The quick verifier uses only the Python standard library:

```powershell
python verify.py
```

It verifies release hashes and independently recomputes 26 mathematical and
scope checks. To hash every archived source artifact as well:

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

- `inventory/artifacts.jsonl`: one SHA-256 row per source artifact.
- `inventory/numerical_objects.jsonl`: detected JSON scalar-array objects.
- `archive/sources/`: byte-preserving source snapshots.
- `release/authority/`: A01-A62 notes, certificates, calculations, and cited
  dependencies.
- `release/results/`: 28 high-signal result objects.
- `release/machine_evidence_catalog.jsonl`: complete machine-evidence index.

Historical files retain original absolute provenance paths. These are evidence
strings, not runtime dependencies. Portable release paths are recorded in the
generated manifests.

## Historical Calculators

The top-level verifier needs no third-party packages. Re-executing all archived
historical calculators additionally requires Python 3.11+, NumPy 2.2.6, and
CRunDec 0.7. The SMDR C source and its own license are archived at the pinned
source state.
