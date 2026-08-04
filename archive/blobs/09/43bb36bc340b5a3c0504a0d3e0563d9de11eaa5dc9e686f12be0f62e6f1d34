from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = (
    ROOT
    / "revised_tex_vnext"
    / "Lorentzian_Base_Compatibility_and_Signature_Stability_in_the_MTT_Fixed_Point_Realization_v2"
    / "main.tex"
)

TEXT = r"""\documentclass[11pt]{article}
\usepackage{series}

\title{Lorentzian Base Compatibility and Signature Stability\\
\large in the MTT Fixed-Point Realization}
\author{Peter Nero}
\date{July 2026}

\begin{document}
\maketitle
\seriestagline

\begin{abstract}
We correct the signature analysis of Modal Triplet Theory (MTT). A tensor of
the form $\langle D_\mu\Psi,D_\nu\Psi\rangle$ is a positive-semidefinite Gram
tensor and cannot have Lorentzian signature. Physical signature must instead
come from the principal symbol of a selected local physical evolution law.
For a nondegenerate quadratic metric symbol we prove that hyperbolicity with
respect to one evolution covector is possible exactly for Lorentzian inertia,
with one sign occurring once. This conditionally excludes Euclidean and
multi-time signatures from the standard one-parameter Cauchy problem, but it
does not select the number of spatial dimensions. The $3+1$ Lorentzian base is
therefore an assumption of the canonical ten-dimensional MTT/Fixed-Points
realization unless a separate dimension-selection theorem is supplied. We
prove local stability of Lorentzian inertia under coefficient perturbations,
show that continuous signature change crosses degeneracy, and give a
principal-symbol descent theorem for fiberwise coherent compression. Control
contraction, internal spectral gaps, physical hyperbolicity, and dimension
selection remain independent gates.
\end{abstract}

\tableofcontents

\section{Correction and scope}

The former paper defined
\[
 K_{\mu\nu}=\langle D_\mu\Psi_\ast,D_\nu\Psi_\ast\rangle_{\rm coh}
\]
using a positive Hilbert inner product and then assigned Lorentzian signature
to $K$. This is impossible.

\begin{proposition}[Positive Gram obstruction]\label{prop:gram}
For vectors $v_0,\ldots,v_{d-1}$ in a real Hilbert space, the Gram matrix
$G_{\mu\nu}=\langle v_\mu,v_\nu\rangle$ is positive semidefinite. Hence it has
no negative eigenvalues and cannot be a Lorentzian metric.
\end{proposition}

\begin{proof}
For every $c\in\mathbb R^d$,
\[
 c^\mu G_{\mu\nu}c^\nu
 =\left\|\sum_\mu c^\mu v_\mu\right\|^2\ge0.
\]
\end{proof}

The Gram tensor may be a useful positive kinetic or information metric. It is
not a causal metric. Inserting an indefinite operator between the vectors can
produce an indefinite form, but that operator is then additional signature
data and must be selected and justified independently.

This revision studies compatibility and stability of a Lorentzian principal
symbol. It does not claim universal signature or dimension selection.

\section{Canonical MTT geometry and independent gates}

The canonical physical realization is
\[
 \pi:M_{10}\to Y_4,
 \qquad \dim Y_4=4,
 \qquad \dim X_x=6,
\]
with globally hyperbolic Lorentzian base $(Y_4,g)$ and compact Riemannian fiber
$X_x$. The base dimension and its Lorentzian signature are part of this
canonical realization. Positive vertical operators act on $X_x$ and do not
determine the causal signature of $Y_4$.

Four gates must remain separate:
\begin{enumerate}
\item the internal gap and coherent spectral projector;
\item stability or contraction of the stabilization flow $R_\tau$;
\item hyperbolicity and causal propagation of a physical evolution $U(t_2,t_1)$;
and
\item selection of base dimension and topology.
\end{enumerate}
The stabilization parameter $\tau$ is not automatically physical time $t$.
Neither a vertical gap nor Banach contraction supplies a null cone.

\section{Principal symbols and physical signature}

Consider a local second-order physical field equation for a multiplet $u^A$,
\[
 \mathcal E_A(u)
 =C_{AB}^{\mu\nu}(x,u,\partial u)\,\partial_\mu\partial_\nu u^B
 +\text{lower-order terms}=0.
\]
Its principal symbol at a frozen background is
\[
 \sigma_{\rm pr}(x,\xi)_{AB}
 =C_{AB}^{\mu\nu}(x)\xi_\mu\xi_\nu.
\]
Characteristics, hyperbolicity, and causal cones come from this symbol after
gauge fixing and constraint reduction. Lower-order damping and internal mass
operators can affect stability without changing the characteristic cone.

For a normally hyperbolic metric-type equation,
\[
 \sigma_{\rm pr}(x,\xi)
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu I.
\]
The physical signature is the inertia of $g^{\mu\nu}$, not the inertia of a
positive state-space inner product.

For a first-order system, the appropriate condition is strong or symmetric
hyperbolicity of $A^\mu\partial_\mu u$. Such a system need not be classified by
one effective metric without an additional characteristic-cone theorem.

\section{Quadratic hyperbolicity and conditional exclusions}

Let $q(\xi)=B(\xi,\xi)$ be a nondegenerate real quadratic form on a real vector
space of dimension $d\ge2$. It is hyperbolic with respect to a covector $n$ if
$q(n)\ne0$ and, for every $\xi$, all roots $s\in\mathbb C$ of
\[
 q(\xi+s n)=0
\]
are real.

\begin{theorem}[Quadratic hyperbolicity criterion]\label{thm:quadratic}
A nondegenerate quadratic form admits a hyperbolicity covector if and only if
its inertia is $(1,d-1)$ or $(d-1,1)$. For a Lorentzian form, the
hyperbolicity covectors are the covectors in the one-sign cone.
\end{theorem}

\begin{proof}
Fix $n$ with $q(n)\ne0$ and decompose
$\xi=a n+\eta$ with $B(n,\eta)=0$. Then
\[
 q(\xi+s n)=q(n)(s+a)^2+q(\eta).
\]
All roots are real for every $\eta\in n^\perp$ exactly when
$q(n)q(\eta)\le0$ for every such $\eta$. Nondegeneracy makes the restriction
to $n^\perp$ definite with sign opposite to $q(n)$. Thus the sign of $q(n)$
occurs exactly once. Conversely, for a vector in the one-sign cone of a
Lorentzian form, its orthogonal complement is definite with the opposite
sign, and the displayed roots are real.
\end{proof}

\begin{corollary}[Euclidean metric symbol]
A definite Euclidean quadratic symbol is not hyperbolic with respect to any
covector. It defines an elliptic rather than a standard hyperbolic Cauchy
problem.
\end{corollary}

This does not exclude Euclidean boundary-value theories, statistical models,
or Wick-rotated calculational descriptions. It excludes their interpretation
as the same real-time metric principal symbol for the standard local physical
Cauchy problem.

\begin{corollary}[Multi-time metric symbols]
A nondegenerate metric symbol of signature $(p,q)$ with $p,q\ge2$, including
$(2,2)$, has no hyperbolicity covector. It therefore does not furnish the
standard single-parameter metric Cauchy problem assumed in the canonical
physical realization.
\end{corollary}

This is a conditional principal-symbol statement, not a universal no-go
theorem for every constrained, nonlocal, ultrahyperbolic, or analytically
continued model.

\begin{corollary}[No selection of three spatial dimensions]
For every $n\ge1$, a metric symbol of inertia $(1,n)$ or $(n,1)$ admits
hyperbolicity covectors. Hyperbolicity alone therefore does not select
$n=3$.
\end{corollary}

Extra spatial dimensions may be incompatible with a particular spectrum,
compactification, observation, or stability requirement, but each such
exclusion needs its own theorem. The internal MTT gap does not automatically
suppress extra base directions.

\section{Signature stability}

\begin{theorem}[Uniform inertia stability]\label{thm:stability}
Let $H(x)$ be a continuous field of real symmetric nondegenerate matrices on a
compact set $K$, all with the same inertia. Define
\[
 \delta_{\rm sig}
 :=\inf_{x\in K}\min_j|\lambda_j(H(x))|>0.
\]
If a continuous symmetric perturbation $E(x)$ satisfies
\[
 \sup_{x\in K}\|E(x)\|_{\rm op}<\delta_{\rm sig},
\]
then $H(x)+E(x)$ has the same inertia as $H(x)$ for every $x\in K$.
\end{theorem}

\begin{proof}
Weyl's eigenvalue perturbation inequality moves every ordered eigenvalue by at
most $\|E(x)\|_{\rm op}$. No eigenvalue can cross zero under the strict bound,
so the numbers of positive and negative eigenvalues are unchanged.
\end{proof}

\begin{corollary}[Continuous signature change crosses degeneracy]
Along a continuous path of real symmetric matrices, a change of inertia
requires at least one zero eigenvalue. Thus a continuous metric signature
change leaves the uniformly nondegenerate hyperbolic class at the transition.
\end{corollary}

For a quasilinear system, inertia stability is only one gate. Uniform strong
hyperbolicity also requires control of the symmetrizer, characteristic roots,
gauge conditions, constraints, and coefficient regularity.

\section{Coherent compression of a hyperbolic realization}

The following theorem states a sufficient bridge from the selected physical
completion to the coherent sector.

\begin{theorem}[Principal-symbol descent]\label{thm:descent}
Let the upper local operator on $M_{10}\to Y_4$ have the form
\[
 \mathcal L_{10}
 =g^{\mu\nu}(x)\nabla_\mu\nabla_\nu\otimes I_{\rm int}
 +\mathcal L_{\rm vert}+\mathcal L_{\rm low},
\]
where $\mathcal L_{\rm vert}$ has no base derivatives of order two and
$\mathcal L_{\rm low}$ has base order at most one. Let $P_x$ be a smooth
fiberwise coherent projector whose action commutes with the scalar base
principal coefficient. Then the compressed operator on $\operatorname{Ran}P$
has principal symbol
\[
 \sigma_{\rm pr}(P\mathcal L_{10}P)(x,\xi)
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu I_{\operatorname{Ran}P}.
\]
Consequently the coherent compression inherits the already selected
Lorentzian characteristic cone.
\end{theorem}

\begin{proof}
Only the two-base-derivative term contributes to the base principal symbol.
Its internal coefficient is the identity, so compression replaces it by the
identity on $\operatorname{Ran}P$. Derivatives of a smooth base-dependent $P_x$
enter commutators of base order at most one and do not alter the principal
symbol.
\end{proof}

This theorem proves descent, not emergence or selection, of Lorentzian
signature. If the upper operator is bilocal over the base, contains
higher-order mixed base/fiber derivatives, or has matrix-valued principal
coefficients that do not preserve $\operatorname{Ran}P$, a separate analysis
is required.

\section{Relation to the corrected MTT spine}

The corrected Foundation supplies the canonical $Y_4$-over-$X_6$ realization,
the joint coherent projector, and the requirement that physical signature
come from a principal symbol. Fixed Points I--VI supply conditional projected
fixed points, equilibrium promotion, stability margins, curved-projector
control, and admissibility diagnostics.

Those results do not select a base metric. Their proper role here is:
\begin{itemize}
\item to ensure that the coherent sector used in
Theorem~\ref{thm:descent} is mathematically controlled;
\item to bound leakage and lower-order perturbations that might invalidate a
chosen physical completion; and
\item to provide independent control-flow stability after hyperbolicity has
been established.
\end{itemize}

The Projection--Admissibility theorem contributes typed continuation and
locality descent. An admissibility exit detects failure of a declared
hyperbolicity or signature margin but does not select a replacement signature.

\section{Compatibility ledger}

A physical signature claim must record:
\begin{enumerate}
\item the physical field equations and gauge-fixed principal symbol;
\item the state about which the symbol is frozen;
\item the hyperbolicity covector or time function;
\item the characteristic cone and domain-of-dependence theorem;
\item the uniform nondegeneracy margin $\delta_{\rm sig}$;
\item symmetrizer and constraint-propagation bounds for systems;
\item the relation, if any, between physical time $t$ and stabilization
parameter $\tau$;
\item the coherent-compression hypotheses; and
\item the independent status of the chosen base dimension.
\end{enumerate}

Without this ledger, a positive kinetic form or stable control flow cannot be
promoted to a spacetime signature theorem.

\section{Scoped signature theorem}

\begin{theorem}[Lorentzian compatibility and stability]\label{thm:scope}
Assume the canonical $3+1$ MTT physical realization is equipped with a local
metric-type physical equation whose principal symbol is Lorentzian and
uniformly nondegenerate. Assume also the coherent-compression hypotheses of
Theorem~\ref{thm:descent}. Then the coherent physical equation inherits the
selected Lorentzian cone, and sufficiently small symmetric coefficient
perturbations preserve its inertia. Definite Euclidean and multi-time metric
symbols are incompatible with the same standard one-parameter quadratic
hyperbolicity condition.
\end{theorem}

The theorem does not derive Lorentzian signature or $3+1$ dimensions from the
MTT Hilbert geometry. It verifies compatibility and perturbative stability
after a physical principal symbol and canonical base have been supplied.

\section{Conclusion}

The positive Gram construction cannot select spacetime signature. Replacing it
with principal-symbol analysis yields a precise and useful result: a standard
metric Cauchy problem requires Lorentzian inertia, that inertia is stable away
from degeneracy, and coherent fiberwise compression can preserve an already
selected causal cone. The same analysis also establishes the limit of the
claim: hyperbolicity permits one time and any number of spatial dimensions, so
three spatial dimensions remain part of the canonical MTT realization pending
a separate selection theorem.

\begin{thebibliography}{99}

\bibitem{Foundation}
P.~Nero,
\newblock \emph{Modal Triplet Theory: Foundations}, revised v7, 2026.

\bibitem{FixedPoints}
P.~Nero,
\newblock \emph{Fixed Points I--VI}, corrected theorem spine, 2026.

\bibitem{Taylor}
M.~E.~Taylor,
\newblock \emph{Partial Differential Equations III: Nonlinear Equations},
\newblock Springer, 2011.

\bibitem{Hormander}
L.~H\"ormander,
\newblock \emph{The Analysis of Linear Partial Differential Operators III},
\newblock Springer, 1985.

\end{thebibliography}

\end{document}
"""


def main() -> None:
    TEX.write_text(TEXT, encoding="utf-8")
    print(f"Updated {TEX}")


if __name__ == "__main__":
    main()
