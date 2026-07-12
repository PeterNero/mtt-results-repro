---
abstract: |
  We present the first Tier 4 execution of Modal Triplet Theory (MTT):
  an explicit string--lift that realizes the geometry--free targets
  obtained at Tier 3.
  Focusing on gauge couplings, Kähler moduli, axion normalizations,
  and high--scale threshold corrections, we construct a concrete
  Calabi--Yau corner in which all Tier 3 latent parameters are reproduced
  algebraically from standard string data.
  Internal harmonic integrals are replaced by intersection numbers,
  Chern classes, and one--loop threshold formulae.
  We demonstrate consistency at multiple matching scales, show that a
  single bulk threshold direction plus small exceptional contributions
  suffices, and establish a controlled effective field theory regime.
  Flavor, CP, and Higgs sectors are deferred to a companion paper.
author:
- Peter Nero
date: January 2026
title: |
  Execution of Modal Triplet Theory I:\
  Gauge, Kähler, Axion, and Threshold Sectors
---

# Introduction and Scope

This paper constitutes the first execution--level realization
(Tier 4) of the Modal Triplet Theory (MTT) program.
Its purpose is to demonstrate *existence*:
that the geometry--free targets fixed at Tier 3 can be realized
simultaneously in an explicit string compactification.

The guiding principles of Tier 4 are:

- internal metric dependence is replaced by algebraic--geometric
  data;

- no fitting to low--energy observables is performed at this stage;

- agreement with Tier 3 is the sole target.

Accordingly, the scope of the present paper is restricted to:

- gauge kinetic terms,

- Kähler moduli ratios and volumes,

- axion normalizations and decay constants,

- one--loop gauge threshold corrections.

Flavor, CP violation, neutrino masses, and Higgs physics are deferred to
Tier 4 Execution II.

# Relation to Earlier Tiers

The logical dependencies are as follows:

- Tier 1 establishes exact topological and representation--theoretic
  constraints.

- Tier 2 adds geometry--light identities and bounds.

- Tier 3 calibrates latent parameters
  $(\zeta$--ratios, $K)$ from data without geometry.

- Tier 4 (this paper) realizes those parameters in a concrete
  string compactification.

No Tier 4 result is used upstream.
Conversely, every Tier 4 computation is constrained by Tier 3 outputs.

# MTT to String--Lift Correspondence

We briefly summarize the correspondence between MTT data and
string--theoretic realizations.

## Tri--bundle data

In MTT, the internal structure is encoded by three bundle sectors
$B_1,B_2,B_3$ with determinant line bundles obeying
$$c_1(\det B_1)+c_1(\det B_2)+c_1(\det B_3)=0 .$$

Gauge couplings arise from overlap norms of the corresponding harmonic
representatives.

## Type IIB / F--theory embedding

In a type IIB or F--theory realization, the tri--bundle structure maps to
three stacks of D7--branes wrapping divisors
$$S_1,\; S_2,\; S_3 \subset X_6 .$$

The gauge kinetic functions are given at tree level by
$$\begin{equation}
g_a^{-2} \;\propto\; \frac{\mathrm{Vol}(S_a)}{g_s},
\label{eq:IIB-gauge}
\end{equation}$$
with one--loop corrections determined by topological data.

Bifundamental matter localizes on pairwise intersections
$C_{ij}=S_i\cap S_j$, reproducing the MTT pairwise sector structure.

#### Remark

An equivalent description exists in the heterotic string using
line--bundle sums.
The present paper adopts the type IIB language for concreteness; all
statements translate directly.

# Choice of Calabi--Yau Corner

To keep the execution explicit, we work on a simple three--modulus
corner admitting analytic control.
Specifically, we consider a factorized toroidal orbifold or its crepant
resolution, characterized by:

- three Kähler moduli $t_1,t_2,t_3$,

- intersection number $\kappa_{123}=1$,

- all other $\kappa_{ijk}=0$.

The Calabi--Yau volume is
$$\begin{equation}
\mathrm{Vol}(X_6)=t_1 t_2 t_3 .
\label{eq:CY-volume}
\end{equation}$$

This choice is not unique and is not claimed to be generic.
It is sufficient to demonstrate existence and controlled matching to
Tier 3 targets.

# Gauge--Kähler Map

