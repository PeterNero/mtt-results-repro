# MTT Selected StrictPhysicalPrefactorSource or FullSMMinimalParameterAudit v1

## Theorem

`StrictPhysicalPrefactorSourceOrFullSMMinimalParameterAuditTheorem` is emitted.

## Strict Source Recheck

Accepted strict `P_EW`/direct-H rows:

```text
AEW source-operator rows = 0
AEW physical-prefactor rows = 0
AEW threshold-convention rows = 0
physical-anchor prefactor rows = 0
direct K_threshold.Omega_H.lambda rows = 0
same-branch source recheck rows = 0
total accepted strict rows = 0
```

Therefore `P_EW` is not promoted as strict selected source data in this
artifact.

## Minimal-Parameter Policy

The H/lambda lane is closed at the one-shared-physical-primitive standard:

```text
H-specific free parameters = 0
shared physical primitives = 1
P_EW.action_prefactor = 0.0685013467625
lambda_H used as selector = false
```

Replay:

```text
lambda_H = P_EW.action_prefactor * s_beta * R_H^RG
lambda_H = 0.1260399999999988
reference = 0.12604
absolute residual = -1.2212453270876722e-15
relative residual = 9.689347247601333e-15
```

## Interpretation

This closes the policy fork opened by the H/lambda empirical audit:

```text
strict no-knob P_EW source = open
minimal one-primitive H/lambda lane = closed
full-SM minimal-parameter ledger = seeded, not closed
```

The next non-looping object is `MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1`.
