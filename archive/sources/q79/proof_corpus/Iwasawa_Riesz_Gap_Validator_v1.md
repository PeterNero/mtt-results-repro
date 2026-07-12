# Iwasawa Riesz Projector And Gap Validator

## Purpose

The previous finite `D_E` validator checks whether a proposed sector operator
has consistent Gram, stiffness, kernel, and zero-mode data. The next mathematical
claim is different:

```text
the listed low modes are selected by an isolated Riesz projector.
```

This note makes that claim executable. It does not construct the selected operator.
It validates a finite spectral certificate once such operator data are supplied.

## Supported Finite Data

For each sector

```text
Q, u, d, L, e, N, H
```

the validator expects:

```text
dimension,
Gram matrix G,
stiffness matrix K,
low eigenvalues lambda_i,
cluster eigenvectors v_i,
residual bounds,
Riesz projector P,
contour radius tau,
complement gap gamma,
truncation error eta.
```

The family sectors must have three low modes. The Higgs carrier must have one
low mode.

## Algebraic Checks

The implemented checks are:

```text
G is positive-definite Hermitian,
K is Hermitian,
K v_i = lambda_i G v_i within the reported residual bounds,
<v_i,v_j>_G = delta_ij,
P^2 = P,
P^* G = G P,
rank(P) is the expected low-cluster dimension,
P = V V^* G for the listed G-orthonormal cluster,
P v_i = v_i.
```

Thus the projector is not an arbitrary matrix. It must be the Gram-orthogonal
projector onto the supplied low spectral cluster.

## Gap And Error Rule

The robust Riesz contour rule is:

```text
epsilon_low + eta < tau < gamma - eta,
```

where:

```text
epsilon_low = max_i(|lambda_i| + residual_i),
eta         = truncation_error_bound,
tau         = contour_radius,
gamma       = complement_gap.
```

This is the finite certificate version of the spectral isolation claim. The low
cluster must lie inside the contour even after its reported error, and the
complement must remain outside the contour after the truncation allowance.

## What This Closes

This closes the validator layer for:

```text
finite low-cluster eigenpair data,
finite Gram-orthogonal Riesz projectors,
finite robust gap/error inequalities.
```

It also gives the next downstream artifacts a precise input format. The reduced
Green operator can be checked against the complement of this projector, and the
zero-mode response formula can then use the same basis:

```text
dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i.
```

## What This Does Not Prove

The validator deliberately does not prove:

```text
the candidate D_E is selected by MTT,
the typed monad or HYM source has been supplied,
the complement spectrum was independently computed,
the truncation bound is sharp,
dotD_alpha1 is known,
the reduced Green operator is known,
Yukawa matrices are computed.
```

Those remain separate no-proxy certificates.

## Verdict

The Riesz/gap proof obligation is now an executable finite gate:

```text
given selected D_E spectral data,
check the low cluster, projector, and robust gap inequality.
```

This moves the frontier from "define the projector" to "supply selected
spectral slot data from the actual MTT operator."
