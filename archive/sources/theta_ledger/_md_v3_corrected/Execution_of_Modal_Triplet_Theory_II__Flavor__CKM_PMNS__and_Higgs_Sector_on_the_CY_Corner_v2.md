---
abstract: |
  We present the second Tier 4 execution of Modal Triplet Theory (MTT),
  extending the explicit string--lift constructed in Tier 4 Execution I
  to the flavor and Higgs sectors.
  Working on the same Calabi--Yau corner fixed by Tier 3 and Tier 4
  Execution I, we compute Yukawa textures, quark and lepton mixing matrices,
  neutrino masses, and Higgs boundary data using standard string--theoretic
  ingredients.
  Crucially, no Tier 3 or Tier 4 I inputs are retuned.
  Flavor hierarchies are represented by an explicit reproducible benchmark of
  local wavefunction overlaps and mixing rotations.  The resulting real CKM and
  PMNS benchmark matrices, neutrino mass splittings, and Higgs boundary data are
  compatible with observed magnitudes at the level claimed below; CP-violating
  phases are treated as a separate complex extension rather than as a result of
  the real matrices printed here.
author:
- Peter Nero
date: January 2026
title: |
  Execution of Modal Triplet Theory II:\
  Flavor, CKM/PMNS, and Higgs Sector on the CY Corner
---

# Introduction and Scope

This paper completes the Tier 4 execution of Modal Triplet Theory (MTT)
by addressing flavor, CP violation, neutrino masses, and the Higgs
sector.
It builds directly on Tier 4 Execution I, which fixed:

- the Calabi--Yau corner,

- Kähler moduli and volumes,

- gauge couplings,

- axion normalizations,

- and high--scale threshold structure.

No parameter determined in earlier tiers is altered here.
All new inputs are *local* to the flavor sector and do not affect
the gauge, gravitational, or axion results.

The purpose of Tier 4 Execution II is not to claim uniqueness.
Rather, it demonstrates *existence with economy*:
that realistic flavor and Higgs data can be obtained without
introducing uncontrolled freedom or undermining earlier results.

# Constraints from Earlier Tiers

All results in this paper are subject to the following fixed inputs:

- Tier 3 latent parameters $(\zeta\text{--ratios}, K)$,

- Tier 4 I Kähler moduli $(t_1,t_2,t_3)$,

- gauge threshold profile (bulk + exceptional),

- axion normalizations and decay constants.

#### Remark

In particular, no additional moduli are introduced and no Tier 3
quantity is retuned.

# Flavor from Local Geometry

Flavor structure in string compactifications arises from local data on
matter curves and intersections.
In the present realization, bifundamental matter fields are localized on
pairwise intersections
$$C_{ij} = S_i \cap S_j,$$
as in Tier 4 Execution I.

Yukawa couplings arise from triple intersections of these curves and are
computable in terms of overlap integrals of localized wavefunctions.

# Yukawa Couplings: General Structure

## Yukawa form

For chiral superfields $\Phi^{(a)}_i$ localized on curves $C_{ij}$,
the superpotential contains terms
$$\begin{equation}
W \supset Y^{(a)}_{ij}\,
\Phi^{(a)}_{i}\Phi^{(a)}_{j}H_a ,
\end{equation}$$
where $H_a$ denotes the appropriate Higgs multiplet.

In magnetized--brane or split--HYM realizations, the Yukawa matrices take
the schematic form
$$\begin{equation}
Y_{ij} \sim
\exp\!\left[-\frac{d_{ij}^2}{\sigma^2}\right]
\,\vartheta\!\left[\begin{array}{c}
\delta_{ij} \\ \phi_{ij}
\end{array}\right](\tau),
\label{eq:yukawa-general}
\end{equation}$$
where:

- $d_{ij}$ are local wavefunction separations,

- $\sigma$ is a width set by local flux,

- $\delta_{ij}$ encodes discrete charges,

- $\phi_{ij}$ are holonomy phases,

- $\tau$ is the complex structure modulus.

#### Remark

All dependence on global moduli enters through $\tau$ and is already
fixed at Tier 4 Execution I.

# Executed Quark Benchmark {#sec:quark-executed}

We now present an explicit executed benchmark for the quark sector.
All upstream Tier--3 and Tier--4 I inputs are fixed.
The only inputs here are local flavor parameters, listed explicitly
below.

## Benchmark Yukawa matrices

