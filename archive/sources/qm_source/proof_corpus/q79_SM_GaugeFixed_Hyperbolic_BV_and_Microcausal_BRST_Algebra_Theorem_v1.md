# q79 SM Gauge-Fixed Hyperbolic BV and Microcausal BRST Algebra Theorem v1

Date: 2026-07-23

## Status

**Closed on an on-shell q79 background-field perturbative chart at the
gauge-fixed hyperbolic free-BV and microcausal BRST-algebra tier.**

This theorem performs the next operation after the continuum classical BV
composition. It:

1. consumes A57's already closed gauge, ghost, left-Weyl and one-Higgs
   fluctuation slots;
2. realizes those slots as Lorentzian differential operators on the selected
   q79 globally hyperbolic spacetime;
3. proves the background Feynman-'t Hooft gauge principal operator is normally
   hyperbolic;
4. adds the antighost and Nakanishi-Lautrup fields as an explicit acyclic BRST
   doublet;
5. obtains advanced and retarded Green operators;
6. defines the microcausal Peierls algebra, free Hadamard star product and
   ghost-number-zero free BRST cohomology.

It does not construct renormalized interacting time-ordered products, solve
the local quantum master equation, prove interacting gauge independence, or
construct a positive physical interacting state.

The executable certificate is:

`certificates/q79_sm_gaugefixed_hyperbolic_bv_microcausal.certificate.json`.

It passes 46 of 46 checks.

## 1. Anti-loop boundary

A57 already establishes the Standard-Model fluctuation complex at the
structural and heat-index level:

\[
\text{gauge one-forms}
\oplus
\text{FP ghosts}
\oplus
\text{left-Weyl matter}
\oplus
\text{one complex Higgs doublet}.
\]

It also derives

\[
b=\left(\frac{41}{10},-\frac{19}{6},-7\right)
\]

and proves that assigning one common internal determinant to every block only
translates the one-loop matching scale. This theorem does not rederive or
rename either A57 result.

The new result is the missing Lorentzian hyperbolic and microlocal
realization. A57's Euclidean/heat-index data are used only for the block
ledger and signs. No global Wick-rotation equivalence or equality between
Euclidean determinants and Lorentzian amplitudes is asserted.

## 2. Perturbative domain

Let \(O\) be a causally convex globally hyperbolic object of the selected q79
framed category. Let

\[
(\bar A,\bar H,\bar\psi=0)
\]

be a smooth on-shell background for the profile-form classical action on the
restricted faithful \(G=S(U(3)\times U(2))\) bundle.

The background is chart data. It is not claimed to be:

- the selected cosmic gauge-bundle sector;
- a selected Higgs vacuum;
- a prediction of electroweak symmetry breaking;
- a numerical mass or coupling source.

Local trivial symmetric-phase charts \((\bar A,\bar H)=(0,0)\) are included.
The on-shell hypothesis is what makes the linearized gauge generator and
quadratic BV operator form a compatible complex.

## 3. Nonminimal field bundle

The perturbative fields are

\[
\Phi=(a,h,\psi,\bar\psi,c,\bar c,b),
\]

where:

\[
\begin{array}{c|c|c}
\text{field}&\text{ghost number}&\text{bundle}\\ \hline
a&0&\Omega^1(O,\operatorname{ad}P)\\
h&0&\Gamma(O,E_H)\\
\psi,\bar\psi&0&
\Gamma(O,S^+\otimes E_{\rm chiral})\text{ and its dual}\\
c&1&\Omega^0(O,\operatorname{ad}P)\\
\bar c&-1&\Omega^0(O,\operatorname{ad}P)\\
b&0&\Omega^0(O,\operatorname{ad}P).
\end{array}
\]

The exact component ledger is:

- gauge one-form: \(4\cdot12=48\) real components;
- Higgs fluctuation: 4 real components;
- left-Weyl matter: \(2\cdot48=96\) complex components;
- ghost, antighost and auxiliary field: 12 adjoint components each.

These are off-shell bundle ranks, not physical polarization counts.

## 4. Linearized BRST differential

Let \(R_{\bar H}\) be the infinitesimal gauge action on the Higgs background.
The free nonminimal BRST differential is

\[
\begin{aligned}
s_0a&=\bar D c,&
s_0h&=-\rho(c)\bar H,\\
s_0\psi&=-\rho(c)\bar\psi=0,&
s_0c&=0,\\
s_0\bar c&=b,&
s_0b&=0.
\end{aligned}
\tag{4.1}
\]

The certificate writes (4.1) as an exact matrix on five rational Fourier
covectors, including a null covector. It obtains

\[
s_0^2=0
\]

for every witness.

The nonminimal pair has matrices

\[
s_{\rm nm}=
\begin{pmatrix}0&0\\1&0\end{pmatrix},
\qquad
h_{\rm nm}=
\begin{pmatrix}0&1\\0&0\end{pmatrix}
\]

