# Iwasawa dotD Alpha1 Response Validator

## Purpose

The reduced Green validator supplies the complement inverse needed for the
linearized zero-mode equation. The next finite object is the response of each
selected zero mode to the selected C1 alpha1 deformation.

This note makes the response claim executable. It does not construct the selected `dotD_alpha1` operator.
It validates supplied finite response data.

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
dotD_alpha1 matrix,
ordered zero-mode basis psi_i,
source vectors s_i,
horizontal response vectors dotPsi_i.
```

Define:

```text
A = G^{-1} K.
```

## Response Equations

The source vector must be:

```text
s_i = Q dotD_alpha1 psi_i.
```

The horizontal response must be:

```text
dotPsi_i = - R s_i = - R Q dotD_alpha1 psi_i.
```

The first-order zero-mode equation must then hold:

```text
A dotPsi_i + s_i = 0.
```

The selected horizontal gauge is:

```text
P dotPsi_i = 0,
<psi_j,dotPsi_i>_G = 0.
```

So neither `s_i` nor `dotPsi_i` can be chosen as a texture knob.

## What This Closes

This closes the validator layer for:

```text
finite dotD source vectors,
finite horizontal zero-mode responses,
linearized zero-mode equations in the selected finite basis.
```

It gives the primitive C1 contraction stage the missing response vectors, once
actual selected data are supplied.

## What Remains Open

The validator does not prove:

```text
the candidate D_E is selected by MTT,
dotD_alpha1 comes from the selected Hessian/C1 source,
the primitive overlap contractions have been evaluated,
the explicit C1 vertex is absent or known,
basis connection terms are zero or known,
Yukawa matrices are computed.
```

## Verdict

The next proof obligation is now:

```text
supply selected dotD_alpha1 matrices,
validate the horizontal responses,
then evaluate the six primitive 3x3 C1 contraction blocks.
```
