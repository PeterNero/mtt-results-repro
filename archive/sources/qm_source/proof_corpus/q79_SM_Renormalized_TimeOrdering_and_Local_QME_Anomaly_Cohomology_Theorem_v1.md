# q79 SM Renormalized Time Ordering and Local QME Anomaly Cohomology Theorem v1

Date: 2026-07-24

## Status

**Closed at the local formal-perturbative Epstein-Glaser, anomaly-obstruction,
and renormalized-QME tier on the declared on-shell q79 background charts.**

The result is a theorem about formal power series of local observables. It is
not a convergent path integral, a nonperturbative Standard Model, or a positive
physical Hilbert-space construction.

The executable certificate is:

`certificates/q79_sm_renormalized_timeordering_local_qme.certificate.json`.

It passes 62 of 62 checks.

## 1. Anti-loop boundary

The preceding certificates already establish:

1. the selected q79 framed globally hyperbolic Lorentzian spacetime;
2. the rank-48 three-family chiral Standard-Model bundle;
3. the faithful group
   \(G=S(U(3)\times U(2))\cong
   (SU(3)\times SU(2)\times U(1))/\mathbb Z_6\);
4. one Higgs doublet and the four gauge-covariant Yukawa channels;
5. the nonlinear classical BRST differential and classical BV master action;
6. the background-gauge Green-hyperbolic free complex;
7. its advanced and retarded propagators;
8. the microcausal Peierls algebra and free Hadamard star product.

This theorem does not rebuild any of those objects. It begins with their
microcausal BV algebra and performs the first renormalized interacting step.

A46 had also evaluated the familiar anomaly table. The genuinely new operation
here is to insert those exact representation rows into the ghost-number-one
local-QME cohomology, connect the result to the anomalous Master Ward identity,
and evaluate the global spin-bordism obstruction for the already selected
faithful quotient.

## 2. Domain

Let \(O\) be a causally convex relatively compact region of a declared on-shell
q79 Standard-Model background chart. Let

\[
\mathcal F_{\mathrm{loc}}(O)
\subset
\mathcal F_{\mu c}(O)
\]

be the local BV functionals inside the previously constructed microcausal
algebra.

The interaction \(V\) is the local power-counting-renormalizable
Standard-Model gauge, one-Higgs, Yukawa, and scalar-potential functional. It is
compactly supported, or interpreted in the algebraic adiabatic limit.

All quantum expressions belong to a formal ring such as

\[
\mathbb C[[\hbar,g_1,g_2,g_3,Y,\lambda]].
\]

No convergence of this series is asserted. The action coefficients remain
profile coordinates unless separately selected by the upper MTT source.

## 3. Renormalized time-ordered products

The Epstein-Glaser construction gives multilinear maps

\[
T_n^{\mathrm{ren}}:
\mathcal F_{\mathrm{loc}}(O)^{\otimes n}
\longrightarrow
\mathcal F_{\mu c}(O)[[\hbar]].
\tag{3.1}
\]

Away from partial diagonals, causal factorization determines \(T_n\)
recursively from lower orders. On a diagonal, the extension theorem for
distributions of finite scaling degree supplies a local extension. The
renormalization freedom is exactly the freedom in that extension.

The selected prescription is required to satisfy:

1. \(T_0=1\);
2. \(T_1=\mathrm{id}\);
3. graded symmetry;
4. causal factorization;
5. locality and background covariance;
6. the microlocal spectrum condition;
7. unitarity;
8. field independence;
9. the action Ward identity;
10. the scaling-degree bound.

Existence at every finite perturbative order follows from the local
Epstein-Glaser construction on globally hyperbolic backgrounds. Two
prescriptions satisfying these conditions differ by a local
Stueckelberg-Petermann map

\[
Z(0)=0,\qquad Z'(0)=\mathrm{id}.
\tag{3.2}
\]

Thus the choice of prescription is a local normalization convention, not a
new physical fitted parameter.

Define

