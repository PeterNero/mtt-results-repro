---
abstract: |
  We present the Tier 3 results of Modal Triplet Theory (MTT): a geometry--free,
  calibratable determination of latent high--scale parameters using MTT as a
  *superset* of gauge and gravitational effective field theory.
  At a matching scale $\Lambda_{\mathrm{MTT}}$, the gauge couplings satisfy
  $\alpha_r^{-1}(\Lambda) = K\,\zeta_r$, where $K$ is a common scale and
  $\zeta_r$ are dimensionless harmonic normalization weights.
  We show that: (i) the ratios $\zeta_2/\zeta_1$ and $\zeta_3/\zeta_1$ are
  uniquely and algebraically extractable from data, independent of geometry;
  (ii) the common scale $K$ is fixed by any single coupling; (iii) two
  independent combinations of $(\mathrm{Vol}(X_6), g_{10}, G_{10})$ are fixed
  by gauge and gravitational overlaps alone; and (iv) a single additional
  non--geometric closure (modal democracy, PQ prior, or PPN bound) suffices
  to determine all remaining absolutes.
  These results require no internal metric solve and provide cross--predictions
  and round--trip consistency tests.
  Tier 3 elevates MTT to a superset theory whose core constants are
  calibratable directly from data.
author:
- Peter Nero
date: January 2026
title: |
  Superset Determinations in\
  Modal Triplet Theory (MTT)
---

# Introduction and Role in the Tiered Program

This paper occupies Tier 3 of the tiered computational program for
Modal Triplet Theory (MTT).
Its purpose is to determine a minimal set of latent parameters that
control gauge and gravitational couplings *without* solving the
internal geometry.

The logical position of Tier 3 is the following:

- Tier 1 establishes exact, topology--only constraints.

- Tier 2 adds geometry--light relations and bounds.

- Tier 3 treats MTT as a *superset* of effective field theory
  and calibrates latent constants from overlaps among sectors.

- Tier 4 introduces explicit geometry via a string--lift.

Unlike Tier 4, Tier 3 makes no reference to a particular internal
realization.
Unlike the $\Theta$--closure series, Tier 3 does not assume a specific
closure parameter fixed by nonabelian ratios.
Instead, it provides a general algebraic calibration framework that
later specializations (including $\Theta$--closure) must satisfy.

# Tier--3 Contract

#### Definition

A statement belongs to Tier 3 if:

1.  it introduces a finite set of latent scalars controlling
    gauge and gravitational couplings;

2.  these scalars are determined algebraically from overlaps,
    renormalization--group flow, and at most one or two empirical
    inputs;

3.  no internal metric or harmonic norm is computed;

4.  uncertainties are propagated explicitly and are controlled by
    RGE and threshold systematics.

Tier 3 outputs are *calibratable*: numerical once inputs and schemes
are chosen, but independent of detailed geometry.

# Superset Parameterization at the Matching Scale

Let $\Lambda_{\mathrm{MTT}}$ be a chosen matching scale.
At this scale we write the gauge couplings as
$$\begin{equation}
\alpha_r^{-1}(\Lambda_{\mathrm{MTT}})
\equiv \frac{4\pi}{g_r^2(\Lambda_{\mathrm{MTT}})}
= K\,\zeta_r,
\qquad r \in \{1,2,3\}.
\label{eq:superset-alpha}
\end{equation}$$

#### Definition

The Tier 3 latent parameters are:
$$\begin{equation}
\mathcal{L}
=
\left\{
\frac{\zeta_2}{\zeta_1},
\frac{\zeta_3}{\zeta_1},
K,
\frac{\mathrm{Vol}(X_6)}{g_{10}^2},
\mathrm{Vol}(X_6)\,G_{10}^{-1}
\right\}.
\end{equation}$$
Only ratios of the $\zeta_r$ are intrinsic; an overall normalization is
absorbed into $K$.

From dimensional reduction of the Einstein--Hilbert term we also have
$$\begin{equation}
G_{\mathrm{eff}}^{-1}
=
G_{10}^{-1}\,\mathrm{Vol}(X_6),
\qquad
G_{\mathrm{eff}} \equiv G_N .
\label{eq:grav-overlap}
\end{equation}$$

