# MTT Selected FivePhysicalClauses or SeventyTwoPrimitiveKernelRows v1

Status: `MTT_SELECTED_FIVEPHYSICALCLAUSES_OR_SEVENTYTWOPRIMITIVEKERNELROWS_BUILT_EXECUTION_CHECKLIST_OPEN`.

This artifact converts the final dynamic-C1 ledger into execution slots.

Route A is the shorter straight route: emit five same-source physical clauses
for `Phi_fin^C1`, no extra physical boundary/source term, `R_Z`, `R_X`, and
`b_selected`.

Route B is the mechanical fallback: execute 72 selected primitive kernel rows,
one for each sector/response/matrix-coordinate slot, with independent
provenance and exactness or error certificates.

The superset strategy is constrained here: multiple encodings may provide
compatibility evidence, but the target remains locked and replay data may only
serve as an after-the-fact acceptance oracle.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
