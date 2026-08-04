# q79 `u1=2`, Space-6 `u2=21` Finite-Groebner D Closure

## Status

`EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D`

## Selected Line

```text
field:          F_101
space:          6
u0,u1,u2:       76,2,21
scalar class:   1
a=v*u3:         28
coordinate map: v=28*t
```

The exact source relation `t*u3-1` and
`v=28*t` give
`v*u3-28` with inverse
`t=83*v`. The source verifier also checks
that parent R rows 1 through 12 restrict exactly to the 12 line rows. Thus
the finite quotient and D terminal come from the same selected parent
operator.

## Finite Quotient

The complete `48`-row reduced Groebner basis
presents a `10`-dimensional quotient with standard
monomials

```text
1, t, u7, u6, u5, u4, u3, h6, h5, h4
```

Buchberger's criterion is checked for all `1128` row
pairs: `804` by the exact
coprime-leading-monomial product criterion and
`324` by explicit S-polynomial
reduction to zero.

All `55` commutative basis products are reduced
exactly. Their canonical table hash is

```text
f551d737d1a3d5c079814b540e2f954acff8dd3e7739e80fc17f304ba74f1a1b
```

All `1000` basis-triple
associativity identities pass. No locality, reducedness, or point count is
assumed.

## Parent Lift And Unit Witness

The four triangular `y` rows reconstruct with multiplication determinants

```text
{'y1': 14, 'y2': 14, 'y3': 14, 'y4': 14}
```

Both endpoint rows, all 12 R rows, and all four `y` rows then vanish in the
quotient. The selected D-terminal determinants are

```text
{'18': 84, '19': 14, '20': 6, '21': 17}
```

In particular, parent row `D18` has determinant
`84`. Its displayed
`10`-coordinate inverse multiplies its
remainder to

```text
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0].
```

Therefore `D18` is a unit in the complete R-only
quotient. Adjoining this selected D row makes the full R/`y`/D ideal the unit
ideal over `F_101` and after every field extension.

## Boundary

This closes exactly space 6, `u1=2`, `u2=21`, equivalently the canonical
line `(class,a)=(1,28)`. It does not classify another line or `u1` value,
prove a characteristic-zero statement, close either mirror zero-zero chart,
or promote the finite obstruction to physical HYM/QG data. The global
symbolic chart count remains `138/140`. New continuous fit parameters: `0`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_space6_u2_021_finite_groebner_D_closure_audit.py
```
