# Interaction-Hessian to Raw Apparatus-Channel Theorem

## Typed Input

Let `F_C` be the selected disturbed evolve-project map for a physical system and
apparatus configuration in context `C`. Linearize it at the prepared joint
state:

\[
D_C=dF_C.
\]

Let the apparatus readout space have an orthogonal pointer decomposition with
projectors `Pi_C,a` summing to the identity.

## Theorem

The raw response channels are canonically

\[
R_{C,a}=\Pi_{C,a}D_C.
\]

They satisfy

\[
\sum_aR_{C,a}^*R_{C,a}=D_C^*D_C.
\]

### Proof

Orthogonality and completeness of the pointer blocks give

\[
\sum_aD_C^*\Pi_{C,a}D_C
=D_C^*\left(\sum_a\Pi_{C,a}\right)D_C
=D_C^*D_C.
\]

If `D_C` is injective on the detected support, this Gram operator is positive
and invertible there. The Apparatus-Response Frame Normalization Theorem then
produces a normalized POVM without a response-scale parameter.

## Meaning

The apparatus need not be a universal theory parameter. It is a physical input
configuration, just as an initial state is. What the theory owes is a fixed rule
that maps that configuration and the common action to `F_C`, `D_C`, and its
pointer blocks.

## Corpus Status

The current measurement corpus supplies:

- localized apparatus disturbance;
- coherent projection and stabilization;
- conditional finite detector kernels; and
- downstream instruments.

It does not yet supply:

1. a typed joint system-apparatus configuration space;
2. a selected interaction term in the MTT action;
3. the resulting differentiable map `F_C`; or
4. source-defined pointer/readout projectors.

Therefore raw channel extraction is now a closed functor, while its physical
interaction derivative remains the operator-source frontier.
