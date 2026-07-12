# Same Source Selected U1 Carrier Projector Theorem v1

## Result

The source-level U1/qutrit carrier support is now imported as selected at the
S3 gerbe source level, and SU2 is closed for scoped weak-split accounting.
The final U1 promotion still does not close because no source emits the actual
quotient projector `P_perp` or the operator trace policy using it.

```text
source_level_rank3_carrier_support_closed = true
rank_quotient_arithmetic_closed = true
su2_weak_split_closed = true
u1_projector_P_perp_emitted = false
u1_operator_trace_policy_emitted = false
promoted_to_selected_threshold_index = false
```

## Tests

- `selected_s3_qutrit_source_level_carrier`: closed=true
  The projective qutrit/S3 carrier is selected at the gerbe source level with block-sector projector retention.
- `rank_three_shape_available`: closed=true
  The executable factorized carrier has rank 3 and would support the 2/3 quotient arithmetic.
- `operator_level_spectral_projector`: closed=false
  The SM-parity repo now distinguishes block projectors from coherent spectral projectors; the certificate closes the distinction but still does not emit the U1 quotient projector P_perp.
- `u1_specific_shared_circle_projector_P_perp`: closed=false
  No imported source supplies the explicit normalized U1 basis vector s and P_perp=I-|s><s|/<s,s> as the threshold trace projector.
- `operator_trace_uses_P_perp`: closed=false
  No imported source states that the U1 threshold determinant trace, in the same scheme as Qa/SU3 and SU2, uses the quotient projector P_perp.

## Minimal Projector Packet

```text
basis = orthonormal rank-3 U1/qutrit carrier basis in the selected S3 gerbe source
shared_vector = explicit selected shared central-circle unit vector s in that basis
projector = P_perp = I - |s><s|/<s,s>
```

Required checks:

- rank(P_perp)=2
- Tr(P_perp)/Tr(I)=2/3
- P_perp commutes with the selected U1 threshold operator or is the stated physical quotient before determinant evaluation
- same threshold scheme as Qa/SU3 log(2008) and selected SU2 weak-split accounting

## Next Required Object

```text
Selected_U1_Quotient_Projector_Pperp_and_Trace_Policy_v1
```
