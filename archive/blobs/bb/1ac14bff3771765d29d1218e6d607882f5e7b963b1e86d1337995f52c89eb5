---
abstract: |
  We formulate the remaining CKM numerator problem as a finite admissibility
  filter on the selected order-448 CP character.  The corpus already supports
  the ingredients needed for this formulation: Yukawa entries are overlap
  integrals of localized coherent modes; central-circle phases contribute to
  CP violation; the proto-spinor bridge represents nil as discrete survivor
  selection; and the delta/projection program treats exact selection as the
  sharp limit of a finite admissibility filter.  Applying these rules to the
  admissible label set in Z_448, the oriented CKM overlap target selects
  q=79 uniquely.  The result is not yet a final derivation, because the target
  phase is still imported from the CKM/Jarlskog benchmark.  It is a precise
  theorem gate: if the MTT overlap kernel computes an oriented CKM phase in
  the stated stability window, the finite survivor label is forced to be 79.
author:
- Peter Nero
date: May 2026
title: |
  Overlap Admissibility Filter for the CKM Label 79
---

# Purpose

The previous label-normalization note showed that the selected order-448
character fixes the denominator but not the numerator.  There are many
primitive labels in `Z_448`, even after imposing the lepton quarter-turn and
phase-sum closure.

This paper gives the correct next mathematical form of the missing theorem.
The numerator should not be derived from cyclic group algebra alone.  It should
be derived as the survivor of an admissibility filter built from the MTT
overlap kernel.

# Corpus support

The broader corpus supports four ingredients.

First, the flavor execution paper writes Yukawa couplings as localized
wavefunction overlap integrals with discrete charges and holonomy phases.

Second, the central-circle paper states that Yukawa phases and CP-violating
relative phases are controlled by the shared central-circle sector, while the
circle also imposes finite holonomy selection rules.

Third, the proto-spinor/worldsheet bridge identifies the nil role with
discrete survivor selection.  Locally this is represented by a basin potential
around an admissible survivor label.

Fourth, the delta/projection papers show that a hard selection rule is the
zero-width limit of a finite admissibility filter

```text
K_epsilon = exp(-J_adm/epsilon^2).
```

So the right object is a finite filter over admissible CP labels, not another
topology-only assertion.

# Admissible label set

Work in the selected CP quotient

```text
Z_448.
```

The exact constraints are:

```text
l = 336,
ord(l)=4,
q+l+r=0 mod 448,
ord(q)=448,
ord(r)=448.
```

Thus

```text
r = -(q+336) mod 448.
```

Let `A_448` be the set of labels satisfying these constraints.  It has

```text
192
```

elements.

# Oriented overlap target

Let the MTT overlap kernel compute an oriented CKM phase

```text
delta_MTT in (0,pi)
```

from a selected overlap formula of the schematic form

```text
Y_abc(Theta)=sum_gamma A_gamma exp(-S_gamma) chi_gamma.
```

The observed benchmark currently gives

```text
delta_0 = asin(J_CKM/(c12 c23 c13^2 s12 s23 s13))
        = 1.107978573420...
```

using

```text
s12=0.2250, s23=0.0411, s13=0.0036, J_CKM=2.9e-5.
```

This is not yet an MTT derivation.  It is the empirical target that the future
overlap computation must reproduce.

# Selection functional

For each admissible label `q`, define

```text
delta(q)=2pi q/448.
```

On the oriented CKM branch, use the cost

```text
E(q;delta_MTT)=dist_branch(delta(q),delta_MTT)^2.
```

Then the admissibility filter is

```text
K_epsilon(q)
= 1_{q in A_448} exp(-E(q;delta_MTT)/epsilon^2).
```

In the sharp limit `epsilon -> 0`, the survivor is the admissible label with
minimum cost.

# Computed survivor for the CKM target

The check script

```text
overlap_admissibility_filter_q79_check.py
```

finds:

```text
selected q = 79
l = 336
r = 33
delta(79) = 1.107972409079
phase error = 6.164e-06
```

The nearest admissible competitor on the oriented branch is

```text
q = 81,
delta(81) = 1.136022343486.
```

The target is separated from the decision boundary by approximately

```text
0.014018 rad.
```

Therefore the selection is stable: any MTT overlap calculation whose oriented
phase lands in the interval

```text
1.079922474671 < delta_MTT < 1.121997376282
```

selects `q=79` over the nearest admissible competitors.

# Theorem gate

#### Conditional theorem

Assume:

1.  the selected CP quotient is the order-448 character already constructed;

2.  the physical lepton branch is the quarter-turn label `l=336`;

3.  pairwise phase-sum closure is imposed;

4.  CKM labels and phase-sum partners must be primitive in `Z_448`;

5.  the selected MTT overlap kernel computes an oriented CKM phase
    `delta_MTT` in the stability interval above.

Then the sharp admissibility-filter survivor is uniquely

```text
q=79, l=336, r=33.
```

#### Proof

The first four assumptions define the finite admissible set `A_448`.
The filter is positive exactly on `A_448` and exponentially suppresses labels
by squared branch distance from `delta_MTT`.  As `epsilon -> 0`, the survivor is
the unique minimizer of that distance.  Direct enumeration of `A_448` shows
that the Voronoi cell of `q=79` on the oriented branch contains the stated
interval.  Hence every `delta_MTT` in the interval has unique minimizer
`q=79`.  The phase-sum partner is then forced:

```text
r=-(79+336)=33 mod 448.
```

# What this achieves

This is real progress, but it must be stated carefully.

It proves that once the finite quotient and branch orientation are fixed, the
specific numerator `79` follows from a continuous overlap phase with a generous
stability margin of about `1.4e-2` radians.

It does not yet prove that MTT computes that phase.  The remaining work is to
evaluate the selected overlap kernel from the shared-circle, localization,
flux, Mukai/Fu-Yau, and nil-survivor data.

# Correct next task

The next calculation should derive `delta_MTT` from actual overlap data:

```text
delta_MTT = arg sum_gamma A_gamma exp(-S_gamma) chi_gamma.
```

The proof succeeds if this value lands in the stability interval above without
entry-local phase tuning.

The proof fails, or must be revised, if the selected MTT overlap kernel lands
outside that interval or requires an arbitrary phase knob to enter it.

# Gate status

```text
finite order-448 CP character available                  PASS
admissible primitive label set defined                   PASS
finite filter selects q=79 from CKM overlap target       PASS
selection stable under 0.014 rad target perturbations    PASS
MTT derives target phase from overlap kernel             OPEN
no entry-local phase tuning                              OPEN
```

# Bottom line

The `q=79` problem is now sharply localized.

Topology gives the grid.  The admissibility filter gives the selection rule.
The remaining proof obligation is to compute the oriented CKM overlap phase
from MTT geometry and show it falls in the `q=79` survivor cell.
