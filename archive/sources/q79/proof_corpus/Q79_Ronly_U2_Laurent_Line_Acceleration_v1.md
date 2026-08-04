# q79 R-only `u2` Laurent-line acceleration theorem

Date: 2026-07-21

## Theorem

Fix either inverse-root space and any nonzero `u1` over `F_101`. The map

```text
(s,a) -> u2 = s*a^(-2),
s in {1,2}, a in {1,...,50},
```

is a bijection onto `F_101^*`. Thus the two scalar-class charts with their
50 sign representatives are exactly the 100 nonzero `u2` specializations,
with neither duplication nor omission.

At any fixed nonzero `a`, the substitutions

```text
u3 = a*v^(-1),
v  = a*u3^(-1)
```

are inverse Laurent-coordinate maps. They identify
`F_101[v,v^(-1)]` with `F_101[u3,u3^(-1)]` and biject the 100 nonzero finite
values in either coordinate.

The exact source audit additionally proves that parent rows 1 through 12 are
independent of `v` and of all four `y` variables, and that the two scalar
classes have literally identical R-only rows in each space. The space-5 and
space-6 cores remain distinct.

Consequently, at fixed `u1` one saturated symbolic `u3` solve for each of the
100 nonzero `u2` values in each space exactly replaces all 100 fixed-`v`
R-only solves on that line. The execution problem is reduced from 20,000
fixed fibers to 200 symbolic Laurent lines without changing the ideal.

## Boundary

This is an exact coordinate and workload reduction, not an emptiness result.
Every symbolic line still needs a literal unit certificate. If an R-only line
is nonunit, complete `R/y/D` closure must be proved separately. The theorem
does not identify the two space cores, lift from characteristic 101, or
promote the polynomial source to physical HYM/QG data.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_Ronly_u2_laurent_line_acceleration_audit.py
```