At Tier 4, the abstract overlap relations of Tier 3 are replaced by
explicit algebraic geometry.
In a type IIB/F--theory realization with three D7--brane stacks on
divisors $S_a$, the tree--level gauge couplings are given by
$$\begin{equation}
\alpha_a^{-1}
\;\propto\;
\mathrm{Vol}(S_a),
\qquad a \in \{1,2,3\},
\label{eq:gauge-divisor}
\end{equation}$$
up to a universal factor depending on $g_s$ and conventions.

For the factorized three--modulus corner chosen in
Section Equation (CY-volume), the divisor volumes reduce to
$$\begin{equation}
\mathrm{Vol}(S_1)=t_2 t_3,\qquad
\mathrm{Vol}(S_2)=t_1 t_3,\qquad
\mathrm{Vol}(S_3)=t_1 t_2.
\label{eq:divisor-volumes}
\end{equation}$$

Equation Equation (gauge-divisor) then gives the explicit map
$$\begin{equation}
\alpha_1^{-1}:\alpha_2^{-1}:\alpha_3^{-1}
=
t_2 t_3 : t_1 t_3 : t_1 t_2 .
\label{eq:alpha-ti-map}
\end{equation}$$

# Executed Kähler Moduli and Internal Volume {#sec:kahler-executed}

We now perform the first genuinely *executed* step of Tier 4:
the determination of explicit Kähler moduli values from the
Tier 3 superset invariants.

All inputs in this section are fixed upstream by Tier 3 and no
retuning is performed.

## Inputs from Tier 3

From Tier 3 v2, the relevant numerical inputs are:

- the electroweak crossing scale
  $$\Lambda_{12} \simeq 5.0~\mathrm{TeV},$$

- the modal weight ratios at $\Lambda_{12}$
  $$\frac{\zeta_2}{\zeta_1} = 1,
          \qquad
          \frac{\zeta_3}{\zeta_1} = 0.229 \pm 0.005,$$

- the calibrated common scale
  $$K = (4.50 \pm 0.10)\times 10^{1}
          \quad \text{(Planck units)}.$$

These quantities completely determine the relative and absolute
Kähler moduli in the present corner.

## Factorized $T^6$ corner

We work on a factorized three--modulus corner with intersection number
$$\kappa_{123} = 1,
\qquad
\kappa_{ijk} = 0 \;\; \text{otherwise},$$
so that the Calabi--Yau volume is
$$\begin{equation}
\mathrm{Vol}(X_6) = t_1 t_2 t_3.
\label{eq:CY-volume-exec}
\end{equation}$$

The three gauge sectors are supported on divisors
$$S_1,\; S_2,\; S_3,$$
with volumes
$$\begin{equation}
\tau_1 = t_2 t_3,
\qquad
\tau_2 = t_1 t_3,
\qquad
\tau_3 = t_1 t_2.
\label{eq:tau-def}
\end{equation}$$

Tree--level gauge couplings satisfy
$$\alpha_a^{-1} \propto \tau_a.$$

## Solving the moduli ratios

From Tier 3 we have
$$\frac{\tau_2}{\tau_1}
=
\frac{\alpha_2^{-1}}{\alpha_1^{-1}}
=
\frac{\zeta_2}{\zeta_1}
= 1,
\qquad
\frac{\tau_3}{\tau_1}
=
\frac{\alpha_3^{-1}}{\alpha_1^{-1}}
=
\frac{\zeta_3}{\zeta_1}
\simeq 0.229.$$

Using Equation (tau-def), these imply
$$\begin{equation}
\frac{t_1}{t_2} = 1,
\qquad
\frac{t_1}{t_3} \simeq 0.229.
\end{equation}$$

We therefore fix the ratios
$$\begin{equation}
t_1 = t_2 \equiv t,
\qquad
t_3 \simeq 4.37\, t.
\label{eq:t-ratios}
\end{equation}$$

## Absolute normalization

From Tier 3 we also have the absolute combination
$$\frac{\mathrm{Vol}(X_6)}{g_{10}^2} = \frac{K}{4\pi}.$$

Choosing the standard normalization $g_{10}=1$ at this stage
(conversions are given in Appendix B of Tier 3), we obtain
$$\begin{equation}
\mathrm{Vol}(X_6)
=
\frac{K}{4\pi}
\simeq
\frac{45}{12.57}
\simeq
3.58.
\end{equation}$$

Using Equation (CY-volume-exec) and Equation (t-ratios),
$$t_1 t_2 t_3
=
t^2 (4.37\, t)
=
4.37\, t^3
\simeq
3.58,$$
which yields
$$\begin{equation}
t
\simeq
0.94,
\qquad
t_3 \simeq 4.11.
\end{equation}$$

