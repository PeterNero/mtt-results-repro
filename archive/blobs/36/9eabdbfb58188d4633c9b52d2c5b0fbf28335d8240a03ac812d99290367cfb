# q79 SM Gauge-Fixed Hyperbolic BV and Equicausal BRST Algebra Theorem v2

Date: 2026-07-24

## Status

**Closed on each declared on-shell q79 background chart at the
gauge-fixed Green-hyperbolic free-BV and equicausal BRST-algebra tier.**

This theorem supersedes the functional-domain clauses of
`q79_SM_GaugeFixed_Hyperbolic_BV_and_Microcausal_BRST_Algebra_Theorem_v1`.
The v1 principal-symbol, Green-operator, BRST-doublet and gauge-parameter
calculations remain valid. The correction is that unrestricted microcausal
functionals are not, in general, closed under the Peierls bracket and are not
known to satisfy time-slice through the standard chain homotopy.

The active functional domain is now the equicausal subcomplex
\(\mathcal F_{\rm ec}\).

The executable certificate is:

`certificates/q79_sm_gaugefixed_hyperbolic_bv_equicausal.certificate.json`.

It passes 54 of 54 checks.

## 1. Why v2 is required

The v1 theorem used the traditional statement

\[
\mathcal F_{\mu c}
\text{ is closed under the Peierls bracket}.
\]

Hawkins, Rejzner and Visser give an explicit counterexample: even for one
fixed linear Green-hyperbolic operator, the Peierls bracket of regular
functionals can fail to be a smooth functional. They also show that the
usual microcausal complex is not closed under the chain homotopy used for
time-slice.

This is directly applicable to the v1 setup because that setup also fixes a
linearized Green-hyperbolic operator on each background chart. Restricting
to a fixed background therefore does not remove the counterexample.

The repair is not to abandon microlocal control. It is to strengthen it from
a pointwise wavefront condition to an equicontinuous family condition.

Primary source:

- E. Hawkins, K. Rejzner and B. Visser, *A novel class of functionals for
  perturbative algebraic quantum field theory*, arXiv:2312.15203v3.

## 2. Preserved q79 input

Let \(O\) be a causally convex relatively compact region of the selected q79
globally hyperbolic framed Lorentzian spacetime. Restrict the selected spin
structure and faithful

\[
G=S(U(3)\times U(2))
\]

bundle to \(O\), and choose a smooth on-shell perturbative background

\[
(\bar A,\bar H,\bar\psi=0).
\]

The following v1 conclusions are unchanged:

1. background Feynman-'t Hooft gauge cancels derivative gauge-Higgs mixing;
2. the gauge, ghost and Higgs Hessians are normally hyperbolic;
3. the fermion Hessian is Dirac type;
4. the nonminimal BRST differential squares to zero;
5. the \((\bar c,b)\) pair is contractible;
6. the dynamical blocks have unique advanced and retarded Green operators;
7. changing the free gauge parameter changes the action by an \(s_0\)-exact
   term.

The exact rational witnesses for these statements are retained without
alteration.

## 3. Ambient microcausal class

Let \(\mathcal E\) be the graded configuration space after algebraic
elimination of \(b\). The ambient microcausal condition is

\[
\operatorname{WF}\!\left(F^{(n)}(\phi)\right)
\cap
\left(\bar V_+^n\cup\bar V_-^n\right)
=\varnothing.
\tag{3.1}
\]

Condition (3.1) remains useful. It controls distributional products at a
fixed configuration. It is not, by itself, sufficient to control how the
derivatives vary as \(\phi\) moves through configuration space.

Accordingly, this theorem retains \(\mathcal F_{\mu c}\) only as an ambient
wavefront class. It makes no closure or time-slice claim for all of
\(\mathcal F_{\mu c}\).

## 4. Equicausal domain

For every compact configuration set \(C\subset\mathcal E\), every derivative
order \(n\), and the prescribed open wavefront cone \(\Gamma_n\), extend

\[
F^{(n)}(\phi)
\]

