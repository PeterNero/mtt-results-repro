# q79 R-only class-free core and representative-line theorem

Date: 2026-07-20

## Exact reduction theorem

For each mirror space `5` and `6`, consider the two inverse-root scalar
charts over `F_101`. Retain parent row `0`, the six `h` recurrences
`1,...,6`, and the six R-terminal rows `7,...,12`.

These thirteen rows contain neither `y1,...,y4` nor `v`. Parent rows
`14,...,17` have successive nonzero constant pivots in `y1,...,y4`, so every
solution of the retained rows extends uniquely through the omitted `y` chain.
The companion endpoint

```text
v^2*u2*u3^2 = s,  s in {1,2},
```

forces `u2*u3` nonzero. Its projection is represented exactly by the
Rabinowitsch row

```text
t*u2*u3 = 1.
```

Consequently the four scalar charts reduce to two 15-variable, 14-cubic
cores, one per space. The two scalar classes in a fixed space emit identical
cores. The space-5 and space-6 cores have different SHA-256 hashes and are not
transported into one another.

Over an algebraic closure, either scalar chart extends from its space core by
choosing the required square root `v`. Over `F_101`, the two scalar charts
partition the nonzero `u2` values by square class, so their union is the
class-free core.

## Exact line theorem

For each of the four `(space,scalar class)` pairs, fix

```text
u1 = 1,
a = v*u3 = 1,
u2 = s,
```

and exhaust `v=1,...,100`. The map `v -> u3=v^-1` is a bijection of
`F_101*`, so this is the complete nonzero-`u3` line at the displayed
`(u1,u2)` coordinates.

Every one of the 400 fixed fibers has a literal reduced Groebner basis
`[1]`. Each computation uses only the six `h` recurrences and six R-terminal
rows in the resulting 10-variable cubic ring. No D-terminal row is used, no
timeout is counted, and no continuous fit parameter is introduced.

## Accounting

The exact status is:

```text
four scalar charts -> two class-free cubic cores: closed
four representative nonzero-v lines:             closed
fixed endpoint fibers on those lines:             400/400 unit
remaining endpoint lines:                         39,996
remaining fixed endpoint fibers:                  3,999,600
```

The global space-5 and space-6 core computations reached guarded timeouts.
Those timeouts are not unit-ideal results. The complete four-chart no-go
therefore remains open.

## Claim boundary

This theorem proves the exact reduction and the four displayed finite-field
lines. It does not classify the other `(u1,a)` lines, identify the two mirror
spaces, or promote the finite-field obstruction to selected physical HYM or
quantum-gravity data.

The next proof object is a triangular jet or Groebner-pivot stratification in
`(u1,a)`. A checkpointed exhaustive cover of the remaining 39,996 lines is an
exact fallback, not yet a completed theorem.

## Reproduce

The committed certificate is
`certificates/Q79_Ronly_ClassFree_Core_and_Representative_Lines_v1.json`.
Regenerate its deterministic consolidation with:

```text
python scripts/certify_q79_Ronly_classfree_representative_lines.py
```

The optional fixed-fiber solver producer is
`scripts/benchmark_q79_Ronly_representative_v_lines.py`; it requires
`python-flint` and msolve 0.10.1.
