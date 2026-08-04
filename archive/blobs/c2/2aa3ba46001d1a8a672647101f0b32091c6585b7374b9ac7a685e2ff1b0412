# q79 Cauchy-Slice Quantum Kinematics and Dynamics Source Cutset Theorem v1

Date: 2026-07-23

Status:
`SELECTED_CAUCHY_FINITE_SYMBOL_HILBERT_FUNCTOR_CLOSED_EXACT_PHYSICAL_PROPAGATOR_AND_LAB_COMPARISON_OPEN`

## 1. Scope and source control

This theorem uses three already selected objects:

1. `A_QG`, the adopted q79/Z64/Q_WW finite-root-stack Lorentzian
   realization;
2. `A_causal`, its one binary time-orientation and retarded-boundary mark;
3. the exact q79 finite carrier
   \[
   F_{\rm q79}=L_{\rm sh}\otimes_{\mathbb R}
   (\mathbb R^3_D\oplus\mathbb R^3_E)
   \]
   with the parallel projectors
   \[
   P=P_{\rm Haar},\qquad Q=I-P.
   \]

The selected Lorentzian closure supplies
\[
Y^4\simeq\mathbb R\times\Sigma^3
\]
and a global coframe up to diffeomorphism and local Lorentz gauge. Its
restriction to a spacelike Cauchy support gives a positive Riemannian metric
`h` and volume measure `dmu_h`.

This note does not use the A52 profile product triple. A52 explicitly imports
its four-dimensional spin triple and Wick dictionary, so it cannot be used as
an MTT source theorem for the construction below.

## 2. The selected Cauchy finite-symbol system

Let `F_Sigma -> Sigma` be the rank-six complex finite-symbol associated bundle
in the selected q79 gauge class. No frame or sheet ordering is chosen. Define
\[
\mathcal H_\Sigma
 =L^2(\Sigma,d\mu_h;F_\Sigma).
\]

On this Hilbert space define
\[
P_\Sigma=I_{L^2}\otimes P,\qquad
Q_\Sigma=I-P_\Sigma.
\]
Because `P` and `Q` are parallel Hermitian projectors, these definitions are
independent of local q79 frames. They obey
\[
P_\Sigma^2=P_\Sigma=P_\Sigma^*,\qquad
Q_\Sigma^2=Q_\Sigma=Q_\Sigma^*,\qquad
P_\Sigma Q_\Sigma=0.
\]

The exact kinematic package is:

- the state cone
  \[
  \mathfrak S_\Sigma
  =\{\rho\in\mathcal T_1(\mathcal H_\Sigma):
      \rho\geq0,\ \operatorname{Tr}\rho=1\};
  \]
- the ambient algebra `B(H_Sigma)`;
- the finite-local decomposable algebra
  \[
  \mathfrak A_{\rm dec}
  =L^\infty(\Sigma,\operatorname{End}F_\Sigma);
  \]
- its effects `0 <= E <= I`; and
- the global dimensionless unitary group
  \[
  U_\Sigma(s)
  =P_\Sigma+e^{-is}Q_\Sigma.
  \]

This is global on the Cauchy support. It is not merely a copy of `C^6` at one
unspecified base point.

## 3. Exact gauge comparison functor

Form the selected Cauchy/q79 gauge groupoid:

- an object is a representative
  \[
  (\Sigma,h,F_\Sigma,P_\Sigma,Q_\Sigma);
  \]
- a morphism is an orientation-preserving diffeomorphism carrying `h` to
  `h'`, together with a fiberwise unitary q79 gauge map intertwining `P` and
  `Q`.

