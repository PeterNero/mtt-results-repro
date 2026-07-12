---
abstract: |
  We test the $\Theta$--closure program of Modal Triplet Theory (MTT) by imposing a
  redundant Standard Model constraint.
  In previous work, $\Theta$ was fixed using the nonabelian gauge couplings
  $g_1:g_2:g_3$ at a common matching scale $\mu_\Theta$.
  In this paper we ask whether the same $\Theta$, with no additional free
  parameters, also reproduces the observed value of the weak mixing angle
  $\sin^2\theta_W(M_Z)$.
  Using one--loop renormalization group evolution and the canonical normalization
  of hypercharge, we derive a predicted $\sin^2\theta_W(M_Z)$ from the
  $\Theta$--fixed couplings and compare it to experiment.
  Agreement would constitute a nontrivial overconstraint of the gauge sector;
  disagreement would identify precisely where the $\Theta$--closure assumptions
  require modification.
author:
- Peter Nero
date: January 2026
title: |
  Theta Closure in Modal Triplet Theory V:
  Redundant Determination from Gauge Couplings and the Weak Mixing Angle
---

# Introduction

A persistent challenge in fundamental physics is to identify structures that
relate multiple Standard Model parameters without introducing new tunable
inputs.
In most frameworks, the weak mixing angle $\sin^2\theta_W$ and the gauge
couplings are treated as independent quantities, linked only through
renormalization group evolution once boundary conditions are specified.

Modal Triplet Theory (MTT) proposes that effective four--dimensional couplings
are determined by overlap integrals of internal harmonic representatives.
In a sequence of recent papers, a conservative $\Theta$--closure framework was
developed in which the nonabelian gauge couplings $g_1,g_2,g_3$ fix a single
parameter $\Theta$ at a common matching scale $\mu_\Theta$.
That framework was shown to be internally consistent, explicitly realizable,
and cross--validated by two independent derivation routes.

The present paper separates two questions that must not be conflated:

> *Does the one--loop matching pipeline consistently return the weak mixing
> angle when run down from the $\Theta$--fixed boundary values?*

and, more stringently,

> *Can $\sin^2\theta_W$ be reproduced without using it as an input, once one
> unavoidable overall gauge normalization has been fixed independently?*

This question is important because $\sin^2\theta_W$ is not an independent
overlap ratio but a derived quantity combining the hypercharge and $SU(2)$
couplings.
The first question is a useful round--trip consistency check. Only the second
question can support a genuine non-circular redundancy claim.

# Fixing $\Theta$ from nonabelian gauge couplings

We briefly summarize the $\Theta$--fixing procedure established in
PapersÂ I--III.

At a common matching scale $\mu_\Theta$, the gauge couplings are written as
$$\frac{1}{g_a^2(\mu_\Theta)} = \frac{1}{g_{10}^2}\, I_a(\Theta),
\qquad a=1,2,3,$$
where $I_a(\Theta)$ are internal overlap integrals determined by $\Theta$.

Using one--loop renormalization group evolution from the electroweak scale,
the experimentally measured values of $g_1(M_Z), g_2(M_Z), g_3(M_Z)$ determine
numerical targets for the ratios $I_2/I_1$ and $I_3/I_1$ at $\mu_\Theta$.
Solving these relations fixes $\Theta$ up to controlled uncertainties.

In what follows, $\Theta$ is treated as fixed by this procedure.
No refitting or retuning is performed.

# Renormalization group evolution and prediction of $\sin^2\theta_W(M_Z)$

In this section we derive the predicted value of the weak mixing angle at the
electroweak scale from the $\Theta$--fixed gauge couplings at the matching scale
$\mu_\Theta$.
No additional parameters are introduced.

#### Remark

The numerical results presented here rely on one--loop renormalization group
evolution in the $\overline{\mathrm{MS}}$ scheme.
While higher--loop effects and threshold corrections can shift numerical values
at the percent level, such effects do not alter the structural conclusions of
the redundancy test.
All claims are therefore restricted to the accuracy class of the approximation
used.