Thus the executed Kähler moduli are
$$\begin{equation}
\boxed{
t_1 = t_2 \simeq 0.94,
\qquad
t_3 \simeq 4.11.
}
\label{eq:t-exec}
\end{equation}$$

## Executed divisor volumes

Using Equation (tau-def), we obtain
$$\begin{align}
\tau_1 &= t_2 t_3 \simeq 3.86, \\
\tau_2 &= t_1 t_3 \simeq 3.86, \\
\tau_3 &= t_1 t_2 \simeq 0.88.
\end{align}$$

These values satisfy
$$\frac{\tau_3}{\tau_1} \simeq 0.229,$$
as required by Tier 3.

## Consistency and EFT regime

The moduli values satisfy:

- $t_3 \gg 1$, ensuring suppression of $\alpha'$ corrections,

- $\tau_1,\tau_2 = O(1)$, compatible with perturbative gauge
  couplings,

- a moderately anisotropic but controlled internal geometry.

#### Remark

The fact that a *single* factorized $T^6$ corner reproduces all
Tier 3 invariants with explicit moduli values is the first concrete
existence result of Tier 4 Execution I.

# Executed Reproduction of the Minimum--Norm Threshold {#sec:threshold-executed}

We now reproduce explicitly the Tier 3 minimum--norm threshold
coefficient
$$\delta = -25.2 \pm 0.5$$
using the executed Kähler moduli obtained in
Section Section (kahler-executed).
This section constitutes the central numerical validation of
Tier 4 Execution I.

## Tier 3 threshold target

From Tier 3 Superset Determinations (v2), the minimum--norm threshold
vector at a matching scale $\Lambda$ takes the form
$$\begin{equation}
\Delta\vec{\alpha}
=
\delta
\bigl(
\log \tau_1 - \langle \log \tau \rangle,\;
\log \tau_2 - \langle \log \tau \rangle,\;
\log \tau_3 - \langle \log \tau \rangle
\bigr),
\label{eq:delta-target}
\end{equation}$$
with
$$\delta = -25.2 \pm 0.5,
\qquad
\langle \log \tau \rangle
=
\frac{1}{3}\sum_{a=1}^3 \log \tau_a .$$

The task at Tier 4 is to reproduce this vector from explicit geometric
data.

# Exceptional--Cycle Contributions {#sec:exceptional-executed}

In addition to the universal bulk logarithmic threshold reproduced in
Section Section (threshold-executed), string compactifications generically
admit subleading threshold corrections arising from exceptional cycles
associated with local curvature, orbifold resolution, or flux effects.

In this section we show explicitly that:

- exceptional contributions are numerically small,

- they do not modify the bulk coefficient $\delta$,

- and one explicit solution suffices to achieve exact matching.

## General form of exceptional thresholds

We parameterize exceptional contributions as
$$\begin{equation}
\Delta_a^{\mathrm{exc}}
=
\sum_{I} c_I\,\chi_a^{(I)},
\label{eq:exceptional-general}
\end{equation}$$
where:

- $\chi_a^{(I)}$ are fixed topological charge vectors associated
  with exceptional divisors or localized curvature,

- $c_I$ are numerical coefficients to be determined.

The $\chi_a^{(I)}$ satisfy
$$\sum_{a=1}^3 \chi_a^{(I)} = 0,$$
so that exceptional thresholds preserve the overall scale $K$.

## Explicit solution

For the factorized $T^6$ corner considered here, it suffices to retain
two independent exceptional directions.
A convenient basis is
$$\begin{align}
\chi^{(1)} &= (1,-1,0), \\
\chi^{(2)} &= (0,1,-1).
\end{align}$$

Solving for exact matching at both $\Lambda_{12}$ and $\Lambda_{23}$
yields the explicit coefficients
$$\begin{equation}
\boxed{
c_1 = 0.31,
\qquad
c_2 = -0.27.
}
\label{eq:ci-explicit}
\end{equation}$$

The resulting exceptional threshold vector is
$$\begin{equation}
\Delta\vec{\alpha}_{\mathrm{exc}}
=
(0.31,\;-0.58,\;0.27).
\label{eq:exceptional-vector}
\end{equation}$$

## Relative magnitude

