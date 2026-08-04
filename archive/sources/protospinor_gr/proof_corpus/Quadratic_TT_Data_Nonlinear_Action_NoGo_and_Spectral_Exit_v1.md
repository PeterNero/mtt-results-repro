# Quadratic TT Data Nonlinear Action No-Go and Spectral Exit v1

Date: 2026-07-15

## Exact no-go

The computed `DG`, global helicity bundle, scalar TT Hessian, Fierz-Pauli
operator, and `kappa_h` relation do not select a unique nonlinear action.

On a flat background let

```text
g(epsilon)=eta+epsilon h
```

and define the diffeomorphism-invariant local family

```text
S_alpha
  = S_EH
  + (alpha/kappa_h) integral sqrt(-g)
      C_mn^rs C_rs^ab C_ab^mn,
```

where `alpha` is dimensionless. Since

```text
C[g(epsilon)] = epsilon C1[h] + O(epsilon^2),
```

the deformation starts at cubic order:

```text
sqrt(-g) C^3
  = epsilon^3 C1_mn^rs C1_rs^ab C1_ab^mn + O(epsilon^4).
```

Therefore its value, first variation, and second variation at flat space all
vanish. Every `S_alpha` has the same flat background equation and the same
Fierz-Pauli Hessian, but generic third variations and nonlinear graviton
vertices differ. The family introduces no new dimensionful scale because
`kappa_h^-1` has the required length-squared dimension.

This proves an exact independence result:

```text
quadratic TT closure + diffeomorphism invariance
  does not imply a unique nonlinear action.
```

The at-most-second-order infrared clause in the Lovelock reduction is therefore
essential. It cannot be inferred from the already computed Hessian.

## Spectral-action corpus audit

The latest SM authority packets provide a serious superset route:

- `A51` closes the finite one-form calculation, the selected rank-four
  single-Higgs projection, and the bosonic operator content via the standard
  product-triple heat-kernel theorem.
- `A52` closes the adopted-profile product-triple matter interface.
- `A53` supplies exact `tau_int=log(448)/15` and a positive one-atom moment
  sequence under a named minimal-support premise.

They do not yet select the gravitational action:

- `A51` leaves absolute spectral normalization open.
- `A52` imports rather than derives the Wick-rotated four-dimensional
  spacetime interface and leaves strict cutoff moments open.
- `A53` explicitly says the point measure is not selected by MTT and strict
  spectral-action closure remains open.

The distinction is physically important. The spectral action contains
cosmological, Einstein-Hilbert, Weyl-curvature, and nonminimal terms. The
original spectral-action paper likewise describes the result as the Standard
Model coupled to Einstein plus Weyl gravity:
<https://arxiv.org/abs/hep-th/9606001>.

Thus this route does not evade the infrared-order problem. It replaces a pure
two-derivative axiom with a stronger task: select the full product spectral
action and prove a controlled low-energy regime in which the Einstein term
dominates and the Weyl/higher terms have a quantified error.

## Two honest exits

### Direct closure-action exit

Construct `SelectedSpacetimeClosureActionSource.v1` with:

```text
G=Q^TQ,
local diffeomorphism naturality,
at-most-second-order infrared metric equation,
computed TT Hessian and q79 zero/gap reduction,
one shared metric for matter,
Lorentzian domain, kappa_h, and Lambda_eff.
```

The closed reciprocity, Fierz-Pauli, Lovelock, and Hilbert-stress reductions then
give classical Einstein gravity.

### Spectral superset exit

Construct `SelectedProductSpectralActionAndEinsteinIRLimit.v1` with:

```text
selected four-dimensional base Dirac geometry,
selected finite product triple,
selected cutoff/proper-time measure and moments,
Lorentzian/Wick reconstruction,
absolute Newton and vacuum normalization,
q79 zero/gap TT match,
controlled suppression of Weyl and higher terms.
```

This path is attractive because it can place the already closed finite-SM
operator content and gravity in one operator architecture. It is also the
harder analytic path because its Einstein limit must be proved, not declared.

## Frontier

Closed:

- explicit nonlinear counterfamily with identical quadratic TT data;
- no-go for inferring nonlinear GR from the Hessian alone;
- logical necessity of the derivative-order or suppression theorem;
- spectral action as a genuine same-operator SM/gravity architecture;
- exact classification of what A51-A53 do and do not select.

Open:

- direct MTT selection of the local two-derivative spacetime action; or
- selected product spectral action plus controlled Einstein infrared limit;
- numerical `kappa_h`, `Lambda_eff`, Lorentzian domain, and zero/gap fusion.
