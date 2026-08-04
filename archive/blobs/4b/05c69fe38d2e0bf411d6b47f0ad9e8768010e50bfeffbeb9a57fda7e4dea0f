---
abstract: |
  We establish the Tier 2 results of Modal Triplet Theory (MTT): relations and
  bounds that require no internal metric solve and no harmonic norm evaluation,
  but go beyond purely topological statements.
  These results rely only on algebraic identities, symmetry assumptions,
  spectral positivity, and effective--field--theory control.
  They include: a high--scale electroweak mixing identity
  $\sin^2\theta_W = 3/8$ under modal democracy; sensitivity bounds around
  democracy; holonomy determinant and phase sum rules; qualitative
  renormalization--group sign structure; curvature--mass drift identities
  and FRW bounds; and a post--Newtonian estimate
  $\gamma = 1 + O(\Delta_{\mathrm{curv}})$.
  All results are exact identities or rigorous inequalities within their
  assumptions and form the geometry--light bridge between the topology--only
  (Tier 1) foundations and the calibratable and geometric tiers.
author:
- Peter Nero
date: January 2026
title: |
  Geometry--Light Relations in\
  Modal Triplet Theory (MTT)
---

# Introduction and Scope

This paper occupies Tier 2 in the tiered computational program of
Modal Triplet Theory (MTT).
Its purpose is to isolate statements that:

- do not depend on a detailed internal metric,

- do not require harmonic normalization integrals,

- but are not purely topological.

Tier 2 results are *geometry--light*: they depend on symmetry,
positivity, spectral gaps, or effective--field--theory structure, but not
on detailed geometric data.
They therefore provide nontrivial physical content while remaining robust
against model--dependent realization choices.

This paper should be read in conjunction with:

- the Tier 1 topology--only foundations, and

- the Tiered Roadmap for Calculations in MTT.

No Tier 3 calibration or Tier 4 string--lift input is used here.

# Tier--2 Contract

#### Definition

A statement belongs to Tier 2 if:

1.  it uses only algebraic identities, symmetry assumptions, or
    inequalities,

2.  it does not depend on internal metric data or harmonic norms,

3.  it is exact or bounded (not fitted),

4.  its assumptions are explicitly stated and minimal.

Typical Tier 2 assumptions include:

- equality of modal weights ("modal democracy"),

- existence of a spectral gap,

- smoothness and positivity of effective operators,

- standard EFT power counting.

Tier 2 results serve two roles:

1.  they already constrain physical observables,

2.  they define targets and consistency conditions for higher tiers.

# Preliminaries and Notation

At a matching scale $\Lambda$, gauge couplings are written as
$$\begin{equation}
\alpha_r^{-1}(\Lambda)
\equiv \frac{4\pi}{g_r^2(\Lambda)}
= K\,\zeta_r,
\qquad r \in \{1,2,3\},
\label{eq:alpha-zeta}
\end{equation}$$
where $K$ is a common scale and $\zeta_r > 0$ are dimensionless weights,
defined only up to overall normalization.

Hypercharge is taken in GUT normalization,
$$g' = \sqrt{\frac{3}{5}}\,g_1.$$

No assumption is made here about the numerical value of $K$ or the
$\zeta_r$ beyond those stated explicitly in each result.

# High--Scale Electroweak Mixing under Modal Democracy

We begin with the most direct Tier 2 relation: the value of the weak
mixing angle at a high matching scale under a symmetry assumption on
the modal weights.

## Modal democracy

#### Definition

At a matching scale $\Lambda$, we say that the electroweak sector
satisfies *modal democracy* if the corresponding modal weights are
equal,
$$\begin{equation}
\zeta_1 = \zeta_2 .
\label{eq:modal-democracy}
\end{equation}$$

This condition expresses symmetry of the underlying modal sectors and
does not depend on geometry, normalization, or absolute coupling values.

## High--scale identity

#### Theorem

Assume modal democracy Equation (modal-democracy).
With GUT normalization $g'=\sqrt{3/5}\,g_1$, the weak mixing angle at
the matching scale $\Lambda$ satisfies
$$\begin{equation}
\sin^2\theta_W(\Lambda) = \frac{3}{8}.
\end{equation}$$

#### Proof

