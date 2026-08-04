# q79 Covariant Projective-Module HYM Symbol Naturality and Compression-Residual Theorem v1

**Date:** 2026-07-26
**Repository:** `mtt-qm-source-proof`
**Blockers:** `B.GEO.01`, `B.HS.01`
**Certificate:** `certificates/q79_covariant_projective_module_hym_symbol_naturality_cutset.certificate.json`

## Status

This theorem closes the universal mathematical construction needed by
`B.GEO.01`:

```text
curved unitary/HYM connection
    -> finite matrix-valued projective symbol p(x)
    -> covariant differential and curvature
    -> unitary Hessian-form transport
    -> external 1<2<3 lane flag
    -> invariant finite restriction or exact Feshbach operator.
```

The universal contract is `10/10`.

The actual q79 same-source diagram remains `0/3`. The selected visible and
hidden HYM endpoints, their explicit source-hashed projective symbol, and the
physical finite matching residual have not been emitted. Therefore
`B.GEO.01` remains open.

## Source Boundary

The current corpus establishes the following distinct tiers:

1. The shared q79 differential line and finite root-stack Hessian commute
   exactly. The same packet explicitly leaves continuum nonzero-Chern HYM
   naturality open.
2. The finite projected HYM carrier is exact at its declared cutoff.
3. A selected rank-two continuum HYM witness exists in a certified Wiener
   ball, but no rank-three physical transfer is claimed.
4. The physical heterotic deformation bundle

   \[
   Q_{\rm phys}
   =
   T^*X\oplus {\rm ad}(TX)\oplus {\rm ad}(E_v)
   \oplus {\rm ad}(E_h^\tau)\oplus TX
   \]

   has complex rank \(102\). The hidden order-three twist cancels in
   \({\rm ad}(E_h^\tau)\), making this deformation bundle ordinary even
   though \(E_h^\tau\) itself remains twisted.
5. The 27-state carrier is post-projection data. It is not the rank-102
   physical Galerkin Jacobian.
6. The native \(1<2<3\) flag is separate from the family and gauge factors.

The missing language was therefore not another flat finite matrix. It was an
exact curved projective module followed by a typed finite-reduction rule.

## Theorem A: Universal Curved Projector Symbol

Let \(X\) be the compact q79 six-manifold and let
\((E,h,\nabla)\) be a supplied finite-rank Hermitian bundle with unitary
connection. By the Narasimhan-Ramanan universal-connection theorem, there are
a finite integer \(N\), a fiberwise isometric embedding

\[
U:E\longrightarrow X\times\mathbb C^N
\]

and a smooth projection

\[
p=UU^*\in M_N(C^\infty(X))
\]

such that the connection on \(E\) is induced by the Grassmann connection on
the finite projective module \(pC^\infty(X)^N\):

\[
p\,d(Us)=U\nabla s.
\]

Thus \(U\) is an exact connection-preserving module isometry. Its curvature
identity is

\[
F_p=p(dp)\wedge(dp)p=UF_\nabla U^*.
\]

Consequently every Chern-Weil form is preserved. A nonzero-Chern HYM
connection is represented without being flattened.

The word "finite" here refers to the matrix size \(N\). The entries \(p(x)\)
are smooth functions and generally carry infinitely many base modes. This is
not a finite Fourier, Toeplitz, or root-stack truncation.

### Coupled Complex

Apply the construction blockwise to the ordinary rank-102 bundle
\(Q_{\rm phys}\). Let \(U_Q\) denote the direct-sum isometry and \(p_Q\) its
projector. Once the selected endpoint connections satisfy holomorphy and the
differential Bianchi identity, all same-source Atiyah and anomaly maps
transport with them:

\[
U_Q\bar D_Q=\bar D_p U_Q.
\]

Because \(U_Q\) is unitary for the same base metric and Sobolev domains,

\[
\bar D_p^*=U_Q\bar D_Q^*U_Q^*
\]

and hence

\[
H_p
=
(\bar D_p+\bar D_p^*)^2
=
U_Q(\bar D_Q+\bar D_Q^*)^2U_Q^*.
\]

