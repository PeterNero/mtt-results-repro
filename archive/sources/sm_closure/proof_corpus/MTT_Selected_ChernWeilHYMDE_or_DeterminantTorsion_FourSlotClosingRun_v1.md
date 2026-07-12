# MTT Selected ChernWeilHYMDE or DeterminantTorsion FourSlotClosingRun v1

This artifact checks the four remaining operator-source slots after the
stationary `Phi_fin` slot closure.

It closes one more slot:
`selected_HYM_or_RouteC_residual`.

The selected source value is the diagonal rank-two HYM Newton/Galerkin solve on
the q79/F,m=1 `V_alpha` branch:

- metric `H=diag(exp(u), exp(-u))`
- connection `A_HYM=du*T3`
- final residual `8.208178923714022e-13`
- tolerance `1e-12`

This is not a full sector-ready Qa/SU3 operator packet.  It does not close the
same-source Chern-Weil row, transition `rho_E`/Cech-Dolbeault `D_E`, determinant
/ heat / torsion response, or dynamic `Phi_fin^C1`.

Current count is now five closed operator-source slots and three open slots.

Next artifact: `MTT_Selected_ChernWeilDE_or_DeterminantTorsion_ThreeSlotClosingRun_v1`.
