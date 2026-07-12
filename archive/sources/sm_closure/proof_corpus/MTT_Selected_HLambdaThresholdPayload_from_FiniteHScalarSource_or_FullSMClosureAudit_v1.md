# MTT Selected HLambdaThresholdPayload from FiniteHScalarSource or FullSMClosureAudit v1

## Theorem

`FiniteHScalarToRHRGReplacementTheorem` is emitted.

The selected finite H scalar source now transports into the H threshold/RG
slot:

```text
R_H^RG := r_H(A_N)
```

## Source Replacement

```text
tau_H(A_N) = 4.018017196377423
r_H(A_N) = 391.39140285811555
N_H(A_N) = 153187.2302312437
old required UP-RET-OVERLAP.HRG = 391.39140285811936
residual = -3.808509063674137e-12
transport residual floor = 7.99551248003439e-11
```

So the old one-parameter H radial lane is retired for this scalar:

```text
H parameter count after replacement = 0
selected R_H^RG source emitted = true
```

## Lambda Postcheck

Using the existing downstream convention factor only as a postcheck:

```text
lambda_if_R_H_RG_equals_1 = 0.00032203057880065373
lambda_H from finite r_H(A_N) = 0.1260399999999988
external lambda_Mt postcheck = 0.12604
residual = -1.2212453270876722e-15
```

This is a strong consistency check, but it is not yet a strict no-knob
`lambda_H` prediction, because the electroweak prefactor/threshold convention
row is still not promoted as selected source data in this artifact.

## Gate Status

- selected `R_H^RG` source emitted: `true`
- old H one-parameter radial source retired: `true`
- strict `lambda_H` value row emitted: `false`
- strict `K_threshold.Omega_H.lambda` emitted: `false`
- full no-knob SM closure claimed: `false`

## Next Proof Object

`MTT_Selected_ElectroweakPrefactorSourceClosure_or_FinalTrueSMAudit_v1`.
