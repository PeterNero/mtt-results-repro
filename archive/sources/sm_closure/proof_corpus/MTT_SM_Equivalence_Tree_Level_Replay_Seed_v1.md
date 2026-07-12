# MTT SM-Equivalence Tree-Level Replay Seed v1

Status: `MTT_SM_EQUIVALENCE_TREE_LEVEL_REPLAY_SEED_BUILT_PARTIAL_NUMERIC_REPLAY`.

## Result

The first numeric replay is executable.  It builds diagonal Yukawa matrices from
the frozen measured masses and `v`, then replays the masses through
`m_f=y_f v/sqrt(2)` with residual below machine precision.  It also computes a
tree-level Higgs quartic seed and an on-shell electroweak coupling seed from
`m_W`, `m_Z`, and `v`.

This is not full SM-equivalence.  CKM, PMNS, full running gauge couplings,
common-scale RG transport, and full complex Yukawa matrices remain open.

## Next

Build `MTT_SM_Equivalence_CKM_Gauge_PMNS_Convention_Fill_v1`.
