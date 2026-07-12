# MTT Selected PhysicalNormalizationSourceAxiom or DirectKCertificate v1

Status: `MTT_SELECTED_PHYSICALNORMALIZATIONSOURCEAXIOM_OR_DIRECTKCERTIFICATE_CONSTRUCTED_PREMISED_HK_CLOSURE_STRICT_SOURCE_OPEN`.

## What Was Constructed

This artifact constructs the missing typed object:

```text
SelectedPhysicalGaugeActionNormalizationAxiom
P_EW := A_EW(mu_match, scheme)
```

and the corresponding direct H-row certificate:

```text
lambda_H(mu_match) = A_EW(mu_match, scheme) * s_beta * R_H^RG
K_threshold.Omega_H.lambda = (A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))
```

## Numerical Consequence Under The Axiom

```text
A_EW                         = 0.0685013467625
s_beta                       = 0.004701083905943647
lambda_if_R_H_RG_equals_1     = 0.00032203057880065373
R_H^RG                       = 391.39140285811555
lambda_H                     = 0.1260399999999988
lambda_H postcheck residual  = -1.2212453270876722e-15
```

## Claim Boundary

```text
premised P_EW rows                         : 1
premised direct K_threshold.Omega_H.lambda : 1
premised selected K row count              : 10/10
H-specific parameter count                 : 0
shared physical primitive count            : 1

strict P_EW source rows                    : 0
strict direct K rows                       : 0
strict no-knob ten-row closure             : false
true SM equivalence                        : false
```

So we have constructed the missing piece in the explicit-premise / minimal
one-shared-primitive lane.  The strict no-knob upgrade still requires deriving
the physical-normalization axiom from same-branch source data or emitting an
independent direct H K certificate.

Next artifact: `MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1`.