Assign each object its `H_Sigma` and each morphism `(phi,u)` the pull-push map
\[
(\mathcal U_{\phi,u}\psi)(x)
 =u_x\,\psi(\phi^{-1}x).
\]
The change-of-variables formula for the coframe-induced measures and the
fiberwise unitarity of `u` give
\[
\|\mathcal U_{\phi,u}\psi\|_{h'}
=\|\psi\|_h.
\]
Composition and identities are inherited from composition of diffeomorphisms
and bundle maps. Moreover,
\[
\mathcal U_{\phi,u}P_\Sigma
=P_{\Sigma'}\mathcal U_{\phi,u},\qquad
\mathcal U_{\phi,u}Q_\Sigma
=Q_{\Sigma'}\mathcal U_{\phi,u}.
\]
The same relation holds for `U_Sigma(s)`. Thus this is an exact functor to
Hilbert spaces with zero comparison error at the finite-symbol tier.

This functor compares gauge representatives. It does not map laboratory
preparations to states or detector settings to effects and instruments.

## Theorem A: Cauchy finite-symbol quantum kinematics

After `A_QG` and `A_causal`, the selected Lorentzian coframe and q79 finite
carrier canonically determine, up to the declared gauge groupoid:

1. a global Cauchy-slice Hilbert space for the finite-symbol sector;
2. its normal state cone;
3. its decomposable finite-local observable/effect algebra;
4. the global lift of the normalized q79 Hessian projectors and dimensionless
   unitary flow; and
5. an exact gauge comparison functor.

The construction introduces no continuous or discrete numerical parameter and
uses no observed value.

## 4. Why this does not yet select physical dynamics

The normalized Hessian fixes the operator shape `Q`, not the conversion from
its parameter `s` to physical time. Every
\[
H_\omega=\omega Q_\Sigma,\qquad\omega>0,
\]
has the same normalized q79 Hessian shape. The physical rate `omega` is not
fixed by the projector identities.

There is a second, independent issue. The internal q79 generator does not
select spatial propagation. An exact two-cell Galerkin witness is enough to
prove nonuniqueness. Let
\[
K=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
On `R^2 tensor F_q79`, both
\[
H_0=I_2\otimes Q,\qquad
H_1=I_2\otimes Q+K\otimes I_6
\]
are self-adjoint and preserve the same `P/Q` sectors. Nevertheless,
\[
\operatorname{rank}H_0=8,\qquad
\operatorname{rank}H_1=10.
\]
They therefore generate inequivalent dynamics while satisfying the same
finite q79 projector and gauge constraints. This is a source nonuniqueness
proof, not a proposal to replace the continuum by two cells.

The previously proved q79 dephasing semigroup lifts pointwise to the Cauchy
state cone. The additive one-anchor clock theorem conditionally fixes its
reference coefficient `log(448)` without a second clock knob. Upper MTT has
not selected that clock lift, the context rate, or the same-action
preparation/apparatus source, so this conditional reduced dynamics is not a
strict source closure.

## Theorem B: dynamics source cutset

The data
\[
(\Sigma,h,F_\Sigma,P_\Sigma,Q_\Sigma)
\]
select Cauchy kinematics but do not select:

1. a physical inter-slice propagator;
2. a spatial kinetic law and its domain;
3. a preparation-to-state map; or
4. a detector-setting-to-effect/instrument map.

At least one additional typed source object is necessary. A sufficient single
object is

```text
SelectedCauchyDynamicsAndLaboratoryComparison.v1
```

with:

```text
state-space scope: finite-symbol or continuum HYM,
self-adjoint Hamiltonian or CPTP generator and domain,
physical clock/metrology map,
Cauchy propagator with composition and covariance,
preparation -> state map,
setting -> effect/instrument map,
exactness or error certificate.
```

These rows should descend from one selected physical action and apparatus
interface. They are not seven independent fit parameters.

## 5. Type boundary

The theorem closes a global Cauchy system for the selected finite-symbol
sector. It does not claim:

- the nonzero-Chern inverse-Fourier-Mukai/HYM continuum state space;
- a Fock space or local QFT;
- that compact shared-circle phase is physical time;
- that the gauge comparison functor is an empirical comparison functor; or
- that A52's imported profile product triple has become source-derived.

The continuum-HYM upgrade remains tied to the HYM/Fourier-Mukai frontier. The
physical dynamics and laboratory interface are the direct `B.QM.02` exit.

## 6. Frontier delta

Before this theorem, only fiberwise `C^6` kinematics and a dimensionless
internal flow were certified. After it, the selected Lorentzian branch and
finite q79 carrier have an exact global Cauchy-slice Hilbert/state/observable
construction and a zero-error gauge comparison functor.

`B.QM.02` remains open, but "find a global Hilbert space" is no longer the
undifferentiated blocker. The open object is now the selected physical
propagator plus the same-action laboratory comparison interface.