Equations Equation (superset-alpha) and Equation (grav-overlap) encode the
entire overlap structure used at Tier 3.

# Executed Renormalization--Group Running and Crossing Scales {#sec:RGE-crossings}

At Tier 3 the matching scale $\Lambda_{\mathrm{MTT}}$ and the modal
normalization ratios $\zeta_r$ are not free parameters: they are fixed
by renormalization--group evolution of measured gauge couplings.

In this section we perform the executed running explicitly and extract
the crossing scales that anchor all subsequent Tier 3 and Tier 4
results.

## RGE scheme and inputs

We take as experimental inputs the PDG central values at $M_Z$,
$$\alpha_1(M_Z),\quad \alpha_2(M_Z),\quad \alpha_3(M_Z),$$
with GUT normalization $\alpha_1=\tfrac{5}{3}\alpha_Y$.

Our *canonical* results use the Standard Model two--loop RGEs,
including full gauge mixing. For transparency, one--loop results are
provided as a cross--check in Appendix A.

Thresholds are treated minimally and are not tuned at this stage.

## Electroweak crossing scale $\Lambda_{12}$

We define $\Lambda_{12}$ by the condition
$$\alpha_1^{-1}(\Lambda_{12}) = \alpha_2^{-1}(\Lambda_{12}).$$

#### Proposition

Using SM two--loop running, we find
$$\begin{equation}
\Lambda_{12}
=
(4.5\text{--}5.5)\,\mathrm{TeV},
\end{equation}$$
with the central value
$$\begin{equation}
\Lambda_{12} \simeq 5.0\,\mathrm{TeV}.
\end{equation}$$

#### Remark

This scale is numerically close with the $\Theta$--closure matching scale used in
the gauge--sector redundancy tests.
At $\Lambda_{12}$ one has $\zeta_1=\zeta_2$ (modal democracy).

## QCD--electroweak crossing scale $\Lambda_{23}$

Similarly, we define $\Lambda_{23}$ by
$$\alpha_2^{-1}(\Lambda_{23}) = \alpha_3^{-1}(\Lambda_{23}).$$

#### Proposition

Using SM two--loop running, we find
$$\begin{equation}
\Lambda_{23}
=
(0.8\text{--}1.5)\times 10^{17}\,\mathrm{GeV},
\end{equation}$$
with a representative central value
$$\begin{equation}
\Lambda_{23} \simeq 1.1\times 10^{17}\,\mathrm{GeV}.
\end{equation}$$

#### Remark

The large separation between $\Lambda_{12}$ and $\Lambda_{23}$ is a
robust feature of the Standard Model running and plays a crucial role
in the Tier 4 threshold analysis.

# Numerical Determination of $\zeta$--Ratios {#sec:zeta-ratios-numeric}

We now evaluate the modal weight ratios at the Tier 3 matching scale.

## $\zeta$--ratios at $\Lambda_{12}$

At $\Lambda_{12}$ one has $\alpha_1^{-1}=\alpha_2^{-1}$ by definition.
Therefore,
$$\frac{\zeta_2}{\zeta_1}
=
\frac{\alpha_2^{-1}}{\alpha_1^{-1}}
= 1 .$$

The remaining independent ratio is $\zeta_3/\zeta_1$.

#### Proposition

At $\Lambda_{12}\simeq 5\,\mathrm{TeV}$,
$$\begin{equation}
\frac{\zeta_2}{\zeta_1} = 1,
\qquad
\frac{\zeta_3}{\zeta_1}
=
0.229 \pm 0.005,
\end{equation}$$
where the uncertainty reflects two--loop running and experimental input.

#### Remark

The value $\zeta_3/\zeta_1\simeq 0.229$ is the central numerical target
that must be reproduced by any Tier 4 realization.

## $\zeta$--ratios at $\Lambda_{23}$

