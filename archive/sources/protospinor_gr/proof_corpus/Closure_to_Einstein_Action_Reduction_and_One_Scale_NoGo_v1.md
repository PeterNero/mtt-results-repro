# Closure to Einstein Action Reduction and One-Scale No-Go v1

Date: 2026-07-15

## Result

The chain from closure strain to classical GR can now be stated without
conflating its proved and selected parts:

```text
q79/proto-spinor carrier
  -> selected comparison field Q
  -> G=Q^T Q and e=(1/2)log G
  -> finite closure Hessian H_e=kappa_e Id
  -> metric TT Hessian H_h=(kappa_e/4)Id
  -> unique Fierz-Pauli quadratic operator
  -> unique Einstein-Hilbert nonlinear metric completion
  -> Hilbert stress tensor and Einstein equation
```

The first five arrows are already constructed at their declared tiers. The
last two arrows are now unique mathematical reductions, conditional on one
still-missing MTT source statement: the selected closure response must be a
local, diffeomorphism-natural four-dimensional spacetime action whose metric
equation has at most two derivatives in the infrared.

This is real progress over the previous four-hypothesis action gate. A separate
self-adjointness assumption is unnecessary for a genuine variational Hessian,
and a separate stress normalization is unnecessary once matter and gravity
vary with respect to one shared metric.

## 1. Hessian reciprocity is automatic on the closure slice

The revised closure-strain paper declares a real `C^3` scalar functional
`J` and a stationary point `S_*`. Therefore Schwarz symmetry gives

```text
D^2 J(S_*)[u,v] = D^2 J(S_*)[v,u].
```

On the finite six-dimensional real strain slice, define the Riesz operator by

```text
<u,Hv> = D^2 J(S_*)[u,v].
```

Then `<u,Hv>=<Hu,v>` and hence `H=H*`. This closes self-adjointness of the
finite closure Hessian. The same second-variation identity makes the Jacobi
operator of a real local spacetime action formally self-adjoint after its
boundary conditions are fixed. It does not prove that the present closure
functional has already been promoted to that spacetime action.

## 2. Nonlinear Einstein completion

Assume that the selected physical field is a four-dimensional Lorentzian
metric and that its metric equation is:

1. local and diffeomorphism-natural;
2. symmetric and identically divergence-free;
3. built from the metric and at most its first two derivatives; and
4. metric-only in the infrared gravitational sector.

The four-dimensional Lovelock classification then leaves only

```text
a G_mn + b g_mn.
```

Matching the nonzero quadratic term to the already computed unique
Fierz-Pauli block gives the dynamically unique action

```text
S_grav = 2 kappa_h integral sqrt(-g) (R - 2 Lambda),
```

up to boundary terms and four-dimensional topological densities. This is the
nonlinear Einstein-Hilbert completion, not yet an MTT selection of its
hypotheses. Lovelock's original classification is
<https://doi.org/10.1063/1.1665613>. Deser's independent self-coupling route
shows how locality and consistent coupling of the linear gauge current generate
the Einstein nonlinearity: <https://arxiv.org/abs/gr-qc/0411023>.

`Lambda` is permitted but not selected here. Flat-background expansion requires
the total vacuum tadpole to cancel; cosmology requires an independent selected
vacuum-energy result.

## 3. Stress and exact normalization

For all retained matter fields `Phi` coupled to the same metric, define

```text
T_mn = -(2/sqrt(-g)) delta S_matter/delta g^(mn).
```

Using

```text
delta S_matter
  = -(1/2) integral sqrt(-g) T_mn delta g^(mn),
```

variation of the common action gives

```text
G_mn + Lambda g_mn = (4 kappa_h)^(-1) T_mn.
```

The repository convention is

```text
kappa_h       = 1/(32 pi G4),
2 kappa_h     = 1/(16 pi G4),
(4 kappa_h)^-1 = 8 pi G4.
```

Thus the standard Einstein equation follows exactly. Diffeomorphism invariance
of the matter action and the matter equations give `nabla^m T_mn=0`; the
contracted Bianchi identity enforces the same compatibility. No extra
gravitational stress coefficient remains beyond `kappa_h`. The open physical
point is whether one MTT-selected action couples every retained sector to this
same metric.