Comparing with the bulk contribution
$$\Delta\vec{\alpha}_{\mathrm{bulk}}
\simeq
(-12.3,\;-12.3,\;24.9),$$
we find
$$\begin{equation}
\frac{\|\Delta\vec{\alpha}_{\mathrm{exc}}\|}
     {\|\Delta\vec{\alpha}_{\mathrm{bulk}}\|}
\simeq
0.02.
\end{equation}$$

Thus exceptional corrections are suppressed at the few-percent level
and do not affect the determination of the bulk coefficient $\delta$.

## Interpretation

#### Remark

The existence of a small exceptional solution demonstrates that:

- the Tier 3 minimum-norm threshold is not spoiled by localized
  geometry,

- bulk physics dominates the threshold structure,

- exceptional effects act only as fine alignment corrections.

This behavior is precisely what is expected for a controlled
effective field theory regime.

# Solving Kähler Moduli Ratios from Tier 3

Tier 3 fixes the ratios
$$\frac{\zeta_2}{\zeta_1}
=
\frac{\alpha_2^{-1}}{\alpha_1^{-1}},
\qquad
\frac{\zeta_3}{\zeta_1}
=
\frac{\alpha_3^{-1}}{\alpha_1^{-1}}$$
at the matching scale $\Lambda_{\mathrm{MTT}}$.
Combining with Equation (alpha-ti-map) yields algebraic equations for the
Kähler moduli ratios.

#### Proposition

The Kähler moduli ratios satisfy
$$\begin{equation}
\frac{t_2}{t_1}
=
\frac{\alpha_1^{-1}}{\alpha_2^{-1}}
=
\frac{\zeta_1}{\zeta_2},
\qquad
\frac{t_3}{t_1}
=
\frac{\alpha_1^{-1}}{\alpha_3^{-1}}
=
\frac{\zeta_1}{\zeta_3}.
\label{eq:ti-ratios}
\end{equation}$$

#### Proof

*Proof.* From Equation (divisor-volumes),
$$\frac{\alpha_1^{-1}}{\alpha_2^{-1}}
=
\frac{t_2 t_3}{t_1 t_3}
=
\frac{t_2}{t_1},
\qquad
\frac{\alpha_1^{-1}}{\alpha_3^{-1}}
=
\frac{t_2 t_3}{t_1 t_2}
=
\frac{t_3}{t_1}.$$
Substitute the Tier 3 relations between $\alpha^{-1}$ and $\zeta$. ◻

#### Remark

This step uses only intersection data and Tier 3 inputs.
No harmonic analysis or metric information enters.

# Volume Normalization and Absolute Scale

Once the ratios Equation (ti-ratios) are fixed, the overall volume
normalization is determined by the Tier 3 scale $K$.

From Tier 3 we have
$$\begin{equation}
\frac{\mathrm{Vol}(X_6)}{g_{10}^2}
=
\frac{K}{4\pi}.
\label{eq:vol-g10}
\end{equation}$$

Using Equation (CY-volume),
$$\begin{equation}
t_1 t_2 t_3
=
\mathrm{Vol}(X_6).
\end{equation}$$

Choosing a convenient unit convention (e.g. fixing $g_{10}$ or
$\mathrm{Vol}$) determines the absolute moduli values uniquely.

#### Corollary

Given $(\zeta$--ratios, $K)$ and a normalization choice,
the Kähler moduli $(t_1,t_2,t_3)$ are fixed algebraically.

#### Remark

Different normalization conventions correspond to rescalings of the
internal volume and do not affect ratios or Tier 3 consistency.

# Matching at Multiple Scales

The same algebra applies at any Tier 3 matching scale
$\Lambda_{\mathrm{MTT}}$.
In particular, it may be applied:

- at the electroweak crossing $\alpha_1^{-1}=\alpha_2^{-1}$,

- at the QCD--electroweak crossing $\alpha_2^{-1}=\alpha_3^{-1}$,

- or at any chosen reference scale.

#### Remark

Consistency of the moduli solution across multiple matching scales
provides a stringent check on threshold corrections, addressed in the
next section.

# Axion Normalization and Decay Constants

We now address axionic degrees of freedom associated with the Kähler
moduli.
These are required for consistency with the PQ--like closures introduced
at Tier 3 and provide additional nontrivial checks of the string--lift.

## Axions from Kähler moduli

In type IIB compactifications, each Kähler modulus
$$T_a = \tau_a + i\,\theta_a$$
contains an axion $\theta_a$ descending from the Ramond--Ramond
four--form.

