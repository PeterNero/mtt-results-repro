# UST.G3B Scale-Orbit and Dimensionless-Readout Theorem v1

**Date:** 2026-08-03

**Status:** `EXACT_COMMON_SCALE_QUOTIENT_THEOREM_PHYSICAL_SCALE_SELECTION_OPEN`

## 1. Scope

The locked q79 Hodge-action theorem reduces the bare closure-charge square to
one positive scale ray. `UST.G2` corrects the physical Hessian to

\[
H_{\mathrm{phys}}=\Delta_{\mathcal Y,1}+K^\dagger K
\]

for an orthogonal residual target. This theorem determines what remains
invariant when one common positive normalization multiplies the complete
physical residual norm.

It does not select the physical scale. It also does not erase independently
weighted residual sectors. The one-ray conclusion applies only after the
relative target metric and the physical operator `K` have been selected.

## 2. Common-Scale Theorem

Let `H` be a nonnegative self-adjoint operator with compact resolvent and let
`lambda > 0`. Define

\[
H_\lambda=\lambda H.
\]

Then:

\[
\ker H_\lambda=\ker H,
\qquad
P_{0,\lambda}=P_0,
\qquad
P_{+,\lambda}=P_+.
\]

The eigenspaces are unchanged and every positive eigenvalue scales uniformly:

\[
\mu_j(H_\lambda)=\lambda\mu_j(H).
\]

On the orthogonal complement of the kernel, the reduced Green operator obeys

\[
G_\lambda=\lambda^{-1}G.
\]

Consequently, positive spectral ratios, multiplicities, eigenspace
representations and condition numbers of fixed finite spectral truncations are
scale invariant.

The semigroups satisfy

\[
e^{-tH_\lambda}=e^{-(\lambda t)H},
\qquad
e^{-itH_\lambda}=e^{-i(\lambda t)H}.
\]

Thus the common scale fixes the conversion between internal repair time and a
physical clock; it does not change the dimensionless orbit structure.

## 3. Full-Residual Application

Let

\[
\Phi=(\Phi_{MC},R_{phys})
\]

use one selected target metric. Multiplying that entire target metric by
`lambda`, equivalently replacing `Phi` by `sqrt(lambda) Phi`, gives

\[
J_\lambda=\sqrt\lambda J,
\qquad
K_\lambda=\sqrt\lambda K,
\]

and hence

\[
H_{phys,\lambda}
=\lambda\left(\Delta_{\mathcal Y,1}+K^\dagger K\right).
\]

The physical extra rows may change the harmonic space through
`ker(Delta_Y) intersect ker(K)`, but an overall positive normalization cannot
change it afterward.

For a general target metric

\[
W=\begin{pmatrix}W_0&C\\C^\dagger&W_R\end{pmatrix},
\]

uniform replacement `W -> lambda W` gives `H_W -> lambda H_W`. By contrast,
independent replacements of `W_0`, `C` or `W_R` generally change dimensionless
operator shape. Such relative weights are physical source data, not part of
the harmless common scale ray.

## 4. Nonlinear and Newton Consequences

Let `E` be a twice differentiable repair cost and define

\[
E_\lambda=\lambda E.
\]

Its critical points are unchanged. At a nondegenerate critical point, or on a
fixed reduced complement using the Moore-Penrose inverse,

\[
\nabla E_\lambda=\lambda\nabla E,
\qquad
\operatorname{Hess}E_\lambda=\lambda\operatorname{Hess}E,
\]

so the Newton correction is invariant:

\[
-(\operatorname{Hess}E_\lambda)^+\nabla E_\lambda
=-(\operatorname{Hess}E)^+\nabla E.
\]

The common scale therefore cannot select a different local solution branch.
It can change gradient-flow speed, absolute fluctuation frequencies and the
normalization of the physical action.

## 5. Finite Readouts

For an exact isometric same-source readout `T_fin`,

\[
H_{fin,\lambda}=T_{fin}H_\lambda T_{fin}^\dagger
=\lambda H_{fin}.
\]

The finite kernel, spectral projectors, normalized eigenspaces, eigenvectors
under any fixed basis convention, and matrices such as

\[
\widehat H_{fin}=\frac{H_{fin}}{\operatorname{tr}_+(H_{fin})}
\]

are invariant. Absolute finite eigenvalues are not. An approximate readout
must scale its error bounds consistently; this theorem does not turn an
uncertified approximation into an exact map.

## 6. What Can Proceed Before Scale Selection

Conditional on the selected physical endpoint and relative target metric, the
following can be computed on the positive-ray quotient:

- harmonic dimension and projector;
- automorphism representations on zero and positive modes;
- normalized mode shapes and spectral ratios;
- normalized finite matrices and dimensionless interaction tensors;
- local Newton direction and branch uniqueness tests.

The following remain scale dependent:

- absolute eigenvalues, masses and gaps;
- conversion of repair parameter to physical time;
- absolute action, energy, length, Planck and Newton normalization;
- any observable whose units are not removed by a declared ratio.

## 7. Parameter Ledger

After selecting all relative physical row weights, the full repair Hessian has

```text
dimensionless Hodge-shape parameters: 0
common positive normalization rays:   at most 1
empirical fitted values introduced:   0
```

If separate sector weights remain, this ledger does not apply: each
unselected ratio is an additional dimensionless source parameter and must be
reported in `UST.G3`.

## 8. Frontier Delta

Closed:

- common-scale action on the corrected full physical Hessian;
- invariance of kernel, projectors, eigenspaces, ratios and Newton correction;
- inverse scaling of the reduced Green operator;
- normalized finite-readout invariance;
- exact distinction between one overall ray and unselected relative weights.

Open:

- selected physical endpoint and `K`;
- selected relative target metric;
- derivation or binding of the positive physical normalization;
- absolute mass/time/Planck/Newton conversion;
- physical cyclic/BV action theorem.

This closes `UST.G3B` universally and does not promote `UST.G3`.

## 9. Subsequent Repair-Metric Binding

`UST.G2P` subsequently binds the minimal orthogonal endpoint-induced `L2`
metric at structural repair tier. Once the physical endpoint supplies the
coefficients of `K`, this is sufficient to compute the scale-free repair
outputs listed in Section 6. It does not prove that the metric is uniquely
source-forced or is the physical action metric, and it does not select the
remaining common absolute scale.
