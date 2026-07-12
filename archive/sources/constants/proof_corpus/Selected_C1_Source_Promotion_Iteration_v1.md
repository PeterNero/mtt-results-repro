# Selected C1 Source Promotion Iteration v1

## Result

The iteration did not find a legal selected-source import.  It did find the
precise circularity blocking the C1 rebuild:

```text
source promotion wants selected D_E/dotD/Riesz/Green payload
C1 rebuild wants selected source plus selected D_E/dotD/Riesz/Green payload
```

Therefore the next step cannot be another flag lift.  The non-circular break
point is `FiniteEmissionMorphism_Phi_fin_with_selected_payload`, implemented as
`Selected_PhiFin_C1_Emission_Packet_v1`.

## Imported Candidates

| input | classification | status | usable as proof source |
| --- | --- | --- | --- |
| `local_rebuild_attempt` | `negative_rebuild_attempt` | `SELECTED_C1_OPERATOR_REBUILD_ATTEMPT_EXECUTED_SELECTED_BLOCKS_STILL_OPEN` | no |
| `q79_promotion_gate` | `validator_gate_not_source` | `IWASAWA_SELECTED_SOURCE_PROMOTION_GATE_FORMULATED` | no |
| `q79_valpha_sufficiency` | `conditional_sufficiency_theorem` | `SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_PROVED_SOURCE_OPEN` | no |
| `q79_m1_deresponse_target` | `conditional_lifted_consistency_check` | `TIME_ORIENTED_M1_DERESPONSE_TARGET_COHERENT_SELECTED_SOURCE_OPEN` | no |
| `sm_source_origin_lemma` | `reduction_to_phi_fin` | `MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_LEMMA_REDUCED_TO_FINITE_EMISSION_MORPHISM` | no |
| `gr_paper_lemma` | `conditional_paper_lemma` | `ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN` | no |

## Cycle

Source promotion currently needs:

- theorem-derived selected_source_verified
- selected D_E/Riesz/Green/dotD payload
- nonzero same-branch dotD/source response

The C1 payload rebuild currently needs:

- selected source certificate
- selected D_E/Riesz/Green/dotD payload
- selected primitive C1 contractions
- selected sector response matrices
- selected Hessian blocks

This is why the conditional and hypothetical packets validate cleanly while the
honest packets fail: the validators are not the missing theorem.

## Solution Breakpoint

`FiniteEmissionMorphism_Phi_fin_with_selected_payload`

It starts from the selected Strominger/HYM minimizer in the fixed q79/F,m=1 S3/GS sector and emits finite rho_E, D_E, Riesz/Green, dotD, and C1 data as images of that source, rather than importing selected flags from validators.

It must emit:

- selected non-identity rho_E or equivalent connection
- finite selected D_E blocks
- Riesz gaps and reduced Green operators with error/gap control
- same-branch dotD_alpha1 matrices and source vector b_selected
- primitive C1 overlap tensors
- sector response matrices giving A_selected

## Acceptance Tests

- does not set selected_source_verified by hand
- does not use hypothetical_selected packets
- does not use observed masses, mixings, gauge constants, or benchmark residuals
- emits A_selected and b_selected from one branch source
- passes D_E, Riesz/gap, reduced Green, dotD, and C1 response audits honestly
