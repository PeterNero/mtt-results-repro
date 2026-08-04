# q79 R-only `u1=2` Complete Cross-Space Cover

## Status

`EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED`

Coverage: `COMPLETE_NONZERO_U2_CROSSSPACE_COVER`

## Theorem

At `u1=2`, the complete saturated symbolic-line ideals are unit at the
required R-only or full R/`y`/D tier for

```text
space 5: u2=1,...,100
space 6: u2=1,...,100.
```

Each R-only literal basis `[1]` excludes the entire displayed Laurent line
over `F_101` and every scalar extension. A nonunit R-only basis is counted
only when an exact finite-quotient certificate proves a selected D terminal
is invertible. Thus the theorem closes `200/200` symbolic lines and
represents `20000` canonical fixed `F_101` fibers.

## Exact Accounting

```text
space-5 contiguous lines closed:                100/100
space-6 contiguous lines closed:                100/100
cross-space lines closed:                       200/200
literal R-only unit lines:                          190
D-augmented unit lines:                              10
canonical fixed F_101 fibers represented:         20000
remaining unclassified u1=2 lines:                 0
new continuous fit parameters:                           0
```

## Finite-Quotient Exceptions

- space 5 `u2=4`: R-only quotient dimension `10`, `D18` determinant `95`.
- space 5 `u2=23`: R-only quotient dimension `20`, `D18` determinant `1`.
- space 5 `u2=31`: R-only quotient dimension `10`, `D18` determinant `36`.
- space 5 `u2=73`: R-only quotient dimension `10`, `D18` determinant `95`.
- space 5 `u2=75`: R-only quotient dimension `20`, `D18` determinant `1`.
- space 6 `u2=14`: R-only quotient dimension `20`, `D18` determinant `1`.
- space 6 `u2=21`: R-only quotient dimension `10`, `D18` determinant `84`.
- space 6 `u2=53`: R-only quotient dimension `10`, `D18` determinant `1`.
- space 6 `u2=59`: R-only quotient dimension `20`, `D18` determinant `1`.
- space 6 `u2=91`: R-only quotient dimension `3`, `D18` determinant `38`.

No nonunit R-only output is promoted by itself.

## Exact Solver Provenance

```text
engine:       msolve 0.10.1
binary bytes: 70980672
binary SHA256:a4c2beb9a7d186394af6bb21e235f76e3bfb3d0e6fdf872c27b517b8a6e87e13
mode:         one thread, exact F_101 reduced Groebner basis
```

Every counted log is checked for characteristic `101`, one thread, DRL,
reduced-basis output, zero invalid equations, and a completed solver timing.
Literal unit lines additionally require the solver's single-element/no-solution
verdict. Inputs, outputs, logs, and the provenance baseline are hash-bound.

## Next Exact Obligations

```text
space 5: all u2=1,...,100 closed (ALL_100_LINES_CLOSED)
space 6: all u2=1,...,100 closed (ALL_100_LINES_CLOSED).
```

## Boundary

All `200` nonzero-`u2`, `u1=2` cross-space lines are classified.
The theorem does not address the other `98` nonzero `u1` values, either
mirror zero-zero chart, or a characteristic-zero system. It does not promote
the finite-field obstruction to physical HYM or quantum-gravity data. The
global symbolic chart count remains `138/140`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_contiguous_prefix_audit.py
```
