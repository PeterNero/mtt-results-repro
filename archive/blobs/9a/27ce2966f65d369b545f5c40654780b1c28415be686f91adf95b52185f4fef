# MTT Inverse Superset Search Spec v1

## Purpose

This artifact turns inverse reconstruction into an executable search
specification.  It defines the superset search domains, discovery targets,
non-target constraints, scoring terms, rejection rules, and promotion gates.

It still does not run the numeric search.  It closes the specification needed
to run it without confusing backfitting with no-knob proof.

## Search Domains

### finite_topology_packet: selected SM source packet

- Variables:
  - `finite_quotient` (DISCRETE): corpus-supported finite quotients and period selectors
  - `family_index` (INTEGER): index or holonomy values compatible with three families
  - `line_bundle_charge_packet` (INTEGER_VECTOR): topology-only hypercharge/anomaly-compatible charge lattice
  - `representation_table` (FINITE_TABLE): SM candidate reps with source maps
- Discovery targets: `representation_count`, `hypercharge_pattern`, `anomaly_zero_pattern`
- Non-target constraints:
  - `source_map_exists`
  - `three_family_index`
  - `generic_anomaly_formula_matches`
- Promotion output: selected representation/anomaly packet candidate

### qa_su3_operator_packet: color/operator source gate

- Variables:
  - `D_E_or_rho_E` (ALGEBRAIC_OPERATOR): typed operator candidates from Qa/SU3 and non-SM packet repos
  - `typed_monad_maps` (MATRIX_OR_MAP_PACKET): Cech-Dolbeault, monad, or section-ring map candidates
  - `section_ring_generators` (FINITE_GENERATOR_SET): candidate source generators with multiplication rules
  - `Freed_Witten_Bianchi_source` (BOOLEAN_CERTIFICATE): mapped-source consistency certificate
- Discovery targets: `color_embedding`, `operator_rank_pattern`, `selected_representation_support`
- Non-target constraints:
  - `Bianchi_or_Freed_Witten_pass`
  - `same_branch_selector`
  - `typed_maps_compose`
- Promotion output: Qa/SU3 color/operator packet candidate

### theta_gauge_threshold_packet: gauge coupling thresholds

- Variables:
  - `heat_kernel_spectrum` (SPECTRAL_PACKET): finite/zeta/determinant spectra from theta and non-SM work
  - `threshold_packet` (ALGEBRAIC_PACKET): allowed threshold kernels
  - `normalization_index` (RATIONAL_OR_INTEGER): U1/SU2/SU3 embedding normalization candidates
  - `renormalization_scheme_map` (CONVENTION_MAP): declared convention transforms only
- Discovery targets: `alpha_em`, `sin2_theta_w`, `alpha_s`
- Non-target constraints:
  - `same_source_branch_as_sm_packet`
  - `scheme_declared`
  - `thresholds_not_free_per_constant`
- Promotion output: selected gauge threshold packet candidate

### flavor_overlap_packet: Yukawa, CKM, PMNS, CP

- Variables:
  - `overlap_kernel_blocks` (MATRIX_PACKET): theta/string overlap and heavy-link candidates
  - `q79_cp_character` (FINITE_CHARACTER): q79 or compatible finite branch characters
  - `Higgs_carrier_section` (SECTION): Higgs carrier/source candidates
  - `family_basis_map` (UNITARY_OR_INTEGER_MAP): basis maps tied to family index, not CKM targets
- Discovery targets: `mass_ratios`, `CKM`, `PMNS`, `CP_phase`
- Non-target constraints:
  - `same_family_selector`
  - `same_Higgs_carrier`
  - `finite_CP_branch_matches`
- Promotion output: selected flavor overlap packet candidate

### absolute_normalization_packet: dimensionful normalization

- Variables:
  - `modal_gap` (POSITIVE_REAL_OR_ALGEBRAIC): candidate internal gap values
  - `internal_volume` (POSITIVE_REAL_OR_ALGEBRAIC): selected compactification/geometry volume candidates
  - `shared_circle_scale` (POSITIVE_REAL_OR_ALGEBRAIC): shared-circle scale candidates
  - `unit_dictionary_anchor` (CONVENTION_MAP): unit conversion anchors with provenance