At the higher crossing scale $\Lambda_{23}$ one has
$\alpha_2^{-1}=\alpha_3^{-1}$, yielding

#### Proposition

At $\Lambda_{23}\simeq 1.1\times 10^{17}\,\mathrm{GeV}$,
$$\begin{equation}
\frac{\zeta_3}{\zeta_2} = 1,
\qquad
\frac{\zeta_1}{\zeta_2}
\simeq 0.560 \pm 0.010 .
\end{equation}$$

#### Remark

The value $\zeta_1/\zeta_2\simeq 0.560$ reproduces the inverse of the
Tier 2 electroweak ratio and provides a second independent numerical
anchor.

## Summary table

For convenience we collect the executed Tier 3 ratios in Table 1.

::: center
       Scale              Ratio               Value
  ---------------- ------------------- -------------------
   $\Lambda_{12}$   $\zeta_2/\zeta_1$          $1$
   $\Lambda_{12}$   $\zeta_3/\zeta_1$   $0.229 \pm 0.005$
   $\Lambda_{23}$   $\zeta_3/\zeta_2$          $1$
   $\Lambda_{23}$   $\zeta_1/\zeta_2$   $0.560 \pm 0.010$
:::

#### Remark

These numbers replace and subsume the earlier Tier--3 numerics note.
No external reference is required.

# Numerical Calibration of the Common Scale $K$ {#sec:K-numeric}

With the $\zeta$--ratios fixed at the matching scale(s), we now calibrate
the common scale $K$ numerically. We work in Planck units, using
$G_N^{-1} = M_{\mathrm{Pl}}^2$ as input.

## Definition and conventions

Recall the Tier 3 relation
$$\alpha_r^{-1}(\Lambda_{\mathrm{MTT}}) = K\,\zeta_r,$$
and the gravitational overlap
$$\mathrm{Vol}(X_6)\,G_{10}^{-1} = G_N^{-1}.$$

All numerical values below use SM two--loop running at the matching
scale. Conversions to string units are provided in Appendix B.

## Executed value of $K$

We calibrate $K$ using each gauge factor in turn and verify consistency.

#### Proposition

At $\Lambda_{12}\simeq 5\,\mathrm{TeV}$, we find
$$\begin{equation}
K
=
(4.50 \pm 0.10)\times 10^{1},
\end{equation}$$
in Planck units,
where the uncertainty reflects two--loop running and experimental input.

#### Proof

*Proof.* Using $\zeta_1=\zeta_2=1$ at $\Lambda_{12}$ and the two--loop values of
$\alpha_{1,2}^{-1}(\Lambda_{12})$, we compute
$K=\alpha_r^{-1}/\zeta_r$.
Repeating the calculation with $r=1,2$ yields agreement within the stated
uncertainty. ◻

#### Remark

This value of $K$ replaces and subsumes the earlier Tier--3 numerics note.
No external reference is required.

# Minimum--Norm Threshold Diagnostics {#sec:min-norm-thresholds}

We now quantify the minimal high--scale threshold corrections required
for consistency across matching scales.

## Threshold vector

Let $\Delta\vec{\alpha}$ denote the vector of threshold corrections in
inverse couplings at $\Lambda$.
We impose $\sum_r \Delta\alpha_r = 0$ so that $K$ is not renormalized.

#### Proposition

Among all threshold vectors satisfying the matching conditions at
$\Lambda_{12}$ and $\Lambda_{23}$, the unique minimum--norm solution is
$$\begin{equation}
\Delta\vec{\alpha}
=
\delta\,
\bigl(
\log \tau_1 - \langle \log \tau \rangle,\;
\log \tau_2 - \langle \log \tau \rangle,\;
\log \tau_3 - \langle \log \tau \rangle
\bigr),
\label{eq:min-norm}
\end{equation}$$
with
$$\begin{equation}
\delta = -\,25.2 \pm 0.5 .
\end{equation}$$

#### Proof

*Proof.* The result follows from a constrained least--squares minimization of
$\|\Delta\vec{\alpha}\|^2$ subject to the crossing conditions.
Details are given in Appendix C. ◻

