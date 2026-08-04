# MTT Selected Quark/Lepton-Resolved Positive Density Source or Kinetic Weight Emission v1

## Exact reduction

Starting from the A67 positive C1 traces, the minimal Q/L-resolved ansatz is

```text
(Q,u,d,L,e,N) = (12s,6s,6s,12,6t,6).
```

It gives `K3/K2=3s/(3s+1)`. If only the colored factor is allowed (`t=1`), elimination of
`s` proves the exact relation

```text
K1/K2 = 6/5 - (4/5)(K3/K2).
```

At the accepted color ratio this predicts `0.952130379274019`, not
`1.9568425763574`. Quark suppression alone is therefore insufficient.

## Unique two-factor reconstruction

The two independent profile ratios invert uniquely to

```text
s = 0.14964437750608711,  -log(s)/tau_int = 4.6672185544181151,
t = 3.4262679849988702,   log(t)/tau_int = 3.0258312712240567.
```

This is an exact reconstruction, not a prediction: it uses two measured profile coordinates.

## Source-native clue

The inferred costs lie strikingly close to `14/3` and `3`. With the already selected
`tau_int=log(448)/15`, those simple costs give

```text
s = 448^(-14/45), t = 448^(1/5),
K/K2 = [1.9418974820588115, 1.0, 0.30988505827302176],
relative residuals (U1,SU3) = [-0.007637351353221411, 0.00015502461464977912].
```

The SU3 residual is about `0.0155%`; the U1 residual is about `0.764%`. This is useful evidence for
a two-order source, but not closure. There is now a corpus-native factorization clue:

```text
colored cost = nil sevenfold * color-completion Schur half * C2(3)
             = 7 * (1/2) * (4/3) = 14/3,
lepton cost  = three charged-lepton basins * conjectural unit circle cost = 3.
```

The Schur half and the three-basin structure are supported, but the nil sevenfold remains a
carried-forward candidate and no theorem yet maps each charged-lepton basin to a unit positive
kinetic exponent. Therefore neither cost is yet emitted by one selected MTT operator.

Next artifact: `MTT_Selected_QuarkOrderAndSharedCircleCostSpectrum_or_TwoFactorDensityValueEmission_v1`.