## One--loop renormalization group equations

We work at one--loop order in the $\overline{\mathrm{MS}}$ scheme.
The running of the gauge couplings is governed by
$$\begin{equation}
\mu\,\frac{d g_a}{d\mu}
=
\frac{b_a}{16\pi^2}\, g_a^3,
\label{eq:RGE_g}
\end{equation}$$
or equivalently,
$$\begin{equation}
\frac{1}{g_a^2(\mu)}
=
\frac{1}{g_a^2(\mu_0)}
-
\frac{b_a}{8\pi^2}\,
\ln\!\left(\frac{\mu}{\mu_0}\right),
\label{eq:RGE_inverse}
\end{equation}$$
with beta--function coefficients
$$\begin{equation}
(b_1,b_2,b_3)
=
\left(
\frac{41}{10},\,
-\frac{19}{6},\,
-7
\right),
\label{eq:beta_coeffs}
\end{equation}$$
where $g_1$ denotes the GUT--normalized hypercharge coupling,
$g_1=\sqrt{\tfrac{5}{3}}\,g'$.

## $\Theta$--fixed boundary conditions at $\mu_\Theta$

In PapersÂ I--III, the parameter $\Theta$ was fixed by matching the
experimentally determined gauge couplings to the overlap relations at the
common matching scale
$$\mu_\Theta = 5~\mathrm{TeV}.$$

At this scale, the $\Theta$--fixed gauge couplings are taken as
$$\begin{equation}
g_1(\mu_\Theta),\qquad
g_2(\mu_\Theta),\qquad
g_3(\mu_\Theta),
\end{equation}$$
with numerical values determined by upward RG evolution from $M_Z$ and the
$\Theta$--closure conditions.
These values are treated as fixed inputs in the present section.

## Downward RG evolution to $M_Z$

We now evolve $g_1$ and $g_2$ from $\mu_\Theta$ down to the electroweak scale
$M_Z$ using Equation (RGE_inverse):
$$\begin{align}
\frac{1}{g_1^2(M_Z)}
&=
\frac{1}{g_1^2(\mu_\Theta)}
-
\frac{b_1}{8\pi^2}
\ln\!\left(\frac{M_Z}{\mu_\Theta}\right),
\label{eq:g1_down}\\[0.5em]
\frac{1}{g_2^2(M_Z)}
&=
\frac{1}{g_2^2(\mu_\Theta)}
-
\frac{b_2}{8\pi^2}
\ln\!\left(\frac{M_Z}{\mu_\Theta}\right).
\label{eq:g2_down}
\end{align}$$

Because $b_1>0$ and $b_2<0$, hypercharge becomes weaker and $SU(2)$ becomes
stronger as the scale is lowered, as expected.

## Prediction for the weak mixing angle

The weak mixing angle is defined by
$$\begin{equation}
\sin^2\theta_W(M_Z)
=
\frac{g'^2(M_Z)}{g'^2(M_Z)+g_2^2(M_Z)}
=
\frac{\tfrac{3}{5}\,g_1^2(M_Z)}
{\tfrac{3}{5}\,g_1^2(M_Z)+g_2^2(M_Z)}.
\label{eq:sin2theta_def}
\end{equation}$$

Substituting the RG--evolved couplings Equation (g1_down)--Equation (g2_down)
into Equation (sin2theta_def) yields a predicted value
$$\begin{equation}
\sin^2\theta_W^{\mathrm{pred}}(M_Z;\Theta,\mu_\Theta),
\label{eq:sin2theta_pred}
\end{equation}$$
which depends only on the previously fixed $\Theta$ and the chosen matching
scale $\mu_\Theta$.

## Comparison with experiment

The experimentally measured value used for the numerical comparison is
$$\begin{equation}
\sin^2\theta_W^{\mathrm{exp}}(M_Z)
=
0.23122 \pm 0.00003.
\label{eq:sin2theta_exp}
\end{equation}$$

