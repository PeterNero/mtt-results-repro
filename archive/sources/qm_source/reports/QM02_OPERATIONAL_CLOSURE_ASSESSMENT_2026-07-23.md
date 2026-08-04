# B.QM.02 Operational Closure Assessment

Date: 2026-07-23

## Verdict

All clauses of the `B.QM.02` exit certificate are now composed on one explicit
domain:

```text
canonical q79 P_Haar/Q binary apparatus
+ finite-symbol Cauchy carrier
+ one metrological clock anchor
+ ideal bounded Markov/Fock recorder.
```

This is a genuine minimal-data closure tier, not universal quantum-field
theory.

## What changed

The previous theorem closed the Cauchy Hilbert/state/observable system and
gauge comparison functor but stopped before physical dynamics. The new
composition uses results that already existed in separate packets:

- the q79 Hessian selects the `P/Q` jump amplitudes;
- a preparation-blind clock forces equal sector rates;
- the additive one-anchor theorem fixes the dimensionless exponent
  `gamma0*t0=log(448)`;
- the collision recorder gives the exact finite-grid CP instrument;
- the bounded two-channel Fock dilation gives continuous reduced dynamics.

The resulting generator is

```text
Lbar(rho)=log(448)[P rho P+Q rho Q-rho],
```

and the exact intrinsic-time propagator is

```text
Phi_u(rho)
  =P rho P+Q rho Q+448^(-u)(P rho Q+Q rho P).
```

## Exact checkpoint

At `u=1`, for the first q79 carrier basis preparation:

```text
ready = 1/448,
P record = 149/448,
Q record = 149/224.
```

Conditioned on an emitted record, the weights are exactly `(1/3,2/3)`.
No observed probability is used to obtain these values.

The executable certificate verifies:

- the 20-dimensional block-diagonal superoperator range;
- the rank-16 dephasing generator;
- the exact GKSL identity;
- two-channel informative minimality;
- semigroup composition;
- the `1/7 * 1/64 = 1/448` checkpoint composition;
- instrument completeness;
- preparation normalization; and
- q79 gauge covariance.

The `1/7` and `1/64` factorization is an exact algebra witness only. No
separate physical Lens/Circle time intervals are claimed.

## Why the Fock step is legitimate

The collision model already requires a fresh-pointer or quantum-noise
continuum. The jump operators are bounded, so the standard
Hudson-Parthasarathy construction gives a unitary cocycle. Attal and Pautrat
prove that repeated interactions converge to this continuous quantum-noise
limit and that Lindblad generators arise from such limits:
<https://arxiv.org/abs/math-ph/0311002>.

The separate q79 free-graviton Fock result is not used as the apparatus
environment. Its two helicities are not relabelled as `P/Q` records.

## Exact scope

Closed at this tier:

- global finite-symbol Cauchy Hilbert system;
- state cone and declared observable algebra;
- one-anchor physical reduced dynamics;
- exact continuous Fock dilation;
- preparation second-moment map;
- canonical `P/Q` effect and instrument map;
- gauge-covariant comparison functor;
- explicit ideal-domain zero-error certificate.

Not closed by this result:

- objective actualization or the upper MTT Born source (`B.QM.01`);
- arbitrary apparatus contexts;
- finite-bandwidth laboratory error estimates;
- spatial field propagation, locality or a field net (`B.QFT.01`);
- the physical nonzero-Chern continuum HYM carrier (`B.HS.01`);
- interacting quantum gravity or UV completion.

## Status recommendation

Record:

```text
B.QM.02:
  CLOSED at canonical-q79-binary one-anchor finite-symbol tier;
  OPEN at strict zero-anchor and universal-apparatus tier.
```

This avoids both errors:

1. leaving the blocker generically open after its declared finite-domain exit
   has been constructed; and
2. promoting a restricted operational model into a claim of full quantum
   mechanics, QFT or objective measurement closure.

The next highest-value quantum target is again `B.QM.01`, specifically the
same-source realized-record/SecondMomentCaptureDescent theorem. Local QFT
becomes the next structural target once the central ledger accepts this
restricted `B.QM.02` closure tier.
