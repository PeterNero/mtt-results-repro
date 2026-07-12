# MTT Selected CKMSectorPairWeightSourceTheorem or FullFlavorGalerkinRun v1

Status: `MTT_SELECTED_CKMSECTORPAIR_WEIGHT_SOURCE_ATTEMPT_ORBIT_IMPORTED_SCALAR_EVALUATOR_OPEN`.

## Theorem

`CKMSectorPairWeightSourceReductionTheorem` is proved.

The selected pure-Weyl/lambda-orbit/second-order matrix layer is now imported
into the CKM sector-pair weight problem. It supplies:

```text
orbit spectrum          = [1.0, 4.0, 7.0]
commutator norm squared = 324.0
CP-odd invariant        = 972*sqrt(3)
lambda representatives  = ['phase_lambda_1+omega__shift_lambda_1+omega', 'phase_lambda_1+omega2__shift_lambda_1+omega2']
```

This closes the qualitative three-family/CP source domain for the CKM weight
attempt. It does not emit the scalar weights.

## CKM Weight Obligation

```text
W12 = 1.412367346933010
W23 = 6.829844553504131
W13 = 23.108007593901789
```

An invariant extraction scan over the selected orbit constants was executed.
Accepted selected weight rows remain `0/3`.

## Exact Remaining Object

The missing row is no longer a generic coefficient-source issue. It is the
selected scalar evaluator:

```text
E_CKM^ij = Tr_N(Pi_CKM^ij K_CKM(Delta_v, Orbit_lambda, C1/Hessian/zero-mode value rows))
```

This evaluator needs the same value-execution ingredients as the typed
`R_theta` scalar frontier: zero-mode bases, metric/Gram rule, Riesz/Green,
finite Hessian C1 source blocks, rho_E/sector projectors, dotD/deltaTheta, and
primitive C1 sector contractions.

Next artifact: `MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1`.