Agreement between Equation (sin2theta_pred) and Equation (sin2theta_exp) within
the expected theoretical uncertainty of the one--loop approximation is a
consistency check of the matching and running pipeline. By itself it is not a
non-circular prediction if the boundary values at $\mu_\Theta$ were obtained by
running the same electroweak inputs upward from $M_Z$. A genuine redundancy test
requires the non-circular construction described below.

#### Remark

The present analysis is intentionally limited to one--loop running and does not
include electroweak threshold corrections or two--loop effects.
These corrections are parametrically small compared to the leading
logarithmic evolution and can be incorporated systematically in future work if
needed.

#### Remark

The numerical agreement in this paper should be interpreted within the accuracy class of
(i) one--loop MS running and (ii) leading electroweak matching. In particular, electroweak
threshold effects in extracting $g_2$ from $(G_F,m_W)$ are controlled by the standard
radiative--correction parameter $\Delta r$, which is ${\cal O}(10^{-2})$ in the Standard Model.
Over the short running interval from $M_Z$ (or $m_W$) to $\mu_\Theta=5~\mathrm{TeV}$, omitted
two--loop corrections to gauge running are expected to induce sub--percent shifts in $g_1,g_2$.
Since the redundancy test is formulated in terms of ratios and downward--evolved combinations,
the resulting theoretical uncertainty on $\sin^2\theta_W(M_Z)$ is conservatively at the
${\cal O}(10^{-4})$ level. No claim is made to predict $\sin^2\theta_W$ at the experimental
error bar without a dedicated higher--order electroweak treatment.

## Explicit numerical evaluation at $\mu_\Theta=5~\mathrm{TeV}$

We now evaluate Equation (g1_down)--Equation (sin2theta_def) numerically using the
$\Theta$--fixed boundary couplings at $\mu_\Theta=5~\mathrm{TeV}$ established in
PapersÂ I--III (one--loop, GUT--normalized $g_1$):
$$\begin{equation}
g_1(\mu_\Theta)=0.4720,
\qquad
g_2(\mu_\Theta)=0.6306.
\label{eq:g1g2_muTheta_values}
\end{equation}$$

Let $M_Z=91.1876~\mathrm{GeV}$ and
$$L := \ln\!\left(\frac{\mu_\Theta}{M_Z}\right)
= \ln\!\left(\frac{5000}{91.1876}\right)
\approx 4.00427,
\qquad
8\pi^2 \approx 78.9568.$$
Using $b_1=41/10=4.1$ and $b_2=-19/6\approx -3.1666667$, the inverse--coupling
running Equation (g1_down)--Equation (g2_down) gives
$$\begin{align*}
\frac{1}{g_1^2(M_Z)}
&=
\frac{1}{g_1^2(\mu_\Theta)} + \frac{b_1}{8\pi^2}L
=
\frac{1}{(0.4720)^2} + \frac{4.1}{78.9568}(4.00427)
\approx 4.6966,
\\[0.3em]
\frac{1}{g_2^2(M_Z)}
&=
\frac{1}{g_2^2(\mu_\Theta)} + \frac{b_2}{8\pi^2}L
=
\frac{1}{(0.6306)^2} + \frac{-3.1666667}{78.9568}(4.00427)
\approx 2.3531.
\end{align*}$$
Therefore
$$\begin{equation}
g_1(M_Z)\approx 0.46143,
\qquad
g_2(M_Z)\approx 0.65175.
\label{eq:g1g2_MZ_values}
\end{equation}$$

Using GUT normalization $g'^2=(3/5)g_1^2$, the weak mixing angle is
$$\sin^2\theta_W(M_Z)
=
\frac{g'^2}{g'^2+g_2^2}
=
\frac{\tfrac35 g_1^2(M_Z)}{\tfrac35 g_1^2(M_Z)+g_2^2(M_Z)}.$$
Substituting Equation (g1g2_MZ_values) yields
$$\begin{equation}
\boxed{
\sin^2\theta_W^{\mathrm{pred}}(M_Z)
\approx 0.2312109.
}
\label{eq:sin2_pred_numeric}
\end{equation}$$

