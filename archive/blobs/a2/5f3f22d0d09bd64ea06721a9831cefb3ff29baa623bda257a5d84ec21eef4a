# Iwasawa Reduced Green Operator Validator

## Purpose

The Riesz/gap validator checks that a low spectral cluster is isolated. The
next object needed by the C1 response formula is the reduced Green operator on
the complement of that cluster.

This note makes the Green-operator claim executable. It does not construct the selected operator.
It validates a finite candidate once selected spectral data are supplied.

## Finite Contract

For each sector

```text
Q, u, d, L, e, N, H
```

the validator expects:

```text
Gram matrix G,
stiffness matrix K,
Riesz projector P,
complement projector Q,
reduced Green operator R,
complement gap gamma,
truncation error eta,
Green norm bound.
```

Define the finite operator:

```text
A = G^{-1} K.
```

The supplied complement must be:

```text
Q = I - P.
```

## Green Equations

The reduced Green operator is not a free matrix. It must satisfy:

```text
A R = Q,
R A = Q,
R P = 0,
P R = 0,
Q R = R,
R Q = R.
```

The projector and Green operator must also be self-adjoint in the supplied
Gram metric:

```text
P^* G = G P,
Q^* G = G Q,
R^* G = G R.
```

These equations certify that `R` is the inverse of `A` on the complement and
vanishes on the selected low cluster.

## Gap Norm Rule

The gap/error data must obey:

```text
gamma > eta,
green_norm_bound >= 1/(gamma - eta).
```

This is the finite bound needed before using the Green operator in the response
formula. It prevents a hidden blow-up in the horizontal solve.

## Link To The C1 Response

The downstream formula is:

```text
dotPsi_a,i = -R_a Q_a dotD_a Psi_a,i.
```

This validator supplies the `R_a Q_a` part of that formula. It deliberately
does not supply `dotD_a`, the source vector `dotD_a Psi_a,i`, or the primitive
Yukawa contractions.

## What This Closes

This closes the validator layer for:

```text
finite complement projectors,
finite reduced Green operators,
inverse-on-complement identities,
gap-derived Green norm bounds.
```

## What Remains Open

The validator does not prove:

```text
the candidate D_E is selected by MTT,
the selected spectral slot data have been supplied,
the selected reduced Green operator has been computed,
dotD_alpha1 is known,
horizontal zero-mode responses are known,
Yukawa matrices are computed.
```

## Verdict

The next proof obligation is now sharply separated:

```text
first validate selected spectral slots and reduced Green operators;
then validate dotD_alpha1 and the horizontal response vectors.
```

No flavor entry is introduced as a fit parameter at this stage.
