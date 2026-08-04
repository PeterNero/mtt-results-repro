---
abstract: |
  We present a tiered methodology for extracting predictions from the Modal
  Triplet Theory (MTT) without requiring a full internal metric solve.
  The program is organized into four operational tiers with explicit
  contracts: inputs allowed, tools employed, and outputs guaranteed.
  Tier 1 delivers exact, topology--only results independent of geometry.
  Tier 2 adds geometry--light relations and inequalities.
  Tier 3 treats MTT as a *superset* theory and backfits a minimal set
  of latent constants from overlaps among gauge, gravitational, and
  auxiliary sectors using one (or two) empirical inputs.
  Tier 4 introduces a string--lift, mapping MTT bundles to heterotic or
  type IIB/F--theory compactifications so that internal data reduce to
  intersection numbers, Chern classes, periods, and standard threshold
  formulae.
  We give explicit algorithms, uncertainty accounting, and a consolidated
  test matrix that separates what is proved, what is executed numerically,
  and what remains open.
  This paper defines the computational architecture of the MTT program and
  serves as the methodological reference for subsequent results.
author:
- Peter Nero
date: January 2026
title: |
  A Tiered Roadmap for Calculations in\
  Modal Triplet Theory (MTT)
---

# Introduction and Scope

Modal Triplet Theory (MTT) realizes the Standard Model and gravity as
emergent sectors of a higher--dimensional modal geometry with three
interlocking bundle factors.
The theory has matured to the point where a wide range of exact,
bounded, and calibratable predictions can be obtained *without*
solving the internal metric problem directly.

The purpose of this paper is *not* to present new phenomenological
results.
Instead, it provides a *roadmap* that organizes the calculational
program into operational tiers with clearly defined contracts.
Each tier specifies:

- what inputs are permitted,

- what mathematical tools may be used,

- and what class of outputs is guaranteed.

This separation serves three goals:

1.  to deliver exact or bounded results as early as possible,

2.  to make explicit which conclusions are rigid and which are
    execution--dependent,

3.  to prevent confusion between necessity (structure) and existence
    (realization).

Later papers in the MTT series instantiate particular tiers.
This paper defines the framework against which those results should be
read and evaluated.

#### Numerical provenance.

All explicit numerical results that were previously distributed across standalone
numerics notes have been fully subsumed into the corresponding Tier 3 and Tier 4
execution papers. The present Roadmap defines methodology, tier contracts, and
validation criteria only; it does not duplicate executed results. Concretely:
Tier 3 numerics (crossing scales, $\zeta$-ratios, $K$, minimum-norm thresholds,
and $\alpha_s(M_Z)$ cross-predictions) appear in *Superset Determinations in
Modal Triplet Theory (MTT)*, and Tier 4 numerics (Kähler moduli, thresholds,
axions, Yukawas, CKM/PMNS, and Higgs boundary data) appear in
*Execution of Modal Triplet Theory I* and *Execution of Modal Triplet
Theory II*. Earlier numerics notes may therefore be retired without loss of content.

## Latent parameters and conventions

We work on a spacetime of the form
$$M_{10} = Y_4 \times X_6 ,$$
where $Y_4$ is a smooth, oriented, spin four--manifold and $X_6$ is the
internal modal space.

The central latent quantities used throughout the program are:

- a common gauge scale
  $$K := \frac{4\pi\,\mathrm{Vol}(X_6)}{g_{10}^2} ,$$

- dimensionless harmonic normalization weights
  $$\alpha_r^{-1}(\Lambda) \equiv \frac{4\pi}{g_r^2(\Lambda)} = K\,\zeta_r,
    \qquad r \in \{1,2,3\},$$

- and the gravitational overlap
  $$G_{\mathrm{eff}}^{-1} = G_{10}^{-1}\,\mathrm{Vol}(X_6),
    \qquad G_{\mathrm{eff}} \equiv G_N .$$

The $\zeta_r$ are defined only up to an overall normalization absorbed
into $K$; only ratios $\zeta_a/\zeta_b$ are intrinsic.
Hypercharge is always taken in GUT normalization,
$g' = \sqrt{3/5}\,g_1$.

# Tier Taxonomy and Contracts

We partition the MTT calculational program into four operational tiers.
Each tier has a strict contract specifying allowed inputs, tools, and
outputs.

#### Definition

A *tier* is defined by:

1.  the class of admissible inputs,

2.  the mathematical tools permitted,

3.  the type of outputs guaranteed,

4.  and the accuracy class of those outputs.

Later tiers may use results from earlier tiers but not vice versa.

## Tier 0: Units and conventions

Tier 0 fixes units ($c=\hbar=k_B=1$), normalization conventions, and
notation.
It produces no physical predictions.

## Tier 1: Topology--only predictions (exact)

#### Inputs.