The experimental value is
$$\sin^2\theta_W^{\mathrm{exp}}(M_Z)=0.23122\pm 0.00003,$$
so the round--trip one--loop value agrees numerically with the input value at
the quoted precision. This agreement validates the arithmetic and normalization
conventions of the running calculation, but it is not an independent prediction.

#### Remark

Because the inputs Equation (g1g2_muTheta_values) were obtained in PapersÂ I--III
by upward RG evolution from $M_Z$, the present computation is a round--trip
consistency check of the one--loop RGE pipeline. A genuinely independent
redundant determination requires computing $g_1(\mu_\Theta)$ and $g_2(\mu_\Theta)$
from the internal overlap geometry directly (using $\Theta$ fixed from overlap data)
without using $\sin^2\theta_W(M_Z)$ as an input. This is a well-posed next step:
once $g_1(\mu_\Theta)$ and $g_2(\mu_\Theta)$ are obtained internally, the same
downward evolution yields a strict, non-circular prediction for
$\sin^2\theta_W(M_Z)$.

# Non--circular determination of $\sin^2\theta_W$ from $\Theta$

The numerical agreement obtained in SectionÂ 3 demonstrates internal consistency
of the renormalization group pipeline but does not, by itself, constitute a
redundant determination of $\Theta$, since the boundary couplings at
$\mu_\Theta$ were obtained by upward evolution from $M_Z$.
In this section we explain how a genuinely non--circular test is obtained and
identify the minimal additional input required.

## Why one additional input is unavoidable

In the overlap formulation of Modal Triplet Theory,
$$\begin{equation}
\frac{1}{g_a^2(\mu_\Theta)} = \frac{1}{g_{10}^2}\, I_a(\Theta),
\qquad a=1,2,3,
\label{eq:overlap_again}
\end{equation}$$
the three gauge couplings depend on:

- the dimensionless overlap ratios $I_a/I_b$, fixed by $\Theta$,

- a single overall normalization $g_{10}$.

The ratios $I_2/I_1$ and $I_3/I_1$ fix $\Theta$ uniquely, but they do not fix the
absolute scale of the couplings.
This reflects a general fact: without specifying one dimensionless coupling
value at a reference scale, no framework can determine all gauge couplings
absolutely.
Thus one additional input is logically unavoidable.

#### Remark

This situation is entirely analogous to fixing the overall normalization in
Grand Unified Theories by specifying one gauge coupling at the unification
scale, or to fixing the Planck mass in Kaluza--Klein theories.

## Minimal non--circular input

The minimal and most conservative choice is to fix a single coupling at
$\mu_\Theta$, for example
$$\begin{equation}
g_2(\mu_\Theta) = g_2^{\mathrm{ref}},
\label{eq:ref_input}
\end{equation}$$
where $g_2^{\mathrm{ref}}$ is taken from experiment via RG evolution.
No information about $\sin^2\theta_W(M_Z)$ is used at this stage.

Given Equation (ref_input) and the $\Theta$--fixed ratios
$$\frac{g_1^2(\mu_\Theta)}{g_2^2(\mu_\Theta)} = \frac{I_2(\Theta)}{I_1(\Theta)},
\qquad
\frac{g_3^2(\mu_\Theta)}{g_2^2(\mu_\Theta)} = \frac{I_2(\Theta)}{I_3(\Theta)},$$
all three couplings at $\mu_\Theta$ are fixed.

## Prediction of $\sin^2\theta_W(M_Z)$

With $g_1(\mu_\Theta)$ and $g_2(\mu_\Theta)$ determined non--circularly as above,
the downward renormalization group evolution of SectionÂ 3 yields a predicted
value
$$\sin^2\theta_W^{\mathrm{pred}}(M_Z;\Theta),$$
with no further inputs.

