# q79 Explicit Cech Projector, Connection Correction, and Twisted-Adjoint Compiler Theorem v1

**Date:** 2026-07-26
**Repository:** `mtt-qm-source-proof`
**Blockers:** `B.HS.01`, `B.GEO.01`
**Certificate:** `certificates/q79_explicit_cech_projector_connection_compiler_cutset.certificate.json`

## Status

The preceding projective-module theorem proved that every supplied unitary
q79 HYM connection has a curvature-preserving finite matrix-valued symbol. Its
embedding was existential.

This theorem replaces that existential step by an explicit finite compiler:

```text
endpoint transition cocycle + Hermitian metric + local connection forms
    -> unitary Cech cocycle
    -> explicit finite projector p
    -> explicit connection correction Gamma
    -> exact physical connection, curvature and Hessian
    -> ordinary rank-102 q79 coupled complex.
```

The compiler contract is `12/12`. It introduces no post-endpoint symbol
selector and no physical parameter.

The actual physical q79 instantiation remains `0/3`, because `B.HS.01` has not
yet emitted the endpoint cocycles, metrics and HYM connections. The intrinsic
finite subspace and its `QHP` or Feshbach execution also remain open.

## 1. Input Data

Let \(E\to X\) be a rank-\(r\) Hermitian bundle over compact q79 \(X\). Choose:

1. a finite good cover \(\{V_i\}_{i=1}^m\);
2. holomorphic transition matrices \(g_{ij}\);
3. local Hermitian metric matrices \(h_i\);
4. a smooth partition \(\{\chi_i\}\) subordinate to the cover with

   \[
   \sum_i\chi_i^2=1;
   \]

5. local unitary connection forms \(A_i\) for the supplied connection.

Coordinates obey \(v_i=g_{ij}v_j\), and metric compatibility gives

\[
h_j=g_{ij}^*h_i g_{ij}.
\]

Define unitary transition matrices

\[
u_{ij}=h_i^{1/2}g_{ij}h_j^{-1/2}.
\]

Then

\[
u_{ij}^*u_{ij}=I,\qquad
u_{ij}u_{jk}=u_{ik}.
\]

The square roots are smooth positive square roots. They change frames, not
the physical bundle or connection.

## 2. Explicit Cech Projector

In local frame \(k\), define

\[
U_k:\mathbb C^r\longrightarrow\mathbb C^{mr},
\qquad
(U_k)_i=\chi_i u_{ik}.
\]

Because \(\sum_i\chi_i^2=1\),

\[
U_k^*U_k
=
\sum_i\chi_i^2u_{ki}u_{ik}
=I.
\]

Thus \(U_k\) is fiberwise isometric. Its global range projector is

\[
p=UU^*,
\]

whose \(ij\) block is

\[
p_{ij}=\chi_i\chi_j u_{ij}.
\]

Indeed,

\[
\begin{aligned}
(p^2)_{ij}
&=\sum_l
\chi_i\chi_lu_{il}\,
\chi_l\chi_ju_{lj}\\
&=\chi_i\chi_j
\left(\sum_l\chi_l^2\right)u_{ij}\\
&=p_{ij}.
\end{aligned}
\]

Unitarity also gives \(p^*=p\). Therefore

\[
p\in M_{mr}(C^\infty(X))
\]

is an explicit smooth Hermitian idempotent with

\[
\Gamma(E)\simeq pC^\infty(X)^{mr}.
\]

This formula is source-hashable once the endpoint atlas and metric are
source-hashed.

## 3. Why the Projector Alone Is Not Enough

The Grassmann connection induced by this convenient Cech embedding is

\[
A_k^{(0)}
=
U_k^*dU_k
=
\sum_i\chi_i^2 u_{ki}\,du_{ik}.
\]

The term \(\sum_i\chi_i\,d\chi_i\) vanishes because

\[
\sum_i\chi_i\,d\chi_i
=\frac12d\sum_i\chi_i^2
=0.
\]

In general \(A_k^{(0)}\) is not the physical HYM connection \(A_k\).
Therefore \(p\,d\) must not be promoted by itself.

The difference

\[
\Delta_k=A_k-A_k^{(0)}
\]

transforms tensorially:

\[
\Delta_j=u_{ji}\Delta_i u_{ij}.
\]

It consequently defines the global projective-module one-form

\[
\Gamma=U\Delta U^*,
\qquad
p\Gamma p=\Gamma.
\]

Define

\[
D_p=p\,d+\Gamma
\]

on the range of \(p\). For a local section \(s\),

\[
\begin{aligned}
D_p(Us)
&=p\,d(Us)+U\Delta U^*Us\\
&=U(ds+A^{(0)}s)+U\Delta s\\
&=U(ds+As).
\end{aligned}
\]

Hence

\[
D_pU=U\nabla_A
\]

exactly.