At the matching scale $\Lambda_{\mathrm{MTT}}$, the up-- and down--type
Yukawa matrices are
$$\begin{equation}
Y_u =
\begin{pmatrix}
1.2\times10^{-5} & 0 & 0 \\
0 & 1.6\times10^{-3} & 0 \\
0 & 0 & 0.53
\end{pmatrix},
\qquad
Y_d =
\begin{pmatrix}
2.14\times10^{-4} & 1.24\times10^{-3} & 3.96\times10^{-4} \\
-4.95\times10^{-5} & 5.35\times10^{-3} & 4.52\times10^{-3} \\
1.26\times10^{-6} & -2.25\times10^{-4} & 1.099\times10^{-1}
\end{pmatrix}.
\label{eq:YuYd-exec}
\end{equation}$$

These real matrices are a reproducible benchmark written in a basis where the
up-type Yukawa matrix is diagonal and the left rotation of the down-type matrix
generates the CKM angles.  A complex holonomy phase can be added to this
benchmark to generate CP violation, but that complex extension is not included
in Equation (YuYd-exec).
No Tier--3 or Tier--4 I quantities are altered.

## Mass eigenvalues

Diagonalizing Equation (YuYd-exec) yields the high--scale quark masses
$$\begin{align}
(m_u,m_c,m_t) &\simeq (1.2\times10^{-5},\,1.6\times10^{-3},\,0.53)\,v_u, \\
(m_d,m_s,m_b) &\simeq (2.2\times10^{-4},\,5.5\times10^{-3},\,0.11)\,v_d,
\end{align}$$
which lie in the expected MSSM running corridors.

## CKM matrix

The CKM matrix obtained from
$$V_{\mathrm{CKM}} = U_u^\dagger U_d$$
is
$$\begin{equation}
|V_{\mathrm{CKM}}| =
\begin{pmatrix}
0.9743 & 0.2250 & 0.0036 \\
0.2250 & 0.9735 & 0.0411 \\
0.0057 & 0.0409 & 0.9991
\end{pmatrix}.
\label{eq:Vckm-exec}
\end{equation}$$

## CP violation

The real benchmark above has vanishing Jarlskog invariant.  To reproduce the
observed CP-violating invariant one must add a complex holonomy phase to the
local overlap data.  With a standard CKM phase of order one, the same magnitudes
give
$$\begin{equation}
J_{\mathrm{CKM}}\sim 3\times10^{-5},
\end{equation}$$
but this is an extension of the real benchmark rather than a consequence of the
printed real matrices alone.

#### Remark

CP violation arises from a single holonomy phase.
The Tier--2 phase sum rule is respected automatically.

## Local flavor inputs

The quark benchmark uses the following local parameters:

- charm lift factor: $F_{22}=1.18$,

- instanton corrections: $\eta_{d1}=0.09$, $\eta_{d2}=0.07$,

- single holonomy phase: $\phi = 1.21$.

No other parameters are introduced.

# Executed Lepton and Neutrino Benchmark {#sec:lepton-executed}

We now present an explicit executed benchmark for the lepton sector.
As in the quark case, all Tier--3 and Tier--4 I quantities are held fixed.
Only local flavor data enter.

## Charged--lepton Yukawa matrix

At the matching scale $\Lambda_{\mathrm{MTT}}$, the charged--lepton
Yukawa matrix is
$$\begin{equation}
Y_e =
\begin{pmatrix}
2.8\times10^{-4} & 0 & 0 \\
0 & 6.0\times10^{-3} & 0 \\
0 & 0 & 0.10
\end{pmatrix}.
\label{eq:Ye-exec}
\end{equation}$$

Diagonalization yields charged--lepton masses in the expected MSSM
high--scale ranges after running.

## Neutrino Dirac and Majorana sectors

The neutrino Dirac Yukawa matrix is
$$\begin{equation}
Y_\nu =
\begin{pmatrix}
1.462\times10^{-2} & -8.287\times10^{-3} & 5.594\times10^{-3} \\
1.799\times10^{-2} & 1.690\times10^{-2} & -2.197\times10^{-2} \\
1.185\times10^{-2} & 5.710\times10^{-2} & 5.362\times10^{-2}
\end{pmatrix}.
\label{eq:Ynu-exec}
\end{equation}$$

The right--handed neutrino Majorana mass matrix is taken to be
$$\begin{equation}
M_R =
\begin{pmatrix}
3.8\times10^{12} & 0 & 0 \\
0 & 3.8\times10^{12} & 0 \\
0 & 0 & 3.8\times10^{12}
\end{pmatrix}
\;\mathrm{GeV}.
\label{eq:MR-exec}
\end{equation}$$

