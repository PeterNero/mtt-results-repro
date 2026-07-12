## Selected Strominger Minimizer and Finite Phi_fin Trace

Target paper: `C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md`

Status: `APPENDIX_DRAFT_PROOF_SLOT_OPEN`

Proof label: **Theorem slot I1**

Purpose: convert a current selected-source caveat into an explicit theorem slot. This section does not promote any lifted diagnostic flag.

Statement to add:

> For the q79/F,m=1 S3/Green-Schwarz branch selected by the MTT admissibility functional, the Strominger/HYM minimizer has a canonical finite Phi_fin trace whose residual, rho_E, metric, connection, D_E, Riesz/Green, dotD, and C1 primitive payloads are the Route-C finite packets.

Current blockers closed if and only if the statement is proved:
- `route_c_residual.selected_source_verified`
- `selected_minimizer_identifier`
- `Phi_fin_selected_values`

Proof obligations:
- Define the exact selection functional on the q79/F,m=1 S3/GS sector.
- Prove existence/uniqueness or canonical equivalence class of the selected minimizer.
- Define Phi_fin as a functorial Galerkin/Cech trace, not a fitted projection.
- Prove Phi_fin preserves branch orientation, torsion m=1, S3 class, and GS cancellation.
- Emit selected values or a reproducible algorithm with error/gap certificate.

Dependencies inside the selected-source appendix chain:
None. This section is a root policy/source-selection section.

Executable or corpus artifacts to cite while proving this section:
- `candidate_data/finite_emission_morphism_phifin.candidate.json`
- `candidate_data/routec_selected_source_origin_lemma.candidate.json`

Safe wording before proof:

> Until this theorem is proved, Route-C packets are admissible numerical/support data, not selected-source proof data.

Required guardrail sentence:

> No observed masses, mixings, thresholds, or fitted constants are used to select the source, branch, cover, operator, or promotion flag in this section.

Cross-repo consistency note:
- `mtt-q79-proof-repro`: Algebraic validator success under lifted flags is a diagnostic, not selected-source proof. Evidence: Iwasawa Route-C branch smoke attempt reports Route-C, D_E, and Riesz/Green failing only because selected_source_verified is false.
- `mtt-nonsm-constants-no-knob`: The same theorem-derived flag policy must govern constants outside the SM packet as well. Evidence: Finite selected-connection source attempts reject packets whose downstream algebra works only after selected flags are lifted.
