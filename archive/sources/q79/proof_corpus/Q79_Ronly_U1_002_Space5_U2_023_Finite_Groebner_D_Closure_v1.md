# q79 `u1=2`, Space-5 `u2=23` Finite-Groebner D Closure

## Status

`EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D`

## Selected Line

```text
field:          F_101
space:          5
u0,u1,u2:       76,2,23
scalar class:   1
a=v*u3:         27
coordinate map: v=27*t
```

The exact source relation `t*u3-1` and
`v=27*t` give
`v*u3-27` with inverse
`t=15*v`. The verifier also checks that
parent R rows 1 through 12 restrict exactly to the 12 symbolic-line rows.
Thus the finite quotient and selected D terminal come from the same parent
operator.

## Finite Quotient

The complete `78`-row reduced Groebner basis
presents a `20`-dimensional quotient with standard
monomials

```text
1, t, u7, u6, u5, u4, u3, h6, h5, h4, h3, h2, h1, t^2, u7*t, u6*t, u5*t, u4*t, h6*t, h5*t
```

Buchberger's criterion is checked for all `3003` row
pairs: `2211` by the exact
coprime-leading-monomial product criterion and
`792` by explicit S-polynomial
reduction to zero.

All `210` commutative basis products are reduced
exactly. Their canonical table hash is

```text
91f39c75931ac62f856618e06e1b21b4f85912f6971b8ee81b2b52068178da5e
```

All `8000` basis-triple
associativity identities pass. No locality, reducedness, or point count is
assumed.

## Parent Lift And Unit Witness

The four triangular `y` rows reconstruct with multiplication determinants

```text
{'y1': 95, 'y2': 95, 'y3': 95, 'y4': 95}
```

Both endpoint rows, all 12 R rows, and all four `y` rows then vanish in the
quotient. The selected D-terminal determinants are

```text
{'18': 1, '19': 95, '20': 87, '21': 95}
```

In particular, parent row `D18` has determinant
`1`. Its displayed
`20`-coordinate inverse multiplies its
remainder to

```text
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
```

Therefore `D18` is a unit in the complete R-only
quotient. Adjoining this selected D row makes the full R/`y`/D ideal the unit
ideal over `F_101` and after every field extension.

## Boundary

This closes exactly space 5, `u1=2`, `u2=23`, equivalently the canonical
line `(class,a)=(1,27)`. It does not classify another line or `u1` value,
prove a characteristic-zero statement, close either mirror zero-zero chart,
or promote the finite obstruction to physical HYM/QG data. The global
symbolic chart count remains `138/140`. New continuous fit parameters: `0`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_space5_u2_023_finite_groebner_D_closure_audit.py
```
