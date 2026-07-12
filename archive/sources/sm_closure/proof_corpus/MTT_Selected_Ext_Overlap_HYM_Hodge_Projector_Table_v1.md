# MTT Selected Ext Overlap HYM Hodge Projector Table v1

## Result

For the unit selected Ext row

```text
eta_00^unit = 32^(1/4) * Theta_{2,0}(z1;i) tensor Eta_{-4,0}(z2;i) dbar_z2
```

this artifact emits the row-level transition, harmonic, Hodge/Lambda, and gauge
projector data.

## Transition Table

For `L^2=(2,-4,0)` in generator order `g1,...,g6`:

```text
g1 -> 1
g2 -> exp(2*pi - 4*pi*i*z1)
g3 -> 1
g4 -> exp(-4*pi + 8*pi*i*z2)
g5 -> 1
g6 -> 1
```

The shared circle remains trivial.

## Hodge And Projector Data

In the equal-radius unitary coframe, the `dbar_z2` factor has unit local norm,
the theta metric supplies the line-bundle norm, and the unit-rescaled row has
`L2` norm one.  The row projector is:

```text
P_eta_00(v)=<eta_00^unit,v> eta_00^unit.
```

The row is harmonic in the canonical product theta metric model:

```text
barpartial eta_00 = 0
barpartial^* eta_00 = 0
```

## Guardrail

This does not solve the nonlinear HYM connection.  It supplies the normalized
harmonic Ext seed and the row-level projector needed by that solve.  The next
equation is:

```text
Lambda(F_{A_split + eta_00^unit + a_HYM})_0 = 0,
d_A^* a_HYM = 0.
```

## Next Artifact

`MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1`.
