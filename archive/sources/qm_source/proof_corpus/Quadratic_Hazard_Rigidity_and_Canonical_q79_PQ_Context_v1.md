# Quadratic-Hazard Rigidity and the Canonical q79 P/Q Context

## Hazard Rigidity

Let `h_a(z)` be the instantaneous response assigned to outcome `a` for a pure
finite-carrier amplitude `z`. Assume each response is nonnegative, continuous,
complex homogeneous of degree two, and satisfies the parallelogram identity.
Assume also

\[
\sum_a h_a(z)=\|z\|^2.
\]

Complex polarization gives a unique Hermitian sesquilinear form for each
`h_a`; finite-dimensional Riesz representation gives a unique positive operator
`E_a` with

\[
h_a(z)=\langle z,E_a z\rangle.
\]

The normalization identity for all `z` implies `sum_a E_a=I`. Thus a normalized
quadratic response law is necessarily a POVM response law. No observed
probability values enter.

## Canonical q79 Binary Context

The exact finite geometry already selects

\[
P=P_{\rm Haar},\qquad Q=I-P.
\]

Both are positive orthogonal projectors and `P+Q=I`. Therefore they define one
canonical binary response context:

\[
h_{\rm coh}(z)=\|Pz\|^2,
\qquad
h_{\rm strain}(z)=\|Qz\|^2.
\]

For the first basis vector in either permutation copy, exact rational
calculation gives

\[
h_{\rm coh}=1/3,
\qquad
h_{\rm strain}=2/3.
\]

These are selected response values, not fitted probabilities. The first is the
symmetric/coherent component and the second the closure-strain component.

## Scope

This closes the rate-operator source for one binary q79 context. It does not
derive:

1. the physical clock or instrument converting response into an outcome;
2. arbitrary apparatus contexts;
3. physical time normalization; or
4. objective trajectories.

General contexts require selected apparatus coupling operators `M_C,a` or an
equivalent decomposition of the physical interaction Hessian. Merely unitarily
rotating `P,Q` would import a context unless that rotation is emitted by the
apparatus dynamics.
