# q79 SM APS-Boundary-Crossing Line Reduction and Shared-Line Source-Cutset Theorem v1

## Status

This theorem resolves the algebraic part of the first noncollar q79
boundary-phase target.

For the already certified finite APS witness

\[
A(s)=\operatorname{diag}(-2,s,3),\qquad -1\leq s\leq1,
\]

it proves:

1. one positive regular crossing and spectral flow \(+1\);
2. an APS negative-projector rank jump from two to one;
3. impossibility of ordinary unitary presentation transport across the jump;
4. exact determinant-line factorization through one crossing kernel line;
5. a \(U(1)\)-stabilizer no-go for selecting a phase from the operator and
   projector data alone;
6. the unique nontrivial abstract comparison of spectral-flow parity with the
   finite q79 shared sign character, which gives \(-1\) for this witness.

The sixth item is a finite parity shadow. It is not an identification with the
full Dai-Freed analytic determinant phase.

## 1. Inputs

The theorem composes:

1. the local q79 auxiliary elliptic-BV package and its paired generalized-APS
   boundary domain;
2. the finite-shell comparison theorem, including the exact crossing path
   above;
3. the common-phase torsor quotient theorem;
4. the q79 universal flat differential-line packet;
5. the determinant-object type-separation packet from the SM repository;
6. standard spectral-flow, eta/Maslov and determinant-line theorems.

The two new repository inputs are hash pinned in `source_manifest.json`.

## 2. Exact regular crossing

At the three distinguished parameters,

\[
\begin{aligned}
A_-&=A(-1)=\operatorname{diag}(-2,-1,3),\\
A_0&=A(0)=\operatorname{diag}(-2,0,3),\\
A_+&=A(1)=\operatorname{diag}(-2,1,3).
\end{aligned}
\tag{2.1}
\]

With a zero mode assigned to the complementary adjoint APS domain, the
negative spectral projectors are

\[
\begin{aligned}
P_-^-&=\operatorname{diag}(1,1,0),\\
P_-^0&=\operatorname{diag}(1,0,0),\\
P_-^+&=\operatorname{diag}(1,0,0).
\end{aligned}
\tag{2.2}
\]

The crossing projector is

\[
P_K=\operatorname{diag}(0,1,0),
\qquad
K_{\mathrm{cross}}=\ker A_0=\operatorname{span}_{\mathbb C}(e_1).
\tag{2.3}
\]

Since

\[
\dot A(0)=\operatorname{diag}(0,1,0),
\]

the crossing form on \(K_{\mathrm{cross}}\) is

\[
\Gamma(e_1)=\langle e_1,\dot A(0)e_1\rangle=1.
\tag{2.4}
\]

The crossing is regular and positive. Therefore

\[
\operatorname{sf}(A)=+1.
\tag{2.5}
\]

The certificate checks (2.1)-(2.5) over exact rational arithmetic.

## 3. Why presentation transport stops

Unitary conjugation preserves projector rank. Equations (2.2) give

\[
\operatorname{rank}P_-^-=2,\qquad
\operatorname{rank}P_-^+=1.
\tag{3.1}
\]

Consequently no unitary \(U\) can satisfy

\[
UP_-^-U^\dagger=P_-^+.
\tag{3.2}
\]

This is why the prior gauge/frame, diffeomorphism and temporal presentation
transports cannot simply be extended through this crossing. Their
constant-rank hypothesis genuinely fails.

The minimal stabilization deficit is exactly one.

## 4. Crossing-line factorization

The negative spaces split orthogonally as

\[
E_-(A_-)=E_-(A_+)\oplus K_{\mathrm{cross}},
\tag{4.1}
\]

because

\[
P_-^-=P_-^++P_K,\qquad P_-^+P_K=0.
\tag{4.2}
\]

Equivalently, there is an exact sequence

\[
0\longrightarrow E_-(A_+)
\longrightarrow E_-(A_-)
\longrightarrow K_{\mathrm{cross}}
\longrightarrow0.
\tag{4.3}
\]

The determinant functor gives the canonical line isomorphism

\[
\det E_-(A_-)
\cong
\det E_-(A_+)\otimes\det K_{\mathrm{cross}}.
\tag{4.4}
\]

In the ordered basis,

\[
e_0\wedge e_1
\longleftrightarrow
e_0\otimes e_1.
\tag{4.5}
\]

Equation (4.4) is canonical. A scalar map

\[
\det E_-(A_-)\longrightarrow\det E_-(A_+)
\]

is not: it additionally requires a unit trivialization of
\(\det K_{\mathrm{cross}}=K_{\mathrm{cross}}\), or equivalently a unit dual
covector.

Thus the vague boundary phase is reduced to one exactly typed line.

## 5. Stabilizer no-go

For \(u\in U(1)\), define

\[
U(u)=\operatorname{diag}(1,u,1).
\tag{5.1}
\]

Every \(U(u)\):

1. is unitary;
2. commutes with \(A(s)\) for every \(s\);
3. fixes all projectors in (2.2)-(2.3);
4. acts on \(K_{\mathrm{cross}}\) by multiplication by \(u\).

