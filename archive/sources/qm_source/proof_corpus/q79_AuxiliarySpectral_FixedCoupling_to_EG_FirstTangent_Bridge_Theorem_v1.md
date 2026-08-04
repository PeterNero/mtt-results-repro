# q79 Auxiliary-Spectral Fixed-Coupling to EG First-Tangent Bridge Theorem v1

## Status

**Closed at the normalized relative-\(S\) source/cocycle-generator
first-tangent tier on the existing auxiliary gauge-covariant spectral
family.**

The physical external regulator is not selected, the second and higher
coupling derivatives are not matched, and no regulator-independent
fixed-coupling Cstar net or global interacting state is constructed.

This theorem advances the physical-continuum promotion table from \(0/9\) to
\(1/9\). It does not alter the already closed \(5/5\) finite-regulator Cstar
landing or the \(1/6\) Borel-source table.

## 1. Inputs

The proof uses the following existing results without reopening them:

1. the cofinal finite-rank auxiliary BV/Cauchy spectral family
   \[
   P_N=\mathbf 1_{[0,\Lambda_N]}(\Delta_{\rm BV});
   \]
2. exact transport of that family on the based q79 gauge/frame presentation
   orbit;
3. a compact-gauge physical Cstar algebra and bounded fixed-coupling dynamics
   at every finite auxiliary regulator;
4. the direct Lorentzian Epstein-Glaser (EG) prescription and its local
   normalized Stueckelberg-Petermann (SP) comparison;
5. the normalization
   \[
   Z(0)=0,\qquad DZ(0)=\operatorname{id}.
   \]

The regulator family is auxiliary presentation data. Nothing in this theorem
promotes it to the regulator selected by the still-open upper q79 action.

## 2. Finite-Regulator Family

At one finite spectral cutoff \(N\), let

\[
H_N(\lambda)=H_{0,N}+\lambda V_N,
\qquad V_N=P_NVP_N,
\]

on the finite physical Hilbert space, where \(V\) is the same declared action
source used by the formal Lorentzian theory. Assume \(H_{0,N}\) and \(V_N\)
are bounded, self-adjoint and invariant under the compact gauge action.
Define

\[
U_{N,\lambda}(t)=e^{-itH_N(\lambda)},\qquad
\alpha^\lambda_{N,t}(A)
=U_{N,\lambda}(t)^* A U_{N,\lambda}(t)
\]

and the interaction-picture relative cocycle

\[
W_{N,\lambda}(t)
=U_{N,0}(t)^*U_{N,\lambda}(t).
\]

Finite rank is stronger than needed here: boundedness already makes
\(\lambda\mapsto U_{N,\lambda}(t)\) norm entire.

## 3. Norm-Duhamel Tangent

### Theorem 3.1

For every finite \(N\) and every real \(t\),

\[
\left.\frac{d}{d\lambda}W_{N,\lambda}(t)\right|_{\lambda=0}
=-i\int_0^t\alpha^0_{N,s}(V_N)\,ds.
\]

For every \(A\in\mathcal A_N^{\rm phys}\),

\[
\left.\frac{d}{d\lambda}
\alpha^\lambda_{N,t}(A)\right|_{\lambda=0}
=i\int_0^t
\left[\alpha^0_{N,s}(V_N),\alpha^0_{N,t}(A)\right]\,ds.
\]

Equivalently,

\[
\left.\frac{d}{d\lambda}
\alpha^\lambda_{N,t}(A)\right|_{\lambda=0}
=i\int_0^t
\alpha^0_{N,s}\!\left(
[V_N,\alpha^0_{N,t-s}(A)]
\right)\,ds.
\]

### Proof

The bounded-operator Duhamel identity gives

\[
\left.\frac{d}{d\lambda}
e^{-it(H_{0,N}+\lambda V_N)}\right|_{\lambda=0}
=-i\int_0^t
e^{-i(t-s)H_{0,N}}V_Ne^{-isH_{0,N}}\,ds.
\]

Multiplication on the left by \(e^{itH_{0,N}}\) gives the first formula.
Writing

\[
\alpha^\lambda_{N,t}(A)
=W_{N,\lambda}(t)^*\alpha^0_{N,t}(A)W_{N,\lambda}(t)
\]

and differentiating gives the commutator formula. The second displayed form
uses the automorphism property of \(\alpha^0\). All derivatives and integrals
converge in operator norm. QED.

The right-hand side is exactly the first interaction-picture
Bogoliubov/Dyson retarded coefficient in the same finite regulator.

## 4. Gauge and Gauss Descent

Let \(G_N\) be the compact regulator gauge group and \(\Pi_N\) the
Gauss-neutral projector. If

\[
[U_N(g),H_{0,N}]=[U_N(g),V_N]=0,
\]

then the Duhamel integrand is gauge invariant. Hence the tangent intertwines
the Haar conditional expectation:

\[
E_N\!\left(\delta_{V_N,t}A\right)
=\delta_{V_N,t}\!\left(E_N(A)\right).
\]

If \(A=\Pi_NA\Pi_N\) and \(V_N\) preserves \(\Pi_N\mathcal H_N\), then

\[
\delta_{V_N,t}A
=\Pi_N(\delta_{V_N,t}A)\Pi_N.
\]

Thus the first tangent descends to the same finite physical Cstar corner as
the nonzero-coupling dynamics.

## 5. EG/SP First-Tangent Identification

First identify the source across the nested spectral family. Let

\[
\mathcal D_{\rm fin}=\bigcup_M\operatorname{Ran}P_M
\]

inside the declared common operator domain of \(V\). For
\(\phi,\psi\in\mathcal D_{\rm fin}\), both vectors are fixed by \(P_N\) for
all sufficiently large \(N\). Hence

