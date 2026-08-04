# q79 Cubic Norm and Full-Monodromy Root-Stack Strain Bridge v1

Date: 2026-07-15

## The unbranched map is natural, not an arbitrary matrix

For the cubic sheet algebra `A`, the existing map has the intrinsic form

```text
B_a(x,y) = Tr_A(a*x*y),
C_b(x,y) = D^2 N_A|_b(x,y)/sqrt(2),
J(a,b)   = B_a + C_b.
```

On the split locus `A=R^3`, `N_A(x)=x1*x2*x3`. Its Hessian is

```text
[[0,b3,b2],[b3,0,b1],[b2,b1,0]],
```

so this is exactly the previously computed diagonal plus opposite-edge map.
The normalization is forced by the Frobenius norm.

Equivariance alone would not prove uniqueness: the full `S3` intertwiner space
has dimension `8`, and the lane-preserving space has
dimension `4`. The q79 algebra and atom structure
remove that freedom. The diagonal term is the unital regular representation.
For the rank-three lane, complement sends each sheet atom to its unique
opposite edge. Exhaustion gives one `S3`-equivariant atom bijection. Equivalently,
the orthogonal commutant has four sign maps, but only one preserves the
canonical positive atom cone. Thus the displayed map carries no continuous or
discrete physical parameter.

## Why the coarse branch extension fails

For the generic cubic algebra `R[t]/(t^3+p*t+q)`, the exact symbolic audit gives

```text
det(J_flat)=(-Disc(t^3+p*t+q))^3.
```

For the simple branch model `(t^2-u)(t-1)`, the Smith valuations at `u=0` are

```text
[0, 0, 0, 1, 1, 1].
```

Hence the rank falls from six to `3`. The trace/norm formula
does extend across ramification as a morphism, but it cannot be a bundle
isomorphism on the coarse finite-flat algebra. This is an exact discriminant
no-go, not a missing numerical fit.

## The full cusp monodromy

Use the local cubic `z^3-3*x*z+2*y`, whose discriminant is proportional to
`x^3-y^2`. Newton-Puiseux analysis on the three-blowup SNC resolution gives

```text
strict transform : transposition, root order 2
E1               : three-cycle,  root order 3
E2               : transposition, root order 2
E3               : identity,      root order 1
```

The exceptional discriminant multiplicities are `2,3,6`, exactly as in the
existing 18-cusp certificate. The old order-two root stack on the strict
transform and `E2` is therefore exactly the determinant/sign substack. It was
correct for the SpinC line, but it did not yet retain the full `S3` sheet
carrier: that also requires an order-three root along every `E1`.

After the third blowup, `E3` meets the strict transform, `E1`, and `E2` at
three distinct points, so the nontrivial root divisors are disjoint. The
minimal full-monodromy completion is consequently unambiguous:

```text
root order 2 on the strict transform,
root order 3 on every E1,
root order 2 on every E2,
no root on E3.
```

## Rank-preserving global bridge

On this multi-root stack the q79 local system extends as the associated
orbifold bundle for its finite `S3` representation. Since `J` intertwines all
six `S3` elements, it descends globally and stays a rank-six Frobenius
isometry. The finite orthogonal connection is flat, hence orbifold HYM, and
`nabla J=0`.

An isotropy group carrying local monodromy `g` must have order divisible by
`ord(g)`. Taking exactly `ord(g)` is therefore the unique minimal effective
completion. Under strict same-source continuation -- preserve all six lanes,
their metric and connection, and add no new support map -- this root stack is
forced. The coarse extension is excluded by its rank drop.

## Exact boundary

This closes the previously open branch-locus continuation for the finite
q79 `S3` carrier at the unique minimal strict same-source tier. It does not yet
prove that primitive MTT must choose this physical continuation rather than
terminate the realization, nor does it identify the flat finite-monodromy
connection with the independently selected inverse-Fourier-Mukai/HYM Hessian
and overlap kernels. The full complex shared line also still needs an explicit
real/phase-neutral treatment outside the already real `Z64` helicity-two
subcarrier.

Current status:

```text
Q79_CUBIC_NORM_MAP_AND_COARSE_BRANCH_NOGO_CLOSED_FULL_MONODROMY_ROOTSTACK_STRAIN_BRIDGE_CLOSED_STRICT_SAME_SOURCE_MINIMAL_CONTINUATION_SELECTED_INVERSE_FOURIER_MUKAI_HESSIAN_AND_PRIMITIVE_PHYSICAL_BRANCH_OPEN
```