on \((\bar c,b)\). They satisfy

\[
s_{\rm nm}h_{\rm nm}+h_{\rm nm}s_{\rm nm}=I_2.
\tag{4.2}
\]

Thus \((\bar c,b)\) is contractible and contributes no BRST cohomology.

## 5. Background Feynman-'t Hooft gauge

Use the background-covariant gauge condition

\[
\mathcal G(a,h)
=\bar D^\mu a_\mu-R_{\bar H}^\dagger h
\tag{5.1}
\]

and gauge-fixing fermion

\[
\Psi_\xi
=\int_O
\left\langle
\bar c,\mathcal G(a,h)+\frac{\xi}{2}b
\right\rangle d\mathrm{vol}_g.
\tag{5.2}
\]

The calculation representative is \(\xi=1\). This is a gauge choice, not a
physical parameter.

The derivative gauge-Higgs mixing from the covariant Higgs kinetic term has
coefficient \(+1\). The cross term from (5.1) has coefficient \(-1\). The
certificate verifies their exact sum is zero.

A change of \(\xi\) is free-classically BRST exact:

\[
\frac{\partial S_{\rm gf}}{\partial\xi}
=s_0\left[
\frac12\int_O\langle\bar c,b\rangle d\mathrm{vol}_g
\right].
\tag{5.3}
\]

Both sides have exact coefficient \(1/2\). Equation (5.3) proves independence
of the free classical cohomology representative. It is not yet the
interacting quantum gauge-independence theorem.

## 6. Exact principal-symbol calculation

For a covector \(k\), the mixed-index principal symbol of the ungauge-fixed
Yang-Mills Hessian is

\[
\sigma_{\rm YM}(k)^\mu{}_\nu
=k^2\delta^\mu{}_\nu-k^\mu k_\nu.
\tag{6.1}
\]

At \(\xi=1\), gauge fixing contributes

\[
\sigma_{\rm gf}(k)^\mu{}_\nu
=k^\mu k_\nu.
\tag{6.2}
\]

Therefore

\[
\sigma_{\rm YM+gf}(k)^\mu{}_\nu
=k^2\delta^\mu{}_\nu.
\tag{6.3}
\]

The certificate evaluates (6.1)-(6.3) exactly over \(\mathbb Q\) on five
covectors for signature \(+---\). Every non-null symbol has rank four and the
null witness has rank zero. Equation (6.3), not merely the sample, is an
algebraic identity because the two longitudinal tensors cancel coefficient by
coefficient.

The ghost and Higgs operators have the same scalar wave principal symbol.
The fermion operator has the Lorentzian Dirac symbol certified in the previous
q79 continuum theorem. Background curvature, Higgs masses and Yukawa
background masses are zeroth order and do not alter the characteristic cone.

## 7. Hyperbolic operator complex

After eliminating the algebraic \(b\) field, the dynamical blocks are:

\[
\begin{aligned}
P_1&=-\bar D^2\delta_\mu{}^\nu
     -2\,\operatorname{ad}(\bar F_\mu{}^\nu)
     +\text{Higgs-background zeroth-order terms},\\
P_{\rm gh}&=-\bar D^2+R_{\bar H}^\dagger R_{\bar H},\\
P_H&=-\bar D^2+\operatorname{Hess}V|_{\bar H}
     +\text{gauge-background zeroth-order terms},\\
D_{\bar A,\bar H}&=\text{the background Dirac-Yukawa operator}.
\end{aligned}
\tag{7.1}
\]

The first three are normally hyperbolic and the last is Dirac type. Hence
each block has unique advanced and retarded Green operators

\[
E_i^\pm
\]

with causal support. Their graded direct sum defines the causal propagator

\[
\Delta_{\rm gf}=E^-_{\rm gf}-E^+_{\rm gf}.
\tag{7.2}
\]

The antighost/auxiliary doublet is treated algebraically before forming
(7.2).

## 8. Microcausal functional algebra

Let \(\mathcal F_{\mu c}(O)\) be the graded compactly supported smooth
functionals on the gauge-fixed dynamical field space after algebraic
elimination of \(b\). Polynomial antifield dependence may be retained as BV
source directions, but antifields are not propagated. In the dynamical field
arguments, the \(n\)-th functional derivatives satisfy

\[
\operatorname{WF}(F^{(n)})
\cap
\left(
\bar V_+^n\cup\bar V_-^n
\right)
=\varnothing.
\tag{8.1}
\]

The graded Peierls bracket is

\[
\{F,G\}_{\rm P}
=\left\langle
F^{(1)},\Delta_{\rm gf}G^{(1)}
\right\rangle.
\tag{8.2}
\]

The microlocal composition theorem makes (8.2) well defined and closes
\(\mathcal F_{\mu c}(O)\) under the bracket.

For a compatible graded Hadamard two-point choice \(H\), define