\[
\langle\phi,V_N\psi\rangle
=\langle P_N\phi,V P_N\psi\rangle
=\langle\phi,V\psi\rangle
\]

eventually. This is exact matrix-element stabilization on the common finite
spectral core. It is not operator-norm convergence of the generally
unbounded continuum interaction.

The certified Lorentzian comparison has the form

\[
\widehat S=S_{\rm EG}\circ Z
\]

with \(Z(0)=0\) and \(DZ(0)=\operatorname{id}\). The chain rule therefore
gives

\[
D\widehat S(0)[V]
=DS_{\rm EG}(0)[DZ(0)V]
=DS_{\rm EG}(0)[V].
\]

Consequently the normalized relative-\(S\) source tangent is independent of
the chosen representative inside the certified SP orbit. The mixed
coupling/time cocycle-generator tangent is

\[
\left.
\frac{\partial^2}{\partial t\,\partial\lambda}
W_{N,\lambda}(t)\right|_{(0,0)}
=-iV_N.
\]

The finite Duhamel coefficient is the same first regulated Dyson coefficient.
The prior direct Lorentzian bridge already supplies coefficientwise
graphwise cutoff removal in the formal equicausal topology. Combining that
bridge with the common-source stabilization above lands this first
source/generator tangent on the Lorentzian EG/SP first tangent.

This closes precisely:

```text
formal_EG_tangent_identification
```

at the following scope:

```text
relative-S source derivative and cocycle-generator tangent at the origin;
first retarded coefficient in the existing formal coefficientwise topology,
with inserted observables compared by the SP tangent transport.
```

No Cstar-norm convergence of the finite-time Duhamel response is asserted.

## 6. Composite-Probe Qualification

The normalization \(DZ(0)=\operatorname{id}\) does **not** imply literal
scheme independence of an untransported interacting composite field.

The correct comparison of Bogoliubov maps is schematically

\[
\widehat R_V(F)
=R_{Z(V)}\!\left(DZ(V)F\right).
\]

Differentiating at \(V=\lambda V_0\), \(\lambda=0\), can produce

\[
D^2Z(0)(V_0,F).
\]

The exact scalar jet

\[
Z_a(x)=x+ax^2
\]

has \(Z_a(0)=0\) and \(Z_a'(0)=1\), but

\[
\left.
\frac{\partial^2}{\partial\lambda\,\partial\varepsilon}
\left[
Z_a(\lambda v+\varepsilon f)-Z_a(\lambda v)
\right]
\right|_{0}
=2avf.
\]

For \(a=v=f=1\), this is exactly \(2\), not zero.

Therefore:

- the relative-\(S\)/cocycle first tangent is fixed;
- the corresponding observable response is compared after the required
  \(DZ(\lambda V)\) transport;
- literal equality of untransported composite fields is not claimed;
- second and higher EG/SP jet matching remains a separate problem.

This qualification is necessary for the \(1/9\) promotion to be rigorous.

## 7. Exact Executable Witness

The certificate uses

\[
U_G=\operatorname{diag}(1,1,-1,-1),\qquad
\Pi_G=\operatorname{diag}(1,1,0,0)
\]

and

\[
V=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&2\\
0&0&2&0
\end{pmatrix},
\qquad
A=E_{11}.
\]

For the witness \(H_0=0\) and \(t=1\),

\[
\dot W_0=-iV,
\qquad
\dot\alpha_0(A)=i[V,A]
=i
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\]

The exact rational checks verify:

- self-adjoint and gauge-invariant \(V\);
- a self-adjoint, gauge-invariant, Gauss-neutral probe;
- equality of the Duhamel and first retarded coefficients;
- star-compatible Leibniz action on all \(16^2\) matrix-unit pairs;
- gauge covariance on all 16 matrix units;
- preservation of the Gauss-neutral corner;
- equality of the full and compressed common-source tangents on the retained
  finite core;
- the first-order cocycle law;
- the nonzero \(Z''\) composite-probe qualification.

The witness time and quadratic SP coordinate are proof coordinates only.
They are not q79 physical parameters.

## 8. Frontier After the Theorem

| Layer | Previous | Current |
|---|---:|---:|
| finite fixed-coupling Cstar landing | 5/5 | 5/5 |
| physical continuum-promotion rows | 0/9 | 1/9 |
| Borel source rows | 1/6 | 1/6 |

The eight open continuum rows are:

1. upper-action selection of the external regulator family;
2. a nonperturbative full nonabelian chiral measure;
3. a cofinal embedding or asymptotic-morphism package;
4. a uniform Lieb-Robinson or asymptotic-microcausality bound;
5. a uniform phase-space, energy or nuclearity bound;
6. a vanishing norm-level Gauss/BRST/Ward defect;
7. an ultrafilter-independent or independently selected limit;
8. a selected positive global interacting state.

Higher fixed-coupling/EG jets and Cstar-norm convergence of the finite-time
Duhamel response remain open inside the analytic work needed by these rows.
`B.QFT.02` and `B.ACTION.01` therefore remain open.

## 9. Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

## 10. Primary Mathematical Benchmarks

- R. Brunetti, M. Duetsch and K. Fredenhagen,
  *Perturbative Algebraic Quantum Field Theory and the Renormalization
  Groups*, arXiv:0901.2038.
- D. Buchholz and K. Fredenhagen,
  *A C*-algebraic approach to interacting quantum field theories*,
  arXiv:1902.06062.

These references supply the SP and relative-\(S\) frameworks. The q79
spectral-family attachment, exact gauge/Gauss witness, acceptance accounting
and nonpromotion boundary are the contribution of this theorem.
