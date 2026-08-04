# Selected Local Determinant Computation Interface v1

## Purpose

The previous reduction left a single live electroweak C1 source:

```text
selected index-weighted local determinant response.
```

This note closes the executable accounting for that source.  It does not
compute the selected spectra.  It specifies exactly what spectral data must be
supplied, how it is turned into the determinant response, and how the result
feeds the existing electroweak C1 response calculator.

## Determinant Accounting

For each gauge factor

```text
a in {U1, SU2, SU3},
```

let the selected local threshold operator have positive eigenvalues
`lambda_{a,j}`, multiplicities `m_{a,j}`, and representation/index weights
`w_{a,j}`.  The determinant response per selected C1 unit is:

```text
p_a = sum_j m_{a,j} w_{a,j} log(lambda_{a,j}/mu^2).
```

The universal trace is irrelevant to the weak split.  The live scalar is:

```text
lambda_12 = p_U1 - p_SU2.
```

The already closed C1 bridge then gives:

```text
Delta_G_12 = v1_tilde lambda_12/(4 pi).
```

## Executable Interface

The calculator is:

```text
scripts/compute_selected_local_determinant_response.py
```

The open input template is:

```text
certificates/selected_local_determinant_spectrum.template.json
```

It accepts:

```text
selected_local_determinant:
  reference_scale_squared: positive real
  gauge_factor_spectra:
    U1:
      - eigenvalue: positive real
        multiplicity: real
        index_weight: real
    SU2:
      - ...
    SU3:
      - ...
```

The script refuses to compute if any gauge-factor spectrum is absent.

## Source Alignment

The finite-projection corpus supplies the spectral/heat-kernel language:

```text
K_int(z,z';tau) = sum_j exp(-tau mu_j^2) phi_j(z) phi_j^*(z')
```

and emphasizes that finite coherent kernels depend on geometry, topology,
boundary conditions, and bundle structure before taking a delta-shadow limit.

Theta II supplies explicit Nil scalar Laplacian formulas and lower-bound
structure, so there is a valid mathematical home for spectra.  But scalar
Laplacian bounds are not yet the gauge-factor-resolved determinant table.

Topology supplies the group-theoretic weights and multiplicities.  It does not
alone supply the finite determinant amplitude.

## No-Knob Discipline

The spectral table must be selected before electroweak comparison.  It may use
selected topology, flux, boundary conditions, bundle connections, and operator
spectra.  It may not be chosen to reproduce:

```text
sin^2(theta_W),
alpha_EM,
lambda_12,
Delta_G_12,
or measured gauge couplings.
```

## Verdict

The determinant accounting map is now closed.  The remaining physics gate is
not an ambiguous electroweak coefficient any more.  It is the selected
gauge-factor-resolved spectrum:

```text
{lambda_{a,j}, m_{a,j}, w_{a,j}} for a in {U1,SU2,SU3}.
```

Once this table is supplied by MTT selection, the remaining electroweak C1
response is an executable calculation.
