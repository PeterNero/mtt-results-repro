from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = (
    ROOT
    / "revised_tex_vnext"
    / "Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4"
    / "main.tex"
)

TEXT = r"""\documentclass[11pt]{article}
\usepackage{series}

\renewcommand{\PartRoman}{VI}
\hypersetup{
  unicode=true,
  pdftitle={Fixed Points VI: Formal Synthesis and Physical Interpretations},
  pdfauthor={Peter Nero}
}

\title{Fixed Points VI: Formal Synthesis and Physical Interpretations}
\author{Peter Nero}
\date{July 2026}

\begin{document}
\maketitle
\seriestagline

\begin{abstract}
We synthesize the corrected FP--I--V results without promoting their control
parameter, projections, or diagnostics into an unproved fundamental field
theory. The rigorous spine consists of conditional projected fixed-point
existence, strict-Lyapunov promotion to equilibrium, joint-mode damping and
disturbance floors, perturbative persistence of a curved spectral cluster,
curvature leakage, intrinsic first-order centroid modulation, frozen linear
Ornstein--Uhlenbeck covariance, canonical-correlation bounds, and declared
admissibility exits. We distinguish three logical levels throughout:
inherited theorem, conditional model completion, and physical interpretation.
A Lorentzian gauge/gravity action, quantum covariance, particle identities,
merger, measurement, and cosmology belong to the latter two levels unless
additional source and equivalence theorems are supplied. We also correct the
Gaussian Lyapunov sign and nonnormal resolvent bounds, and show why an
instantaneous equal-time bilocal kernel is not microcausal merely because it
leaves the principal symbol unchanged. A local mediator is the consistent
route to causal overlap dynamics.
\end{abstract}

\tableofcontents

\section{Logical levels and common geometry}

Every statement in this synthesis has one of the following statuses.
\begin{description}
\item[Inherited theorem.] A consequence of FP~I--V under hypotheses restated
or cited here.
\item[Conditional completion.] A mathematically specified extra model whose
conclusions hold if that model and its hypotheses are adopted.
\item[Physical interpretation.] A proposed reading that is not established by
the fixed-point theorems alone.
\end{description}

Let $\mathcal H$ be the declared control Hilbert space. The joint internal
operator is constructed from the nil, lens, and shared-circle data using the
strong-commutation and domain hypotheses of FP~II. Its coherent projector
$P$ is the joint spectral projector. A product of three bundle projectors is
permitted only when those projectors strongly commute; otherwise the product
need not be an orthogonal projector. Write $Q=I-P$.

On a curved bundle, the normalized Laplace-type operator is
\[
 L_x=\nabla_x^\ast\nabla_x+\mathcal R_x.
\]
When the selected low cluster remains separated, FP~IV defines the curved
Riesz projector $P_{\mathcal R}(x)$. Retaining the old projector $P$ instead
requires the off-diagonal leakage block $Q\mathcal RP$.

The parameter of the FP gradient flow is a stabilization or control
parameter. Identifying it with Lorentzian proper time, coordinate time, or a
quantum evolution parameter is a conditional completion, not an inherited
theorem.

\section{Fixed-point and equilibrium synthesis}

Let $\Phi_\tau$ be a well-defined time-$\tau$ map for the declared control
flow and set $T=P\Phi_\tau$ on a closed bounded convex set $K\subset\mathcal H$.

\begin{theorem}[Corrected fixed-point chain]\label{thm:fixed-chain}
Assume one of the following FP~I alternatives:
\begin{enumerate}
\item $T(K)\subset K$ and $T:K\to K$ is continuous and compact; or
\item $T(K)\subset K$ and $T$ is continuous and condensing for a declared
measure of noncompactness.
\end{enumerate}
Then $T$ has a fixed point $u_\ast\in K$. This proves
$P\Phi_\tau(u_\ast)=u_\ast$. If, in addition, the trajectory through
$u_\ast$ remains in the projected invariant set and obeys a strict Lyapunov
identity
\[
 \mathcal C(u(\tau))-\mathcal C(u(0))
 =-\int_0^\tau\mathcal D(u(s))\,ds,
 \qquad \mathcal D\ge0,
\]
with $\mathcal D(u)=0$ exactly at equilibria, then $u_\ast$ is an equilibrium
of the declared flow.
\end{theorem}

\begin{proof}
The first conclusion is Schauder's or Darbo--Sadovskii's theorem. At a
projected recurrent point, the Lyapunov values at the two endpoints agree.
The displayed identity forces $\mathcal D=0$ along the intervening orbit, and
strictness gives equilibrium. Without the second step, a projected time-step
fixed point is not automatically a steady solution.
\end{proof}

\begin{proposition}[Conditional contraction uniqueness]\label{prop:unique}
Suppose a steady equation can be written on a specified Banach space as
$u=-A^{-1}N(u)$, where $A^{-1}$ exists on that space and
\[
 \|A^{-1}\|\operatorname{Lip}(N)<1
\]
on an invariant complete subset. Then the steady solution there is unique.
No uniqueness conclusion follows from a vertical spectral gap if $A$ has an
unremoved kernel or if the displayed inverse estimate is not proved.
\end{proposition}

\section{Joint-mode stability and disturbance floors}

Let $\alpha$ be one joint modal label, including multiplicity. After the
one-sided nonlinear estimate, suppose a noncoherent amplitude satisfies
\[
 \frac{d}{dt}|a_\alpha|
 \le-\gamma_\alpha|a_\alpha|+|f_\alpha(t)|,
 \qquad \gamma_\alpha>0.
\]
Then the deterministic input-to-state floor is
$\|f_\alpha\|_\infty/\gamma_\alpha$. For the exact scalar It\^o equation
\[
 da_\alpha=-\gamma_\alpha a_\alpha\,dt
 +\sqrt{q_\alpha}\,dW_\alpha,
\]
the stationary variance is $q_\alpha/(2\gamma_\alpha)$. Deterministic force
amplitude and stochastic power have different units and cannot be represented
by one shared disturbance threshold.

For infinitely many modes, bundlewise stochastic control requires the
appropriate weighted covariance trace; deterministic control requires its
own weighted series. These are sufficient nonlinear stability criteria.
Gaussian invariant laws are asserted only for exact linear OU systems.

\section{Curvature, centroid motion, and interaction}

Let the uncurved noncoherent spectrum start at $\lambda_\ast>0$. If
$\|\mathcal R\|<\lambda_\ast/2$, the selected low spectral cluster remains
separated and has a curved Riesz projector of the same rank. If the uncurved
projector is retained and the one-sided $Q$-sector damping margin is
$\gamma_Q>0$, FP~IV gives the schematic sharp form
\[
 \frac{d}{dt}\|q\|
 \le-\gamma_Q\|q\|+\|Q\mathcal RP\|\,\|p\|+\|QF\|,
\]
and therefore a curvature-induced leakage floor.

For a localized profile inside a strongly convex normal ball, the centroid is
the Karcher mean. A first-order gradient parent flow yields a first-order
modulation equation
\[
 G_{ij}(X)\dot X^j=-\partial_iV_{\rm eff}(X)+\varepsilon_i.
\]
A Newton equation requires a separately declared inertial parent theory.

For two profiles, absolute cross-term control proves only
\[
 |E_{\rm int}|\le C\mathcal O.
\]
Attraction requires $E_{\rm int}\le-c\mathcal O$; repulsion requires the
opposite sign. Even a proved attractive sign does not establish merger,
collapse, or a transition rate without a dynamical connection theorem.

\section{Frozen Gaussian multi-structure theory}

Consider the real linear SDE
\begin{equation}
 d\zeta=A\zeta\,dt+B\,dW_t,
 \qquad Q:=BB^\top .
 \label{eq:linear-sde}
\end{equation}

\begin{theorem}[Semigroup covariance and resolvent bounds]\label{thm:semigroup}
Assume
\[
 \|e^{tA}\|\le M e^{-\omega t},
 \qquad t\ge0,quad M\ge1,quad\omega>0.
\]
Then~\eqref{eq:linear-sde} has stationary covariance
\[
 \Sigma=\int_0^\infty e^{tA}Qe^{tA^\top}\,dt,
\]
which solves
\[
 A\Sigma+\Sigma A^\top+Q=0.
\]
Moreover,
\[
 \|\Sigma\|\le\frac{M^2\|Q\|}{2\omega},
 \qquad
 \|A^{-1}\|\le\frac{M}{\omega}.
\]
\end{theorem}

\begin{proof}
The semigroup estimate makes both integrals converge. Differentiation of the
covariance integrand gives the Lyapunov equation, while
$A^{-1}=-\int_0^\infty e^{tA}\,dt$. Taking norms proves the bounds.
\end{proof}

For a normal $A$, one may often take $M=1$ with $\omega$ given by the spectral
abscissa. For a nonnormal matrix, the spectral abscissa alone does not imply
$\|A^{-1}\|\le1/\omega$ or
$\|\Sigma\|\le\|Q\|/(2\omega)$; transient amplification must be controlled.

Under the block-diagonal damping assumptions of FP~V, the cross covariance
satisfies a Sylvester equation. Canonical correlation is normalized by the
smallest positive eigenvalues of the marginal covariance blocks, not their
largest operator norms.

\section{Classical covariance versus quantum covariance}

The covariance produced by~\eqref{eq:linear-sde} is classical. To interpret it
as a bosonic quantum covariance one must separately specify canonical
commutation relations, a value of $\hbar$, and quantum dynamics whose noise
and damping satisfy the complete-positivity constraints. Only then is
\[
 \Sigma+\frac{i\hbar}{2}\Omega\succeq0
\]
the physical uncertainty condition. Classical positivity of $\Sigma$ does not
imply this inequality.

For a declared bipartite Gaussian quantum state, nonpositivity after partial
transpose certifies entanglement. PPT is exact for the two-mode $1\times1$
case; in general multimode bipartitions PPT need not be sufficient for
separability. These facts classify an already constructed quantum Gaussian
state. They do not quantize the FP control flow or derive particle statistics.

\section{Admissibility and exit}

Let $m_j(x)$, $j\in\mathcal J$, be a finite family of continuous declared
margins: curved cluster separation, one-sided damping, or explicit
deterministic/stochastic performance tolerances. Define
\[
 \mathcal D_\varepsilon
 =\{x:m_j(x)\ge\varepsilon\ \forall j\},
 \qquad
 \mathfrak B(x)=\max_j[-m_j(x)].
\]
Then $x\in\mathcal D_0$ exactly when $\mathfrak B(x)\le0$. Along a continuous
path, a change from $\mathfrak B\le0$ to $\mathfrak B>0$ has a first boundary
time at which $\mathfrak B=0$.

This is an exact exit diagnostic for the declared constraints. It does not
prove that $\mathfrak B$ is a physical energy or force. It does not establish
which state follows exit. A mountain-pass theorem needs an actual energy
functional, and basin selection needs a post-exit evolution or transition
kernel.

For affine observables of a frozen Gaussian system, FP~V supplies finite-grid
and Borell--TIS continuous-time exit estimates. A Lipschitz nonlinear function
of a Gaussian process is not generally Gaussian. Equal-time cross-correlation
can bound simultaneous observed exits, but cannot prove causal propagation or
non-propagation.

\section{Status of a Lorentzian master action}

A local Lorentzian gauge/gravity/matter action may be appended as a
\emph{conditional completion}, for example schematically
\[
 S_{\rm cand}=\int\sqrt{-g}\left[
 \frac{M_{\rm Pl}^2}{2}R-\Lambda
 -\frac14\sum_r\operatorname{tr}F_r^2
 -\sum_a|D\varphi_a|^2-V(\varphi)
 +\sum_b\bar\psi_b(i\gamma^\mu D_\mu-M_b)\psi_b
 \right]d^4x.
\]
The FP~I--V theorems do not select the gauge group, representations, number of
fields, couplings, Yukawa matrices, or potential. Nor do they prove that the
gradient control flow is the Euler--Lagrange evolution of $S_{\rm cand}$.

If a mass term depends on curvature, such as
$M_a^2=m_a^2+\xi_aR$, its metric variation contributes nonminimal terms to
the gravitational field equation; it cannot be inserted while retaining the
minimally coupled Einstein equation unchanged. Likewise, a point-particle
Lorentz-force law requires a controlled localized-solution limit and is not a
consequence of gauge covariance alone.

Three internal structures do not by themselves prove three gauge factors,
bosonic or fermionic statistics, bifundamental matter, the Standard Model
particle assignment, anomaly cancellation, or equivalence with a quantum
field theory. Those require independent representation, source, and matching
theorems.

\section{Bilocal overlap and causality}

Consider an equal-parameter interaction of the form
\[
 \mathcal N[\phi](t,x)
 =\int_{\Sigma_t}K(x,y)|\phi(t,y)|^2\,d\mu_t(y)\,\phi(t,x).
\]

\begin{proposition}[Instantaneous bilocal obstruction]\label{prop:bilocal}
If $K(x,y)$ is nonzero for spatially separated $x$ and $y$, the equation at
$(t,x)$ depends instantaneously on data at $y$. Leaving the differential
principal symbol unchanged is therefore insufficient to prove the usual
local domain-of-dependence property. An $L^1$ bound on $K$ may help local
well-posedness, but it does not establish microcausality.
\end{proposition}

\begin{proof}
Choose two initial data sets that agree near $x$ but differ near a separated
point $y$ where $K(x,y)\ne0$. Their bilocal source values at $(t,x)$ differ at
the same parameter time. Thus the source is not determined by data in an
arbitrarily small causal neighborhood of $x$.
\end{proof}

\begin{proposition}[Local-mediator completion]\label{prop:mediator}
Introduce a local mediator $\chi$ with a hyperbolic equation, for example
\[
 (\Box_g+m_\chi^2)\chi=g_\chi|\phi|^2,
\]
and couple $\chi$ locally back to $\phi$. Under the standard regularity,
gauge, and constraint hypotheses for the resulting local hyperbolic system,
its domain of dependence is governed by the local characteristics. Eliminating
$\chi$ with a retarded Green operator produces a causal retarded memory
kernel, not in general a symmetric equal-time bilocal action.
\end{proposition}

This local parent theory is the preferred route if overlap dynamics is meant
to represent physical causal interaction.

\section{Physical interpretation ledger}

\paragraph{Supported within the declared control model.}
The series supports coherent/noncoherent projection under operator-domain
hypotheses, conditional fixed points, strict-Lyapunov equilibrium promotion,
damping estimates and disturbance floors, perturbative curved-cluster
persistence, curvature leakage, intrinsic first-order centroid modulation,
frozen linear covariance, and admissibility exit diagnostics.

\paragraph{Conditional after adding a model.}
Gauge forces, Lorentzian motion, quantum uncertainty, Gaussian entanglement,
decoherence, thermodynamic entropy production, and causal overlap can be
studied after a compatible local Lorentzian or open-quantum model is specified.
Their parameters and consistency conditions are additional data.

\paragraph{Not derived by this series.}
The present theorems do not derive boson/fermion identity, particle masses,
Standard Model representations, merger or collapse rules, the Born rule,
measurement outcomes, emergent time, inflation, horizons, or a cosmological
arrow of time. These may motivate later work but are not conclusions of
FP~I--VI.

\section{Synthesis theorem and remaining obligations}

\begin{theorem}[Scoped FP synthesis]\label{thm:synthesis}
Assume the operator, compactness or condensing, strict-Lyapunov, one-sided
damping, curvature-smallness, covariance, and margin hypotheses stated in
FP~I--V and summarized above. Then the declared control model has:
\begin{enumerate}
\item a projected time-step fixed point, promoted to an equilibrium only by
the strict Lyapunov condition;
\item quantified noncoherent damping and deterministic/stochastic floors;
\item a persistent curved low cluster and a quantified old-projector leakage
term;
\item intrinsic first-order centroid modulation under the modulation
hypotheses;
\item exact stationary covariance for the frozen linear OU sector and
correctly normalized correlation bounds; and
\item exact detection, plus conditional Gaussian probability bounds, for
exit from a declared admissible domain.
\end{enumerate}
No Lorentzian, quantum, particle-physics, merger, measurement, or cosmological
claim follows without its additional completion theorem.
\end{theorem}

The principal remaining obligations for a physical theory are therefore
constructive rather than interpretive: select the physical state space and
operator from MTT geometry; derive a local causal action or evolution; prove
the relation between its solutions and the FP control flow; derive field
content and couplings; and establish empirical matching without importing the
target observables as source data.

\section{Conclusion}

The corrected Fixed Points series is a coherent conditional control and
spectral framework. Its strongest results concern existence under explicit
compactness hypotheses, stability margins, curved spectral persistence,
leakage, modulation, Gaussian covariance, and admissibility diagnostics. FP~VI
does not weaken those results by surrounding them with broader interpretations;
it identifies exactly what they prove and exactly which bridges remain before
they can support a fundamental spacetime, quantum, or particle theory.

\begin{thebibliography}{99}

\bibitem{FPI}
P.~Nero,
\newblock \emph{Fixed Points I: Fixed Points over Multi--Bundle Manifolds},
\newblock revised v6, 2026.

\bibitem{FPII}
P.~Nero,
\newblock \emph{Fixed Points II: Fixed Points in a 10D Modal Model},
\newblock revised v3, 2026.

\bibitem{FPIII}
P.~Nero,
\newblock \emph{Fixed Points III: Disturbance--Damping Balance and Stability},
\newblock revised v4, 2026.

\bibitem{FPIV}
P.~Nero,
\newblock \emph{Fixed Points IV: Curvature, Centroid Motion, and Structural
Transitions on Bundle Manifolds},
\newblock revised v4, 2026.

\bibitem{FPV}
P.~Nero,
\newblock \emph{Fixed Points V: Curvature Coupling, Multi--Structure Dynamics,
and Admissibility Barriers},
\newblock revised v6, 2026.

\bibitem{DaPratoZabczyk}
G.~Da~Prato and J.~Zabczyk,
\newblock \emph{Stochastic Equations in Infinite Dimensions},
\newblock Cambridge University Press, 1992.

\bibitem{SimonPPT}
R.~Simon,
\newblock Peres--Horodecki separability criterion for continuous variable
systems,
\newblock \emph{Physical Review Letters} \textbf{84} (2000), 2726--2729.

\end{thebibliography}

\end{document}
"""


def main() -> None:
    TEX.write_text(TEXT, encoding="utf-8")
    print(f"Updated {TEX}")


if __name__ == "__main__":
    main()