Topology of $Y_4$, spin structure, Chern classes of line bundles, flux
balance conditions, and representation assignments.

#### Tools.

Index theory, cohomology, group theory, anomaly bookkeeping, and
selection rules.

#### Outputs.

Exact, discrete statements independent of any internal metric:

- family number by Dirac index,

- exact Standard Model hypercharges from difference charges,

- cancellation of all local gauge and gravitational anomalies,

- absence of the SU(2) Witten global anomaly for three families,

- topological criterion for Dirac vs. Majorana masses,

- strong--CP relaxation via a central PQ--like symmetry with integer
  domain--wall number,

- forbiddance of many baryon/lepton violating operators,

- equality of low--energy wave speeds $c_{\mathrm{grav}}=c_{\mathrm{em}}$,

- holonomy determinant/phase sum rules.

#### Accuracy class.

Exact (topological).

## Tier 2: Geometry--light relations (bounded)

#### Inputs.

Tier 1 structure plus mild symmetry or positivity assumptions (e.g. modal democracy, spectral gaps).

#### Tools.

Algebraic identities, inequalities, sign analysis, and first--principles
bounds.

#### Outputs.

Relations and bounds that do not require harmonic norms:

- high--scale electroweak mixing
  $\sin^2\theta_W = 3/8$ under modal symmetry,

- holonomy phase/determinant sum constraints,

- qualitative renormalization--group sign structure,

- curvature--mass drift identities and FRW bounds,

- PPN bound $\gamma = 1 + O(\Delta_{\mathrm{curv}})$.

#### Accuracy class.

Exact identities or rigorous inequalities.

## Tier 3: Calibratable constants via superset overlaps

Tier 3 treats MTT as a *superset theory*.
Instead of computing internal harmonic norms directly, one introduces a
small set of latent scalars and determines them algebraically from
overlaps among gauge, gravitational, and auxiliary sectors using a
single matching.

#### Inputs.

- Low--energy gauge couplings evolved to a matching scale
  $\Lambda_{\mathrm{MTT}}$ via a specified RGE scheme (SM or MSSM,
  one-- or two--loop).

- Newton's constant $G_N$.

- One additional non--geometric closure (modal democracy, PQ
  prior, or PPN bound).

#### Latent variables.

$$\mathcal{L} =
\left\{
\frac{\zeta_2}{\zeta_1},
\frac{\zeta_3}{\zeta_1},
K,
\frac{\mathrm{Vol}(X_6)}{g_{10}^2},
\mathrm{Vol}(X_6) G_{10}^{-1}
\right\}.$$

#### Tools.

Renormalization--group evolution, algebraic ratios, overlap identities,
and linear error propagation.

#### Outputs.

- Geometry--independent extraction of $\zeta$--ratios from data.

- Calibration of $K$ from a single coupling.

- Determination of two independent combinations of
  $(\mathrm{Vol}, g_{10}, G_{10})$.

- Cross--predictions at $\Lambda_{\mathrm{MTT}}$
  (e.g. $\sin^2\theta_W(\Lambda)$, $g_3^2/g_2^2$).

- Round--trip consistency checks under RGE flow.

#### Accuracy class.

Percent--level, controlled by RGE scheme and threshold systematics.

### Algorithm 1: Overlap--Backfit

1.  Choose a matching scale $\Lambda_{\mathrm{MTT}}$ and RGE scheme.

2.  Run $(\alpha_1,\alpha_2,\alpha_3)$ from $M_Z$ to
    $\Lambda_{\mathrm{MTT}}$.

3.  Extract ratios
    $$\frac{\zeta_2}{\zeta_1}
            = \frac{\alpha_2^{-1}(\Lambda)}{\alpha_1^{-1}(\Lambda)},
            \qquad
            \frac{\zeta_3}{\zeta_1}
            = \frac{\alpha_3^{-1}(\Lambda)}{\alpha_1^{-1}(\Lambda)}.$$

4.  Calibrate $K = \alpha_r^{-1}(\Lambda)/\zeta_r$ using any $r$.

5.  Use $G_N$ to fix $\mathrm{Vol}(X_6) G_{10}^{-1}$.

6.  Apply one closure to solve $(\mathrm{Vol}, g_{10}, G_{10})$.

7.  Run back to $M_Z$ and verify agreement within uncertainties.

## Tier 4: String--lift geometry for quantitative predictions

Tier 4 introduces a concrete geometric realization.
The defining principle is that internal harmonic integrals are replaced
by standard algebraic--geometric data.

#### Inputs.

- Tier 3 latents $(\zeta$--ratios, $K)$.

- Choice of embedding: heterotic line--bundle sum or
  type IIB/F--theory D7--brane stacks.

#### Tools.

Intersection rings $\kappa_{ijk}$, Chern classes, line--bundle slopes,
Picard--Fuchs periods, flux and tadpole constraints, one--loop threshold
formulae.