- Discovery targets: `G_N`, `Planck_scale`, `absolute_unit_scale`
- Non-target constraints:
  - `compatible_with_GR_response`
  - `compatible_with_nonSM_status`
  - `single_anchor_not_per_constant`
- Promotion output: absolute normalization candidate


## Scoring Terms

### target_residual

- Role: `RANKING_ONLY`
- Definition: Dimensionless residual against measured constants after declared conventions are applied.
- Weight policy: May rank candidates inside inverse search; cannot select final proof object alone.

### complexity_penalty

- Role: `ANTI_OVERFIT`
- Definition: Penalize continuous degrees of freedom, per-target knobs, large arbitrary tables, and unexplained precision.
- Weight policy: High penalty for one knob per measured constant.

### discreteness_bonus

- Role: `PROMOTION_SIGNAL`
- Definition: Reward integer, finite, algebraic, index-theoretic, or section-ring data over continuous free values.
- Weight policy: Required for promotion unless an independent source-selection theorem exists.

### corpus_alignment_score

- Role: `PROMOTION_SIGNAL`
- Definition: Reward explicit support from topology-only, theta, string/flux, q79, Qa/SU3, non-SM, or GR artifacts.
- Weight policy: A numerically good candidate with zero source alignment is rejected.

### cross_sector_consistency

- Role: `REJECTION_AND_RANKING`
- Definition: Require the same branch to support SM packet, color/operator data, thresholds, flavor, and normalization where applicable.
- Weight policy: Hard reject for branch mismatch on promoted candidates.

### forward_replay_score

- Role: `PROMOTION_GATE`
- Definition: Recompute observables from candidate packet with measured constants removed from selector inputs.
- Weight policy: Mandatory before any candidate can enter a forward proof ledger.


## Rejection Rules

- Reject any candidate whose only support is target residual minimization.
- Reject any candidate using separate independent continuous knobs for each measured constant.
- Reject any candidate that changes branch between gauge, flavor, color, and normalization sectors.
- Reject any candidate that uses CKM, PMNS, masses, or couplings to choose the family index or representation packet.
- Reject any candidate with no typed source map for the selected operator or representation data.
- Reject any candidate that cannot be replayed forward without measured constants as selectors.

## Promotion Gates

### G0_inverse_candidate

- Requirement: Candidate found by inverse search and fully labeled as discovery-only.
- Closes: search hit, not proof

### G1_compression

- Requirement: Fitted knobs compress to discrete, algebraic, finite, or independently corpus-selected data.
- Closes: anti-overfit plausibility gate

### G2_source_alignment

- Requirement: Candidate has explicit support in the corpus or adjacent proof repos.
- Closes: corpus legitimacy gate

### G3_cross_sector

- Requirement: Same branch supports the relevant SM packet, Qa/SU3, theta, flavor, and normalization sectors.
- Closes: superset coherence gate

### G4_forward_replay

- Requirement: Measured targets are removed from selectors and observables are recomputed from candidate source data.
- Closes: candidate can enter forward proof obligations


## Required First Run

- Run id: `qa_su3_first`
- Reason: The current forward blocker is the selected Qa/SU3 color/operator packet.
- Domains: `finite_topology_packet`, `qa_su3_operator_packet`
- Targets allowed: `representation_count`, `hypercharge_pattern`, `anomaly_zero_pattern`, `color_embedding`, `operator_rank_pattern`
- Targets forbidden as selectors: `masses`, `CKM`, `PMNS`, `gauge_coupling_values`
- Expected output: ranked candidate packets plus rejection/promotion labels

## Search Spec Theorem

The inverse program is well-posed only if target residuals are demoted to
ranking evidence and promotion requires compression, corpus alignment,
cross-sector consistency, and forward replay.  Under this policy, backfitting
can be used as a disciplined discovery method for the missing selected packet
without claiming no-knob derivation.

The first run should focus on the Qa/SU3 and finite-topology packet because
that is the current forward SM-parity blocker.

## What This Closes

- inverse_search_space
- scoring_policy
- anti_overfit_rejection_rules
- promotion_gates
- first_numeric_run_scope

## What Remains Open

- actual_numeric_inverse_search
- ranked_candidate_packets
- compression_scores
- corpus_alignment_scores
- forward_replay
- selected_Qa_SU3_color_operator_packet

## Next Artifact

```text
MTT_Inverse_Qa_SU3_First_Search_Run_v1
```
