# MTT Selected HYM Projector SourcePromotion Route A v1

Status: `MTT_SELECTED_HYM_PROJECTOR_SOURCE_PROMOTION_ROUTE_A_REDUCED_TO_PHIFIN_TRACE`.

## Route A Question

Can the clean model-active `B_N` projector packet be promoted to the selected
HYM/Strominger projector packet?

Current answer: not yet.

## What Route A Closes

The finite side is closed:

```text
ambient dimension = 27
basis = F3xF3_gerbe_twisted_fourier_N1_rank3
zero cluster = ['phi_(0,0)_e0', 'phi_(0,0)_e1', 'phi_(0,0)_e2']
gap = 4.386490844928603
projector checks pass = True
End0 equivariance passes = True
```

So the obstruction is not rank, basis, gap, or equivariance.

## What Blocks Promotion

The selected-source side is still open:

```text
selected_source_verified = False
selected_dotD_source_verified = False
alpha1_driver_verified = False
Phi_fin selected payload closed = False
```

Therefore Route A reduces to the selected `Phi_fin` trace/equivalence theorem:
prove that the selected q79/F,m=1 S3/GS HYM/Strominger minimizer has the emitted
smooth `B_N` model-active packet as its finite Galerkin trace, including
`D_E`, Riesz/Green, projectors, `dotD_alpha1`, and gap/error contracts.

## Superset Use

This uses the superset correctly:

- `End0` plus `B_N` closes the finite value side,
- HYM/Strominger supplies the selected minimizer,
- `Phi_fin` must bridge the selected minimizer to finite values,
- q79/S3/GS/Theta/SU5 data constrain the branch and later routing but do not
  flip source flags.

No measured constants, benchmark matrices, residual target fitting, or lifted
flags are used as proof.

Next artifact: `MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1`.