## 4. q79 reduction and the unavoidable scale

For the unwarped product reduction of the declared ten-dimensional ansatz,

```text
S10 = (2 kappa10^2)^(-1) integral sqrt(|g10|) R10,
```

the normalized constant internal mode gives

```text
V6/(2 kappa10^2) = 2 kappa_h,
kappa_h = V6/(4 kappa10^2)
        = V6/(32 pi G10),
G4 = G10/V6.
```

Warping, a nonconstant dilaton, higher-curvature terms, or threshold corrections
replace `V6` by a weighted overlap. They do not invalidate the need to compute
that overlap from the selected action.

There is now an exact no-go for extracting Newton's constant from the currently
closed scale-free q79 packet alone. Under an internal homothety

```text
g_X -> r^2 g_X,
V6 -> r^6 V6,
phi0 -> r^-3 phi0,
```

the topology, connectedness, rank-one harmonic projector, and unit normalized
internal residue remain unchanged, while at fixed parent coupling

```text
kappa_h -> r^6 kappa_h.
```

Therefore those closed data cannot select a numerical `kappa_h`. At least one
dimensionful primitive or an equivalent metric-scale theorem is necessary.
Writing

```text
V6  = v6 ell_*^6,
G10 = g10 ell_*^8
```

gives

```text
kappa_h = [v6/(32 pi g10)] ell_*^-2.
```

One length primitive is sufficient only after the full source selects the
dimensionless ratio `v6/g10`. From the four-dimensional point of view,
`kappa_h`, equivalently `V6/G10`, is one effective normalization.

## 5. Theta IV reconciliation

Theta IV was right to isolate one effective gravitational normalization. Its
specific calculation cannot remain a proof source because it uses the retired
literal `S1_cen x Sigma2 x Sigma3` geometry and obtains
`V=31.8 R1^3`, rather than the weighted six-volume of the active q79 branch.

Retain:

```text
G4^-1 = V6/G10
```

as a conditional dimensional-reduction relation.

Replace:

```text
V6 = 31.8 R1^3
```

with the selected q79 weighted overlap on
`X6_q79=P_delta x S1_shared`. Until that metric/action calculation is emitted,
the numerical Newton prediction remains open.

## 6. Exact remaining source packet

The next proof object is no longer an unspecified GR bridge. It is
`SelectedSpacetimeClosureActionSource.v1`, containing:

```text
physical_metric       = G=Q^TQ on Lorentzian Y4
naturality             = J4[f*G,f*Phi]=J4[G,Phi]
local_IR_order         = at most second-order metric equation
quadratic_match        = D2J4|E_TT = kappa_h Fierz-Pauli
internal_reduction     = weighted q79 zero/gap overlaps
matter_map             = one shared metric for all retained sectors
Lorentzian_domain      = time orientation, gauge, boundary domain
scale                  = selected V6/G10 or one-primitive equivalent
vacuum_energy          = selected Lambda_eff or cancellation theorem
```

Once this packet is sourced, Lovelock and the variation above supply the full
classical Einstein equations, their nonlinear completion, universal Hilbert
stress coupling, and conservation law. Quantum gravity remains a separate
program.

## Claim boundary

Closed now:

- finite closure-Hessian self-adjointness;
- reduction of the physical self-adjointness hypothesis to variational origin;
- unique nonlinear Einstein completion under the explicit Lovelock hypotheses;
- exact Hilbert stress and Newton coefficient relations;
- no independent stress-normalization knob beyond `kappa_h`;
- the scale-free q79-to-numerical-Newton no-go;
- structural retention and numerical correction of Theta IV.

Still open:

- MTT selection of the local diffeomorphism-natural spacetime action;
- MTT selection of the two-derivative infrared order;
- the weighted q79 reduction and zero/gap action coefficients;
- the numerical value of `kappa_h` or `G4`;
- `Lambda_eff`, Lorentzian domain data, and the quantum theory.
