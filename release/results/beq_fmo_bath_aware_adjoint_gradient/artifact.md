# Bath-Aware Discrete Adjoint Gradient Theorem

## Setting

Fix one finite HEOM rung, one pulse duration `T`, and `N` piecewise-constant
three-axis control rows `u_j`. Let

\[
L_j=L_0+\sum_{a=1}^3 u_{j,a}L_a,
\qquad
S_j=\exp(\Delta t L_j^*),
\qquad
\Delta t=T/N.
\]

The terminal weighted population observable is a hierarchy vector `x_N`. Its
bath-active pullback is computed in reverse segment order,

\[
x_j=S_jx_{j+1},\qquad j=N-1,\ldots,0.
\]

Let `P` restrict the root ADO to the seven-dimensional single-exciton block, and
let `o` be the vectorized target root observable. Define

\[
J(u)=\frac{\|Px_0-o\|_2^2}{\|o\|_2^2}.
\]

## Theorem

Set

\[
p_0=\frac{P^*(Px_0-o)}{\|o\|_2^2},
\qquad
p_{j+1}=S_j^*p_j=\exp(\Delta t L_j)p_j.
\]

Then the exact derivative of the finite-rung, finite-segment objective is

\[
\boxed{
\frac{\partial J}{\partial u_{j,a}}
=2\operatorname{Re}\left\langle
p_j,
\mathcal L_{\exp}
(\Delta t L_j^*,\Delta t L_a^*)x_{j+1}
\right\rangle ,
}
\]

where `L_exp(A,E)` is the Frechet derivative of the matrix exponential at `A`
in direction `E`.

## Proof

Only `S_j` depends on `u_{j,a}` at segment `j`. The chain rule and the defining
property of the Frechet derivative give

\[
d x_j=
\mathcal L_{\exp}(\Delta t L_j^*,\Delta t L_a^*)x_{j+1},d u_{j,a}.
\]

Moving the objective differential from `x_0` through the earlier segment maps
produces `p_j`. Since the controls are real,

\[
dJ=2\operatorname{Re}\langle p_j,d x_j\rangle,
\]

which is the displayed formula.

For sparse execution, no dense Frechet matrix is required. The block identity

\[
\exp\begin{pmatrix}A&E\\0&A\end{pmatrix}
\begin{pmatrix}0\\v\end{pmatrix}
=
\begin{pmatrix}\mathcal L_{\exp}(A,E)v\\e^A v\end{pmatrix}
\]

computes each derivative action with one sparse exponential action.

## Scope

This theorem is exact for the selected finite HEOM generator and discrete control
family. It supplies a bath-aware gradient; it does not prove global optimality,
HEOM convergence, physical `K_ij`, absolute-field calibration, or detector
realizability. A candidate found at an economical rung must still be replayed on
a predeclared depth/bath-expansion ladder.
