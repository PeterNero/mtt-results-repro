# MTT Selected PSM C1 02 LocalPrincipleRouteAValidation or UnpatchedA1aActualSource v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-LOCAL`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Status: `MTT_SELECTED_PSM_C1_02_LOCAL_PRINCIPLE_ROUTE_A_VALIDATES_UNPATCHED_A1A_SOURCE_OPEN`

## Result

Under the accepted local `SelectedWeylVariationActionPrinciple`, Route A passes
the strict source validator. That gives a clean local proof-spine route.

This is not the unpatched theorem. The local principle is an explicit premise,
so the unpatched `SI-1u-A1a` physical action source remains open.

## Superset Use

We are using three constrained paths, not knobs:

- straight path: derive `SI-1u-A1a` from the physical action text;
- local path: validate Route A relative to the accepted local principle;
- fallback path: independent finite-C1/Galerkin execution.

All paths are locked to the same strict validator and use no observed constants
or target fitting.

## Next

Next artifact: `MTT_Selected_PSM_C1_02_UnpatchedA1aActualPhysicalSource_or_RouteBIndependentExecution_v1`
