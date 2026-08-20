# MTT Results Reproduction

Current snapshot: 2026-08-20

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
   Standard-Model baseline and adds a 2026-08-20 promoted-results layer, with
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
checks all curated hashes, including the portable q79 quantum-gravity terminal
dependency closure. Use `python verify.py --full-archive` to check every mirrored
artifact and every hash-only index row. See `STATUS.md` for the scientific
boundary and `REPRODUCIBILITY.md` for the complete rebuild procedure.

## Snapshot Contents

- 24 configured source trees/documents;
- 25,490 SHA-256-indexed committed artifacts;
- 21,778 byte-mirrored artifacts and 3,712 hash-only bulk diagnostics;
- 56,295 detected numerical objects;
- all 99 configured authority entries indexed;
- 62 frozen A01-A62 baseline entries plus the 37-entry A63-A99 authority extension;
- 28 baseline short-path results plus 133 current promoted results;
- a 77-file, 206-edge exact-byte q79 terminal dependency closure;
- a lock to 139 canonical papers and all 138 latest Zenodo records;
- zero commercial-book artifacts in the public result archive.

## Build the exhaustive inventory

From a checkout next to the source repositories:

```powershell
python tools/build_inventory.py --source-root .. --committed-only
python tools/snapshot_sources.py --source-root ..
python tools/build_release.py
```

The generated inventory is deterministic and includes SHA-256 hashes for every
indexed artifact. Source repositories are pinned in
`config/source_repositories.json`; public mirroring policy is explicit in
`config/archive_policy.json`.

The current census covers 24 sources, including the frozen SM baseline and the
newer QM/QFT source proof, quantum-gravity cutsets, closure-dynamics language
work, the preprojection repair calculus, Eta9 execution packets, and the
unified-source theorem repository. Large
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
QM, free/formal QFT, projective HYM geometry, cohesive-superconnection and
nonlinear repair-descent language, Eta9 reductions, the A63-A99 SM authority
extension, and the unified-source dependency chain through the committed G3FR
frontier. The hidden branch now includes a locally free
holomorphic projective rank-nine object and an existential projective HYM
connection at their declared tiers. It does not promote the common visible-hidden
physical endpoint, the detecting meridian and period computation, the
interacting nonperturbative QFT construction, or the unified-source hypothesis
to closed physical theorems.

The new geometry layer closes the global support-stratified strain symbol,
corrects the former global deck-`S3` requirement to an associated monodromy
local system, globalizes the shared-root `C4` action, and compresses the literal
2/11 Fourier-Mukai/HYM checklist to three sequential physical-source packages.
The hidden qutrit adjoint decomposition also gives a conditional rank-102 mask
reduction from 10,404 to 1,548 ordered positions. None of these results supplies
the selected visible/common HYM endpoint or its physical matrix entries.

The preprojection repair layer adds 21 exact local, finite/formal or
selected-topological certificates. Its strongest new implications are the
twisted-Morita descent of the curved coefficient calculus, the strict rational
Hirsch transfer of the selected q79 topology, the transported-metric comparison
contract and the derivation of all finite/formal repair vertices and Wick graph
weights from one residual-and-metric jet. These results reduce dependencies and
locate the remaining physical data; they do not select the endpoint, identify a
Lorentzian/BV action, quantize the repair functional or construct the literal
continuum-to-27 intertwiner.

G3FR gives an exact finite component-20 inverse-system description, but its
same-source characteristic-zero promotion is the strict G3FS exit and remains
open. A clean checkout of the committed UST snapshot currently lacks the
required generated packed-matrix self-test object, so that campaign is retained
as an ongoing, nonportable frontier rather than a promoted portable proof
package. See `release/current_snapshot.json` and `STATUS.md`.

The q79 dependency closure under `release/dependency_closures/` is a portability
layer only. It preserves the exact packets and computer-algebra scripts needed
by recursive verification when their historical source folders are absent; it
does not promote any open q79 result or replace the checks inside those packets.

The public paper corpus is pinned by `release/paper_corpus_lock.json` to the
`mtt-papers` commit whose 138 released PDFs exactly match the latest Zenodo
records. The commercial book *The Universe Has a Bad Memory* is intentionally
excluded from both public repositories.

The BEQ/FMO layer now also includes the predeclared canonical `D3,K1`
higher-corner stabilization certificate and the independently replayed two-seed
direct bath-aware control result. The tested canonical waveform and both local
direct-control candidates are rejected at their declared tiers; bath-aware
controllability and calibrated apparatus realization remain open. The broad
100 fs finite-probe branch passes all four bounded rows at exploratory `D1,K0`,
then fails its first depth comparisons. The one authorized corrected-accuracy
`D4,K0` rung passes the inherited replay gate and stabilizes the effect tensor
relative to `D3,K0`, but all four bounded rows fail. The frozen classifier thus
records a stable negative for this profile. No `D5` rung is authorized; this is
not infinite-HEOM convergence or a general readout no-go.
