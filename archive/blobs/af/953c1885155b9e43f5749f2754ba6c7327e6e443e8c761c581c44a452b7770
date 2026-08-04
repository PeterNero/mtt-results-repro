# NonSplitRouteC and MinimalHselGret Import v1

Status: `NONSPLIT_ROUTEC_AND_MINIMAL_HSEL_GRET_IMPORTED_PROMOTION_OPEN`.

The visible side has been reduced to two live same-source lanes.  The primary
fill lane is the non-split rank-two `V_alpha` packet; the parallel repair lane
is Route-C finite HYM/Strominger.  Both lanes now share the same blocker:
`SameSourceSymmetryBreakingSource.v1`.

The QA/SU3 side has a concrete finite Galerkin candidate:

```text
H_sel = [[26, -3, 0], [-3, 10, 0], [0, 0, 8]]
det(H_sel) = 2008
G_ret = [['10/251', '3/251', 0], ['3/251', '26/251', 0], [0, 0, '1/8']]
selected covector = [0, 0, 1]
tau = {'F1': 1, 'F2': -1, 'F3': 0, 'F4': -1, 'F5': 1, 'G1': -1, 'G2': 1, 'G3': 0, 'G4': 1, 'G5': -1, 'P': 0}
```

This closes the finite algebraic `H_sel/G_ret/tau` layer only.  Smooth
same-source operator promotion, selected `D_E/dotD/Riesz/Green`, primitive C1
overlaps, `A_selected`, `b_selected`, Yukawas, and full SM closure remain open.

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `MTT_SameSource_SymmetryBreaking_Source_v1`.
Parallel QA/SU3 artifact: `Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1`.
