# MTT Selected AEWCorrectionFactorSourceTheorem or PhysicalNormalizationRun v1

Status: `MTT_SELECTED_AEWCORRECTIONFACTOR_SOURCE_THEOREM_OR_PHYSICALNORMALIZATIONRUN_EXECUTED_SHARP_NEARMISS_STRICT_PEW_OPEN`.

## Result

The active strict PEW/H-lambda frontier is narrowed without moving backwards:

```text
strict charged K rows closed          : 9/10
finite H radial source R_H^RG closed  : true
minimal one-primitive H/lambda lane   : closed
strict P_EW source rows               : 0
direct K_threshold.Omega_H.lambda rows: 0
strict no-knob ten-row closure        : false
```

The best internal base clue remains:

```text
A_EW_base = 8*Delta_G12/pi^2 = 0.06849557446844383
A_EW_postcheck = 0.0685013467625
required correction = 1.0000842725110486
required epsilon = 8.427251104858868e-05
```

## Correction Search

The constrained source-window correction scan found:

```text
- 1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(103*p_Y^2): correction=1.000084272517845, eps-rel-resid=8.065e-08, accepted=false
- 1 + lambda_12/(2008*(Omega0/sqrt(alpha_phys))*pi^2): correction=1.000084272418448, eps-rel-resid=1.099e-06, accepted=false
- 1 + 1/(50*lambda_12*log(2008)^2*(Omega0/sqrt(alpha_phys))): correction=1.000084270272704, eps-rel-resid=2.656e-05, accepted=false
- 1 + s_beta*(Omega0/sqrt(alpha_phys))^2/(20*lambda_12^2): correction=1.000084269454826, eps-rel-resid=3.627e-05, accepted=false
- 1 + (Omega0/sqrt(alpha_phys))/(448*p_a*p_Y): correction=1.000084276000313, eps-rel-resid=4.140e-05, accepted=false
```

The sharpest new target is
`1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(103*p_Y^2)`, which gives
`A_EW=0.06850134676296551` with relative residual `6.7957279123184764e-12`.
It is not promoted because the denominator `103` and the correction functional
are not selected by a same-source gauge/action normalization theorem.

## Next Exact Object

`MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1`.
