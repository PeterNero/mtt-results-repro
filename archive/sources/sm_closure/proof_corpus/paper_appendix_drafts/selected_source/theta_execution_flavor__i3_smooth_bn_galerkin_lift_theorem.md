## Smooth Gerbe-Twisted B_N Galerkin Lift

Target paper: `C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md`

Status: `APPENDIX_DRAFT_PROOF_SLOT_OPEN`

Proof label: **Theorem slot I3**

Purpose: convert a current selected-source caveat into an explicit theorem slot. This section does not promote any lifted diagnostic flag.

Statement to add:

> The F3^2 x C3 twisted Fourier scaffold is the first finite level of a convergent smooth non-invariant Galerkin basis B_N for the selected Iwasawa/Strominger branch, with controlled quadrature and truncation error.

Current blockers closed if and only if the statement is proved:
- `R4_full_selected_basis_data`
- `selected_deck_or_equivalent_cover`
- `smooth scalar basis functions phi_m`
- `full_iwasawa_truncation_error_certificate`

Proof obligations:
- Define the smooth nil/Heisenberg theta basis extending the F3^2 Fourier scaffold.
- Prove quotient/deck equivariance for the selected Iwasawa lattice.
- Prove Gram positivity and convergence of quadrature.
- Prove complement gap stability under increasing N.
- Bound truncation error between model active Laplacian and full Iwasawa/Strominger operator.

Dependencies inside the selected-source appendix chain:
- `I1_selected_strominger_minimizer_to_phifin_trace`
- `I2_projective_rhoe_source_promotion`

Executable or corpus artifacts to cite while proving this section:
- `candidate_data/selected_routec_smooth_bn_galerkin_lift.candidate.json`

Safe wording before proof:

> The 27-mode scaffold gives a verified finite model; it is not yet a full smooth Galerkin convergence theorem.

Required guardrail sentence:

> No observed masses, mixings, thresholds, or fitted constants are used to select the source, branch, cover, operator, or promotion flag in this section.

Cross-repo consistency note:
- `mtt-q79-proof-repro`: Algebraic validator success under lifted flags is a diagnostic, not selected-source proof. Evidence: Iwasawa Route-C branch smoke attempt reports Route-C, D_E, and Riesz/Green failing only because selected_source_verified is false.
- `mtt-nonsm-constants-no-knob`: The same theorem-derived flag policy must govern constants outside the SM packet as well. Evidence: Finite selected-connection source attempts reject packets whose downstream algebra works only after selected flags are lifted.
