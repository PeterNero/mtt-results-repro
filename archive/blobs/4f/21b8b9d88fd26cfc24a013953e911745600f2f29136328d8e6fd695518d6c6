# MTT Selected dotD alpha1 Transport-Derivative Probe v1

Status: `MTT_SELECTED_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_NORMALIZATION_OPEN`.

## Result

The missing transport derivative is now algebraically fixed.  For

```text
psi_sel = U psi_model
U = exp(-u ad(T3))
h = du/dalpha
```

we have

```text
dU/dalpha = -h ad(T3) U
delta psi = -h ad(T3) psi_sel
dotD_h = dh ad(T3)
D_sel(delta psi) + dotD_h psi_sel = 0
```

So the transported dotD source formula is closed.  The existing finite dotD
matrices also pass the validator when both selected flags are supplied by
theorem:

```text
full-flag probe exit code = 0
```

## Boundary

The alpha1 driver is still not promoted.  The selected Ext-density tangent is
nontrivial and has residual

```text
6.751979459438445e-13
```

but the repo still needs one same-branch source-strength normalization theorem
to identify this tangent with the physical alpha1 derivative.  Until that is
proved, the honest dotD validator cannot be marked fully closed.

No observed constants, benchmark targets, or lifted selected flags are used.

Next artifact: `MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1`.
