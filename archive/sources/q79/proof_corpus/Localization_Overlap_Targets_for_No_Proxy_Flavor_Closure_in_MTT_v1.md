---
abstract: |
  We translate the corrected flavor benchmark of Modal Triplet Theory (MTT) from
  matrix entries into localization-overlap targets.  In local string/geometric
  realizations, Yukawa magnitudes are commonly controlled by Gaussian or
  heat-kernel overlap factors of the form $\exp[-d^2/\sigma^2]$, while phases
  are controlled by holonomy characters.  The no-proxy flavor-closure problem
  therefore reduces, in part, to deriving a small set of dimensionless
  localization distances from the same pairwise bundle and calibrated geometry
  data.  This paper computes the target distances corresponding to the corrected
  CKM angles, PMNS angles, and fermion hierarchy ratios.  These targets do not
  yet prove closure; they define the geometric data that a successful no-proxy
  localization graph must generate.
author:
- Peter Nero
date: May 2026
title: |
  Localization-Overlap Targets for No-Proxy Flavor Closure in Modal Triplet Theory
---

# Purpose and scope

The corrected flavor benchmark now has three layers:

1.  real matrices reproducing masses and mixing magnitudes;

2.  complex holonomy phases reproducing CP benchmarks;

3.  finite holonomy characters discretizing those phases.

The next no-proxy step is to remove arbitrary matrix magnitudes.  In a local
geometric realization, the natural replacement is a localization-overlap model:
flavor hierarchies and mixing angles arise from distances between localized
zero-mode wavefunctions, not from chosen entries.

This paper computes the localization targets that the geometry must reproduce.
It is not yet a derivation of those targets from topology.

# Gaussian overlap convention

We use the dimensionless Gaussian convention
$$
\epsilon=\exp(-D^2),
$$
where
$$
D:=\frac{d}{\sigma}.
$$

Thus a target overlap magnitude $\epsilon$ corresponds to
$$
D(\epsilon)=\sqrt{-\log\epsilon}.
$$

This convention absorbs sector-dependent widths into the dimensionless
distance.  A later no-proxy solve must derive $d$ and $\sigma$ from the common
geometry rather than choosing $D$ directly.

# Mixing-angle localization targets

For the CKM benchmark we use
$$
s_{12}=0.2250,\qquad s_{23}=0.0411,\qquad s_{13}=0.0036.
$$

The corresponding localization distances are
$$
D_{12}^{q}=\sqrt{-\log(0.2250)}\approx1.221,
$$
$$
D_{23}^{q}=\sqrt{-\log(0.0411)}\approx1.787,
$$
$$
D_{13}^{q}=\sqrt{-\log(0.0036)}\approx2.372.
$$

For the PMNS benchmark
$$
\theta_{12}=33.4^\circ,\qquad
\theta_{23}=46.8^\circ,\qquad
\theta_{13}=8.6^\circ,
$$
so
$$
s_{12}\approx0.5505,\qquad s_{23}\approx0.7290,\qquad s_{13}\approx0.1495.
$$

The corresponding localization distances are
$$
D_{12}^{\ell}\approx0.773,
\qquad
D_{23}^{\ell}\approx0.562,
\qquad
D_{13}^{\ell}\approx1.378.
$$

The large PMNS angles therefore correspond to shorter localization distances
than the CKM angles, as expected in a geometric-overlap picture.

# Mass-hierarchy localization targets

Normalize each sector to its heaviest family.  Then a hierarchy ratio
$y_i/y_3$ corresponds to
$$
D_i=\sqrt{-\log(y_i/y_3)}.
$$

## Up quarks

Using
$$
(y_u,y_c,y_t)=(1.2\times10^{-5},\,1.6\times10^{-3},\,0.53),
$$
we obtain
$$
D_u\approx3.270,\qquad
D_c\approx2.409,\qquad
D_t=0.
$$

## Down quarks

Using
$$
(y_d,y_s,y_b)=(2.2\times10^{-4},\,5.5\times10^{-3},\,0.11),
$$
we obtain
$$
D_d\approx2.493,\qquad
D_s\approx1.731,\qquad
D_b=0.
$$