It follows immediately that

\[
F_{D_p}=UF_AU^*.
\]

The Chern-Weil forms and the HYM equation are preserved. On the same metric
and Sobolev domain,

\[
D_p^*=U\nabla_A^*U^*
\]

and every functorially constructed gauge-fixed Hessian satisfies

\[
H_p=UH_AU^*.
\]

This is the constructive version of the preceding universal-connection
result. The complete symbol is the pair

```text
(p, Gamma),
```

not the projector \(p\) alone.

## 4. Twisted Hidden Adjoint Descent

Let \(E_h^\tau\) be the order-three twisted hidden rank-nine endpoint. Its
unitary local lifts obey

\[
u_{ij}u_{jk}u_{ki}
=
\alpha_{ijk}I_9,
\qquad
\alpha_{ijk}^3=1.
\]

The fundamental bundle remains twisted. However,

\[
\operatorname{Ad}(u_{ij})
\operatorname{Ad}(u_{jk})
\operatorname{Ad}(u_{ki})
=
\operatorname{Ad}(\alpha_{ijk}I_9)
=I.
\]

Therefore

\[
\operatorname{ad}(E_h^\tau)
=
\operatorname{End}_0(E_h^\tau)
\]

is an ordinary rank-\(80\) bundle and has an honest Cech projector and
corrected connection.

### Exact Qutrit Witness

For

\[
W(a,b)=X^aZ^b,\qquad ZX=\omega XZ,
\]

one has

\[
W(a,b)W(c,d)
=
\omega^{bc}W(a+c,b+d).
\]

Among the 81 products, 36 have nonzero central phase. On matrix units,

\[
\operatorname{Ad}(a,b)E_{jk}
=
\omega^{b(j-k)}E_{j+a,k+a}.
\]

The certificate checks all

\[
9\cdot9\cdot9=729
\]

composition rows and finds zero failures. It also verifies that the scalar
identity is fixed and that removal of this scalar lane leaves rank \(80\).

This is the exact finite witness for the hidden-twist cancellation already
required by the physical deformation complex. It does not make
\(E_h^\tau\) itself ordinary.

## 5. Rank-102 q79 Compiler

The physical preprojection bundle is

\[
\mathcal Q_{\rm phys}
=
T^*X
\oplus\operatorname{ad}(TX)
\oplus\operatorname{ad}(E_v)
\oplus\operatorname{ad}(E_h^\tau)
\oplus TX.
\]

Its complex ranks are

\[
3+8+8+80+3=102.
\]

Apply the preceding construction blockwise:

\[
p_Q
=
p_{T^*X}\oplus p_{\operatorname{ad}TX}
\oplus p_{\operatorname{ad}E_v}
\oplus p_{\operatorname{ad}E_h}
\oplus p_{TX}.
\]

The diagonal connection is

\[
D_Q^{\rm diag}=p_Qd+\Gamma_Q^{\rm diag}.
\]

For every supplied same-source Atiyah, anomaly or gauge-fixing map

\[
\Phi_{ba}:E_a\longrightarrow E_b,
\]

define

\[
\widehat\Phi_{ba}=U_b\Phi_{ba}U_a^*.
\]

Thus the complete coupled differential is compiled by conjugating each
declared source block. If the endpoint holomorphy and differential Bianchi
conditions give

\[
\bar D_Q^2=0,
\]

then the compiled differential obeys

\[
\bar D_p^2=0
\]

and

\[
\bar D_pU_Q=U_Q\bar D_Q.
\]

The adjoint, harmonic projector, Green operator and Hessian transport in the
same way whenever their declared domains exist.

No matrix entry is selected by this compiler. All entries are determined by
the endpoint transitions, endpoint connections, tangent-connection
convention and coupling maps.

## 6. Presentation Independence

