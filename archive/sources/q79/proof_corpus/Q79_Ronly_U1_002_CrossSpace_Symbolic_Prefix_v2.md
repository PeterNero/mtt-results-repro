# q79 R-only `u1=2` Cross-Space Symbolic Prefix

## Status

`EXACT_U1_002_CROSSSPACE_SEVEN_SYMBOLIC_LINES_CLOSED`

## New result

The exact `u1=2` cover now reaches both independent class-free q79 cores.
The complete accounting is

```text
space 5: u2=1,2,3  -> literal R-only basis [1]
space 5: u2=4      -> nonunit R quotient, closed by D18
space 5: u2=5      -> literal R-only basis [1]
space 6: u2=1,2    -> literal R-only basis [1]
```

Thus seven symbolic lines, representing `700` canonical fixed `F_101` fibers,
are closed at the required R-only or complete R/`y`/D tier.

## First `u1=2` exceptional stratum

The exact space-5 `u2=4` reduced basis has `48` rows rather than `[1]`. Under
the certified bijection

```text
u2 = s*a^(-2),
```

it is the canonical line `(s,a)=(1,50)`. Its basis has three affine pivots
and all `45` quadratic products among nine free coordinates. Hence its exact
quotient is the ten-dimensional algebra with standard basis

```text
1, h4, h5, h6, u3, u4, u5, u6, u7, v.
```

The computed symbolic-`u3` basis uses `t*u3=1`. The diagonal Laurent
isomorphism

```text
t -> 99*v,   v -> 50*t
```

transports it to the canonical relation `v*u3=50`. The inverse transport
reproduces all `48` source rows exactly, and all `10^3=1000` multiplication
associativity checks pass.

The four omitted `y` rows then reconstruct by exact unit pivots. In the
complete quotient, parent terminal `D18` has multiplication determinant

```text
det(m_D18) = 95 mod 101,
```

and the emitted inverse multiplies it to `(1,0,...,0)`. Therefore the full
R/`y`/D line ideal is unit over `F_101` and every field extension. The
nonunit R-only output is not promoted on its own.

The two subsequent exact solves require no terminal repair. Space-5 `u2=5`
is the canonical `(s,a)=(1,9)` line, and space-6 `u2=2` is the canonical
`(s,a)=(2,1)` line. Both return literal complete reduced basis `[1]`.

## Accounting

```text
space-5 symbolic-u2 lines closed at u1=2:      5/100
space-6 symbolic-u2 lines closed at u1=2:      2/100
cross-space lines closed:                       7/200
R-only unit lines:                                  6
D-augmented unit lines:                             1
canonical fixed F_101 fibers closed:              700
remaining unclassified symbolic-u2 lines:         193
new continuous fit parameters:                      0
```

## Boundary

This is exact finite-field and scheme-theoretic progress inside the two open
inverse-root charts. It does not close the other `193` lines at `u1=2`, the
other `98` nonzero `u1` values, either mirror zero-zero chart, or a
characteristic-zero system. It does not promote the obstruction to physical
HYM or quantum-gravity data. The global symbolic chart count remains
`138/140`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_cross_space_symbolic_prefix_v2_audit.py
```
