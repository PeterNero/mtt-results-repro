# Closure-Strain STF Tensor Decomposition v1

## Result

The corrected route has a clean algebraic backbone:

`closure/bookkeeping strain -> STF tensor sector -> TT plus/cross`

Represent local closure strain as a `3 x 3` tensor. It decomposes into:

- three antisymmetric gauge/rotation directions
- one scalar radial trace direction
- five symmetric trace-free tensor directions

After imposing transversality for a local propagation covector, the STF tensor
sector reduces to the two standard TT modes:

- plus: `(xx - yy)`
- cross: `(xy + yx)`

## Status

This closes the tensor algebra for the corrected route. It does not yet close
the MTT source theorem, because the selected MTT Hessian on this STF strain
sector is still missing.

The next gate is:

`selected closure-strain Hessian on STF tensor sector`
