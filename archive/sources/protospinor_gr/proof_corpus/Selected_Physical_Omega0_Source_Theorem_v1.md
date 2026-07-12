# Selected Physical Omega0 Source Theorem v1

## Result

`Omega_0` is not physically closed, but the remaining source problem is now
precise.

Closed internal inputs:

```text
lambda_star_norm = 15
s_star = 1.46464677470183
internal alpha = 1 as normalized exact-branch convention
```

The legal damping-scale schema is:

```text
tau_adm = log(C_Q/epsilon_adm) / lambda_star
Lambda_eff = sqrt(lambda_star / log(C_Q/epsilon_adm))
Omega_0 = chi_omega * sqrt(alpha_phys) * sqrt(15 / log(C_Q/epsilon_adm))
omega_gap_phys = Omega_0 / s_star
Lambda_gap_phys = sqrt(15) * Omega_0 / s_star
```

`chi_omega` records the remaining convention:

```text
chi_omega = 1       if Omega_0 is identified directly with Lambda_eff
chi_omega = s_star  if omega_gap_phys is identified with Lambda_eff
```

## Internal Candidate Table

These are internal-only values under `C_Q=1`, `epsilon_adm=1/N`,
`alpha=1`, and `chi_omega` as shown. They are not physical predictions.

| N | Lambda_eff internal | R1 internal | Omega0 if direct | Omega0 if omega_gap=Lambda_eff |
|---:|---:|---:|---:|---:|
| 64 | 1.89914128021651 | 0.526553769546832 | 1.89914128021651 | 2.78157115077222 |
| 79 | 1.85281624239624 | 0.539718930090284 | 1.85281624239624 | 2.71372133354082 |
| 448 | 1.56750938592616 | 0.637954712729934 | 1.56750938592616 | 2.2958475664116 |

## What Remains

The open physical source objects are:

```text
alpha_phys or equivalent physical inverse-length/action unit
C_Q
epsilon_adm
chi_omega
selected finite-resolution branch N, if N is used
```

Theta `5 TeV`, observed Newton/Planck values, cosmological scales, and particle
masses are still forbidden as no-knob inputs.
