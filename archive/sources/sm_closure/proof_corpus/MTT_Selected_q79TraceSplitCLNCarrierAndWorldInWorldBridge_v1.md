# MTT Selected q79 Trace-Split CLN Carrier and World-in-World Bridge v1

## Result

The q79 degree-three spectral cover supplies a canonical global realization of
the MTT `1+2+3=6` rank pattern, but it is not the nested ordered-sheet flag used
in the earlier A45 source interpretation.

Let

```text
pi:C -> K3
```

be the q79 determinant-zero degree-three spectral cover. It is the pullback of
the universal relative degree-three divisor over `|3*0|`. Hence it is finite
locally free of degree three and

```text
A = pi_* O_C
```

is a rank-three algebra bundle. The unit and trace obey

```text
Tr_A(1)=3.
```

Because the theory is over characteristic zero, the maps

```text
p_cen  = (1/3) unit o Tr,
p_lens = I-p_cen
```

are canonical complementary idempotents. Therefore

```text
A = O direct-sum A_0,       A_0=ker(Tr),
rank(O)=1, rank(A_0)=2, rank(A)=3.
```

Pull these bundles to `X=P_delta x S1_shared` and tensor every lane by the
same shared-circle line/local-system carrier `L_shared`. The six-direction
filter carrier is then

```text
H_CLN = L_shared tensor (O direct-sum A_0 direct-sum A),
rank(H_CLN)=1+2+3=6.
```

This construction adds no continuous parameter. The numerical holonomy of
`L_shared`, if it is used as a value-bearing phase, remains a separate source
question.

## Why this is better than a global sheet flag

The q79 spectral surface is connected (`b0=1`). Away from the branch locus its
three sheets therefore have transitive monodromy. A globally selected first
sheet would split the cover, so no global ordered sheet flag is available.
What survives monodromy canonically is exactly:

```text
constant/trace line             rank 1,
trace-zero standard plane       rank 2,
full permutation carrier        rank 3.
```

The earlier A45 linear-algebra statement remains true conditionally: if a
complete flag is supplied, it is unitarily equivalent to the displayed nested
projectors. What was not proved there is that the corpus rank count by itself
supplies the inclusion maps of a complete flag. The q79 geometry instead
selects orthogonal incremental lanes. This matches the Book's wording that the
three bundles add `1`, `2`, and `3` filter directions and that the Laplacians
commute.

This correction does not change the computed 27x27 matrix, Yukawa, mass, or
electroweak profile values. It changes only the claimed provenance of the
nested projectors.

## Orientation and the proto-spinor target

On the unbranched locus, let `P_sigma` be the real permutation action on the
three sheets. Odd permutations reverse orientation. There is a canonical
parameter-free correction

```text
rho_plus(sigma)=sign(sigma) P_sigma.
```

For every `sigma in S3`, `rho_plus(sigma)` is orthogonal with determinant one.
Thus the sign-twisted three-sheet carrier has `SO(3)` monodromy and the standard
Euclidean metric. Its invariant line and orthogonal plane are the same
rank-`1+2` trace decomposition, with the line carrying the sign character.

This supplies the correct oriented rank-three target for the world-in-world
polar construction. It does not yet prove a `Spin(3)` lift. That next check is
the lift of the actual q79 sheet monodromy to the binary double cover, or
equivalently the relevant `w2` obstruction.

## World-in-world polar bridge

For an invertible real `3x3` map `Q`, polar decomposition gives

```text
Q=R S,       R in SO(3),       S=S^T>0,
Mat(3,R)=so(3) direct-sum Sym(3),
dimensions 9=3+6.
```

The theorem above now supplies a q79-side oriented rank-three carrier on which
such a local map can live. The missing statement is no longer "where do ranks
1,2,3 come from?" It is the typed same-source map that identifies the real
world-in-world carrier with the sign-twisted q79 sheet carrier and emits the
actual `Q` or closure Hessian.

Eight physical bridge fields remain open: the real-carrier intertwiner, the
Spin lift, continuation across the branch locus, the selected `Q`/Hessian, a
gap/degeneracy certificate, the proto-spinor `J` map on the rank-two lane, any
value-bearing shared-circle holonomy, and HYM/connection covariance.

## Scope

Closed here:

```text
q79 finite-flat rank-three pushforward algebra,
canonical rank-one trace and rank-two trace-zero lanes,
shared-circle rank pattern 1+2+3=6,
transitive-monodromy no-go for a global ordered sheet flag,
canonical SO(3) sign-twist of the sheet carrier.
```

Still open:

```text
actual q79 sheet-monodromy Spin(3) lift,
same-source world-in-world carrier intertwiner,
selected Q/Hessian and branch-locus continuation,
proto-spinor J and HYM connection compatibility,
the independent A136 weighted-thimble interval decision.
```

No observed Standard Model value and no fitted continuous parameter enters this
theorem.

## External mathematical anchors

- [Finite locally free morphisms](https://stacks.math.columbia.edu/tag/02K9)
- [Trace and discriminant of a finite locally free morphism](https://stacks.math.columbia.edu/tag/0BVH)
- [Direct summands of finite locally free sheaves](https://stacks.math.columbia.edu/tag/01C5)

Next artifact:
`MTT_Selected_q79SignedPermutationSpinLiftAndWorldInWorldQSource_v1`.
