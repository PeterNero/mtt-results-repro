# Selected HYM Newton/Galerkin or Adjoint Functor Import v1

## Result

The value-solve gate advances one level.

The rank-2 versus rank-3 mismatch is no longer a conceptual blocker: because
`det(V_alpha)=L tensor L^-1` is trivial, the canonical adjoint carrier

```text
End_0(V_alpha)
```

has rank 3. A selected HYM connection `A` induces `ad(A)`, with curvature
`F_ad(A)=ad(F_A)`. This adds no continuous parameter.

## First Coefficient Solve

The first coefficient solve is attempted in the adjoint Galerkin carrier. The
algebraic `su(2)` adjoint matrices are emitted, and the unknown manifest is now
fixed:

```text
Hermitian metric endomorphism coefficients: 81
connection one-form coefficients:          486
total connection-form solve slots:          567
```

The solve still does not emit selected coefficients. The next true object is
the selected `End_0(V_alpha)` finite basis/differential table, or a proof that
the current 27-mode `B_N` scaffold is that selected finite basis.

## Status

```text
SELECTED_HYM_ADJOINT_TRANSFER_IMPORTED_FIRST_COEFFICIENT_SOLVE_TABLES_OPEN
```

Next:

```text
MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1
```
