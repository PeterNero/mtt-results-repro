# MTT SM-Equivalence CKM Gauge PMNS Convention Fill v1

Status: `MTT_SM_EQUIVALENCE_CKM_GAUGE_PMNS_CONVENTION_FILL_BUILT_REPLAY_READY`.

## Result

CKM and PMNS seed matrices are now convention-filled for downstream measured
SM-equivalence replay.  The gauge packet fixes the `M_Z`-scale convention and
normalization formulas but leaves `alpha_em(M_Z)` and the full
`alpha_1, alpha_2, alpha_3` numeric triplet open.

## Guardrail

These values are measured replay inputs.  They do not select MTT source
structure, topology, dynamic overlap tensors, `A_selected`, `b_selected`, or
no-knob kernels.

## Next

Build `MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1`.