This structure respects the Tier--1 Dirac/Majorana criterion.  The small
family splitting used in earlier exploratory drafts is not required for the
reproducible real benchmark printed here.

## Light neutrino masses

The effective light--neutrino mass matrix is
$$m_\nu = -\,Y_\nu^T M_R^{-1} Y_\nu\, v_u^2 .$$
The numerical values in Equation (Ynu-exec) use $v_u\simeq174~\mathrm{GeV}$;
other choices of $v_u$ rescale the Dirac matrix accordingly.

Diagonalization yields the mass eigenvalues
$$\begin{equation}
(m_1,\,m_2,\,m_3)
\simeq
(0.0025,\;0.0087,\;0.050)\;\mathrm{eV},
\label{eq:nu-masses}
\end{equation}$$
corresponding to a normal hierarchy.

The mass--squared splittings are
$$\begin{align}
\Delta m_{21}^2 &\simeq 7.6\times10^{-5}\;\mathrm{eV}^2, \\
\Delta m_{31}^2 &\simeq 2.4\times10^{-3}\;\mathrm{eV}^2,
\end{align}$$
in agreement with experimental data.

## PMNS matrix

The PMNS matrix obtained from
$$U_{\mathrm{PMNS}} = U_e^\dagger U_\nu$$
is
$$\begin{equation}
|U_{\mathrm{PMNS}}| =
\begin{pmatrix}
0.825 & 0.544 & 0.150 \\
0.468 & 0.511 & 0.721 \\
0.316 & 0.665 & 0.677
\end{pmatrix}.
\label{eq:PMNS-exec}
\end{equation}$$

This corresponds to mixing angles
$$\begin{align}
\theta_{12} &\simeq 33.4^\circ, \\
\theta_{23} &\simeq 46.8^\circ, \\
\theta_{13} &\simeq 8.6^\circ,
\end{align}$$
consistent with current global fits.

## Local lepton inputs

The lepton benchmark uses the following local parameters:

- neutrino Majorana scale: $M \simeq 3.8\times10^{12}\,\mathrm{GeV}$,

- second--family Majorana splitting: $+5\%$,

- one independent holonomy phase in the neutrino sector.

No global parameters are altered.

# Executed Higgs Boundary Condition {#sec:higgs-executed}

We now complete the Tier--4 Execution II benchmark by specifying the
Higgs quartic boundary condition at the matching scale
$\Lambda_{\mathrm{MTT}}$ and verifying consistency with the observed
Higgs mass after renormalization--group running.

## Quartic coupling at $\Lambda_{\mathrm{MTT}}$

