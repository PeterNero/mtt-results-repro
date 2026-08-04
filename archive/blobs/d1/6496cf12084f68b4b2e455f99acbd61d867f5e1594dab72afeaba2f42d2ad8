---
abstract: |
  We formulate the selected channel-weight extraction protocol for the
  rank-one Yukawa lift.  The q79 branch, Theta scaffold, Iwasawa rank-one
  seed, finite channel sets, and q79 channel restriction now leave a finite
  list of 28 possible overlap channels.  This note defines exactly what
  counts as a no-proxy weight for those channels: each coefficient must be a
  selected zero-mode overlap prefactor A_gamma times an action factor
  exp(-S_gamma) times the allowed finite character chi_gamma.  It also records
  what is forbidden: Execution II benchmark entries, observed masses, observed
  mixing angles, empirical Gaussian distances, and post-hoc phases.  The
  protocol closes the ambiguity of what must be computed, but it does not yet
  compute the numerical A_gamma, S_gamma, kinetic metrics, corrected Yukawa
  matrices, or RG matching.
author:
- Peter Nero
date: May 2026
title: |
  Selected Channel-Weight Extraction Protocol for the Rank-One Lift
---

# Purpose

The hard-leap blocker has been reduced to selected coefficients:

```text
A_gamma,
S_gamma,
C6 orientation/nonzero status,
family kinetic metrics,
RG and threshold matching.
```

The danger at this stage is subtle.  The old Execution II matrices are useful
benchmarks, but if their entries are copied into the proof as coefficients,
the program becomes proxy fitting again.  The next artifact therefore has to
say exactly what is allowed to count as a selected channel weight.

# Fixed Inputs

The current proof ladder supplies:

```text
Theta scaffold:
  mu_Theta = 5 TeV,
  I2/I1 = 0.560,
  I3/I1 = 0.229,
  c = 1.439 R1,
  (f2 R_lens)^2 = 0.280 R1.

Iwasawa seed:
  lambda_123 = 1,
  tree-level E6 27^3 Yukawa has rank one.

Finite channel sets:
  Gamma_u, Gamma_d, Gamma_e, Gamma_nuD,
  seven source classes per sector.

q79 restriction:
  C6 channels may carry labels {79,369},
  non-C6 channels carry label {0}.
```

Thus the coefficient problem is finite.  There are four sectors and seven
channel types per sector:

```text
4 x 7 = 28 channel slots.
```

The kinetic-metric source `C5` remains outside the channel sets because it is
not a Yukawa overlap insertion.  It is part of canonical normalization.

# Weight Formula

For a sector

```text
s in {u,d,e,nuD}
```

and an allowed channel

```text
gamma in Gamma_s,
```

the selected channel weight must have the form:

```text
W_{s,gamma,ij}(Theta)
  = A_{s,gamma,ij}(Theta)
    exp(-S_{s,gamma}(Theta))
    chi_{s,gamma}(Theta).
```

Here:

```text
A_{s,gamma,ij}
  selected L2-normalized triple-overlap prefactor, including the sector's
  E6/SM tensor contraction and the selected channel insertion O_gamma;

S_{s,gamma}
  selected action, distance, spectral, flux, or closure-strain cost;

chi_{s,gamma}
  selected finite character, restricted by the q79 channel rule.
```

The raw Yukawa matrix is then:

```text
Y_s^raw(Theta)
  = y0_s E33
    + sum_{gamma in Gamma_s minus C0} W_{s,gamma}(Theta).
```

The tree seed `C0` is the Iwasawa-normalized rank-one piece:

```text
lambda_123 = 1,
S_C0 = 0,
chi_C0 = 1,
matrix representative = E33 after family relabeling.
```

Low-energy sector prefactors for that seed remain part of Higgs embedding,
kinetic normalization, threshold, and RG matching.  The protocol does not
claim a final top, bottom, tau, or neutrino Yukawa value from `lambda_123`
alone.

# Character Filter

The finite character factor is not adjustable:

```text
chi_{s,gamma} =
  exp(2 pi i 79/448)   or exp(2 pi i 369/448),  gamma is C6,
  1,                                                     otherwise.
```

The orientation choice between `79` and `369`, and the question whether the
C6 coefficient is zero or nonzero in a given sector, remain open.

# Allowed Sources of A_gamma

The prefactor `A_gamma` may only be computed from selected internal data:

