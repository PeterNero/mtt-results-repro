# MTT SM-Equivalence Reference Data Values Fill v1

Status: `MTT_SM_EQUIVALENCE_REFERENCE_DATA_VALUES_FILL_BUILT_PARTIAL_REPLAY_SEED`.

## Result

The first frozen measured-reference packet is built.  It fills PDG 2025 mass
seeds, CODATA 2022 `alpha` and `G_F`, derives `v=(sqrt(2)G_F)^(-1/2)`, and
computes tree-level diagonal Yukawa magnitudes.

This is intentionally partial.  It does not yet fill CKM, PMNS, the full
`alpha_1, alpha_2, alpha_3` running triplet, RG transport to a common scale, or
full complex Yukawa matrices.

## Guardrail

The filled values are downstream SM-equivalence inputs only.  They do not select
source structure, topology, branch, dynamic overlap tensor, `A_selected`,
`b_selected`, or no-knob kernels.

## Next

Build `MTT_SM_Equivalence_Tree_Level_Replay_Seed_v1`: run the first tree-level replay from the frozen seed values and
identify the exact remaining convention packets needed for full SM-equivalence.
