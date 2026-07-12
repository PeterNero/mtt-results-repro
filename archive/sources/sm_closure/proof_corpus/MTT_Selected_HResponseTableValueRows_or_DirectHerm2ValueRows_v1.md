# MTT Selected HResponseTableValueRows or DirectHerm2ValueRows v1

Status: `MTT_SELECTED_HRESPONSETABLEVALUEROWS_OR_DIRECTHERM2VALUEROWS_EXECUTED_ZERO_ROWS_SOURCE_EMISSION_OPEN`

## Theorem

The active domain is no longer the blocker.  The selected `B_Huv/R_H/M_source`
typing and Herm(2) extractors are imported from the previous packet:

```text
M_source = (R_H^* H_response R_H + (R_H^* H_response R_H)^*)/2
H_uv = B_Huv^* M_source B_Huv
```

The remaining gate is the value-row source itself.

Current execution:

- required `H_response` table rows/certificates: `7`
- accepted `H_response` rows/certificates: `0`
- emitted `H_response` table rows: `0`
- required direct Herm(2) rows/certificates: `8`
- accepted direct Herm(2) rows/certificates: `0`
- emitted direct Herm(2) rows/certificates: `0`

The required direct row/certificate slots are:

```text
Hdd, Hdu_equals_conj_Hud_certificate, Hud_im, Hud_re, Huu, quotient_admissibility_certificate, same_source_exactness_or_error_certificate, source_ownership_certificate
```

Rejected as source shortcuts in this packet:

- diagonal HYM metric
- `A^T A = 12 I_2` compressed C1 normal matrix
- Herm(2) polar reconstruction law
- controlled HRG/lambda calibration
- static H logdet support
- selected `s_beta` projection bridge

Next artifact: `MTT_Selected_HResponseRowSourceEmission_or_DirectHerm2CertificatePayload_v1`
