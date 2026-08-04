# QFT02 Diffeomorphism-Transported Regulator-Orbit Assessment

Date: 2026-07-24

## Decision

The diffeomorphism freedom already declared by the selected q79 coframe has
now been propagated through the full linear BV regulator and its boundary
package.

The result closes two presentation directions:

```text
1. spin-liftable chart diffeomorphisms equal to the identity on a
   boundary collar;

2. ambient-isotopic rounded regions when the metric, coframe, faithful
   bundle, BV fields, boundary operator and boundary polarization are
   all transported together.
```

The second direction is stronger than the earlier boundary-fixed path, but it
is still a covariance theorem. It does not identify physically different
geometries.

## Exact Chain

For the induced bulk and boundary unitaries:

```text
Q_t         = U_t Q_0 U_t^-1;
Delta_t     = U_t Delta_0 U_t^-1;
trace_t U_t = V_t trace_0;
A_t         = V_t A_0 V_t^-1;
P_APS,t     = V_t P_APS,0 V_t^-1.
```

Consequently:

```text
C_Lambda,t  = U_t C_Lambda,0 U_t^-1;
h_t         = U_t h_0 U_t^-1;
L_UV,t      = U_t L_UV,0;
Dom_t       = U_t Dom_0.
```

After pullback by `U_t` and `V_t`, all bulk and boundary data are constant.
This gives exact relative results:

```text
APS spectral flow = 0;
BV-BFV flux       = 0;
eta spectrum      = constant;
shell determinant = constant;
free pushforward  = canonically equivalent.
```

## Why the Moving-Boundary Case Is Not Trivial

The exact certificate uses a nonidentity rational boundary unitary. The raw
boundary displacement and raw APS projector both change. The induced boundary
unitary then returns them exactly to their initial values.

Thus the proof does not silently assume a fixed boundary. It verifies the
correct relative comparison for a transported boundary.

The certificate also retains a separate based-collar witness, where the
boundary unitary is literally the identity and the interior transform is
nontrivial.

## Corrected Region-Shape Status

The previous status row listed "region shape or embedding" as one undivided
open coordinate. It now splits:

```text
ambient-isotopic pushforward of the full source package:
  closed as presentation;

shape change in a fixed background, nonisometric deformation,
nonisotopic embedding or untransported boundary data:
  open as genuine quotient data.
```

This is a strict reduction of the regulator quotient, not a relabeling of the
same open problem.

## Extended Quotient

The presentation group is now:

```text
Diff_spin,0^+
  semidirect
(
  based faithful gauge
  x residual liftable frame
  x compactly supported BV gauge fixing
).
```

The remaining regulator problem lives on:

```text
R_admissible / G_presentation_extended.
```

Its open coordinates are:

```text
nonisotopic or nontransported region embeddings;
nonisometric positive metrics modulo diffeomorphism/frame gauge;
nontransported Cauchy-normal or Euclideanization choices;
nontransported boundary/BFV polarizations;
inequivalent spin structures and disconnected domains;
nonconjugate crossings and crossing torsion;
uniform interacting cutoff removal.
```

## Objective Status

This does not yet supply a preferred physical regulator or a nonperturbative
continuum limit. It proves that a broad class of apparent regulator choices
are only q79 presentation choices and can be quotiented out exactly.

The next useful target is the first genuinely geometric quotient direction:
either prove controlled independence under relative-collar positive-metric
deformation, including crossings and determinant data, or derive a q79
selection principle for one metric/boundary-polarization class.

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
certificates/q79_sm_diffeomorphism_transported_regulator_orbit.certificate.json
```
