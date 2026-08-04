# MTT Selected Neutral Common-Circle Factorization and Holonomy Scalar Reduction v1

## Selected operator

The selected source-level common-circle operator is

```text
H_cen = diag(1,zeta_3,zeta_3^2).
```

It is unitary, has order three, trace zero and determinant one. For the
proto-spinor co-aligned neutral sector, the residual common nil holonomy is a
central phase, hence

```text
H_nu(phi_nu)=exp(i phi_nu) H_cen.
```

Its real eigenvalue channel is exactly

```text
cos(phi_nu+2*pi*k/3), k=0,1,2,
```

which derives the corpus three-basin formula from the selected finite operator.
Moreover `det H_nu=exp(3 i phi_nu)`, so the complete shape uncertainty is the
single scalar `phi_nu=(arg det H_nu)/3 mod 2*pi/3`.

## Boundary

The current source emits `H_cen` only at source level. It does not emit the
operator-level neutral response `H_nu`, its determinant, or the anchored
Hessian scale `mu_nu`. Setting `phi_nu=0` would silently identify two differently
typed objects and is not allowed.

Next artifact: `MTT_Selected_NeutralCentralHolonomyValueAndAnchoredHessianScale_v1`.
