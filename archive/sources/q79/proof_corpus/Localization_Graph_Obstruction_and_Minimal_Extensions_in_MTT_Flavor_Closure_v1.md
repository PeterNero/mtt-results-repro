---
abstract: |
  We test whether the localization-overlap targets for the corrected MTT flavor
  benchmark can be represented by the simplest no-proxy geometry: a single
  Euclidean localization graph with one Gaussian width per sector and pairwise
  mixing magnitudes $\epsilon_{ij}=\exp(-D_{ij}^2)$.  The CKM targets pass this
  test: their inferred distances satisfy the triangle inequalities and embed in
  a two-dimensional Euclidean localization plane.  The PMNS targets do not:
  the inferred distances violate the triangle inequality,
  $D_{12}^{\ell}+D_{23}^{\ell}<D_{13}^{\ell}$, by about $0.044$.  Therefore a
  single-channel, single-width Euclidean pairwise localization model cannot be
  the final no-proxy flavor closure geometry.  We identify the minimal allowed
  extensions: sector-dependent effective widths, multi-channel overlaps,
  non-Euclidean graph metrics, or seesaw-induced mixing not reducible to a
  single lepton localization triangle.  This converts the flavor-closure problem
  into a sharper pass/fail geometric test.
author:
- Peter Nero
date: May 2026
title: |
  Localization Graph Obstruction and Minimal Extensions in MTT Flavor Closure
---

# Purpose and scope

The localization-target paper translated flavor magnitudes into dimensionless
Gaussian distances
$$
\epsilon=\exp(-D^2).
$$

This paper asks whether those distances can be realized by the simplest possible
localization graph:

1.  three family vertices;

2.  one Euclidean metric;

3.  one effective width per sector;

4.  pairwise mixing magnitudes interpreted directly as Gaussian overlaps between
    family vertices.

This is the most economical no-proxy localization hypothesis.  If it works, the
flavor problem reduces to finding the actual graph in the Tier-4 geometry.  If
it fails, the failure identifies what extra structure is required.

# Simple pairwise localization hypothesis

Let the three family localization centers in a sector be
$$
p_1,\ p_2,\ p_3
$$
in a Euclidean localization space.  Suppose the pairwise mixing magnitude
between families $i$ and $j$ is
$$
s_{ij}\sim\exp(-D_{ij}^2),
\qquad
D_{ij}=\frac{\lVert p_i-p_j\rVert}{\sigma}.
$$

Then the inferred distances must satisfy the triangle inequalities:
$$
D_{12}+D_{23}\ge D_{13},
$$
$$
D_{12}+D_{13}\ge D_{23},
$$
$$
D_{23}+D_{13}\ge D_{12}.
$$

Failure of these inequalities rules out the simple pairwise Euclidean model for
that sector.

# CKM triangle test

From the corrected CKM targets:
$$
s_{12}=0.2250,\qquad s_{23}=0.0411,\qquad s_{13}=0.0036,
$$
we obtained
$$
D_{12}^q=1.221,\qquad
D_{23}^q=1.787,\qquad
D_{13}^q=2.372.
$$

The triangle margins are
$$
D_{12}^q+D_{23}^q-D_{13}^q\approx0.636,
$$
$$
D_{12}^q+D_{13}^q-D_{23}^q\approx1.807,
$$
$$
D_{23}^q+D_{13}^q-D_{12}^q\approx2.937.
$$

All are positive.  Therefore the CKM distance targets are compatible with a
simple Euclidean pairwise localization triangle.

One explicit two-dimensional embedding is
$$
p_1^q=(0,0),
\qquad
p_2^q=(1.221,0),
$$
$$
p_3^q=(1.608,1.744).
$$

This does not prove no-proxy closure for quarks, but it shows that the simplest
geometric interpretation is not immediately obstructed.

# PMNS triangle test

From the corrected PMNS targets:
$$
\theta_{12}=33.4^\circ,\qquad
\theta_{23}=46.8^\circ,\qquad
\theta_{13}=8.6^\circ,
$$
we obtained
$$
D_{12}^{\ell}=0.773,\qquad
D_{23}^{\ell}=0.562,\qquad
D_{13}^{\ell}=1.378.
$$

The first triangle margin is
$$
D_{12}^{\ell}+D_{23}^{\ell}-D_{13}^{\ell}
\approx
-0.044.
$$

Thus
$$
D_{12}^{\ell}+D_{23}^{\ell}<D_{13}^{\ell}.
$$

