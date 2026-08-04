# GR TT Aint Interface Conversion Requirements v1

## Result

If the selected GR TT spectral complement is a scalar rescaling of the TT
response block, then

```text
lambda_GR,TT = c_interface * kappa_STF,int
```

The verifier computes the required `c_interface` values for the two live
candidate gap numbers. This is a diagnostic, not a proof that the scalar
interface ansatz is true.

## Required Conversion Factors

To hit the nil-floor benchmark `lambda_* = 0.25`, the required conversion factor
is order `3` to `6` across the tested internal rows.

To hit the exact Z64 branch `lambda_* = 15`, the required conversion factor is
order `180` to `325` across the tested internal rows.

So the next bridge cannot be hand-waved. It must derive the selected row and the
operator normalization that converts response stiffness into an `A_int` spectral
gap.

## Next Artifact

The next required artifact is:

```text
Selected_GR_TT_Aint_Interface_Data
```

It must provide the selected `N` or internal volume row, the operator relation
between `A_GR,TT` and `H_TT`, the derived conversion factor, and the lowest
positive eigenvalue after quotienting zero modes.
