# MTT q79 Height-Four Complex PGL(3) Completion (A215) v1

The previous Jacobians varied eight real `sl3` generators.  The selected
alignment is complex, so the holomorphic tangent of `PGL(3,C)` contains those
eight generators and their `i` multiples: sixteen real directions in total.

At the A212 rank-3 center, the complex 8-by-8 Jacobian has rank
`8`, condition number `51.5544`,
and determinant magnitude `2.35709e+09`.  Its realification
has rank `16`.

The complex Newton step has maximum coefficient `0.000564417` and
reduces the linearized residual from `0.00590215820625` to
`3.301e-18`.

This removes the artificial real-subgroup residual floor.  It is a linearized,
floating result.  An independent `iG` finite-difference probe, nonlinear
execution, chamber-aware continuation, and interval certification remain
required before claiming a covariant zero.
