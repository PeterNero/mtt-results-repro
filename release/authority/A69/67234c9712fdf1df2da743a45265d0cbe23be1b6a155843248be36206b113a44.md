# MTT Selected Common Quark-Order/Shared-Circle Kinetic Operator or Exact Residual Spectrum v1

## Explicit common operator

On the finite projected A67 carrier define

```text
C_sector = diag(14/3,14/3,14/3,0,-3,0),
W_kin = exp(-tau_int C_sector) Phi_C1^+.
```

This operator is bounded, self-adjoint, strictly positive and gauge commuting. The colored cost has
the conditional corpus factorization `7*(1/2)*C2(3)=14/3`. On a normalized shared circle the
primitive winding has Laplacian cost one, so three charged-lepton basins have direct-sum cost three.
The remaining source assumptions are the Z7-to-color-completion bridge and selection of the dual
inverse-heat sign on the fully anchored charged-lepton lane.

Its exact gauge execution is

```text
K/K2 = [1.9418974820588117, 1.0, 0.3098850582730217].
```

## Scale-transport no-go

Allowing both a common kinetic normalization and ordinary one-loop scale transport gives

```text
g_a^-2 = A K_a + ell b_a/(8 pi^2).
```

The determinant `det[K,b/(8pi^2),g^-2]=-0.0027015691759737131` is nonzero. Therefore no values of
`A` and `ell` reproduce all three accepted couplings. The least-squares residual norm is
`0.01120798752731546`. The discrepancy is not merely a matching-scale choice.

## Exact residual spectrum

Within the proved minimal two-support class, the unique correction is

```text
delta C = delta_q P_colored - delta_e P_e,
delta_q = 0.0005518877514480991,
delta_e = 0.025831271224056707.
```

These values are profile-inferred and are not promoted. The next source theorem must emit this
two-component correction from one selected circle/Lens determinant or replace the rational costs by
one exact same-action spectrum.

Next artifact: `MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1`.
