# MTT Selected H-Sector Determinant/RG Operator Definition or Target-Independent Validation Run v1

Status: `MTT_SELECTED_HSECTORDETERMINANTRGOPERATORDEFINITION_OR_TARGETINDEPENDENTVALIDATIONRUN_OPERATOR_CONTRACT_DEFINED_VALUE_EXECUTION_OPEN`

## Theorem

The H-sector determinant/RG source operator is now defined as a same-source
zeta/logdet or determinant-torsion response on the selected `B_Huv/P_H` Higgs
domain.  This closes the operator contract, not the value.

## Operator

`L_H(mu)=P_H Herm(Hess(F_H(mu))) P_H`

`R_H^RG(mu0->mu1)=exp(-1/2*(logdet_zeta L_H(mu1)-logdet_zeta L_H(mu0)) + integral_gamma_H^sel + index_H^sel)`

## Slot Execution

- closed geometry/domain slots: `9/9`
- missing value/spectrum slots: `8/8`
- logdet kernel executable now: `false`
- target-independent validation run executed: `false`
- accepted `R_H^RG` source count: `0`

## Boundary

First-pass RG transport is classified as SM-parity replay/convention support
only.  It is not a selected no-knob `R_H^RG` source.

Next artifact: `MTT_Selected_HSectorLogDeterminantKernel_or_SelectedHResponseSpectrum_v1`
