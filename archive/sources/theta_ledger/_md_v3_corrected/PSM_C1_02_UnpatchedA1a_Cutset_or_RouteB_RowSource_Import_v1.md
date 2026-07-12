# PSM-C1-02 Unpatched A1a Cutset or Route-B Row Source Import v1

Status: `IMPORTED_A1A_CUTSET_ROUTEB_ROWSOURCE_LAST_FIELD_OPEN`

This artifact imports the sharper PSM-C1-02 cutset discovered after the Route-B
primitive-kernel frontier.

It supersedes the broad statement "prove all primitive kernel source fields" by
recording which fields already validate inside the PSM-C1-02 strict physical
source validator.

## Route A

Route A is reduced to the unpatched I10/I11 physical boundary and
first-variation source theorem.

Closed support:

- C1 response coordinate chart imported;
- finite `Phi_fin` trace operator imported;
- selected minimizer identifier imported;
- transport/dotD trace binding imported;
- normalization compatibility proved;
- canonical `R_Z/R_X/b_selected` replay values fixed;
- conditional I10/I11 witness passes.

Still open:

1. physical first-variation identity;
2. physical boundary cancellation/no extra physical source term;
3. same-source `R_Z/R_X/b_selected` emission.

The current unpatched I10 packet still fails because it lacks the seven binding
evidence entries required by the I10 binding validator.

## Route B

Route B is even sharper.  The extracted strict packet has:

- selected basis independent of residual projector;
- quadrature rule independent of locked target;
- all `72` primitive rows executed;
- formal `110` rows executed;
- exactness/error certificates attached.

The strict physical source validator rejects Route B on exactly one field:

`source_independent_of_residual_projector_replay`

So the Route-B target is now:

`SelectedRowSourceIndependenceFromResidualProjectorReplayTheorem`

This must prove that the selected row formulas, including all primitive rows
and the Hessian/source rows, are emitted before residual-projector replay and
do not use that replay as source.

## Decision

The next best path is Route B unless a direct physical I10/I11 action-binding
proof appears.  Route B has a smaller current missing object: row-source
independence from residual-projector replay.

Next artifact:

`MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1`
