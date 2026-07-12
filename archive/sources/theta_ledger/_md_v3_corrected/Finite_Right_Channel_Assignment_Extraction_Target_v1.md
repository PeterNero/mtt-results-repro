---
abstract: |
  We define the exact extraction test that remains after the finite
  right-channel label theorems.  The projectors are unique and the label
  values have conditional MTT derivations.  The only remaining source step is
  to show that the concrete selected MTT source map assigns those labels to
  the correct weighted right-channel projectors.  This note formulates that as
  trace/projector tests for three source observables:
  S_u^{spin}, S_d^{dyad}, and S_d^{nil}.  Passing these tests promotes the
  current finite-label candidate from a CKM-preserving mass ansatz to a
  selected no-proxy mass source theorem.
author:
- Peter Nero
date: June 2026
title: |
  Finite Right-Channel Assignment Extraction Target
---

# Purpose

The current status is:

```text
projectors unique once labels are selected          PROVED
up labels from retarded spinorial source            PROVED-CONDITIONAL
down labels from dyadic/nil source                  PROVED-CONDITIONAL
```

The remaining problem is not numerical.  It is the assignment:

```text
which selected MTT source label acts on which weighted right-channel projector?
```

# Weighted Right Projectors

For each sector:

```text
Z_x = Y_x G_A^{-1/2},
K_x = Z_x^* Z_x.
```

Because `K_x` has simple spectrum, its projectors are unique:

```text
P_{x,a} = spectral projector of K_x,
a = light, middle, heavy.
```

# Required Source Observables

The concrete selected MTT source map must supply three commuting right-channel
observables:

```text
S_u^spin,
S_d^dyad,
S_d^nil.
```

They must satisfy:

```text
[S_u^spin,K_u]=0,
[S_d^dyad,K_d]=0,
[S_d^nil,K_d]=0.
```

# Assignment Tests

The up-sector spinorial sign assignment is:

```text
Tr(P_{u,1} S_u^spin) = -1,
Tr(P_{u,2} S_u^spin) = +1,
Tr(P_{u,3} S_u^spin) = 0 or heavy-sector inactive.
```

The down-sector dyadic/nil assignment is:

```text
Tr(P_{d,1} S_d^dyad) = 1,
Tr(P_{d,2} S_d^dyad) = 0,

Tr(P_{d,1} S_d^nil)  = 0,
Tr(P_{d,2} S_d^nil)  = 1.
```

Equivalently:

```text
S_d^dyad = P_{d,1} on the light subspace,
S_d^nil  = P_{d,2} on the light subspace.
```

# Mass Source Reconstruction

If the assignment tests pass, then the selected residual source is:

```text
R_u = J(-1/2(P_{u,1}+P_{u,2}) + S_u^spin),

R_d = (1/64)S_d^dyad + (3/2 lambda_nil)S_d^nil.
```

The total mass actions are:

```text
A_u = 4 log(pi)(P_{u,1}+P_{u,2}) + R_u,
A_d = log(pi)(P_{d,1}+P_{d,2}) + R_d.
```

# Theorem Target

To close the quark mass source theorem, prove:

```text
Sigma_MTT | right-channel light space
  supplies S_u^spin, S_d^dyad, S_d^nil
  satisfying the assignment tests above.
```

Then the finite-label mass candidate is no longer a diagnostic.  It becomes
the selected quark mass action source.

# What This Closes

```text
remaining assignment problem made finite      DEFINED
trace/projector extraction tests              DEFINED
next calculation objective                    DEFINED
source theorem itself                         OPEN
```

# Bottom Line

The next computation is exact and small:

```text
compute the three right-channel label observables from Sigma_MTT
and evaluate their traces on P_{u,1},P_{u,2},P_{d,1},P_{d,2}.
```

If the trace table matches:

```text
up spin:       (-1,+1)
down dyad/nil: (1,0), (0,1)
```

then the finite mass source is selected.

