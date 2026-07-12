---
abstract: |
  The SU(5) qutrit basis-transport candidate gives exact nonzero CKM
  heavy-link numbers if MTT selects a relative qutrit Fourier transport between
  10_M and bar5_M.  This note audits whether that selector is already present
  in the proof package or local MTT corpus.  The answer is no: the ingredients
  are present separately, but the direct selection theorem is not found.  The
  candidate therefore remains conditional, and the next proof obligation is a
  selected zero-mode/monad/Galerkin theorem deriving the relative transport.
author:
- Peter Nero
date: May 2026
title: |
  SU(5) Qutrit Transport Selector Hunt
---

# Purpose

The heavy-link candidate has a precise conditional form:

```text
B_10=I_3,
B_bar5=F.
```

If selected, this gives:

```text
Delta_t = (1/sqrt(3), omega^2/sqrt(3)).
```

The remaining question is whether the corpus already proves that relative
transport.

# Source-Hunt Contract

The hunt excludes the newly generated SU(5) qutrit candidate and finite
transport-lemma files, then scans for a document containing all three kinds of
evidence:

```text
SU(5) / 10_M / bar5_M token,
qutrit / Fourier / clock-shift token,
basis-transport / sector-transport / selected-zero-mode token.
```

# Result

The ingredients are found separately:

```text
E6/SU(5) Yukawa split,
qutrit clock-shift and finite-Heisenberg machinery,
Fourier common-gauge guardrail,
selected zero-mode / monad / Galerkin route.
```

But the direct selector is not found:

```text
selected B_10/B_bar5 transport theorem = absent.
```

# Consequence

The candidate remains legitimate but conditional.

It is not:

```text
selected MTT data,
a computed C1 response,
a CKM-angle calculation,
full SM closure.
```

# Next Proof Obligation

The next source must be one of:

```text
typed monad/Cech cohomology that outputs sector bases for 10_M and bar5_M,
non-invariant spectral Galerkin zero modes that output the same relative F,
or a selected bundle/gerbe transition theorem forcing the qutrit Fourier split.
```

Until one of those is proved, the exact numbers are a strong candidate
direction rather than a closed prediction.