\[
F\star_HG
=m\circ
\exp(\hbar\Gamma_H)(F\otimes G).
\tag{8.3}
\]

This is the formal free star algebra. Different Hadamard choices give
isomorphic free algebras through the standard normal-ordering map; no
preferred state is selected.

The free BRST differential acts as a square-zero graded derivation of the
microcausal algebra. The free physical algebra is

\[
\mathfrak A_{\rm phys}^{(0)}(O)
=H^0\!\left(s_0,\mathcal F_{\mu c}(O)[[\hbar]]\right).
\tag{8.4}
\]

The ghost-extended algebra is not itself a positive Hilbert-space
representation. Positivity after physical cohomology remains a separate
theorem.

## 9. Local covariance and time-slice

Background-, spin-lift- and faithful-bundle-preserving embeddings intertwine
the operators (7.1) and their Green operators. They therefore induce
covariant maps on \(\mathcal F_{\mu c}\), the Peierls bracket, the free star
algebra and BRST cohomology.

If the embedding contains a Cauchy surface, Green hyperbolicity yields the
free time-slice isomorphism. This statement is on the selected q79 background
category. It is not a universal theory on every Lorentzian spacetime.

## 10. Theorem

**Theorem.** On every declared on-shell background chart of the selected q79
Lorentzian Standard-Model field stack:

1. the background Feynman-'t Hooft gauge cancels the derivative
   gauge-Higgs mixing;
2. the gauge, ghost and Higgs Hessians are normally hyperbolic and the
   fermion Hessian is Dirac type;
3. the nonminimal free BRST differential squares to zero;
4. the antighost/Nakanishi-Lautrup pair is contractible;
5. the dynamical complex has unique advanced and retarded Green operators;
6. those propagators define a locally covariant microcausal Peierls algebra
   and free Hadamard star algebra;
7. ghost-number-zero free BRST cohomology defines the free physical
   observable domain;
8. changing the free gauge parameter changes the representative by a
   BRST-exact term.

The theorem adds no physical parameter. It does not establish the
renormalized interacting QME or interacting physical state space.

## 11. Exact certificate

The 46 checks comprise:

- 7 source and prior-tier checks;
- 7 A57-consumption checks;
- 10 principal-symbol checks;
- 8 free-BRST and doublet checks;
- 5 primary-theorem registration checks;
- 9 hyperbolic/microcausal construction and guardrail checks.

The exact witness contains:

- five rational covectors and their metric squares;
- the Maxwell, gauge-fixing and combined symbols;
- ranks on null and non-null covectors;
- five square-zero BRST mode matrices;
- the explicit doublet contracting homotopy;
- the exact gauge-Higgs mixing cancellation;
- the exact BRST-exact \(\xi\)-variation coefficient;
- A57's unchanged beta vector.

## 12. Blocker delta

Newly closed `B.QFT.02` clauses:

- A57-to-q79 Lorentzian fluctuation-block interface;
- gauge-fixed hyperbolic free BV complex;
- advanced and retarded propagators;
- microcausal Peierls and free star algebra;
- free ghost-number-zero BRST cohomology domain;
- free classical gauge-parameter independence.

Still open:

- renormalized interacting time-ordered products;
- local QME anomaly classification and counterterms;
- interacting Ward identities;
- interacting gauge-fixing independence;
- positive physical interacting states;
- RG/matching and uncertainty transport;
- nonperturbative completion.

`B.QFT.02` therefore remains open, but the next proof starts at the
renormalized interaction, not at gauge fixing or propagator construction.

`B.ACTION.01` also remains open because the physical global background and
strict action coefficients have not been selected by the upper q79 source.

## 13. Parameter ledger

\[
\begin{array}{l|c}
\text{new physical continuous parameters}&0\\
\text{new physical discrete selectors}&0\\
\text{new fits}&0\\
\text{new observed values}&0
\end{array}
\]

The gauge representative \(\xi=1\) and the on-shell perturbative background
are calculation-domain data, not physical fitted parameters.

## 14. Primary mathematical context

The gauge-complex and Green-hyperbolic construction follows Hack and
Schenkel, *Linear bosonic and fermionic quantum gauge theories on curved
spacetimes*, <https://arxiv.org/abs/1205.3484>.

The microcausal domain and local causal perturbation framework follow
Brunetti and Fredenhagen, *Microlocal Analysis and Interacting Quantum Field
Theories*, <https://arxiv.org/abs/math-ph/9903028>.

The later renormalization freedom is governed by the
Stueckelberg-Petermann framework of Brunetti, Duetsch and Fredenhagen,
<https://arxiv.org/abs/0901.2038>.

The classical-to-quantum BV boundary remains the one formulated by Rejzner,
<https://arxiv.org/abs/1111.5130>, and the stronger interacting gauge-theory
exit is exemplified by Hollands,
<https://arxiv.org/abs/0705.3340>.

## 15. Reproduction

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```
