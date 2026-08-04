# q79 symbolic finite-algebra D-closure theorem v3

Date: 2026-07-21

## Theorem

Let `I_R` be an exact R-only line ideal over a field `K`. Suppose its reduced
Groebner basis gives affine reductions for the eliminated coordinates and one
affine reduction for every quadratic product among the remaining coordinates.
Then the standard monomials form a finite basis of `A=K[x]/I_R`, and the basis
product table determines the complete quotient algebra. It is sufficient to
check associativity on all basis triples.

If the omitted `y` recurrences reconstruct through units in `A` and the image
`d` of a D-terminal has an invertible multiplication matrix

```text
m_d : A -> A, x |-> d*x,
```

then `d` is a unit. The inverse image of `1` under `m_d` is an explicit
inverse, so adjoining the D row makes the full R/y/D ideal equal to `(1)`.
The identity survives arbitrary scalar extension. No locality, reducedness,
or geometric point count is required.

## Exact applications

The verifier applies this lemma to eight fixed-`u1`, fixed-`a`, symbolic-`v`
lines in the two mirror spaces:

| space | class `s` | `a` | standard basis | dimension | D row | determinant |
|---:|---:|---:|---|---:|---:|---:|
| 5 | 1 | 18 | `1,v` | 2 | 18 | 24 |
| 5 | 2 | 2 | `1,u4,u5,u6,u7,v` | 6 | 18 | 36 |
| 5 | 2 | 5 | `1,u7,v` | 3 | 18 | 45 |
| 5 | 2 | 14 | `1,u4,u5,u6,u7,v` | 6 | 19 | 37 |
| 6 | 1 | 47 | `1,u4,u5,u6,u7,v` | 6 | 18 | 56 |
| 6 | 2 | 32 | `1,v` | 2 | 18 | 92 |
| 6 | 2 | 46 | `1,u4,u5,u6,u7,v` | 6 | 18 | 79 |
| 6 | 2 | 47 | `1` | 1 | 18 | 26 |

Every displayed determinant is nonzero in `F_101`. Each certificate contains
the complete multiplication table, all reconstructed coordinates, the D
remainder, an explicit inverse, and the verified product `(1,0,...,0)`. Every
dimension-six quotient passes all `6^3=216` basis associativity checks.

The final row is the reduced-point algebra `F_101` itself; its sole basis
triple is checked explicitly. Therefore all eight complete symbolic-line
ideals are unit over `F_101` and
every field extension. The independent full-parent involution

```text
(a,v) -> (-a,-v)
```

closes eight distinct sign partners, for sixteen symbolic lines in total.

## Reproducibility

The raw symbolic inputs, exact msolve reduced bases and logs, input packets,
and derived quotient certificates are stored under
`candidate_data/q79_Ronly_symbolic_finite_algebra_D_closure`. The audit reruns
the finite-algebra verifier independently for every line, regenerates the
consolidated certificate, and compares every JSON object byte-for-data.

The consolidated certificate is
`certificates/Q79_Ronly_Symbolic_Finite_Algebra_D_Closure_v3.json`.

## Claim boundary

This strengthens four space-5 lines and all four space-6 canonical exceptions
at `u1=1` to scheme-theoretic symbolic-`v` closure. It does not
classify other `a` or `u1` values, close either mirror zero-zero chart, prove
a characteristic-zero result, or supply physical HYM/QG promotion. These
lines were already present in the finite grid, so the chart count remains `138/140`.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_Ronly_symbolic_finite_algebra_D_closure_v3_audit.py
```
