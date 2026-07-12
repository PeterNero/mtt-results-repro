# MTT Selected H Radial Value Source Numeric Search or Pi2HRGFrontier v1

## Theorem

`HRadialPi2ClueAndNumericSearchFrontierTheorem` is emitted.

## Pi2 Clue

The selected charged-profile operator has a strong normalization clue:

```text
base(D_211)             = 0.683917989586
27/(4*pi^2)             = 0.68391798958578
residual                = 2.2004620348070603e-13
Tr(D_211)               = 24.621047625096
243/pi^2                = 24.62104762508808
rank/Tr(D_211)          = 9.869604401086184
pi^2                    = 9.869604401089358
rank/Tr(D_211)-pi^2     = -3.1743496720082476e-12
```

This is real progress: the charged profile matrix is carrying a `pi^2`
normalization. It is not yet a radial H source theorem.

## Bounded Search

The bounded diagnostic search tested source-native expressions built from
`pi^2`, `pi^4`, `q=79`, `rank=243`, `dim=27`, `D_211` scalars, selected
determinant logs, `lambda_12`, and `Delta_G12`.

Accepted radial source expressions: `0`.

Best diagnostic candidate:

```text
(4/1)*frobD^-1*baseD^-1*log92160000^2 = 391.38853383764047
relative residual = 7.330310420582448e-06
```

Hand-checked near miss:

```text
-logdet(D_211) * pi^4 = 391.5301506687795
relative residual     = 0.00035449887158216383
```

These are not promoted because numeric proximity is not a selected source map.

## Current Frontier

The remaining legal exits are:

1. a selected radial transport theorem from the `D_211/pi^2` normalization to
   `r_H` or direct `N_H`;
2. a selected dynamic `Phi_fin/C1` consumer map that emits `UP-RET-OVERLAP.HRG`;
3. an independent non-Higgs prediction of `UP-RET-OVERLAP.HRG`;
4. a direct selected `K_threshold.Omega_H.lambda` row.

## Next Artifact

`MTT_Selected_HRadialTransportMap_or_DynamicPhiFinC1Consumer_v1`
