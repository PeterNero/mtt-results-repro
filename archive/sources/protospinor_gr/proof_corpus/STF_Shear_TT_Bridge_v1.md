# STF Shear TT Bridge v1

## Result

The ordinary linear algebra bridge is closed.

For a spatial symmetric perturbation basis

`h_xx, h_yy, h_zz, h_xy, h_xz, h_yz`

and a propagation direction `z`, impose:

- trace-free: `h_xx + h_yy + h_zz = 0`
- transverse: `h_xz = 0`, `h_yz = 0`
- no longitudinal scalar mode in the TT block: `h_zz = 0`

The constraint rank is `4`, so the remaining dimension is:

`6 - 4 = 2`.

A basis is:

- plus: `(1, -1, 0, 0, 0, 0)`
- cross: `(0, 0, 0, 1, 0, 0)`

## Consequence

If MTT independently identifies lens shear with transverse symmetric trace-free
spatial shear, then the projection to `h_TT_plus` and `h_TT_cross` is fixed.

The remaining blocker is no longer the TT math. It is the MTT source
identification:

`lens transport/shear -> STF transverse metric shear`.