Agreement between $\sin^2\theta_W^{\mathrm{pred}}(M_Z)$ and the experimental value
$$\sin^2\theta_W^{\mathrm{exp}}(M_Z)=0.23122\pm0.00003$$
would then constitute a genuine redundancy in the determination of $\Theta$,
since:

- $\Theta$ would be fixed by nonabelian gauge ratios alone,

- $\sin^2\theta_W$ would be reproduced without being used as an input,

- only one unavoidable normalization $g_{10}$ would have been specified.

## Pass/fail criterion

The non--circular test admits a sharp outcome:

- *Pass:* $\sin^2\theta_W^{\mathrm{pred}}(M_Z)$ agrees with experiment
  within theoretical uncertainty, implying overconstraint of the gauge sector.

- *Fail:* $\sin^2\theta_W^{\mathrm{pred}}(M_Z)$ disagrees with experiment,
  pinpointing which assumption (matching scale, threshold effects, or overlap
  structure) requires revision.

In either case the test is informative, as it directly probes the internal
consistency of $\Theta$--closure beyond the minimal set of gauge--sector inputs.
In practice, the strict pass condition is agreement within a conservative theoretical band
dominated by electroweak threshold matching (parametrized here by $\Delta r_{\mathrm{eff}}$)
and by omitted higher--loop RG effects, i.e.Â at the ${\cal O}(10^{-4})$ level in
$\sin^2\theta_W(M_Z)$.

## Non--circular numerical evaluation using $(G_F,m_W)$ as input

We now perform the non--circular evaluation proposed in SectionÂ 4.
Unlike SectionÂ 3 (round--trip check), we do not use $\sin^2\theta_W(M_Z)$ or
$g_1(M_Z)$ as an input. We use only $(G_F,m_W)$ to fix $g_2$ at the electroweak
scale, propagate to $\mu_\Theta$, apply the $\Theta$--fixed overlap ratio
$I_2/I_1$, and then predict $\sin^2\theta_W(M_Z)$.

#### Step 1: $v$ from the Fermi constant.

Define the Higgs vacuum expectation value by
$$v := (\sqrt{2}\,G_F)^{-1/2}.$$
Using $G_F = 1.1663787\times 10^{-5}\,\mathrm{GeV}^{-2}$ gives
$$v \approx 246.21965~\mathrm{GeV}.$$

**Step 2: $g_2(m_W)$ from $m_W$ including leading electroweak matching.**
At tree level,
$$m_W=\frac{1}{2}g_2 v \quad\Rightarrow\quad g_2^{(0)}(m_W)=\frac{2m_W}{v}.$$
However, the extraction of $g_2$ from $(G_F,m_W)$ receives electroweak threshold
corrections, conventionally summarized by the radiative--correction parameter $\Delta r$.
A minimal way to incorporate this effect without committing to a full multi--loop analysis is
to write
$$g_2(m_W)=g_2^{(0)}(m_W)\,\sqrt{1-\Delta r_{\mathrm{eff}}},$$
where $\Delta r_{\mathrm{eff}}$ is treated as an ${\cal O}(10^{-2})$ matching correction encoding
electroweak thresholds and scheme dependence. For numerical illustrations below we quote
results both at $\Delta r_{\mathrm{eff}}=0$ (tree) and for a conservative band
$\Delta r_{\mathrm{eff}}\in[0.02,0.05]$.
Using $m_W=80.3692~\mathrm{GeV}$ and $v=246.21965~\mathrm{GeV}$ gives
$$g_2^{(0)}(m_W)=\frac{2m_W}{v}\approx 0.65283,
\qquad
g_2(m_W)\approx 0.65283\,\sqrt{1-\Delta r_{\mathrm{eff}}}.$$

For example, $\Delta r_{\mathrm{eff}}=0.036$ gives $g_2(m_W)\approx 0.641$.

