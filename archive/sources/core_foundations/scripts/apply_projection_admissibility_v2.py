from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = (
    ROOT
    / "revised_tex_vnext"
    / "The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2"
    / "main.tex"
)

TEXT = r"""\documentclass[11pt]{article}
\usepackage{series}
\usepackage{mathtools}

\title{The Projection--Admissibility Principle\\
\large Descent, Recovery, and Structural Constraints on Effective Description}
\author{Peter Nero}
\date{July 2026}

\begin{document}
\maketitle
\seriestagline

\begin{abstract}
We replace the former noninvertibility obstruction by a typed theory of
projection, descent, recovery, and admissibility. For an upper evolution
$\Phi_t$, an initial reduction $P_0$, and a final reduction $P_t$, four
different questions arise. A right section selects one compatible upper
representative; a left decoder recovers the actual upper input; an autonomous
reduced map exists exactly when upper evolution respects the initial
equivalence classes; and an effective merger is noninjectivity of that reduced
map. Noninjectivity of a cross-level projection does not forbid a right
section. We prove the correct factor-through theorem, a valid no-right-section
criterion for a genuinely contractive reduced self-map, a section-conditioning
diagnostic, and locality descent for fiberwise coherent compression of a local
operator net. Probability requires an upper measure and disintegration;
entropy, irreversibility, and an arrow of time require additional structures.
Applications to open systems, Wilsonian reduction, exterior gravity, and MTT
are consequently reconstructions or conditional realizations rather than
corollaries of noninjectivity alone.
\end{abstract}

\tableofcontents

\section{Scope and correction of the former obstruction}

The previous version argued that a noninjective map cannot have a right
inverse. That statement is false. A surjection may be highly noninjective and
still admit a section. For example,
\[
 r:\mathbb R^2\to\mathbb R,\qquad r(x,z)=x,
 \qquad s(x)=(x,0)
\]
satisfies $r\circ s=\operatorname{id}_{\mathbb R}$.

The mistake was a type error. A right inverse chooses one preimage; it does not
recover the preimage that was actually supplied. Actual microscopic recovery
is a left-inverse condition. Autonomous effective evolution is a third
condition, namely factorization through the initial reduction. This paper
keeps those objects separate.

The results are structural set-theoretic, topological, metric,
measure-theoretic, or operator-algebraic theorems according to the hypotheses
stated in each section. No probability, entropy, Hilbert structure, geometry,
or physical time is inferred from a bare map of sets.

\section{Typed projection and evolution data}

Let $A$ be an admissible upper state domain and let
\[
 \Phi_t:A\to X_t
\]
be an upper evolution map. Invertibility of $\Phi_t$ is not needed for the
basic typing results. Let
\[
 P_0:A\to Y_0,
 \qquad
 P_t:\Phi_t(A)\to Y_t
\]
be surjective reduction maps onto their declared effective images, and define
the cross-level output map
\[
 T_t=P_t\circ\Phi_t:A\to Y_t.
\]

The fibers of $P_0$ define the initial effective equivalence relation
\[
 x\sim_0x'\quad\Longleftrightarrow\quad P_0(x)=P_0(x').
\]

\begin{definition}[Representative section]
A representative section for $T_t$ is a map $S_t:Y_t\to A$ satisfying
\[
 T_t\circ S_t=\operatorname{id}_{Y_t}.
\]
It chooses one upper state compatible with each final effective state.
\end{definition}

\begin{definition}[Exact upper decoder]
An exact decoder is a map $D_t:T_t(A)\to A$ satisfying
\[
 D_t\circ T_t=\operatorname{id}_A.
\]
It recovers the actual upper input from the final effective output.
\end{definition}

\begin{definition}[Autonomous reduced evolution]
An autonomous reduced evolution is a map $F_t:Y_0\to Y_t$ satisfying
\[
 F_t\circ P_0=P_t\circ\Phi_t.
\]
\end{definition}

\begin{definition}[Effective merger]
If $F_t$ exists, an effective merger occurs when distinct initial effective
states $y\ne y'$ satisfy $F_t(y)=F_t(y')$.
\end{definition}

These four definitions have different domains and equations. They are not
interchangeable notions of inversion.

\section{Projection--descent and recovery theorem}

\begin{theorem}[Projection--descent and recovery]\label{thm:main}
For the typed data above:
\begin{enumerate}
\item A set-theoretic representative section $S_t$ exists if $T_t$ is
surjective and the relevant choice principle is available. A continuous,
measurable, local, or Lipschitz section requires a theorem in that category.
\item An exact decoder $D_t:T_t(A)\to A$ exists only if $T_t$ is injective.
Conversely, if $T_t$ is injective, its inverse on $T_t(A)$ is an exact decoder.
\item An autonomous reduced evolution $F_t$ exists if and only if
\begin{equation}
 P_0(x)=P_0(x')
 \quad\Longrightarrow\quad
 P_t(\Phi_t x)=P_t(\Phi_t x')
 \label{eq:factor}
\end{equation}
for all $x,x'\in A$. When it exists, $F_t$ is unique.
\item If~\eqref{eq:factor} holds and there are $x,x'\in A$ with
$P_0(x)\ne P_0(x')$ but
$P_t(\Phi_t x)=P_t(\Phi_t x')$, then $F_t$ is noninjective. The prior
effective state cannot be decoded uniquely from the final effective state.
\end{enumerate}
\end{theorem}

\begin{proof}
The first item is the definition of a section of a surjection. If
$D_tT_t=\operatorname{id}_A$ and $T_t(x)=T_t(x')$, applying $D_t$ gives
$x=x'$, proving the second item. For the third, necessity follows by applying
$F_t$ to equal initial effective states. Under~\eqref{eq:factor}, define
\[
 F_t(P_0x):=P_t(\Phi_tx).
\]
The implication makes the value independent of the representative;
surjectivity of $P_0$ gives existence and uniqueness. The last item follows
directly from the definition of $F_t$.
\end{proof}

\begin{corollary}[Noninjectivity does not obstruct representative selection]
Noninjectivity of $T_t$ rules out an exact decoder, not a representative
section. Surjectivity is the set-theoretic gate for a right section.
\end{corollary}

\section{A valid no-right-section obstruction}

There is a correct obstruction when the map in question is a self-map of the
same reduced space and its image is provably too small.

\begin{theorem}[Finite-diameter contraction obstruction]\label{thm:diameter}
Let $(Y_A,d)$ have finite positive diameter $D$, and let
$G:Y_A\to Y_A$ satisfy
\[
 d(Gy,Gy')\le\kappa d(y,y')+c\varepsilon,
 \qquad0\le\kappa<1,\quad c\varepsilon\ge0.
\]
Then
\[
 \operatorname{diam}G(Y_A)\le\kappa D+c\varepsilon.
\]
If $(1-\kappa)D>c\varepsilon$, then $G$ is not surjective and therefore has no
right section $S:Y_A\to Y_A$ with $G\circ S=\operatorname{id}_{Y_A}$.
\end{theorem}

\begin{proof}
Take the supremum of the displayed inequality over all pairs. Under the strict
condition the image diameter is smaller than $D$, whereas a surjective image
would equal $Y_A$ and have diameter $D$.
\end{proof}

This theorem concerns a reduced self-map $G:Y_A\to Y_A$. It does not apply to
a cross-level map $T_t:A\to Y_t$ merely because that map is noninjective.
Moreover, the additive-error inequality is not a Banach contraction. Banach
requires a genuine Lipschitz constant below one on a complete invariant
domain.

\section{Stable representative continuation}

Suppose $A,Y_t$ are metric spaces. For all Lipschitz right sections define the
best section condition number
\[
 \kappa_{\rm sec}(t)
 :=\inf\{\operatorname{Lip}(S_t):T_tS_t=\operatorname{id}_{Y_t}\},
\]
with $\kappa_{\rm sec}(t)=+\infty$ if no Lipschitz section exists.

\begin{proposition}[Section-conditioning diagnostic]
If $\kappa_{\rm sec}(t)$ remains bounded on an interval and a chosen family of
sections attains a uniform bound, representative selection is uniformly
Lipschitz on that interval. Blow-up of $\kappa_{\rm sec}$ or loss of
surjectivity is an obstruction to such stable continuation. It is not, by
itself, a physical singularity, entropy law, or stochastic transition.
\end{proposition}

For spectral projections, a parallel diagnostic is failure of bounded
norm-resolvent continuation of the selected Riesz projector. These two
diagnostics are related only when a realization proves the relation.

\section{Admissibility without automatic selection}

Let $m_j(t,x)$ be declared continuous margins and define
\[
 A_t^\delta=\{x:m_j(t,x)\ge\delta\text{ for every }j\}.
\]
The margins may record operator domains, spectral separation, complementary
damping, leakage, contraction, truncation error, section conditioning, or
physical hyperbolicity. A first exit from $A_t^0$ means that at least one
declared description condition fails.

Exit does not imply that $T_t$ has no set-theoretic section; the failed margin
must be identified. Nor does exit select a new state. One must stop the reduced
description, derive continuation from upper dynamics, or add a hybrid reset
law. A reset is new continuation data and must prove conservation,
measurability, and any assigned probabilities.

\section{Measure-dependent stochastic reduction}

Projection does not create a probability measure. A stochastic reduced law
can be induced only after preparation or invariant measure data are supplied.

\begin{theorem}[Measure-dependent reduced kernel]\label{thm:kernel}
Let $A,Y_0,Y_t$ be standard Borel spaces, let $P_0$ be measurable, and let
$\mu$ be a probability measure on $A$. Let $\{\mu_y\}$ be a regular
conditional distribution of $x$ given $P_0(x)=y$. Then
\[
 K_t(y,B)
 :=\mu_y\bigl(\{x:P_t(\Phi_tx)\in B\}\bigr)
\]
defines a Markov kernel from $Y_0$ to $Y_t$, up to the usual
$(P_0)_\#\mu$-null sets. If autonomous descent holds, then
\[
 K_t(y,\cdot)=\delta_{F_t(y)}
\]
for almost every $y$.
\end{theorem}

\begin{proof}
Regular conditional distributions exist on standard Borel spaces. Measurability
and countable additivity pass through the measurable preimage defining $K_t$.
Under descent, $P_t\Phi_tx=F_t(P_0x)$ is constant on each conditional fiber.
\end{proof}

Different upper measures, even with the same projection fibers, may induce
different kernels. Fiber cardinality alone does not determine weights and does
not imply the Born rule.

\section{Information, entropy, and temporal direction}

Noninjectivity states only that some distinctions are absent from the reduced
state. Quantitative information requires a sigma-algebra, coding, metric, or
probability measure. Entropy requires a specified entropy functional and
state. Monotone entropy production requires a dynamical theorem such as data
processing for a declared stochastic channel, a coarse-graining inequality,
or a thermodynamic balance law.

Likewise, failure of an exact decoder does not by itself establish an arrow of
time. A temporal arrow requires an oriented evolution family and an asymmetric
property such as a semigroup without inverse in the chosen category, a
monotone Lyapunov/entropy functional, or a boundary condition. A
representative section is not a reverse-time evolution.

Universality also needs more than equivalence classes. It requires stability
of reduced laws under a declared class of microscopic perturbations, for
example the basin-local contraction estimate of the corrected Foundation and
Fixed Points spine.

\section{Locality descent under coherent compression}

Let $\pi:M_{10}\to Y_4$ be the canonical physical bundle and let
\[
 P=\int_{Y_4}^{\oplus}P_x\,d\mu(x)
\]
be a decomposable fiberwise coherent projector. Suppose
$O\mapsto\mathcal A_{10}(\pi^{-1}O)$ is an upper local net. Define
\[
 \mathcal A_{10}^P(O)
 =\{A\in\mathcal A_{10}(\pi^{-1}O):[A,P]=0\}
\]
and
\[
 \mathcal A_4(O)
 =\{PAP|_{\operatorname{Ran}P}:A\in\mathcal A_{10}^P(O)\}.
\]

\begin{theorem}[Fixed-point locality descent]\label{thm:locality}
If the upper net is isotonic, then $\mathcal A_4$ is isotonic. If upper
observables assigned to spacelike separated base regions commute, then their
compressed coherent observables commute. Thus microcausality descends on the
$P$-compatible subalgebra.
\end{theorem}

\begin{proof}
Upper inclusion immediately gives compressed inclusion. For compatible
$A,B$, commutation with $P$ gives
\[
 [PAP,PBP]|_{\operatorname{Ran}P}=P[A,B]P|_{\operatorname{Ran}P},
\]
which vanishes for spacelike separated upper observables.
\end{proof}

This theorem does not imply state factorization. Entangled or otherwise
nonfactorizing states may restrict to the descended net. A projection nonlocal
over the base, or an observable not preserving $\operatorname{Ran}P$, lies
outside this theorem.

\section{Corrected realizations}

\subsection{Open quantum systems}

For a system and environment, partial trace
\[
 P(\rho_{SE})=\operatorname{Tr}_E\rho_{SE}
\]
is noninjective but surjective onto system density matrices when an environment
state is available. The assignment
$S(\rho_S)=\rho_S\otimes\sigma_E$ is a representative section. It is not an
exact decoder of the actual correlated state $\rho_{SE}$.

A state-independent reduced channel exists only under assignment and
compatibility conditions. Initial system--environment correlations can make
the future reduced state depend on more than $\rho_S$, violating the descent
criterion. Probabilities are already supplied by the quantum state and Born
rule; they are not derived from noninjectivity of partial trace.

\subsection{Wilsonian reduction}

Integrating out high-frequency modes maps UV actions or measures to lower-scale
effective data. Distinct UV inputs may have the same IR image, so exact UV
decoding generally fails. A representative UV completion, when it exists,
is a section and is nonunique. Autonomous RG evolution requires a selected
theory space and closure or controlled truncation; it does not follow from
coarse graining alone. Universality requires a fixed-point/basin stability
theorem.

\subsection{Exterior gravity}

Restriction of a global solution to an exterior domain can be noninjective.
An exterior-to-global extension, where constraint-compatible extensions exist,
is a representative section rather than recovery of the actual interior.
Autonomous exterior evolution requires boundary conditions, flux data, and a
well-posed domain. Horizon area or entropy is not obtained from
noninjectivity alone.

\subsection{Modal Triplet Theory}

In the corrected MTT Foundation, $P$ is the joint coherent spectral projector
and $R_\tau$ is the stabilization flow. An autonomous coherent map exists
exactly when $P R_\tau$ is constant on the relevant initial $P$-fibers. Exact
invariance is a sufficient special case. FP~I--VI provide conditional
fixed-point, damping, curved-projector, covariance, and admissibility results.

The internal gap and Riesz-projector continuation can support stable coherent
reduction. They do not by themselves derive a measure, Born weights, entropy,
a reset outcome, quantum field theory, gravity, or cosmology. MTT is therefore
a conditional realization of the typed framework only to the extent that each
gate is verified.

\section{Scoped projection--admissibility theorem}

\begin{theorem}[Scoped principle]\label{thm:scope}
For typed upper evolution and reductions:
\begin{enumerate}
\item representative selection, exact recovery, autonomous descent, and
effective merger obey the separate conditions in Theorem~\ref{thm:main};
\item a reduced self-map has no right section when its image diameter is
strictly smaller than its state-space diameter;
\item stable representative continuation can be tested by section
conditioning or, in spectral realizations, bounded projector continuation;
\item an upper measure and regular conditional distributions induce a reduced
Markov kernel; and
\item upper locality descends to the coherent $P$-compatible compressed net.
\end{enumerate}
No probability rule, entropy production, arrow of time, universality class,
geometry, or Hilbert structure follows from noninjectivity alone.
\end{theorem}

\section{Conclusion}

Projection and admissibility remain useful organizing ideas once their maps
are typed correctly. The corrected principle says precisely when effective
dynamics descends, what a section can and cannot recover, when a reduced map
truly loses a right section, and which additional measure, stability, and
locality data support stronger conclusions. This narrower theorem is more
useful than the former universal obstruction because each downstream claim
now has a checkable mathematical gate.

\begin{thebibliography}{99}

\bibitem{Foundation}
P.~Nero,
\newblock \emph{Modal Triplet Theory: Foundations}, revised v7, 2026.

\bibitem{FixedPoints}
P.~Nero,
\newblock \emph{Fixed Points I--VI}, corrected theorem spine, 2026.

\bibitem{Kechris}
A.~S.~Kechris,
\newblock \emph{Classical Descriptive Set Theory},
\newblock Springer, 1995.

\bibitem{BreuerPetruccione}
H.-P.~Breuer and F.~Petruccione,
\newblock \emph{The Theory of Open Quantum Systems},
\newblock Oxford University Press, 2002.

\end{thebibliography}

\end{document}
"""


def main() -> None:
    TEX.write_text(TEXT, encoding="utf-8")
    print(f"Updated {TEX}")


if __name__ == "__main__":
    main()
