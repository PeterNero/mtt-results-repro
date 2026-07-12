from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "revised_tex_vnext" / "Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v4" / "main.tex"


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _: replacement, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return updated


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")
    text = text.replace(r"\date{January, 2026}", r"\date{July 2026}", 1)
    body = r"""\begin{abstract}
We rebuild curvature coupling and structural transitions on the corrected
FP--I--III spine. A Laplace-type operator is normalized as
$L=\nabla^\ast\nabla+\mathcal R$. Curvature can shift the spectral cluster,
mix coherent and noncoherent sectors, and create a leakage floor. If
$\|\mathcal R\|<\lambda_\ast/2$, the full curved operator retains a separated
low cluster and defines a new Riesz projector; if one retains the unperturbed
projector, the term $Q\mathcal RP$ must appear explicitly. Centroids are defined
intrinsically by a Karcher mean inside a convex normal ball. A first-order
gradient parent flow yields a first-order modulation law; a Newtonian law
requires a separately specified inertial parent equation. Absolute interaction
bounds give $|E_{\rm int}|\le C\mathcal O$, while attraction or repulsion needs a
sign hypothesis. Structural transitions are controlled by a Lyapunov mountain-
pass/work theorem, and exit detection is separated from selection of the
post-transition basin.
\end{abstract}

\tableofcontents

\section{Inherited control framework}

We use the corrected FP--I/II Riemannian control geometry, joint internal
operators, and projected stabilization flow. The projector $P$ below is the
unperturbed joint harmonic projector and $Q=I-P$. FP--III supplies separate
deterministic and stochastic disturbance bounds. No statement here identifies
the stabilization parameter with physical Lorentzian time.

Existence of a projected step fixed point is inherited only after the corrected
Schauder/Darbo hypotheses are verified. Promotion to a full equilibrium uses
the strict Lyapunov identity of FP--II.

\section{Curved Laplace-type operator}

Let $E\to B$ be a Hermitian bundle with compatible connection $\nabla$. A
Laplace-type operator is written
\begin{equation}
L=\nabla^\ast\nabla+\mathcal R,
\label{eq:weitzenbock}
\end{equation}
where $\nabla^\ast\nabla\ge0$ is the rough/connection Laplacian and
$\mathcal R=\mathcal R^\ast$ is the curvature endomorphism. We identify the
unperturbed vertical operator with $A_0=\nabla^\ast\nabla$ in the selected
sector and assume
\[
\operatorname{spec}(A_0)\subset\{0\}\cup[\lambda_\ast,\infty),
\qquad \lambda_\ast>0.
\]

Relative to $P\oplus Q$, curvature has four blocks
\[
\mathcal R=
\begin{pmatrix}
P\mathcal RP&P\mathcal RQ\\
Q\mathcal RP&Q\mathcal RQ
\end{pmatrix}.
\]
Define the noncoherent negative-part and leakage bounds
\begin{align}
\operatorname{Re}\langle q,Q\mathcal RQq\rangle
&\ge-\rho_Q\|q\|^2,\\
\ell_{QP}&:=\|Q\mathcal RP\|.
\end{align}
The scalar lower bound $\rho_Q$ does not control the off-diagonal block
$Q\mathcal RP$.

\section{Gap persistence and the curved projector}

\begin{theorem}[Bounded-curvature cluster persistence]\label{thm:gap}
Assume $\mathcal R$ is bounded and self-adjoint with
$r:=\|\mathcal R\|<\lambda_\ast/2$. Then the spectrum of
$L=A_0+\mathcal R$ lies in the $r$-neighborhood of
$\operatorname{spec}(A_0)$. The low cluster and the remaining spectrum are
separated by at least
\[
\lambda_{\rm gap}^{\mathcal R}\ge\lambda_\ast-2r>0.
\]
A contour in this separation defines the full curved Riesz projector
\[
P_{\mathcal R}=\frac{1}{2\pi i}\int_\Gamma(z-L)^{-1}\,dz,
\]
which has the same finite rank as $P$ along the norm-continuous perturbation
$A_0+s\mathcal R$, $0\le s\le1$.
\end{theorem}

Using $P_{\mathcal R}$ eliminates linear leakage because
$[L,P_{\mathcal R}]=0$, but changes the coherent subspace. If the bounded-
perturbation condition is unavailable, gap persistence and the Riesz projector
must be proved directly for the full curved operator; the unperturbed gap may
not simply be reused.

For base-dependent curvature and projectors, modulation and locality estimates
also require bounds on $\nabla\mathcal R$, $\nabla P_{\mathcal R}$, and any
commutator with the base control operator. These gradient terms are not
contained in the scalar loss $\rho_Q$.

\section{Curvature leakage and stability floor}

Consider
\[
\partial_t\Psi=-(A_0+\mathcal R)\Psi-N(\Psi)+F,
\qquad p=P\Psi,quad q=Q\Psi.
\]
Assume unperturbed coherence invariance $QN(p)=0$ and the one-sided estimate
\[
\operatorname{Re}\langle q,Q(N(p+q)-N(p))\rangle
\ge-L_Q\|q\|^2.
\]

\begin{theorem}[Noncoherent leakage bound]\label{thm:leakage}
Let
\[
\gamma_Q:=\lambda_\ast-L_Q-\rho_Q>0.
\]
Then
\begin{equation}
D^+\|q(t)\|
\le-\gamma_Q\|q(t)\|+\ell_{QP}\|p(t)\|+\|QF(t)\|.
\label{eq:leakage-dini}
\end{equation}
Consequently,
\begin{align}
\|q(t)\|
&\le e^{-\gamma_Qt}\|q(0)\|\\
&\quad+\int_0^t e^{-\gamma_Q(t-s)}
\bigl(\ell_{QP}\|p(s)\|+\|QF(s)\|\bigr)\,ds.
\end{align}
If $p$ and $QF$ are uniformly bounded, then
\[
\limsup_{t\to\infty}\|q(t)\|
\le\frac{\ell_{QP}\sup_t\|p(t)\|+sup_t\|QF(t)\|}{\gamma_Q}.
\]
\end{theorem}

Thus positive damping need not drive the old $Q$ component to zero. Exact
decay to the old coherent sector requires $Q\mathcal RP=0$ and vanishing
noncoherent forcing, or replacement of $P$ by a verified curved projector.

\section{Intrinsic centroid and modulation}

Let
\[
d\nu_t(y)=\frac{\rho(y,t)\,d\operatorname{vol}_Y(y)}
{\int_Y\rho(\cdot,t)\,d\operatorname{vol}_Y}
\]
be the normalized density measure. Assume its support lies in a geodesically
convex normal ball on which the squared-distance functional is strictly
convex.

\begin{definition}[Karcher centroid]
The centroid is the unique minimizer
\[
X(t)=\operatorname*{argmin}_{z\in Y}
\frac12\int_Y d_Y(z,y)^2\,d\nu_t(y).
\]
\end{definition}

This definition is coordinate invariant. A coordinate average is used only
after choosing a normal chart and estimating its curvature-dependent error.

Let $\{\Psi_X:X\in\mathcal M\}$ be a smooth localized profile manifold and
write
\[
\Psi(t)=\Psi_{X(t)}+r(t),
\qquad
\langle r,\partial_{X^i}\Psi_X\rangle=0.
\]
Define the positive tangent Gram matrix
$G_{ij}(X)=\langle\partial_{X^i}\Psi_X,
\partial_{X^j}\Psi_X\rangle$ and
$V_{\rm eff}(X)=C[\Psi_X]$.

\begin{theorem}[First-order modulation law]\label{thm:modulation}
For the first-order gradient flow $\partial_t\Psi=-\nabla C(\Psi)$, assume the
profile decomposition is unique, $G(X)$ is uniformly invertible, and the
remainder and curvature-gradient terms are controlled. Projection onto the
tangent space gives
\[
G_{ij}(X)\dot X^j=-\partial_iV_{\rm eff}(X)+\varepsilon_i(t),
\]
where $\varepsilon_i$ is bounded by the modulation remainder, localization
width, $\nabla\mathcal R$, and projector-variation errors specified by the
model.
\end{theorem}

A second-order law
$M_{ij}(X)\ddot X^j+\cdots=-\partial_iV_{\rm eff}$ is retained only when the
parent field equation contains an explicit inertial/kinetic second-order term.
It does not follow from the FP first-order gradient flow.

\section{Overlap and interaction sign}

For two profiles define
\[
E_{\rm int}:=C[\Psi_1+\Psi_2]-C[\Psi_1]-C[\Psi_2].
\]
Let $\mathcal O(\Psi_1,\Psi_2)\ge0$ be a declared overlap functional.

\begin{assumption}[Absolute cross-term control]\label{ass:cross}
All quadratic and nonlinear cross terms obey
\[
|E_{\rm int}|\le C_{\rm int}\mathcal O(\Psi_1,\Psi_2).
\]
\end{assumption}

This assumption yields exactly the displayed absolute estimate. It does not
yield positive constants $c_1,c_2$ with
$c_1\mathcal O\le E_{\rm int}\le c_2\mathcal O$.

\begin{theorem}[Signed interaction criterion]\label{thm:sign}
If a model additionally proves
$E_{\rm int}\le-c\mathcal O$ with $c>0$, overlap lowers the energy and is
energetically attractive. If it proves
$E_{\rm int}\ge c\mathcal O$, overlap raises the energy and is energetically
repulsive. Neither sign follows from overlap magnitude alone.
\end{theorem}

Energetic attraction still does not prove dynamical merger. The flow must have
access to the merged basin and avoid intervening conserved quantities or
barriers.

\section{Existence and equilibrium status}

The corrected FP--I/II theorems apply to the curved flow only after the full
operator supplies the required sectoriality, smoothing, invariant set,
compactness/confinement, and projector hypotheses. A Schauder or Darbo result
first gives a projected step fixed point. It becomes an equilibrium only when
the strict Lyapunov identity is verified. Curvature does not preserve the old
fixed-point structure automatically.

\section{Structural transitions}

Let $\mathcal B_-$ and $\mathcal B_+$ be two basins for a continuous gradient
flow with Lyapunov energy $C$. Define the mountain-pass level
\[
c_{-+}:=\inf_{\gamma\in\Gamma_{-+}}\max_{s\in[0,1]}C(\gamma(s)),
\]
where $\Gamma_{-+}$ is the set of continuous paths joining the two basins.

\begin{theorem}[Energy-barrier exclusion with work]\label{thm:barrier}
Assume trajectories are continuous in the energy topology and satisfy
\[
C[\Psi(t)]\le C[\Psi(0)]+W_{\rm ext}(t),
\qquad W_{\rm ext}(t)\le W_\ast.
\]
If $C[\Psi(0)]+W_\ast<c_{-+}$, the trajectory cannot pass from
$\mathcal B_-$ to $\mathcal B_+$. For an unforced gradient flow,
$W_\ast=0$.
\end{theorem}

Noise-driven transitions require probabilistic exit estimates and are not
covered by this deterministic theorem.

\begin{theorem}[Exit does not determine selection]\label{thm:exit}
Let $\mathcal A$ be an admissible region and
$\tau_{\rm exit}=\inf\{t:\Psi(t)\notin\mathcal A\}$. Finite
$\tau_{\rm exit}$ detects loss of admissibility only. Identification of the
post-exit basin requires a separate basin-accessibility and convergence or
selection theorem.
\end{theorem}

\section{Conclusion}

Curvature is not merely a scalar subtraction from a damping margin. It can
shift the spectral cluster, rotate the coherent projector, and leak coherent
amplitude into the old noncoherent sector. FP IV v4 makes those effects
explicit. Centroid motion is intrinsic and first order for a gradient parent
flow; interaction signs and dynamic merger require additional hypotheses; and
barrier crossing is controlled by total energy plus work. These corrected
statements preserve the useful curvature and transition program without
claiming that overlap or positive damping alone selects a new physical basin.

"""
    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?(?=\\begin\{thebibliography\})",
        body,
        "paper body",
    )
    PAPER.write_text(text, encoding="utf-8", newline="\n")
    print(f"Updated {PAPER}")


if __name__ == "__main__":
    main()
