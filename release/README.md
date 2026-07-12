# Curated Release Surface

This directory contains the readable publication layer built from the complete
archive.

- `authority_manifest.json` classifies all A01-A62 entries and records every
  bundled source hash.
- `authority/Axx/` contains each theorem note, its candidate/certificate,
  builder/audit, subordinate packets, and directly cited dependencies.
- `result_manifest.json` selects 28 high-signal matrices, values, spectra,
  ledgers, and adjacent-program summaries.
- `results/` contains those result objects in short stable paths.
- `parameter_ledger.json` separates MTT construction primitives from measured
  profile coordinates and transported outputs.
- `machine_evidence_catalog.jsonl` indexes every certificate, result packet,
  calculation, audit, report, and data object in the complete archive.

Every release object references SHA-256 entries from
`inventory/artifacts.jsonl` and declares whether it is exact, numerically
certified, profile replay, conditional, no-go, open, retired, or support-only.

Historical packets are never allowed to override a later authority entry.
