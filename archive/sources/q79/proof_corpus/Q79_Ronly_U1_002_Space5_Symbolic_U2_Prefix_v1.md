# q79 R-only `u1=2`, Space-5 Symbolic-`u2` Prefix

## Status

`EXACT_U1_002_SPACE5_THREE_U2_SYMBOLIC_LINES_CLOSED`

## Statement

Work over `F_101` in the selected q79 space-5 R-only core. Fix

```text
u1 = 2,  u0*u1^2 = 1,  hence u0 = 76.
```

For each fixed nonzero `u2`, retain parent rows `R1,...,R12` and use the
Laurent coordinate `u3` with saturation `t*u3-1=0`. The exact reduced
Groebner bases for

```text
u2 = 1, 2, 3
```

are all the literal one-element basis `[1]`. Thus each saturated R-only ideal
is the whole polynomial ring over `F_101`; it remains the whole ring after
every field extension.

The certified bijection

```text
(scalar class s, canonical a) -> u2 = s*a^(-2)
```

identifies these values with

```text
u2=1 -> (s,a)=(1,1)
u2=2 -> (s,a)=(2,1)
u2=3 -> (s,a)=(2,13).
```

Each symbolic `u3` line represents all `100` nonzero fixed-`u3` fibers over
`F_101`. The three unit lines therefore close `300` canonical fixed fibers.
No `D` terminal is required because the R-only ideal is already unit.

## Exact construction

The committed family packet is regenerated directly from the class-free
space-5 parent core. It specializes `u1=2`, substitutes the selected
`u0=76`, fixes each of the `100` nonzero `u2` values, and rescales the
saturation variable by the invertible `u2` coefficient. All `100` emitted
inputs and their hashes are retained even though only the first three have
been classified.

The unit results use exact finite-field arithmetic in `msolve 0.10.1`. The
raw inputs, reduced-basis outputs, logs, family packet, builder, runner, and
binary fingerprint are hash-bound by the certificate.

## Accounting and boundary

```text
emitted space-5 u1=2 symbolic-u2 lines: 100
exactly classified:                         3
proved unit:                                3
remaining unclassified:                   97
canonical fixed F_101 fibers closed:      300
new continuous fit parameters:              0
```

This is the first exact prefix beyond the completed `u1=1` finite slice. It
does not close the other `97` space-5 lines, any space-6 `u1=2` line, either
mirror zero-zero chart, or a characteristic-zero system. It also does not by
itself promote the finite obstruction to physical HYM or quantum-gravity
data. The global symbolic chart count remains `138/140`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_space5_symbolic_u2_prefix_audit.py
```
