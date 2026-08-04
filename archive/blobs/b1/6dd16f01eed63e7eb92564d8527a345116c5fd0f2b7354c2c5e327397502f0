# Affine Capture Representation and Second-Moment Descent Theorem

## Purpose

This theorem identifies the exact remaining mathematical condition for turning
upper MTT preparation/capture statistics into finite quantum effects. It replaces
several loosely stated probability requirements by one quotient condition.

## Preparation Quotient

For a normalized ensemble `lambda` on finite-carrier unit vectors, define

\[
q(\lambda)=\rho_\lambda
=\int |z\rangle\langle z|\,d\lambda(z).
\]

Two ensembles are equivalent when they have the same second moment. Let
`K_C,a(lambda)` be the physical capture probability of outcome `a` in context
`C`.

## Second-Moment Capture Descent

The required condition is

\[
q(\lambda_1)=q(\lambda_2)
\quad\Longrightarrow\quad
K_{C,a}(\lambda_1)=K_{C,a}(\lambda_2)
\]

for every physical context and outcome. This is exactly the fiber-invariance
criterion for descent through the moment quotient.

## Theorem

Assume:

1. capture probabilities are affine under classical mixing of upper preparation
   ensembles;
2. each context is normalized over its outcomes; and
3. second-moment capture descent holds.

Then there are unique effects `E_C,a` on the finite q79 carrier such that

\[
K_{C,a}(\lambda)
=\operatorname{Tr}(\rho_\lambda E_{C,a}),
\qquad
\sum_aE_{C,a}=I.
\]

### Proof

Classical mixing makes each capture probability affine on upper measures.
Second-moment descent defines an affine function on the density-operator cone.
Every affine probability functional on the finite density cone has a unique
Hermitian trace-dual representative. Positivity on all density operators puts
that representative in the effect interval, and context normalization forces
the effects to sum to the identity.

Thus the trace rule is not an additional assumption after descent. It is the
unique finite-dimensional representation of the descended capture functional.

## Exact Countermodel

Let `p` be a unit vector in the `P_Haar` sector and `q` a unit vector in its
complement. Let ensemble `A` be the equal mixture of `p,q`, and ensemble `B` the
equal mixture of `(p+q)/sqrt(2),(p-q)/sqrt(2)`. Both have the same density.
Define a normalized binary capture kernel by

\[
K_1(\lambda)=\int \|P_{\rm Haar}z\|^4d\lambda(z),
\qquad K_2=1-K_1.
\]

Then

\[
(K_1,K_2)(A)=(1/2,1/2),
\qquad
(K_1,K_2)(B)=(1/4,3/4).
\]

The kernel is normalized and affine in the upper preparation measure, but it
does not descend through `rho`. Because `P_Haar` commutes with diagonal `S3`,
`J_DE` and the normalized Hessian, the countermodel also preserves all three
exact finite symmetries. Therefore normalization, upper-measure linearity,
shared-circle Haar data and finite q79 symmetry do not prove the Born
representation.

## Frontier

The remaining MTT-specific theorem is now one statement:

> **SecondMomentCaptureDescent.** The physical disturbed evolve-project capture
> law is insensitive to all upper preparation information beyond the selected
> finite-carrier second moment.

Equivalently, the physical capture functionals must lie in the quadratic span
`z -> <z,E z>`. This must be derived from the selected MTT dynamics or adopted
as a clearly named physical axiom; it cannot be inferred from basin existence.