The PMNS targets cannot be realized as three points in a Euclidean metric with a
single Gaussian width and direct pairwise overlap interpretation.

#### Proposition

The corrected PMNS localization targets obstruct the simple pairwise Euclidean
localization model.

#### Proof

Any three Euclidean points define distances satisfying the triangle
inequalities.  The inferred PMNS distances violate
$D_{12}+D_{23}\ge D_{13}$.  Therefore no such Euclidean triangle exists.

# Interpretation of the obstruction

The obstruction is small but real.  The deficit is
$$
\Delta_{\triangle}
=
D_{13}^{\ell}-D_{12}^{\ell}-D_{23}^{\ell}
\approx0.044.
$$

Equivalently, increasing the two shorter lepton distances by a common factor
$$
s_{\min}
=
\frac{D_{13}^{\ell}}{D_{12}^{\ell}+D_{23}^{\ell}}
\approx1.033
$$
would restore the triangle inequality.

This means the lepton sector is close to a simple localization geometry, but not
exactly compatible with it under the naive assumptions.

# Minimal extensions

The obstruction tells us what additional structure is minimally required.

## Extension A: sector-dependent effective widths

If $s_{ij}$ uses different effective widths for different channels,
$$
s_{ij}\sim\exp\!\left(-\frac{d_{ij}^2}{\sigma_{ij}^2}\right),
$$
then the inferred $D_{ij}$ are not distances in a single metric.  This can solve
the triangle problem, but it risks becoming a proxy knob unless the width ratios
are derived from flux or representation data.

## Extension B: multi-channel overlaps

If
$$
s_{ij}\sim\left|\sum_{\kappa} A_\kappa
\exp(-D_{ij,\kappa}^2)e^{i\phi_{ij,\kappa}}\right|,
$$
then the effective magnitude is not a single Gaussian distance.  This is natural
in stringy or resolved-intersection settings, but the allowed channels
$\kappa$ must be topologically enumerated.

## Extension C: non-Euclidean graph metric

A graph distance or ultrametric can differ from Euclidean pairwise distances.
However, any metric still satisfies the triangle inequality.  To solve the PMNS
deficit, the effective $D_{ij}$ must either fail to be a metric distance or
arise after channel-dependent transformations.

## Extension D: seesaw-induced mixing

PMNS mixing is not determined by charged-lepton localization alone.  It arises
from
$$
U_{\mathrm{PMNS}}=U_e^\dagger U_\nu,
$$
and the neutrino sector may involve
$$
m_\nu=-Y_\nu^T M_R^{-1}Y_\nu v_u^2.
$$

Therefore the PMNS targets need not correspond to a single three-point lepton
localization triangle.  The obstruction may indicate that neutrino seesaw
geometry, rather than charged-lepton geometry alone, is essential.

# No-proxy consequence

The simple quark graph can be used as a candidate target.  The lepton graph
cannot.

Therefore a successful no-proxy flavor closure must include at least one of:

- derived channel-dependent widths;

- derived multi-channel overlap sums;

- derived seesaw localization structure;

- a different mapping from PMNS angles to localization distances.

It may not simply assign independent distances to the three PMNS entries.

# Updated flavor-closure target

The no-proxy flavor closure problem should now be stated in two parts.

## Quark target

Find a small localization graph reproducing:
$$
(D_{12}^q,D_{23}^q,D_{13}^q)
\approx
(1.221,1.787,2.372),
$$
with finite holonomy character phase
$$
k_{12}=79\ \mathrm{mod}\ 448.
$$

## Lepton target

Find a charged-lepton plus neutrino/seesaw localization structure whose
effective PMNS output reproduces:
$$
(\theta_{12},\theta_{23},\theta_{13})
\approx
(33.4^\circ,46.8^\circ,8.6^\circ),
$$
without interpreting all three angles as direct single-channel Euclidean
pairwise overlaps.

# Conclusion

The first localization graph test gives a useful split result:

- CKM mixing magnitudes are compatible with the simplest Euclidean pairwise
  localization geometry.

- PMNS mixing magnitudes are not.

This is progress, not failure.  It prevents the no-proxy program from adopting
an over-simple flavor geometry and identifies the minimal places where real MTT
structure must enter: multi-channel overlap, flux-dependent widths, or seesaw
geometry.

The next calculation is therefore sharper:

> solve the quark localization triangle and build the lepton PMNS output from a
> charged-lepton plus neutrino/seesaw graph, rather than from a single lepton
> triangle.

