# MTT q79 Height-Four Imaginary Holomorphic Check (A216) v1

The same-source A212 evaluator was executed at `exp(+ihG_1)` and
`exp(-ihG_1)` with `h=1.0e-06`.  Both endpoints remain in the same fixed
handle chamber and the same post-Picard-Lefschetz radial chamber.

The centered imaginary-direction derivative agrees with `i` times the
independently computed real A213 derivative to relative error
`0.000325737`.  Its signed midpoint replay error is
`1.26085e-08` in maximum norm.

This is an independent numerical check of the holomorphic tangent rule used
by A215.  It checks one of eight complex generators and is not an interval
proof of holomorphicity or a proof of a covariant zero.
