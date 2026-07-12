# MTT Inverse Qa/SU3 First Search Run v1

## Purpose

This artifact executes the first inverse superset ranking run for the current
SM-parity blocker: the finite-topology and Qa/SU3 color/operator packet gate.

The run uses structural targets only.  It does not use measured masses, CKM,
PMNS, gauge couplings, or other measured constants.  Its target-fitting role is
therefore discovery-only structural ranking, not no-knob proof.

## Source Inputs

- `full_corpus_dependency_audit`: C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\full_corpus_dependency_audit.candidate.json (present)
- `period_gate`: C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\ctwist_period_normalization_or_a01_exit.candidate.json (present)
- `a01_de_operator_exit_gate`: C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\a01_de_operator_exit_gate.candidate.json (present)
- `cech_dolbeault_scaffold`: C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\cech_dolbeault_matrix_packet_scaffold.candidate.json (present)
- `selected_multiplication_or_de_gate`: C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\selected_multiplication_constants_or_de_source_gate.candidate.json (present)

## Run Configuration

- Run id: `qa_su3_first`
- Domains: `finite_topology_packet`, `qa_su3_operator_packet`
- Allowed targets used: `representation_count`, `hypercharge_pattern`, `anomaly_zero_pattern`, `color_embedding`, `operator_rank_pattern`
- Forbidden targets used: []
- Measured constants used: `False`
- Target-fitting role: `DISCOVERY_ONLY_STRUCTURAL_RANKING`

## Ranked Candidates

### 1. finite_cech_dolbeault_cochain_packet

- Label: Build the 11-space finite Cech/Dolbeault cochain packet.
- Type: `PRIMARY_MATRIX_CONSTRUCTION_TARGET`
- Scores: `{'target_support': 3, 'compression': 3, 'corpus_alignment': 3, 'cross_sector_consistency': 2, 'forward_replay_readiness': 1, 'total': 12}`
- Promotion gates: `G0_inverse_candidate=True`, `G1_compression=True`, `G2_source_alignment=True`, `G3_cross_sector=True`, `G4_forward_replay=False`
- Rejection reason: `none`
- Evidence:
  - Cech/Dolbeault scaffold indexes 11 spaces and five typed product blocks.
  - All five products target P by charge.
  - Selected multiplication gate names this route as a primary matrix construction target.
- Missing for promotion:
  - Selected section/cochain bases for F1..F5, G1..G5, P.
  - Selected product tables or mu_i.
  - Selected f,g entries and gf=0 verification from selected values.
  - Freed-Witten/Green-Schwarz/Bianchi and projector checks.
- Promoted to forward packet: `False`

### 2. same_source_DE_dotD_or_rhoE_response

- Label: Build same-source D_E, dotD, or rho_E response data.
- Type: `PRIMARY_OPERATOR_PROMOTION_ROUTE`
- Scores: `{'target_support': 3, 'compression': 2, 'corpus_alignment': 3, 'cross_sector_consistency': 2, 'forward_replay_readiness': 1, 'total': 11}`
- Promotion gates: `G0_inverse_candidate=True`, `G1_compression=True`, `G2_source_alignment=True`, `G3_cross_sector=True`, `G4_forward_replay=False`
- Rejection reason: `none`
- Evidence:
  - A01/D_E gate requires selected D_E/rho_E or equivalent operator packet.
  - Selected multiplication gate names same-source D_E/dotD response as a primary operator route.
  - Validator shapes exist but selected operator values are still absent.
- Missing for promotion:
  - Selected non-identity D_E/dotD/rho_E matrix.
  - Spectral, heat, Riesz, torsion, or finite-part operator exit.
  - Same-source typed matrices tying operator output to f,g/product packet.
- Promoted to forward packet: `False`

### 3. a01_de_operator_exit_acceptance_gate

- Label: Use the existing A01/D_E operator exit gate as the acceptance test.
- Type: `ACCEPTANCE_GATE_NOT_SOURCE`
- Scores: `{'target_support': 2, 'compression': 1, 'corpus_alignment': 3, 'cross_sector_consistency': 2, 'forward_replay_readiness': 1, 'total': 9}`
- Promotion gates: `G0_inverse_candidate=True`, `G1_compression=False`, `G2_source_alignment=True`, `G3_cross_sector=True`, `G4_forward_replay=False`
- Rejection reason: `none`
- Evidence:
  - Gate is already built and lists required inputs.
  - It rejects identity rho_E, generic f,g existence, q79 import, and measured residuals.
- Missing for promotion:
  - This is not itself a source packet.
  - Needs selected matrices before it can promote anything.
