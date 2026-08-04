# One-Anchor Additive Physical-Clock Lift and q79 Rate Theorem

## Statement

On the selected `N=448` branch, the internal complement gap and admissibility
checkpoint are

```text
lambda_int=15,
tau_int=log(448)/15.
```

Let one physical metrological anchor define

```text
t0=1/E0=L0                    (c=1),
alpha_phys=tau_int E0^2=tau_int/L0^2,
tau_phys=t0^2.
```

Assume the map from noncompact physical time to heat/proper time is strongly
continuous, additive, starts at zero, and passes through the selected
checkpoint `tau(t0)=tau_phys`. Then it is uniquely

```text
tau(t)=t0 t.
```

Consequently the physical q79 cross-coherence rate is

```text
lambda_phys=15 alpha_phys,
gamma=lambda_phys t0
     =log(448)E0
     =log(448)/L0,
```

and after one coherence-clock interval

```text
exp(-gamma t0)=1/448.
```

No second clock scale is introduced beyond the one metrological primitive
already required by the GR normalization family.

## Proof

A continuous additive map from the nonnegative physical-time semigroup to the
nonnegative proper-time semigroup has the form `tau(t)=beta t`. The checkpoint
condition gives `beta=tau_phys/t0=t0`. Multiplying the normalized gap by the
physical action scale gives `lambda_phys=15 alpha_phys`. Therefore

```text
gamma=lambda_phys beta
     =15 (log(448)/15) E0^2 (1/E0)
     =log(448)E0.
```

The length-anchor expression is equivalent. Multiplying by `t0` gives
`log(448)`, and exponentiation gives `1/448` exactly.

The tempting map `tau=t^2` passes through the checkpoint but is not additive:
`(t+s)^2` is not `t^2+s^2`. It therefore cannot generate the required
time-homogeneous physical dephasing semigroup.

## Penrose Target

The remaining rate-selection equation is now

```text
E_PQ^(G,ell)/hbar = log(448)E0
```

or equivalently `log(448)/L0`. The left side still requires selected physical
branch mass profiles, `G_eff`, and external smearing. This theorem fixes the
right side and proves that the clock does not require a second continuous
parameter.

This direct equality can hold only for a selected reference context. It cannot
be universal over arbitrary mass profiles because Penrose energy varies
quadratically with their difference. General contexts require a
preparation-dependent dimensionless factor multiplying the reference rate.

## Scope

The theorem is conditional on the additive clock lift and checkpoint
identification. These conditions are mathematically sufficient and unique but
are not yet derived from upper MTT dynamics. The result does not select an
objective instrument or realized outcome.
