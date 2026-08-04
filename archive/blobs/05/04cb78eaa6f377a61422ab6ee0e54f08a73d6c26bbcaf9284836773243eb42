# MTT Core Axioms and Measured-Parameter Interface v1

## Purpose

This artifact closes the SM-parity measured-input policy.  It does not close
SM-parity itself, and it does not claim no-knob derivation of constants.

SM-parity means MTT may admit measured values at the same standard used by
SM/QFT/GR, but only as typed downstream data.  No-knob closure remains the
stronger target: every measured value must keep a replacement target from
selected internal MTT data.

## Core Axioms

- `sector_axiom`: An MTT sector S is a typed modal package with carriers, maps, admissibility data, and declared interfaces.
- `admissibility_axiom`: Adm(S) is checked before measured parity inputs are admitted; measured values cannot establish Adm(S).
- `selection_axiom`: Sel(S) or Sigma_S records source data selected by MTT/corpus structure, not by empirical target fitting.
- `observable_axiom`: Obs_S maps selected sector data and admitted parameters to observables with explicit conventions.
- `measured_parameter_axiom`: Param_S contains typed slots whose measured values may enter only as SM-parity inputs.
- `non_selection_axiom`: Measured parity inputs are downstream data and cannot choose source, topology, quotient, operator packet, or branch.
- `upgrade_axiom`: Every measured parity input has a no-knob upgrade target that remains open until the selected internal computation is supplied.

## Parameter Classes

- `MEASURED_PARITY_INPUT`: A value admitted at the same standard as SM/QFT/GR measured parameters.
- `SELECTED_SOURCE_DATA`: Internal MTT/corpus data selected before empirical parameter use.
- `DIAGNOSTIC_FIXTURE`: Prototype, validator, benchmark, or identity map used to test machinery.
- `NO_KNOB_TARGET`: A future derivation obligation replacing a measured parity input.

## Slot Schema

Every measured parity slot must declare:

```text
name, sector, kind, value_domain, units, convention, uncertainty, provenance, allowed_use, forbidden_use, no_knob_target, downstream_artifacts
```

## Admission Rules

- The slot must be declared before any downstream computation that uses it.
- The slot must be typed by sector and kind.
- The value domain, units, convention, uncertainty, and provenance must be explicit.
- The value may be used only for SM-parity recovery or empirical comparison.
- The value may not select a source, branch, operator packet, topology, quotient, or representation.
- The value may not be reused as evidence for no-knob closure.
- Every measured slot must carry a no-knob replacement target.
- Diagnostic fixtures and identity validators must be excluded from physical parameter slots.

## Forbidden Shortcuts

- source selection by measured constants
- branch or quotient selection by target residual
- post-hoc fitting after observing the desired output
- direct q79/S3 import as a Qa/SU3 proof source
- generic existence theorem replacing actual maps
- identity rho_E or diagnostic validator treated as physical data
- benchmark Yukawa, CKM, PMNS, threshold, or mass entries treated as selected matrices

## Sector Interfaces

- `QM`: Hilbert/state, observable, Born/record, and update slots. Policy: Measurement rules may be axiomatized for SM-parity; no-knob target is record/Born selection from admissibility.
- `QFT`: Field content, gauge action, local operator algebra, renormalized parameter slots, and scale conventions. Policy: Renormalized couplings may be measured parity inputs after sector selection.
- `SM`: Gauge group, representation packet, Higgs carrier, Yukawa matrices, mixing matrices, CP phases, and RG scheme. Policy: Gauge/Yukawa/CP/Higgs values may be measured inputs only after the SM sector embedding is declared.
- `GR`: Metric, connection/curvature, stress-energy coupling, Newton scale, cosmological/boundary slots. Policy: Dimensionful anchors may be measured for parity while physical absolute normalization remains a no-knob target.
- `Units`: Unit system, conversion anchors, dimensional conventions, and uncertainty propagation. Policy: Dimensionful values require units and provenance; unit choices cannot be hidden knobs.

## Theorem

The measured-parameter interface is admissible for SM-parity iff each measured
value is declared as a typed slot before downstream use, carries units,
convention, uncertainty, provenance, and a no-knob upgrade target, and is not
used to select the MTT source, topology, quotient, operator packet, branch, or
representation.

Therefore this artifact permits measured constants as SM-parity data while
blocking target fitting and blocking their reuse as no-knob proof.

## What This Closes

- core_axiom_scaffold
- measured_parameter_admission_policy
- parameter_slot_schema
- forbidden_shortcuts
- no_knob_upgrade_obligation

## What Remains Open

- SM_sector_embedding_theorem
- QM_QFT_GR_recovery_theorem
- empirical_equivalence_ledger
- no_knob_constants

## Next Artifact

```text
MTT_SM_Sector_Embedding_Interface_v1
```
