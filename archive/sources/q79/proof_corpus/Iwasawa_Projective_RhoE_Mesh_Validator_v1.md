---
abstract: |
  We add an executable projective finite-mesh rho_E validator.  Unlike the
  ordinary rho_E mesh validator, it accepts corner products that agree up to a
  scalar central unit phase.  This is the finite contract needed for
  twisted-bundle, gerbe, B-field, discrete-torsion, and magnetic-translation
  candidates.  The qutrit clock-shift carrier passes with 274 strict mismatches
  but zero projective mismatches and 274 nontrivial central twists.  The
  pure-gauge nonabelian carrier passes only as a trivial projective case with no
  central twist.  A deliberately noncentral corrupted candidate fails.
author:
- Peter Nero
date: May 2026
title: |
  Iwasawa Projective rho_E Mesh Validator
---

# Purpose

The projective magnetic carrier showed:

```text
ordinary vector-bundle corner products fail,
but every failure is a scalar central phase.
```

That behavior should not live only inside one constructor script.  We need a
general validator for future twisted candidates.

# Validator

The executable validator is:

```text
scripts/validate_iwasawa_projective_rhoE_mesh.py
```

It consumes the same finite boundary-target table format as:

```text
scripts/validate_iwasawa_rhoE_mesh.py.
```

But the corner law is weakened from strict equality:

```text
product(path_2) = product(path_1)
```

to projective equality:

```text
product(path_2) product(path_1)^(-1) = lambda I,
|lambda| = 1.
```

# Audit Cases

The qutrit magnetic-translation carrier passes:

```text
strict mismatch count = 274,
projective mismatch count = 0,
nontrivial central twist count = 274.
```

The pure-gauge nonabelian carrier also passes, but only trivially:

```text
strict mismatch count = 0,
projective mismatch count = 0,
nontrivial central twist count = 0.
```

A deliberately noncentral corrupted candidate fails the projective validator.

# Interpretation

This validator separates three cases:

```text
1. strict ordinary vector-bundle data,
2. genuine projective/twisted data,
3. invalid noncentral corner data.
```

The projective magnetic carrier is in case 2.

# Guardrail

Passing this validator does not prove that a twist is selected by MTT.

The missing selected data are still:

```text
selected gerbe class,
selected B-field or discrete torsion,
twisted Bianchi/Freed-Witten compatibility,
twisted sector projectors,
twisted D_E and dotD response.
```

# Correct Next Step

Now the next search is well-posed:

```text
find selected twist data in the corpus,
or formulate a twisted-source promotion gate,
or convert the central twist into selected D_E/dotD response data.
```

The important advance is that the projective route is now executable and
auditable, while still blocked from overclaiming selected SM closure.
