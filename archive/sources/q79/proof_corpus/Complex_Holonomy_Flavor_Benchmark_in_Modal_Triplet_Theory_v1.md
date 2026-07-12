---
abstract: |
  We extend the corrected real Tier-4 flavor benchmark of Modal Triplet Theory
  (MTT) to a complex holonomy benchmark with nonzero CP violation.  The previous
  benchmark reproduced quark and lepton mixing magnitudes but, being real, had
  vanishing Jarlskog invariant.  Here we introduce a minimal complex holonomy
  phase assignment satisfying the MTT phase-sum bookkeeping constraint and show
  that the quark CKM phase can reproduce $J_{\mathrm{CKM}}\simeq2.9\times10^{-5}$
  without altering the calibrated gauge or gravitational data.  We also provide
  a corresponding complex PMNS benchmark with a leptonic Dirac phase, while
  emphasizing that this remains a reproducible complex benchmark rather than a
  no-proxy derivation.  The result supplies the next execution layer needed for
  the no-proxy flavor-closure test: CP violation is now represented explicitly,
  but must still be derived from shared holonomy/localization bottleneck data.
author:
- Peter Nero
date: May 2026
title: |
  Complex Holonomy Flavor Benchmark in Modal Triplet Theory:
  CKM CP Violation, PMNS Phases, and the Phase-Sum Constraint
---

# Purpose and scope

The corrected Tier-4 flavor benchmark printed real Yukawa matrices.  Those
matrices reproduce mass and mixing magnitudes but necessarily have zero CP
violation.  The no-proxy closure paper then identified the next required step:
complex phases must be introduced through holonomy data, not through independent
entry-wise fitting.

This paper performs the minimal complex benchmark step.  It does not yet prove
no-proxy flavor closure.  It shows that the benchmark can be extended to complex
matrices with realistic CKM CP violation while keeping the phase bookkeeping
compatible with the MTT line-bundle phase sum rule.

# Holonomy phase bookkeeping

The topology-only MTT layer gives the canonical trivialization
$$
L_{12}\otimes L_{23}\otimes L_{31}\cong\mathbb C,
$$
and therefore the holonomy phase constraint
$$
\phi_{12}+\phi_{23}+\phi_{31}\in 2\pi\mathbb Z.
$$

For the benchmark we choose three holonomy phases
$$
\phi_{12}=\delta_q,\qquad
\phi_{23}=\delta_\ell,\qquad
\phi_{31}=-(\delta_q+\delta_\ell),
$$
so the sum rule is exactly satisfied.

The quark phase $\delta_q$ is used in the CKM benchmark.  The lepton phase
$\delta_\ell$ is used in the PMNS benchmark.  The compensating phase
$\phi_{31}$ is not an independent fit parameter; it is fixed by the sum rule.

# CKM benchmark with nonzero Jarlskog invariant

We use the standard three-angle, one-phase parameterization
$$
V_{\mathrm{CKM}}
=
\begin{pmatrix}
c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta_q}\\
-s_{12}c_{23}-c_{12}s_{23}s_{13}e^{i\delta_q}
&
c_{12}c_{23}-s_{12}s_{23}s_{13}e^{i\delta_q}
&
s_{23}c_{13}\\
s_{12}s_{23}-c_{12}c_{23}s_{13}e^{i\delta_q}
&
-c_{12}s_{23}-s_{12}c_{23}s_{13}e^{i\delta_q}
&
c_{23}c_{13}
\end{pmatrix}.
$$

The real benchmark magnitudes are retained:
$$
s_{12}=0.2250,\qquad
s_{23}=0.0411,\qquad
s_{13}=0.0036.
$$

The Jarlskog invariant is
$$
J_{\mathrm{CKM}}
=
c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta_q.
$$

Choosing
$$
\delta_q=1.10798\ \mathrm{rad}
$$
gives
$$
J_{\mathrm{CKM}}\simeq2.90\times10^{-5}.
$$

The corresponding CKM magnitudes are
$$
|V_{\mathrm{CKM}}|
\simeq
\begin{pmatrix}
0.9743 & 0.2250 & 0.0036\\
0.2249 & 0.9735 & 0.0411\\
0.0083 & 0.0404 & 0.9991
\end{pmatrix}.
$$

