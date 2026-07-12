# Q79 Selected Alpha1 Tangent or Retarded Overlap Kernel v1

## Result

The analytic retarded/Riesz kernel formula is proved on the locked q79/F,m=1
`B_N` gap layer.  The selected physical source values are still open.

This removes one blocker cleanly: once a selected same-branch `alpha1` tangent
or equivalent retarded-overlap source is supplied, the horizontal response is
not ambiguous.  It is

```text
dotPsi_i = - G Q dotD_alpha1 Psi_i, with P dotPsi_i = 0.
```

## Locked Input

- basis: `F3xF3_gerbe_twisted_fourier_N1_rank3`
- basis dimension: `27`
- selected eta_N: `1.0`
- selected gap lower bound: `2.386490844928603`
- selected Green norm bound: `0.4190252822989217`
- D_E gap/Riesz/Green layer locked: `True`

## Analytic Formulae

```text
P(eps) = (1/(2*pi*i)) int_Gamma (z I - A(eps))^{-1} dz
P'(0) = (1/(2*pi*i)) int_Gamma R0(z) A'(0) R0(z) dz
d/d eps exp(-t A(eps))|0 = - int_0^t exp(-(t-s)A0) A'(0) exp(-s A0) ds
G Q = int_0^infty exp(-t A0) Q dt when A0 has a positive complement gap
dotPsi_i = - G Q dotD_alpha1 Psi_i, with P dotPsi_i=0
```

Sign convention:

```text
The resolvent is R0(z)=(z I - A0)^{-1}; the minus sign in the horizontal response comes from differentiating the zero-mode equation and applying the reduced inverse on P-perp.
```

The exact one-mode check gives all three forms the same response:

```text
L(eps) = [[0, eps*2], [eps*2, 5]]
response = -2/5 = -0.4
```

## Cross-Repo and External Triage

The constants repo says the retarded-overlap lane is classified but sector
charge, transfer normalization, and selected `B_N` tangent remain open.

The SM-parity repo has a selected local Ext-density tangent and Frechet `dotD`
replay in the End0 row model.  It correctly refuses to promote that local
tangent to physical `alpha1` without source normalization or End0-to-sector
routing.

External perturbation theory supplies the Riesz/Duhamel machinery, while the
heterotic/Strominger deformation literature supports the same typed-source
discipline: first-order deformations live in operator/cohomology data, not in
an untyped free scalar.

Triage conclusion:

```text
The analytic retarded/Riesz kernel formula is no longer the blocker. The blocker is the selected physical source-normalization or End0-to-sector routing value fill.
```

## Value-Fill Contract

Before selected `dotD_alpha1` replay can be claimed, the next artifact must
emit:

- same-branch selected alpha1 source-normalization, or selected End0-to-sector routing functor
- normalization value mapping the discrete alpha1 Chern/source row into the tangent direction
- finite B_N operator derivative dotD_alpha1 derived from that source
- proof that the Riesz/Duhamel formula above acts on the same locked q79/F,m=1 basis
- sector-by-sector equality to the existing same-basis dotD_alpha1 value matrices
- honest replay certificate setting selected_dotD_source_verified and alpha1_driver_verified by theorem

Acceptance tests after values exist:

- D_E gap layer remains selected with positive complement gap
- P dotPsi_i=0 horizontal gauge holds
- A dotPsi_i + Q dotD_alpha1 Psi_i = 0 sector by sector
- no diagnostic lifted source flags are used
- no observed masses, CKM angles, thresholds, or benchmark matrices enter

Legal promotion routes:

- Route A: `Identify the discrete alpha1 Chern/source row with the selected infinitesimal Ext-density or equivalent HYM/Strominger tangent.`
- Route B: `Emit a selected End0-to-sector functor and normalization that maps the End0 response to Q,u,d,L,e,N,H sector matrices.`

## What Closes Now

- `analytic_riesz_projection_derivative_formula`: `True`
- `duhamel_retarded_kernel_derivative_formula`: `True`
- `reduced_green_horizontal_response_identity`: `True`
- `conditional_projector_retention_given_selected_tangent`: `True`
- `external_research_and_cross_repo_triage_completed`: `True`
- `selected_tangent_acceptance_contract_written`: `True`
- `target_fitting_excluded`: `True`

## What Remains Open

- `selected_alpha1_source_normalization`: `True`
- `selected_End0_to_sector_routing_values`: `True`
- `selected_alpha1_tangent_parameter_or_kernel_values`: `True`
- `sector_equality_from_selected_derivative_to_dotD_matrices`: `True`
- `honest_dotD_replay_without_lifted_flags`: `True`
- `selected_dotD_source_theorem`: `True`
- `same_branch_alpha1_driver_theorem`: `True`
- `selected_Hess_Xi_finite_blocks`: `True`
- `selected_primitive_C1_contractions`: `True`
- `A_selected`: `True`
- `b_selected`: `True`
- `Yukawa_or_full_SM_closure`: `True`

## Theorem

`Q79AnalyticRetardedRieszKernelFormulaTheorem` is proved as an analytic formula theorem.

On the locked q79/F,m=1 B_N gap layer, any same-branch differentiable selected alpha1 deformation has a unique horizontal first response given by the Riesz/Duhamel reduced Green formula dotPsi_i=-G Q dotD_alpha1 Psi_i.  This proves the analytic retarded-kernel formula and projector-retention criterion conditionally on a selected tangent source.  It does not emit the selected alpha1 tangent, the sector routing normalization, honest dotD replay, C1 response matrices, A_selected, b_selected, Yukawa magnitudes, or full SM closure.

## External References Used

- Perturbation theory for linear operators: https://link.springer.com/book/10.1007/978-3-662-12678-3
- On theoretical and practical aspects of Duhamel's integral: https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-b07432ca-7c06-4303-8967-e42c578b93de
- Algebroids, Heterotic Moduli Spaces and the Strominger System: https://arxiv.org/abs/1402.1532
- Recent Developments in Heterotic Moduli: https://arxiv.org/abs/2409.16524

Next required artifact:
`Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1`.