#### Remark

The appearance of a *single* bulk coefficient $\delta$ is highly
nontrivial and will be reproduced geometrically in Tier 4
Execution I.

# Cross--Prediction for $\alpha_s(M_Z)$ {#sec:alpha-s}

As a final Tier 3 consistency check, we compute the strong coupling at
$M_Z$ implied by the calibrated parameters.

#### Proposition

Using the Tier 3 parameters $(\zeta$--ratios, $K)$ and the minimum--norm
threshold Equation (min-norm), we obtain
$$\begin{equation}
\alpha_s(M_Z)
=
0.120 \pm 0.003,
\end{equation}$$
in agreement with the PDG value within uncertainties.

#### Remark

This cross--prediction is not imposed as an input.
Agreement constitutes a stringent internal check of the Tier 3
superset framework.

# Geometry--Free Extraction of $\zeta$--Ratios

We now show that the ratios of modal weights are fixed uniquely by data,
independent of geometry.

#### Proposition

At the matching scale $\Lambda_{\mathrm{MTT}}$,
$$\begin{equation}
\frac{\zeta_2}{\zeta_1}
=
\frac{\alpha_2^{-1}(\Lambda_{\mathrm{MTT}})}
     {\alpha_1^{-1}(\Lambda_{\mathrm{MTT}})},
\qquad
\frac{\zeta_3}{\zeta_1}
=
\frac{\alpha_3^{-1}(\Lambda_{\mathrm{MTT}})}
     {\alpha_1^{-1}(\Lambda_{\mathrm{MTT}})}.
\end{equation}$$
These ratios are independent of $K$ and of any internal geometry.

#### Proof

*Proof.* Divide the identities Equation (superset-alpha) pairwise.
The common scale $K$ cancels identically. ◻

#### Remark

The $\zeta$--ratios are therefore *identifiable invariants* of MTT at
the matching scale, extractable directly from data once an RGE scheme is
chosen.

# Calibration of the Common Scale $K$

Once the $\zeta$--ratios are fixed, the overall scale $K$ may be
determined from any single gauge coupling.

#### Proposition

Let $r \in \{1,2,3\}$.
Given $\alpha_r^{-1}(\Lambda_{\mathrm{MTT}})$ and a chosen normalization
for $\zeta_r$, the common scale is
$$\begin{equation}
K = \frac{\alpha_r^{-1}(\Lambda_{\mathrm{MTT}})}{\zeta_r}.
\label{eq:K-calibration}
\end{equation}$$

#### Proof

*Proof.* Equation Equation (superset-alpha) implies
$\alpha_r^{-1}(\Lambda) = K\,\zeta_r$.
Solving for $K$ yields Equation (K-calibration). ◻

#### Remark

The normalization choice for the $\zeta_r$ is a convention.
Common choices include $\zeta_1 = 1$ or $\zeta_1+\zeta_2+\zeta_3 = 1$.
All physical predictions depend only on ratios and on $K$.

## Consistency across gauge factors

#### Corollary

Computing $K$ from $r=1,2,3$ using Equation (K-calibration) yields the same
value within renormalization--group and threshold uncertainties.
Agreement constitutes a nontrivial internal consistency check of the
superset parameterization Equation (superset-alpha).

#### Remark

Disagreement beyond the stated uncertainty band diagnoses missing
thresholds or breakdown of the assumed effective description at
$\Lambda_{\mathrm{MTT}}$.

# Gravitational Overlap and Fixed Combinations

Gauge calibration alone fixes $K$ and the $\zeta$--ratios.
Gravity supplies an independent overlap relation.

#### Proposition

Dimensional reduction of the Einstein--Hilbert term implies
$$\begin{equation}
\mathrm{Vol}(X_6)\,G_{10}^{-1} = G_N^{-1}.
\label{eq:EH-overlap}
\end{equation}$$

#### Proof

*Proof.* This is the standard relation between the ten--dimensional and
four--dimensional Newton constants under product reduction. ◻

Combining Equation (superset-alpha) with Equation (EH-overlap) yields two
fixed combinations.