Let \(U\) and \(U'\) be two Cech compilers for the same Hermitian connection,
possibly using different covers, frames or partitions. Put

\[
W=U'U^*.
\]

Then

\[
W^*W=p,\qquad
WW^*=p'.
\]

Thus \(W\) is a partial unitary between the two projective modules. The
corrected connections obey

\[
D_{p'}W=WD_p
\]

on the range of \(p\), and consequently

\[
H_{p'}W=WH_p.
\]

Therefore cover, frame and partition choices are presentations. They are not
physical parameters or branches.

## 7. Intrinsic Finite-Subspace Rule

Presentation independence has an important finite-dimensional consequence.
Let \(P_N\) be a finite projector chosen intrinsically on the physical bundle.
Its two projective presentations are

\[
\widehat P_N=UP_NU^*,
\qquad
\widehat P_N'=U'P_NU'^*.
\]

They satisfy

\[
\widehat P_N'=W\widehat P_NW^*.
\]

The residuals and Feshbach operators are therefore conjugate.

A fixed ambient Fourier window is not generally equal to the transported
projector. Reusing the same ambient window after changing \(U\) can create a
presentation artifact.

### Exact Shared-Circle Witness

Take \(z=e^{ix}\) and the physical line connection

\[
A=\frac{i}{3}\,dx.
\]

Compare

\[
U_0=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
U_1=
\begin{pmatrix}
3/5\\(4/5)z
\end{pmatrix}.
\]

Both are isometric. For \(U_1\),

\[
A^{(0)}=\frac{16i}{25}\,dx,
\qquad
\Delta=-\frac{23i}{75}\,dx.
\]

The corrected connection satisfies

\[
(p_1d+\Gamma_1)U_1=U_1(d+i\,dx/3).
\]

The certificate verifies this and the second-order Hessian identity for
source modes \(k=-3,\ldots,3\), whose positive eigenvalues are

\[
\left(k+\frac13\right)^2.
\]

Now choose the intrinsic source window

\[
k\in\{-1,0,1\}.
\]

The second component of \(U_1z^k\) has ambient mode \(k+1\). A raw ambient
window \(\{-1,0,1\}\) therefore removes the second component of the \(k=1\)
state. Exact retained and lost norms are

\[
\frac9{25},
\qquad
\frac{16}{25}.
\]

This is not physical leakage. It is an exact no-go witness against freezing
the ambient cutoff across presentations.

The remaining q79 finite test must therefore:

1. select or identify the finite subspace intrinsically;
2. transport it through the actual \(U_Q\);
3. compute \(QHP\);
4. use bare compression only if \(QHP=0\), otherwise use the exact Feshbach
   operator.

## 8. Revised B.GEO.01 Exit

The physical rows remain:

```text
0/1  source-hashed endpoint Cech cocycles, Hermitian metrics and connections
0/1  actual compiled p_Q, Gamma_Q and rank-102 coupled maps
0/1  intrinsic finite subspace plus QHP=0 or Feshbach equality
```

The status remains `0/3`, because no physical endpoint data are fabricated.
However, the second row is no longer an independent source-selection
problem. Once `B.HS.01` and the declared tangent-connection row emit their
data, the Cech compiler determines it.

The remaining independent mathematical work after the endpoint source is:

```text
identify the intrinsic physical finite subspace
    + compute one residual/Feshbach equality.
```

## 9. Relation to B.HS.01

This theorem does not interfere with the ongoing eta9 calculations.

`B.HS.01` still requires:

- the selected visible `U_eta9` endpoint after `B.ETA9.01` and
  `B.ETA9.02`;
- a genuine hidden twisted-holomorphic locally free rank-nine endpoint;
- one common positive Gauduchon/HYM chamber;
- endpoint HYM connections and anomaly/Bianchi compatibility;
- the declared tangent-connection convention.

Those outputs necessarily possess finite local transition data and local
connection forms. This theorem specifies how to compile them without another
choice.

## 10. Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:     0
new fits:                            0
new observed values:                 0
```

The cover, frames, partition, embeddings \(U_0,U_1\), Laurent mode labels and
the rational witness coefficients are proof/presentation data.

## 11. Claim Boundary

Closed:

- explicit finite projector from supplied endpoint transition data;
- exact correction from its Grassmann connection to the supplied physical
  connection;
- exact curvature, HYM, coupled-differential, adjoint and Hessian transport;
- exact hidden central-twist cancellation in the rank-80 adjoint;
- exact blockwise construction of the ordinary rank-102 carrier;
- presentation independence;
- the intrinsic finite-subspace rule and raw-ambient-cutoff no-go.

Open:

- the selected physical endpoint transition cocycles and HYM metrics;
- their common positive Gauduchon chamber;
- the actual source-hashed numerical \(p_Q,\Gamma_Q\);
- the intrinsic finite subspace and its relation to the current finite
  root-stack carrier;
- the physical \(QHP\) residual or Feshbach equality.

## 12. Primary Interfaces

- M. S. Narasimhan and S. Ramanan, *Existence of Universal Connections*:
  existential universal-connection representation.
- V. Brinzanescu, A. Halanay and G. Trautmann, *Vector Bundles on
  non-Kahler Elliptic Principal Bundles*: twisted Cech/Fourier-Mukai setting
  for non-Kahler principal elliptic bundles.
- A. Perego, *Kobayashi-Hitchin Correspondence for Twisted Vector Bundles*:
  HYM/Hermite-Einstein output after the twisted holomorphic endpoint and
  common Gauduchon polystability are supplied.

## Version Delta

Version 1 makes the projective-module bridge constructive. It identifies the
connection correction omitted by a projector-only description, proves exact
hidden-adjoint descent and rank-102 compilation, and shows that the finite
subspace must be transported intrinsically. It changes no physical acceptance
count and promotes no eta9 or Hull-Strominger endpoint.
