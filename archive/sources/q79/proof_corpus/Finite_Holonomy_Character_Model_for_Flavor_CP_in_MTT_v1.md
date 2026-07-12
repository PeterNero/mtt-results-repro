---
abstract: |
  We replace the continuous benchmark CP phases of the complex holonomy flavor
  paper by characters of a finite cyclic holonomy group.  In the corrected
  complex benchmark, the quark phase $\delta_q\simeq1.10798$ reproduces
  $J_{\mathrm{CKM}}\simeq2.9\times10^{-5}$, while an illustrative leptonic
  phase $\delta_\ell=-\pi/2$ gives a nonzero PMNS Jarlskog invariant.  Here we
  show that both phases can be represented, to benchmark accuracy, by a single
  finite character system on $\mathbb Z_{448}$:
  $k_{12}=79$, $k_{23}=-112$, and $k_{31}=33$ modulo $448$.  The phase-sum rule
  is then exact, $k_{12}+k_{23}+k_{31}=0\pmod{448}$, and the resulting quark
  Jarlskog invariant is $2.899991\times10^{-5}$.  This does not yet derive the
  finite group from MTT topology, but it converts the continuous CP benchmark
  into a discrete holonomy-character target suitable for a no-proxy closure
  proof.
author:
- Peter Nero
date: May 2026
title: |
  A Finite Holonomy Character Model for Flavor CP in Modal Triplet Theory:
  Discretizing CKM and PMNS Phases under the Pairwise Phase-Sum Rule
---

# Purpose and scope

The complex holonomy benchmark introduced phases
$$
\delta_q=1.10798,\qquad \delta_\ell=-\frac{\pi}{2},
$$
and imposed the MTT phase-sum rule by defining
$$
\phi_{31}=-(\delta_q+\delta_\ell).
$$

That was a continuous benchmark.  The no-proxy closure program requires more:
the phases should arise from holonomy characters of the pairwise line bundles,
not from arbitrary real numbers.

This paper takes the next step.  It shows that the benchmark phases can be
encoded by a single finite cyclic character group with exact phase-sum closure.

We do not claim that $\mathbb Z_{448}$ is dynamically or topologically forced.
The result is a finite-character target:

> If MTT topology can force or naturally select this character system, then the
> benchmark CP phases become discrete holonomy data rather than continuous knobs.

# Character setup

Let the relevant holonomy quotient be modeled by a finite cyclic group
$$
\Gamma_{\mathrm{hol}}=\mathbb Z_N.
$$

A unitary character is specified by an integer $k\in\mathbb Z_N$:
$$
\rho_k(1)=\exp\!\left(\frac{2\pi i k}{N}\right).
$$

The associated phase is
$$
\phi_k=\frac{2\pi k}{N}.
$$

The MTT pairwise phase-sum rule becomes the character identity
$$
\rho_{12}\rho_{23}\rho_{31}=1,
$$
equivalently
$$
k_{12}+k_{23}+k_{31}=0\pmod N.
$$

# Finite character solution

Choose
$$
N=448.
$$

Assign the three pairwise character weights
$$
k_{12}=79,\qquad
k_{23}=-112,\qquad
k_{31}=33
\qquad(\mathrm{mod}\ 448).
$$

Then
$$
k_{12}+k_{23}+k_{31}
=
79-112+33
=0,
$$
so the phase-sum rule is exact.

The corresponding phases are
$$
\phi_{12}
=
\frac{2\pi\cdot79}{448}
\approx1.107972,
$$
$$
\phi_{23}
=
-\frac{2\pi\cdot112}{448}
=
-\frac{\pi}{2},
$$
and
$$
\phi_{31}
=
\frac{2\pi\cdot33}{448}
\approx0.462824.
$$

Thus $\phi_{12}$ approximates the target CKM phase
$\delta_q=1.10797857$ within $6.2\times10^{-6}$ radians, while
$\phi_{23}$ gives the illustrative PMNS phase exactly.

# CKM Jarlskog check

