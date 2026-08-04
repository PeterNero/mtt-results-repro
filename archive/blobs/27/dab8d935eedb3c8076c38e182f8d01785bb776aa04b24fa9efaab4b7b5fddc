# Selected Electroweak Kernel Candidate Computation v1

## Purpose

The selected electroweak kernel interface reduced the missing data to:

```text
K_EW -> (mu_Theta, kappa_EW, Delta^sel, scheme).
```

This note computes the strongest threshold candidate currently available from
the corpus: the Execution I bulk plus exceptional threshold profile.

The result is useful, but it is not a no-knob electroweak closure. Directly
importing the Execution I threshold profile into the electroweak kernel is a
diagnostic scaffold, not a proof, because its bulk coefficient and exceptional
coefficients are not source-selected independently of gauge data.

## Source Threshold Data

Execution I gives:

```text
tau_1 = 3.8634,
tau_2 = 3.8634,
tau_3 = 0.8836.
```

The bulk threshold direction is:

```text
d_a = log(tau_a) - average(log tau).
```

Computing:

```text
d = (0.491766144075410,
     0.491766144075410,
    -0.983532288150820).
```

The Tier-3/Execution-I bulk coefficient is:

```text
delta = -25.2.
```

Therefore the alpha-inverse bulk vector is:

```text
Delta_alpha^bulk = delta d
                 = (-12.392506830700340,
                    -12.392506830700340,
                     24.785013661400670).
```

Execution I also gives the exceptional vector:

```text
Delta_alpha^exc = (0.31, -0.58, 0.27).
```

Thus:

```text
Delta_alpha^candidate
  = (-12.082506830700340,
     -12.972506830700340,
      25.055013661400668).
```

All three vectors are trace-free up to rounding, so they preserve the common
overall scale in the `alpha^{-1}` convention.

## Conversion to Kernel Convention

The electroweak kernel uses:

```text
G_a = 1/g_a^2.
```

Execution I writes thresholds in alpha-inverse convention:

```text
alpha_a^{-1} = 4pi/g_a^2 = 4pi G_a.
```

So:

```text
Delta_G = Delta_alpha / (4pi).
```

The candidate threshold vector in kernel convention is:

```text
Delta_G^candidate
  = (-0.961495343523775,
     -1.032319293199668,
      1.993814636723442).
```

## Electroweak Diagnostic

Use the Theta V ratio:

```text
r_12 = g_1^2/g_2^2 = 0.56027.
```

Choose the harmless ratio convention:

```text
zeta_2 = 1,
zeta_1 = 1/r_12.
```

For the diagnostic only, set:

```text
mu_Theta = 5000 GeV,
M_Z = 91.1876 GeV,
kappa_EW = 2.514.
```

This gives:

```text
no threshold:                 sin^2(theta_W) = 0.231213382960,
bulk threshold only:           sin^2(theta_W) = 0.181121977988,
exceptional threshold only:    sin^2(theta_W) = 0.226791123623,
bulk + exceptional threshold:  sin^2(theta_W) = 0.175124626818.
```

The direct full import is therefore not viable as an electroweak prediction.
The bulk threshold is too large in the electroweak kernel convention unless it
is reinterpreted as a high-scale profile already absorbed into the calibrated
Tier-3 data, or unless a source theorem supplies a different electroweak
projection.

## Structural Clue

The bulk direction satisfies:

```text
Delta_alpha^bulk_1 = Delta_alpha^bulk_2.
```

So the bulk component does not distinguish the first two gauge entries by
itself. The first direct `1-2` split comes from the exceptional vector:

```text
Delta_alpha^exc_1 - Delta_alpha^exc_2 = 0.89.
```

In kernel convention:

```text
Delta_G^exc_1 - Delta_G^exc_2 = 0.070823949676.
```

This is the next useful clue: electroweak splitting must come from exceptional,
localized, or representation-sensitive data, not from the symmetric bulk
threshold alone.

## Verdict

The current corpus lets us compute a candidate threshold vector:

```text
Delta_G^candidate
  = (-0.961495343523775,
     -1.032319293199668,
      1.993814636723442).
```

But this candidate is not a no-knob electroweak threshold. It is a diagnostic
import of a Tier-3/Execution-I threshold profile whose coefficients are still
calibrated or structurally fitted.

The correct next computation is therefore:

```text
derive the exceptional/local electroweak threshold coefficients from selected
topology, flux, curvature, or torsion data.
```

Equivalently, replace the imported vector above by:

```text
Delta_G^sel = ThresholdDet(selected branch)/(4pi),
```

with the determinant/torsion data selected before any electroweak comparison.