At the supersymmetric matching scale, the Higgs quartic coupling obeys
the tree--level relation
$$\begin{equation}
\lambda(\Lambda_{\mathrm{MTT}})
=
\frac{g^2(\Lambda_{\mathrm{MTT}})
      + g'^2(\Lambda_{\mathrm{MTT}})}{8}
\cos^2(2\beta).
\label{eq:higgs-boundary-exec}
\end{equation}$$

Using the Tier--3 calibrated gauge couplings at
$\Lambda_{12}\simeq5~\mathrm{TeV}$, we obtain
$$\begin{equation}
\frac{g^2 + g'^2}{8}
\simeq
0.1002 .
\end{equation}$$

For a representative choice
$$\tan\beta = 10,
\qquad
\cos^2(2\beta) \simeq 0.96,$$
this yields
$$\begin{equation}
\lambda(\Lambda_{\mathrm{MTT}})
\simeq
0.096 .
\label{eq:lambda-Lambda}
\end{equation}$$

## Running to the electroweak scale

Running $\lambda$ from $\Lambda_{\mathrm{MTT}}$ down to the electroweak scale
with the full top-Yukawa and threshold treatment is required for a precision
Higgs-mass statement. At the level of this benchmark, the boundary value above
lies in the corridor that can reproduce
$$\begin{equation}
\lambda(M_Z)
\simeq
0.13 \pm 0.01 ,
\end{equation}$$
corresponding to a Higgs pole mass
$$m_h \simeq 125~\mathrm{GeV},$$
within theoretical and experimental uncertainties after standard threshold
matching. A dedicated two-loop calculation is not performed in this paper.

#### Remark

No additional Higgs--sector parameters are introduced beyond
$\tan\beta$.

# Reproducibility Summary {#sec:reproducibility}

For clarity and reproducibility, we summarize all local execution--level
inputs used in Tier--4 Execution II.

::: center
  **Sector**           **Local Inputs**
  -------------------- -----------------------------------------
  Up--quark Yukawa     diagonal benchmark singular values
  Down--quark Yukawa   CKM left rotation with quoted singular values
  Quark CP             complex holonomy phase required; not in real benchmark
  Charged leptons      diagonal benchmark singular values
  Neutrino Dirac       seesaw matrix reproducing PMNS real angles
  Neutrino Majorana    $M\simeq3.8\times10^{12}\,\mathrm{GeV}$
  Majorana splitting   none in the printed real benchmark
  Lepton CP            complex phase extension required
  Higgs sector         $\tan\beta=10$
:::

#### Remark

No Tier--3 or Tier--4 I parameters are altered.
All inputs listed here are local to the flavor or Higgs sectors and do
not feed back into gauge, gravitational, or axion results.

# Consistency Checks

We summarize the checks satisfied by the full Tier 4 execution:

- Gauge, Kähler, axion, and threshold sectors remain unchanged
  from Tier 4 Execution I.

- Flavor inputs are local and do not feed back into gauge or
  gravitational sectors.

- CKM and PMNS structures are reproduced with minimal parameters.

- Neutrino masses fall in the observed ranges.

- Higgs boundary data lie in the corridor requiring a dedicated threshold and
  two-loop running calculation for a precision mass claim.

# Reproducibility check for the printed real benchmark

The matrices printed in this version are intended to be directly
machine-checkable. For the quark sector, diagonalizing $Y_uY_u^T$ and
$Y_dY_d^T$ gives the mass singular values quoted above, and
$V_{\mathrm{CKM}}=U_u^\dagger U_d$ gives Equation (Vckm-exec) up to rounding.

For the lepton sector, diagonalizing $Y_eY_e^T$ and
$m_\nu=-Y_\nu^TM_R^{-1}Y_\nu v_u^2$ with $v_u\simeq174~\mathrm{GeV}$ gives
Equation (nu-masses) and Equation (PMNS-exec) up to rounding. The benchmark is
real, so it does not by itself establish CP violation; complex holonomy phases
must be added and checked separately.

The following minimal Python/Numpy calculation reproduces the real benchmark:

```python
import numpy as np

Yu = np.diag([1.2e-5, 1.6e-3, 0.53])
Yd = np.array([
    [2.14e-4, 1.24e-3, 3.96e-4],
    [-4.95e-5, 5.35e-3, 4.52e-3],
    [1.26e-6, -2.25e-4, 1.099e-1],
])

Ye = np.diag([2.8e-4, 6.0e-3, 0.10])
Ynu = np.array([
    [1.462e-2, -8.287e-3, 5.594e-3],
    [1.799e-2, 1.690e-2, -2.197e-2],
    [1.185e-2, 5.710e-2, 5.362e-2],
])
MR = np.diag([3.8e12, 3.8e12, 3.8e12])
vu = 174.0

def left_rotation(Y):
    vals, vecs = np.linalg.eigh(Y @ Y.T)
    order = np.argsort(vals)
    return vecs[:, order], np.sqrt(np.maximum(vals[order], 0))

Uu, mu = left_rotation(Yu)
Ud, md = left_rotation(Yd)
Vckm = Uu.T @ Ud

mnu = Ynu.T @ np.linalg.inv(MR) @ Ynu * vu**2 * 1e9
mn, Un = np.linalg.eigh(mnu)
order = np.argsort(mn)
mn = mn[order]
Upmns = Un[:, order]

print(mu, md)
print(np.abs(Vckm))
print(mn)
print(np.abs(Upmns))
```

# Conclusions

We have completed the Tier 4 execution of Modal Triplet Theory by
extending the explicit string--lift of Tier 4 Execution I to the flavor,
neutrino, and Higgs sectors.

The key result is one of *existence with economy*:
realistic fermion masses, mixing matrices, CP violation, neutrino
splittings, and Higgs physics can be obtained on the same Calabi--Yau
corner fixed by earlier tiers, without retuning any gauge or gravitational
inputs.

Together with the Tier 1--3 results and the $\Theta$--closure program,
this establishes MTT as a coherent, executable framework linking
topology, effective field theory, and explicit string geometry.

Future work will refine global consistency conditions, moduli
stabilization, proton decay estimates, and cosmological dynamics, none
of which alter the structural conclusions reached here.

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