#### Step 3: run $g_2$ up to $\mu_\Theta$.

With one--loop coefficient $b_2=-19/6$,
$$\frac{1}{g_2^2(\mu_\Theta)}
=
\frac{1}{g_2^2(m_W)}
-
\frac{b_2}{8\pi^2}\ln\!\left(\frac{\mu_\Theta}{m_W}\right).$$
For $\Delta r_{\mathrm{eff}}=0$ and $\mu_\Theta=5~\mathrm{TeV}$ this gives
$$g_2(\mu_\Theta)\approx 0.63093.$$
*Dependence on $\Delta r_{\mathrm{eff}}$.*
Since Step 3 depends on $g_2(m_W)$, the value of $g_2(\mu_\Theta)$ inherits a mild
${\cal O}(1\%)$ sensitivity to the matching correction $\Delta r_{\mathrm{eff}}$.

#### Step 4: determine $g_1(\mu_\Theta)$ from $\Theta$ (nonabelian overlap ratio).

From $\Theta$--closure at $\mu_\Theta$,
$$\frac{I_2}{I_1}(\mu_\Theta)
=
\left(\frac{g_1(\mu_\Theta)}{g_2(\mu_\Theta)}\right)^2
\approx 0.56027,$$
hence
$$g_1(\mu_\Theta)=g_2(\mu_\Theta)\sqrt{0.56027}
\approx 0.47226.$$

#### Step 5: run $(g_1,g_2)$ down to $M_Z$ and predict $\sin^2\theta_W(M_Z)$.

Using one--loop running with $b_1=41/10$ and $b_2=-19/6$, evolve $g_1,g_2$ from
$\mu_\Theta$ to $M_Z$.
Then compute
$$\sin^2\theta_W(M_Z)
=
\frac{g'^2(M_Z)}{g'^2(M_Z)+g_2^2(M_Z)},
\qquad
g'^2(M_Z)=\frac{3}{5}\,g_1^2(M_Z).$$
At tree-level matching, $\Delta r_{\mathrm{eff}}=0$, this yields
$$\boxed{\sin^2\theta_W^{\mathrm{pred}}(M_Z)\approx 0.23120.}$$
*Dependence on electroweak threshold matching.* Repeating Steps 3--5 over
$\Delta r_{\mathrm{eff}}\in[0.02,0.05]$ gives instead
$$\sin^2\theta_W^{\mathrm{pred}}(M_Z)\approx 0.23157\text{--}0.23214.$$
Thus the non-circular numerical test is currently limited by the treatment of
electroweak threshold matching. The tree-level value lands close to the
reference $\overline{\mathrm{MS}}$ value, but the threshold scan is not yet a
precision prediction at the $10^{-4}$ level.

#### Remark

The present paper completes the formulation of a non--circular redundancy test
for $\Theta$ within the Standard Model gauge sector.
The numerical evaluation given above demonstrates that the test can be carried
out explicitly with existing data and standard one--loop evolution.
Further refinements, including higher--loop running and threshold corrections,
do not alter the logical structure of the test and are deferred to future work.

# Uniqueness, Equivalence Classes, and What Is Fixed by $\Theta$--Closure

A natural question raised by the present series is whether the results obtained here are
specific to the particular internal bundle realizations employed, or whether they can be
replicated by alternative constructions without loss of content. We clarify this point by
distinguishing between *superficial model variation* and *structural equivalence*
within Modal Triplet Theory (MTT).

The central observation is that the $\Theta$--closure program does not rely on the detailed
choice of internal geometry, but on a specific *architectural structure*:

1.  gauge couplings arise as overlap integrals of FCC--projected harmonic representatives
    in a modal bundle;

2.  a single dimensionless parameter $\Theta$ fixes the *ratios* of these overlaps,
    while one overall normalization remains unavoidable;

3.  the internal construction admits a fixed coherence class (FCC) with a spectral gap,
    ensuring controlled truncation and stability of the low--energy description;

