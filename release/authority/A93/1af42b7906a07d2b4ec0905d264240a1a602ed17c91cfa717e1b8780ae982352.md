# MTT Selected Neutral LensNil Determinant-Holonomy Execution or One-Scale Finality v1

## Determinant type correction

The neutral factorization uses the ordinary determinant line of the rank-three
family bundle:

```text
det(E_nu)=Lambda^3 E_nu,
Hol_det(E_nu)(gamma)=det H_nu=exp(3 i phi_nu).
```

This is not, by definition, the analytic Quillen/Bismut--Freed line `Det(D_nu)`
of a family of chiral Dirac operators. The latter has an eta/mapping-torus
holonomy. No current index or transgression theorem identifies these two lines.
Therefore the APS route is retained as future mathematics but retired as a
direct source for `phi_nu` in the current proof chain.

## Exact one-coordinate finality

Fix the selected traceless family connection `A0` with holonomy `H_cen`. For a
closed one-form `alpha_gamma` normalized by `integral_gamma alpha_gamma=1`, every

```text
A_phi = A0 + i*phi*alpha_gamma*I3
```

has the same curvature and relative `SU(3)` holonomy, while

```text
Hol(A_phi)=exp(i phi) H_cen,
det Hol(A_phi)=exp(3 i phi).
```

Thus the existing topology, curvature, qutrit and `H_cen` data admit every
`phi` modulo `2*pi/3`. They cannot select its value. Conversely the determinant
recovers exactly that one scalar, so one central holonomy coordinate is both
necessary and sufficient.

The corpus explicitly lists Wilson-line/flat-connection phases as the open
flavor bottleneck. Cross-repo source audits do not select the q64 character or
LensNil flux integers as this neutral local system. This proves current-corpus
finality, not a no-go for a future MTT action that uniquely minimizes the
central holonomy.

## One-holonomy plus one-scale profile

For the massless normal-ordering three-basin profile,

```text
r = 2*sqrt(3)*tan(phi)/(3+sqrt(3)*tan(phi)),
phi = atan(sqrt(3)*r/(2-r)).
```

At the A40 profile, `r=0.029805013927576604` gives
`phi=0.02619638630300379`, reproducing A40 with residual
`0.0`. Once `phi` and one dimensionful splitting
scale are supplied, all 36 A40 mass/Yukawa/matrix rows follow. This replaces two
measured splitting coordinates by one geometric phase and one scale, so the
profile count is unchanged at two; it is a structural compression, not a new
parameter-count reduction.

U5 is now closed at the explicit **one neutral holonomy primitive plus one
absolute scale** profile standard. Strict no-knob U5 remains open, as do the
selected absolute scale, Dirac-only completeness, Majorana exclusion, ordering
selection and covariance. A41's `pi/120` remains an optional target-ranked
benchmark, not the selected value.

No new parameter was added.

Next artifact: `MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1`.
