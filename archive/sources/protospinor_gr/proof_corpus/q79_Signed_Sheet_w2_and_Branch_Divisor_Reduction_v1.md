# q79 Signed-Sheet w2 and Branch-Divisor Reduction v1

Date: 2026-07-15

## Universal obstruction formula

Let

```text
rho_plus(sigma)=sign(sigma) P_sigma in SO(3)
```

and let `a` be the mod-two sign/discriminant class of the q79 sheet monodromy
on the branch complement. Restriction to a transposition subgroup `C2` gives

```text
rho_plus|C2 = 1 direct-sum sign direct-sum sign.
```

Hence its total Stiefel-Whitney class restricts to

```text
(1+a)^2=1+a^2.
```

Restriction from `S3` to this `C2` is injective in mod-two degree two: transfer
back multiplies by the odd index three. Naturality therefore proves

```text
w2(E_rho_plus)=a cup a.
```

For a degree-one mod-two class, `a cup a` is the Bockstein associated to
`0->Z2->Z4->Z2->0`. Consequently,

```text
strict Spin exists on the branch complement
iff the sign character lifts to a Z4 character.
```

This replaces an unspecified list of binary relator signs by one cohomological
test. It is consistent with the local `Dic_3` result: braid generators lift,
while a global relation may still obstruct the lift.

## q79 branch class

The degree-three spectral cover is pulled back from the universal hyperplane
divisor of a smooth plane cubic. Its branch curve in the hyperplane `P2` is the
dual cubic, whose degree is

```text
d(d-1)=3*2=6.
```

Since the genus-two K3 map pulls `O(1)` back to `H`,

```text
[B]=6H.
```

The spectral-surface intersection data independently reproduces this:

```text
R dot pi^*H=(A+B)^2 A=2 A^2 B=12=6 H^2.
```

Because `H^2=2` in the even K3 lattice, `H` cannot be a nontrivial multiple.
The K3 lattice is unimodular, so `[B]=6H` has lattice divisibility six.

## Conditional final Spin decision

For a connected reduced irreducible divisor in a simply connected surface, the
standard meridian/Gysin sequence gives

```text
H1(K3\B;Z)=Z_div([B]).
```

Thus, once reduced irreducibility is certified for the selected pulled-back
dual sextic,

```text
H1(B_open;Z)=Z6.
```

The sign map `Z6->Z2` exists, but it has no lift to `Z4`: an odd image in `Z4`
has order four and cannot be the image of a generator of `Z6`. Therefore

```text
a^2 != 0,
w2 != 0,
strict q79 Spin fails on the branch complement.
```

This last no-go remains conditional on one selected-geometry check: prove that
the pulled-back dual sextic is reduced and irreducible, or compute the same
abelian meridian relation directly. The trial identity-alignment surface is not
a selected source and is not used to promote this condition.

If the no-go closes, it does not invalidate the proto-spinor. It selects the
other already isolated route: construct a genuine SpinC determinant line with
`c1 mod 2=w2`, or replace the singular sheet carrier by a selected smooth HYM
carrier and recompute its obstruction.

Current status:

```text
UNIVERSAL_W2_AND_BRANCH_6H_CLOSED_STRICT_SPIN_NOGO_ONE_COMPLEMENT_CHECK_OPEN
```
