# GR TT Stiffness Modal Gap Interface v1

## Result

The GR TT response stiffness is computable in canonical internal action units:

```text
kappa_STF,int = Vol_int / (32*pi)
```

for the selected internal-volume rows imported from the non-SM normalization
program.

This is not yet the selected GR modal gap. The modal gap `lambda_*` is the
lowest positive spectral value of a selected `A_int` complement after the
correct quotient, projector, and spectral window have been applied.

## Computed Internal Rows

The verifier computes:

```text
N=64:  kappa_STF,int = 0.04618016151525098
N=79:  kappa_STF,int = 0.04973134686087317
N=448: kappa_STF,int = 0.08212905373241541
```

All are positive, so the internal TT response block remains stable in the
closed internal convention.

## Boundary

The gap candidates remain separate:

```text
Theta nil floor benchmark: lambda_* = 0.25
Z64 exact central-circle branch: lambda_* = 15
```

Neither number may replace the GR TT modal gap until the selected GR `A_int`
operator is identified with the corresponding branch. Likewise,
`kappa_STF,int` may not be renamed `lambda_*` without an interface theorem.

## Next Gate

The next required theorem is:

```text
GR_TT_Response_to_Aint_Spectral_Interface_Theorem
```

It must specify the TT closure-strain domain, quotient/projector/window, inner
product, and lowest positive eigenvalue in the same normalization as the branch
gap table.