*Proof.* By definition,
$$\sin^2\theta_W
= \frac{g'^2}{g'^2 + g_2^2}
= \frac{1}{1 + g_2^2/g'^2}.$$
Using GUT normalization $g'^2 = \tfrac{3}{5} g_1^2$,
$$\sin^2\theta_W
= \frac{1}{1 + \tfrac{5}{3}\, g_2^2/g_1^2}.$$
From Equation (alpha-zeta), $g_r^2 \propto 1/\zeta_r$, hence
$g_2^2/g_1^2 = \zeta_1/\zeta_2$.
Under modal democracy this ratio equals unity, yielding
$$\sin^2\theta_W(\Lambda)
= \frac{1}{1 + 5/3}
= \frac{3}{8}.$$ ◻

#### Remark

This identity is algebraic and exact within its assumptions.
It does not rely on renormalization--group evolution, unification, or
detailed internal geometry.

## Sensitivity around democracy

We now quantify the deviation of $\sin^2\theta_W$ from $3/8$ under small
departures from modal democracy.

#### Proposition

Let
$$r := \frac{\zeta_1}{\zeta_2} = 1 + \varepsilon ,
\qquad |\varepsilon| \ll 1.$$
Then
$$\begin{equation}
\sin^2\theta_W(\Lambda)
= \frac{3}{8}
\left(
1 - \frac{5}{8}\,\varepsilon
+ \frac{25}{64}\,\varepsilon^2
+ O(\varepsilon^3)
\right).
\label{eq:sw-expansion}
\end{equation}$$

#### Proof

*Proof.* From the general expression
$$\sin^2\theta_W
= \frac{1}{1 + \tfrac{5}{3} r},$$
set $r = 1 + \varepsilon$ and factor
$$1 + \tfrac{5}{3}(1+\varepsilon)
= \tfrac{8}{3}\left(1 + \tfrac{5}{8}\varepsilon\right).$$
Expanding $(1+x)^{-1}$ in $x=\tfrac{5}{8}\varepsilon$ yields
Equation (sw-expansion). ◻

#### Remark

The leading correction is linear and suppressed by a factor $5/8$.
Moderate deviations from modal democracy therefore induce only mild
shifts in $\sin^2\theta_W$ at the matching scale.

## Interpretation

The value $3/8$ is familiar from grand--unified embeddings.
Here it arises for a different reason: symmetry of modal weights rather
than group--theoretic unification.
Tier 2 does not assume exact unification, only the equality of two
effective normalization factors.

This distinction is important.
The result survives changes of matching scale, RGE scheme, and internal
realization, provided the modal democracy assumption holds.

# Holonomy Determinant and Phase Sum Rules

We now collect geometry--light constraints implied by the canonical
trivialization of the pairwise twisting bundles.

## Determinant and phase identities

Recall from Tier 1 that flux balance implies a canonical trivialization
$$L_{12} \otimes L_{23} \otimes L_{31} \cong \mathbb{C}.$$

#### Theorem

Let $U_{ij}(\gamma)$ denote parallel transport on $L_{ij}$ along a closed
loop $\gamma \subset Y_4$.
Then
$$\begin{equation}
\det U_{12}(\gamma)\,
\det U_{23}(\gamma)\,
\det U_{31}(\gamma)
= 1 .
\end{equation}$$
Equivalently,
$$\begin{equation}
\arg \det U_{12}
+ \arg \det U_{23}
+ \arg \det U_{31}
\in 2\pi \mathbb{Z}.
\end{equation}$$

#### Proof

*Proof.* Choose unitary connections $A_{ij}$ on $L_{ij}$.
The induced connection on the tensor product is
$A_{12}+A_{23}+A_{31}$, which by triviality is pure gauge.
Its holonomy around any closed loop is therefore unity. ◻

#### Remark

This identity constrains relative CP--violating phases across sectors
without fixing their individual values.
It will later restrict CKM/PMNS phase assignments in Tier 4 realizations.

# Renormalization--Group Sign Structure

Tier 2 also includes qualitative information about renormalization
group flow that depends only on representation content.

#### Proposition

At one loop, the beta function
$$\beta(g) := \mu \frac{dg}{d\mu}
= -\frac{g^3}{16\pi^2} b_0 + O(g^5)$$
has coefficient
$$b_0
= \frac{11}{3} C_A
- \frac{4}{3} \sum_f T(R_f)
- \frac{1}{6} \sum_s T(R_s),$$
where the sums run over Weyl fermions and complex scalars.
For Standard Model matter content,
$$b_0^{SU(3)} > 0,
\qquad
b_0^{SU(2)} > 0,
\qquad
b_0^{U(1)} < 0 .$$

#### Proof

*Proof.* This is the standard one--loop result.
The sign depends only on the adjoint Casimir and the Dynkin indices of
the matter representations; no geometry enters. ◻

#### Remark

Tier 2 records only the qualitative sign information.
Quantitative running and matching are deferred to Tier 3.

# Curvature--Mass Drift Identities

We now consider relations between curvature and effective mass scales
that follow from the fixed--point structure of MTT.

#### Theorem

Let an effective mass scale be given by
$$m(x)
= \sqrt{\kappa\bigl(\lambda^{(0)} + \beta R(x)\bigr)},
\qquad
\lambda^{(0)} > 0 .$$
Then
$$\begin{equation}
\nabla_\mu \log m(x)
= \frac{\beta}{2\bigl(\lambda^{(0)}+\beta R(x)\bigr)}
\,\nabla_\mu R(x).
\end{equation}$$

#### Proof

*Proof.* Take the logarithm of $m(x)$ and differentiate. ◻

#### Corollary

If $\lambda^{(0)} + \beta R(x) \ge \lambda_{\min} > 0$ uniformly, then
$$\begin{equation}
\bigl\lvert \nabla_\mu \log m(x) \bigr\rvert
\le
\frac{|\beta|}{2\lambda_{\min}}
\,\lvert \nabla_\mu R(x) \rvert .
\end{equation}$$

## FRW specialization

In a spatially homogeneous FRW spacetime, $R=R(t)$, yielding
$$\begin{equation}
\left\lvert \frac{\dot m}{m} \right\rvert
\le
\frac{|\beta|}{2\lambda_{\min}}
\,|\dot R(t)|.
\end{equation}$$

#### Remark

These relations provide geometry--light bounds on cosmological mass
drift and are independent of the detailed internal realization.

# Post--Newtonian Bound

Tier 2 also yields a bound on post--Newtonian deviations.

#### Theorem

Let $\Delta_{\mathrm{curv}}$ denote the fixed--point curvature remainder
in the effective gravitational equations.
In the weak--field, stationary regime,
$$\begin{equation}
\gamma = 1 + O(\Delta_{\mathrm{curv}}).
\end{equation}$$

#### Proof

*Proof.* In de Donder gauge, linearized gravity obeys
$$\square \bar h_{\mu\nu}
= -16\pi G_N T_{\mu\nu} + S_{\mu\nu},$$
where $S_{\mu\nu}$ encodes curvature--suppressed corrections.
If $\|S\| \le C\,\Delta_{\mathrm{curv}}\|T\|$, the spatial and temporal
metric potentials differ only at $O(\Delta_{\mathrm{curv}})$. ◻

#### Remark

Solar--system bounds therefore translate directly into constraints on
$\Delta_{\mathrm{curv}}$.
These will serve as non--geometric closures in Tier 3.

# Conclusions

We have collected the Tier 2 results of Modal Triplet Theory:
relations and bounds that require no internal metric solve but provide
nontrivial physical content.
They rely only on symmetry, algebraic identities, positivity, and EFT
control.

Tier 2 serves as the bridge between:

- the exact, topology--only foundations of Tier 1, and

- the calibratable and geometric tiers that follow.

In particular, Tier 2 already fixes high--scale electroweak mixing under
a symmetry assumption, constrains CP--violating phases, bounds
curvature--induced mass drift, and limits post--Newtonian deviations.
These results define targets and consistency conditions for the
subsequent Tier 3 calibration and Tier 4 realization of MTT.

::: thebibliography
99

P. Nero,
*Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255621>

P. Nero,
*Modal Triplet Theory: Foundation*,
Zenodo preprint, September 2025.
<https://doi.org/10.5281/zenodo.16949762>

P. Nero,
*Fixed Points I--VI: Complete Coherence Spine*,
Zenodo preprints, August 2025.
<https://doi.org/10.5281/zenodo.16948748>

P. Nero,
*The Projection--Admissibility Principle: Structural Constraints on Effective Physical Description*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255838>

P. Nero,
*Closure and Inevitability in Modal Triplet Theory*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255510>

P. Nero,
*Coherence Capacity as the Fundamental Resource of Effective Physics*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255905>

P. Nero,
*Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18256048>

P. Nero,
*Modal Triplet Theory: From MTT to Quantum Mechanics*,
Zenodo preprint, September 2025.
<https://doi.org/10.5281/zenodo.17074246>

P. Nero,
*From MTT to Quantum Field Theory*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17068816>

P. Nero,
*Modal Triplet Theory: From MTT to General Relativity*,
Zenodo preprint, October 2025.
<https://doi.org/10.5281/zenodo.16950597>

P. Nero,
*Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17077671>

P. Nero,
*Measurement as Disturbance and Stabilization in Modal Triplet Theory*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17177404>

P. Nero,
*Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18256408>

P. Nero,
*Modal Fixed Points, Bell's Beables, and the Limits of Factorization*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17076300>

P. Nero,
*Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*,
Zenodo preprint, August 2025.
<https://doi.org/10.5281/zenodo.18208884>

P. Nero,
*From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18254862>
:::
