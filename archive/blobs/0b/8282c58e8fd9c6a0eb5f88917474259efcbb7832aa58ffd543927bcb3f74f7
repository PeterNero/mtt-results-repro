# Selected Qa/SU3 Spectral Fallback Reduction

## Claim

The next Qa/SU3 gate has been reduced from a broad "construct the spectral
fallback" instruction to a narrower selected-source solve.

The already certified q79 data imply:

```text
terminal monad arithmetic closed
non-invariant spectral fallback input contract closed
finite Galerkin execution protocol closed
rho_E / metric / sector finite algebra passes honestly
```

The remaining failure is not the finite validator pipeline.  In the honest
current q79 branch, the validator exits are:

```text
rhoE_mesh       PASS
rhoE_metric     PASS
sector_maps     PASS
route_c_residual FAIL
D_E action       FAIL
Riesz/gap        FAIL
reduced Green    FAIL
dotD response    FAIL
```

The failed validators fail because `selected_source_verified` or
`selected_dotD_source_verified` is not justified.  When q79 runs the same
finite packet with lifted smoke flags, all finite validators pass, but that is
only a smoke test.  It proves that the algebraic validator pipeline is
available, not that the selected source has been constructed.

## What This Closes

The broad spectral fallback has become an executable source problem:

1. construct a selected same-branch `D_E` source by typed monad/Cech data,
   corrected non-invariant Dolbeault data, or a direct selected
   HYM/Strominger solve;
2. justify the selected-source flags without lifted smoke assumptions;
3. rerun the existing finite validators for `D_E`, Riesz/gap, reduced Green,
   `dotD_alpha1`, and sector maps.

This means the finite matrix side is ready to receive real source data.  The
current blocker is the origin of the operator, not the shape of the validator.

## What Is Still Open

The following are still open:

```text
selected D_E source
actual non-invariant basis values B_N
operator/stiffness matrices
low eigenpairs and Psi_i representatives
selected dotD_alpha1 values
primitive overlap or C1 contractions
full SM closure
```

## Guardrail

The lifted Route C smoke files are not a proof source.  They are a consistency
test showing that, if a genuine selected source supplies the missing flags, the
existing finite validator chain has the right form.

The next object is:

```text
Selected_Qa_SU3_RouteC_Source_Solve_or_Typed_Operator_v1
```

It must justify `selected_source_verified` and
`selected_dotD_source_verified` from a genuine same-branch source, then rerun
the existing q79 validators without lifted smoke flags.
