# q79 SM Based-Gauge/Frame Regulator-Orbit Independence and Quotient Cutset Theorem v1

Date: 2026-07-24

## Verdict

An actual q79-sourced regulator path has now been constructed.

On the rounded compact chart `X`, take:

```text
R_t: liftable residual spatial-frame path,
g_t: faithful internal gauge path,
R_t=g_t=1 on a collar of boundary(X).
```

Their spin/faithful representations give a unitary path `U_t` on the full
linear Standard-Model BV complex. Its cotangent lift satisfies

```text
Q_t = U_t Q_0 U_t^-1,
Delta_t = U_t Delta_0 U_t^-1.
```

Because `U_t` is literally the identity on the boundary collar:

```text
A_boundary(t) = A_boundary(0),
P_APS(t)      = P_APS(0),
spectral flow = 0,
BFV flux      = 0.
```

All finite Hodge projectors, Hodge Lagrangian cycles and free finite-shell
QME pushforwards are canonically transported. The eta spectrum and
determinant half-density are constant under this unitary conjugation.

Thus regulator independence is closed on the connected, boundary-identity
q79 gauge/frame **presentation orbit**. It is not closed between inequivalent
points of the quotient

```text
R_admissible / G_0,boundary.
```

No physical parameter, selector, fit or observed value is added.

## 1. Why this path is selected rather than invented

The hash-pinned q79 coframe certificate states:

```text
global coframe:
  closed up to diffeomorphism and local Lorentz gauge;

Q_WW spatial solder:
  closed up to diffeomorphism and frame gauge.
```

Its adapted representative is

```text
theta^0 = N dt,
theta^a = Q_WW^a_i (dx^i + N^i dt).
```

Once the Cauchy normal and time orientation are fixed, the compact residual
frame gauge is spatial `SO(3)`, with lift `Spin(3)`. Spatial rotations leave
the auxiliary positive metric

```text
g_E = sum_a theta^a tensor theta^a
```

unchanged. The faithful Standard-Model bundle independently has its usual
unitary gauge action.

The local regulator theorem already restricts infinitesimal gauge
transformations to the based group at the artificial boundary. Requiring the
frame path to be the identity on the same collar is the corresponding spin
condition. It preserves the physical fields while preventing the regulator
wall from acquiring new boundary data.

## 2. Presentation group

Define

```text
G_0,boundary =
  Gauge_0(P; boundary)
  x Frame_0^Spin(3)(X; collar)
  x BVCan_c(X interior).
```

The three factors are:

1. identity-component faithful internal gauge transformations equal to one
   on the collar;
2. liftable residual spatial-frame transformations equal to one on the
   collar;
3. compactly supported BV gauge-fixing canonical transformations.

The first two act by unitary bundle maps. Fields and ghosts transform in
their declared representations; antifields transform by the cotangent dual.
The third is the already certified compactly supported change of
gauge-fixing fermion.

Large nonliftable frame changes, inequivalent spin structures and
disconnected domain data are outside this group.

## 3. Full-BV conjugation theorem

Let `U_t` be the field/ghost unitary induced by `(R_t,g_t)` and its cotangent
lift on antifields. Then

```text
omega(U_t x,U_t y) = omega(x,y).
```

Gauge covariance of the de Rham, Yang-Mills, Higgs and Weyl rows gives

```text
Q_t U_t = U_t Q_0.
```

The adjoints obey the same relation because `U_t` is unitary. Hence

```text
Delta_t U_t = U_t Delta_0.
```

Functional calculus therefore gives, for every cutoff,

```text
C_Lambda(t)
  = 1_[0,Lambda](Delta_t)
  = U_t C_Lambda(0) U_t^-1.
```

The spectrum and projector ranks are constant. On a positive finite shell,

```text
h_t = U_t h_0 U_t^-1,
L_t = U_t im(Q_0^dagger).
```

Consequently the Hodge contraction, BV pairing and nondegenerate shell
quadratic form are preserved exactly.

## 4. Boundary theorem

The boundary trace satisfies

```text
Tr_boundary U_t = Tr_boundary.
```

Therefore:

- relative gauge/ghost data are unchanged;
- Dirichlet Higgs data are unchanged;
- the adapted chiral boundary operator is unchanged;
- its negative APS projector and complementary adjoint projector are
  unchanged;
- field and antifield boundary-Green domains are unchanged.

Since the entire path of boundary operators is constant,

```text
sf(A_boundary(t)) = 0.
```

This is stronger than cancellation of several crossings: no boundary
crossing occurs.

## 5. BV-BFV flux

The bulk BV symplectic variation normally leaves boundary BFV data. Here the
boundary displacement is

```text
delta_boundary = Tr_boundary (U_t-1) = 0.
```