Suppose the operator path, Hermitian structure and spectral projectors
selected a unit vector \(v\in K_{\mathrm{cross}}\) equivariantly. Since the
data are fixed by \(U(-1)\), equivariance would require

\[
v=U(-1)v=-v,
\]

and hence \(v=0\), contradicting unit norm.

Therefore:

```text
B.QFT.02_source_free_crossing_phase_selection
  = excluded_by_U1_stabilizer_nogo.
```

The certificate verifies the stabilizer action exactly for
\(u=1,i,-1,-i\). The general no-go is the one-line group argument above.

## 6. Finite shared-sign parity shadow

Spectral flow is additive. Its parity defines

\[
\mathbb Z\xrightarrow{\bmod 2}\mathbb Z_2.
\tag{6.1}
\]

The elements of \(\mathbb Z_{64}\) annihilated by multiplication by two are
exactly

\[
\{0,32\}.
\tag{6.2}
\]

Hence the unique nontrivial homomorphism

\[
\mathbb Z_2\longrightarrow\mathbb Z_{64}
\tag{6.3}
\]

sends \(1\mapsto32\). The q79 shared-line character sends

\[
0\mapsto+1,\qquad32\mapsto-1.
\tag{6.4}
\]

Composing (6.1), (6.3) and (6.4) gives the exact parity character

\[
\chi_{\mathrm{par}}(A)=(-1)^{\operatorname{sf}(A)}.
\tag{6.5}
\]

For (2.5),

\[
\chi_{\mathrm{par}}(A)=-1.
\tag{6.6}
\]

This closes an abstract finite parity comparison. It does not prove that the
physical continuum boundary crossing line is the pullback of the q79 shared
line, nor that (6.6) is the complete exponentiated eta invariant.

## 7. Why the older flavor phase cannot fill the gap

The SM type-separation packet distinguishes:

1. \(\det(E_\nu)=\Lambda^3E_\nu\), the ordinary determinant of the
   rank-three neutral-family bundle;
2. \(\operatorname{Det}(D_\nu)\), the analytic determinant line of a chiral
   Dirac family.

Their bases, fibers and holonomy functors differ. No current index,
transgression or holonomy-equality theorem identifies them. Therefore the
previous neutral-family holonomy cannot be inserted as the boundary
Dai-Freed phase.

This prevents a tempting but invalid reuse of the SM parity result.

## 8. Minimal physical source contract

Promoting the finite parity shadow to a physical relative boundary phase
requires all of:

1. a selected physical q79 noncollar boundary family
   \(A_{\partial}(s)\);
2. its actual crossing kernel line \(K_{\partial}\);
3. a unitary parallel intertwiner
   \[
   \iota_{\partial}:
   K_{\partial}\longrightarrow
   c_{\partial}^{*}L_{64}^{\mathrm{univ}};
   \]
4. the boundary classifying path or loop \(c_{\partial}\), including the
   endpoint comparison needed to obtain a scalar;
5. an analytic index/transgression comparison with the Dai-Freed determinant
   line;
6. the eta/Maslov/BFV and finite-counterterm normalization.

The current finite witness supplies item 2 only at its model tier. The
universal shared-line packet supplies the target of item 3 at the finite
root-stack-symbol tier, but not \(\iota_{\partial}\).

## 9. Theorem

For the exact finite APS crossing (2.1), the endpoint determinant comparison
factors through one and only one crossing line as in (4.4). The operator and
projector data do not select a unit trivialization of that line. The unique
nontrivial abstract spectral-flow-parity comparison with the finite q79
shared sign character gives \(-1\), but the physical analytic determinant
phase remains open until the source contract in Section 8 is supplied.

Accordingly,

```text
B.QFT.02_finite_APS_crossing_line_reduction
  = closed_exact

B.QFT.02_noncollar_boundary_phase_dimension
  = reduced_to_one_crossing_line_plus_eta_BFV_counterterm_data

B.QFT.02_full_relative_Dai_Freed_phase
  = open.
```

## 10. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed inputs:                0
```

The sign in (6.6) is a derived abstract parity character, not a fitted phase
or a promoted physical observable.

## 11. Reproduction

Run:

```powershell
python scripts/verify.py
python -m unittest discover -s tests -v
```

The generated certificate is:

```text
certificates/q79_sm_boundary_crossing_line_reduction.certificate.json
```

## 12. References

- B. Booss-Bavnbek, M. Lesch and J. Phillips, *Unbounded Fredholm Operators
  and Spectral Flow*, arXiv:math/0108014.
- P. Kirk and M. Lesch, *The eta-invariant, Maslov index, and spectral flow
  for Dirac-type operators on manifolds with boundary*,
  arXiv:math/0012123.
- X. Dai and D. S. Freed, *Eta-Invariants and Determinant Lines*,
  arXiv:hep-th/9405012.
- A. S. Cattaneo, P. Mnev and N. Reshetikhin, *Perturbative quantum gauge
  theories on manifolds with boundary*, arXiv:1507.01221.
