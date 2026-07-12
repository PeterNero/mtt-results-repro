# Selected STF Hessian Form v1

## Result

The selected TT-sector Hessian form is closed up to one positive scale:

```text
H_TT = kappa_STF * I_2,    kappa_STF > 0
```

in the `(TT_plus, TT_cross)` basis.

## Why

The closure-strain tensor route already reduces the anchored physical tensor
sector to the two TT modes. A local rotation by `pi/4` in the transverse plane
acts on `(plus, cross)` as a spin-2 rotation by `pi/2`. Invariance of a
symmetric quadratic Hessian under that action forces equal diagonal entries and
zero off-diagonal mixing.

The positive anchored quadratic normal form then forces the common stiffness
`kappa_STF` to be positive.

## Boundary

This is not yet full GR closure. The actual selected numerical value of
`kappa_STF`, the absolute Newton/Planck normalization, and the stress-energy
response map remain open.
