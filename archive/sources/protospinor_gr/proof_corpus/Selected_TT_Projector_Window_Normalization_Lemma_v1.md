# Selected TT Projector Window Normalization Lemma v1

## Result

The TT projector/window structure is now sourced.

The quantum-gravity source identifies the TT spectral operator as the projected
linearized graviton/Lichnerowicz operator on TT modes and supplies the SPT
factorization:

```text
B = exp(-tau0 E/2) B0 exp(-tau0 A_int/2)
```

with `tau0 > 0`, and the propagator bound:

```text
||Delta_prop(k)|| <= C0 exp(-tau0 k^2)/(k^2 + lambda_star)
```

So the previous `eta_TT` scalar is no longer an abstract normalization label. It
is the selected TT Q-sector spectral gap `lambda_star` for the projected TT
operator.

## Boundary

The source does not compute the numerical value of that gap. It treats
`lambda_star`, `tau0`, `C0`, and the projector constants as geometric/projector
data.

Therefore the remaining gate is not a convention choice. It is:

```text
Selected_TT_QSector_Spectral_Gap_Computation
```

This must compute the spectrum of the projected TT operator on the selected
Q-sector, or prove a same-branch identification with an internal `A_int`
complement whose spectrum is already known.