\[
S(V)=T^{\mathrm{ren}}\exp(iV/\hbar)
\tag{3.3}
\]

and the Bogoliubov map

\[
R_V(F)
=S(V)^{-1}\star
\bigl(S(V)\cdot_T F\bigr).
\tag{3.4}
\]

Equation (3.4) defines the formal interacting local algebra.

## 4. The faithful quotient rows

Use left-handed Weyl fields and the integer normalization \(q_6=6Y\):

\[
\begin{array}{c|c|c|r|r}
\text{field}&SU(3)&SU(2)&q_6&\dim\\ \hline
Q&3&2&1&6\\
u^c&\bar3&1&-4&3\\
d^c&\bar3&1&2&3\\
L&1&2&-3&2\\
e^c&1&1&6&1\\
N^c&1&1&0&1.
\end{array}
\tag{4.1}
\]

The dimension is 16 per family and 48 for three families.

Let \(t_3\) be \(1,-1,0\) for \(3,\bar3,1\), and let \(p_2\) be 1 for an
\(SU(2)\) doublet and 0 for a singlet. Descent to the faithful quotient is the
congruence

\[
2t_3+3p_2+q_6=0\pmod 6.
\tag{4.2}
\]

For the rows in (4.1), the six left sides are

\[
6,\ -6,\ 0,\ 0,\ 6,\ 0.
\tag{4.3}
\]

Every row therefore descends to the same
\((SU(3)\times SU(2)\times U(1))/\mathbb Z_6\) group. This matters because the
later global-anomaly calculation must use the actual global gauge group, not
only its Lie algebra.

## 5. Local QME anomaly

The renormalized BV formalism replaces the singular formal BV Laplacian by the
finite anomaly map in the anomalous Master Ward identity. Schematically,

\[
\frac12
\{S_0+V,S_0+V\}_{T_{\mathrm{ren}}}
-\Delta_V(V)=0.
\tag{5.1}
\]

The possible breaking

\[
\mathcal A(V)=\Delta_V(V)
\tag{5.2}
\]

is:

- local and covariant;
- of ghost number \(+1\);
- of order \(O(\hbar)\);
- constrained by the extended Wess-Zumino relation
  \(s\mathcal A=0\) modulo total derivatives.

Its nontrivial part therefore lies in

\[
H_{\mathrm{loc}}^{1,4}(s\mid d).
\tag{5.3}
\]

At the four-dimensional power-counting-renormalizable internal-gauge tier,
the potentially nonzero coefficients are:

\[
\begin{array}{c|c}
\text{coefficient}&\text{six-form term}\\ \hline
A_{333}&\operatorname{tr}(F_3^3)\\
A_{33Y}&F_Y\operatorname{tr}(F_3^2)\\
A_{22Y}&F_Y\operatorname{tr}(F_2^2)\\
A_{YYY}&F_Y^3\\
A_{\mathrm{grav}\,\mathrm{grav}\,Y}&
F_Yp_1(TO).
\end{array}
\tag{5.4}
\]

There is no \(SU(2)^3\) coefficient because \(SU(2)\) has no invariant
symmetric cubic tensor. Terms with one nonabelian generator and two
hypercharge factors vanish by tracelessness. Terms mixing distinct
semisimple factors vanish by tensor-product trace factorization. The Higgs,
gauge, and FP-ghost blocks are nonchiral and add no chiral matter anomaly.

## 6. Exact coefficient calculation

Normalize the fundamental twice-Dynkin index to 1. Per family, the six row
contributions are:

\[
\begin{array}{c|rrrrr}
 &A_{333}&A_{33Y}&A_{22Y}&A_{YYY}&
A_{\mathrm{grav}\,\mathrm{grav}\,Y}\\ \hline
Q   & 2&  2& 3&   6&  6\\
u^c &-1& -4& 0&-192&-12\\
d^c &-1&  2& 0&  24&  6\\
L   & 0&  0&-3& -54& -6\\
e^c & 0&  0& 0& 216&  6\\
N^c & 0&  0& 0&   0&  0.
\end{array}
\tag{6.1}
\]