#### Outputs.

- Kähler moduli ratios and divisor volumes.

- Gauge kinetic matrix and axion decay constants.

- High--scale threshold profiles consistent with Tier 3 targets.

- (Optionally) Yukawa textures, CKM/PMNS, Higgs boundary data.

#### Accuracy class.

Model--dependent execution with explicit uncertainty bands.

### Algorithm 2: String--Lift Backfit

1.  Choose a pilot Calabi--Yau (or toroidal) compactification with
    three distinguished divisors or line bundles satisfying
    $c_1$--balance.

2.  Compute intersection numbers $\kappa_{ijk}$ and topological
    invariants.

3.  Solve for Kähler moduli ratios from the Tier 3 $\zeta$--ratios.

4.  Calibrate $K$ using one gauge coupling and $G_N$.

5.  Include one--loop thresholds and check consistency with Tier 3
    minimal or minimum--norm profiles.

6.  Compute selected Yukawa entries or axion couplings as desired.

# Toolbox and Validation Workflows

This section summarizes the computational tools associated with each
tier and the validation checks that ensure internal consistency across
the program.

## Tier--wise tool summary

#### Tier 1 tools.

- Index theorems (Atiyah--Singer).

- Chern class algebra and flux balance.

- Group--theoretic anomaly sums.

- Line--bundle triviality and selection rules.

#### Tier 2 tools.

- Algebraic identities (phase/determinant sums).

- Renormalization--group sign analysis.

- Curvature--mass inequalities and PPN bounds.

#### Tier 3 tools.

- One-- and two--loop RGE solvers (SM/MSSM, piecewise).

- Algebraic ratio extraction and calibration.

- Least--squares or minimum--norm threshold diagnostics.

- Linear error propagation and small MCMC fits (optional).

#### Tier 4 tools.

- Algebraic geometry: intersection rings $\kappa_{ijk}$.

- Line--bundle cohomology and slope stability.

- Picard--Fuchs solvers for periods.

- Flux, tadpole, and anomaly consistency checks.

- One--loop threshold formulae.

## Validation and cross--checks

At each tier, internal consistency is enforced by explicit checks:
**Validation and cross--checks.**

- Internal algebra:
  indices, anomaly cancellation, and phase sum rules.

- RGE round--trip:
  parameters extracted at $\Lambda_{\mathrm{MTT}}$ are run back
  to $M_Z$ and compared with data
  (see Tier 3 Superset Determinations, Sec. 19).

- Normalization consistency:
  the scale $K$ agrees when extracted from different gauge factors.

- String--lift closure:
  slopes, tadpoles, and massless $U(1)$ conditions are satisfied,
  and threshold profiles remain controlled.

# TOE Test Matrix

The following matrix summarizes the status of major tests organized by
tier. "Proved" denotes a rigorous derivation from MTT axioms;
"Executed" denotes a completed numerical or algebraic realization;
"Planned" denotes a well--specified pipeline not executed here.

**Tier 1 (Topology--only).**

- Family number by index Proved

- Exact SM hypercharges Proved

- Local and global anomaly cancellation Proved

- Dirac vs. Majorana criterion Proved

- Strong--CP relaxation, integer $N_{\mathrm{DW}}$ Proved

- Operator forbiddance Proved

- $c_{\mathrm{grav}} = c_{\mathrm{em}}$ Proved

**Tier 2 (Geometry--light relations).**

- High--scale electroweak mixing identity
  $\sin^2\theta_W = 3/8$ under modal democracy, with controlled
  sensitivity to deviations.

- Holonomy determinant and phase sum rules implied by canonical
  trivialization.

- Qualitative renormalization--group sign structure
  (recalled from Tier 1 for completeness).

- Curvature--mass drift identities and FRW bounds.

- Post--Newtonian inequality target
  $\gamma = 1 + O(\Delta_{\mathrm{curv}})$, understood as a
  conditional Tier--2 bound.

**Tier 3 (Superset calibration).**

- Geometry--independent extraction of modal weight ratios
  $\zeta_2/\zeta_1$ and $\zeta_3/\zeta_1$ from executed RGE running.

- Executed determination of crossing scales
  $\Lambda_{12}$ and $\Lambda_{23}$ (SM two--loop canonical).

- Numerical calibration of the common scale $K$ (Planck units),
  consistent across gauge factors.

- Determination of the two invariant combinations
  $\mathrm{Vol}(X_6)/g_{10}^2$ and
  $\mathrm{Vol}(X_6)\,G_{10}^{-1}$.

- Executed minimum--norm threshold diagnostic with a single bulk
  coefficient $\delta = -25.2 \pm 0.5$.

- Cross--prediction of $\alpha_s(M_Z)$ without additional tuning.

