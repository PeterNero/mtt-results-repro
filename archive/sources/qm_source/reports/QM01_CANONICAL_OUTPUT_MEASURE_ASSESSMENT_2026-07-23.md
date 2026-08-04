# QM01 Canonical Output-Measure Assessment

Date: 2026-07-23

Repository baseline:
`d9a17635b5b59550de88020a5e51ccc3be98bd98`

Kernel model:
`79076e8fe7aaefb793e491513c99812d9720d2f8d2714d74210aeec1c48a7f7f`

Blocker:
`B.QM.01`

## Result

The selected canonical q79 Hudson-Parthasarathy recorder has a commuting
outgoing number-process algebra. Restricting the already selected normal
preparation-plus-vacuum state to that algebra gives a unique classical
stopped-output measure.

The exact first-record effects are

\[
F_u(r)=e^{-\gamma u}I,\qquad
F_u(ds,a)=\gamma e^{-\gamma s}P_a\,ds.
\]

Their CP instrument is

\[
\mathcal I_{r,u}(\rho)=e^{-\gamma u}\rho,
\]

\[
\mathcal I_{a,u}(\rho)
=(1-e^{-\gamma u})P_a\rho P_a.
\]

This is exactly the instrument already certified in the operational
`B.QM.02` packet.

## Frontier change

Before this result, the recorder supplied its unitary, jump operators and CP
instrument, but the classical path measure and its relationship to
`SecondMomentCaptureDescent` had not been proved from the commuting output
algebra.

Now, for every normalized upper preparation in the declared canonical
`P/Q` apparatus context,

\[
\mu_{\lambda,u}(ds,a)
=\gamma e^{-\gamma s}
\operatorname{Tr}(\rho_\lambda P_a)\,ds.
\]

Therefore equal second moments imply equal complete stopped-history laws.
The former fourth-moment rule is excluded on this selected recorder domain.

## Correct status

`B.QM.01` is now complete at the canonical binary operational-output tier,
relative to the normal-state probability semantics already accepted in
`B.QM.02`.

It is not globally or ontologically closed:

- arbitrary apparatus source maps remain open;
- finite-bandwidth and non-Markov corrections remain open;
- a pre-quantum derivation of state-expectation probability remains open if
  demanded;
- the measure does not select one uniquely actual sample path.

The last item belongs to the objective-collapse/actualization problem. It
must not be smuggled into the claim that a classical output measure exists.

## Primitive count

For the canonical operational output measure:

```text
new stochastic primitives:          0
new continuous parameters:          0
new discrete numerical selectors:   0
new fitted values:                   0
observed probabilities used:        0
```

The earlier marked-Poisson construction remains a valid one-primitive
objective-trajectory completion. It is no longer needed merely to represent
the canonical recorder's operational output law.

## Exact checkpoint

At one intrinsic q79 interval:

```text
ready = 1/448
P     = 149/448
Q     = 149/224
```

Conditional on a record:

```text
P = 1/3
Q = 2/3
```

The machine certificate also verifies subdivision consistency:

```text
1/7 x 1/64 = 1/448
(1-1/7) + (1/7)(1-1/64) = 447/448.
```

## Recommended central ledger wording

```text
B.QM.01:
  CLOSED at canonical q79 binary one-anchor operational output-measure tier.
  OPEN for universal apparatus contexts, pre-quantum probability semantics
  if required, and objective single-history actualization.
```

This wording advances the frontier without claiming that an abelian
probability space, by itself, explains why one history is ontically actual.
