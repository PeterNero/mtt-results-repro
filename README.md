# MTT Results Reproduction

Current snapshot: 2026-07-12

This repository is a self-contained numerical-results capsule for Modal Triplet
Theory (MTT). It collects the matrices, spectra, scalar values, covariance
objects, exact discrete calculations, profile replays, conditional candidates,
and no-go results produced across the MTT calculation repositories.

The repository has three deliberately separate layers:

1. `inventory/` is exhaustive. It records every machine result, certificate,
   calculation script, audit, and detected numerical object from the pinned
   source repositories.
2. `archive/` is exhaustive and hash-preserving. It contains every indexed
   source artifact, including open, no-go, superseded, and retired routes.
3. `release/` is curated. It contains the latest authoritative objects,
   with explicit claim tiers, stable short paths, provenance hashes, and the
   calculations available for each authority bundle.

Publication of a result here does not change its epistemic status. In
particular, profile replay is not relabeled as a no-knob prediction, and a
conditional theorem is not relabeled as unconditional closure.

## Claim tiers

- `DERIVED_EXACT`: exact from declared mathematical inputs.
- `NUMERIC_CERTIFIED`: numerical result with an executable residual or error certificate.
- `PROFILE_REPLAY`: reproduces admitted measured/profile inputs.
- `CONDITIONAL`: follows only under explicitly listed premises.
- `NO_GO`: executable obstruction or impossibility result.
- `OPEN`: required object or value is not yet emitted.
- `RETIRED`: historical route retained only for provenance.

## Verify

```powershell
python verify.py
```

The verifier independently recomputes the headline finite calculations and
checks all curated hashes. Use `python verify.py --full-archive` to check every
archived artifact. See `STATUS.md` for the scientific boundary and
`REPRODUCIBILITY.md` for the complete rebuild procedure.

## Snapshot Contents

- 16 configured source trees/documents;
- 15,351 archived artifacts;
- 10,921 detected numerical objects;
- 62 current authority entries;
- 553 files in the current authority bundles;
- 28 short-path key results;
- 12,284 machine-evidence catalog rows.

## Build the exhaustive inventory

From a checkout next to the source repositories:

```powershell
python tools/build_inventory.py --source-root ..
python tools/snapshot_sources.py --source-root ..
python tools/build_release.py
```

The generated inventory is deterministic and includes SHA-256 hashes for every
indexed artifact. Source repositories are pinned in
`config/source_repositories.json`.

The current census covers 16 sources, including all Git repositories under the
calculation workspace, the loose foundation/fixed-point calculations, the
simulation design, the book audit, and the standalone master corrigendum.

## Current publication boundary

The internally verified baseline is embedded renormalized-Standard-Model
equivalence at the declared one-shared-physical-primitive/profile standard.
Strict zero-primitive/no-knob derivation and unique observed-universe selection
remain open. The finite internal spectrum source contract is closed at `10/10`,
while the selected common determinant is proved to provide only a matching-scale
translation rather than a nonuniversal gauge-coupling prediction.
