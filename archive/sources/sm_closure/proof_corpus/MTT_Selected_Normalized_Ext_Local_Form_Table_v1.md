# MTT Selected Normalized Ext Local Form Table v1

## Claim

The selected Ext row for the direct `End_0(V_alpha)` route is now fixed at the
cohomological local-form level:

```text
eta_00 = Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2
```

It represents the selected Cech/Kunneth basis label
`theta_plus_0_tensor_eta_minus_0` with coefficient `1` in
`H^1(X,L^2)`, where `L^2=(2,-4,0)` and the shared circle degree is zero.

## Straight Path

The straight path is:

```text
selected AH/Ext source -> eta_00 symbolic Dolbeault row -> End_0 local table
```

This is the direct `V_alpha`/`End_0(V_alpha)` route.  It does not pass through
the gerbe-twisted `B_N` scaffold as a proof source.

## Superset Support Path

The reduced q79 Kunneth/Yoneda scalar proof is used only as support for the
basis coefficient.  In that model, the selected vector

```text
[1,0,0,0,0,0,0,0]
```

maps to a nonzero target vector with first coefficient `1`.  This locks the
cohomological scalar of the selected row, but it is not an analytic HYM or
quadrature computation.

## Guardrail

The coefficient `1` is a cohomological normalization in the selected basis.  It
is not a physical `L2` norm, not a Hermitian extension-metric normalization, and
not a computed overlap integral.

## What Remains

The next true gate is the selected `L2` theta quadrature and overlap table for
`eta_00`: theta norms, transition-compatible overlap values, an equivalent
global Dolbeault representative or partition-of-unity table, and the Hodge /
Lambda / gauge-projector data needed by the Newton-Galerkin solve.

## Next Artifact

`MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1`.
