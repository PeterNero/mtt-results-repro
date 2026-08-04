# MTT Selected HYM Adjoint-Galerkin First Coefficient Solve v1

## Claim

The first coefficient solve has been attempted honestly.  The algebraic adjoint
carrier is now explicit: `End_0(V_alpha)` has the three real generators
`T1,T2,T3` with `epsilon_ijk` commutator matrices.  This adds no continuous
parameter.

The solve does not close.  The current artifacts still do not contain the
selected local differential tables needed to run Newton/Galerkin.

## Unknown Vector

At the current 27-mode support level:

```text
Hermitian metric endomorphism coefficients: 27 * 3 = 81
connection one-form coefficients:          27 * 3 * 6 = 486
total connection-form solve slots:          567
```

These are solve slots, not fitted parameters.  They must be fixed by the HYM
residual, gauge slice, selected Ext local representative, and selected
Gauduchon metric.

## Missing Tables

The next true object is not another abstract HYM theorem.  It is the selected
finite differential table for `End_0(V_alpha)`:

- selected `End_0(V_alpha)` basis, or proof that the 27-mode `B_N` scaffold is
  that basis;
- `d`, `barpartial`, wedge/product, Hodge/Lambda, quadrature, and gauge
  projector tables;
- local-form representative of the selected Ext class.

The 8-slot Cech cohomology vector is not a connection coefficient vector; it can
seed the solve only after it is represented by local forms.

## Next Artifact

`MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1`.