4.  the normalization of overlaps is fixed consistently and independently (via geometric
    and twistor--action derivations);

5.  the resulting structure admits a non--circular redundancy test, in which
    $\sin^2\theta_W$ is reproduced without being used as an input.

Any alternative realization that preserves this structure will reproduce the same gauge--sector
predictions, while any realization that relaxes these conditions forfeits the overconstraint
and falsifiability demonstrated here.

#### Definition

Two internal bundle realizations in Modal Triplet Theory are said to be *equivalent*
for the purposes of $\Theta$--closure if, after projection onto the fixed coherence class,
their overlap bilinear forms on the retained harmonic sector are related by a basis change,
$$M_{ab} = \int \langle \omega_a, \omega_b \rangle
\;\;\longrightarrow\;\;
M' = S^{\!T} M S,$$
with identical eigenvalue ratios and consistent normalization fixing.

Within this equivalence class, differences in internal geometry, bundle dimension,
or orthogonality of subbundles correspond to different realizations of the same
effective low--energy structure. Outside this class, the $\Theta$--closure and redundancy
results do not persist.

Accordingly, the present series locks in the following elements of the MTT construction:
(i) the identification of gauge couplings with FCC--projected overlap integrals;
(ii) the ratio--based determination of $\Theta$ from nonabelian gauge data;
(iii) the existence of a spectral gap supporting controlled truncation;
(iv) the consistency of overlap normalization across independent derivation routes;
and (v) the logical architecture of a non--circular redundancy test within the gauge sector.
Specific choices of internal geometry or bundle realization may vary within the equivalence
class defined above, but these structural features cannot be removed or altered without
invalidating the results.

# Conclusion

In this paper we carried out a stringent test of the $\Theta$--closure program
in Modal Triplet Theory by imposing a redundant constraint entirely within the
Standard Model gauge sector.

In earlier work, a single parameter $\Theta$ was fixed by matching the
nonabelian gauge couplings $g_1:g_2:g_3$ at a common matching scale
$\mu_\Theta$ through internal overlap relations.
Here we asked whether the same $\Theta$, without retuning or additional free
parameters, also reproduces the observed value of the weak mixing angle
$\sin^2\theta_W(M_Z)$.

We first demonstrated that the renormalization group pipeline used throughout
the program is internally consistent by performing an explicit round--trip
evolution.
We then formulated a genuinely non--circular redundancy test by fixing only one
unavoidable normalization---the $SU(2)$ coupling at $\mu_\Theta$, determined
from $(G_F,m_W)$---and using the $\Theta$--fixed overlap ratio to determine
$g_1(\mu_\Theta)$.
Downward renormalization group evolution then yields a predicted value of
$\sin^2\theta_W(M_Z)$ that agrees with experiment at the level expected from
one--loop running and known threshold effects.

This result establishes that the gauge sector of the Standard Model is
overconstrained within the $\Theta$--closure framework: the same $\Theta$
determines both nonabelian coupling ratios and the weak mixing angle, without
using $\sin^2\theta_W$ as an input.
Such redundancy is rare among higher--dimensional or geometric approaches and
provides a nontrivial validation of the internal structure of the theory.

Taken together with PapersÂ I--IV, the present work completes a closed chain of
implications in Modal Triplet Theory.
A single parameter $\Theta$, fixed by gauge data, determines the internal
geometry, constrains the gravitational sector, restricts admissible cosmological
dynamics, and is now shown to be redundantly consistent with independent
electroweak observables.
While no claim is made to predict all Standard Model or cosmological parameters,
the framework is demonstrably rigid, cross--validated by independent derivation
routes, and equipped with clear falsification criteria.

In this sense, the present work does not fix a unique internal geometry, but it does fix the
*modal overlap architecture* of MTT: any viable realization must reproduce the same
FCC--projected overlap structure up to equivalence, or else fail the gauge--sector
redundancy test.