```text
selected family zero modes,
selected Higgs zero mode,
selected E6/SM tensor contraction,
selected channel insertion O_gamma,
selected Theta geometry,
selected bundle/flux data,
selected L2 normalization.
```

Equivalently, an admissible representative has the schematic form:

```text
A_{s,gamma,ij}
  = integral_X
      Omega wedge Tr(
        Psi_{L,i}^{(s)}
        wedge O_gamma(Theta)
        wedge Psi_{R,j}^{(s)}
        wedge H_s
      )
```

with the precise wedge/contraction convention fixed by the sector and the
E6-to-SM dictionary.

# Allowed Sources of S_gamma

The action/cost `S_gamma` must be read from the selected source class:

```text
C0: tree seed, S=0.
C1: alpha-prime/curvature order and selected curvature functional.
C2: instanton or nonperturbative action.
C3: repaired flux-quantized Lens-Nil deformation cost.
C4: retained non-invariant spectral cost.
C6: pure flat q79 holonomy has no extra real action unless paired with another
    geometric insertion.
C7: closure-strain basin cost.
```

This is deliberately stricter than the benchmark.  A Gaussian distance may be
used only if it is derived as a local limit of one of these selected costs.

# Forbidden Inputs

The following are not allowed to define `A_gamma`, `S_gamma`, or
`chi_gamma`:

```text
Execution II benchmark matrix entries,
observed fermion masses,
observed CKM angle magnitudes,
observed PMNS angle magnitudes,
empirical Gaussian distances chosen after comparison,
entry-wise phases outside the q79 restriction rule,
post-hoc threshold choices fitted to flavor output.
```

These data may be used only after the selected overlap certificate is frozen,
as comparison targets.

# Canonical Normalization

The raw matrices are not physical observables until the family kinetic metrics
are computed.  If:

```text
K_{L,s}, K_{R,s}
```

are the selected post-breaking L2 kinetic matrices for the left and right
zero modes in sector `s`, then:

```text
Y_s^can
  = K_{L,s}^{-1/2} Y_s^raw K_{R,s}^{-1/2}.
```

Only after this step can singular values and mixing matrices be computed.

# Theorem

#### No-Proxy Weight Extraction Theorem

Given the current Theta/q79/Iwasawa branch, the finite channel sets, and the
q79 channel restriction, a rank-one lift coefficient is admissible as a
no-proxy MTT coefficient only if it is produced by:

```text
W_{s,gamma,ij}
  = A_{s,gamma,ij}(Theta)
    exp(-S_{s,gamma}(Theta))
    chi_{s,gamma}(Theta)
```

with `gamma` in the finite channel set for sector `s`, `A_gamma` and
`S_gamma` evaluated from selected geometry/bundle/flux/zero-mode data, and
`chi_gamma` obeying the q79 support rule.

Benchmark matrix entries and observed mass/mixing data are forbidden as
coefficient sources.

#### Proof

The finite channel-set certificate supplies exactly seven allowed source
classes in each of four sectors.  The q79 restriction certificate supplies the
finite character support: C6 carries only `79` or `369`, and every non-C6
source is character-trivial.  The Iwasawa seed supplies the unique normalized
tree rank-one term with `lambda_123=1`.  The Theta scaffold fixes the scale,
overlap ratios, direct lens/nil normalizations, and gap regime before flavor
comparison.

Therefore any admissible rank-one lift correction must be one of the finite
channel slots and must be evaluated from the selected branch data attached to
that slot.  Adding a matrix entry, distance, phase, or threshold after looking
at the observed flavor data is not a selected channel evaluation.  It is a
proxy input.  The stated formula is therefore the necessary no-proxy
extraction protocol.

# What This Closes

This closes:

```text
finite coefficient domain,
weight formula,
C0 tree seed normalization functional,
q79 character filter,
no-proxy input filter.
```

# What Remains Open

This does not close:

```text
numerical A_gamma values,
numerical S_gamma values,
C6 orientation signs,
C6 nonzero status,
family kinetic metrics,
DeltaY matrices,
canonical Yukawa matrices,
RG and threshold matching.
```

# Bottom Line

The next hard calculation is now unambiguous:

```text
evaluate the listed A_gamma and S_gamma functionals
on the selected Theta/q79/Iwasawa branch.
```

That is where actual no-proxy mass and CKM-angle closure either happens or
fails.
