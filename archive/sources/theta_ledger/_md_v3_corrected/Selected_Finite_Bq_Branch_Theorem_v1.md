---
abstract: |
  We consolidate the selected finite B_q branch for quark CKM magnitudes.  The
  branch is generated from non-CKM sources: q79 finite CP character, Z3 bridge
  reduction, proto-spinor anchor profile, color-singlet Schur completion,
  retarded predecessor orientation, primitive lens-nil gap after no-double
  counting, and topology-only hypercharge-square stiffness.  This fixes
  sigma=-1, Lambda_q=lambda_lens-lambda_nil, mu_u=8, and mu_d=2.  The resulting
  CKM diagnostic is quark-shaped without entry-wise Yukawa fitting.  The theorem
  is conditional on the selected-source premises already isolated in the
  component notes; the remaining execution task is to extract the full Hessian
  blocks and verify that they realize the same charge-twist curvature.
author:
- Peter Nero
date: June 2026
title: |
  Selected Finite B_q Branch Theorem for Quark CKM Magnitudes
---

# Purpose

The B_q branch is now spread across several notes.  This paper states the
assembled branch as one finite theorem packet.

# Selected Inputs

The selected finite inputs are:

```text
q = 79 mod 448,
tau = exp(2 pi i 79/448),
family carrier = Z3,
b_ij = -(i+j) mod 3,
J = (0, lambda_nil/lambda_lens, 1),
lambda_lens = 3.57,
lambda_nil = 0.25.
```

# Selected B_q Constants

The component source notes select:

```text
color Schur coefficient: 1/2,
orientation:             sigma = -1,
gap coefficient:          Lambda_q = lambda_lens - lambda_nil,
up stiffness:             mu_u = 8,
down stiffness:           mu_d = 2.
```

The provenance is:

```text
1/2       <- color-singlet two-channel Schur completion,
sigma=-1 <- q79 retarded predecessor orientation,
Lambda_q <- no double counting after internal color completion,
mu_u,d   <- topology-only hypercharge-square charge-twist Hessian.
```

# Selected Quark Kernel

For `x in {u,d}` define:

```text
s_u = 1,
s_d = 2,
C_x[b] = exp(-mu_x J_b) tau^{s_x b}.
```

Define:

```text
D_q(i,j,b)^2 =
  (J_i - J_b)^2
  + (1/2)(J_j - J_{b-1})^2.
```

Then:

```text
Y_x[i,j] =
  C_x[b_ij]
  exp[-(lambda_lens-lambda_nil) D_q(i,j,b_ij)^2].
```

No entry of `Y_u` or `Y_d` is independently assigned.

# Diagnostic Output

Using the anchored inverse metric:

```text
G_A^{-1} = diag(exp(-2J_0), exp(-2J_1), exp(-2J_2)),
```

the check computes:

```text
H_u = Y_u G_A^{-1} Y_u^*,
H_d = Y_d G_A^{-1} Y_d^*,
V = U_u^* U_d.
```

The resulting magnitude matrix is approximately:

```text
|V| =
[[0.974646, 0.223566, 0.009109],
 [0.223057, 0.974019, 0.039148],
 [0.017615, 0.036129, 0.999192]].
```

This is CKM-shaped:

```text
|V_us| about 0.224,
|V_cb| about 0.039,
|V_ub| about 0.009.
```

The residual against a standard CKM magnitude target is about:

```text
0.014322.
```

The residual is not used to select the branch.  It is only an after-the-fact
diagnostic.

# Theorem: Selected Finite B_q Branch

Assume the selected-source premises proved or isolated in the component notes:

1.  the q79 finite CP character branch is selected;

2.  the retained family bridge is the `Z3` bridge `b_ij=-(i+j) mod 3`;

3.  the proto-spinor anchor profile is

    ```text
    J=(0,lambda_nil/lambda_lens,1);
    ```

4.  quark color admissibility requires hidden two-channel color-singlet Schur
    completion;

5.  the B_q hidden adjacent role uses the same retarded predecessor orientation
    as the q79 CP branch;

6.  color redundancy is counted internally by the Schur completion, so the
    remaining primitive gap is `lambda_lens-lambda_nil`;

7.  the sector closure-strain Hessian contains the topology-only
    hypercharge-square charge-twist block with two-ended Yukawa normalization.

Then the selected finite B_q branch is:

```text
sigma=-1,
Lambda_q=lambda_lens-lambda_nil,
mu_u=8,
mu_d=2,
```

and the quark kernel is the one above.

# Proof

Items 1--3 supply the finite CP phase, family bridge, and first-order anchored
metric.

Item 4 gives the Schur coefficient:

```text
1/2.
```

Item 5 gives:

```text
sigma=-1.
```

Item 6 gives:

```text
Lambda_q=lambda_lens-lambda_nil.
```

Item 7 gives primitive right-sector charge numerators:

```text
q_u=2,
q_d=1,
```

and quadratic two-ended stiffness:

```text
mu_x = 2 q_x^2.
```

Therefore:

```text
mu_u=8,
mu_d=2.
```

Substituting these constants into the bridge formula gives the selected finite
B_q kernel.

# What This Closes

```text
finite B_q branch constants from non-CKM sources      SELECTED-CONDITIONAL
entry-wise Yukawa fitting avoided                     CHECKED
CKM-shaped quark mixing obtained                      CHECKED
swapped-stiffness diagnostic branch retired           SUPPORTED
```

# What Remains

This theorem is not yet full SM closure.  The remaining tasks are:

```text
extract full H_u^cl,H_d^cl,H_anchor from Sigma_MTT     OPEN
verify charge-twist Hessian block in the full operator OPEN
derive absolute Yukawa singular values/masses          OPEN
include RG running and threshold normalization         OPEN
close lepton/PMNS and neutral sector consistently      OPEN
```

# Bottom Line

The quark CKM-magnitude branch is now finite and specified:

```text
(q, sigma, Lambda_q, mu_u, mu_d)
= (79 mod 448, -1, lambda_lens-lambda_nil, 8, 2).
```

It is selected conditionally by MTT source structure, not by fitting CKM
entries.  The next level is no longer branch selection; it is full Hessian and
mass execution.

