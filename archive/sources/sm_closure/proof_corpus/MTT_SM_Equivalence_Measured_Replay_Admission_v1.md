# MTT SM-Equivalence Measured Replay Admission v1

Status: `MTT_SM_EQUIVALENCE_MEASURED_REPLAY_ADMISSION_BUILT_DYNAMIC_OVERLAP_AS_NO_KNOB_UPGRADE`.

## Result

For this SM-equivalence branch, dynamic overlap/C1 primitive emission is
reclassified correctly:

```text
dynamic overlap tensor / A_selected / b_selected = no-knob upgrade target
measured Yukawa, CKM/PMNS, Higgs, gauge inputs = downstream SM-equivalence slots
```

This does not weaken the no-knob program.  It simply matches the Standard Model
standard: the SM itself uses measured Yukawa matrices, mixings, CP phases, Higgs
parameters, and gauge couplings.

## Admission Rule

Measured SM values may enter only after the source/interface boundary is
declared.  They may be used to replay SM calculations and empirical equivalence.
They may not select:

- source structure,
- topology or branch,
- primitive C1 contractions,
- dynamic overlap tensors,
- `A_selected` or `b_selected`.

## Next

Build `MTT_SM_Equivalence_Measured_Parameter_Replay_Manifest_v1`: a typed manifest of measured slots, conventions, provenance,
uncertainties, and replay targets.  That manifest is the immediate SM-equivalence
path.  Dynamic overlap remains the no-knob upgrade path.
