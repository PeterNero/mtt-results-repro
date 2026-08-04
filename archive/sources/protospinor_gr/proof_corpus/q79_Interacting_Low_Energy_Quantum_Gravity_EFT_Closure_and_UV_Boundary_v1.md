# q79 Interacting Low-Energy Quantum Gravity EFT Closure and UV Boundary v1

Date: 2026-07-15

Status:
`Q79_INTERACTING_LOW_ENERGY_QG_EFT_PARITY_CLOSED_AT_FIXED_ORDER_LOCAL_WILSON_VALUES_PRIMITIVE_MTT_MEASURE_AND_UV_COMPLETION_OPEN`

## What is newly closed

The q79 finite-source construction already supplies the positive two-helicity
massless graviton, the unique two-derivative TEGR/Einstein action shape, and the
relative Hilbert stress coupling. There is therefore a standard interacting
quantum route which does not require the rejected permanent-Gaussian claim:
quantize that action as quantum general relativity effective field theory.

At the declared parity tier, define

```text
Obs_QG,EFT^MTT
  = Readout o LSZ/Inclusive o Green o Q_GR,EFT o E_q79.
```

`Q_GR,EFT` is the standard background-field BRST/BV perturbative construction,
imported as parity structure. This is exactly the standard used by the closed
renormalized-SM observable functor: equality of the renormalized action,
measure convention, state, scale, scheme, and coefficients through order `N`
implies equality of generating functionals and gauge-invariant observables
through order `N`. It is not rebranded as an MTT derivation of quantization.

The selected three-family SM representation also passes all six stored anomaly
rows, including the even `SU(2)` doublet count. This removes the already-audited
SM gauge/mixed-anomaly obstruction at the parity tier; it does not replace a
constructive proof of the full gravitational BV measure.

## Exact power-counting theorem

For a connected graph made from two-derivative Einstein vertices,

```text
D = 4L + 2V - 2I,
L = I - V + 1,
therefore D = 2L + 2.
```

The required local counterterms consequently have derivative order `2L+2`.
At every fixed loop/derivative order, the diffeomorphism-invariant local basis
is finite, so the theory is renormalizable and predictive order by order as an
EFT. The exact table begins

```text
tree:     2 derivatives
one loop: 4 derivatives
two loop: 6 derivatives.
```

The long-distance nonanalytic loop terms come from the massless low-energy
propagators. Local UV counterterms cannot imitate those nonanalytic terms, so
their coefficient class is fixed once `kappa_h`, the low-energy spectrum, and
the causal state are fixed. No new Wilson parameter enters that class.

## The exact UV boundary

For `Lambda_eff=0`, pure Einstein gravity has no physically relevant on-shell
one-loop divergence. At two loops, however, the pure-gravity S matrix has the
nonzero Goroff-Sagnotti divergence

```text
Gamma_div^(2) proportional to
  [209/(2880 (4 pi)^4 epsilon)] kappa_gr^2
  integral sqrt(-g) R_mn^rs R_rs^ab R_ab^mn,

kappa_gr^2 = 32 pi G_eff = 1/kappa_h.
```

This establishes both halves of the result:

1. interacting low-energy q79 quantum gravity reaches the standard predictive
   quantum-GR EFT tier at every declared finite order;
2. the same calculation proves that `kappa_h` and `Lambda_eff` alone cannot be
   a UV-complete interacting quantum theory.

The finite q79 internal algebra fixes internal traces and the helicity block,
but it does not change the `D=2L+2` spacetime power counting.

## Parameter ledger

At two derivatives there are exactly the already-recorded coordinates
`kappa_h` (or `G_eff`) and `Lambda_eff`. Free quantization adds none. The
UV-independent nonanalytic long-distance quantum class adds none. Local
higher-derivative terms require finitely many Wilson coefficients at each
fixed order, but their numerical values are not yet emitted by the selected
MTT source; across all orders this is an unbounded tower unless a genuine UV
completion selects it.

Gauge choice, subtraction scheme, and renormalization scale are conventions,
not new physical fit parameters. Initial, causal, or asymptotic state data are
state data rather than law parameters.

## What remains for full quantum gravity

The remaining hard target is no longer the existence of an interacting
low-energy quantum theory. It is one of the genuinely stronger exits:

1. derive the higher-curvature Wilson rows from the selected q79 operator and
   control their full remainder; or
2. select and prove a nonperturbative UV fixed theory with its quantum measure,
   BV/constraint closure, unitarity, and continuum limit.

Primitive MTT selection of the Lorentzian realization, numerical `kappa_h`,
`Lambda_eff`, and a unique cosmic state remain separate source/value questions.

## Primary comparison sources

- Donoghue, low-energy gravity EFT and UV-independent nonanalytic corrections:
  https://arxiv.org/abs/gr-qc/9405057
- Donoghue, modern quantum-GR EFT review:
  https://arxiv.org/abs/2211.09902
- 't Hooft and Veltman, one-loop gravity:
  https://inspirehep.net/literature/95368
- Goroff and Sagnotti, two-loop pure gravity:
  https://inspirehep.net/literature/213907
