# MTT CONST EW 02 Weak Mixing B6 K_EW Kernel Gate v1

Status: `MTT_CONST_EW_02_B6_KEW_KERNEL_GATE_BUILT_PROJECTION_CLOSED_VALUES_OPEN`

Label: `CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL`

## Result

B6 builds the actual kernel gate.

Closed now:

- `K_EW` contract shape,
- Theta ratio high-scale tree value,
- exceptional/local trace-free projection basis,
- formula `Delta_alpha_12 = 2*c1 - c2`,
- internal `rho_UV` support,
- current-corpus no-knob negative gate.

The ratio edge remains

`r_12 = 0.56027`,

with high-scale tree value

`sin^2(theta_W)(mu_Theta) = 0.2515877565744274`.

## Boundary

The physical low-scale/effective weak angle is not derived.

Still needed:

- `x = g2(mu_Theta)^2`,
- `mu_Theta`,
- `T1,T2` or source-derived `c1,c2`,
- RG/matching scheme,
- optional effective-angle profile `kappa_l`,
- bridge from `rho_UV` to electroweak entries if that route is used.

Execution-I gives diagnostic coefficients

`c1 = 0.31`, `c2 = -0.27`,

with

`Delta_G_12 = 0.07082394967589342`.

These are not promoted as a no-knob prediction because the current certificates
do not derive them from selected topology, flux, curvature, torsion, or
determinant data.

## Superset Use

We combine three paths without collapsing them:

- Theta ratio path gives high-scale tree ratio data.
- Exceptional/local path gives the correct trace-free projection form.
- rho_UV path gives an internally closed response number but no electroweak map.

The locked target is now the kernel:

`K_EW -> (mu_Theta, x, T1, T2, scheme)`.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE`.
