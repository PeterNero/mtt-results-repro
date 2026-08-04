# q79 Canonical Cauchy Quantum Model and Minimal Fock Recorder Theorem v1

Date: 2026-07-23

Status:
`B_QM_02_EXIT_COMPLETE_ON_CANONICAL_Q79_BINARY_ONE_ANCHOR_FINITE_SYMBOL_DOMAIN_GENERAL_CONTEXT_AND_STRICT_ZERO_ANCHOR_OPEN`

## 1. Completion data and scope

Work at the following declared minimal-data tier:

```text
A_QG:
  the selected q79/Z64/Q_WW finite-root-stack Lorentzian realization;

A_causal:
  one time orientation and retarded boundary class;

A_met:
  one metrological calibration t0=1/E0=L0 in c=hbar=1 units;

C_PQ:
  an apparatus context that interrogates the q79 Hessian spectrum P/Q.
```

`A_met` fixes units. It introduces no dimensionless coupling and is necessary
whenever dimensionful predictions are compared with a laboratory clock. The
selected dimensionless checkpoint is independent of its numerical unit:
\[
\gamma_0t_0=\log 448.
\]

The domain of this theorem is the canonical q79 binary finite-symbol
experiment. It does not include arbitrary apparatus contexts, the nonzero-Chern
continuum HYM carrier, a local field net, or objective single-outcome
actualization.

## 2. Cauchy quantum system

The previous Cauchy theorem supplies
\[
\mathcal H_\Sigma=L^2(\Sigma,d\mu_h;F_{\rm q79}),
\]
the normal state cone
\[
\mathfrak S_\Sigma
=\{\rho\in\mathcal T_1(\mathcal H_\Sigma):
  \rho\geq0,\ \operatorname{Tr}\rho=1\},
\]
and the decomposable q79 observable algebra. Let
\[
P=P_\Sigma,\qquad Q=Q_\Sigma=I-P.
\]
These are bounded, parallel, orthogonal projectors and are invariant under the
selected Cauchy/q79 gauge groupoid.

Use intrinsic physical time
\[
u=t/t_0\in\mathbb R_+.
\]
The one-anchor theorem gives the dimensionless rate
\[
\bar\gamma=\gamma_0t_0=\log448.
\]

## 3. Selected reduced propagator

Define on trace-class states
\[
\mathcal L_{\rm q79}(\rho)
=\log448\,[P\rho P+Q\rho Q-\rho].
\]
Because `P` and `Q` are bounded, this generator is bounded on the whole
trace-class space. Its exact semigroup is
\[
\Phi_u(\rho)
=P\rho P+Q\rho Q
448^{-u}(P\rho Q+Q\rho P).
\]
The four `P/Q` blocks prove directly that
\[
\Phi_{u+v}=\Phi_u\Phi_v,\qquad
\Phi_0=I.
\]
Each map is completely positive and trace preserving. At one reference
interval,
\[
\Phi_1(P\rho Q)=\frac1{448}P\rho Q.
\]

For two Cauchy representatives related by the already certified gauge
comparison unitary `U_21`, the reduced inter-slice map is
\[
\mathfrak P_{21}
=\operatorname{Ad}_{U_{21}}\circ\Phi_{u_2-u_1}.
\]
It composes exactly. This is the selected internal record-sector dynamics; it
does not claim a spatial kinetic or field-propagation law.

## Theorem A: exact canonical reduced dynamics

At the declared completion tier, the q79 finite action, preparation-blind
clock condition and one-anchor lift determine a gauge-covariant CPTP
propagator on every Cauchy trace-class state. It has no dimensionless fit
parameter and has zero mathematical approximation error on its stated domain.

## 4. Informative jump representation

The Hessian-square-root theorem selects the two record amplitudes. In intrinsic
time they are
\[
L_p=\sqrt{\log448}\,P,\qquad
L_q=\sqrt{\log448}\,Q.
\]
Their Gram sum is
\[
L_p^*L_p+L_q^*L_q
=\log448\,(P+Q)
=\log448\,I.
\]
The corresponding GKSL generator is
\[
\sum_{a=p,q}L_a\rho L_a^*
-\frac12\left\{\sum_aL_a^*L_a,\rho\right\}
=\mathcal L_{\rm q79}(\rho).
\]

The amplitudes `P` and `Q` are linearly independent. Two orthogonal nonzero
record labels therefore require noise multiplicity two. A one-channel
phase-flip dilation can reproduce the nonselective dephasing channel, but
cannot encode both informative `P` and `Q` records.

## 5. Minimal continuous Fock dilation

Let
\[
\mathcal F_{\rm rec}
=\Gamma_s\!\left(L^2(\mathbb R_+;\mathbb C^2_{\rm record})\right)
\]
with vacuum `Omega`. The bounded Hudson-Parthasarathy equation is
\[
\begin{aligned}
dU_u={}&
\sum_{a=p,q}
\left(L_a\,dA_a^\dagger-L_a^\dagger\,dA_a\right)U_u\\
&-\frac{\log448}{2}U_u\,du .
\end{aligned}
\]
The Hudson-Parthasarathy unitarity relations hold because the drift is
one half of the jump Gram. Bounded coefficients give a unique unitary adapted
cocycle on the exponential domain. Vacuum reduction gives
\[
\operatorname{Tr}_{\mathcal F_{\rm rec}}
\left[
U_u(\rho\otimes|\Omega\rangle\langle\Omega|)U_u^*
\right]
=\Phi_u(\rho).
\]

