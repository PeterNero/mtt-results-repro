# MTT Selected H Radial Norm Law or Value-Source Derivation v1

## Result

The radial law is now derived, but the numeric radial value is not yet selected.

With `s_beta`, trace-free quotient, ordered `T3`, and the q79 lens-circle `+i` phase fixed, the Huv block is the selected Herm(2) ray

```text
H_tf(r) = r * [[sqrt(s_beta), i*sqrt(1-s_beta)],
             [-i*sqrt(1-s_beta), -sqrt(s_beta)]].
```

The radial scalar is therefore

```text
r_H = sqrt(Tr(H_tf^2)/2) = ||H_tf||_F/sqrt(2) = spectral_radius(H_tf).
```

This closes the meaning of `r_H`: it is the selected H radial action/Hessian norm. It does not yet close the value.

## Value-Source Audit

The three legal numeric routes were rechecked:

- typed HRG / strict `R_H^RG` value map: `0` accepted source rows
- direct H/lambda `K_threshold.Omega_H.lambda` row: absent; ten-row K closure remains `9/10`
- determinant/RG radial operator: domain contract defined, value not emitted

Best finite-invariant diagnostic near miss: `z448*sqrt2/phi` = `391.56635790614365` with relative error `0.0004470078973290815`. It is not promoted.

## Next Target

```text
MTT_Selected_HRadialActionNormValue_or_HLambdaThresholdRow_v1
```

