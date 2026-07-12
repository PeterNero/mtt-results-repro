# Finite C1 Source-Identity Theorem Proof or Explicit Source-Principle Patch

Status: `CONSTRUCTED_THEOREM_FORK_PATCH_READY_UNPATCHED_PROOF_OPEN`

This artifact constructs the next fork after the Dynamic C1 wall-break import.
It is intentionally a fork, not a closure claim.

## The Target Theorem

`SelectedFiniteC1SourceIdentityTheorem`

For the selected q79/F,m=1 branch, the finite C1 trace/quadrature row system
used to emit the 110 dynamic C1 rows must be source-identical to the physical
differentiated `PhiFin^C1` action variation.  In particular:

- the primitive 72 rows,
- the sector response rows,
- the Hessian/source rows,
- `b_selected`,
- and the residual columns `R_Z`, `R_X`

must be emitted by the same selected physical source, not by residual replay,
postcheck reconstruction, observed data, or benchmark fitting.

## What Is Already Available

- Formal 110-row execution is complete.
- Formal `A`, `b`, `deltaTheta`, and sector matrices are emitted.
- Primitive 72 postcheck values are loaded.
- Finite trace measure assembly is closed as a formal subclause.
- Cross-repo and corpus support converge on the same source-identity principle.
- The strict validator passes under the explicit local source-identity
  principle.
- Patched dynamic C1 and declared SM-parity replay close under that principle.

## Why This Is Not An Unpatched Proof Yet

The existing derivation attempts still fail at source ownership:

- finite trace assembly is support, not source promotion;
- exact row values are postcheck support, not source promotion;
- independent row-kernel source IDs are support-only;
- independent quadrature/Hessian source derivation reduces back to source
  identity;
- same-source `PhiFin^C1` emission still lacks physical action identity,
  boundary cancellation, independent `b_selected`, and non-replay row
  provenance.

Therefore the unpatched theorem remains open.

## Legal Route A: Unpatched Proof

To close the theorem without a patch, prove all of:

1. Physical action identity:
   the selected physical `PhiFin^C1` variation equals the finite trace C1
   action on the selected basis/quadrature.
2. Boundary/source cancellation:
   no extra physical boundary term or hidden source term survives the
   differentiated variation.
3. Row provenance:
   the primitive, sector, and Hessian rows are emitted from the physical action
   source, not from residual-projector replay.
4. Same-source `b_selected`:
   the source vector is emitted by the same branch and normalization as the
   row system.
5. Validator replay:
   the strict 110-row source validator passes without local axiom flags.

If these hold, the patched wall-break becomes an unpatched theorem.

## Legal Route B: Explicit Source-Principle Patch

If Route A cannot be derived from existing MTT action text, insert the local
principle explicitly:

`SelectedFiniteC1SourceIdentityPrinciple`

The selected finite C1 trace/quadrature action is the physical differentiated
`PhiFin^C1` action source for the selected q79/F,m=1 branch, with no extra
boundary/source term, and its primitive, sector, Hessian, and `b_selected`
rows are source-owned by that action.

Under this principle:

- strict 110-row source validation passes,
- exact dynamic C1 values promote inside the patched spine,
- declared SM-parity replay closes,
- true SM equivalence and full no-knob closure remain separate frontiers.

## Current Decision

This construction does not choose Route B as a proof.  It records Route B as a
paper-ready premise and keeps Route A as the unpatched theorem target.

Next artifact:

`MTT_Selected_PhysicalActionIdentity_or_IndependentC1RowSourceExport_v1`
