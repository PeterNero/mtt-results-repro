# MTT Selected PrimitiveC1Tensor HessianSourceMap or HonestGalerkinC1Execution v1

Status: `MTT_SELECTED_PRIMITIVEC1TENSOR_HESSIANSOURCEMAP_OR_HONESTGALERKINC1EXECUTION_BUILT_SOURCE_MAP_CANDIDATE_VALUES_OPEN`.

The missing source map is now explicit.  The candidate is:

```text
Z/clock phase leg -> R_Z residual/Hessian source
X/shift active leg -> R_X residual/Hessian source
shared support     -> canonical Q_residual, rank 6
```

The residual shapes are already exact:

```text
||R_Z||^2 = 4.0
||R_X||^2 = 2.0
rank target = 2
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

But this remains a candidate, not a selected value packet.  The selected-source
bit is still false for both residual operators, and `b_selected` is not emitted.

The next theorem must either select this source map from MTT geometry or run an
honest selected Galerkin C1 execution in the same 72-real coordinate system.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1`.
