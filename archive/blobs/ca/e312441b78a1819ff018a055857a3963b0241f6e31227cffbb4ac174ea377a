# q79 R-only symbolic-v line theorem

Date: 2026-07-20

## Theorem

Let `s` be either scalar square-class representative `1` or `2` in
`F_101`. For each independent mirror-space chart `5` and `6`, restrict the
selected R-only system by

```text
u1 = 1,
u0 = 1,
u2 = s,
v*u3 = 1.
```

Retain the six `h` recurrence rows and the six R-terminal rows. The resulting
ideal has 13 cubic-or-lower generators in

```text
F_101[h1,h2,h3,h4,h5,h6,u3,u4,u5,u6,u7,v].
```

For all four `(space,s)` pairs, msolve 0.10.1 returns the literal reduced
Groebner basis `[1]`. Therefore each displayed symbolic line is empty not
only over `F_101`, but over every extension of `F_101`, including its
algebraic closure.

## Exact restriction

The line input is not an interpolation through the earlier 100 samples. It
is obtained directly from the parent polynomial rows. The endpoint

```text
u0*u1^2 - 1 = 0
```

vanishes identically after `u0=u1=1`. The scalar endpoint becomes

```text
s*v^2*u3^2 - s
  = s*(v*u3 - 1)*(v*u3 + 1),
```

so it is implied exactly by the added line relation `v*u3-1=0`. The selected
R-only rows contain no `y1,...,y4`; the predecessor theorem proves that their
four constant-pivot rows reconstruct uniquely. No D-terminal row is used.

The deterministic certifier reparses the parent and restricted polynomial
files, performs the substitutions in `F_101`, compares all twelve selected
rows monomial by monomial, verifies the endpoint factorization, and checks
each committed reduced basis and execution log.

## Results

```text
space  scalar class  elapsed seconds  max RSS KiB  reduced basis
5      1             262.59           1,060,836    [1]
5      2             284.41           1,060,532    [1]
6      1             283.33           1,060,824    [1]
6      2             284.28           1,059,924    [1]
```

This strictly strengthens the predecessor result on the same four lines:
the earlier certificate checked all 100 `F_101` points per line, whereas the
new calculation proves the symbolic line ideal itself is unit. The 400
finite-field fibers are therefore subsumed rather than counted as 400 new
closures.

## Accounting

```text
displayed symbolic-v line ideals:                  4/4 closed
F_101 points already covered on those lines:       400
additional parameter lines closed by this result:  0
remaining finite endpoint lines:                   39,996
```

The reduced generic-`u2` coefficient-field computation at fixed `u1=1`
reached its 900-second guard without deciding unit or nonunit status. That is
a computational boundary, not evidence for either outcome.

## Claim boundary

This is a characteristic-101 algebraic theorem for four displayed R-only
restrictions. It is not a theorem over characteristic zero, does not classify
the other 39,996 finite parameter lines, and does not decide the complete
R-only core or the simultaneous R/D system. It also does not promote these
finite polynomial rows to selected physical HYM or quantum-gravity data.

The next exact target is a generic-`u2` unit identity over `F_101(u2)` with
its denominator polynomial retained. Such an identity would reduce the
remaining work at fixed `u1` to the finite roots of that denominator; those
exceptional lines would then be checked together with the simultaneous D
conditions.

## Reproduce

Regenerate the deterministic certificate with:

```text
python scripts/certify_q79_Ronly_symbolic_v_lines.py
```

The four committed solver inputs, outputs, packets, and logs are under
`candidate_data/q79_Ronly_symbolic_v_lines`. The exact line emitter is
`scripts/emit_q79_Ronly_symbolic_v_line.py`; it requires `python-flint`.
