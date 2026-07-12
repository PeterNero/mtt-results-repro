# MTT Selected ZeroModeHessianPrimitiveRowExecution or PureWeylRows v1

Status: `MTT_SELECTED_ZEROMODEHESSIANPRIMITIVEROWEXECUTION_OR_PUREWEYLROWS_BUILT_IDENTITY_FREE_PURE_WEYL_ROWS_CLOSED_LAMBDA_OPEN`.

The important advance is that pure Weyl rows do **not** need the rejected
identity-subtraction shortcut. The exact primitive execution already emits
direct `R_Z` and `R_X` rows:

```text
R_Z rows = 18
R_X rows = 18
zero-route rows = 36
all 72 exact = true
VSD-01 source assembly closed = true
```

So the unscaled selected pure-Weyl primitive row layer is closed. What remains
open is the scaling/physics layer:

```text
lambda_static representative selected = false
lambda_static * R_Z/R_X rows emitted  = false
selected second-order matrices        = false
higher-response scalar rows executed  = false
true SM equivalence                   = false
full no-knob closure                  = false
```

Next artifact: `MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1`.
