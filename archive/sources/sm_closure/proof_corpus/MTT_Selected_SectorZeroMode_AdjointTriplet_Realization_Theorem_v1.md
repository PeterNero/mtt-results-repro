# MTT Selected Sector Zero-Mode Adjoint-Triplet Realization Theorem v1

Status: `MTT_SELECTED_SECTOR_ZEROMODE_ADJOINT_TRIPLET_THEOREM_PROVED_SOURCE_ACTION_OPEN`.

## Theorem

If a selected matter sector zero-mode carrier `K_s` is real three-dimensional
and carries a selected nonzero irreducible bracket-preserving action

```text
rho_s : End0(V_alpha) -> so(K_s),
```

then `K_s` is orthogonally equivalent to the adjoint triplet
`span(T1,T2,T3)`.  If the selected Higgs zero-mode carrier `K_H` is real
one-dimensional, every `End0(V_alpha)` action on it is trivial, so `H` is the
End0 singlet.

## Proof

`End0(V_alpha)` has the validated `su(2)` bracket table
`[T1,T2]=T3`, `[T2,T3]=T1`, `[T3,T1]=T2`.  The real irreducible
three-dimensional representation of `su(2)` is unique up to orthogonal
equivalence: it is the spin-1 representation, i.e. the adjoint action.  The
model matrices from the previous carrier artifact are skew, rank-two
generators with equal Frobenius norm and they satisfy the same bracket table.

For the Higgs sector, a one-dimensional representation has abelian target
`gl(1,R)`.  Since `su(2)` is perfect, any Lie algebra map
`su(2)->gl(1,R)` vanishes.  Thus the one-dimensional selected Higgs carrier is
forced to be the trivial End0 singlet.

## What This Closes

- The representation-choice freedom is removed once the selected End0 action
  on sector zero modes is supplied.
- The universal rank `19 = 6*3+1` carrier is the unique representation type
  compatible with six selected matter triplets and one selected Higgs singlet.
- This uses the straight End0 path; the superset path only supplies compatible
  rank/projector/SU5-E6 constraints.

## What Remains Open

- selected zero-mode carriers and the source map `rho_s`,
- selected sector Gram normalization,
- selected `Z -> u/e`, `X -> d/nuD`, or replacement matter-slot routing,
- selected `1_M` Dirac-neutrino rule,
- physical `dotD_alpha1` extraction.

No observed constants, benchmark matrices, or target values are used.

Next artifact: `MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1`.