Hence

\[
\begin{aligned}
A_{333}&=2-1-1=0,\\
A_{33Y}&=2-4+2=0,\\
A_{22Y}&=3-3=0,\\
A_{YYY}&=6-192+24-54+216=0,\\
A_{\mathrm{grav}\,\mathrm{grav}\,Y}
&=6-12+6-6+6=0.
\end{aligned}
\tag{6.2}
\]

The certificate evaluates (6.1)-(6.2) over exact integers. Cancellation holds
already per family, so the exact three-family class vector is

\[
\boxed{(0,0,0,0,0)}.
\tag{6.3}
\]

No measured coupling, mass, mixing angle, or threshold value enters this
calculation.

## 7. Removal of the local obstruction

The local BRST cohomology theorem separates a QME breaking into:

\[
\mathcal A
=
\sum_i a_i\mathcal A_i^{\mathrm{nontrivial}}
+sB+dC.
\tag{7.1}
\]

Equation (6.3) gives \(a_i=0\) for every nontrivial gauge-anomaly
representative in (5.4). The remainder \(sB+dC\) is removed by a finite local
counterterm, equivalently by a Stueckelberg-Petermann normalization change.

The Adler-Bardeen theorem then supplies a subtraction scheme in which
one-loop cancellation persists to all perturbative orders. Its application
here is at the theorem's formal, truncation-by-truncation level. It does not
prove convergence of the perturbation series.

Consequently, one may choose \(T^{\mathrm{ren}}\) so that the renormalized QME
holds order by order:

\[
\frac12
\{S_0+V,S_0+V\}_{T_{\mathrm{ren}}}
-\Delta_V(V)=0.
\tag{7.2}
\]

This is an existence theorem for a compatible local subtraction scheme. It
does not claim that every arbitrary renormalization prescription satisfies
(7.2) without finite normalization.

## 8. Quantum BRST cohomology

In the QME scheme, the renormalized quantum-BV differential

\[
\widehat s_V
\tag{8.1}
\]

is well defined and satisfies

\[
\widehat s_V^2=0.
\tag{8.2}
\]

The interacting physical local-observable algebra is therefore

\[
\mathfrak A_{\mathrm{phys,int}}(O)
=H^0\!\left(
\widehat s_V,\mathfrak A_{\mathrm{int}}(O)
\right).
\tag{8.3}
\]

Compactly supported changes of gauge-fixing fermion act by quantum BV
canonical maps. Because the QME anomaly class vanishes, these maps induce
isomorphisms of (8.3). This is formal interacting gauge-fixing independence.

Equation (8.3) defines the algebraic physical sector. It does not prove that
this cohomology has a preferred positive Hilbert-space representation.

## 9. Global anomaly obstruction

The local QME sees infinitesimal gauge transformations. A separate global
test is required for the faithful quotient.

There are four weak doublets per family:

\[
3Q+L=4,
\tag{9.1}
\]

and therefore 12 for three families. The familiar Witten parity is zero.

More strongly, the spin-bordism computation for the exact selected group gives

\[
\Omega^{\mathrm{Spin}}_5
\left(
B\bigl((SU(3)\times SU(2)\times U(1))/\mathbb Z_6\bigr)
\right)
=0.
\tag{9.2}
\]

Combining (9.2) with the local cancellation in (6.3) removes the residual
spin global gauge-anomaly bordism obstruction on the declared orientable spin
category.

This does not choose a preferred numerical phase convention for every
fermion determinant. It proves absence of the obstruction to a consistent
choice. Nonspin, unorientable, and boundary-anomaly extensions are outside
the theorem.

## 10. Theorem

**Theorem.** On every declared on-shell q79 Standard-Model background chart
with the faithful \(\mathbb Z_6\)-quotient bundle and admissible
power-counting-renormalizable kinetic signs:

