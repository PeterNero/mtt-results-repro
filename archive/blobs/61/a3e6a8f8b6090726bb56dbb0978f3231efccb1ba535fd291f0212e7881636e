# MTT Selected FHuvRestrictionMatrixRows or BSelectedProjectionExecution v1

Status: `MTT_SELECTED_FHUVRESTRICTIONMATRIXROWS_OR_BSELECTEDPROJECTIONEXECUTION_C1_PAYLOAD_IMPORTED_PROJECTION_TENSOR_OPEN`

## Theorem

The strict dynamic C1 ledger now supplies the promoted compressed Hessian/source
payload:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
```

This removes the old `b_selected` source-promotion blocker for the Huv frontier.
It does **not** yet emit `F_Huv` rows, because `A^T A` is a compressed C1
normal matrix, while the Huv theorem requires:

```text
M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv
```

The missing object is now sharply identified as either:

- the source-owned C1 variation-coordinate map for the selected `B_Huv` columns,
  or
- the ambient 27x27 selected `Hess(F_C1)` matrix entries.

The forbidden naive promotion `A^T A -> M_Huv` was tested and rejected: it gives
scalar `12 I_2`, trace-free norm `0.0`, and no non-diagonal
`Omega` row.

Accepted `F_Huv` rows: `0`.
Selected `s_beta` retained as projection support: `0.004701083905943647`.

Next artifact: `MTT_Selected_C1ToBHuvProjectionTensor_or_FHuvRows_v1`
