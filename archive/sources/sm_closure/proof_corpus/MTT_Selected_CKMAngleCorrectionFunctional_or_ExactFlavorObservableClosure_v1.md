# MTT Selected CKMAngleCorrectionFunctional or ExactFlavorObservableClosure v1

Status: `MTT_SELECTED_CKMANGLECORRECTIONFUNCTIONAL_DYNAMICC1_DOMAIN_CLOSED_EXACT_ROWS_OPEN`.

## Theorem

`CKMAngleCorrectionFunctionalDynamicC1DomainTheorem` is proved.

The active Step10/VSD01 source stack supplies the selected dynamic C1 correction
domain:

```text
A^T A          = 12 I_2
A^T b          = (12, 12)
deltaTheta_C1  = (1, 1)
rank           = 2
primitive rows = 72
formal rows    = 110
||R_Z||_F^2    = 4.000000000000000
||R_X||_F^2    = 2.000000000000000
```

This retires the old dynamic C1 source-promotion/Galerkin replay loop for the
CKM correction target. The open object is narrower: selected sector-pair
projection/evaluator rows for `s12`, `s23`, and `s13`.

## Required Corrections

The leading map already computed:

```text
s12 = sqrt(|Y_d1|/|Y_d2|)
s23 = sqrt(|Y_u1|/|Y_u2|)
s13 = sqrt(|Y_u1|/|Y_u3|)
```

To match the measured replay packet, the multiplicative corrections would be:

```text
C12 = 1.003152605685118
C23 = 1.015245188735500
C13 = 1.051580374093531
```

These numbers are recorded only as the obligation/postcheck, not as selected
source values.

## Acceptance Decision

Accepted exact CKM correction rows: `0`.

Reason: the selected dynamic C1 payload provides a valid source domain, but the
current accepted packets do not emit the three sector-pair evaluator rows
`Pi_CKM^12`, `Pi_CKM^23`, and `Pi_CKM^13`. The diagnostic finite-source scan
is rejected as source evidence because near-hits have no row certificate.

Next artifact: `MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1`.
