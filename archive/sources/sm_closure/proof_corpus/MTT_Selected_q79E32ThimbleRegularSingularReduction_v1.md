# MTT Selected q79 E32 Thimble Regular-Singular Reduction v1

## Exact local theorem

A135 checks the exact interval-certified Picard-Lefschetz matrix `T` for each
of the `71` thimbles in the A134 weighted chain. In every case,

```text
N = T - I,       rank(N) = 1,       N^2 = 0,
T^T J T = J.
```

The primitive generator `v` of `image(N)` also satisfies `N v=0` and
`T v=v`. These are exact integer identities, not floating diagnostics. Since
`N^2=0`, the local monodromy logarithm truncates:

```text
log(T) = N.
```

Thus the compact Gauss-Manin residue is conjugate, up to local loop
orientation, to `+N/(2*pi*i)` or `-N/(2*pi*i)` and is square-zero. The node is
finite, so the affine puncture summand used by the five-period frame is fixed;
extending the residue by zero preserves square-zero nilpotence. The selected
vanishing cycle is in its kernel, so its period is the monodromy-invariant
log-free Frobenius branch.

## Computable recurrence

Write the regular-singular system as

```text
x dY/dx = (R + B_1 x + B_2 x^2 + ...) Y,      R^2=0.
```

For `Y_0 in ker(R)`, every analytic coefficient is uniquely determined by

```text
Y_n = (nI-R)^(-1) sum_(k=1)^n B_k Y_(n-k),
(nI-R)^(-1) = (1/n)(I+R/n).
```

The `E32` endpoint tail is then the ordinary integral of the analytic series
`q_E32(x)Y(x)`. This removes the false fixed-frame blow-up encountered by a
raw matrix-norm Gronwall bound and supplies the correct certificate design:
certified Frobenius seed, majorant tail, then ordinary-point continuation.

## Frontier

A135 closes the singular-structure theorem for all selected thimbles. It does
not yet emit the numerical `B_k`, `Y_0`, and `q_k` balls, so the weighted
71-thimble interval remains open with radius budget
`0.0028396520372426367`.
No observed Standard Model value is used.
