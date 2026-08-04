---
abstract: |
  We test the branch suggested by the color-singlet source of B_q.  If the
  hidden two-channel Schur completion already carries the color-redundancy
  multiplicity, then the breakdown coefficient should plausibly use the
  primitive lens-to-nil gap lambda_lens - lambda_nil rather than
  lambda_lens - 3 lambda_nil.  This produces a more CKM-shaped diagnostic when
  combined with the reversed adjacent-orientation branch.  The result is a
  refinement target, not a proof: MTT must still select the orientation and
  sector stiffnesses without using CKM data.
author:
- Peter Nero
date: June 2026
title: |
  Reduced Color-Gap Branch Diagnostic for the Quark B_q Operator
---

# Purpose

The previous B_q candidate used

```text
Lambda_q = lambda_lens - 3 lambda_nil.
```

That was a plausible color-counting target before the source of the `1/2`
coefficient was known.  The new color-singlet source changes the accounting:
the hidden two-channel Schur completion already implements the color-neutral
redundancy cost.

Therefore the cleaner primitive gap to test is

```text
Lambda_q = lambda_lens - lambda_nil.
```

# Accounting Principle

Use one color multiplicity mechanism only.

```text
Option A:
  color multiplicity in Lambda_q
  -> lambda_lens - 3 lambda_nil

Option B:
  color multiplicity in B_q Schur completion
  -> lambda_lens - lambda_nil
```

Once B_q contains the hidden two-channel completion coefficient, Option B is
more economical.  It avoids counting the same nil/color redundancy twice.

# Diagnostic Branches

The old branch is:

```text
mu_u = 8,
mu_d = 2,
Lambda_q = lambda_lens - 3 lambda_nil,
sigma = +1.
```

The reduced-gap, up-stiff branch is:

```text
mu_u = 8,
mu_d = 2,
Lambda_q = lambda_lens - lambda_nil,
sigma = -1.
```

The finite dictionary also contains an even closer diagnostic branch:

```text
mu_u = 2,
mu_d = 8,
Lambda_q = lambda_lens - lambda_nil,
sigma = -1.
```

That branch is not automatically preferred, because assigning the stronger
stiffness to the down sector may conflict with the expected up-sector mass
hierarchy.  It remains a diagnostic sibling until masses are computed from the
same source.

# Numerical Diagnostic

The check script compares the absolute mixing matrices against the observed CKM
magnitudes only as a diagnostic, not as an input to the construction.

It finds:

```text
old branch residual              about 0.018795
reduced-gap up-stiff residual    about 0.014322
best finite-dictionary residual  about 0.007946
```

Thus the color-source refinement improves the quark mixing shape, but it also
exposes that the exact finite branch is still not uniquely selected.

# Theorem Target

The next theorem should prove one of the following:

```text
Selected orientation theorem:
  sigma = -1 or sigma = +1 is forced by the selected nil/color retarded kernel.

Selected stiffness theorem:
  (mu_u, mu_d) is forced by the up/down closure-strain Hessian blocks.

Selected gap theorem:
  Lambda_q = lambda_lens - lambda_nil is forced because B_q already carries
  hidden color completion, or Lambda_q = lambda_lens - 3 lambda_nil is forced
  because color counting lives outside the Schur completion.
```

# What This Changes

This does not retire the previous B_q candidate.  It refines the search:

```text
the 1/2 coefficient is now sourced;
the reduced primitive color gap is now the cleaner candidate;
the orientation/stiffness branch remains open.
```

# Bottom Line

The strongest current no-proxy route is:

```text
first-order anchored bridge
+ color-singlet Schur completion B_q
+ reduced primitive lens-to-nil gap
+ selected retarded adjacent orientation
+ selected up/down Hessian stiffnesses.
```

The first two items are now supported/proved as schema.  The last three are the
remaining finite branch-selection problem.