1. local covariant Epstein-Glaser time-ordered products exist to every finite
   perturbative order;
2. they define a formal interacting Bogoliubov algebra;
3. the ghost-number-one local gauge-anomaly class is represented by the five
   coefficients in (5.4);
4. the exact selected three-family carrier gives the zero vector (6.3);
5. local QME breakings are therefore removable by finite local counterterms;
6. the Adler-Bardeen theorem supplies an all-orders formal subtraction scheme
   satisfying the renormalized QME;
7. the resulting quantum-BV differential is nilpotent;
8. interacting physical local observables are its ghost-number-zero
   cohomology;
9. compactly supported gauge-fixing changes induce isomorphic cohomologies;
10. the global spin gauge-anomaly bordism obstruction also vanishes for the
    faithful quotient.

The theorem adds no physical parameter.

## 11. What remains open

This theorem does not close `B.QFT.02` overall. The remaining hard clauses are:

- a positive physical interacting state or representation theorem;
- an explicit state-selection rule for the physical q79 background;
- numerical RG evolution and matching from selected upper action data;
- uncertainty transport to observable predictions;
- an infrared scattering/adiabatic-limit construction where required;
- nonperturbative completion or convergence;
- observable comparison with experiment.

`B.ACTION.01` remains open because the upper q79 source has not selected every
physical action coefficient and global vacuum datum.

An explicit determinant-phase convention is also not constructed, although
the spin-bordism obstruction to such a choice is zero.

## 12. Parameter ledger

\[
\begin{array}{l|c}
\text{new physical continuous parameters}&0\\
\text{new physical discrete selectors}&0\\
\text{new fits}&0\\
\text{new observed inputs}&0.
\end{array}
\]

The renormalization prescription is a local normalization choice inside the
Stueckelberg-Petermann orbit. Physical predictions must be scheme independent
after matching; that later numerical matching is not performed here.

## 13. Frontier delta

Before this theorem, the q79 Standard-Model construction stopped at a
gauge-fixed free microcausal BV algebra.

After this theorem:

- the renormalized local interaction algebra exists formally;
- its complete power-counting gauge-anomaly vector is exact and zero;
- a local all-orders QME normalization scheme exists;
- the interacting quantum-BV cohomology domain is defined;
- formal gauge-fixing independence is available;
- the faithful quotient's spin global-anomaly obstruction is zero.

The frontier has therefore moved from "construct renormalized interactions and
test their anomaly" to "construct positive physical states and execute
selected RG/matching and observable comparison."

## 14. Primary mathematical context

Local causal renormalization and scaling-degree extension:

- R. Brunetti and K. Fredenhagen,
  *Microlocal Analysis and Interacting Quantum Field Theories*,
  <https://arxiv.org/abs/math-ph/9903028>.

Renormalized BV products, the anomalous Master Ward identity, and the quantum
BV operator:

- K. Fredenhagen and K. Rejzner,
  *Batalin-Vilkovisky formalism in perturbative algebraic quantum field
  theory*, <https://arxiv.org/abs/1110.5232>.

Local ghost-number-one BRST cohomology:

- G. Barnich, F. Brandt, and M. Henneaux,
  *Local BRST cohomology in gauge theories*,
  <https://arxiv.org/abs/hep-th/0002245>.

Locally covariant chiral anomalies:

- J. Zahn, *Locally covariant chiral fermions and anomalies*,
  <https://arxiv.org/abs/1407.1994>.

All-orders gauge-anomaly cancellation:

- D. Anselmi,
  *Adler-Bardeen theorem and cancellation of gauge anomalies to all orders in
  nonrenormalizable theories*, <https://arxiv.org/abs/1501.07014>.

Global anomalies for the faithful Standard-Model quotient:

- J. Davighi, B. Gripaios, and N. Lohitsiri,
  *Global anomalies in the Standard Model(s) and Beyond*,
  <https://arxiv.org/abs/1910.11277>.

## 15. Reproduction

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```
