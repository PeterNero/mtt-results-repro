# Selected Qa/SU3 m=1 Chern-Weil Operator Source Attempt

## Result

The Chern-Weil/operator-source construction is advanced, but not closed.

Closed or imported as usable:

```text
formal trace-free Chern-Weil row is realizable
no current integrality contradiction is present
standard Chern-character label is 4 alpha_1
split abelian line-pair shortcut is rejected as an HYM source
rank-two non-split V_alpha extension has c1=0 and c2=4 alpha_1 arithmetic
finite H^1(X,L^2) input format is defined
printed c2=0 monad is not the visible alpha_1 source
same-source gap is confirmed by the fusion validator
```

So the visible `Tr_F` row is no longer an algebraic fantasy.  The blocker is
that it has not yet been realized by a selected stable/non-split source that can
feed the operator stack.

## Route Ranking

1. `non_split_rank2_V_alpha_extension`
   Primary live route.  It has the right Chern arithmetic and avoids the split
   HYM no-go.  Its next data are finite: compute `H^1(X,L^2)`, supply a closed
   non-exact extension class, then prove stability/HYM or Route-C residual.

2. `Route_C_or_direct_HYM_selected_solve`
   Best execution engine or fallback source.  The validators exist, but current
   data still fail selected-source and same-branch derivative flags.

3. `printed_three_family_monad`
   Retained as a matter/zero-mode seed, not the visible Chern-Weil source,
   because it has `c2=0` while the visible source needs `c2=4 alpha_1`.

4. `split_abelian_line_pair`
   Useful as an integral target witness, retired as an HYM source because
   individual primitivity fails for positive radii.

## Next Object

```text
Selected_Qa_SU3_M1_Rank2_Ext_H1_Source_Data_v1
```

Preferred first target:

```text
L = (1,-2,0)
L^2 = (2,-4,0)
c2(V_alpha) = 4 alpha_1
```

This object must supply finite Cech/Dolbeault data for `L^2`: bases
`C0,C1,C2`, matrices `d0,d1`, proof that `d1*d0=0`, and a closed non-exact
extension vector.  Until that is supplied, the selected source certificate and
all downstream `D_E/Riesz/Green/dotD/C1` payload entries remain open.
