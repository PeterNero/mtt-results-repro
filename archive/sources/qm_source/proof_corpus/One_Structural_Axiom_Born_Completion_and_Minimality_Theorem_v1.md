# One-Structural-Axiom Born Completion and Minimality Theorem

## Base Theory

Let `T_fin` contain the exact finite q79 carrier, shared complex line,
`P_Haar`, normalized Hessian, finite state/effect cones, classical mixing of
upper preparation ensembles, normalized physical outcome contexts, and the
exact finite symmetries.

## Independence

`T_fin` has both:

1. a quadratic capture model
   `K_a(lambda)=integral <z,E_a z>d lambda`, which descends through `rho`; and
2. the normalized q79-symmetric fourth-moment model
   `K_1(lambda)=integral ||P_Haar z||^4d lambda`, which does not descend.

Both respect the current finite symmetries and upper-measure mixing. Therefore
`T_fin` does not decide the Born trace rule. Some logically independent
physical condition is necessary.

## Completion Axiom

Adopt one structural axiom:

> **A_Born: SecondMomentCaptureDescent.** For every selected physical context
> and outcome, the capture probability of an upper preparation ensemble depends
> on that ensemble only through
> `rho_lambda=integral |z><z|d lambda`.

This axiom contains no probability values, continuous constants or discrete
numerical selectors.

## Completion Theorem

`T_fin+A_Born` has unique effects `E_C,a` satisfying

\[
K_{C,a}(\lambda)=\operatorname{Tr}(\rho_\lambda E_{C,a}),
\qquad \sum_aE_{C,a}=I.
\]

### Proof

Upper-measure mixing makes capture affine. `A_Born` descends each affine
functional to the density cone. Finite-dimensional trace duality gives a unique
Hermitian representative; positivity makes it an effect, and context
normalization makes the family a POVM. The trace equation follows identically.

## Minimality

The two base-theory models prove that zero additional logical input cannot close
the theorem relative to the currently declared assumptions. One axiom is
sufficient. This is logical minimality at the current theory boundary, not a
claim that every equivalent axiomatisation has a unique sentence count.

## Ledger

```text
new structural axioms:           1
new continuous parameters:       0
new discrete numerical selectors:0
observed probabilities used:     0
```

## Status

The axiom is a completed candidate, not yet adopted as MTT law. A zero-axiom
upgrade would derive it from the selected disturbed dynamics. The
Quadratic-Hazard First-Capture Theorem supplies one explicit sufficient
mechanism, pending a selected clock/rate source.

This completion addresses finite outcome probabilities. It does not by itself
provide objective trajectories, physical time normalization or the global
quantum dynamics required by `B.QM.02`.
