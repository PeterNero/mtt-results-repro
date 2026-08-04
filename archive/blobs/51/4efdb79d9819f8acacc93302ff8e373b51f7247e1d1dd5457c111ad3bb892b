# q79 fixed-u1 exceptional-line D-closure theorem

Date: 2026-07-20

## Theorem

In the space-5, scalar-class-1 inverse-root chart over `F_101`, impose

```text
u1 = u0 = 1,
a = v*u3 = 18,
u2 = 18^(-2) = 77.
```

The exact reduced Groebner basis of the selected 13-row R-only symbolic-line
ideal is triangular and presents its complete quotient algebra as

```text
A = F_101[v]/(v^2 + 90v + 5)
  = F_101[v]/((v - 56)^2).
```

Thus this R-only exception is one nonreduced point of length two. It is not a
positive-dimensional branch and is not merely a finite-point observation.

The four omitted `y` coordinates reconstruct uniquely in `A`; each recurrence
has the constant unit pivot `99`. After that lift, both endpoint rows, all six
`h` recurrences, all six R terminals, and all four `y` recurrences vanish in
`A`. The first D-terminal row reduces to

```text
D18 = 100 + 97v.
```

The certificate verifies the explicit Bezout identity

```text
68*(v^2 + 90v + 5) + (36 + 17v)*(100 + 97v) = 1
```

in `F_101[v]`. Therefore `D18` is a unit in the complete nonreduced quotient.
Adjoining the selected D terminal makes the full R/D ideal on this symbolic
line the unit ideal over `F_101` and after every field extension, including
the algebraic closure. In particular, the terminal eliminates both the
support point and its nilpotent tangent direction.

## Sign partner

All 22 rows of each of the four space-5/space-6, class-1/class-2 inverse-root
parents are even in `v`. Under

```text
(a,v) -> (-a,-v),
```

the parent is fixed, `u2=s*a^(-2)` and `u3=a/v` are fixed, and the line
relation `v*u3-a` maps to its negative. Hence each complete R/y/D line scheme
is isomorphic to its sign partner. The deterministic certificate checks all
88 parent rows, all 200 nonzero scalar-selection cases, and all 20,000
nonzero `(a,v)` cases. The representatives `a=1,...,50` therefore form an
exact canonical cover of all 100 nonzero values.

The line `a=18` theorem consequently also closes `a=83=-18`, with no second
calculation and no added parameter.

## Exact artifacts

The symbolic-line input, exact msolve 0.10.1 output, execution log, and input
packet are committed under
`candidate_data/q79_Ronly_fixed_u1_exceptional_line`. The parent chart is the
already committed input under
`candidate_data/q79_Ronly_classfree_representative_lines`.

The two deterministic certificates are:

```text
certificates/Q79_Ronly_FixedU1_Exceptional_Line_D_Closure_v1.json
certificates/Q79_Inverse_Root_V_Sign_Involution_v1.json
```

Their checkers use exact finite-field polynomial arithmetic through
`python-flint`. They reconstruct every quotient coordinate, evaluate all
source rows, and verify the displayed Bezout identity directly.

## Claim boundary

This closes exactly the canonical `u1=1, a=18` symbolic line and, by the
proved involution, its `a=83` sign partner. It does not classify other `a`
lines, other `u1` values, the two remaining mirror charts as a whole, or any
characteristic-zero lift. It also does not by itself promote the finite
polynomial system to selected physical HYM or quantum-gravity data.

The running finite-cutset computation is separate: it exhausts all 50
canonical `a` values at `u1=1` in every space/scalar chart and sends every
R-only exception to the complete R/y/D parent. That calculation must finish
before any full fixed-`u1` or full-chart no-go is claimed.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_Ronly_fixed_u1_exceptional_line_D_closure_audit.py
```
