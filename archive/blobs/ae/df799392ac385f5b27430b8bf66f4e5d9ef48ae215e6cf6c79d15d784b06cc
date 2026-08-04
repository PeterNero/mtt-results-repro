# Primitive C1 Right-Label Source Promotion Theorem Attempt v1

## Target Theorem

```text
PrimitiveC1RightLabelSourcePromotionTheorem
```

Target statement:

The selected MTT source functional on the q79 finite branch emits the primitive
C1 row operators used by the right-channel adapter, with intrinsic finite
normalization, before any residual-projector replay or mass-target comparison.

## Result

The theorem is not closed unconditionally from the currently available packets.
The strongest correct result is a conditional promotion theorem plus a precise
source cutset.

## What Is Closed

The following pieces are now closed enough to use:

```text
selected q79 branch                         closed
right-channel weighted projectors           closed once B_q branch is fixed
Schur/Riesz projection rule                  proved
finite trace/Frobenius pairing               source-supported
first primitive row formula                  source-specified
u/d primitive row adapter shape              diagnostic and exact to < 1e-12
source-level Weyl carrier                    closed in Route C support
conditional Weyl-pair A span                 exact
```

The adapter check proves:

```text
u row operator -> spin label by affine contrast
d row operator -> dyad/nil labels by affine indicator maps
```

with residuals below numerical roundoff.

## What Is Still Not Closed

The imported primitive rows still carry:

```text
selected_emitted=false
source_owner_verified=false
residual_replay_dependency=true
```

The SM-parity row-source validator also rejects the best current fill because:

```text
selected_basis_feeds_72_primitive_rows       missing
no_residual_projector_replay_used_as_source  missing
row_formula_source_theorem_derived           missing
source_independent_of_residual_projector     false
```

Thus the current data cannot honestly assert:

```text
source_owner_verified=true
selected_emitted=true
residual_replay_dependency=false
```

## Conditional Promotion Theorem

```text
ConditionalPrimitiveC1RightLabelPromotionTheorem
```

Assume a packet `P` satisfying `MTTPrimitiveC1ToRightLabelAdapter.v1` on the
selected q79 branch, with:

```text
source_owner_verified=true
selected_emitted=true
residual_replay_dependency=false
target_fitting_used=false
observed_data_used_as_selector=false
primitive_rows_u_phase, primitive_rows_d_phase emitted pre-residual
finite_normalization_rule emitted from the same source
```

Then the finite right-channel label rows are selected by MTT geometry:

```text
S_u^spin = affine_contrast(E_K(A_u))
S_d^dyad = affine_indicator_1(E_K(A_d))
S_d^nil  = affine_indicator_2(E_K(A_d))
```

where:

```text
E_K(A)=sum_a P_a A P_a
```

and the trace table is:

```text
Tr(P_u1 S_u^spin) = -1
Tr(P_u2 S_u^spin) = +1
Tr(P_d1 S_d^dyad) = +1
Tr(P_d2 S_d^dyad) = 0
Tr(P_d1 S_d^nil)  = 0
Tr(P_d2 S_d^nil)  = +1
```

Consequently the finite right-channel mass-label schema can be promoted from
candidate to source-derived label data.

## Proof

Because the selected right Gram spectra are simple, each right-channel
projector `P_a` is uniquely determined by the selected B_q branch.  For any
selected raw row operator `A`, the Schur/Riesz conditional expectation

```text
E_K(A)=sum_a P_a A P_a
```

is the unique trace-preserving projection of `A` into the commutant of the
right Gram operator.  Therefore `E_K(A)` is diagonal in the selected
right-channel eigenbasis and has projector traces

```text
t_a = Tr(P_a A).
```

For the up sector, the emitted primitive row has distinct first-two traces.
The unique affine contrast mapping these two traces to `(-1,+1)` is intrinsic
once the source packet supplies the row operator and the ordered selected
right-channel projectors.  Applying this contrast to `E_K(A_u)` gives
`S_u^spin`.

For the down sector, the emitted primitive row has distinct first-two traces.
The two unique affine indicator maps sending these traces to `(1,0)` and
`(0,1)` give `S_d^dyad` and `S_d^nil`.  These are finite functional-calculus
operators of the selected projected row and therefore introduce no entry-wise
flavor knobs.

The construction uses only the selected source packet, the selected right
projectors, and finite trace normalization.  It does not use observed masses,
CKM entries, or target fitting.  Thus the acceptance fields of the payload
promote the labels exactly.

## Current Cutset

The remaining theorem to prove is not a numerical adapter theorem.  It is the
source theorem:

```text
SelectedPrimitiveKernelSourceTheorem
```

or equivalently one of the Route C exits:

```text
SelectedMatterSlotChargeAndOverlapNormalizationTheorem
SelectedOverlapTransferFunctorTheorem
full selected Galerkin source replay
```

Once one of those emits the u/d primitive row operators with independent
source provenance, the right-label promotion theorem follows immediately by
the conditional proof above.

## Status

```text
UNCONDITIONAL_PROMOTION_OPEN
CONDITIONAL_PROMOTION_PROVED
SOURCE_CUTSET_EXACT
```
