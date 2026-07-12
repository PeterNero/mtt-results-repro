# Dimensionless Modal-Gap Operator Reduction v1

## Result

The selected modal-gap problem reduces to a concrete finite packet:

```text
A_int = sum_{n=1}^3 kappa_n Delta_Bn
B_adm = P chi(A) exp(-tau A) chi(A) P
lambda_A = min_n kappa_n lambda_n
```

on the incoherent/physical quotient sector.

The corpus also links the QG UV damping scale to the gap:

```text
Lambda_int^2 ~ tau0^-1 ~ lambda_star
```

Using the internal foundation bound:

```text
lambda_star = 0.25
sqrt(lambda_star) = 0.5
tau0 ~ 1/lambda_star = 4
```

These are internal-unit consequences only.

## Still Open

To close the selected dimensionless operator, we still need:

- selected `kappa_1,kappa_2,kappa_3`
- selected fiber spectra `lambda_n` on the `rho_UV` branch
- the quotient/projector/window packet `P, chi, tau`
- proof that the bound `0.25` is saturated rather than only a lower bound

To close physical Newton/Planck units, we still need a separate physical unit
theorem. The `5 TeV` Theta scale remains a calibration benchmark, not a
no-knob derived value.
