# MTT Selected StromingerTraceC1FirstVariation or QuadratureExecutionPlan v1

Status: `MTT_SELECTED_STROMINGERTRACE_C1_FIRSTVARIATION_OR_QUADRATURE_EXECUTION_PLAN_BUILT_OPEN`.

This gate converts the previous cutset into executable next steps.

Route A now requires the I11 first-variation certificate:

```text
selected trace map values        = False
first-variation identity         = False
Hessian/coercivity clause        = False
boundary cancellation            = False
normalization compatibility      = False
```

Route B now has a row schedule:

```text
zero-mode basis rows       = 19
primitive contraction rows = 72
hessian source rows        = 2
sector matrix rows         = 36
```

Locked replay target:

```text
A^T A      = [[12.0, 0.0], [0.0, 12.0]]
A^T b      = [12.0, 12.0]
deltaTheta = [1.0, 1.0]
```

Next artifact: `MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1`.
