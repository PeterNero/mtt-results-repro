# MTT Results Reproduction

Current snapshot: 2026-08-16

This repository is a self-contained numerical-results capsule for Modal Triplet
Theory (MTT). It collects the matrices, spectra, scalar values, covariance
objects, exact discrete calculations, profile replays, conditional candidates,
and no-go results produced across the MTT calculation repositories.

The repository has three deliberately separate layers:

1. `inventory/` is exhaustive. It records every machine result, certificate,
   calculation script, audit, and detected numerical object from the pinned
   source repositories.
2. `archive/` is publication-safe and hash-preserving. It byte-mirrors ordinary
   artifacts under short content-addressed paths and keeps an exact SHA-256/size
   index for bulk diagnostics that would make a normal Git clone impractical.
   Original source paths remain in the inventory and blob map. Open, no-go,
   superseded, and retired routes remain discoverable at their declared tier.
3. `release/` is curated and versioned. It preserves the 2026-07-12 A01-A62
   Standard-Model baseline and adds a 2026-08-16 promoted-results layer, with
   explicit claim tiers, stable short paths, provenance hashes, and paper-corpus
   identity data.

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
mirrored artifact and every hash-only index row. See `STATUS.md` for the scientific boundary and
`REPRODUCIBILITY.md` for the complete rebuild procedure.

## Snapshot Contents

- 23 configured source trees/documents;
- 29,060 SHA-256-indexed artifacts;
- 21,924 byte-mirrored artifacts and 7,136 hash-only bulk diagnostics;
- 61,647 detected numerical objects;
- all 99 configured authority entries indexed;
- 62 frozen A01-A62 baseline entries plus the 37-entry A63-A99 authority extension;
- 28 baseline short-path results plus 100 current promoted results;
- a lock to 139 canonical papers and all 138 latest Zenodo records;
- zero commercial-book artifacts in the public result archive.

## Build the exhaustive inventory

From a checkout next to the source repositories:

```powershell
python tools/build_inventory.py --source-root ..
python tools/snapshot_sources.py --source-root ..
python tools/build_release.py
```

The generated inventory is deterministic and includes SHA-256 hashes for every
indexed artifact. Source repositories are pinned in
`config/source_repositories.json`; public mirroring policy is explicit in
`config/archive_policy.json`.

The current census covers 22 sources, including the frozen SM baseline and the
newer QM/QFT source proof, quantum-gravity cutsets, closure-dynamics language
work, Eta9 execution packets, and unified-source theorem repository. Large
exploratory trees remain exhaustively indexed where configured; only explicitly
selected artifacts enter the promoted current layer.

## Current publication boundary

The preserved internally verified baseline is embedded renormalized-Standard-Model
equivalence at the declared one-shared-physical-primitive/profile standard.
Strict zero-primitive/no-knob derivation and unique observed-universe selection
remain open. The finite internal spectrum source contract is closed at `10/10`,
while the selected common determinant is proved to provide only a matching-scale
translation rather than a nonuniversal gauge-coupling prediction.

The August layer adds exact or explicitly conditional results in operational
QM, free/formal QFT, projective HYM geometry, cohesive-superconnection language,
Eta9 reductions, the A63-A99 SM authority extension, and the unified-source
dependency chain through the committed G3FR frontier. The hidden branch now includes a locally free
holomorphic projective rank-nine object and an existential projective HYM
connection at their declared tiers. It does not promote the common visible-hidden
physical endpoint, the detecting meridian and period computation, the
interacting nonperturbative QFT construction, or the unified-source hypothesis
to closed physical theorems. G3FR also gives an exact finite component-20
inverse-system description, but its same-source characteristic-zero promotion
is the strict G3FS exit and remains open. The source verifier currently reports
two stale G3DI artifact locks, so G3FR is retained as the current committed
frontier rather than promoted as a portable verified proof package. See
`release/current_snapshot.json` and `STATUS.md`.

The public paper corpus is pinned by `release/paper_corpus_lock.json` to the
`mtt-papers` commit whose 138 released PDFs exactly match the latest Zenodo
records. The commercial book *The Universe Has a Bad Memory* is intentionally
excluded from both public repositories.

The BEQ/FMO layer now also includes the predeclared canonical `D3,K1`
higher-corner stabilization certificate and the independently replayed two-seed
direct bath-aware control result. The tested canonical waveform and both local
direct-control candidates are rejected at their declared tiers; bath-aware
controllability and calibrated apparatus realization remain open.
