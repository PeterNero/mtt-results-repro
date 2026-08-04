# Same-Source Preparation Moment and Basin-Dilation Theorem

## Status

This theorem composes upper preparation ensembles with finite detector kernels.
It closes the algebraic consistency of preparation, effects, probability
noncontextuality and coarse-graining, conditional on one physical calibration
statement. It does not claim that MTT dynamics has already supplied that
calibration.

## 1. Preparation Moment Map

Let `H_fin` be the exact finite q79 complex carrier. A preparation protocol `x`
supplies a normalized ensemble `lambda_x` on its unit vectors. Define

\[
\rho_x=\int |z\rangle\langle z|\,d\lambda_x(z).
\]

This is positive and has trace one. It depends only on the preparation's second
moment. Different upper ensembles may have the same density operator; this is
the expected ensemble equivalence of quantum state descriptions, not an extra
theory parameter.

## 2. Detector Moment Map

For a context `C`, let the finite detector operators satisfy

\[
\sum_a M_{C,a}^*M_{C,a}=I,
\qquad E_{C,a}=M_{C,a}^*M_{C,a}.
\]

Then direct finite-dimensional calculation gives

\[
\int \|M_{C,a}z\|^2\,d\lambda_x(z)
=\operatorname{Tr}(\rho_xE_{C,a}).
\]

Consequently:

1. probabilities are normalized;
2. coarse-graining is additive;
3. two contexts that emit the same effect have the same probability; and
4. probabilities are independent of the ensemble decomposition of `rho_x`.

Thus probability noncontextuality and coarse-graining are not independent MTT
axioms once both preparations and detectors factor through these same-source
moment maps.

## Theorem

Every normalized upper preparation ensemble and normalized finite detector
family induces a density operator, a POVM and one probability functional with
the trace form above. The construction is functorial under unitary changes of
finite-carrier frame and depends on no observed probability values.

## 3. Exact Ensemble Nonuniqueness

On a two-dimensional subspace, the equal ensembles

\[
\{e_1,e_2\}/2
\quad\text{and}\quad
\{(e_1+e_2)/\sqrt2,(e_1-e_2)/\sqrt2\}/2
\]

both have density `I_2/2`. They therefore give the same probability `1/2` for
the plus projector despite being distinct upper ensembles. The verifier checks
this over exact rational projector entries.

## 4. Basin-Dilation No-Go

For any probability vector `(p_1,...,p_n)`, add one uniform coordinate
`u in [0,1]` and partition it into consecutive intervals of lengths `p_i`.
This realizes the desired weights as deterministic context-indexed events.

Therefore the existence of a basin atlas reproducing trace weights cannot be
the missing physical theorem. Such an atlas can always be manufactured after
the probabilities are known. It has source content only if the selected MTT
dynamics emits it independently.

## 5. Remaining Physical Gate

The frontier is reduced to the **quadratic-response capture calibration**:

\[
K^{\rm capture}_{x,C}(a)
=\int \|M_{C,a}z\|^2\,d\lambda_x(z)
\]

for the detector operators and preparation ensemble emitted by the same
disturbed evolve-project dynamics.

This equality must be proved from the physical MTT flow, projection, disturbance
law and basin capture. It cannot be supplied by a fitted partition, an arbitrary
threshold dilation, or shared-circle Haar averaging alone.