## Charged leptons

Using
$$
(y_e,y_\mu,y_\tau)=(2.8\times10^{-4},\,6.0\times10^{-3},\,0.10),
$$
we obtain
$$
D_e\approx2.424,\qquad
D_\mu\approx1.677,\qquad
D_\tau=0.
$$

## Light neutrinos

Using
$$
(m_1,m_2,m_3)=(0.0025,\,0.0087,\,0.050)\ \mathrm{eV},
$$
we obtain
$$
D_{\nu_1}\approx1.731,\qquad
D_{\nu_2}\approx1.322,\qquad
D_{\nu_3}=0.
$$

# Target table

::: center
  Quantity              Magnitude             $D=\sqrt{-\log\epsilon}$
  --------------------- --------------------- -------------------------
  CKM $s_{12}$          $0.2250$              $1.221$
  CKM $s_{23}$          $0.0411$              $1.787$
  CKM $s_{13}$          $0.0036$              $2.372$
  PMNS $s_{12}$         $0.5505$              $0.773$
  PMNS $s_{23}$         $0.7290$              $0.562$
  PMNS $s_{13}$         $0.1495$              $1.378$
  $y_u/y_t$             $2.26\times10^{-5}$   $3.270$
  $y_c/y_t$             $3.02\times10^{-3}$   $2.409$
  $y_d/y_b$             $2.00\times10^{-3}$   $2.493$
  $y_s/y_b$             $5.00\times10^{-2}$   $1.731$
  $y_e/y_\tau$          $2.80\times10^{-3}$   $2.424$
  $y_\mu/y_\tau$        $6.00\times10^{-2}$   $1.677$
  $m_1/m_3$             $5.00\times10^{-2}$   $1.731$
  $m_2/m_3$             $1.74\times10^{-1}$   $1.322$
:::

# Interpretation

The targets have a clear hierarchy:

- CKM mixing requires relatively separated quark localization centers.

- PMNS mixing requires more overlapping lepton localization centers.

- first-family mass suppression requires distances around $2.4$--$3.3$ in
  units of the relevant width.

- neutrino mass ratios are much less hierarchical than up-quark ratios.

This is qualitatively consistent with a localization picture.  The no-proxy
question is whether the pattern can be generated from a shared graph rather
than imposed entry by entry.

# No-proxy localization criterion

#### Definition

A localization graph $\mathcal G_{\mathrm{loc}}$ passes the no-proxy magnitude
test if the target distances above arise from:

1.  a finite set of family vertices;

2.  pairwise bundle intersection data;

3.  width/flux data inherited from the calibrated geometry;

4.  a finite allowed set of instanton or exceptional classes;

5.  no independent entry-wise distance assignments.

#### Fail condition

If each Yukawa entry requires its own distance, width, or suppression factor,
then the construction is only a reparameterization of the Yukawa matrices and
does not constitute flavor closure.

# Candidate graph problem

The next concrete task is:

> Find a small localization graph whose induced pairwise and trilinear distances
> reproduce the target table within high-scale flavor uncertainties.

This can be formulated as a finite optimization problem:

$$
\min_{\mathcal G_{\mathrm{loc}},\,\sigma,\,\mathcal I}
\sum_a
\left(
D_a^{\mathrm{model}}-D_a^{\mathrm{target}}
\right)^2,
$$
subject to:

- shared vertices across quark and lepton sectors;

- phase compatibility with the finite holonomy character model;

- no per-entry free widths;

- topology-only selection rules for allowed channels.

# Conclusion

This paper converts the corrected flavor benchmark into localization-overlap
targets.  It does not yet derive the targets, but it removes ambiguity about
what a successful no-proxy geometry must produce.

Together with the finite holonomy-character paper, the flavor closure problem
now has two explicit target layers:

1.  discrete holonomy characters for CP phases;

2.  dimensionless localization distances for magnitudes.

The next step is to solve, or fail to solve, the finite localization graph
problem.