continuously to the corresponding distribution space
\(\mathcal D'_{\Gamma_n}\). A compactly supported microcausal functional is
**equicausal** when

\[
\left\{
\widetilde F^{(n)}(\phi):\phi\in C
\right\}
\]

is an equicontinuous family of linear maps for every \(C\) and \(n\).

Write the resulting space as

\[
\mathcal F_{\rm ec}(O).
\]

This condition is strong enough to:

- integrate derivatives along configuration-space curves without creating
  uncontrolled singularities;
- apply the Leibniz rules required by the Peierls bracket and star product;
- preserve the chain homotopy used in the time-slice proof.

Local functionals, Wick polynomials and their multilocal products lie in the
equicausal class.

## 5. Application to the q79 field stack

The q79 perturbative field carrier is a finite direct sum of vector bundles:

\[
\Omega^1(O,\operatorname{ad}P)
\oplus\Gamma(O,E_H)
\oplus\Gamma(O,S^+\otimes E_{\rm chiral})
\oplus\text{ghost and antifield directions}.
\]

Wavefront sets of vector-bundle-valued distributions are defined
componentwise and are invariant under smooth changes of local frame. The
equicausal theorem is formulated for arbitrary finite-rank vector bundles
and for multivector fields.

The polynomial ghost and antifield directions and finite CAR factors do not
add new spacetime wavefront cones. The locally covariant BV grading is
carried by the prior Rejzner/Hollands construction. Thus the equicausal
condition applies componentwise to the finite q79 SM bundle and its BV
multivector complex.

This is a local perturbative statement. It is not a construction of a global
interacting Hilbert space.

## 6. Peierls and star products

Let

\[
\Delta_{\rm gf}=E^-_{\rm gf}-E^+_{\rm gf}
\]

be the graded causal propagator of the gauge-fixed free complex. On
\(\mathcal F_{\rm ec}(O)\), define

\[
\{F,G\}_{\rm P}
=
\left\langle F^{(1)},\Delta_{\rm gf}G^{(1)}\right\rangle.
\tag{6.1}
\]

For a compatible graded Hadamard two-point function \(H\), define

\[
F\star_HG
=
m\circ\exp(\hbar\Gamma_H)(F\otimes G).
\tag{6.2}
\]

The equicausal closure theorem gives

\[
\{\,\mathcal F_{\rm ec},\mathcal F_{\rm ec}\,\}_{\rm P}
\subseteq\mathcal F_{\rm ec}
\]

and

\[
\mathcal F_{\rm ec}[[\hbar]]
\star_H
\mathcal F_{\rm ec}[[\hbar]]
\subseteq
\mathcal F_{\rm ec}[[\hbar]].
\]

The free BRST differential is a square-zero graded derivation on this
domain. The corrected free physical observable algebra is

\[
\mathfrak A_{\rm phys}^{(0)}(O)
=
H^0\!\left(
s_0,\mathcal F_{\rm ec}(O)[[\hbar]]
\right).
\tag{6.3}
\]

## 7. Time-slice

For a Cauchy embedding \(O\hookrightarrow O'\), the smooth multivector
complex has a chain homotopy constructed from the Green operators. The
equicausal complex is closed under that homotopy. Therefore the inclusion is
a quasi-isomorphism:

\[
H^\bullet\!\left(\mathcal X_{\rm ec}(O),\delta\right)
\cong
H^\bullet\!\left(\mathcal X_{\rm ec}(O'),\delta\right).
\tag{7.1}
\]

Equation (7.1) is the rigorous free time-slice statement used here. The
corresponding statement for the unrestricted microcausal complex is not
asserted.

## 8. Hadamard presentation

Two compatible Hadamard covariances differ by a smooth symmetric kernel
\(w\). With the convention

\[
\Gamma_w
=
\frac12
\left\langle
w,\frac{\delta^2}{\delta\phi^2}
\right\rangle,
\qquad
\beta_w=\exp(\hbar\Gamma_w),
\]

the normal-ordering map satisfies

\[
\beta_w(F\star_HG)
=
\beta_w(F)\star_{H+w}\beta_w(G).
\tag{8.1}
\]

It also obeys

\[
\beta_0=1,\qquad
\beta_{w_2}\beta_{w_1}=\beta_{w_1+w_2},\qquad
\beta_w^{-1}=\beta_{-w}.
\tag{8.2}
\]

Equations (8.1)-(8.2) do not select a preferred Hadamard state. They identify
equivalent presentations once \(H\) and \(H+w\) are given.

## 9. Theorem

**Theorem.** On every declared on-shell q79 background chart:

1. the previously certified gauge-fixed SM fluctuation complex is
   Green-hyperbolic;
2. its free BV functional carrier may be chosen as the equicausal
   multivector complex;
3. local functionals and Wick polynomials belong to this carrier;
4. the Peierls bracket and compatible Hadamard star product close on it;
5. the free BRST differential is a square-zero graded derivation;
6. ghost-number-zero BRST cohomology defines the free physical algebra;
7. Cauchy embeddings induce the equicausal time-slice quasi-isomorphism;
8. smooth changes of Hadamard covariance give star-isomorphic
   presentations.

No physical parameter is added.

## 10. Relation to later q79 results

The later renormalized-QME and formal-state certificates consume:

- the unchanged Green-hyperbolic complex;
- local and multilocal interaction functionals;
- Wick polynomial observables;
- the anomaly-free renormalized BV theorems.

All of those inputs are contained in, or compatible with, the equicausal
successor domain. Their algebraic anomaly, QME, quartet and finite-state
witnesses are not reopened.

This does not claim that the Epstein-Glaser time-ordering operator extends to
every equicausal functional. Its active renormalized domain is the local and
multilocal/Wick subalgebra, which is equicausal and is the domain used by the
downstream interaction theorem.

Their historical references to a closed unrestricted microcausal algebra
must be read through this v2 replacement.

## 11. Claim boundary

Closed:

- q79 gauge-fixed Green-hyperbolic free BV complex;
- equicausal Peierls and Hadamard-star algebra;
- equicausal free BRST cohomology;
- equicausal time-slice;
- Hadamard-seed presentation isomorphism.

Superseded:

- unrestricted microcausal Peierls closure;
- unrestricted microcausal time-slice through the standard homotopy.

Still open at this tier:

- renormalized interacting time ordering and QME, except where closed by the
  later theorem;
- positive physical interacting states, except where closed formally by the
  later local-state theorem;
- fixed-coupling C*-completion;
- literal local quasi-equivalence;
- selected global state and nonperturbative completion.

## 12. Parameter ledger

\[
\begin{array}{l|c}
\text{new physical continuous parameters}&0\\
\text{new physical discrete selectors}&0\\
\text{new fits}&0\\
\text{new observed values}&0
\end{array}
\]

The background, gauge representative and Hadamard covariance are
presentation data, not new physical fit parameters.
