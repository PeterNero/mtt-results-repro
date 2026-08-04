# Quadratic-Hazard First-Capture Born Theorem

## Construction

Let a normalized finite detector context have operators `M_C,a` with

\[
\sum_aM_{C,a}^*M_{C,a}=I.
\]

For a unit finite-carrier state `z`, define rates

\[
r_{C,a}(z)=\|M_{C,a}z\|^2.
\]

They are nonnegative and sum to one. Suppose the disturbed capture dynamics,
conditional on `z`, produces independent exponential clocks `T_C,a` with these
rates, and the first clock to ring determines the stabilized outcome.

## Theorem

The probability that outcome `a` captures first is

\[
\Pr(T_{C,a}=\min_bT_{C,b}\mid z)
=\frac{r_{C,a}(z)}{\sum_br_{C,b}(z)}
=r_{C,a}(z).
\]

For an upper preparation ensemble `lambda_x`, therefore,

\[
\Pr(a\mid x,C)
=\int\|M_{C,a}z\|^2d\lambda_x(z)
=\operatorname{Tr}(\rho_xE_{C,a}),
\qquad E_{C,a}=M_{C,a}^*M_{C,a}.
\]

### Proof

For fixed `z`, the joint survival probability to time `t` is
`exp(-t sum_b r_C,b)`. Integrating the density that clock `a` rings at `t`
while every clock survives to `t` gives

\[
\int_0^\infty r_{C,a}e^{-t\sum_br_{C,b}}dt
=r_{C,a}/\sum_br_{C,b}.
\]

Detector normalization makes the denominator one. Averaging over `lambda_x`
and applying the preparation-moment identity gives the trace formula.

## Exact Scope

This is a complete constructive mechanism for
`SecondMomentCaptureDescent`. It also gives normalization, coarse-graining and
probability noncontextuality for equal effects.

It is not yet an MTT source theorem. The current corpus provides normalized
finite detector kernels and a linearized OU disturbance sector, but it does not
derive independent exponential capture clocks with the displayed rates.
Generic OU first-passage times are not exponential, and the existence of a
Markov approximation alone does not identify a jump hazard.

The canonical fixed-point kernel does not finish the construction on the exact
finite q79 symbol either. With `A=Q` and `P=P_Haar`, projector algebra gives

\[
P_{\rm Haar}e^{-\tau Q}P_{\rm Haar}=P_{\rm Haar}.
\]

Thus its coherent restriction loses `tau` and supplies one projector rather
than a normalized physical outcome context. Additional apparatus/context
operators are essential.

## Physical Exit Contract

MTT must provide either:

1. an exact finite jump generator whose outcome intensities are
   `M_C,a^*M_C,a`; or
2. a controlled Davies/Markov/secular limit deriving those clocks and rates,
   with a declared domain and error bound.

Once either contract is met, the remaining finite Born-source gate closes
without fitted probabilities or an independent Born postulate.
