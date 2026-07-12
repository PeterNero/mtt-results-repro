---
abstract: |
  The selected finite B_q branch fixes a CKM-shaped quark mixing packet, and
  the weighted right-eigenchannel theorem identifies the only algebraic place
  where an additional mass hierarchy can enter without spoiling that CKM
  packet.  This note extracts the allowed no-proxy source classes for those
  right-channel actions from the corpus and tests simple structural constants.
  The result is not yet a mass proof: it narrows the remaining problem to a
  finite geometric source calculation for the actions A_{x,a}.
author:
- Peter Nero
date: June 2026
title: |
  Weighted Right-Eigenchannel Action Source Candidates for No-Proxy Mass Closure
---

# Purpose

The selected finite B_q branch gives the correct CKM-shaped left geometry but
quark singular values that are too shallow.

The right-eigenchannel theorem shows that an extra positive action layer can
change the singular values while preserving CKM only if it acts in the
canonically weighted right singular basis:

```text
Z_x = Y_x G_A^{-1/2} = U_x S_x V_x^*,
Z_x' = U_x S_x P_x V_x^*,
P_x = diag(exp(-A_{x,1}), exp(-A_{x,2}), 1).
```

The remaining source problem is therefore:

```text
derive A_{x,a} from selected MTT geometry, not from observed quark masses.
```

# Required Numbers

The current selected B_q packet requires:

```text
A_u = (4.480058, 4.615899, 0),
A_d = (1.158678, 1.526516, 0).
```

Equivalently:

```text
mean(A_u light modes) = 4.547979,
mean(A_d light modes) = 1.342597,

split(A_u) = (-0.067920, +0.067920),
split(A_d) = (-0.183919, +0.183919).
```

Thus the source has two jobs:

```text
1. produce sector-scale actions of order q_u^2 and q_d^2;
2. produce smaller family/eigenchannel splittings without changing U_u or U_d.
```

# Corpus-Supported Source Candidate Classes

The corpus supports the following no-proxy mechanisms.

```text
1. localized zero-mode overlap actions;
2. holomorphic or instanton prefactors attached to allowed exceptional classes;
3. right-singlet line-bundle action costs;
4. Higgs-overlap normalization diagonal after the selected right projection;
5. nil-survivor finite-width corrections after the retarded left projection;
6. common bottleneck data: G_loc, line bundles, holonomy characters, widths W,
   and a finite allowed set I of instanton or exceptional classes.
```

The corpus rejects the following as proof sources:

```text
1. entry-wise Yukawa fitting;
2. independent sector-local retuning;
3. observed masses or CKM entries used as inputs;
4. arbitrary family-basis diagonal prefactors.
```

# First Structural Constant Test

The hypercharge-square stiffness theorem selected topology-only sector
numerators:

```text
q_u = 2,
q_d = 1.
```

A natural zero-mode normalization primitive is a Gaussian or overlap
normalization constant.  The simplest dimensionless candidate is:

```text
A_{x,a}^{(0)} = q_x^2 log(pi).
```

This gives:

```text
up base   = 4 log(pi) = 4.578920,
down base = 1 log(pi) = 1.144730.
```

Residuals against the required right-channel actions are:

```text
A_u - 4 log(pi) = (-0.098861, +0.036979),
A_d - 1 log(pi) = (+0.013949, +0.381786).
```

This is useful but not sufficient.  It suggests a plausible base measure
factor, especially for the up mean and the first down channel, but it does not
derive the family/eigenchannel splittings and it leaves the second down channel
too high.  Therefore `q_x^2 log(pi)` is a candidate primitive, not a closure.

# Correct Next Source Form

The mass action should be sought in the form:

```text
A_{x,a} =
  q_x^2 A_0
  + Delta_{x,a}^{width}
  + Delta_{x,a}^{inst}
  + Delta_{x,a}^{H}
  + Delta_{x,a}^{nil},
```

where:

```text
A_0
  is a common zero-mode or measure normalization action;

Delta_{x,a}^{width}
  is selected by localized wavefunction widths from the common G_loc data;

Delta_{x,a}^{inst}
  is selected by the finite allowed instanton/exceptional class set I;

Delta_{x,a}^{H}
  is selected by Higgs-overlap normalization;

Delta_{x,a}^{nil}
  is selected by nil-survivor finite-width correction after retarded
  projection.
```

Each correction must be diagonal in the selected weighted right eigenchannel
basis, or must become diagonal there after the selected projection.

# Selection Test for a Proposed Source

A proposed source is admissible only if it passes all checks:

```text
1. It is computed from the same selected MTT branch as q=79 and B_q.
2. It supplies A_u=(4.480058,4.615899,0) and
   A_d=(1.158678,1.526516,0) within the chosen precision.
3. It acts in the weighted right eigenchannels of Z_x=Y_x G_A^{-1/2}.
4. It preserves the selected left CKM matrix.
5. It uses no observed quark masses, CKM entries, or entry-wise Yukawa fits.
6. It uses common bottleneck data rather than independent sector-local knobs.
```

# What This Closes

```text
allowed source classes extracted from corpus          EXTRACTED
required right-channel action values imported         CHECKED
simple Gaussian log(pi) primitive tested              DIAGNOSTIC
mass-source proof status                              OPEN
```

# Bottom Line

We have not yet proved the quark masses.  We have made the last missing object
much sharper:

```text
SelectedMassActionSource:
  a no-proxy geometric source that produces the four light-mode actions
  in the weighted right singular channels.
```

The best next calculation is to compute the right-channel zero-mode/instanton
action operator from the same selected local packet and compare its two light
eigenvalues in each sector with the four required actions above.
