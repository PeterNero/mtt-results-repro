# MTT Selected HScalarFunctionalOnFiniteProjectedHYMAlgebra or HalfDensitySourceRule v1

## Theorem

`HScalarFunctionalOnFiniteProjectedHYMAlgebraTheorem` is emitted.

## Source Functional

Inside the selected finite projected algebra `A_N`, define:

```text
k_H(A_N) =
  25/7
  + sqrt(3)*s_beta
  + (log Tr_N exp_N(-2u_N) - log Tr_N exp_N(2u_N))/8
  - s_beta*(Tr_N exp_N(-u_N) - Tr_N exp_N(u_N))/2
```

All operations are exact finite `A_N` operations: `Tr_N`, `exp_N`,
`star_N`, `Delta_N`, and `Green_N`.

## Value Emission

```text
k_H(A_N) = 3.5795828145988784
tau_H(A_N) = 4.018017196377423
r_H(A_N) = 391.39140285811555
```

Accepted H scalar source rows: `1`.

Strict `tau_H` source promoted: `true`.

Strict `r_H` source promoted: `true`.

## Downstream Comparison Only

The controlled frontier value is used only as a postcheck:

```text
tau_H(controlled frontier) = 4.018017196377461
tau_H(A_N) - tau_H(controlled) = -3.8191672047105385e-14
relative residual = 9.505104179628199e-15
selected replay floor = 8.208178923714022e-13
```

## Boundary

This does not yet close full SM/no-knob closure. The next step is to transport
`r_H(A_N)` into the H/lambda threshold payload:

```text
K_threshold.Omega_H.lambda
lambda_H/quartic threshold payload
ten-row K-threshold closure
```

## Next Proof Object

`MTT_Selected_HLambdaThresholdPayload_from_FiniteHScalarSource_or_FullSMClosureAudit_v1`.