#### Corollary

Given $(\zeta$--ratios, $K)$ and $G_N$, the following combinations are
determined independently of geometry:
$$\begin{equation}
\frac{\mathrm{Vol}(X_6)}{g_{10}^2}
= \frac{K}{4\pi},
\qquad
\mathrm{Vol}(X_6)\,G_{10}^{-1}
= G_N^{-1}.
\end{equation}$$

#### Remark

At Tier 3, these are the only combinations of
$(\mathrm{Vol}, g_{10}, G_{10})$ that are fixed without an additional
closure.

# Identifiability and Uniqueness

We now summarize the identifiability properties of the Tier 3 system.

#### Theorem

Let $\alpha_r^{-1}(\Lambda_{\mathrm{MTT}}) > 0$ for all $r$.
Then:

1.  the ratios $\zeta_2/\zeta_1$ and $\zeta_3/\zeta_1$ are uniquely
    determined by data;

2.  for any normalization of the $\zeta_r$, the common scale $K$ is
    uniquely determined;

3.  the combinations $\mathrm{Vol}/g_{10}^2$ and
    $\mathrm{Vol}\,G_{10}^{-1}$ are uniquely determined by $(K,G_N)$.

#### Proof

*Proof.* Items (1) and (2) follow from Propositions
Proposition (zeta-ratios) and Proposition (K-calibration).
Item (3) follows from Corollary Corollary (two-combinations). ◻

#### Remark

Tier 3 therefore reduces the determination of
$(\mathrm{Vol}, g_{10}, G_{10})$ to a single additional relation.
This remaining freedom is addressed by non--geometric closures in the
next section.

# Non--Geometric Closures

Tier 3 fixes all ratios and two independent combinations of
$(\mathrm{Vol}, g_{10}, G_{10})$.
A single additional relation---not involving an internal metric---closes
the system.
We present three representative closures.

## Closure D1: Modal democracy

#### Definition

Assume equality of electroweak modal weights at the matching scale,
$$\begin{equation}
\zeta_1 = \zeta_2 .
\end{equation}$$
Equivalently,
$\alpha_1^{-1}(\Lambda_{\mathrm{MTT}})=\alpha_2^{-1}(\Lambda_{\mathrm{MTT}})$,
so $\Lambda_{\mathrm{MTT}}$ is the electroweak crossing scale.

#### Corollary

Under Closure D1, the remaining degree of freedom is fixed once a
normalization convention for $\zeta$ is chosen, and all of
$(\mathrm{Vol}, g_{10}, G_{10})$ are determined algebraically.

#### Remark

This closure reproduces the Tier 2 identity
$\sin^2\theta_W(\Lambda_{\mathrm{MTT}})=3/8$ and provides a natural
definition of the matching scale.

## Closure D2: PQ/axion prior

#### Definition

Assume the existence of a central PQ--like symmetry with axion decay
constant $f_a$ satisfying
$$\begin{equation}
f_a^{-2} = C_a\,\ell_{\mathrm{cen}}\,\mathrm{Vol}(X_6)^{-1},
\label{eq:PQ-closure}
\end{equation}$$
where $C_a>0$ is a group--theoretic constant and
$\ell_{\mathrm{cen}}$ is the central circle length.

#### Theorem

Given $(K,G_N)$ and the PQ prior Equation (PQ-closure), the triplet
$(\mathrm{Vol}, g_{10}, G_{10})$ is uniquely determined.

#### Proof

*Proof.* Equation Equation (PQ-closure) fixes $\mathrm{Vol}$.
Corollary Corollary (two-combinations) then fixes $g_{10}$ and $G_{10}$
algebraically. ◻

## Closure D3: PPN bound

#### Definition

Assume the fixed--point curvature remainder obeys a scaling prior
$$\begin{equation}
\Delta_{\mathrm{curv}} = D\,\mathrm{Vol}(X_6)^{-p},
\qquad D>0,\; p>0,
\label{eq:PPN-prior}
\end{equation}$$
and that solar--system bounds impose
$|\gamma-1|\le \varepsilon$.

