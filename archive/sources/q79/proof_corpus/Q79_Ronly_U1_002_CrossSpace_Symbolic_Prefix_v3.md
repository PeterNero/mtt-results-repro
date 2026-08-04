# q79 R-only `u1=2` Cross-Space Symbolic Prefix, Version 3

## Status

`EXACT_U1_002_CROSSSPACE_NINE_SYMBOLIC_LINES_CLOSED`

## Increment over Version 2

Version 2 closed seven saturated symbolic lines across the two independent
class-free q79 cores. Two further exact msolve computations now give

```text
space 5: u2=6 -> literal reduced R-only basis [1]
space 6: u2=3 -> literal reduced R-only basis [1].
```

The proved coordinate bijection `u2=s*a^(-2)` identifies them as

```text
space 5: (scalar class,a)=(1,44)
space 6: (scalar class,a)=(2,13).
```

Each input retains the twelve selected R rows and the nonzero-`u3`
saturation. A literal complete reduced basis `[1]` therefore proves that the
whole displayed Laurent line is empty over `F_101` and after every scalar
extension. No D terminal is needed for either new line.

## Consolidated Accounting

```text
space-5 symbolic-u2 lines closed at u1=2:      6/100
space-6 symbolic-u2 lines closed at u1=2:      3/100
cross-space lines closed:                       9/200
R-only unit lines:                                  8
D-augmented unit lines:                             1
canonical fixed F_101 fibers represented:          900
remaining unclassified symbolic-u2 lines:         191
new continuous fit parameters:                      0
```

The one D-augmented line remains space-5 `u2=4`, whose exact R-only quotient
has dimension ten and whose selected `D18` multiplication determinant is
`95`. Version 3 imports that independently audited finite-algebra witness; it
does not relabel the nonunit R-only output as unit.

## Boundary

This theorem closes exactly the nine displayed `u1=2` lines. It does not
classify the other `191` lines, any of the other `98` nonzero `u1` values,
either mirror zero-zero chart, or a characteristic-zero system. It does not
promote the finite-field obstruction to physical HYM or quantum-gravity data.
The global symbolic chart count remains `138/140`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_cross_space_symbolic_prefix_v3_audit.py
```
