# Primitive C1 to Right-Label Adapter Payload Contract v1

## Purpose

This contract defines the exact bridge needed to promote the sibling SM-parity
primitive C1 row pattern into the right-channel label source required by the
finite mass-action branch.

It is not a closure claim.  It is the next packet shape.

## Schema

```text
MTTPrimitiveC1ToRightLabelAdapter.v1
```

## Required Source Fields

The packet must emit:

```text
branch_id
source_packet_id
source_owner_verified
selected_emitted
observed_data_used_as_selector=false
target_fitting_used=false
primitive_rows_u_phase
primitive_rows_u_shift
primitive_rows_d_shift
right_projector_basis_u
right_projector_basis_d
projection_rule E_K(A)=sum_a P_a A P_a
finite_normalization_rule
trace_table
exactness_or_error_certificate
residual_replay_dependency=false
```

Routing correction:

```text
u/e live on the selected Z/clock/phase leg
d/nuD live on the selected X/shift/translation leg
```

Therefore the promotable down-sector row is `primitive_rows_d_shift`.  The
older `primitive_rows_d_phase` entry is legacy diagnostic support only unless a
same-source alias theorem proves it is identical to the selected `d_shift`
operator before residual replay.

## Required Trace Table

After Schur/Riesz projection into the selected weighted right-channel
eigenbasis:

```text
Tr(P_u1 S_u^spin) = -1
Tr(P_u2 S_u^spin) = +1
Tr(P_d1 S_d^dyad) = +1
Tr(P_d2 S_d^dyad) = 0
Tr(P_d1 S_d^nil)  = 0
Tr(P_d2 S_d^nil)  = +1
```

The third light/heavy complement trace must also be reported.  It may not be
silently discarded.

## Current Support-Level Adapter

The current imported primitive rows reconstruct nontrivial matrices with:

```text
u phase/shift spectrum = (-0.366025, +1.000000, +1.366025)
d phase/shift spectrum = (+0.000000, +0.500000, +0.500000)
```

Their projected first-two-channel traces can be affinely normalized into the
required label rows:

```text
up spin:    scale=+3.31494423885, offset=-3.22145332947
down dyad:  scale=-7.38590275834, offset=+2.67139193562
down nil:   scale=+7.38590275834, offset=-1.67139193562
```

This is a strong structural match, but not proof, because the imported rows are
explicitly marked:

```text
selected_emitted=false
source_owner_verified=false
residual_replay_dependency=true
```

## Promotion Theorem

To close this path, prove:

```text
PrimitiveC1RightLabelSourcePromotionTheorem
```

Statement:

The selected MTT source functional on the q79 finite branch emits the same
primitive C1 row operators used by the adapter, with an intrinsic finite
normalization rule, before any residual-projector replay or mass-target
comparison is applied.

## Acceptance Test

The theorem must imply all of:

```text
source_owner_verified=true
selected_emitted=true
residual_replay_dependency=false
target_fitting_used=false
observed_data_used_as_selector=false
trace residuals < 1e-12
```

If those pass, the finite right-channel mass labels can be promoted from
candidate/schema to source-derived labels.

## Rejected Shortcuts

The following are not sufficient:

- residual-projector replay rows without independent source ownership;
- affine matching after looking at target masses;
- raw qutrit matrix spectra without right-projector trace verification;
- external HYM existence without finite row emission;
- measured CKM or Yukawa values used to choose the adapter.