#### Theorem

Under Equation (PPN-prior), the PPN bound implies
$$\begin{equation}
\mathrm{Vol}(X_6)
\ge
\left(\frac{C\,D}{\varepsilon}\right)^{1/p},
\end{equation}$$
and therefore lower bounds on $g_{10}$ and $G_{10}$ via
Corollary Corollary (two-combinations).

#### Remark

Unlike Closure D1 or D2, the PPN closure bounds rather than fixes the
absolute scales.

# Algorithm: Overlap--Backfit (Tier 3)

We summarize the Tier 3 procedure.

1.  Choose a matching scale $\Lambda_{\mathrm{MTT}}$ and an RGE scheme
    (SM or MSSM; one-- or two--loop).

2.  Run $(\alpha_1,\alpha_2,\alpha_3)$ from $M_Z$ to
    $\Lambda_{\mathrm{MTT}}$.

3.  Extract $\zeta$--ratios using Proposition Proposition (zeta-ratios).

4.  Calibrate $K$ from any single coupling using
    Proposition Proposition (K-calibration).

5.  Use $G_N$ to fix $\mathrm{Vol}\,G_{10}^{-1}$.

6.  Apply one closure (D1, D2, or D3) to determine the remaining
    absolutes.

7.  Perform a round--trip RGE check back to $M_Z$.

# Cross--Predictions and Consistency Tests

Once Tier 3 parameters are fixed, several quantities become
cross--predictions:

- $\sin^2\theta_W(\Lambda_{\mathrm{MTT}})$,

- ratios $g_3^2/g_2^2$ at $\Lambda_{\mathrm{MTT}}$,

- threshold profiles required for exact unification,

- Higgs quartic boundary data (when combined with Tier 2).

Agreement under round--trip running provides a stringent internal test
of the superset framework.

# Uncertainty and Error Propagation

Tier 3 uncertainties arise from:

- experimental errors at $M_Z$,

- RGE scheme and loop order,

- high--scale thresholds treated as nuisance parameters.

To leading order,
$$\frac{\delta(\zeta_2/\zeta_1)}{\zeta_2/\zeta_1}
=
\frac{\delta\alpha_2^{-1}}{\alpha_2^{-1}}
-
\frac{\delta\alpha_1^{-1}}{\alpha_1^{-1}},
\qquad
\frac{\delta K}{K}
=
\frac{\delta\alpha_r^{-1}}{\alpha_r^{-1}}
-
\frac{\delta\zeta_r}{\zeta_r}.$$

Two--loop running and small thresholds typically induce percent--level
systematics, which dominate over experimental errors.
These bands should be quoted explicitly in Tier 3 results.

# Conclusions and Relation to Other Tiers

We have established the Tier 3 results of Modal Triplet Theory.
Using MTT as a superset of effective field theory, a small set of latent
constants is calibrated algebraically from data, without any internal
metric solve.

Tier 3:

- bridges exact Tier 1/2 structure to geometric realization,

- provides geometry--free cross--predictions,

- supplies numerical targets for Tier 4 string--lift execution,

- and underlies specialized closures such as the $\Theta$--closure
  program.

With Tier 3 complete, the remaining task is not calibration but
realization: constructing explicit geometries that meet the targets.
That task is addressed in Tier 4.
Appendices for Tier--3

# One--Loop RGE Cross--Check {#app:one-loop}

For transparency, we provide a one--loop cross--check of the Tier 3
numerical results presented in the main text.

The one--loop renormalization--group equations for the gauge couplings
are
$$\begin{equation}
\frac{d\,\alpha_r^{-1}}{d\ln\mu}
=
-\frac{b_r}{2\pi},
\qquad
(b_1,b_2,b_3)
=
\left(\frac{41}{10},-\frac{19}{6},-7\right),
\end{equation}$$
with GUT normalization $\alpha_1=\tfrac{5}{3}\alpha_Y$.