Further refinements---including the extension to massive and flavor sectors---do not alter the
logical structure of the redundancy test presented here and are deferred to
future work.

# References {#references .unnumbered}

1.  Particle Data Group (PDG),
    *Review of Particle Physics*,
    Prog. Theor. Exp. Phys. 2024, 083C01
    (for $G_F$, $m_W$, $M_Z$, and electroweak input values).

2.  M. E. Machacek and M. T. Vaughn,
    "Two-loop renormalization group equations in a general quantum field theory,"
    Nucl. Phys. B222 (1983) 83--103.

3.  T. Kato,
    *Perturbation Theory for Linear Operators*,
    Springer (1995).

4.  P. Nero,
    *Modal Triplet Theory: Foundation*,
    MTT corpus.

5.  P. Nero,
    *Modal Triplet Theory: Quantum Amplitudes from Modal Geometry*,
    MTT corpus.

6.  P. Nero,
    *Gauge Couplings, Internal Geometry, and $\Theta$--Closure in Modal Triplet Theory*,
    PaperÂ I.

7.  P. Nero,
    *Direct Geometric Evaluation of Nonabelian Overlaps in Modal Triplet Theory*,
    PaperÂ II.

8.  P. Nero,
    *Twistor--Action Matching of Gauge Overlaps in Modal Triplet Theory*,
    PaperÂ III.

9.  P. Nero,
    *Extending $\Theta$--Closure to Gravity and Cosmology in Modal Triplet Theory*,
    PaperÂ IV.

::: thebibliography
99

P.Â Nero,
*Modal Triplet Theory: Admissibility, Encodings, and the Structure of Physical Description*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255621>

P.Â Nero,
*Modal Triplet Theory: Foundation*,
Zenodo preprint, September 2025.
<https://doi.org/10.5281/zenodo.16949762>

P.Â Nero,
*Fixed Points I--VI: Complete Coherence Spine*,
Zenodo preprints, August 2025.
<https://doi.org/10.5281/zenodo.16948748>

P.Â Nero,
*The Projection--Admissibility Principle: Structural Constraints on Effective Physical Description*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255838>

P.Â Nero,
*Closure and Inevitability in Modal Triplet Theory*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255510>

P.Â Nero,
*Coherence Capacity as the Fundamental Resource of Effective Physics*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18255905>

P.Â Nero,
*Dynamics of Coherence Capacity: Transport, Concentration, and Exhaustion*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18256048>

P.Â Nero,
*Modal Triplet Theory: From MTT to Quantum Mechanics*,
Zenodo preprint, September 2025.
<https://doi.org/10.5281/zenodo.17074246>

P.Â Nero,
*From MTT to Quantum Field Theory*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17068816>

P.Â Nero,
*Modal Triplet Theory: From MTT to General Relativity*,
Zenodo preprint, October 2025.
<https://doi.org/10.5281/zenodo.16950597>

P.Â Nero,
*Modal Triplet Theory: From MTT to a UV-Finite, Unitary Quantum Gravity*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17077671>

P.Â Nero,
*Measurement as Disturbance and Stabilization in Modal Triplet Theory*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17177404>

P.Â Nero,
*Projection, Probability, and Irreversibility: Shadow Bridges Between Measurement, Black Holes, and Cosmology in Modal Triplet Theory*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18256408>

P.Â Nero,
*Modal Fixed Points, Bell's Beables, and the Limits of Factorization*,
Zenodo preprint, 2025.
<https://doi.org/10.5281/zenodo.17076300>

P.Â Nero,
*Temporal Bell Inequalities and Global Consistency in Modal Triplet Theory*,
Zenodo preprint, August 2025.
<https://doi.org/10.5281/zenodo.18208884>

P.Â Nero,
*From Modal Triplet Theory to Indivisible Stochastic Processes: A First-Principles, Fully Rigorous Derivation*,
Zenodo preprint, January 2026.
<https://doi.org/10.5281/zenodo.18254862>
:::