- Promoted to forward packet: `False`

### 4. fixed_gerbe_Bfield_or_period_selector

- Label: Find a fixed same-branch gerbe/B-field representative or finite central quotient.
- Type: `ALTERNATE_PERIOD_SELECTOR_ROUTE`
- Scores: `{'target_support': 2, 'compression': 2, 'corpus_alignment': 2, 'cross_sector_consistency': 1, 'forward_replay_readiness': 0, 'total': 7}`
- Promotion gates: `G0_inverse_candidate=True`, `G1_compression=True`, `G2_source_alignment=True`, `G3_cross_sector=False`, `G4_forward_replay=False`
- Rejection reason: `none`
- Evidence:
  - Period gate derives the scalar A=1 condition.
  - Full corpus audit says same-branch period selector or finite quotient remains open.
  - This route could remove the need for arbitrary period normalization.
- Missing for promotion:
  - Same-branch selector for R^4/alpha_prime or finite central quotient.
  - Deligne/B-field representative tied to Qa/SU3 packet.
  - Mapped Bianchi/Freed-Witten certificate.
- Promoted to forward packet: `False`

### 5. q79_s3_finite_torsion_pattern

- Label: Use q79/S3 finite torsion as an off-branch pattern only.
- Type: `GUARDRAIL_PATTERN_ONLY`
- Scores: `{'target_support': 1, 'compression': 2, 'corpus_alignment': 2, 'cross_sector_consistency': 0, 'forward_replay_readiness': 0, 'total': 5}`
- Promotion gates: `G0_inverse_candidate=False`, `G1_compression=False`, `G2_source_alignment=False`, `G3_cross_sector=False`, `G4_forward_replay=False`
- Rejection reason: `OFF_BRANCH_PATTERN_ONLY`
- Evidence:
  - Period gate records q79/S3 as the strongest finite torsion pattern.
  - Full corpus audit forbids direct q79/S3 import into Qa/SU3.
- Missing for promotion:
  - Not same branch.
  - No pushdown map to Qa/SU3 selected packet.
- Promoted to forward packet: `False`

### 6. pure_convenience_solve_gf_zero

- Label: Choose arbitrary values satisfying Sum_i mu_i a_i b_i = 0.
- Type: `REJECTED_UNDERDETERMINED_NOT_SELECTED`
- Scores: `{'target_support': 2, 'compression': 0, 'corpus_alignment': 0, 'cross_sector_consistency': 0, 'forward_replay_readiness': 0, 'total': 2}`
- Promotion gates: `G0_inverse_candidate=False`, `G1_compression=False`, `G2_source_alignment=False`, `G3_cross_sector=False`, `G4_forward_replay=False`
- Rejection reason: `TARGET_OR_CONVENIENCE_FIT_ONLY`
- Evidence:
  - The gf=0 equation is easy to satisfy formally.
  - Selected multiplication gate proves this is massively underdetermined before selection.
- Missing for promotion:
  - No selected bases.
  - No selected mu_i.
  - No selected f,g entries.
  - No selected D_E/dotD/rho_E source.
- Promoted to forward packet: `False`


## Decision

Top candidate:

```text
finite_cech_dolbeault_cochain_packet
```

Result: Ranked first-run candidates; no candidate promoted.

Best next move: Construct the finite Cech/Dolbeault cochain packet first, while keeping same-source D_E/dotD/rho_E as the operator acceptance route.

Reason: The cochain route has the strongest compression and source alignment, and it supplies the selected values needed by both gf=0 and the operator exit gate.

## First-Run Theorem

The first inverse Qa/SU3 search run does not promote a selected packet.  It does
rank the live routes and shows that the strongest next construction is the
finite Cech/Dolbeault cochain packet, with same-source D_E/dotD/rho_E retained
as the operator acceptance path.  The pure gf=0 convenience solve and direct
q79/S3 import remain rejected.

## What This Closes

- first_inverse_Qa_SU3_ranking_run
- ranked_candidate_routes
- best_next_construction_route_identified
- convenience_fit_rejected
- off_branch_q79_import_rejected

## What Remains Open

- selected_11_space_finite_cochain_packet
- selected_product_tables_or_mu_i
- selected_f_g_matrix_entries
- same_source_DE_dotD_or_rhoE
- Freed_Witten_GS_Bianchi_and_projector_checks
- forward_replay
- selected_Qa_SU3_color_operator_packet

## Next Artifact

```text
MTT_Selected_Qa_SU3_Finite_Cochain_Construction_Plan_v1
```
