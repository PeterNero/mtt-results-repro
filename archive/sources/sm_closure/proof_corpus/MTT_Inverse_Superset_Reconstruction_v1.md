# MTT Inverse Superset Reconstruction v1

## Purpose

This artifact starts the inverse reconstruction track.  It deliberately allows
observed constants as discovery data so the superset branch space can be
searched.  It does not allow those constants to become forward selectors, and
it does not claim no-knob prediction.

The point is practical: a successful inverse fit may reveal the missing
selected packet needed by the current SM-parity frontier.

## Source Registry

- `selected_sm_packet_audit`: 2/2 present
- `no_knob_backlog`: 2/2 present
- `theta_program`: 2/2 present
- `topology_and_string_sources`: 2/2 present
- `q79_flavor_branch`: 2/2 present
- `qa_su3_packet`: 2/2 present
- `nonsm_constants`: 2/2 present

## Measured Targets and Candidate Superset Knobs

### gauge_couplings

- Measured targets: `alpha_em`, `sin2_theta_w`, `alpha_s`, `running_thresholds`
- Allowed use: `DISCOVERY_ONLY`
- Candidate superset knobs:
  - `heat_kernel_spectrum`
  - `threshold_packet`
  - `U1_normalization`
  - `SU2_SU3_embedding_index`
  - `same_branch_period_selector`
- Promotion test: Recovered knobs must be discrete or corpus-selected before they can enter the forward ledger.

### yukawa_masses_mixings

- Measured targets: `fermion_mass_ratios`, `CKM`, `PMNS`, `CP_phase`, `Higgs_yukawa_slots`
- Allowed use: `DISCOVERY_ONLY`
- Candidate superset knobs:
  - `overlap_kernel_blocks`
  - `typed_multiplication_maps`
  - `family_holonomy_or_index`
  - `q79_CP_branch`
  - `Higgs_carrier_section`
- Promotion test: Recovered overlap data must be computable from the same selected source packet, not from benchmark flavor entries.

### gravity_and_dimensionful_scales

- Measured targets: `G_N`, `Planck_scale`, `cosmological_normalization`, `absolute_units`
- Allowed use: `DISCOVERY_ONLY`
- Candidate superset knobs:
  - `internal_volume`
  - `modal_gap`
  - `G10_over_R1_cubed`
  - `shared_circle_scale`
  - `unit_dictionary_anchor`
- Promotion test: Recovered scale must match an independently selected normalization object.

### qa_su3_color_operator_packet

- Measured targets: `color_embedding`, `representation_packet`, `anomaly_table`, `operator_packet`
- Allowed use: `DISCOVERY_ONLY`
- Candidate superset knobs:
  - `D_E_or_rho_E_operator`
  - `typed_monad_maps`
  - `Cech_Dolbeault_representatives`
  - `section_ring_generators`
  - `Freed_Witten_Bianchi_source`
- Promotion test: Recovered packet must instantiate the selected representation/anomaly table and pass the Qa/SU3 source gate.


## Reconstruction Stages

### inverse_fit

- Purpose: Use observed constants to search the superset branch space.
- Claim allowed: A branch or packet is compatible with observed data.
- Claim forbidden: MTT predicts the constants from first principles.

### compression

- Purpose: Check whether fitted knobs collapse to a small discrete or algebraic packet.
- Claim allowed: The inverse fit points to a compact candidate source.
- Claim forbidden: A continuous free knob is promoted as selected data.

### corpus_alignment

- Purpose: Demand independent support from topology, theta, string/flux, q79, Qa/SU3, or non-SM artifacts.
- Claim allowed: The candidate is corpus-aligned.
- Claim forbidden: A numerically convenient packet is accepted without source evidence.

### forward_replay

- Purpose: Remove the measured constants as selectors and recompute forward from the candidate packet.
- Claim allowed: The candidate graduates into a forward proof obligation.
- Claim forbidden: The inverse fit itself closes SM-parity or no-knob closure.


## Guardrails

- Measured constants may rank candidate branches but may not select final source data.
- Every fitted knob must be tagged as continuous, discrete, algebraic, or corpus-selected.
- Continuous fitted knobs remain parity inputs or discovery diagnostics unless independently selected.
- No observed masses, couplings, CKM, PMNS, or CP values may be used inside a no-knob proof step.
- Promotion requires forward replay with the measured targets removed from the selector set.
- A candidate that fits one sector must also survive cross-sector consistency checks.

## Link Back to SM-Parity Closure

Backfitting can help SM-parity closure if it recovers a compact packet that
passes independent promotion tests.  In particular, it may propose the missing
`D_E` or `rho_E` operator packet, typed monad maps, section-ring generators,
period selector, or selected representation table required by:

```text
MTT_Qa_SU3_Color_Operator_Packet_Source_Gate_v1
```

The recovered packet must then be replayed forward with the measured constants
removed from the selector set.

## Inverse Reconstruction Theorem

Measured constants may be used as boundary data for branch discovery.  A branch
found this way can become a serious candidate only if its fitted knobs compress
to a discrete, algebraic, or corpus-selected packet and survive forward replay
without target values as selectors.

Therefore this artifact opens a legitimate search path toward the selected
SM-packet gate, while preserving the distinction between inverse discovery,
SM-parity closure, and no-knob proof.

## What This Closes

- inverse_reconstruction_program_started
- measured_constants_discovery_policy
- promotion_path_into_SM_parity_gate
- guardrails_against_backfit_as_proof

## What Remains Open

- actual_numeric_inverse_fit_run
- superset_branch_search_space_implementation
- candidate_knob_compression_test
- corpus_alignment_score
- forward_replay_without_targets
- selected_Qa_SU3_color_operator_packet

## Next Artifact

```text
MTT_Inverse_Superset_Search_Spec_v1
```
