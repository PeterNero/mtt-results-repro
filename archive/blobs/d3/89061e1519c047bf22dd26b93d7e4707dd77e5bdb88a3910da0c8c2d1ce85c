# QFT02 Based Gauge/Frame Regulator-Orbit Assessment

Date: 2026-07-24

## Decision

The previous finite-shell theorem compared arbitrary regulator endpoints only
after an admissible gapped path and compatible boundary transport were
supplied. This assessment supplies the first such path class from selected q79
geometry itself.

The result closes regulator independence on the connected presentation orbit

```text
G_0,boundary
  = based faithful internal gauge paths
  x liftable residual spatial-frame paths
  x compactly supported BV gauge-fixing canonical maps.
```

It does not close independence between inequivalent points of the regulator
quotient.

## Selected Source

The pinned q79 Lorentzian coframe certificate gives the adapted split

```text
theta0 = N dt,
thetaa = Q_WW^a_i(dxi + N^i dt),
```

with the spatial soldering closed up to diffeomorphism and frame gauge. On the
rounded auxiliary chart, choose a liftable residual `Spin(3)` frame path
`R_t` and a faithful `S(U(3) x U(2))` gauge path `g_t`, both equal to the
identity on a collar of the artificial boundary.

Their unitary representation and cotangent BV lift define

```text
U_t = rho_spin(R_t) tensor rho_faithful(g_t),
Q_t = U_t Q_0 U_t^-1,
Delta_t = U_t Delta_0 U_t^-1.
```

These are presentation changes already licensed by the selected coframe and
bundle data. They introduce no physical parameter.

## Exact Consequences

Since `U_t|boundary=1`, all boundary restrictions are literally constant:

```text
A_boundary(t) = A_boundary(0),
P_APS(t)      = P_APS(0),
Dom(t)        = Dom(0).
```

It follows that:

```text
APS spectral flow             = 0;
BV-BFV boundary displacement  = 0;
BV-BFV boundary flux          = 0;
finite Hodge cycles           = canonically transported;
finite shell determinants     = invariant;
free finite-shell pushforward = equivalent.
```

Dai-Freed transport supplies the canonical determinant-line identification on
open paths. For faithful internal gauge loops, the previously certified
vanishing Standard-Model spin-bordism obstruction removes the corresponding
global gauge-anomaly obstruction. A central sign from a spatial Spin lift is
invisible on the declared fermion-parity-even observable net. No preferred
absolute partition-function phase is asserted.

## Exact Finite Witness

The certificate contains an eight-dimensional rational BV witness with one
boundary and one interior contractible block. The interior block is rotated by

```text
U_int = [[3/5, -4/5],
         [4/5,  3/5]]
```

on both fields and antifields, while the boundary block is fixed. Exact
rational arithmetic verifies:

```text
U^T U = I;
U^T omega U = omega;
det(U) = 1;
trace_boundary U = trace_boundary;
Q_1 = U Q_0 U^-1;
Delta_1 = Delta_0;
Flux_BFV = 0;
det(H_shell,0) = det(H_shell,1) = 4.
```

This witness verifies the algebraic mechanism. The q79 coframe and faithful
bundle certificates supply its geometric path class.

## What Is Closed

```text
actual q79-sourced connected regulator path class;
zero APS flow on that path class;
zero BV-BFV flux on that path class;
canonical Hodge-cycle and determinant transport;
free finite-shell QME-pushforward independence on the orbit;
formal physical-cohomology presentation independence.
```

## Quotient Cutset

The correct remaining regulator space is

```text
R_admissible / G_0,boundary.
```

The theorem removes gauge, residual-frame and compactly supported
gauge-fixing coordinates. It does not identify:

```text
rounded region shape or embedding;
positive metric outside the residual-frame orbit;
Cauchy normal or Euclideanization;
boundary condition or BFV polarization class;
inequivalent spin structure or disconnected-domain data;
nonconjugate spectral crossings and crossing torsion;
uniform interacting cutoff removal.
```

These are now the genuine regulator-selection coordinates. Treating any of
them as a mere gauge path would overstate the result.

## Remaining QFT02 Exit

`B.QFT.02` remains open overall. The next regulator theorem should select one
point, or prove independence on a connected component, of the quotient above.
After that, the main analytic obligation is a uniform interacting
cutoff-removal theorem leading to a fixed-coupling gauge-BRST completion and
physical state.

This result is therefore a strict frontier advance: the prior five-part path
obstruction is solved on the full connected presentation orbit, and the
selection problem has been reduced to quotient-level geometry.

## Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

## Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Machine-readable certificate:

```text
certificates/q79_sm_based_gauge_frame_regulator_orbit.certificate.json
```
