# q79 symbolic finite-algebra D-closure theorem

Date: 2026-07-20

## Finite-quotient lemma

Let `K` be a field and let `I_R` be an ideal whose exact reduced Groebner
basis has affine pivot rows for the eliminated coordinates and one quadratic
pivot row for every product `z_i*z_j` among `k` remaining coordinates. Then
the standard monomials

```text
1, z1, ..., zk
```

form a basis of the complete quotient algebra `A=K[x]/I_R`. Reading the
quadratic rows as product reductions determines every multiplication in `A`.
Associativity can therefore be checked on the `(k+1)^3` triples of basis
elements.

Suppose the omitted `y` recurrences reconstruct by units of `A`, and let `d`
be the image of one selected D-terminal row after that reconstruction. If the
matrix of multiplication

```text
m_d : A -> A,  x |-> d*x
```

has nonzero determinant, then `m_d` is invertible. Applying its inverse to
the algebra unit produces an explicit `d^(-1)` in `A`, so `d*d^(-1)=1`.
Consequently adjoining that D row to `I_R` gives the unit ideal. This identity
survives every field extension of `K`.

The lemma needs no assumption that `A` is local, reduced, or supported at a
known number of geometric points.

## Application to the q79 lines

Apply the lemma over `K=F_101` to the four space-5 inverse-root lines

```text
u1 = u0 = 1,
u2 = s*a^(-2),
v*u3 = a,
```

with the following exact data:

| scalar class `s` | `a` | standard basis | `dim A` | unit D row | `det(m_D)` |
|---:|---:|---|---:|---:|---:|
| 1 | 18 | `1,v` | 2 | 18 | 24 |
| 2 | 2 | `1,u4,u5,u6,u7,v` | 6 | 18 | 36 |
| 2 | 5 | `1,u7,v` | 3 | 18 | 45 |
| 2 | 14 | `1,u4,u5,u6,u7,v` | 6 | 19 | 37 |

Every determinant is nonzero in `F_101`. The certificates contain the full
multiplication table, the reconstructed affine and `y` coordinates, the D
remainder vector, its exact inverse vector, and the product vector

```text
(1,0,...,0).
```

The dimension-six cases each pass all `6^3=216` basis associativity checks.
They are not forced into the square-zero local pattern observed on the
dimension-two and dimension-three lines. The general finite-algebra argument
closes them without such a decomposition.

Therefore all four complete R/y/D symbolic-line ideals are unit over `F_101`
and after every field extension, including the algebraic closure.

## Sign partners

The independently proved full-parent involution

```text
(a,v) -> (-a,-v)
```

fixes the parent equations and transports each line scheme isomorphically to
its sign partner. The theorem therefore closes eight distinct fixed-`a`
symbolic lines in total, with no new solve and no added parameter.

## Reproducibility

For each line, the repository stores the symbolic input, input-construction
packet, exact msolve 0.10.1 reduced basis, solver log, and derived finite-
algebra certificate under
`candidate_data/q79_Ronly_symbolic_finite_algebra_D_closure`.

The verifier reconstructs every product from the reduced basis, checks
commutativity and associativity, evaluates all thirteen symbolic R-line rows,
reconstructs the four `y` rows by exact quotient units, evaluates all 22
parent rows, and verifies the displayed D inverse. The consolidated result is

```text
certificates/Q79_Ronly_Symbolic_Finite_Algebra_D_Closure_v1.json
```

## Claim boundary

This strengthens four canonical `space5, u1=1` lines from a finite list of
`F_101` endpoint checks to complete symbolic-`v` scheme closure. Their four
sign partners are closed by transport.

It does not classify the other three R-exceptional canonical lines currently
known in the finite space-5 cover, any other `a` or `u1`, either space-6
scalar class, or the two remaining mirror charts globally. It is not a
characteristic-zero lift or a physical HYM/QG promotion. Because these lines
were already included in the finite-grid theorem, the finite chart accounting
remains `138/140`; the gain is the stronger scheme-theoretic tier.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_Ronly_symbolic_finite_algebra_D_closure_audit.py
```
