---
abstract: |
  The mass-action source theory battery found a compact finite-label
  approximation to the four missing weighted right-eigenchannel actions.  After
  the common Gaussian zero-mode base q_x^2 log(pi), the residuals are closely
  matched by selected MTT scales: the up-sector split is (-3/2 J,+1/2 J), with
  J=lambda_nil/lambda_lens; the down-sector split is (1/64,3/2 lambda_nil).
  This candidate preserves CKM by acting in the weighted right singular basis
  and reproduces the target mass ratios to small log error.  It is not yet a
  proof: the finite labels must still be derived from the selected
  theta/lens/nil/right-channel source operator.
author:
- Peter Nero
date: June 2026
title: |
  Finite-Label Right-Channel Mass Operator Candidate
---

# Purpose

The battery found that the missing mass actions have a compact finite-label
fingerprint when measured against the Gaussian zero-mode base:

```text
A_{x,a}^{base} = q_x^2 log(pi).
```

Use:

```text
J = lambda_nil/lambda_lens,
lambda_nil = 0.25,
lambda_lens = 3.57.
```

Then define the finite right-channel residual operator:

```text
eig(R_u) = (-3/2 J, +1/2 J, 0),
eig(R_d) = (1/64, +3/2 lambda_nil, 0).
```

The candidate mass actions are:

```text
A_u^cand = 4 log(pi) + (-3/2 J, +1/2 J, 0),
A_d^cand = 1 log(pi) + (1/64, +3/2 lambda_nil, 0).
```

# Numerical Values

This gives:

```text
A_u^cand = (4.473878, 4.613934, 0),
A_d^cand = (1.160355, 1.519730, 0).
```

The required actions are:

```text
A_u^req = (4.480058, 4.615899, 0),
A_d^req = (1.158678, 1.526516, 0).
```

So the action residuals are:

```text
Delta A_u = (-0.006180, -0.001965),
Delta A_d = (+0.001677, -0.006786).
```

# Interpretation

The labels are suggestive:

```text
-3/2 J, +1/2 J
```

look like a retarded right-channel split using the already selected
anchor ratio:

```text
J = lambda_nil/lambda_lens.
```

The down-sector labels:

```text
1/64, 3/2 lambda_nil
```

look like one dyadic survivor-width correction plus one nil half-channel
correction.

This is exactly the kind of finite eigenvalue data a selected right-channel
operator could produce.  But the labels are not proved until they are derived
from `Sigma_MTT`.

# CKM Preservation

Because the candidate acts in the weighted right singular basis:

```text
Z_x = Y_x G_A^{-1/2} = U_x S_x V_x^*,
Z_x' = U_x S_x exp(-A_x^cand) V_x^*,
```

the left singular vectors `U_x` are unchanged.  Therefore the CKM matrix is
preserved exactly up to numerical roundoff.

# Status

```text
Gaussian q_x^2 log(pi) base                  DIAGNOSTIC
finite residual labels found                 CANDIDATE
CKM-preserving action placement              PROVED by right-channel theorem
mass-ratio accuracy                          CHECKED
label derivation from Sigma_MTT              OPEN
```

# What Must Be Proved Next

The next target is to construct a finite self-adjoint right-channel operator:

```text
R_x =
  R_width,x
  + R_nil,x
  + R_dyadic,x
  + R_anchor,x
  + R_Higgs,x
```

such that, in the selected weighted right basis:

```text
spec_light(R_u) = (-3/2 J, +1/2 J),
spec_light(R_d) = (1/64, +3/2 lambda_nil).
```

If this operator is derived from selected MTT data, the quark mass closure will
move from an action-target theorem to an actual no-proxy source theorem.