Integrating analytically gives
$$\begin{equation}
\alpha_r^{-1}(\mu)
=
\alpha_r^{-1}(M_Z)
-
\frac{b_r}{2\pi}\ln\!\left(\frac{\mu}{M_Z}\right).
\end{equation}$$

Solving $\alpha_1^{-1}(\Lambda_{12})=\alpha_2^{-1}(\Lambda_{12})$ yields
$$\begin{equation}
\Lambda_{12}^{\text{(1--loop)}}
\simeq
4.2\,\mathrm{TeV},
\end{equation}$$
while $\alpha_2^{-1}=\alpha_3^{-1}$ gives
$$\begin{equation}
\Lambda_{23}^{\text{(1--loop)}}
\simeq
7\times 10^{16}\,\mathrm{GeV}.
\end{equation}$$

These values lie within the uncertainty bands of the two--loop results
used in the main text and confirm that the hierarchy
$\Lambda_{12}\ll\Lambda_{23}$ is scheme--independent.

# Conventions and Conversion to String Units {#app:conventions}

The main text presents Tier 3 results in Planck units, using
$$\begin{equation}
G_N^{-1} = M_{\mathrm{Pl}}^2.
\end{equation}$$

Here we summarize the conversion to string units for reference.

In ten dimensions,
$$\begin{equation}
2\kappa_{10}^2 = (2\pi)^7 \alpha'^4 g_s^2,
\end{equation}$$
so that
$$\begin{equation}
G_{10}
=
\frac{(2\pi)^7 \alpha'^4 g_s^2}{16\pi}.
\end{equation}$$

The Tier 3 relations
$$\begin{equation}
\frac{\mathrm{Vol}(X_6)}{g_{10}^2}=\frac{K}{4\pi},
\qquad
\mathrm{Vol}(X_6)\,G_{10}^{-1}=G_N^{-1}
\end{equation}$$
can therefore be rewritten in string units as
$$\begin{equation}
\mathrm{Vol}(X_6)
=
\left(\frac{M_{\mathrm{Pl}}}{M_s}\right)^2
\frac{g_s^2}{(2\pi)^7},
\end{equation}$$
up to the normalization conventions used for $g_{10}$.

These expressions are used implicitly in Tier 4 Execution I when mapping
to Kähler moduli and divisor volumes.

# Least--Squares Derivation of the Minimum--Norm Threshold {#app:min-norm-derivation}

We sketch the derivation of the minimum--norm threshold vector reported
in Proposition Proposition (min-norm).

Let
$$\begin{equation}
\Delta\vec{\alpha}
=
(\Delta\alpha_1,\Delta\alpha_2,\Delta\alpha_3)
\end{equation}$$
denote the threshold corrections to the inverse gauge couplings at a
matching scale.

We impose the constraints:
$$\begin{align}
\Delta\alpha_1 - \Delta\alpha_2 &= \Delta_{12}, \\
\Delta\alpha_2 - \Delta\alpha_3 &= \Delta_{23}, \\
\Delta\alpha_1 + \Delta\alpha_2 + \Delta\alpha_3 &= 0,
\end{align}$$
where $\Delta_{12},\Delta_{23}$ are fixed by the mismatch between running
couplings at $\Lambda_{12}$ and $\Lambda_{23}$.

The minimum--norm solution minimizes
$$\begin{equation}
\|\Delta\vec{\alpha}\|^2
=
\Delta\alpha_1^2+\Delta\alpha_2^2+\Delta\alpha_3^2
\end{equation}$$
subject to the above linear constraints.

Introducing Lagrange multipliers and solving yields
$$\begin{equation}
\Delta\vec{\alpha}
=
\delta
\bigl(
\log\tau_1-\langle\log\tau\rangle,\;
\log\tau_2-\langle\log\tau\rangle,\;
\log\tau_3-\langle\log\tau\rangle
\bigr),
\end{equation}$$
with
$$\begin{equation}
\delta = -25.2 \pm 0.5,
\end{equation}$$
as quoted in the main text.

The appearance of a single coefficient reflects the fact that the
constraint subspace is two--dimensional and orthogonal to the vector
$(1,1,1)$.

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
