# q79 inverse-root diagonal-symmetry no-go

Date: 2026-07-20

## Question

Can a rowwise diagonal action on the 19 inverse-root variables transport every
nonzero `u1` value to `u1=1`, thereby replacing the remaining 100 endpoint
fibers by the one computed slice?

## Exact calculation

For a polynomial row to be semi-invariant under weights `w_i`, every pair of
monomials in that row must have equal weight. The verifier includes every such
exponent-difference constraint from all 22 rows of each of the four parent
charts. The resulting matrices have 19 columns and exact ranks

```text
                 over Q   mod 2   mod 5
all four charts     19      18      19
```

Full rank modulo 5 implies that a weight modulo 100 must vanish modulo 25.
Writing it as `25z`, the remaining constraint is exactly the kernel modulo 4.
The verifier enumerates the complete mod-2 kernel, lifts every admissible
class through mod 4, checks all original constraints, and obtains precisely

```text
(0,...,0),
(0,...,0,50),
```

where the final coordinate is `v`. Thus the complete finite rowwise diagonal
symmetry is the identity together with `v -> -v`. In particular, every such
symmetry fixes `u1`.

## Consequence

The known sign involution is not a fragment of a larger diagonal torus. No
rowwise diagonal `F_101^*` action can move any `u1 != 1` fiber to the computed
`u1=1` slice. The remaining endpoint fibers therefore require a nonlinear or
generator-mixing intertwiner, a parameter-stratified proof, or exact cover.

## Claim boundary

This is a route-elimination theorem. It does not rule out triangular
automorphisms, coordinate maps that mix generators or rows, or an equivalent
source presentation before inverse-root normalization. It does not close a
mirror chart and does not change the `138/140` chart count.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_inverse_root_diagonal_symmetry_nogo_audit.py
```
