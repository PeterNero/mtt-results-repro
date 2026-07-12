# Selected Omega Convention Theorem v1

## Result

The dimensionless convention factor is closed:

```text
chi_omega = 1.
```

This is not a new physical parameter. It fixes the symbol convention:

```text
Omega0 := Lambda_eff,phys
```

while the post-radius physical gap unit remains:

```text
omega_gap_phys = Omega0 / s_star
s_star = 1.46464677470183
```

The alternative convention,

```text
omega_gap_phys := Lambda_eff,phys
Omega0 = s_star * omega_gap_phys
```

is mathematically equivalent, but it makes `Omega0` a derived post-radius
symbol. The repository's Omega0 gate uses `Omega0` as the primitive source scale,
so the selected convention is `chi_omega=1`.

## Reduced Formula

Using the already closed facts:

```text
N = 448
epsilon_adm = 1/448
C_Q = 1
lambda_star = 15
```

the physical scale is reduced to:

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
Omega0/sqrt(alpha_phys) = 1.56750938592616
```

and:

```text
omega_gap_phys/sqrt(alpha_phys) = 1.0702303196928
Lambda_gap_phys/sqrt(alpha_phys) = 4.14498420477644
```

## Still Open

Only the actual physical action/unit anchor remains:

```text
alpha_phys
```

No observed Newton, Planck, cosmological, mass, or TeV value is used.
