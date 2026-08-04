# q79 Ordinary Exterior/Dual HYM No-Go and Derived-Kernel Cutset v1

Status:
`Q79_ORDINARY_EXTERIOR_DUAL_HYM_COVARIANCE_CLOSED_SAME_BRANCH_JDE_EXTENSION_CLOSED_NOGO_NONLOCAL_DERIVED_KERNEL_PATH_EXACTLY_TYPED_OPEN`

## The standard HYM functors

For a rank-three connection, the dual and exterior-square differentials are

```text
A -> -A^T,
A -> tr(A) I - A^T.
```

The second identity is derived exactly in the executable certificate by
differentiating `Lambda^2(I+tA)` in the oriented opposite-edge basis. The same
formulas hold for curvature. On an `SU(3)` connection `tr(F)=0`, so both give
`-F^T`. They preserve type `(1,1)`, primitivity, and the Hilbert-Schmidt norm.
Thus ordinary dual/exterior transport really does preserve the HYM equations.

That valid statement is not the needed quarter-turn.

## Exact sector action

Use the ordered Hermitian basis

```text
(D11,D22,D33 ; S23,S13,S12 ; K23,K13,K12).
```

Ordinary duality acts as

```text
(-I3, -I3, +I3),
```

and exterior square acts as

```text
(ones(3)-I3, -I3, +I3).
```

Both preserve `D`, `S`, and `K` separately. The required map instead is

```text
J_DE(d,s)=(-s,d),
J_DE^2=-I.
```

Therefore neither ordinary functor equals `J_DE`. Ordinary duality is an
involution, and exterior square also has no diagonal/edge exchange. This closes
the most obvious attempted extension of the flat twisted-exterior symbol.

## The chirality obstruction

For any complex bundle,

```text
c_k(V*)=(-1)^k c_k(V).
```

Consequently `c3(V*)=-c3(V)`. The sectioned q79 reference branch has `c3=6`,
so its dual has `c3=-6`. More generally, any intended chiral branch with
nonzero `c3` cannot be complex-linearly self-dual on a compact connected
complex threefold: `V isomorphic to V*` would force `2 c3=0`, hence `c3=0` in
the torsion-free top cohomology.

Duality can relate opposite-chirality branches and gives them equal HYM energy.
It does not act within one selected chiral branch and does not force that
branch's projected Hessian to be `J_DE` invariant.

## What survives

The remaining Fourier-Mukai route must be genuinely nonlocal. A valid
same-branch construction must provide all of the following:

1. the normalized relative Poincare gerbe and vanishing integral restriction;
2. a holomorphic Prym-gerbe trivialization;
3. an inverse-gerbe twisted rank-one spectral sheaf;
4. its WIT index and locally free rank-three inverse transform;
5. determinant zero, actual total-space `c3`, balanced stability, and HYM;
6. a same-branch Fourier-Mukai autoequivalence stabilizing the Chern character;
7. its real action on the selected six-dimensional `Ext1`/deformation plane;
8. exact checks `T=J_DE`, `T^2=-I`, and preservation of the `L2` Gram form and
   projected HYM Hessian.

The current q79 packets close only the first two topological inputs: normalized
Poincare data and integral Dixmier-Douady restriction zero. They do not yet
emit the holomorphic trivialization, spectral sheaf, locally free transform, or
balanced HYM connection. The certificate records this as `2/11`, rather than
mistaking a categorical Fourier-Mukai availability theorem for the selected
physical operator.

## Consequence for the GR program

The ordinary bundle-functor route is now closed no-go. The live choices are:

```text
nonlocal same-branch Fourier-Mukai autoequivalence satisfying the 11-row test,
autonomous Lens/modular descent with the selected structures,
or direct computation of the projected 2x2 HYM Hessian.
```

No measured value and no fitted parameter is used.

## Primary references

- Friedman, Morgan, and Witten, [Vector Bundles over Elliptic Fibrations](https://arxiv.org/abs/alg-geom/9709029)
- Caldararu, [Derived Categories of Twisted Sheaves on Elliptic Threefolds](https://arxiv.org/abs/math/0012083)
- Brinzanescu, Halanay, and Trautmann, [Vector Bundles on non-Kahler Elliptic Principal Bundles](https://arxiv.org/abs/1008.3365)
