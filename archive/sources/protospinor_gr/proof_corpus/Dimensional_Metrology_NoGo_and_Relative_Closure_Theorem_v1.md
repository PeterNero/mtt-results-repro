# Dimensional Metrology No-Go and Relative Closure Theorem v1

## Calculated Solution

The selected branch now has a closed relative physical scale solution:

```text
tau_int = log(448)/15 = 0.406986215494332
sqrt(tau_int) = 0.637954712729934
1/sqrt(tau_int) = 1.56750938592616
```

The physical chain is:

```text
tau_phys = tau_int / alpha_phys
ell_coh = sqrt(tau_int / alpha_phys)
Lambda_eff = sqrt(alpha_phys / tau_int)
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
```

Equivalently:

```text
ell_coh * Lambda_eff = 1
Lambda_eff / sqrt(alpha_phys) = 1/sqrt(tau_int)
```

## One-Anchor Absolute Solution

If a physical coherent length `L0` is selected by an independent rod/clock
construction, then:

```text
alpha_phys = tau_int / L0^2
tau_phys = L0^2
ell_coh = L0
Lambda_eff = 1/L0
Omega0 = sqrt(tau_int)/L0
```

If instead a physical coherent energy `E0` is selected, then:

```text
alpha_phys = tau_int * E0^2
tau_phys = 1/E0^2
ell_coh = 1/E0
Lambda_eff = E0
Omega0 = sqrt(tau_int)*E0
```

These are the same solution written in different metrological coordinates.

## No-Go Boundary

There is no further arithmetic trick that turns this relative solution into an
absolute SI number. For any positive scale `s`:

```text
alpha_phys -> s^2 alpha_phys
Lambda_eff -> s Lambda_eff
ell_coh -> ell_coh/s
```

leaves the internal branch facts and all dimensionless ratios invariant.
Therefore an absolute SI prediction needs exactly one metrological primitive,
or an internally constructed physical rod/clock process.

## Status

```text
relative physical scale solution: CLOSED
absolute SI scale without metrology: NOT AVAILABLE
minimum absolute extension: one rod/clock/energy primitive
```
