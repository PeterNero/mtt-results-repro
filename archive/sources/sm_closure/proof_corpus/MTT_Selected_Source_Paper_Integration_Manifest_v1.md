# MTT Selected Source Paper Integration Manifest

Status: `MTT_SELECTED_SOURCE_PAPER_INTEGRATION_MANIFEST_BUILT_INSERTIONS_OPEN`

Every current `not theorem-derived` or `selected_source_verified=false` blocker must become a named paper insertion, not a loose caveat.  This manifest maps those blockers to theorem sections, target papers, proof obligations, and conservative wording.

Global rule: diagnostic lifted flags can prove algebraic consistency only.  Promotion requires a named theorem deriving the selected flags from MTT source data.

## I1_selected_strominger_minimizer_to_phifin_trace

Target papers: strominger_system, flux_selection

Section title: **Selected Strominger Minimizer and Finite Phi_fin Trace**

Theorem slot: For the q79/F,m=1 S3/Green-Schwarz branch selected by the MTT admissibility functional, the Strominger/HYM minimizer has a canonical finite Phi_fin trace whose residual, rho_E, metric, connection, D_E, Riesz/Green, dotD, and C1 primitive payloads are the Route-C finite packets.

Proof obligations:
- Define the exact selection functional on the q79/F,m=1 S3/GS sector.
- Prove existence/uniqueness or canonical equivalence class of the selected minimizer.
- Define Phi_fin as a functorial Galerkin/Cech trace, not a fitted projection.
- Prove Phi_fin preserves branch orientation, torsion m=1, S3 class, and GS cancellation.
- Emit selected values or a reproducible algorithm with error/gap certificate.

Safe wording: Until this theorem is proved, Route-C packets are admissible numerical/support data, not selected-source proof data.


## I2_projective_rhoe_source_promotion

Target papers: strominger_system, flux_selection, theta_nonabelian_overlaps

Section title: **Projective/Twisted rho_E Source Promotion**

Theorem slot: The selected S3 Deligne/Cech class induces the Heisenberg/Weyl projective rho_E packet on the active F3^2 deck shadow, with central phase fixed by the same gerbe/Green-Schwarz data and not by empirical targets.

Proof obligations:
- Construct the gerbe module or twisted Chan-Paton bundle on the selected cover.
- Show the active g1,g2 deck image forces the F3^2 Heisenberg cocycle.
- Prove g3..g6 are in the kernel or quantify their smooth lift action.
- Show the clock/shift packet is canonical up to gauge equivalence.
- Prove compatibility with Freed-Witten and GS data.

Safe wording: The current Heisenberg/Weyl packet is a canonical numerical candidate; source promotion remains open.


## I3_smooth_bn_galerkin_lift_theorem

Target papers: theta_nonabelian_overlaps, theta_execution_flavor, strominger_system

Section title: **Smooth Gerbe-Twisted B_N Galerkin Lift**

Theorem slot: The F3^2 x C3 twisted Fourier scaffold is the first finite level of a convergent smooth non-invariant Galerkin basis B_N for the selected Iwasawa/Strominger branch, with controlled quadrature and truncation error.

Proof obligations:
- Define the smooth nil/Heisenberg theta basis extending the F3^2 Fourier scaffold.
- Prove quotient/deck equivariance for the selected Iwasawa lattice.
- Prove Gram positivity and convergence of quadrature.
- Prove complement gap stability under increasing N.
- Bound truncation error between model active Laplacian and full Iwasawa/Strominger operator.

Safe wording: The 27-mode scaffold gives a verified finite model; it is not yet a full smooth Galerkin convergence theorem.


## I4_selected_DE_action_and_source_flags

Target papers: theta_nonabelian_overlaps, theta_execution_flavor, strominger_system

Section title: **Selected D_E Action, Sector Projectors, and Source Flags**

Theorem slot: The selected Strominger/HYM operator D_E restricts to the emitted smooth B_N basis with sector kernels Q,u,d,L,e,N,H, and the selected_source_verified flags are theorem consequences of the minimizer and Phi_fin trace.

Proof obligations:
- Derive D_E from the selected connection, not from a model-active substitute.
- Prove the 27-mode matrix is the N=1 truncation of the selected D_E.
- Construct sector projectors in the same basis.
- Prove family kernels have dimension 3 and Higgs kernel dimension 1 for the selected operator.
- Specify exactly when selected_source_verified may be set true.

Safe wording: The current D_E matrix layer is validator-consistent under diagnostic source lift; the honest selected flags remain false.


## I5_dotD_alpha1_and_C1_response

Target papers: theta_execution_flavor, theta_nonabelian_overlaps

Section title: **dotD_alpha1, Riesz/Green Response, and C1 Overlap Tensor**

Theorem slot: The alpha1 deformation differentiates the selected D_E within the same branch and same B_N basis, producing horizontal responses, Riesz/Green inverses, and finite C1 overlap tensors used for the Route-C response.

Proof obligations:
- Define alpha1 as a same-branch deformation of the selected source.
- Compute dotD_alpha1 matrices in the emitted B_N basis.
- Prove horizontal gauge and reduced Green equations.
- Emit primitive C1 overlap contractions and Hessian/source blocks.
- Prove no benchmark masses, CKM/PMNS, or observed constants enter selection.

Safe wording: dotD and C1 response should not be promoted until alpha1_driver_verified and selected_dotD_source_verified are theorem-derived.


## I6_parameter_policy_appendix_update

Target papers: parameters_falsifiability, theta_superset

Section title: **Diagnostic Lifts, Superset Repairs, and Theorem-Derived Flags**

Theorem slot: A candidate may pass diagnostic lifted-flag validators only as algebraic consistency evidence; proof promotion requires an explicitly cited theorem that derives the selected flags from MTT source data.

Proof obligations:
- Define diagnostic lift, superset convergence, superset repair, and straight proof.
- State which flags require theorem derivation.
- Require every promoted flag to cite a named theorem and reproducible artifact.
- Forbid observed constants as source selectors.
- Add falsifier templates for selected-source promotion failures.

Safe wording: Diagnostic success is not proof; it identifies exactly which theorem insertion is missing.