The same argument applies to any gauge-fixed Hessian built functorially from
the supplied connection, curvature, metric, gauge slice, and action.

This proves exact connection and Hessian-form naturality after the physical
source is supplied. It does not select that source.

## Exact Nonzero-Chern HYM Witness

On the affine chart of \(\mathbb{CP}^1\), put

\[
d=1+u^2+v^2
\]

and

\[
p(u,v)
=
\frac1d
\begin{pmatrix}
1 & u-iv\\
u+iv & u^2+v^2
\end{pmatrix}.
\]

Exact polynomial arithmetic verifies

\[
p^*=p,\qquad p^2=p,\qquad {\rm tr}(p)=1,
\]

and

\[
p(\partial_u p)p=p(\partial_v p)p=0.
\]

Its Chern density is

\[
{\rm Tr}\bigl(p[\partial_up,\partial_vp]\bigr)
=
\frac{2i}{(1+u^2+v^2)^2}.
\]

Therefore

\[
\frac{1}{2\pi i}\int_{\mathbb R^2}
{\rm Tr}\bigl(p[\partial_up,\partial_vp]\bigr)\,du\,dv
=1.
\]

The curvature is proportional to the Fubini-Study form, so the connection is
Hermitian-Einstein/HYM on this line. This is an exact curved-symbol witness,
not a q79 visible or hidden bundle.

## Theorem B: Correct Placement of the 1<2<3 Flag

Suppose a stable HYM gauge factor is irreducible. Any parallel endomorphism
commutes with its holonomy. Its parallel endomorphism algebra is therefore
scalar. A scalar idempotent is only \(0\) or \(I\).

Hence a nontrivial nested rank-one/rank-two/rank-three flag cannot be inserted
inside an irreducible stable rank-three gauge bundle. Doing so would reduce
its holonomy and contradict the intended stable simple source.

The correct architecture is a tensor factor:

\[
\mathcal E_{\rm pre}
=
\Gamma(p_Q\mathbb C^N)
\widehat\otimes H_{\rm lane}
\widehat\otimes L_{\rm shared},
\]

where

\[
p_1={\rm diag}(1,0,0),\qquad
p_2={\rm diag}(1,1,0),\qquad
p_3=I_3
\]

act only on \(H_{\rm lane}\). The physical connection is

\[
\nabla_{\rm pre}
=
\nabla_Q\otimes I\otimes I
+I\otimes d_{\rm lane}\otimes I
+I\otimes I\otimes\nabla_{\rm shared}.
\]

The lane projectors

\[
P_j=p_Q\otimes p_j
\]

are then parallel:

\[
\nabla_{{\rm End}}P_j=0.
\]

They preserve the relative \(1<2<3\) sectors while leaving the irreducible
HYM holonomy untouched.

The shared differential line is a separate flat scalar tensor factor. It is
not identified with the curved HYM bundle. Applying the same flat line and
connection on both sides preserves the commuting diagram and the declared
holonomy.

### Exact Flag Witness

Tensor the preceding Bott projector with the three constant lane projectors:

\[
P_j^{\rm Bott}=p_{\rm Bott}\otimes p_j.
\]

After clearing the common denominator, the certificate verifies exactly:

```text
(P_j)^*=P_j
(P_j)^2=P_j
P_i P_j=P_i for i<=j
rank(P_1),rank(P_2),rank(P_3)=1,2,3
nabla_End(P_j)=0.
```

It also verifies on a rational rank-three irreducibility witness that the
gauge commutant is one dimensional, while the external lane projectors have
total ranks \(3,6,9\) and commute with the full gauge action.

## Theorem C: Exact Finite Reduction

Let \(H\) be the transported physical Hessian, \(P\) a declared finite
orthogonal projector, and \(Q=I-P\). Define the off-diagonal residual

\[
R=QHP.
\]

The bare Galerkin matrix \(PHP\) is an exact restriction of \(H\) if and only
if

\[
R=0.
\]

When \(R\ne0\), the exact finite operator at spectral parameter \(z\) is the
Feshbach-Schur map

\[
F_P(H-z)
=
P(H-z)P
-PHQ\,[Q(H-z)Q]^{-1}QHP,
\]

