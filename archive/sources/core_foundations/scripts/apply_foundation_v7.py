from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "revised_tex_vnext" / "Modal_Triplet_Theory__Foundation_v7" / "main.tex"

TEXT = r"""\documentclass[11pt]{article}
\usepackage{series}
\usepackage{mathrsfs}

\title{Modal Triplet Theory: Foundations}
\author{Peter Nero}
\date{July 2026}

\begin{document}
\maketitle
\seriestagline

\begin{abstract}
We give a corrected functional-analytic foundation for Modal Triplet Theory
(MTT). The abstract architecture is a Hilbert bundle with three compatible
vertical structures, a joint coherent spectral projector, a stabilization
flow, and explicitly separate hypotheses for gap, invariance, existence,
contraction, truncation, and admissibility. The canonical physical realization
is a ten-dimensional bundle $M_{10}\to Y_4$ with compact Riemannian fiber
$X_6$; the central circle is bundle data and is not counted as an additional
product dimension. Strong commutation or a single total internal operator is
assumed rather than inferred from notation. Complementary-mode stability uses
a stable-semigroup estimate that remains valid for nonnormal generators.
Projected time-step fixed points are distinguished from equilibria, and
Banach, Schur--Feshbach, projector-stability, and basin-robustness statements
are given with their required domains. Stabilization time, physical time, and
renormalization scale are separated. Selection by reset is identified as a
hybrid law unless derived from continuous upper dynamics. Lorentzian signature
belongs to a hyperbolic principal symbol in a physical completion, not to a
positive Hilbert-space Gram form. A complete admissibility ledger records the
independent obligations inherited by every downstream MTT realization.
\end{abstract}

\tableofcontents

\section{Status, scope, and logical vocabulary}

This paper defines an abstract control and reduction architecture. It does not
derive a particular quantum theory, gauge group, particle spectrum, spacetime
equation, probability law, or numerical constant. Downstream claims must use
one of the following statuses:
\begin{description}
\item[Axiom or assumption.] Input structure of a realization.
\item[Conditional theorem.] A consequence proved from listed hypotheses.
\item[Characterization.] A necessary form for objects satisfying the premises.
\item[Reconstruction or embedding.] Recovery or representation of a known
framework after compatible data are supplied.
\item[Calibration or postdiction.] Numerical agreement using target-related
input or model selection.
\item[Held-out prediction.] A quantity not used in construction, calibration,
scale choice, or branch selection.
\item[Interpretation.] A conceptual reading without theorem status.
\end{description}

The word ``physical'' is reserved for a realization equipped with a selected
state space, local evolution law, observable map, and empirical interpretation.

\section{Dimension-neutral architecture and physical realization}

\subsection{Abstract Hilbert-bundle form}

Let $Y$ be a smooth base and let $\mathscr H\to Y$ be a real or complex
separable Hilbert bundle. A state belongs to a declared Sobolev space
\[
 \mathcal H=H^s(Y;\mathscr H),
\]
with $s$ chosen so that every nonlinear map and operator domain used below is
well defined. The abstract results are dimension neutral.

The modal triplet is represented by three compatible vertical structures
\[
 (\mathcal E_i,A_i,P_i),\qquad i=1,2,3,
\]
on the same internal Hilbert fiber. Here $A_i$ is a nonnegative self-adjoint
vertical operator and $P_i$ is its selected low spectral projector. The
triplet is not automatically a product of three coordinate manifolds.

\subsection{Canonical physical realization}

The canonical physical specialization is
\[
 \pi:M_{10}\longrightarrow Y_4,
 \qquad X_x=\pi^{-1}(x),qquad\dim X_x=6,
\]
where $Y_4$ is a four-dimensional globally hyperbolic Lorentzian base in the physical completion
and each compact fiber $X_x$ is Riemannian. In a local trivialization,
$M_{10}\simeq Y_4\times X_6$. Positive elliptic modal operators act vertically
on $X_6$ and do not create additional causal directions.

If $X_6$ is explicitly factorized as $F_1\times F_2\times F_3$, then
$\sum_i\dim F_i=6$. A shared phase circle is represented by a principal
$U(1)$ bundle or Hermitian line bundle $L_{\rm cen}\to X_6$. It is not appended
as a seventh independent product coordinate. Recursive nil/lens/circle
descriptions may be used as bundle or filtration data, but their dimensions
must not be added unless an actual product decomposition is proved.

\section{Three independent evolution parameters}

The foundation distinguishes:
\begin{enumerate}
\item a stabilization flow $R_\tau$ with control parameter $\tau\ge0$;
\item a physical propagator $U(t_2,t_1)$, supplied only by a selected physical
completion; and
\item a renormalization or coarse-graining scale $\mu$.
\end{enumerate}
No equality among $\tau$, $t$, and $\log\mu$ is assumed. A theorem relating any
two of them must specify the map, units, domain, and approximation error.

We write the stabilization equation as
\[
 \partial_\tau\Psi=F(\Psi),\qquad R_\tau(\Psi_0)=\Psi(\tau).
\]
Well-posedness is imposed on a declared interval and invariant domain; global
well-posedness is not part of the abstract foundation unless proved in a
specific realization.

\section{Joint vertical operator and coherent projector}

\begin{assumption}[Joint spectral structure]\label{ass:joint}
For each base point, the $A_i$ are nonnegative self-adjoint operators whose
spectral measures strongly commute. Their quadratic forms have a common dense
domain. Equivalently, a realization may provide one nonnegative self-adjoint
total internal operator $A_{\rm int}$ directly.
\end{assumption}

Under strong commutation define
\[
 P=\prod_{i=1}^3\mathbf1_{I_i}(A_i),\qquad Q=I-P,
\]
for declared isolated low spectral sets $I_i$. The product is then an
orthogonal projector independent of ordering. Base-only coefficients or
separate variable names do not, by themselves, prove strong commutation.

For harmonic selection one may instead use the form sum
$A_{\rm int}=A_1+A_2+A_3$. Nonnegativity gives
\[
 \ker A_{\rm int}=\bigcap_i\ker A_i,
\]
provided the form sum is well defined. The coherent projector is then the
spectral projector of $A_{\rm int}$ at zero.

\begin{assumption}[Internal gap and Sobolev boundedness]\label{ass:gap}
There is $\lambda_{\rm int}>0$ such that, in quadratic-form sense,
\[
 A_{\rm int}\succeq\lambda_{\rm int}Q,
\]
and $P,Q$ extend boundedly to every Sobolev space used by the dynamics.
\end{assumption}

The internal gap separates the selected fiber cluster from complementary
fiber modes. It does not by itself imply invariance under $R_\tau$, existence
of a fixed point, coherent contraction, suppression of arbitrarily high
four-dimensional energy, or selection of a physical state.

\section{Stable complementary dynamics}

Let $\Psi_\ast$ be a reference state at which the stabilization vector field is
Fr\'echet differentiable, and set $L=DF(\Psi_\ast)$. The stable sign convention
is that $L_{QQ}=QLQ$ generates decay:
\[
 \|e^{\tau L_{QQ}}\|\le M_Qe^{-\omega_Q\tau},
 \qquad M_Q\ge1,quad\omega_Q>0.
 \label{eq:q-semigroup}
\]
This estimate, rather than spectral abscissa alone, is authoritative for a
nonnormal generator.

\begin{proposition}[Gap-to-decay under a bounded perturbation]
Suppose $Q\mathcal H$ is invariant and
\[
 L_{QQ}=-\kappa A_{\rm int}|_{Q\mathcal H}+B_Q,
 \qquad \kappa>0,quad B_Q\in\mathcal B(Q\mathcal H).
\]
If $\omega_Q:=\kappa\lambda_{\rm int}-\|B_Q\|>0$, then
\[
 \|e^{\tau L_{QQ}}\|\le e^{-\omega_Q\tau}.
\]
\end{proposition}

\begin{proof}
The self-adjoint semigroup generated by
$-\kappa A_{\rm int}|_{Q\mathcal H}$ has norm at most
$e^{-\kappa\lambda_{\rm int}\tau}$. The bounded perturbation estimate gives
the additional factor $e^{\|B_Q\|\tau}$.
\end{proof}

For a general sectorial or nonnormal $L_{QQ}$, the constants $M_Q$ and
$\omega_Q$ must be proved directly. A positive vertical operator cannot be
identified with the stabilization generator without the minus sign and the
lower-order terms.

\section{Independent logical gates}

The following gates are independent and must not be collapsed:
\begin{description}
\item[Gap.] Spectral separation for $A_{\rm int}$.
\item[Projector stability.] Persistence and regularity of $P$ under parameter
or curvature variation.
\item[Invariance.] $R_\tau(P\mathcal H)\subseteq P\mathcal H$, equivalently
$QF(Pu)=0$ in a differentiable autonomous realization.
\item[Existence.] A fixed-point theorem applies on a declared invariant domain.
\item[Equilibrium identification.] A projected time-step fixed point is shown
to be stationary.
\item[Contraction.] The coherent reduced map is strictly contractive.
\item[Truncation.] The influence of $Q$ on $P$ is quantitatively bounded.
\item[Selection.] A continuation or reset rule is supplied at admissibility
exit.
\end{description}

No gate in this list follows solely from the gate preceding it.

\section{Projected fixed points and equilibria}

Let $K\subset P\mathcal H$ be nonempty, closed, bounded, and convex and define
\[
 T_\tau=P R_\tau|_K.
\]

\begin{theorem}[Projected time-step existence]\label{thm:existence}
Assume $T_\tau(K)\subset K$ and either:
\begin{enumerate}
\item $T_\tau:K\to K$ is continuous and compact; or
\item $T_\tau$ is continuous and condensing for a declared measure of
noncompactness.
\end{enumerate}
Then there is $u_\ast\in K$ with $T_\tau u_\ast=u_\ast$.
\end{theorem}

\begin{proof}
Apply Schauder in the first case and Darbo--Sadovskii in the second.
\end{proof}

The conclusion is a \emph{projected time-step fixed point}. It is not named an
equilibrium merely because $P R_\tau u_\ast=u_\ast$.

\begin{theorem}[Strict-Lyapunov equilibrium promotion]\label{thm:promotion}
Suppose $P\mathcal H$ is invariant, so that
$P R_\tau u_\ast=R_\tau u_\ast=u_\ast$, and along the orbit
\[
 \mathcal C(R_\tau u)-\mathcal C(u)
 =-\int_0^\tau\mathcal D(R_su)\,ds,
 \qquad\mathcal D\ge0,
\]
where $\mathcal D(v)=0$ exactly when $F(v)=0$. Then the fixed point from
Theorem~\ref{thm:existence} is an equilibrium.
\end{theorem}

\begin{proof}
Endpoint recurrence makes the left side zero. Nonnegativity and continuity
force $\mathcal D=0$ along the orbit; strictness gives $F(u_\ast)=0$.
\end{proof}

\begin{theorem}[Banach gate]\label{thm:banach}
If $K$ is complete, $T_\tau(K)\subset K$, and
\[
 \|T_\tau u-T_\tau v\|\le q\|u-v\|,
 \qquad0\le q<1,
\]
then $T_\tau$ has a unique fixed point in $K$, and its iterates converge to
that point. The theorem does not apply without the invariant complete domain.
\end{theorem}

\section{Schur--Feshbach reduction with domains}

Let $\mathcal H=P\mathcal H\oplus Q\mathcal H$. Consider a closed block
operator
\[
 L=\begin{pmatrix}L_{PP}&L_{PQ}\\L_{QP}&L_{QQ}\end{pmatrix}
\]
with domain $P\mathcal H\oplus\mathcal D(L_{QQ})$. Assume:
\begin{enumerate}
\item $0\in\rho(L_{QQ})$ and
$L_{QQ}^{-1}:Q\mathcal H\to\mathcal D(L_{QQ})$ is bounded in the graph norm;
\item $L_{PP}$ and $L_{QP}:P\mathcal H\to Q\mathcal H$ are bounded; and
\item $L_{PQ}:\mathcal D(L_{QQ})\to P\mathcal H$ is graph-norm bounded, so
$L_{PQ}L_{QQ}^{-1}$ is bounded.
\end{enumerate}

\begin{theorem}[Schur--Feshbach equation]\label{thm:feshbach}
Under these hypotheses, solving $L(p,q)=(f_P,f_Q)$ is equivalent to
\[
 S p=f_P-L_{PQ}L_{QQ}^{-1}f_Q,
 \qquad
 q=L_{QQ}^{-1}(f_Q-L_{QP}p),
\]
where
\[
 S=L_{PP}-L_{PQ}L_{QQ}^{-1}L_{QP}.
\]
If $\|L_{QQ}^{-1}\|\le C_Q/\omega_Q$, then
\[
 \|S-L_{PP}\|
 \le\|L_{PQ}L_{QQ}^{-1}\|\,\|L_{QP}\|
 \le\frac{C_Q\|L_{PQ}\|_{\rm gr}\|L_{QP}\|}{\omega_Q}.
\]
\end{theorem}

\begin{proof}
The $Q$ block equation gives the displayed formula for $q$. Substitution in
the $P$ block equation gives $S$. The bound follows from the declared graph
norm and inverse estimates.
\end{proof}

This is a local linear reduction near the reference state. Nonlinear
truncation additionally requires control of nonlinear remainders and of the
time interval on which the eliminated sector remains small.

\section{Projector stability and basin-local robustness}

\begin{proposition}[Riesz-projector stability]
Let $A(\epsilon)$ be a norm-resolvent-continuous family and let a contour
$\Gamma$ remain in the resolvent set while enclosing one isolated cluster.
Then
\[
 P(\epsilon)=\frac{1}{2\pi i}\oint_\Gamma(z-A(\epsilon))^{-1}\,dz
\]
is norm continuous and has constant finite rank. This proves projector
stability, not dynamical stability of a fixed point.
\end{proposition}

\begin{theorem}[Basin-local fixed-point robustness]\label{thm:robust}
Let $T,\widetilde T:K\to K$ be contractions on the same complete invariant
domain with contraction constant at most $q<1$. If
\[
 \sup_{u\in K}\|T(u)-\widetilde T(u)\|\le\varepsilon,
\]
then their fixed points satisfy
\[
 \|u_\ast-\widetilde u_\ast\|\le\frac{\varepsilon}{1-q}.
\]
\end{theorem}

\begin{proof}
Insert and subtract $T(\widetilde u_\ast)$ and absorb the resulting
$q\|u_\ast-\widetilde u_\ast\|$ term.
\end{proof}

This is the justified foundation for a local robustness or universality
claim. It is not global universality across arbitrary microscopic models.

\section{Projection, descent, and recovery types}

Let $r:X\to Y_{\rm eff}$ be a surjective reduction map on a microscopic state
space $X$, and let $\Phi:X\to X$ be a microscopic step.

\begin{theorem}[Autonomous descent criterion]\label{thm:descent}
There exists a unique reduced map $\overline\Phi:Y_{\rm eff}\to Y_{\rm eff}$
satisfying
\[
 \overline\Phi\circ r=r\circ\Phi
\]
if and only if
\[
 r(x)=r(x')\quad\Longrightarrow\quad r(\Phi x)=r(\Phi x').
\]
\end{theorem}

\begin{proof}
Necessity follows by applying $\overline\Phi$. For sufficiency define
$\overline\Phi(r(x))=r(\Phi x)$; the implication makes this independent of the
representative, and surjectivity gives uniqueness.
\end{proof}

A section $s:Y_{\rm eff}\to X$ obeys $r\circ s=\operatorname{id}$ and chooses
one representative. It does not recover every microscopic state. Exact
microscopic recovery would require $s\circ r=\operatorname{id}_X$, which is
possible only when $r$ is injective. An effective merger combines reduced
descriptions and is neither kind of inverse unless separately typed and
proved.

If $r$ is fiberwise over the base and the microscopic generator is local in
base variables, a reduced local generator may descend when the invariance
criterion holds and all coefficients depend locally and smoothly on the base
jet. A projection nonlocal in base variables does not inherit locality merely
from being a projector.

\section{Admissibility and hybrid selection}

Let $m_j(u)$ be declared continuous margins and define
\[
 \mathcal A_\varepsilon
 =\{u:m_j(u)\ge\varepsilon\text{ for all }j\},
 \qquad
 \mathfrak B(u)=\max_j[-m_j(u)].
\]
Then $u\in\mathcal A_0$ exactly when $\mathfrak B(u)\le0$. This is a diagnostic
encoding of declared constraints, not automatically an energy or force.

At a first exit from $\mathcal A_0$, three logically different constructions
are possible:
\begin{enumerate}
\item stop the reduced description;
\item continue the upper dynamics and derive a new reduced chart; or
\item impose a reset $S:\partial\mathcal A_0\to\mathcal A_0$.
\end{enumerate}
The third option defines a hybrid dynamical system. It changes the continuation
law and must separately prove existence, measurability, conservation, and any
probability assigned to alternative reset outcomes. Calling the reset
``selection'' does not make it part of the original flow.

\section{Complete admissibility-margin ledger}

Every realization must record the following entries independently:
\begin{enumerate}
\item \textbf{Geometry/domain:} base, fiber, dimensions, bundle regularity,
operator domains, and boundary conditions.
\item \textbf{Joint spectral structure:} strong commutation or a selected
total operator, the spectral contour, rank, and Sobolev boundedness of $P$.
\item \textbf{Internal gap:} $\lambda_{\rm int}$ and its uniformity domain.
\item \textbf{Complementary stability:} $M_Q,\omega_Q$ and the generator sign.
\item \textbf{Leakage/invariance:} $QF(Pu)$ or a quantitative leakage bound.
\item \textbf{Existence gate:} the invariant set $K$ and the compact,
condensing, or contraction theorem actually used.
\item \textbf{Equilibrium gate:} stationarity equation or strict Lyapunov
promotion.
\item \textbf{Coherent contraction:} norm, basin, and factor $q<1$.
\item \textbf{Truncation:} mixing blocks, inverse/domain bounds, nonlinear
remainder, and error interval.
\item \textbf{Projector robustness:} perturbation topology and resolvent
contour.
\item \textbf{Admissibility:} each margin $m_j$, its units, and its source.
\item \textbf{Continuation/selection:} stop, upper continuation, or hybrid
reset, including conservation and probability data.
\item \textbf{Physical hyperbolicity:} principal symbol, constraints, causal
domain, and relation between $t$ and $\tau$.
\item \textbf{Scale separation:} internal gap $\lambda_{\rm int}$, coherent
contraction scale, external four-dimensional cutoff $\Lambda_{4D}$, curvature
scale, and RG scale $\mu$.
\item \textbf{Numerical provenance:} source-independent inputs, fitted inputs,
branch selection, uncertainty, and held-out outputs.
\end{enumerate}

No single scalar ``coherence scale'' may replace this ledger unless a theorem
derives all identifications with dimensions and errors.

\section{Lorentzian physical completion}

The Hilbert inner product and every Gram tensor constructed from it are
positive semidefinite. They cannot acquire Lorentzian signature. In a local
physical completion, causal signature is instead read from the principal
symbol. For a second-order field equation this has the schematic form
\[
 \sigma_{\rm pr}(x,\xi)=g^{\mu\nu}(x)\xi_\mu\xi_\nu I+\text{gauge blocks}.
\]
Lorentzian hyperbolicity, constraint propagation, and a domain-of-dependence
theorem must be verified for the selected equations. The canonical base
dimension $3+1$ is part of the canonical FP physical realization; it is not
derived by the abstract Hilbert-bundle theory.

\section{Foundation synthesis theorem}

\begin{theorem}[Scoped MTT foundation]\label{thm:foundation}
Assume the dimension-neutral Hilbert-bundle architecture, joint spectral
structure, internal gap, stable complementary semigroup, and the separately
listed hypotheses for a chosen fixed-point theorem. Then the model possesses
a bounded coherent decomposition and a projected time-step fixed point. Under
strict Lyapunov and invariance hypotheses that point is an equilibrium. Under
the Banach gate it is unique in the declared basin. Under the Schur--Feshbach
hypotheses the local linear complementary sector can be eliminated with the
displayed error bound. Under contraction and map-closeness hypotheses the
fixed point is basin-locally robust. Autonomous reduced dynamics exists
exactly under the descent criterion.
\end{theorem}

None of these conclusions supplies a physical probability law, Lorentzian
field equation, quantum representation, particle spectrum, Standard Model
matching, cosmology, or numerical prediction. Those are downstream
obligations governed by the admissibility ledger.

\section{Conclusion}

The corrected Foundation provides a typed and noncircular spine for the MTT
corpus. It identifies what the triplet and projector mean, how complementary
stability is proved, which fixed-point conclusion is available, how reduction
is typed, and where physical assumptions enter. Its value is precisely this
separation: later realizations can now be tested against explicit gates rather
than inheriting conclusions from an undifferentiated appeal to coherence.

\begin{thebibliography}{99}

\bibitem{FixedPoints}
P.~Nero,
\newblock \emph{Fixed Points I--VI}, corrected theorem spine,
\newblock revised editions, 2026.

\bibitem{Kato}
T.~Kato,
\newblock \emph{Perturbation Theory for Linear Operators},
\newblock Springer, 1995.

\bibitem{EngelNagel}
K.-J.~Engel and R.~Nagel,
\newblock \emph{One-Parameter Semigroups for Linear Evolution Equations},
\newblock Springer, 2000.

\bibitem{Deimling}
K.~Deimling,
\newblock \emph{Nonlinear Functional Analysis},
\newblock Springer, 1985.

\end{thebibliography}

\end{document}
"""


def main() -> None:
    TEX.write_text(TEXT, encoding="utf-8")
    print(f"Updated {TEX}")


if __name__ == "__main__":
    main()
