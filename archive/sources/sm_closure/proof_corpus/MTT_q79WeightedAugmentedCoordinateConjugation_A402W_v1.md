# MTT q79 Weighted Augmented Coordinate Conjugation (A402W) v1

For the selected exact n3 transport, write the augmented state as
`u=(nu,I)` with five lift coordinates and eight integrated-residue coordinates.
The Taylor system has block-triangular form

`u' = M u + f`, with `M = [[A,0],[R,0]]`.

A402W uses the constant invertible coordinate map

`S = diag(I_5, 0.1 I_8)`, `z = S u`.

Therefore the executed weighted system is exactly

`z' = (S M S^-1) z + S f`,

and its physical endpoint is recovered by `u=S^-1 z`. The value `0.1` is a
validator preconditioner, not selected geometry, source data, or a physical free
parameter. Any positive scale gives an equivalent ODE; this value keeps the lift
and output error coordinates numerically comparable.

The dedicated audit independently reconstructs the Taylor matrix and forcing,
checks coefficientwise interval overlap after conjugation and inverse conjugation,
checks the two zero feedback blocks, and compares ordinary and weighted certified
one-step endpoints. The maximum endpoint-center difference is
`1.58798e-110`, and every physical component interval overlaps.

This closes the weighted-coordinate equivalence used by A402. It does not by
itself close the full contour execution, relative-chain theorem, interval-Newton
self-map, covariant zero, or Standard Model closure.
