from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = (
    ROOT
    / "revised_tex_vnext"
    / "Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v6"
    / "main.tex"
)

BODY = r"""\begin{abstract}
We formulate multi-structure covariance and admissibility diagnostics on the
corrected FP--I--IV spine. Curvature enters through the full Laplace-type
operator and its curved spectral projector, not through an unproved affine
eigenvalue rule. Exact Gaussian claims are restricted to frozen linear
Ornstein--Uhlenbeck systems. Their stationary covariance satisfies a Lyapunov
equation, and block-diagonal damping gives a correct cross-covariance and
canonical-correlation estimate. Admissibility is encoded by a finite or
trace-controlled family of declared spectral, damping, and performance
margins. The resulting deficit score detects exit but is neither a force nor
an energy unless a separate variational source theorem is supplied. For
affine Gaussian margin observables we prove finite-grid and continuous-time
exit bounds. Cross-correlation controls simultaneous exits on a declared
observation grid; it does not by itself prove localization, non-propagation,
or selection of a post-exit state.
\end{abstract}

\tableofcontents

\section{Inherited setting and scope}

Let $I=[t_0,t_1]$ be a finite parameter interval and let $(B,g_t)$ be a
Riemannian base with uniformly bounded geometry on $I$. This formulation does
not identify the FP stabilization parameter with physical Lorentzian time.
Existence of a projected fixed point and promotion to a full equilibrium are
inherited only when the hypotheses of FP~I and FP~II hold. Disturbance floors
are interpreted according to FP~III, and curvature uses the full operator and
projector construction of FP~IV.

At a frozen configuration $x$, write
\[
 L_x=\nabla_x^\ast\nabla_x+\mathcal R_x,
 \qquad P_x=P_{\mathcal R}(x),\qquad Q_x=I-P_x .
\]
The contour defining $P_x$ is assumed to remain in the resolvent set. If the
old uncurved projector is used instead, the leakage term $Q\mathcal RP$ from
FP~IV must be retained.

All matrix theorems below are finite dimensional. They also extend to a
separable Hilbert space when the noise covariance is trace class, the
semigroup is exponentially stable, and every displayed covariance product is
well defined. Modal sums are never used without a finite truncation or an
explicit summability hypothesis.

\section{Curved modal damping and exact OU modes}

Let $\alpha$ denote a joint spectral label, including multiplicity. In a
frozen $Q_x$-sector linearization, suppose the scalar mode satisfies the It\^o
equation
\begin{equation}
 da_\alpha=-\gamma_\alpha(x)a_\alpha\,dt
              +\sqrt{q_\alpha(x)}\,dW_\alpha(t),
 \qquad \gamma_\alpha(x)>0 .
 \label{eq:scalar-ou}
\end{equation}
Here $\gamma_\alpha$ is the damping margin obtained after the one-sided
nonlinear estimate; it is not a shared deterministic/stochastic disturbance
parameter. Curvature dependence is inherited from $L_x$. An affine response
formula for an eigenvalue is an additional approximation, not a consequence
of the Weitzenbock identity.

\begin{lemma}[Exact scalar OU variance]\label{lem:ou}
Equation~\eqref{eq:scalar-ou} has the unique invariant law
\[
 \mathcal N\!\left(0,\frac{q_\alpha}{2\gamma_\alpha}\right).
\]
Deterministic forcing $f_\alpha$ instead gives the input-to-state scale
$|f_\alpha|/\gamma_\alpha$; these two quantities are not interchangeable.
\end{lemma}

\begin{proof}
The variation-of-constants formula gives
\[
 a_\alpha(t)=e^{-\gamma_\alpha t}a_\alpha(0)
 +\sqrt{q_\alpha}\int_0^t e^{-\gamma_\alpha(t-s)}\,dW_\alpha(s).
\]
It\^o isometry yields variance
$q_\alpha(1-e^{-2\gamma_\alpha t})/(2\gamma_\alpha)$, which converges to the
displayed value. The deterministic scale follows by integrating the stable
kernel against a bounded input.
\end{proof}

\section{Multi-structure covariance}

Collect a finite set of frozen linearized amplitudes in $a(t)\in\mathbb R^d$:
\begin{equation}
 da=-\Gamma a\,dt+B\,dW_t,
 \qquad Q:=BB^\top,
 \label{eq:vector-ou}
\end{equation}
where $\Gamma=\Gamma^\top\succeq\gamma_0 I$ with $\gamma_0>0$.

\begin{theorem}[Stationary covariance]\label{thm:covariance}
Equation~\eqref{eq:vector-ou} has a unique centered Gaussian invariant law
with covariance
\[
 \Sigma=\int_0^\infty e^{-t\Gamma}Qe^{-t\Gamma}\,dt .
\]
It is the unique solution of
\[
 \Gamma\Sigma+\Sigma\Gamma=Q,
 \qquad \|\Sigma\|_{\rm op}\le\frac{\|Q\|_{\rm op}}{2\gamma_0}.
\]
\end{theorem}

\begin{proof}
Exponential stability makes the integral converge. Differentiating the
integrand proves the Lyapunov equation. Uniqueness follows by applying the
stable semigroup to the homogeneous equation, and the norm estimate follows
from $\|e^{-t\Gamma}\|\le e^{-\gamma_0t}$.
\end{proof}

Partition the structures into $A$ and $B$ and assume for this section that
\[
 \Gamma=\operatorname{diag}(\Gamma_A,\Gamma_B),\qquad
 \Gamma_A\succeq\gamma_A I,\quad
 \Gamma_B\succeq\gamma_B I.
\]
Then the cross block obeys the Sylvester equation
\[
 \Gamma_A\Sigma_{AB}+\Sigma_{AB}\Gamma_B=Q_{AB}.
\]

\begin{lemma}[Cross-covariance bound]\label{lem:cross-covariance}
Under the block-damping hypothesis,
\[
 \|\Sigma_{AB}\|_{\rm op}
 \le \frac{\|Q_{AB}\|_{\rm op}}{\gamma_A+\gamma_B}.
\]
In particular, $Q_{AB}=0$ implies $\Sigma_{AB}=0$ in this frozen linear model.
\end{lemma}

\begin{proof}
The Sylvester solution is
$\Sigma_{AB}=\int_0^\infty e^{-t\Gamma_A}Q_{AB}e^{-t\Gamma_B}\,dt$.
Taking norms proves the claim.
\end{proof}

\begin{definition}[Canonical cross-correlation]\label{def:canonical}
For a positive semidefinite covariance block matrix, define
\[
 \rho_{AB}:=
 \|\Sigma_A^{\dagger/2}\Sigma_{AB}\Sigma_B^{\dagger/2}\|_{\rm op}.
\]
The covariance support inclusions imply $0\le\rho_{AB}\le1$. Let
$m_A,m_B>0$ denote the smallest positive eigenvalues of $\Sigma_A,\Sigma_B$
on their supports.
\end{definition}

\begin{theorem}[Damping bound for canonical correlation]\label{thm:canonical}
Under the preceding hypotheses,
\[
 \rho_{AB}
 \le
 \frac{\|Q_{AB}\|_{\rm op}}
 { (\gamma_A+\gamma_B)\sqrt{m_A m_B}}.
\]
Consequently the right-hand side being smaller than $\rho_0\in(0,1)$ is a
sufficient condition for $\rho_{AB}<\rho_0$.
\end{theorem}

\begin{proof}
Use submultiplicativity, the identities
$\|\Sigma_A^{\dagger/2}\|=m_A^{-1/2}$ and
$\|\Sigma_B^{\dagger/2}\|=m_B^{-1/2}$, and
Lemma~\ref{lem:cross-covariance}.
\end{proof}

The smallest positive covariance eigenvalues are essential. Replacing them
by $\|\Sigma_A\|$ and $\|\Sigma_B\|$ reverses the relevant normalization and
does not bound canonical correlation.

\section{Admissibility margins and deficit score}

Fix a finite family of continuous margins $m_j(x)$, $j\in\mathcal J$. They may
include:
\begin{itemize}
\item separation of the curved low spectral cluster from the rest of the
spectrum;
\item positive one-sided damping margins $\gamma_\alpha(x)$;
\item declared deterministic performance bounds
$r^{\rm det}_\alpha-|f_\alpha|/\gamma_\alpha$;
\item declared stochastic variance bounds
$r^{\rm stoch}_\alpha-q_\alpha/(2\gamma_\alpha)$.
\end{itemize}
For an infinite family, replace finiteness by uniform convergence and compact
control sufficient to make the infimum below continuous.

\begin{definition}[Admissible domains and deficit score]\label{def:deficit}
Set
\[
 \mathcal D_\varepsilon
 :=\{x:m_j(x)\ge\varepsilon\text{ for every }j\in\mathcal J\},
 \qquad
 \mathfrak B(x):=\max_{j\in\mathcal J}[-m_j(x)].
\]
Then $x\in\mathcal D_0$ exactly when $\mathfrak B(x)\le0$, and
$x\in\mathcal D_\varepsilon$ exactly when
$\mathfrak B(x)\le-\varepsilon$.
\end{definition}

\begin{proposition}[Diagnostic status]\label{prop:diagnostic}
The score $\mathfrak B$ is an exact scalar encoding of the declared margin
constraints. It is not inserted into the evolution equation. It is not a
physical energy, selection potential, or infinite enforcement cost unless an
independent variational source theorem identifies it with such an object.
\end{proposition}

\begin{theorem}[Deterministic exit detection]\label{thm:exit}
Let $X:I\to B$ be continuous and suppose the margins are continuous. If
$X(t_0)\in\mathcal D_0$ and $\mathfrak B(X(t_1))>0$, there is a first exit time
\[
 \tau:=\inf\{t\in[t_0,t_1]:\mathfrak B(X(t))>0\},
\]
with $\mathfrak B(X(\tau))=0$. At times with $\mathfrak B(X(t))>0$, at least
one declared constraint fails.
\end{theorem}

\begin{proof}
The maximum of finitely many continuous functions is continuous. The result
follows from the intermediate value theorem and the definition of first exit.
\end{proof}

This theorem detects loss of the declared description. It neither supplies a
force causing the exit nor selects the state or basin after exit.

\section{Gaussian exit estimates}

We now impose the stronger structure actually needed for Gaussian claims.
Assume the stationary solution of~\eqref{eq:vector-ou} and an exact affine
linearized margin model
\begin{equation}
 m_j(t)=\bar m_j+\ell_j^\top a(t),
 \qquad \bar m_j>0 .
 \label{eq:affine-margin}
\end{equation}
Thus $Z_j(t):=\ell_j^\top a(t)$ is a centered stationary Gaussian process with
\[
 v_j:=\operatorname{Var}Z_j(t)
 =\ell_j^\top\Sigma\ell_j
 \le\|\ell_j\|^2\frac{\|Q\|}{2\gamma_0}.
\]
A merely Lipschitz nonlinear function of a Gaussian process is not generally
Gaussian, so~\eqref{eq:affine-margin} cannot be replaced by Lipschitz
regularity alone.

\begin{theorem}[Finite-grid exit bound]\label{thm:grid}
For observation times $t_1,\ldots,t_N$,
\[
 \mathbb P\!\left(\min_{j\in\mathcal J,\,1\le k\le N}m_j(t_k)<0\right)
 \le
 \sum_{j\in\mathcal J}N
 \exp\!\left(-\frac{\bar m_j^2}{2v_j}\right),
\]
with a zero-variance term interpreted as zero when $\bar m_j>0$.
\end{theorem}

\begin{proof}
For each pair $(j,k)$, the Gaussian tail bound gives
$\mathbb P(Z_j(t_k)<-\bar m_j)\le
\exp[-\bar m_j^2/(2v_j)]$. Apply the union bound. No temporal independence is
required.
\end{proof}

\begin{theorem}[Continuous-time Gaussian exit bound]\label{thm:continuous}
Assume each $Z_j$ is separable with almost surely continuous paths and
\[
 e_j:=\mathbb E\sup_{t\in I}[-Z_j(t)]<\infty,
 \qquad \sigma_j^2:=\sup_{t\in I}\operatorname{Var}Z_j(t).
\]
If $\bar m_j>e_j$ for every $j$, then
\[
 \mathbb P\!\left(\inf_{t\in I}\min_{j\in\mathcal J}m_j(t)<0\right)
 \le
 \sum_{j\in\mathcal J}
 \exp\!\left[-\frac{(\bar m_j-e_j)^2}{2\sigma_j^2}\right].
\]
\end{theorem}

\begin{proof}
Apply the Borell--TIS inequality to the separable Gaussian process $-Z_j$ and
then take a union bound over the finite constraint family.
\end{proof}

Finiteness of $e_j$ can be verified from the canonical increment metric by a
metric-entropy bound. Exponential covariance decay alone suggests the usual
$\sqrt{\log(1+\gamma_0|I|)}$ scale, but that scale is not asserted without the
required entropy estimate.

\section{Simultaneous exits and the limit of correlation data}

For two scalar affine margin observables at a fixed time, standardize the
exit variables as $U=-Z_A/\sigma_A$ and $V=-Z_B/\sigma_B$. Suppose
$-1<\rho_0<1$, $\operatorname{Corr}(U,V)\le\rho_0$, and the standardized positive margins
obey $u_A=\bar m_A/\sigma_A$, $u_B=\bar m_B/\sigma_B$.

\begin{lemma}[Fixed-time simultaneous-exit bound]\label{lem:simultaneous}
\[
 \mathbb P(U\ge u_A,\,V\ge u_B)
 \le
 \exp\!\left[-\frac{(u_A+u_B)^2}{4(1+\rho_0)}\right].
\]
For $N$ declared observation times at which the same bounds hold, the
probability of a simultaneous observed exit is at most $N$ times the
right-hand side.
\end{lemma}

\begin{proof}
The joint event implies $U+V\ge u_A+u_B$, while
$\operatorname{Var}(U+V)\le2(1+\rho_0)$. Apply the one-dimensional Gaussian
tail bound and then the union bound over observation times.
\end{proof}

\begin{proposition}[No propagation theorem from covariance alone]
Equal-time covariance or canonical correlation does not determine causal
propagation, temporal clustering, or a post-exit transition. Such conclusions
require a specified coupled evolution or transition kernel and control of
cross-time covariance. Therefore FP~V makes no probabilistic censorship or
non-propagation claim from $\rho_{AB}$ alone.
\end{proposition}

\section{Conclusion}

FP~V now supplies a rigorous frozen-linear covariance layer and a correctly
scoped admissibility layer. Curvature is handled through the FP~IV full
operator and projector. Joint modes use the FP~II/III indexing and disturbance
conventions. Canonical correlation is normalized by the smallest positive
covariance eigenvalues, and Gaussian persistence is proved only for affine
Gaussian margin observables under the assumptions required by the relevant
concentration theorem. The deficit score detects a declared loss of
admissibility but is not promoted to dynamics, energy, propagation, or
post-exit selection.

"""


def main() -> None:
    text = TEX.read_text(encoding="utf-8")
    start = text.index(r"\begin{abstract}")
    end = text.index(r"\begin{thebibliography}")
    text = text[:start] + BODY + text[end:]
    text = text.replace(r"\date{January, 2025}", r"\date{July 2026}")
    old_notation = r"""% =========================================================
% Local notation
% =========================================================

\newcommand{\Aop}{A}

\newcommand{\Ltwo}{L^{2}}
\newcommand{\HoneF}{H^{1}_{F}}

\newcommand{\lamNW}{\lambda^{(\omega)}_{n}}
\newcommand{\kappaN}{\kappa_{n}}
\newcommand{\gammaNW}{\gamma^{(\omega)}_{n}}
\newcommand{\deltaNW}{\delta^{(\omega)}_{n}}

\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\Tr}{\mathrm{Tr}}

"""
    text = text.replace(old_notation, "")
    TEX.write_text(text, encoding="utf-8")
    print(f"Updated {TEX}")


if __name__ == "__main__":
    main()
