# MTT Selected H Radial Source Value or Direct NH Execution v1

## Theorem

`HRadialSourceValueOrDirectNHExecutionTheorem` is emitted.

## Strict Result

- Strict `N_H=Hess(F_H)[U_H,U_H]` emitted: `false`.
- Strict source-owned `r_H` emitted: `false`.
- Strict `R_H^RG` source constructed: `false`.
- Direct `K_threshold.Omega_H.lambda` emitted: `false`.
- Strict selected `K_threshold` rows remain
  `9/10`.

## Controlled Minimal-Parameter Result

The one-parameter lane is now explicit and executable:

- primitive: `UP-RET-OVERLAP.HRG`;
- role: global H-threshold/RG transport strength;
- calibrated value: `391.39140285811936`;
- controlled `N_H=r_H^2`: `153187.23023124668`;
- conditional H K layer row count: `10/10`.

This closes a controlled/minimal H layer only. It calibrates `lambda_H`; it does not predict `lambda_H`, and it is not strict no-knob closure.

## Next Artifact

`MTT_Selected_StrictFiniteHActionSource_or_UPRetOverlapHRGCrossUse_v1`
