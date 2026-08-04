# MTT Selected Axion-Quality Instanton Suppression Bound v1

## Exact quality theorem

Write

```text
V(theta)=chi_QCD[1-cos(theta+theta_bar)] + DeltaV(theta),
DeltaV=-sum_j Lambda_j^4 cos(n_j theta+delta_j).
```

Define

```text
M0=sum Lambda_j^4,
M1=sum |n_j| Lambda_j^4,
M2=sum n_j^2 Lambda_j^4.
```

For a tolerance `epsilon`, the three exact sufficient inequalities are

```text
M1 < chi_QCD sin(epsilon),
M2 < chi_QCD cos(epsilon),
2 M0 < chi_QCD [1+cos(epsilon)].
```

They imply that the unique global minimum satisfies
`dist(theta+theta_bar,2*pi*Z)<epsilon`. This is not a small-angle
linearization: derivative signs exclude all stationary points outside the
zero and opposite-point neighborhoods, strict convexity fixes the zero
neighborhood, and the `M0` bound excludes the opposite point globally.

## What closes

The selected heterotic gerbe gauge symmetry makes the perturbative local
potential for the universal axion exactly zero. The q79 order-three gerbe has
de Rham `H=0` and neither helps nor harms this continuous mode. Thus the
perturbative quality subproblem is closed, and the full nonperturbative test is
now executable once its source values are supplied.

## What remains

The current corpus does not emit the selected hidden gauge spectrum,
confinement/instanton scales, anomaly harmonics, wrapped NS5 cycle and action,
worldsheet-instanton table, prefactors, or phases on the same q79 branch. That
payload is `0/9`. A brane-tension formula alone is insufficient without the
selected volume and coupling.

For orientation only, a one-instanton prefactor at `10^16`--`10^17 GeV` would
need an action of roughly `181`--`190` for `epsilon=1e-10`; those numbers use
external QCD/scale benchmarks and are not MTT predictions.

U6 remains `9/10`, with zero new continuous parameters.

Next artifact: `MTT_Selected_q79HiddenGaugeAndNS5InstantonActionPacket_v1`.
