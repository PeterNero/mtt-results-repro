# q79 Shared-Circle Clutching C2/C3 Independence and Holomorphic Cutset v1

## Exact result

Let `P_delta -> K3` be the selected primitive circle bundle with

```text
delta = H-L,   delta^2 = -4,   H.delta = 0,
```

and let `X=P_delta x S1_shared`.  Because the K3 lattice is unimodular and
`delta` is primitive, cup product with `delta` maps `H2(K3,Z)` onto
`H4(K3,Z)`.  The integral Gysin sequence therefore gives

```text
H*(P_delta,Z) ranks = (1,0,21,21,0,1)
H4(X,Z) = H3(P_delta,Z) cup t = Z^21
H6(X,Z) = H5(P_delta,Z) cup t = Z,
```

with no relevant torsion.  Fiber integration identifies `H3(P_delta,Z)`
with `delta-perp` in the K3 lattice.  Since `H.delta=0`, there is a unique
primitive class `Hhat` satisfying `pi_!(Hhat)=H`; hence

```text
u = Hhat cup t in H4(X,Z)
```

is a canonical primitive mixed shared-circle class.

## Simultaneous clutching theorem

The odd K-theory Atiyah-Hirzebruch spectral sequence collapses on the free odd
cohomology of `P_delta`:

```text
K1(P_delta) = Z^22, graded by H3(P_delta,Z) plus H5(P_delta,Z).
```

For maps from a five-complex, `SU3` is already in the relevant stable range.
Its five-stage Postnikov tower gives

```text
0 -> H5(P_delta,Z) -> [P_delta,SU3] -> H3(P_delta,Z) -> 0.
```

The degree-six k-invariant cannot obstruct a map on `P_delta`.  Thus a
clutching map may carry an arbitrary degree-three class `a` and an independent
degree-five winding `k`.  Its mapping-torus bundle on `X` has, with the stated
Bott normalization,

```text
c1(E_g) = 0,
c2(E_g) = -a cup t,
c3(E_g) = 2 k [X]^*.
```

Choosing `a=-m Hhat` proves a smooth `SU3` bundle exists for every

```text
c2 = m u,   c3 = 2k.
```

In particular, the existing reference coefficient and chirality winding are
simultaneously topologically admissible:

```text
m=9,   k=+/-3   ->   c2=9u,   c3=+/-6,   index=+/-3.
```

No continuous fit parameter is introduced.  The old A103 construction was the
special `m=0` member, because its clutching map factored through `S5`; its
vanishing `c2` did not constitute a no-go for the full mapping-torus channel.

## Precise boundary

This closes a real topological compatibility gap.  It does **not** prove that
the `m=9,k=+/-3` member is selected by MTT, nor that its smooth bundle admits
the required holomorphic structure.  The next construction must still emit:

1. the inverse-gerbe twisted rank-one sheaf on the selected spectral cover;
2. WIT and a locally free determinant-zero rank-three inverse transform;
3. its actual total-space `c2` and `c3`, including the mapping-torus class;
4. balanced stability and an HYM connection;
5. the differential Bianchi identity on the same Fu-Yau branch.

There is an additional guard.  Pullback `H4(K3)->H4(X)` vanishes, so the
reference identity `9+11+4=24` is a base/differential allocation, not by itself
the total-space cohomological Bianchi theorem.  That identity must be replayed
after the non-pullback holomorphic bundle is constructed.

## UV consequence

The obstruction is no longer topological incompatibility between instanton
and chirality data.  It is now sharply holomorphic and analytic: construct the
selected twisted spectral object and prove local freeness, HYM, and the
differential anomaly equation.  UV completion is not claimed.

## Primary sources

- [Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Vector bundles and F theory](https://arxiv.org/abs/alg-geom/9709029)
- [Fu-Yau anomaly solutions](https://arxiv.org/abs/hep-th/0604137)