Thus the induced variation of the boundary symplectic potential and BFV
polarization is zero. In particular,

```text
Flux_BFV(U_t) = 0.
```

No compensating boundary action or counterterm is required on this orbit.
This conclusion would fail for transformations that act nontrivially on the
collar.

## 6. Determinant transport

For every open based path, the chiral operators and positive Hodge squares
are unitarily conjugate. Their singular spectra, boundary eta spectra and
finite-shell determinants are constant. The unitary itself gives the
canonical map between determinant-line fibers.

For closed faithful internal-gauge loops, the prior result

```text
Omega_5^Spin(B((SU3 x SU2 x U1)/Z6)) = 0
```

removes the declared spin global gauge-anomaly bordism obstruction. The
local anomaly vector also vanishes.

A spatial-frame path can have two Spin lifts differing by the central sign.
That sign is fermion parity. The declared physical q79 observable net is the
fermion-parity-even subnet, so the two lifts induce the same physical
observable map.

This proves canonical transport on the declared presentation orbit. It does
not select a preferred standalone numerical phase for an unnormalized
partition function.

## 7. Free and formal-interacting consequences

The preceding finite-shell theorem now applies to an actual q79 path:

```text
P_*^(t) = U_t P_*^(0) U_t^-1
```

on BV cohomology, with the determinant half-density transported by `U_t`.
Hence the free finite-shell effective theories agree.

Compactly supported gauge-fixing changes are already known to act by quantum
BV canonical maps on the formal interacting physical cohomology. Combining
that result with the gauge/frame conjugation proves presentation independence
of the formal physical algebra.

This is not a fixed-nonzero-coupling C*-limit or nonperturbative interacting
path integral.

## 8. Exact finite witness

The certificate separates one boundary and one interior contractible BV
block with Hodge eigenvalues `1` and `4`. It applies

```text
R =
[ 3/5 -4/5 ]
[ 4/5  3/5 ]
```

to the interior field and antifield rows while acting as the identity on the
boundary block.

It verifies exactly over the rationals:

```text
U^T U = I,
U^T omega U = omega,
det U = 1,
Tr_boundary U = Tr_boundary,
Q_1 = U Q_0 U^-1,
Delta_1 = Delta_0,
C_Lambda(1) = C_Lambda(0),
P_APS(1) = P_APS(0),
Flux_BFV = 0.
```

The Hodge-cycle quadratic determinant is

```text
det H_shell = 4
```

at both endpoints.

## 9. Quotient cutset

The regulator selection problem is no longer allowed to count frame gauge,
based faithful gauge or compactly supported gauge-fixing coordinates as
physical choices.

The genuine remaining quotient coordinates are:

```text
rounded-region shape or embedding;
positive metric beyond residual frame gauge;
Cauchy-normal or Euclideanization choice;
boundary-condition/BFV-polarization class;
inequivalent spin structure or disconnected domain data;
nonconjugate spectral crossings and crossing torsion;
uniform interacting cutoff removal.
```

The next comparison theorem should work on a fixed region and fixed product
collar while varying the interior positive metric. That is the first
non-presentation direction in the quotient.

## 10. Frontier

Closed now:

```text
actual q79 regulator path:
  connected boundary-identity gauge/frame orbit;

APS spectral flow on that path:
  exactly zero;

BV-BFV boundary flux:
  exactly zero;

determinant transport:
  canonical on open paths and physical even observables;

free finite-shell pushforward:
  orbit independent;

formal interacting physical cohomology:
  presentation independent.
```

Still open:

```text
independence between inequivalent quotient-moduli points;
relative-collar interior metric deformation;
nonconjugate crossing stabilization;
uniform interacting regulator removal;
fixed-coupling gauge-BRST C*-completion and selected state.
```

`B.QFT.02` remains open overall, but three components of the prior obstruction
vector are now exactly zero on the actual q79 presentation orbit.

## 11. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The path coordinates are gauge/presentation coordinates and disappear in
the quotient.

## 12. External theorem boundary

Bulk-to-boundary typing follows the
[classical BV-BFV framework](https://arxiv.org/abs/1201.0290), while
finite/family pushforward and change-of-data control use the
[quantum BV-BFV construction](https://arxiv.org/abs/1507.01221).
Determinant-line and eta transport use
[Dai and Freed](https://arxiv.org/abs/hep-th/9405012). The faithful Standard
Model global-anomaly guard uses
[Davighi, Gripaios and Lohitsiri](https://arxiv.org/abs/1910.11277).

These results do not prove independence under changes of region, positive
metric or boundary-polarization class.

## 13. Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_sm_based_gauge_frame_regulator_orbit.certificate.json
```
