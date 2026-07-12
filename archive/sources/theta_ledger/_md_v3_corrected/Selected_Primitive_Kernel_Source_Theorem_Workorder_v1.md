# Selected Primitive Kernel Source Theorem Workorder v1

## Objective

Fill `MTTSelectedPrimitiveKernelSourcePayload.v1` without residual replay.

This is the smallest object that turns the current conditional right-label
promotion into an unconditional source theorem.

## Input Files

```text
selected_primitive_kernel_source_payload.template.json
selected_primitive_kernel_source_payload.current_attempt.json
selected_primitive_kernel_source_payload_check.py
Primitive_C1_Right_Label_Source_Promotion_Theorem_Attempt_v1.md
```

## Current Rejection

The current attempt is numerically good but rejected for 14 source-owner
reasons:

```text
selected_emitted must be true
source_owner_verified must be true
source_independent_of_residual_projector_replay must be true
row_formula_source_theorem_derived must be true
selected_basis_feeds_required_primitive_rows must be true
finite_normalization_rule_emitted must be true
residual_replay_dependency must be false
exactness_or_error_certificate must be supplied
u_phase.pre_residual must be true
u_phase.independent_source_emitted must be true
u_phase.residual_replay_dependency must be false
d_phase.pre_residual must be true
d_phase.independent_source_emitted must be true
d_phase.residual_replay_dependency must be false
```

These are proof obligations, not numerical tuning knobs.

## Legal Closure Routes

### Route A: SelectedPrimitiveKernelSourceTheorem

Prove that the finite C1 source functional emits the required row kernels:

```text
K_u_phase
K_d_phase
```

before residual projection.  The proof must identify the selected basis,
finite trace pairing, source functional, and exactness certificate.

### Route B: Route C Matter-Slot/Overlap Normalization

Prove:

```text
SelectedMatterSlotChargeAndOverlapNormalizationTheorem
```

or:

```text
SelectedOverlapTransferFunctorTheorem
```

This must independently emit:

```text
Z-like phase carrier -> u/e
X-like shift carrier -> d/nuD
normalization from selected trace/inner-product/Hessian kernel
```

and then restrict to the `u_phase` and `d_phase` right-label rows.

### Route C: Full Selected Galerkin Source Replay

Run or import a selected Galerkin/HYM source computation that emits the row
values with:

```text
independent_source_emitted=true
residual_replay_dependency=false
exactness_or_error_certificate supplied
```

The residual-projector rows may only be used as a postcheck.

## Acceptance Command

When a filled payload exists, validate it with:

```text
python _md_v3_corrected/selected_primitive_kernel_source_payload_check.py path/to/filled_payload.json
```

The current attempt intentionally reports:

```text
strict source validation  EXPECTED-REJECT
```

The target filled payload must report:

```text
strict source validation  PASS
current source status     CLOSED
```

## Immediate Next Work

The most promising route is Route B, because the sibling repo already has:

```text
source-level Weyl carrier closed
active shift (1,1) provenance closed
conditional Weyl-pair transfer exact
```

but still lacks:

```text
selected sector routing independent of the locked target
selected transfer normalization
selected b_selected
promotion of conditional A to A_selected
```

So the next theorem to attack is:

```text
SelectedMatterSlotChargeAndOverlapNormalizationTheorem
```

with the explicit goal of filling `selected_primitive_kernel_source_payload.template.json`.