- Round--trip RGE consistency checks within stated uncertainties.

**Tier 4 (String--lift execution).**

- Existence of a consistent Calabi--Yau corner realizing the
  Tier 3 invariants (proved at the level of explicit construction).

- Executed gauge and Kähler sectors:
  explicit $t_i$, $\tau_i$, and $\mathrm{Vol}(X_6)$.

- Executed axion sector:
  explicit decay constants $f_a$ with ratios matching
  $\zeta$--ratios.

- Executed reproduction of Tier 3 minimum--norm thresholds from
  geometry, including the bulk coefficient $\delta=-25.2$ and
  small exceptional--cycle corrections.

- Executed flavor and Higgs sectors:
  explicit Yukawa matrices, CKM matrix and Jarlskog invariant,
  PMNS matrix and neutrino masses, and Higgs quartic boundary data.

- Explicit uncertainty accounting and EFT control checks.

# Roadmap and Milestones

With the tiered structure now fully instantiated, the Modal Triplet
Theory (MTT) program admits a clear and stable execution roadmap.
Each milestone below corresponds to a completed or well-defined tier,
with explicit success criteria and canonical paper references.

**M0: Methodological foundation (completed).**

- Definition of the tier taxonomy, contracts, and validation
  criteria.

- Separation of topology--only results from geometry--light,
  calibratable, and execution--level results.

- Consolidation of all numerical provenance into Tier 3 and
  Tier 4 execution papers.

**M1: Tier 1 exact constraints (completed).**

- Topology--only derivation of Standard Model hypercharges,
  family number, and anomaly cancellation.

- Dirac versus Majorana mass criterion and SU(2) global anomaly
  test.

- Canonical trivialization and holonomy phase sum rules.

**M2: Tier 2 geometry--light relations (completed).**

- High--scale electroweak mixing identity
  $\sin^2\theta_W=3/8$ under modal democracy.

- Curvature--mass drift identities and FRW bounds.

- Conditional post--Newtonian inequality
  $\gamma = 1 + O(\Delta_{\mathrm{curv}})$.

**M3: Tier 3 superset determinations (completed).**

- Geometry--independent extraction of $\zeta$--ratios and the
  common scale $K$ from executed RGE running.

- Executed determination of crossing scales
  $\Lambda_{12}$ and $\Lambda_{23}$.

- Minimum--norm threshold diagnostic with a single bulk
  coefficient $\delta=-25.2\pm0.5$.

- Cross--prediction of $\alpha_s(M_Z)$ and round--trip consistency
  checks.

**M4: Tier 4 execution I --- gauge, axion, and thresholds
(completed).**

- Explicit Calabi--Yau corner realizing all Tier 3 invariants.

- Executed Kähler moduli, divisor volumes, and internal volume.

- Explicit axion decay constants and geometric reproduction of the
  Tier 3 threshold structure.

**M5: Tier 4 execution II --- flavor and Higgs sectors
(completed).**

- Executed quark and lepton Yukawa matrices.

- Explicit CKM and PMNS matrices with CP violation.

- Neutrino masses and splittings from a seesaw realization.

- Executed Higgs quartic boundary condition consistent with
  $m_h\simeq125$ GeV.

**M6: Future directions (planned).**

- Proton decay operators and lifetime estimates.

- Moduli stabilization and vacuum selection.

- Cosmological dynamics and early--universe applications.

# Conclusions and Outlook

We have presented a fully tiered and execution--complete framework for
calculations in Modal Triplet Theory (MTT).
All results formerly distributed across standalone numerics notes have
been consolidated into the main text of the Tier 3 and Tier 4 execution
papers, leaving the present Roadmap as a purely methodological guide.

The tier structure cleanly separates:

- exact, topology--only constraints (Tier 1),

- geometry--light identities and bounds (Tier 2),

- geometry--free calibration of latent parameters (Tier 3),

- and explicit string--lift realizations (Tier 4).

This separation clarifies which results are rigid consequences of the
theory and which depend on particular realizations.
In particular, Tier 3 establishes MTT as a superset framework in which
all gauge and gravitational invariants are fixed algebraically from data
prior to any geometric input.
Tier 4 then demonstrates that these invariants can be realized
simultaneously in explicit string compactifications, including realistic
flavor and Higgs sectors, without retuning upstream inputs.

The resulting program is coherent, non--regressive, and falsifiable:
failure at any tier would isolate the source of inconsistency.
Conversely, successful execution through Tier 4 shows that topology,
effective field theory, and string geometry can be integrated into a
single calculational pipeline.

Future work will focus on extending the Tier 4 execution to global
consistency conditions, vacuum selection, and cosmology.
These developments will refine, but not alter, the structural results
established here.

The tiered Roadmap provided in this paper is intended as the canonical
reference for navigating the MTT corpus and for assessing future
extensions of the theory.

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