These are consistent with the intended high-scale benchmark accuracy.

# Complex Yukawa realization

As in the real benchmark, choose a basis in which the up-type Yukawa matrix is
diagonal:
$$
Y_u=\mathrm{diag}(1.2\times10^{-5},\,1.6\times10^{-3},\,0.53).
$$

Let
$$
D_d=\mathrm{diag}(2.2\times10^{-4},\,5.5\times10^{-3},\,0.11).
$$

Define
$$
Y_d=V_{\mathrm{CKM}}D_d.
$$

Then
$$
Y_dY_d^\dagger
=
V_{\mathrm{CKM}}D_d^2V_{\mathrm{CKM}}^\dagger,
$$
so the left diagonalization of $Y_d$ reproduces the benchmark CKM matrix.  No
entry-wise matrix tuning is performed after the phase and singular values are
chosen.

#### Remark

This is still a benchmark construction.  No-proxy closure requires deriving
$D_d$, the three angles, and $\delta_q$ from the shared bottleneck data rather
than selecting them as phenomenological targets.

# PMNS complex benchmark

For the lepton sector we use the same standard parameterization with angles
$$
\theta_{12}=33.4^\circ,\qquad
\theta_{23}=46.8^\circ,\qquad
\theta_{13}=8.6^\circ.
$$

As a representative complex benchmark, choose
$$
\delta_\ell=-\frac{\pi}{2}.
$$

This gives
$$
|U_{\mathrm{PMNS}}|
\simeq
\begin{pmatrix}
0.825 & 0.544 & 0.150\\
0.388 & 0.575 & 0.721\\
0.410 & 0.611 & 0.677
\end{pmatrix},
$$
and the leptonic Jarlskog invariant
$$
J_{\mathrm{PMNS}}\simeq -3.35\times10^{-2}.
$$

This matrix is within the intended illustrative range for PMNS magnitudes.  A
precision lepton-sector fit requires current global-fit inputs, matter of
convention for Majorana phases, and RGE treatment of the high-scale benchmark.

# Phase-sum closure

With
$$
\delta_q=1.10798,\qquad
\delta_\ell=-\frac{\pi}{2},
$$
the compensating holonomy phase is
$$
\phi_{31}
=
-(\delta_q+\delta_\ell)
\approx
0.46282.
$$

Therefore
$$
\phi_{12}+\phi_{23}+\phi_{31}=0
\quad(\mathrm{mod}\ 2\pi).
$$

This demonstrates that the complex CKM and PMNS benchmark phases can be embedded
in a phase-sum-compatible holonomy assignment.

# What is and is not achieved

This paper achieves:

- a nonzero CKM Jarlskog invariant in the MTT flavor benchmark;

- a complex PMNS benchmark with a leptonic Dirac phase;

- explicit phase-sum-rule bookkeeping;

- a reproducible script-level benchmark.

This paper does not yet achieve:

- derivation of $\delta_q$ from topology;

- derivation of $\delta_\ell$ from topology;

- derivation of the compensating phase from a concrete line-bundle connection;

- no-proxy closure of flavor;

- prediction of Majorana phases.

# Pass-forward requirement

The next no-proxy calculation must replace the selected phases
$$
\delta_q,\quad \delta_\ell,\quad \phi_{31}
$$
by holonomy characters of the pairwise line bundles:
$$
\rho_{ij}:\pi_1(Y_4)\to U(1),
$$
with
$$
\rho_{12}\rho_{23}\rho_{31}=1.
$$

Only then can CP violation be claimed as derived rather than benchmarked.

# Conclusion

The corrected real flavor benchmark established reproducible mass and mixing
magnitudes but had no CP violation.  This paper supplies the next execution
layer: a complex holonomy-compatible benchmark with realistic CKM CP violation
and an illustrative leptonic CP phase.

The result strengthens the execution program, but it also sharpens the remaining
test.  The phases are now explicit, so the no-proxy closure problem becomes
concrete:

> derive $\delta_q$, $\delta_\ell$, and the compensating phase from the shared
> pairwise line-bundle holonomy data, or concede that CP remains an unresolved
> bottleneck.