The repeated-interaction result supplies the same limit constructively. For a
collision interval `Delta`, choose
\[
\cos^2\theta_\Delta=e^{-\gamma_0\Delta}.
\]
The reduced collision map is exactly `Phi_Delta`, and every grid composition
is exactly `Phi_nDelta`. The interaction angle has the standard
square-root-time scaling required for the continuous quantum-noise limit.
Attal and Pautrat prove this repeated-to-continuous passage and show that
Lindblad generators arise from such collision limits:
<https://arxiv.org/abs/math-ph/0311002>.

### Type guard

The separate q79 free-graviton theorem establishes a conditional
two-helicity Fock sector. It is compatibility evidence only. Graviton
helicities are not identified with the `p/q` apparatus record channels.
`F_rec` is the minimal unitary dilation space of the recorder semigroup.

## Theorem B: minimal informative Fock completion

Once the canonical q79 `P/Q` recorder and preparation-blind rate are fixed,
the continuous informative dilation has two record channels and is unique up
to record-channel unitary gauge. It adds no numerical parameter or physical
particle identification.

## 6. Operational comparison functor

Define the preparation/apparatus category as follows.

An object contains:

1. a normalized upper preparation ensemble `lambda` whose second moment is
   trace class;
2. the canonical q79 apparatus `C_PQ`;
3. the ready Fock vacuum; and
4. an observation horizon `u`.

The preparation map is
\[
\lambda\longmapsto
\rho_\lambda
=\int|z\rangle\langle z|\,d\lambda(z).
\]

The stopped first-record instrument is
\[
\mathcal I_{r,u}(\rho)=448^{-u}\rho,
\]
\[
\mathcal I_{p,u}(\rho)
=(1-448^{-u})P\rho P,
\]
\[
\mathcal I_{q,u}(\rho)
=(1-448^{-u})Q\rho Q.
\]
Its sum is exactly `Phi_u`. The associated effects are
\[
E_{r,u}=448^{-u}I,\qquad
E_{p,u}=(1-448^{-u})P,\qquad
E_{q,u}=(1-448^{-u})Q,
\]
and they sum to the identity.

Unitary q79 frame changes and Cauchy diffeomorphisms intertwine the
preparation, channel, instrument and effect maps. Hence this is a covariant
comparison functor with zero error inside the ideal bounded Markov/Fock
domain.

At `u=1`, for the first q79 carrier basis preparation, the exact effects give
\[
\left(
\Pr(r),\Pr(p),\Pr(q)
\right)
=
\left(
\frac1{448},
\frac{149}{448},
\frac{149}{224}
\right).
\]
Conditional on a non-ready record, the weights are
\[
\left(\frac13,\frac23\right).
\]
These are consequences of the instrument and trace pairing. They are not
used as construction inputs.

## Theorem C: operational comparison closure

On the declared canonical binary domain, the preparation second-moment map,
q79 Fock recorder and stopped-record instrument give a complete covariant
map from upper preparation/apparatus data to states, effects, CP instruments
and reduced evolution. The domain and zero-error idealization are explicit.

Finite-bandwidth apparatus corrections require a separate correlation-time
estimate and are not hidden in this theorem.

## 7. Separation from the Born-source blocker

This theorem constructs an operational quantum instrument. It does not derive
why one individual record is actualized or prove
`SecondMomentCaptureDescent` from upper MTT dynamics. Those are `B.QM.01`
obligations.

In particular:

```text
B.QM.02:
  state space + algebra + reduced dynamics + comparison functor;

B.QM.01:
  source of realized-record weights and objective actualization.
```

The two blockers must not be merged merely because a CP instrument uses the
standard trace pairing to state its operational probabilities.

## 8. Parameter and declaration ledger

```text
inherited A_QG declarations:                 1 discrete
inherited A_causal declarations:             1 binary boundary mark
metrological calibrations:                   1 dimensionful unit anchor
declared apparatus contexts in this domain:  1 categorical context
new universal dimensionless parameters:      0
new fitted parameters:                       0
observed probabilities used as selectors:    0
new stochastic primitives:                   0
```

The Fock vacuum is the apparatus ready state. It is not claimed to be a unique
cosmic vacuum.

## 9. Closure verdict

The `B.QM.02` exit certificate is complete at the canonical q79 binary
one-anchor finite-symbol tier:

- Hilbert space: closed;
- state cone: closed;
- observable algebra: closed;
- reduced dynamics and Cauchy propagator: closed;
- preparation/apparatus comparison functor: closed;
- domain and error: explicit.

The stronger unaugmented claim that upper MTT derives an absolute clock
without a metrological anchor remains open and is dimensionally impossible
without breaking the scale symmetry. General apparatus contexts remain under
`B.QM.01`; local QFT and the continuum HYM carrier remain under
`B.QFT.01` and `B.HS.01`.