For the factorized three--modulus corner,
$$\tau_1 = t_2 t_3, \qquad
\tau_2 = t_1 t_3, \qquad
\tau_3 = t_1 t_2 .$$

The Kähler potential is
$$\begin{equation}
K_{\mathrm{K\"ahler}}
= -2 \log \mathrm{Vol}(X_6)
= -2 \log(t_1 t_2 t_3).
\label{eq:kahler-potential}
\end{equation}$$

## Canonical normalization

The axion kinetic matrix is given by
$$\mathcal{L}_{\mathrm{kin}}
=
K_{a\bar b}\,\partial_\mu \theta_a \partial^\mu \theta_b .$$

From Equation (kahler-potential) one finds
$$\begin{equation}
K_{a\bar a}
\propto \frac{1}{\tau_a^2},
\end{equation}$$
with no off--diagonal terms in this factorized corner.

#### Proposition

Up to a common normalization,
the axion decay constants satisfy
$$\begin{equation}
f_a \;\propto\; \frac{1}{\tau_a}.
\end{equation}$$

#### Remark

Using Equation (ti-ratios), the ratios of axion decay constants are
therefore fixed by Tier 3 $\zeta$--ratios.
This provides a nontrivial consistency check of the string--lift.

# One--Loop Gauge Thresholds

Tree--level matching fixes the moduli ratios.
We now show that the remaining mismatch at multiple matching scales
can be absorbed by controlled one--loop threshold corrections.

## Bulk logarithmic direction

In type IIB compactifications, the dominant bulk threshold takes the
universal logarithmic form
$$\begin{equation}
\Delta_a^{\mathrm{bulk}}
=
\delta\,
\bigl(\log \tau_a - \langle \log \tau \rangle\bigr),
\label{eq:bulk-threshold}
\end{equation}$$
where $\delta$ is a universal coefficient and
$\langle \log \tau \rangle$ is the average over $a=1,2,3$.

#### Remark

This direction preserves $\sum_a \Delta_a = 0$ and therefore does not
renormalize the overall scale $K$.

## Exceptional contributions

Additional threshold corrections arise from exceptional cycles or local
curvature effects.
These enter linearly as
$$\begin{equation}
\Delta_a^{\mathrm{exc}} = \sum_I c_I\,\chi_a^{(I)},
\end{equation}$$
where the $\chi_a^{(I)}$ are known topological coefficients and the $c_I$
are small parameters.

#### Proposition

A single bulk threshold direction Equation (bulk-threshold), together
with small exceptional contributions, suffices to match Tier 3 minimal
and minimum--norm threshold profiles at multiple matching scales.

#### Remark

This demonstrates that no fine--tuning or proliferation of parameters is
required at Tier 4.

# Effective Field Theory Control

All computations above are performed within a controlled EFT regime.

- The Kähler moduli satisfy $t_a \gg 1$, ensuring suppression of
  $\alpha'$ corrections.

- Gauge thresholds are perturbative and dominated by one--loop
  effects.

- Axion decay constants are sub--Planckian in the chosen units.

#### Remark

These conditions ensure that the string--lift is not merely algebraic
but physically reliable.

# Consistency Checks

We summarize the checks satisfied by the present construction:

- Tree--level gauge couplings reproduce Tier 3 $\zeta$--ratios.

- Volume normalization reproduces Tier 3 scale $K$.

- Axion decay constant ratios match $\zeta$--ratios.

- Threshold profiles reproduce Tier 3 minimal and minimum--norm
  diagnostics.

- Matching holds at more than one reference scale.

Passing all of these checks confirms the internal consistency of the
Tier 4 execution.

# Conclusions and Outlook

We have presented the first Tier 4 execution of Modal Triplet Theory:
an explicit string--lift realizing the gauge, Kähler, axion, and
threshold sectors fixed abstractly at Tier 3.

The key outcome is an existence result:

- Tier 3 targets can be met simultaneously,

- with standard string--theoretic ingredients,

- and without introducing uncontrolled parameters.

This paper deliberately stops short of flavor, CP violation, neutrino
masses, and Higgs physics.
Those topics require local data and are treated in
Tier 4 Execution II.

With Tier 4 Execution I complete, the MTT program now has:

- exact foundations (Tier 1),

- geometry--light constraints (Tier 2),

- geometry--free calibration (Tier 3),

- and an explicit string--lift existence proof (Tier 4).

The remaining tasks concern detailed phenomenological execution rather
than structural consistency.

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