whenever the complementary inverse exists. The second term is the
same-source self-energy. It is determined by the physical Hessian and its
complementary Green operator; it is not a new fit parameter.

### Exact Rational Witness

Take

\[
P={\rm diag}(1,1,0,0)
\]

and compare

\[
H_0={\rm diag}(1,2,3,4)
\]

with

\[
H_1=
\begin{pmatrix}
1&0&1/2&0\\
0&2&0&0\\
1/2&0&3&0\\
0&0&0&4
\end{pmatrix}.
\]

Both have the same bare compression

\[
PH_0P=PH_1P={\rm diag}(1,2,0,0).
\]

For \(H_0\), \(QH_0P=0\). For \(H_1\),

\[
\lVert QH_1P\rVert_F^2=\frac14.
\]

The leading principal minors of \(H_1\) are

\[
1,\quad2,\quad\frac{11}{2},\quad22,
\]

so \(H_1\) is strictly positive. Its exact self-energy at \(z=0\) is

\[
\Sigma(0)=
\begin{pmatrix}
1/12&0\\
0&0
\end{pmatrix},
\]

and the effective finite Hessian is

\[
F_P(H_1)=
\begin{pmatrix}
11/12&0\\
0&2
\end{pmatrix}.
\]

The certificate verifies the exact block factorization and determinant
identity. Thus identical bare finite matrices need not represent the same
physical operator.

## q79 Exit Contract

The physical `B.GEO.01` exit now has three concrete rows:

```text
0/1  selected source-hashed visible/hidden HYM endpoints and connections
0/1  explicit p_Q, U_Q and rank-102 coupled-complex commuting diagram
0/1  transported finite subspace plus QHP=0 or Feshbach equality
```

The first row is `B.HS.01`. The second is its universal-connection
instantiation. The third is one finite residual/effective-operator
calculation.

No additional symbol functor needs to be invented. Conversely, no finite
root-stack matrix may be promoted until the third row is executed.

## Consequence for the Physical-Family Program

The previous physical-family theorem required

```text
B.HS.01 + B.GEO.01 + B.ACTION.01.
```

This result completes the universal mathematical part of `B.GEO.01`, but the
actual q79 diagram remains open. Therefore:

```text
full-domain chiral measure: 0/4
continuum reduced product:  1/9
```

Neither count changes.

## Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:     0
new fits:                            0
new observed values:                 0
```

The Bott chart coordinates and the rational Schur witness are proof data.
The physical spectral point and finite subspace must be selected by the
future same-source q79 geometry/action.

## Claim Boundary

Closed:

- exact curved connection-to-projective-symbol representation after a
  unitary connection is supplied;
- exact connection, curvature, Dolbeault-complex, adjoint, and Hessian-form
  naturality;
- correct external tensor-factor placement of the \(1<2<3\) flag;
- exclusion of a nontrivial parallel flag inside an irreducible stable HYM
  gauge factor;
- exact invariant-subspace/Feshbach criterion for finite reduction.

Open:

- the selected physical visible and hidden q79 endpoints;
- explicit \(U_Q\) and \(p_Q\) from those source hashes;
- the connection-transported finite q79 subspace;
- the physical \(QHP\) residual and complementary Green operator;
- equality with the existing finite root-stack Hessian or its corrected
  Feshbach successor;
- the selected upper action and full physical BV Hessian.

## Primary Mathematical Interfaces

- M. S. Narasimhan and S. Ramanan, *Existence of Universal Connections*:
  finite Grassmannian realization of supplied unitary connections.
- M. Griesemer and D. Hasler, *On the Smooth Feshbach-Schur Map*:
  exact isospectral finite-sector elimination.
- C.-Y. Hsiao and G. Marinescu, *Berezin-Toeplitz Quantization for Lower
  Energy Forms*: finite Toeplitz products have controlled large-level
  asymptotics, not automatic finite-cutoff equality.

## Version Delta

Version 1 replaces the ambiguous request for a flat "spectral/Weyl symbol"
with an exact curved projective-module construction. It fixes the location of
the \(1<2<3\) flag, proves the finite-reduction criterion, and reduces the
physical q79 exit to three source-bearing rows without promoting any of them.
