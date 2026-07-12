## Selected D_E Action, Sector Projectors, and Source Flags

Target paper: `C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps.md`

Status: `APPENDIX_DRAFT_PROOF_SLOT_OPEN`

Proof label: **Theorem slot I4**

Purpose: convert a current selected-source caveat into an explicit theorem slot. This section does not promote any lifted diagnostic flag.

Statement to add:

> The selected Strominger/HYM operator D_E restricts to the emitted smooth B_N basis with sector kernels Q,u,d,L,e,N,H, and the selected_source_verified flags are theorem consequences of the minimizer and Phi_fin trace.

Current blockers closed if and only if the statement is proved:
- `operator_slots[*].selected_source_verified`
- `selected_D_E_source_promotion`
- `sector_projectors`
- `R3_full_selected_operator_spectral_data`

Proof obligations:
- Derive D_E from the selected connection, not from a model-active substitute.
- Prove the 27-mode matrix is the N=1 truncation of the selected D_E.
- Construct sector projectors in the same basis.
- Prove family kernels have dimension 3 and Higgs kernel dimension 1 for the selected operator.
- Specify exactly when selected_source_verified may be set true.

Dependencies inside the selected-source appendix chain:
- `I1_selected_strominger_minimizer_to_phifin_trace`
- `I3_smooth_bn_galerkin_lift_theorem`

Executable or corpus artifacts to cite while proving this section:
- `candidate_data/selected_routec_de_action_on_smooth_bn.candidate.json`

Safe wording before proof:

> The current D_E matrix layer is validator-consistent under diagnostic source lift; the honest selected flags remain false.

Required guardrail sentence:

> No observed masses, mixings, thresholds, or fitted constants are used to select the source, branch, cover, operator, or promotion flag in this section.

Cross-repo consistency note:
- `mtt-q79-proof-repro`: Algebraic validator success under lifted flags is a diagnostic, not selected-source proof. Evidence: Iwasawa Route-C branch smoke attempt reports Route-C, D_E, and Riesz/Green failing only because selected_source_verified is false.
- `mtt-nonsm-constants-no-knob`: The same theorem-derived flag policy must govern constants outside the SM packet as well. Evidence: Finite selected-connection source attempts reject packets whose downstream algebra works only after selected flags are lifted.
