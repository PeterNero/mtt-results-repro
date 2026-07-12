# Selected Primitive Kernel Source Payload Schema v1

## Purpose

This is the missing executable object for the right-label branch.

The conditional theorem already proves that right-channel labels promote once
the primitive C1 row operators are source-owned.  This schema defines the exact
payload that must be emitted to make that antecedent true.

## Schema

```text
MTTSelectedPrimitiveKernelSourcePayload.v1
```

## Minimal Scope

This is not the full 72-row SM-parity payload.  It is the smaller right-label
source payload needed for the finite mass-action theorem:

```text
u:phase primitive row operator
d:phase primitive row operator
selected right-channel projectors
finite source normalization
right-label trace table
source-owner certificate
```

The `u:shift` and `d:shift` rows may be included as consistency checks because
the current support-level rows have phase/shift degeneracy inside each sector,
but the minimal promotion only requires one source-owned up row and one
source-owned down row.

## Required Fields

```text
schema = MTTSelectedPrimitiveKernelSourcePayload.v1
branch_id = q79/F,m=1/S3_GS/selected finite B_q right branch
selected_emitted = true
source_owner_verified = true
residual_replay_dependency = false
observed_data_used_as_selector = false
target_fitting_used = false
source_independent_of_residual_projector_replay = true
row_formula_source_theorem_derived = true
selected_basis_feeds_required_primitive_rows = true
selected_trace_pairing_verified = true
finite_normalization_rule_emitted = true
exactness_or_error_certificate != null
```

## Required Rows

Each primitive row must include:

```text
row_id
sector
response
matrix_3x3
source_functional_id
basis_id
pairing_id
pre_residual = true
independent_source_emitted = true
residual_replay_dependency = false
exactness_or_error_certificate
```

## Required Label Output

The payload must emit:

```text
S_u^spin
S_d^dyad
S_d^nil
```

with trace residuals:

```text
max_abs_trace_residual < 1e-12
```

against:

```text
Tr(P_u1 S_u^spin) = -1
Tr(P_u2 S_u^spin) = +1
Tr(P_d1 S_d^dyad) = +1
Tr(P_d2 S_d^dyad) = 0
Tr(P_d1 S_d^nil)  = 0
Tr(P_d2 S_d^nil)  = +1
```

The third complement trace must be explicitly reported.

## Current Attempt Status

The current support-level adapter values are numerically adequate but fail this
schema because source ownership is not verified.

The current attempt is stored in:

```text
selected_primitive_kernel_source_payload.current_attempt.json
```

and is expected to be rejected until an actual source theorem or selected
Galerkin/Route C payload changes:

```text
selected_emitted
source_owner_verified
residual_replay_dependency
source_independent_of_residual_projector_replay
row_formula_source_theorem_derived
selected_basis_feeds_required_primitive_rows
```

## Closing Route

Any one of the following can fill this schema:

```text
SelectedPrimitiveKernelSourceTheorem
SelectedMatterSlotChargeAndOverlapNormalizationTheorem
SelectedOverlapTransferFunctorTheorem
full selected Galerkin source replay
```

Once this schema validates, `PrimitiveC1RightLabelSourcePromotionTheorem`
promotes from conditional to closed.
