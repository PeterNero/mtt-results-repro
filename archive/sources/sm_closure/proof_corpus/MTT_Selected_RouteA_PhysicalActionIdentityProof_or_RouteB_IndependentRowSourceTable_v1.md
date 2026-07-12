# MTT Selected RouteA PhysicalActionIdentityProof or RouteB IndependentRowSourceTable v1

Status: `MTT_SELECTED_ROUTEA_ACTIONIDENTITY_OR_ROUTEB_ROWSOURCETABLE_BUILT_TABLE_PROVENANCE_OPEN`.

This artifact tries the concrete Route-B table path first. The current `110`-row table is complete as a postcheck object, but the provenance audit rejects it as an independent source table: the primitive and sector rows still carry replay/kernel placeholders, and the two Hessian rows still lack an independent `b_selected` export.

The emitted replacement schema is the next constructive target. Route A remains the parallel legal path through a same-source physical `Phi_fin^C1` action identity.

Next artifact: `MTT_Selected_IndependentC1RowKernelSourceIds_or_PhysicalPhiFinC1ActionProof_v1`.