Using the corrected CKM benchmark angles
$$
s_{12}=0.2250,\qquad
s_{23}=0.0411,\qquad
s_{13}=0.0036,
$$
the Jarlskog invariant is
$$
J_{\mathrm{CKM}}
=
c_{12}c_{23}c_{13}^2s_{12}s_{23}s_{13}\sin\delta_q.
$$

Substituting the finite-character phase
$$
\delta_q=\frac{2\pi\cdot79}{448}
$$
gives
$$
J_{\mathrm{CKM}}
\approx
2.899991\times10^{-5}.
$$

This agrees with the target $2.9\times10^{-5}$ to better than
$10^{-10}$ in absolute value.

# PMNS phase check

The lepton character
$$
k_{23}=-112
$$
gives
$$
\delta_\ell=-\frac{\pi}{2}
$$
exactly because $448$ is divisible by $4$.

For the benchmark PMNS angles
$$
\theta_{12}=33.4^\circ,\qquad
\theta_{23}=46.8^\circ,\qquad
\theta_{13}=8.6^\circ,
$$
this yields
$$
J_{\mathrm{PMNS}}\approx-3.35\times10^{-2}.
$$

This is an illustrative leptonic CP benchmark, not a precision global-fit
claim.

# Why $448$?

The choice $N=448$ is not asserted to be fundamental.  It is a compact finite
cyclic order with three useful properties:

1.  it is divisible by $4$, so $\delta_\ell=-\pi/2$ is exact;

2.  it approximates the CKM phase target with very small error using
    $k_{12}=79$;

3.  the compensating character $k_{31}=33$ is then fixed by the phase-sum rule.

Smaller choices are possible with lower precision.  For example, $N=68$ with
$k_{12}=12$ already gives $J_{\mathrm{CKM}}\approx2.90118\times10^{-5}$, but it
does not make $-\pi/2$ exact because it is not divisible by $4$.  The order
$448$ is therefore a convenient finite benchmark, not a uniqueness claim.

# Relation to no-proxy closure

This paper improves the status of the CP benchmark:

- the phases are no longer arbitrary real numbers;

- the phase-sum rule is exact at the character level;

- CKM CP violation is reproduced with finite discrete data.

However, no-proxy closure still requires deriving the character group and
weights from upstream MTT data.  In particular, a complete closure proof must
show that:

1.  the relevant pairwise line-bundle holonomy quotient is $\mathbb Z_{448}$ or
    an equivalent character group;

2.  the weights $(79,-112,33)$ are selected by topology, admissibility, or
    localization, not by fitting;

3.  the same character data also enter the allowed Yukawa overlap channels;

4.  the resulting CKM and PMNS phases cannot be varied independently.

# Pass-forward target theorem

The desired future theorem has the following form.

#### Target theorem

Assume the MTT pairwise line-bundle system on the chosen Tier-4 corner has
holonomy quotient $\Gamma_{\mathrm{hol}}\cong\mathbb Z_{448}$, and assume the
allowed family localization graph selects the character weights
$$
(k_{12},k_{23},k_{31})=(79,-112,33).
$$
Then the CKM and PMNS benchmark phases are generated by finite holonomy
characters satisfying the MTT phase-sum rule, with
$$
J_{\mathrm{CKM}}\approx2.9\times10^{-5}
$$
and an illustrative leptonic phase $\delta_\ell=-\pi/2$.

The work still needed is to prove the assumptions of this target theorem.

# Conclusion

The complex holonomy benchmark showed that realistic CP violation can be
represented while respecting the phase-sum rule.  The present paper discretizes
that benchmark: a single finite cyclic character system on $\mathbb Z_{448}$
reproduces the CKM CP invariant to benchmark precision, gives an exact
$-\pi/2$ leptonic phase, and satisfies the pairwise phase-sum identity exactly.

This is progress toward no-proxy closure, but not closure itself.  The next
problem is now sharply defined:

> derive the finite holonomy quotient and character weights from the pairwise
> line-bundle topology and localization graph of the Tier-4 corner.

